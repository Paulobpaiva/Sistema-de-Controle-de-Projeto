from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator
from django.utils import timezone


class Worker(models.Model):
    LEVEL_CHOICES = [
        ('admin', 'Administrador'),
        ('manager', 'Gerente'),
        ('collaborator', 'Colaborador'),
    ]
    
    user = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name="Usuário")
    level = models.CharField(
        max_length=20, 
        choices=LEVEL_CHOICES, 
        default='collaborator',
        verbose_name="Nível"
    )
    department = models.CharField(max_length=100, verbose_name="Departamento")
    phone = models.CharField(max_length=20, blank=True, null=True, verbose_name="Telefone")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Data de Criação")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Última Atualização")
    
    class Meta:
        verbose_name = "Trabalhador"
        verbose_name_plural = "Trabalhadores"
        ordering = ['user__first_name', 'user__last_name']
    
    def __str__(self):
        return f"{self.user.get_full_name()} - {self.get_level_display()}"
    
    @property
    def full_name(self):
        return self.user.get_full_name()
    
    @property
    def email(self):
        return self.user.email


class Action(models.Model):
    name = models.CharField(max_length=200, verbose_name="Nome da Ação")
    description = models.TextField(blank=True, null=True, verbose_name="Descrição")
    owner = models.ForeignKey(
        Worker, 
        on_delete=models.PROTECT, 
        related_name='owned_actions',
        verbose_name="Responsável"
    )
    start_date = models.DateField(verbose_name="Data de Início")
    end_date = models.DateField(verbose_name="Data de Término")
    budget = models.DecimalField(
        max_digits=12, 
        decimal_places=2, 
        blank=True, 
        null=True,
        verbose_name="Orçamento"
    )
    status = models.CharField(
        max_length=20,
        choices=[
            ('planning', 'Planejamento'),
            ('in_progress', 'Em Andamento'),
            ('completed', 'Concluído'),
            ('cancelled', 'Cancelado'),
        ],
        default='planning',
        verbose_name="Status"
    )
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Data de Criação")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Última Atualização")
    
    class Meta:
        verbose_name = "Ação"
        verbose_name_plural = "Ações"
        ordering = ['-created_at']
    
    def __str__(self):
        return self.name
    
    @property
    def progress_percentage(self):
        """Calcula o progresso da ação baseado nas atividades"""
        activities = self.activities.all()
        if not activities:
            return 0
        
        completed = activities.filter(status='completed').count()
        total = activities.count()
        return round((completed / total) * 100, 1)
    
    @property
    def is_overdue(self):
        """Verifica se a ação está atrasada"""
        return self.end_date < timezone.now().date() and self.status != 'completed'


class Activity(models.Model):
    STATUS_CHOICES = [
        ('not_started', 'Não Iniciado'),
        ('in_progress', 'Em Andamento'),
        ('completed', 'Concluído'),
        ('paused', 'Pausado'),
    ]
    
    PRIORITY_CHOICES = [
        ('low', 'Baixa'),
        ('medium', 'Média'),
        ('high', 'Alta'),
        ('urgent', 'Urgente'),
    ]
    
    name = models.CharField(max_length=200, verbose_name="Nome da Atividade")
    description = models.TextField(blank=True, null=True, verbose_name="Descrição")
    action = models.ForeignKey(
        Action, 
        on_delete=models.CASCADE, 
        related_name='activities',
        verbose_name="Ação"
    )
    assigned_to = models.ForeignKey(
        Worker, 
        on_delete=models.PROTECT, 
        related_name='assigned_activities',
        verbose_name="Atribuído para"
    )
    status = models.CharField(
        max_length=20, 
        choices=STATUS_CHOICES, 
        default='not_started',
        verbose_name="Status"
    )
    priority = models.CharField(
        max_length=20,
        choices=PRIORITY_CHOICES,
        default='medium',
        verbose_name="Prioridade"
    )
    deadline = models.DateField(verbose_name="Prazo")
    estimated_hours = models.DecimalField(
        max_digits=6, 
        decimal_places=2, 
        blank=True, 
        null=True,
        verbose_name="Horas Estimadas"
    )
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Data de Criação")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Última Atualização")
    
    class Meta:
        verbose_name = "Atividade"
        verbose_name_plural = "Atividades"
        ordering = ['-created_at']
    
    def __str__(self):
        return f"{self.name} - {self.action.name}"
    
    @property
    def is_overdue(self):
        """Verifica se a atividade está atrasada"""
        return self.deadline < timezone.now().date() and self.status != 'completed'
    
    @property
    def total_time_spent(self):
        """Calcula o tempo total gasto na atividade"""
        time_entries = self.time_entries.all()
        total_minutes = sum(
            (entry.end_time - entry.start_time).total_seconds() / 60 
            for entry in time_entries 
            if entry.end_time
        )
        return round(total_minutes / 60, 2)  # Retorna em horas


class TimeEntry(models.Model):
    activity = models.ForeignKey(
        Activity, 
        on_delete=models.CASCADE, 
        related_name='time_entries',
        verbose_name="Atividade"
    )
    worker = models.ForeignKey(
        Worker, 
        on_delete=models.PROTECT,
        verbose_name="Trabalhador"
    )
    start_time = models.DateTimeField(verbose_name="Hora de Início")
    end_time = models.DateTimeField(
        blank=True, 
        null=True, 
        verbose_name="Hora de Término"
    )
    description = models.TextField(verbose_name="Descrição do Trabalho")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Data de Criação")
    
    class Meta:
        verbose_name = "Registro de Tempo"
        verbose_name_plural = "Registros de Tempo"
        ordering = ['-start_time']
    
    def __str__(self):
        return f"{self.activity.name} - {self.worker.full_name} - {self.start_time.date()}"
    
    @property
    def duration_hours(self):
        """Calcula a duração em horas"""
        if self.end_time:
            duration = self.end_time - self.start_time
            return round(duration.total_seconds() / 3600, 2)
        return 0


class Comment(models.Model):
    activity = models.ForeignKey(
        Activity, 
        on_delete=models.CASCADE, 
        related_name='comments',
        verbose_name="Atividade"
    )
    worker = models.ForeignKey(
        Worker, 
        on_delete=models.CASCADE,
        verbose_name="Trabalhador"
    )
    content = models.TextField(verbose_name="Comentário")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Data de Criação")
    
    class Meta:
        verbose_name = "Comentário"
        verbose_name_plural = "Comentários"
        ordering = ['-created_at']
    
    def __str__(self):
        return f"{self.worker.full_name} - {self.created_at.date()}"

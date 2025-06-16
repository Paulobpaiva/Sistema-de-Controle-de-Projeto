from django.contrib import admin
from django.utils.html import format_html
from django.urls import reverse
from django.utils.safestring import mark_safe
from .models import Worker, Action, Activity, TimeEntry, Comment


@admin.register(Worker)
class WorkerAdmin(admin.ModelAdmin):
    list_display = ['user', 'level', 'department', 'phone', 'created_at']
    list_filter = ['level', 'department', 'created_at']
    search_fields = ['user__first_name', 'user__last_name', 'user__email', 'department']
    readonly_fields = ['created_at', 'updated_at']
    
    fieldsets = (
        ('Informações do Usuário', {
            'fields': ('user', 'level', 'department')
        }),
        ('Contato', {
            'fields': ('phone',)
        }),
        ('Informações do Sistema', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )


@admin.register(Action)
class ActionAdmin(admin.ModelAdmin):
    list_display = ['name', 'owner', 'status', 'start_date', 'end_date', 'progress_bar', 'is_overdue_display']
    list_filter = ['status', 'start_date', 'end_date', 'owner__level']
    search_fields = ['name', 'description', 'owner__user__first_name', 'owner__user__last_name']
    readonly_fields = ['created_at', 'updated_at', 'progress_percentage']
    date_hierarchy = 'start_date'
    
    fieldsets = (
        ('Informações Básicas', {
            'fields': ('name', 'description', 'owner')
        }),
        ('Datas e Status', {
            'fields': ('start_date', 'end_date', 'status')
        }),
        ('Orçamento', {
            'fields': ('budget',)
        }),
        ('Informações do Sistema', {
            'fields': ('created_at', 'updated_at', 'progress_percentage'),
            'classes': ('collapse',)
        }),
    )
    
    def progress_bar(self, obj):
        progress = obj.progress_percentage
        color = 'success' if progress >= 80 else 'warning' if progress >= 50 else 'danger'
        return format_html(
            '<div class="progress" style="width: 100px; height: 20px;">'
            '<div class="progress-bar bg-{}" style="width: {}%">{}%</div>'
            '</div>',
            color, progress, progress
        )
    progress_bar.short_description = 'Progresso'
    
    def is_overdue_display(self, obj):
        if obj.is_overdue:
            return format_html('<span style="color: red;">⚠️ Atrasado</span>')
        return format_html('<span style="color: green;">✓ No Prazo</span>')
    is_overdue_display.short_description = 'Status do Prazo'


@admin.register(Activity)
class ActivityAdmin(admin.ModelAdmin):
    list_display = ['name', 'action', 'assigned_to', 'status', 'priority', 'deadline', 'is_overdue_display']
    list_filter = ['status', 'priority', 'deadline', 'action__status', 'assigned_to__level']
    search_fields = ['name', 'description', 'action__name', 'assigned_to__user__first_name']
    readonly_fields = ['created_at', 'updated_at', 'total_time_spent']
    date_hierarchy = 'deadline'
    
    fieldsets = (
        ('Informações Básicas', {
            'fields': ('name', 'description', 'action', 'assigned_to')
        }),
        ('Status e Prioridade', {
            'fields': ('status', 'priority', 'deadline')
        }),
        ('Estimativas', {
            'fields': ('estimated_hours',)
        }),
        ('Informações do Sistema', {
            'fields': ('created_at', 'updated_at', 'total_time_spent'),
            'classes': ('collapse',)
        }),
    )
    
    def is_overdue_display(self, obj):
        if obj.is_overdue:
            return format_html('<span style="color: red;">⚠️ Atrasado</span>')
        return format_html('<span style="color: green;">✓ No Prazo</span>')
    is_overdue_display.short_description = 'Status do Prazo'


@admin.register(TimeEntry)
class TimeEntryAdmin(admin.ModelAdmin):
    list_display = ['activity', 'worker', 'start_time', 'end_time', 'duration_hours', 'created_at']
    list_filter = ['start_time', 'worker__level', 'activity__status']
    search_fields = ['activity__name', 'worker__user__first_name', 'description']
    readonly_fields = ['created_at', 'duration_hours']
    date_hierarchy = 'start_time'
    
    fieldsets = (
        ('Informações do Registro', {
            'fields': ('activity', 'worker', 'description')
        }),
        ('Horários', {
            'fields': ('start_time', 'end_time')
        }),
        ('Informações do Sistema', {
            'fields': ('created_at', 'duration_hours'),
            'classes': ('collapse',)
        }),
    )


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['activity', 'worker', 'content_preview', 'created_at']
    list_filter = ['created_at', 'worker__level', 'activity__status']
    search_fields = ['content', 'activity__name', 'worker__user__first_name']
    readonly_fields = ['created_at']
    
    def content_preview(self, obj):
        return obj.content[:100] + '...' if len(obj.content) > 100 else obj.content
    content_preview.short_description = 'Conteúdo'

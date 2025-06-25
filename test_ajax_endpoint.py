#!/usr/bin/env python3
"""
Script de teste para verificar o endpoint AJAX de atualização de status
"""

import requests
import json
import sys
from urllib.parse import urljoin

def test_ajax_endpoint():
    """Testa o endpoint AJAX de atualização de status"""
    
    # Configurações
    base_url = "http://localhost:8000"
    login_url = urljoin(base_url, "/accounts/login/")
    activity_list_url = urljoin(base_url, "/activities/")
    
    # Criar sessão para manter cookies
    session = requests.Session()
    
    print("=== Teste do Endpoint AJAX ===")
    print(f"URL Base: {base_url}")
    
    try:
        # 1. Testar se o servidor está rodando
        print("\n1. Verificando se o servidor está rodando...")
        response = session.get(base_url)
        if response.status_code == 200:
            print("✅ Servidor está rodando")
        else:
            print(f"❌ Servidor retornou status {response.status_code}")
            return False
            
        # 2. Verificar se a página de login está acessível
        print("\n2. Verificando página de login...")
        response = session.get(login_url)
        if response.status_code == 200:
            print("✅ Página de login acessível")
        else:
            print(f"❌ Página de login retornou status {response.status_code}")
            return False
            
        # 3. Verificar se a página de atividades está acessível (deve redirecionar para login)
        print("\n3. Verificando redirecionamento para login...")
        response = session.get(activity_list_url)
        if response.status_code == 302:  # Redirecionamento
            print("✅ Redirecionamento para login funcionando")
        else:
            print(f"⚠️  Status inesperado: {response.status_code}")
            
        # 4. Verificar se o CSRF token está presente na página de login
        print("\n4. Verificando CSRF token na página de login...")
        response = session.get(login_url)
        if 'csrfmiddlewaretoken' in response.text:
            print("✅ CSRF token encontrado na página de login")
        else:
            print("❌ CSRF token não encontrado na página de login")
            
        # 5. Testar login (se credenciais estiverem disponíveis)
        print("\n5. Testando login...")
        # Obter CSRF token
        response = session.get(login_url)
        csrf_token = None
        
        # Extrair CSRF token da página
        import re
        csrf_match = re.search(r'name="csrfmiddlewaretoken" value="([^"]+)"', response.text)
        if csrf_match:
            csrf_token = csrf_match.group(1)
            print(f"✅ CSRF token extraído: {csrf_token[:10]}...")
        else:
            print("❌ Não foi possível extrair CSRF token")
            return False
            
        # Tentar login (você precisará fornecer credenciais válidas)
        login_data = {
            'username': 'admin',  # Substitua por um usuário válido
            'password': 'admin123',  # Substitua por uma senha válida
            'csrfmiddlewaretoken': csrf_token
        }
        
        response = session.post(login_url, data=login_data, headers={
            'Referer': login_url
        })
        
        if response.status_code == 302:  # Redirecionamento após login bem-sucedido
            print("✅ Login bem-sucedido")
            
            # 6. Testar acesso à página de atividades
            print("\n6. Testando acesso à página de atividades...")
            response = session.get(activity_list_url)
            if response.status_code == 200:
                print("✅ Página de atividades acessível após login")
                
                # 7. Verificar se há atividades na página
                if 'activity' in response.text.lower():
                    print("✅ Atividades encontradas na página")
                else:
                    print("⚠️  Nenhuma atividade encontrada na página")
                    
                # 8. Testar endpoint AJAX (se houver uma atividade)
                print("\n8. Testando endpoint AJAX...")
                # Tentar encontrar um ID de atividade na página
                activity_id_match = re.search(r'updateStatus\([\'"]([0-9]+)[\'"]', response.text)
                if activity_id_match:
                    activity_id = activity_id_match.group(1)
                    print(f"✅ ID de atividade encontrado: {activity_id}")
                    
                    # Testar endpoint AJAX
                    ajax_url = urljoin(base_url, f"/activities/{activity_id}/update-status/")
                    ajax_data = {
                        'status': 'in_progress',
                        'csrfmiddlewaretoken': csrf_token
                    }
                    
                    response = session.post(ajax_url, data=ajax_data, headers={
                        'X-CSRFToken': csrf_token,
                        'X-Requested-With': 'XMLHttpRequest',
                        'Referer': activity_list_url
                    })
                    
                    print(f"Status da resposta AJAX: {response.status_code}")
                    print(f"Headers da resposta: {dict(response.headers)}")
                    
                    try:
                        json_response = response.json()
                        print(f"Resposta JSON: {json_response}")
                        if json_response.get('success'):
                            print("✅ Endpoint AJAX funcionando corretamente")
                        else:
                            print(f"⚠️  Endpoint AJAX retornou erro: {json_response.get('message')}")
                    except json.JSONDecodeError:
                        print(f"❌ Resposta não é JSON válido: {response.text[:200]}")
                else:
                    print("⚠️  Nenhum ID de atividade encontrado para teste")
            else:
                print(f"❌ Página de atividades retornou status {response.status_code}")
        else:
            print("❌ Login falhou - verifique as credenciais")
            print(f"Status: {response.status_code}")
            print(f"Resposta: {response.text[:200]}")
            
    except requests.exceptions.ConnectionError:
        print("❌ Erro de conexão - verifique se o servidor está rodando")
        return False
    except Exception as e:
        print(f"❌ Erro inesperado: {e}")
        return False
        
    print("\n=== Teste Concluído ===")
    return True

if __name__ == "__main__":
    print("Iniciando teste do endpoint AJAX...")
    print("Certifique-se de que o servidor Django está rodando em http://localhost:8000")
    print("Você pode precisar ajustar as credenciais de login no script\n")
    
    success = test_ajax_endpoint()
    
    if success:
        print("\n✅ Todos os testes passaram!")
    else:
        print("\n❌ Alguns testes falharam. Verifique os logs acima.")
        sys.exit(1) 
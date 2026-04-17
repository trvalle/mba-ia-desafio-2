"""
Script para fazer push de prompts otimizados ao LangSmith Prompt Hub.

Este script:
1. Lê os prompts otimizados de prompts/bug_to_user_story_v2.yml
2. Valida os prompts
3. Faz push PÚBLICO para o LangSmith Hub
4. Adiciona metadados (tags, descrição, técnicas utilizadas)

SIMPLIFICADO: Código mais limpo e direto ao ponto.
"""

import os
import sys
from dotenv import load_dotenv
from langsmith import Client
from langchain_core.prompts import ChatPromptTemplate
from utils import load_yaml, check_env_vars, print_section_header

load_dotenv()


def push_prompt_to_langsmith(prompt_name: str, prompt_data: dict) -> bool:
    """
    Faz push do prompt otimizado para o LangSmith Hub (PÚBLICO).

    Args:
        prompt_name: Nome do prompt
        prompt_data: Dados do prompt

    Returns:
        True se sucesso, False caso contrário
    """
    try:
        # Constrói o ChatPromptTemplate a partir do YAML
        messages = []
        
        for msg in prompt_data.get('messages', []):
            msg_type = msg.get('type', 'human')
            content = msg.get('content', '')
            
            if msg_type == 'system':
                messages.append(('system', content))
            elif msg_type == 'human':
                messages.append(('human', content))
            elif msg_type == 'ai':
                messages.append(('ai', content))
        
        if not messages:
            print("❌ Nenhuma mensagem encontrada no prompt")
            return False
        
        # Cria o ChatPromptTemplate
        prompt_template = ChatPromptTemplate.from_messages(messages)
        
        # Cria cliente do LangSmith
        client = Client()
        
        # Faz push para o Hub
        print(f"📤 Fazendo push do prompt: {prompt_name}")
        client.push_prompt(
            prompt_name,
            object=prompt_template
        )
        
        print(f"✅ Prompt '{prompt_name}' publicado com sucesso!")
        print(f"🔗 Visualize em: https://smith.langchain.com/hub/{prompt_name}")
        
        return True
        
    except Exception as e:
        print(f"❌ Erro ao fazer push do prompt: {e}")
        print("\nPossíveis causas:")
        print("  - LANGSMITH_API_KEY inválida")
        print("  - Formato do prompt incorreto")
        print("  - Problemas de conexão")
        return False


def validate_prompt(prompt_data: dict) -> tuple[bool, list]:
    """
    Valida estrutura básica de um prompt (versão simplificada).

    Args:
        prompt_data: Dados do prompt

    Returns:
        (is_valid, errors) - Tupla com status e lista de erros
    """
    errors = []
    
    # Verifica se tem mensagens
    if 'messages' not in prompt_data:
        errors.append("Campo 'messages' não encontrado")
    elif not prompt_data['messages']:
        errors.append("Lista de mensagens está vazia")
    
    # Verifica cada mensagem
    messages = prompt_data.get('messages', [])
    for i, msg in enumerate(messages):
        if 'type' not in msg:
            errors.append(f"Mensagem {i}: campo 'type' não encontrado")
        if 'content' not in msg:
            errors.append(f"Mensagem {i}: campo 'content' não encontrado")
        elif not msg['content'].strip():
            errors.append(f"Mensagem {i}: conteúdo vazio")
    
    # Verifica se tem pelo menos uma mensagem system ou human
    has_system_or_human = any(msg.get('type') in ['system', 'human'] for msg in messages)
    if not has_system_or_human:
        errors.append("Prompt deve ter pelo menos uma mensagem 'system' ou 'human'")
    
    return (len(errors) == 0, errors)


def main():
    """Função principal"""
    print_section_header("Push de Prompts para o LangSmith")
    
    # Verifica variáveis de ambiente
    if not check_env_vars(['LANGSMITH_API_KEY', 'LANGSMITH_USERNAME']):
        return 1
    
    # Carrega o prompt otimizado (v2)
    prompt_file = "prompts/bug_to_user_story_v2.yml"
    print(f"📂 Carregando prompt: {prompt_file}")
    
    prompt_data = load_yaml(prompt_file)
    if not prompt_data:
        print(f"❌ Erro ao carregar {prompt_file}")
        return 1
    
    print("✅ Prompt carregado com sucesso")
    
    # Valida o prompt
    print("🔍 Validando estrutura do prompt...")
    is_valid, errors = validate_prompt(prompt_data)
    
    if not is_valid:
        print("❌ Prompt inválido. Erros encontrados:")
        for error in errors:
            print(f"   - {error}")
        return 1
    
    print("✅ Prompt válido")
    
    # Faz push para o LangSmith
    username = os.getenv('LANGSMITH_USERNAME')
    prompt_name = f"{username}/bug_to_user_story_v2"
    
    success = push_prompt_to_langsmith(prompt_name, prompt_data)
    
    if success:
        print()
        print("=" * 60)
        print("✅ Push concluído com sucesso!")
        print("=" * 60)
        print()
        print("📁 Próximos passos:")
        print("   1. Verifique o prompt no dashboard do LangSmith")
        print("   2. Execute a avaliação: python src/evaluate.py")
        print("   3. Analise as métricas e itere se necessário")
        print()
        return 0
    else:
        return 1


if __name__ == "__main__":
    sys.exit(main())

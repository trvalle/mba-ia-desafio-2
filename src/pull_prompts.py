"""
Script para fazer pull de prompts do LangSmith Prompt Hub.

Este script:
1. Conecta ao LangSmith usando credenciais do .env
2. Faz pull dos prompts do Hub
3. Salva localmente em prompts/bug_to_user_story_v1.yml

SIMPLIFICADO: Usa serialização nativa do LangChain para extrair prompts.
"""

import os
import sys
from pathlib import Path
from dotenv import load_dotenv
from langsmith import Client
from utils import save_yaml, check_env_vars, print_section_header

load_dotenv()


def pull_prompts_from_langsmith():
    """
    Faz pull do prompt baseline do LangSmith Prompt Hub.
    
    Returns:
        0 se sucesso, 1 se erro
    """
    try:
        # Verifica variáveis de ambiente necessárias
        check_env_vars(['LANGSMITH_API_KEY'])
        
        print_section_header("Pull de Prompts do LangSmith")
        
        # Nome do prompt no Hub
        prompt_name = "leonanluppi/bug_to_user_story_v1"
        
        # Cria cliente do LangSmith
        client = Client()
        
        # Faz pull do prompt
        print(f"🔄 Fazendo pull do prompt: {prompt_name}")
        prompt = client.pull_prompt(prompt_name)
        print(f"✅ Prompt '{prompt_name}' baixado com sucesso")
        
        # Define caminho de saída
        project_root = Path(__file__).parent.parent
        output_path = project_root / 'prompts' / 'bug_to_user_story_v1.yml'
        
        # Converte prompt para dict
        prompt_dict = {
            '_type': 'prompt',
            'input_variables': prompt.input_variables if hasattr(prompt, 'input_variables') else [],
        }
        
        # Extrai mensagens do prompt
        if hasattr(prompt, 'messages'):
            messages = []
            for msg in prompt.messages:
                message_dict = {
                    'type': msg.__class__.__name__.lower().replace('message', ''),
                }
                
                # Trata template de mensagem
                if hasattr(msg, 'prompt'):
                    if hasattr(msg.prompt, 'template'):
                        message_dict['content'] = msg.prompt.template
                elif hasattr(msg, 'content'):
                    message_dict['content'] = msg.content
                
                messages.append(message_dict)
            
            prompt_dict['messages'] = messages
        
        # Salva em YAML
        save_yaml(prompt_dict, output_path)
        print(f"✅ Prompt salvo em: {output_path}")
        
        print()
        print("="  * 60)
        print("✅ Pull concluído com sucesso!")
        print("=" * 60)
        print()
        print("📁 Próximos passos:")
        print("   1. Analise o prompt em: prompts/bug_to_user_story_v1.yml")
        print("   2. Crie uma versão otimizada: prompts/bug_to_user_story_v2.yml")
        print("   3. Use técnicas: Few-shot Learning + Chain of Thought")
        print("   4. Execute: python src/push_prompts.py")
        print()
        
        return 0
        
    except Exception as e:
        print(f"❌ Erro ao fazer pull do prompt: {e}")
        print("\nPossíveis causas:")
        print("  - LANGSMITH_API_KEY inválida ou não configurada")
        print("  - Prompt não encontrado no Hub")
        print("  - Problemas de conexão com a internet")
        return 1


def main():
    """Função principal"""
    return pull_prompts_from_langsmith()


if __name__ == "__main__":
    sys.exit(main())

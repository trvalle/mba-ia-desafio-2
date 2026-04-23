"""
Script para verificar se todas as configurações necessárias estão corretas
antes de executar a avaliação.

Execute este script antes de rodar src/evaluate.py para garantir que tudo está configurado.
"""

import os
import sys
from pathlib import Path
from dotenv import load_dotenv

# Carregar variáveis de ambiente
load_dotenv()

def print_header(text):
    print("\n" + "=" * 70)
    print(text)
    print("=" * 70 + "\n")

def print_check(passed, message):
    icon = "✅" if passed else "❌"
    print(f"{icon} {message}")
    return passed

def check_file_exists(filepath, description):
    exists = Path(filepath).exists()
    return print_check(exists, f"{description}: {filepath}")

def check_env_var(var_name, description):
    value = os.getenv(var_name, "")
    
    # Verificar se não é placeholder
    invalid_placeholders = [
        "your_", "sua_", "seu_", "here", "aqui", 
        "example", "exemplo", "placeholder"
    ]
    
    is_valid = bool(value) and not any(ph in value.lower() for ph in invalid_placeholders)
    
    if is_valid:
        # Mostra início e fim do valor (escondendo meio por segurança)
        if len(value) > 10:
            display_value = f"{value[:4]}...{value[-4:]}"
        else:
            display_value = value[:2] + "***"
        print_check(True, f"{description}: {display_value}")
    else:
        if not value:
            print_check(False, f"{description}: NÃO CONFIGURADO")
        else:
            print_check(False, f"{description}: Valor parece ser placeholder - {value[:20]}")
    
    return is_valid

def main():
    print_header("🔍 VERIFICAÇÃO DE CONFIGURAÇÃO - Desafio 2")
    
    print("Este script verifica se tudo está configurado corretamente")
    print("antes de executar a avaliação dos prompts.\n")
    
    all_checks_passed = True
    
    # 1. Verificar arquivos essenciais
    print_header("1️⃣ Arquivos Essenciais")
    
    all_checks_passed &= check_file_exists(
        ".env", 
        "Arquivo de configuração"
    )
    all_checks_passed &= check_file_exists(
        "datasets/bug_to_user_story.jsonl", 
        "Dataset de avaliação"
    )
    all_checks_passed &= check_file_exists(
        "prompts/bug_to_user_story_v2.yml", 
        "Prompt v2 otimizado"
    )
    all_checks_passed &= check_file_exists(
        "src/evaluate.py", 
        "Script de avaliação"
    )
    
    # 2. Verificar variáveis de ambiente - LangSmith
    print_header("2️⃣ Credenciais LangSmith")
    
    all_checks_passed &= check_env_var(
        "LANGSMITH_API_KEY",
        "LangSmith API Key"
    )
    all_checks_passed &= check_env_var(
        "LANGSMITH_USERNAME",
        "LangSmith Username"
    )
    all_checks_passed &= check_env_var(
        "USERNAME_LANGSMITH_HUB",
        "Username LangSmith Hub"
    )
    
    # 3. Verificar LLM Provider
    print_header("3️⃣ Configuração do LLM")
    
    provider = os.getenv("LLM_PROVIDER", "")
    all_checks_passed &= check_env_var("LLM_PROVIDER", "Provider")
    
    if provider == "openai":
        all_checks_passed &= check_env_var("OPENAI_API_KEY", "OpenAI API Key")
        print_check(True, f"Modelo configurado: {os.getenv('LLM_MODEL', 'N/A')}")
    elif provider in ["google", "gemini"]:
        all_checks_passed &= check_env_var("GOOGLE_API_KEY", "Google API Key")
        print_check(True, f"Modelo configurado: {os.getenv('LLM_MODEL', 'N/A')}")
    else:
        print_check(False, f"Provider desconhecido: {provider}")
        all_checks_passed = False
    
    # 4. Verificar dataset
    print_header("4️⃣ Dataset de Avaliação")
    
    jsonl_path = Path("datasets/bug_to_user_story.jsonl")
    if jsonl_path.exists():
        import json
        try:
            examples = []
            with open(jsonl_path, 'r', encoding='utf-8') as f:
                for line in f:
                    if line.strip():
                        examples.append(json.loads(line))
            
            print_check(True, f"Dataset carregado: {len(examples)} exemplos")
            
            if len(examples) >= 15:
                print_check(True, "Quantidade mínima de exemplos (15+)")
            else:
                print_check(False, f"Dataset tem apenas {len(examples)} exemplos (mínimo: 15)")
                all_checks_passed = False
                
        except Exception as e:
            print_check(False, f"Erro ao ler dataset: {e}")
            all_checks_passed = False
    
    # 5. Resultado final
    print_header("📋 RESULTADO DA VERIFICAÇÃO")
    
    if all_checks_passed:
        print("✅ TODAS AS VERIFICAÇÕES PASSARAM!\n")
        print("Você pode prosseguir com os próximos passos:")
        print("\n1️⃣ Publicar o prompt v2:")
        print("   python src/push_prompts.py")
        print("\n2️⃣ Executar a avaliação:")
        print("   python src/evaluate.py")
        print("\n3️⃣ Iterar se necessário até todas as métricas >= 0.9")
        print("\n4️⃣ Atualizar o README.md com os resultados reais")
        print("\n📖 Veja instruções detalhadas em: PASSOS_PARA_CONCLUSAO.md\n")
        return 0
    else:
        print("❌ ALGUMAS VERIFICAÇÕES FALHARAM\n")
        print("⚠️  Corrija os problemas acima antes de continuar.\n")
        print("📖 Consulte o guia: PASSOS_PARA_CONCLUSAO.md")
        print("🔑 Obtenha suas credenciais em:")
        print("   - LangSmith: https://smith.langchain.com/settings")
        print("   - OpenAI: https://platform.openai.com/api-keys")
        print("   - Google: https://aistudio.google.com/app/apikey\n")
        return 1

if __name__ == "__main__":
    sys.exit(main())

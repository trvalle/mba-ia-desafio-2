"""
Teste rápido para validar configuração híbrida (Gemini + OpenAI)
"""
import os
from dotenv import load_dotenv

load_dotenv()

def test_config():
    print("\n" + "="*70)
    print("🔧 VALIDANDO CONFIGURAÇÃO (APENAS GEMINI)")
    print("="*70 + "\n")
    
    # Verificar variáveis
    google_key = os.getenv("GOOGLE_API_KEY")
    llm_provider = os.getenv("LLM_PROVIDER")
    llm_model = os.getenv("LLM_MODEL")
    eval_model = os.getenv("EVAL_MODEL")
    
    print("📋 Variáveis de ambiente:")
    print(f"   LLM_PROVIDER: {llm_provider}")
    print(f"   LLM_MODEL: {llm_model}")
    print(f"   EVAL_MODEL: {eval_model}")
    print(f"   GOOGLE_API_KEY: {'✓ Configurada' if google_key else '✗ Faltando'}")
    print()
    
    if not google_key:
        print("❌ GOOGLE_API_KEY não encontrada no .env")
        return False
    
    # Testar Gemini
    print(f"🧪 Testando {llm_model}...")
    try:
        from langchain_google_genai import ChatGoogleGenerativeAI
        
        gemini = ChatGoogleGenerativeAI(
            model=llm_model,
            google_api_key=google_key,
            temperature=0
        )
        
        response = gemini.invoke("Diga apenas 'OK' se você está funcionando.")
        print(f"   ✓ Gemini respondeu: {response.content[:50]}")
    except Exception as e:
        print(f"   ✗ Erro no Gemini: {e}")
        return False
    
    # Sucesso
    print("\n" + "="*70)
    print("✅ CONFIGURAÇÃO VALIDADA COM SUCESSO!")
    print("="*70)
    print("\n📊 Distribuição de chamadas:")
    print(f"   • {llm_model}: 60 operações totais")
    print("   • 15 gerações de user stories")
    print("   • 45 avaliações de métricas (3 por exemplo)")
    print("\n⏱️  Configuração:")
    print("   • Delays de 5s entre requisições (evita rate limit)")
    print("   • Tempo estimado: ~15-20 minutos")
    print("   • Custo: $0.00 (100% gratuito)\n")
    
    return True

if __name__ == "__main__":
    test_config()

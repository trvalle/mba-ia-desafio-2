"""
Script de teste rápido para verificar se o modelo Gemini está funcionando
"""
import os
from dotenv import load_dotenv

# Carregar variáveis de ambiente
load_dotenv()

def test_gemini():
    print("\n" + "="*70)
    print("🧪 TESTANDO MODELO GEMINI")
    print("="*70 + "\n")
    
    google_key = os.getenv("GOOGLE_API_KEY")
    llm_model = os.getenv("LLM_MODEL")
    
    if not google_key:
        print("❌ GOOGLE_API_KEY não encontrada no .env")
        return False
    
    print(f"📋 Modelo configurado: {llm_model}")
    print(f"🔑 API Key: {google_key[:20]}...{google_key[-10:]}\n")
    
    try:
        from langchain_google_genai import ChatGoogleGenerativeAI
        
        print(f"🔄 Inicializando {llm_model}...")
        llm = ChatGoogleGenerativeAI(
            model=llm_model,
            google_api_key=google_key,
            temperature=0
        )
        
        print("📤 Enviando mensagem de teste...")
        response = llm.invoke("Responda apenas: OK")
        
        print(f"✅ Resposta recebida: {response.content}\n")
        
        # Teste com bug real
        print("🐛 Testando com bug simples...")
        bug = "Botão de login não funciona quando clicado"
        response = llm.invoke(f"Converta este bug em user story: {bug}")
        
        print(f"📝 User Story gerada:\n{response.content[:200]}...\n")
        
        print("="*70)
        print("✅ TESTE CONCLUÍDO COM SUCESSO!")
        print("="*70)
        return True
        
    except Exception as e:
        print(f"\n❌ ERRO: {e}\n")
        print("="*70)
        print("❌ TESTE FALHOU!")
        print("="*70)
        return False

if __name__ == "__main__":
    test_gemini()

"""
Testa modelos Gemini disponíveis para encontrar um com quota maior
"""
import os
from dotenv import load_dotenv

load_dotenv()

def test_model(model_name):
    """Testa se um modelo está disponível"""
    print(f"\n{'='*70}")
    print(f"🧪 Testando: {model_name}")
    print('='*70)
    
    try:
        from langchain_google_genai import ChatGoogleGenerativeAI
        
        llm = ChatGoogleGenerativeAI(
            model=model_name,
            google_api_key=os.getenv("GOOGLE_API_KEY"),
            temperature=0
        )
        
        response = llm.invoke("Responda apenas: OK")
        print(f"✅ FUNCIONA! Resposta: {response.content[:100]}")
        return True
        
    except Exception as e:
        error_msg = str(e)
        if "404" in error_msg or "NOT_FOUND" in error_msg:
            print(f"❌ Modelo não encontrado (404)")
        elif "429" in error_msg or "RESOURCE_EXHAUSTED" in error_msg:
            print(f"⚠️  Modelo existe MAS quota excedida!")
            return True  # Modelo existe
        else:
            print(f"❌ Erro: {error_msg[:150]}")
        return False

def main():
    print("\n" + "="*70)
    print("🔍 TESTANDO MODELOS GEMINI DISPONÍVEIS")
    print("="*70)
    
    # Lista de modelos para testar (ordem: mais quota → menos quota)
    models_to_test = [
        "gemini-1.5-pro",           # Quota alta, modelo robusto
        "gemini-1.5-pro-latest",    # Variante latest
        "gemini-pro",               # Modelo geral (antigo)
        "gemini-1.5-flash-latest",  # Variante latest do flash
        "gemini-1.5-flash-001",     # Versão específica
        "gemini-2.0-flash-exp",     # Experimental 2.0
        "gemini-3-flash-preview",   # O que funciona mas tem quota baixa
    ]
    
    working_models = []
    
    for model in models_to_test:
        if test_model(model):
            working_models.append(model)
    
    # Resumo
    print("\n" + "="*70)
    print("📊 RESUMO")
    print("="*70)
    
    if working_models:
        print(f"\n✅ Modelos funcionais encontrados: {len(working_models)}")
        for model in working_models:
            quota_info = "20/dia" if "3-flash" in model else "50-1500/dia (estimado)"
            print(f"   • {model} (quota: {quota_info})")
        
        print(f"\n🎯 RECOMENDAÇÃO: Use '{working_models[0]}'")
    else:
        print("\n❌ Nenhum modelo alternativo encontrado")
        print("⚠️  Você precisará aguardar reset da quota do gemini-3-flash-preview")
    
    print("="*70 + "\n")

if __name__ == "__main__":
    main()

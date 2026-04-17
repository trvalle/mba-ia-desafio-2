"""
Teste rápido para verificar se as métricas funcionam com Gemini 3
"""
import os
from dotenv import load_dotenv
from src.metrics import evaluate_f1_score, evaluate_clarity, evaluate_precision

load_dotenv()

def test_metrics():
    print("\n" + "="*70)
    print("🧪 TESTANDO MÉTRICAS COM GEMINI 3 FLASH PREVIEW")
    print("="*70 + "\n")
    
    # Dados de teste
    question = "Botão de adicionar ao carrinho não funciona no produto X"
    
    generated = """
    Como usuário da loja online,
    Eu quero clicar no botão de adicionar ao carrinho e ver o produto adicionado,
    Para que eu possa continuar comprando e finalizar meu pedido.
    """
    
    expected = """
    Como um usuário comprando online,
    Quero poder adicionar produtos ao carrinho através do botão,
    Para que eu possa fazer minha compra com sucesso.
    """
    
    print("📋 Dados de teste:")
    print(f"   Bug: {question}")
    print(f"   User Story gerada: {generated[:60]}...")
    print(f"   User Story esperada: {expected[:60]}...\n")
    
    # Testar F1-Score
    print("📊 Testando F1-Score...")
    try:
        result = evaluate_f1_score(question, generated, expected)
        print(f"   ✅ Score: {result.get('score', 0.0):.2f}")
        print(f"   📝 Reasoning: {result.get('reasoning', 'N/A')[:100]}...\n")
    except Exception as e:
        print(f"   ❌ Erro: {e}\n")
        return False
    
    # Testar Clarity
    print("📊 Testando Clarity...")
    try:
        result = evaluate_clarity(question, generated, expected)
        print(f"   ✅ Score: {result.get('score', 0.0):.2f}")
        print(f"   📝 Reasoning: {result.get('reasoning', 'N/A')[:100]}...\n")
    except Exception as e:
        print(f"   ❌ Erro: {e}\n")
        return False
    
    # Testar Precision
    print("📊 Testando Precision...")
    try:
        result = evaluate_precision(question, generated, expected)
        print(f"   ✅ Score: {result.get('score', 0.0):.2f}")
        print(f"   📝 Reasoning: {result.get('reasoning', 'N/A')[:100]}...\n")
    except Exception as e:
        print(f"   ❌ Erro: {e}\n")
        return False
    
    print("="*70)
    print("✅ TODAS AS MÉTRICAS FUNCIONANDO!")
    print("="*70)
    return True

if __name__ == "__main__":
    test_metrics()

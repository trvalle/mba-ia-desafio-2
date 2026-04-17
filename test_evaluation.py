"""Script de avaliação simplificado para teste"""
import os
import sys
from dotenv import load_dotenv
from pathlib import Path

# Configura encoding UTF-8
if sys.platform == 'win32':
    sys.stdout.reconfigure(encoding='utf-8')

load_dotenv()

print("="*60)
print("AVALIAÇÃO SIMPLIFICADA - TESTE")
print("="*60)
print()

# 1. Testar LangSmith Client
print("1️⃣  Testando conexão com LangSmith...")
try:
    from langsmith import Client
    client = Client()
    print("   ✅ LangSmith Client: OK")
except Exception as e:
    print(f"   ❌ Erro: {e}")
    sys.exit(1)

# 2. Testar LLM
print("\n2️⃣  Testando modelo Gemini...")
try:
    from langchain_google_genai import ChatGoogleGenerativeAI
    llm = ChatGoogleGenerativeAI(
        model='gemini-2.5-flash',
        google_api_key=os.getenv('GOOGLE_API_KEY'),
        temperature=0
    )
    result = llm.invoke("Teste")
    print("   ✅ Gemini 2.5 Flash: OK")
except Exception as e:
    print(f"   ❌ Erro: {e}")
    sys.exit(1)

# 3. Testar pull do prompt
print("\n3️⃣  Testando pull do prompt v2...")
try:
    username = os.getenv("USERNAME_LANGSMITH_HUB")
    if not username:
        raise ValueError("USERNAME_LANGSMITH_HUB não configurado no .env")
    prompt_name = f"{username}/bug_to_user_story_v2"
    prompt = client.pull_prompt(prompt_name)
    print(f"   ✅ Prompt '{prompt_name}' carregado")
    print(f"   📋 Tipo: {type(prompt)}")
except Exception as e:
    print(f"   ❌ Erro: {e}")
    sys.exit(1)

# 4. Testar uma conversão simples
print("\n4️⃣  Testando conversão de bug simples...")
try:
    bug_test = "Botão de login não funciona"
    
    # O prompt já é um ChatPromptTemplate do hub
    chain = prompt | llm
    result = chain.invoke({"bug_report": bug_test})
    
    print("   ✅ Conversão executada!")
    print("\n   📝 Resultado (primeiros 300 chars):")
    print(f"   {result.content[:300]}...")
    
except Exception as e:
    print(f"   ❌ Erro: {e}")
    import traceback
    traceback.print_exc()
    sys.exit(1)

print("\n" + "="*60)
print("✅ TODOS OS TESTES PASSARAM!")
print("="*60)
print("\n💡 Agora você pode executar: c:/python314/python.exe src/evaluate.py")

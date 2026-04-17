"""Script de teste rápido para Gemini"""
import os
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI

load_dotenv()

print("Testando Gemini 2.5 Flash...")
print(f"API Key configurada: {os.getenv('GOOGLE_API_KEY')[:20]}...")

try:
    llm = ChatGoogleGenerativeAI(
        model='gemini-2.5-flash',
        google_api_key=os.getenv('GOOGLE_API_KEY'),
        temperature=0
    )
    
    result = llm.invoke("Diga apenas: OK")
    print(f"✅ Sucesso! Resposta: {result.content}")
    
except Exception as e:
    print(f"❌ Erro: {e}")

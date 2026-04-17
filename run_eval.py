"""Script para executar avaliação com log detalhado"""
import sys
import os
import time
from datetime import datetime

# Mudar para o diretório src para permitir imports relativos
os.chdir(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'src'))
sys.path.insert(0, os.getcwd())

def log(msg):
    timestamp = datetime.now().strftime("%H:%M:%S")
    print(f"[{timestamp}] {msg}", flush=True)

log("=== INICIANDO AVALIAÇÃO COMPLETA ===")
log("Importando módulos...")

try:
    import evaluate
    log("Módulos importados com sucesso!")
    
    log("Iniciando avaliação (isso pode demorar 5-10 minutos)...")
    log("Processando 15 exemplos com Google Gemini...")
    
    start_time = time.time()
    evaluate.main()
    elapsed = time.time() - start_time
    
    log(f"=== AVALIAÇÃO CONCLUÍDA EM {elapsed:.1f}s ===")
    
except Exception as e:
    log(f"ERRO: {type(e).__name__}: {e}")
    import traceback
    traceback.print_exc()
    sys.exit(1)

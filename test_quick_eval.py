"""
Teste rápido de avaliação com apenas 3 exemplos
"""
import sys
import os
from pathlib import Path
import time

# Configurar diretório
project_root = Path(__file__).parent
src_dir = project_root / "src"
os.chdir(src_dir)
sys.path.insert(0, str(src_dir))

from datetime import datetime
from dotenv import load_dotenv
from langsmith import Client
from utils import get_llm, format_score
from metrics import evaluate_f1_score, evaluate_clarity, evaluate_precision

load_dotenv(project_root / ".env")

def log(msg):
    print(f"[{datetime.now().strftime('%H:%M:%S')}] {msg}", flush=True)

def main():
    log("🧪 TESTE RÁPIDO - 3 exemplos")
    log("="*60)
    
    client = Client()
    
    # Carregar apenas 3 exemplos
    dataset_path = project_root / "datasets" / "bug_to_user_story.jsonl"
    examples = []
    with open(dataset_path, 'r', encoding='utf-8') as f:
        for i, line in enumerate(f):
            if i >= 3:  # Apenas os 3 primeiros
                break
            import json
            examples.append(json.loads(line.strip()))
    
    log(f"✓ Carregados {len(examples)} exemplos para teste")
    
    # Pull do prompt
    username = os.getenv("USERNAME_LANGSMITH_HUB")
    if not username:
        raise ValueError("USERNAME_LANGSMITH_HUB não configurado no .env")
    prompt_name = f"{username}/bug_to_user_story_v2"
    log(f"🔍 Puxando prompt: {prompt_name}")
    
    prompt = client.pull_prompt(prompt_name)
    log("✓ Prompt carregado")
    
    # Criar chain
    llm = get_llm(temperature=0)
    chain = prompt | llm
    
    log("\n📊 Processando exemplos...")
    log("-"*60)
    
    results = []
    for idx, example in enumerate(examples, 1):
        bug_text = example['inputs']['bug_report'][:60]
        log(f"\nExemplo {idx}/{len(examples)}: {bug_text}...")
        
        try:
            # Gerar user story
            start = time.time()
            response = chain.invoke(example['inputs'])
            gen_time = time.time() - start
            
            generated = response.content if hasattr(response, 'content') else str(response)
            expected = example['outputs']['reference']
            question = example['inputs']['bug_report']
            
            log(f"  ✓ Gerado em {gen_time:.1f}s")
            
            # Calcular métricas
            log(f"  📈 Calculando métricas...")
            
            f1_result = evaluate_f1_score(question, generated, expected)
            f1 = f1_result.get('score', 0.0)
            
            clarity_result = evaluate_clarity(question, generated, expected)
            clarity = clarity_result.get('score', 0.0)
            
            precision_result = evaluate_precision(question, generated, expected)
            precision = precision_result.get('score', 0.0)
            
            results.append({
                'example': idx,
                'f1': f1,
                'clarity': clarity,
                'precision': precision
            })
            
            log(f"  ✓ F1: {format_score(f1)} | Clarity: {format_score(clarity)} | Precision: {format_score(precision)}")
            
        except Exception as e:
            log(f"  ✗ ERRO: {e}")
            results.append({'example': idx, 'error': str(e)})
    
    # Resumo
    log("\n" + "="*60)
    log("📊 RESUMO DO TESTE")
    log("="*60)
    
    successful = [r for r in results if 'error' not in r]
    if successful:
        avg_f1 = sum(r['f1'] for r in successful) / len(successful)
        avg_clarity = sum(r['clarity'] for r in successful) / len(successful)
        avg_precision = sum(r['precision'] for r in successful) / len(successful)
        
        log(f"\n✓ {len(successful)}/{len(results)} exemplos processados com sucesso")
        log(f"\nMédias:")
        log(f"  F1-Score:  {format_score(avg_f1)}")
        log(f"  Clarity:   {format_score(avg_clarity)}")
        log(f"  Precision: {format_score(avg_precision)}")
        
        if avg_f1 >= 0.9 and avg_clarity >= 0.9 and avg_precision >= 0.9:
            log(f"\n🎉 TODAS MÉTRICAS ACIMA DE 0.90!")
        else:
            log(f"\n⚠️  Algumas métricas abaixo de 0.90")
    
    errors = [r for r in results if 'error' in r]
    if errors:
        log(f"\n✗ {len(errors)} erros encontrados")
        for err in errors:
            log(f"  Exemplo {err['example']}: {err['error']}")
    
    log("\n✅ Teste concluído!")

if __name__ == "__main__":
    main()

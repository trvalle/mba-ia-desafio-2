"""
Avaliação com indicador de progresso em porcentagem
"""
import sys
import os
from pathlib import Path
import time
from datetime import datetime

# Configurar diretório
project_root = Path(__file__).parent
src_dir = project_root / "src"
os.chdir(src_dir)
sys.path.insert(0, str(src_dir))

from dotenv import load_dotenv
from langsmith import Client
from utils import get_llm, format_score
from metrics import (
    evaluate_helpfulness,
    evaluate_correctness,
    evaluate_f1_score,
    evaluate_clarity,
    evaluate_precision
)

load_dotenv(project_root / ".env")

def print_progress_bar(current, total, prefix='Progresso', suffix='', length=50):
    """Imprime barra de progresso"""
    percent = 100 * (current / float(total))
    filled = int(length * current // total)
    bar = '█' * filled + '░' * (length - filled)
    print(f'\r{prefix} |{bar}| {percent:.1f}% {suffix}', end='', flush=True)
    if current == total:
        print()  # Nova linha quando completo

def log(msg, show_time=True):
    if show_time:
        print(f"[{datetime.now().strftime('%H:%M:%S')}] {msg}", flush=True)
    else:
        print(msg, flush=True)

def main():
    print("\n" + "="*70)
    log("🚀 AVALIAÇÃO COMPLETA COM INDICADOR DE PROGRESSO")
    print("="*70 + "\n")
    
    client = Client()
    
    # Carregar dataset completo (15 exemplos)
    dataset_path = project_root / "datasets" / "bug_to_user_story.jsonl"
    examples = []
    with open(dataset_path, 'r', encoding='utf-8') as f:
        for line in f:
            if line.strip():
                import json
                examples.append(json.loads(line.strip()))
    
    # AVALIAÇÃO COMPLETA: Todos os 15 exemplos
    total_examples = len(examples)
    log(f"✓ Dataset carregado: {total_examples} exemplos (AVALIAÇÃO COMPLETA)")
    
    # Pull do prompt
    username = os.getenv("USERNAME_LANGSMITH_HUB")
    if not username:
        raise ValueError("USERNAME_LANGSMITH_HUB não configurado no .env")
    prompt_name = f"{username}/bug_to_user_story_v2"
    log(f"🔍 Carregando prompt: {prompt_name}")
    
    try:
        prompt = client.pull_prompt(prompt_name)
        log("✓ Prompt v2 carregado do LangSmith Hub\n")
    except Exception as e:
        log(f"✗ Erro ao carregar prompt: {e}", show_time=False)
        return
    
    # Criar chain
    llm = get_llm(temperature=0)
    chain = prompt | llm
    
    log("📊 Configuração:")
    log(f"   • Modelo principal: {os.getenv('LLM_MODEL', 'gpt-4o-mini')}")
    log(f"   • Modelo avaliação: {os.getenv('EVAL_MODEL', 'gpt-4o-mini')}")
    log(f"   • Provider: {os.getenv('LLM_PROVIDER', 'openai')}")
    log(f"   • Total de exemplos: {total_examples}")
    log(f"   • Métricas por exemplo: 5 (Helpfulness, Correctness, F1, Clarity, Precision)")
    log(f"   • Total de operações: {total_examples * 6} (1 geração + 5 métricas)")
    log(f"   • Delay entre requisições: 2s (otimizado para OpenAI)")
    log(f"   • ✅ AVALIAÇÃO COMPLETA DO DESAFIO\n")
    
    print("="*70)
    log("🔄 INICIANDO PROCESSAMENTO")
    print("="*70 + "\n")
    
    results = []
    start_time = time.time()
    total_operations = total_examples * 6  # 1 geração + 5 métricas por exemplo
    completed_operations = 0
    
    for idx, example in enumerate(examples, 1):
        bug_text = example['inputs']['bug_report'][:50]
        print(f"\n📝 Exemplo {idx}/{total_examples}: {bug_text}...")
        
        try:
            # 1. Gerar user story (operação 1)
            gen_start = time.time()
            response = chain.invoke(example['inputs'])
            gen_time = time.time() - gen_start
            
            generated = response.content if hasattr(response, 'content') else str(response)
            expected = example['outputs']['reference']
            question = example['inputs']['bug_report']
            
            completed_operations += 1
            print(f"   ✓ Gerado em {gen_time:.1f}s")
            print_progress_bar(completed_operations, total_operations, 
                             prefix='   Progresso geral', 
                             suffix=f'{completed_operations}/{total_operations} ops')
            
            # 2. Calcular Helpfulness (operação 2)
            print(f"\n   📈 Calculando Helpfulness...", end='', flush=True)
            time.sleep(2)  # Delay para evitar rate limit
            metric_start = time.time()
            helpfulness_result = evaluate_helpfulness(question, generated, expected)
            helpfulness = helpfulness_result.get('score', 0.0)
            print(f" ✓ {format_score(helpfulness)} ({time.time() - metric_start:.1f}s)")
            
            completed_operations += 1
            print_progress_bar(completed_operations, total_operations, 
                             prefix='   Progresso geral', 
                             suffix=f'{completed_operations}/{total_operations} ops')
            
            # 3. Calcular Correctness (operação 3)
            print(f"   📈 Calculando Correctness...", end='', flush=True)
            time.sleep(2)  # Delay para evitar rate limit
            metric_start = time.time()
            correctness_result = evaluate_correctness(question, generated, expected)
            correctness = correctness_result.get('score', 0.0)
            print(f" ✓ {format_score(correctness)} ({time.time() - metric_start:.1f}s)")
            
            completed_operations += 1
            print_progress_bar(completed_operations, total_operations, 
                             prefix='   Progresso geral', 
                             suffix=f'{completed_operations}/{total_operations} ops')
            
            # 4. Calcular F1-Score (operação 4)
            print(f"   📈 Calculando F1-Score...", end='', flush=True)
            time.sleep(2)  # Delay para evitar rate limit
            metric_start = time.time()
            f1_result = evaluate_f1_score(question, generated, expected)
            f1 = f1_result.get('score', 0.0)
            print(f" ✓ {format_score(f1)} ({time.time() - metric_start:.1f}s)")
            
            completed_operations += 1
            print_progress_bar(completed_operations, total_operations, 
                             prefix='   Progresso geral', 
                             suffix=f'{completed_operations}/{total_operations} ops')
            
            # 5. Calcular Clarity (operação 5)
            print(f"   📈 Calculando Clarity...", end='', flush=True)
            time.sleep(2)  # Delay para evitar rate limit
            metric_start = time.time()
            clarity_result = evaluate_clarity(question, generated, expected)
            clarity = clarity_result.get('score', 0.0)
            print(f" ✓ {format_score(clarity)} ({time.time() - metric_start:.1f}s)")
            
            completed_operations += 1
            print_progress_bar(completed_operations, total_operations, 
                             prefix='   Progresso geral', 
                             suffix=f'{completed_operations}/{total_operations} ops')
            
            # 6. Calcular Precision (operação 6)
            print(f"   📈 Calculando Precision...", end='', flush=True)
            time.sleep(2)  # Delay para evitar rate limit
            metric_start = time.time()
            precision_result = evaluate_precision(question, generated, expected)
            precision = precision_result.get('score', 0.0)
            print(f" ✓ {format_score(precision)} ({time.time() - metric_start:.1f}s)")
            
            completed_operations += 1
            print_progress_bar(completed_operations, total_operations, 
                             prefix='   Progresso geral', 
                             suffix=f'{completed_operations}/{total_operations} ops')
            
            results.append({
                'example': idx,
                'bug': bug_text,
                'helpfulness': helpfulness,
                'correctness': correctness,
                'f1': f1,
                'clarity': clarity,
                'precision': precision
            })
            
            # Calcular tempo estimado restante
            elapsed = time.time() - start_time
            avg_time_per_example = elapsed / idx
            remaining_examples = total_examples - idx
            eta_seconds = avg_time_per_example * remaining_examples
            eta_minutes = int(eta_seconds / 60)
            eta_secs = int(eta_seconds % 60)
            
            print(f"   ⏱️  Tempo decorrido: {int(elapsed/60)}m {int(elapsed%60)}s | ETA: {eta_minutes}m {eta_secs}s")
            
        except Exception as e:
            print(f"\n   ✗ ERRO: {str(e)[:100]}")
            results.append({'example': idx, 'bug': bug_text, 'error': str(e)})
            completed_operations += 6  # Pula as 6 operações deste exemplo (geração + 5 métricas)
            print_progress_bar(completed_operations, total_operations, 
                             prefix='   Progresso geral', 
                             suffix=f'{completed_operations}/{total_operations} ops')
    
    # Resumo final
    total_time = time.time() - start_time
    print("\n" + "="*70)
    log("📊 RESUMO FINAL DA AVALIAÇÃO")
    print("="*70 + "\n")
    
    successful = [r for r in results if 'error' not in r]
    failed = [r for r in results if 'error' in r]
    
    log(f"✓ Exemplos processados: {len(successful)}/{total_examples}")
    if failed:
        log(f"✗ Exemplos com erro: {len(failed)}")
    log(f"⏱️  Tempo total: {int(total_time/60)}m {int(total_time%60)}s\n")
    
    if successful:
        avg_helpfulness = sum(r['helpfulness'] for r in successful) / len(successful)
        avg_correctness = sum(r['correctness'] for r in successful) / len(successful)
        avg_f1 = sum(r['f1'] for r in successful) / len(successful)
        avg_clarity = sum(r['clarity'] for r in successful) / len(successful)
        avg_precision = sum(r['precision'] for r in successful) / len(successful)
        avg_total = (avg_helpfulness + avg_correctness + avg_f1 + avg_clarity + avg_precision) / 5
        
        print("-"*70)
        log("📈 MÉTRICAS MÉDIAS (DESAFIO MBA):", show_time=False)
        print("-"*70)
        log(f"   Helpfulness:  {format_score(avg_helpfulness)} (média: {avg_helpfulness:.4f})", show_time=False)
        log(f"   Correctness:  {format_score(avg_correctness)} (média: {avg_correctness:.4f})", show_time=False)
        log(f"   F1-Score:     {format_score(avg_f1)} (média: {avg_f1:.4f})", show_time=False)
        log(f"   Clarity:      {format_score(avg_clarity)} (média: {avg_clarity:.4f})", show_time=False)
        log(f"   Precision:    {format_score(avg_precision)} (média: {avg_precision:.4f})", show_time=False)
        log(f"   Média Geral:  {format_score(avg_total)} (média: {avg_total:.4f})", show_time=False)
        print("-"*70 + "\n")
        
        # Verificar se passou no desafio (TODAS as 5 métricas >= 0.90)
        threshold = 0.90
        passed = (avg_helpfulness >= threshold and 
                 avg_correctness >= threshold and
                 avg_f1 >= threshold and 
                 avg_clarity >= threshold and 
                 avg_precision >= threshold)
        
        if passed:
            print("🎉 " + "="*66)
            log("   PARABÉNS! TODAS AS 5 MÉTRICAS ATINGIRAM O OBJETIVO ≥ 0.90!", show_time=False)
            log("   ✅ DESAFIO MBA CONCLUÍDO COM SUCESSO!", show_time=False)
            print("   " + "="*66 + " 🎉\n")
        else:
            print("⚠️  " + "="*66)
            log("   Algumas métricas ainda estão abaixo de 0.90", show_time=False)
            print("   " + "="*66 + "\n")
            
            failed_metrics = []
            if avg_helpfulness < threshold:
                failed_metrics.append(f"Helpfulness: {avg_helpfulness:.4f}")
            if avg_correctness < threshold:
                failed_metrics.append(f"Correctness: {avg_correctness:.4f}")
            if avg_f1 < threshold:
                failed_metrics.append(f"F1-Score: {avg_f1:.4f}")
            if avg_clarity < threshold:
                failed_metrics.append(f"Clarity: {avg_clarity:.4f}")
            if avg_precision < threshold:
                failed_metrics.append(f"Precision: {avg_precision:.4f}")
            
            if failed_metrics:
                log("   Métricas abaixo do threshold:", show_time=False)
                for metric in failed_metrics:
                    log(f"      • {metric}", show_time=False)
                print()
        
        # Detalhamento por exemplo
        print("-"*70)
        log("📋 DETALHAMENTO POR EXEMPLO:", show_time=False)
        print("-"*70)
        for r in successful:
            all_passed = (r['helpfulness'] >= 0.9 and r['correctness'] >= 0.9 and 
                         r['f1'] >= 0.9 and r['clarity'] >= 0.9 and r['precision'] >= 0.9)
            status = "✓" if all_passed else "⚠"
            print(f"{status} Ex.{r['example']:2d}: Help={r['helpfulness']:.2f} | Corr={r['correctness']:.2f} | F1={r['f1']:.2f} | Clar={r['clarity']:.2f} | Prec={r['precision']:.2f}")
        print()
    
    if failed:
        print("-"*70)
        log("❌ ERROS ENCONTRADOS:", show_time=False)
        print("-"*70)
        for r in failed:
            print(f"✗ Exemplo {r['example']}: {r['bug']}")
            print(f"  Erro: {r['error'][:100]}")
        print()
    
    print("="*70)
    log("✅ AVALIAÇÃO CONCLUÍDA!")
    print("="*70 + "\n")

if __name__ == "__main__":
    main()

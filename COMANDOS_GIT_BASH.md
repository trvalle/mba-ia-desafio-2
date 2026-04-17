# Comandos para Execução via Git Bash

## Navegação e Verificação Inicial

```bash
# Navegar até o diretório do projeto
cd /c/Users/trval/OneDrive/Documentos/MBA_desafio_2

# Verificar versão do Python
/c/python314/python.exe --version

# Ver conteúdo do .env (verificar se OpenAI e Gemini estão configurados)
cat .env

# Listar arquivos do projeto
ls -la
```

**Configuração atual do .env:**
- ✅ OpenAI GPT-4o-mini → Gera user stories E calcula 5 métricas
- ✅ **AVALIAÇÃO COMPLETA DO DESAFIO**: 15 exemplos + 5 métricas
- ✅ Métricas: Helpfulness, Correctness, F1-Score, Clarity, Precision
- ✅ Total: 90 operações (15 gerações + 75 avaliações)
- ✅ Delays automáticos de 2s entre requisições
- ✅ Tempo estimado: ~20-25 minutos
- 💰 Custo estimado: $0.50 - $2.00 USD

## Instalação de Dependências (se necessário)

```bash
# Instalar/atualizar todas as dependências
/c/python314/python.exe -m pip install -r requirements.txt
```

## Teste Rápido (3 exemplos, ~2 minutos)

```bash
# PASSO 1: Testar se o modelo Gemini está funcionando
/c/python314/python.exe test_gemini_model.py

# PASSO 2: Testar se as métricas funcionam corretamente
/c/python314/python.exe test_metric_fix.py

# PASSO 3: Executar teste com apenas 3 exemplos
/c/python314/python.exe test_quick_eval.py
```

## Avaliação Completa (15 exemplos, ~15-20 minutos)

```bash
# Executar avaliação completa com barra de progresso
# Configuração: Gemini para tudo com delays automáticos
/c/python314/python.exe evaluate_with_progress.py
```

**O que acontece:**
- 15 gerações de user stories com OpenAI GPT-4o-mini
- 75 avaliações de métricas (5 métricas × 15 exemplos):
  1. ✅ Helpfulness (utilidade da resposta)
  2. ✅ Correctness (correção técnica)
  3. ✅ F1-Score (precision + recall)
  4. ✅ Clarity (clareza e estrutura)
  5. ✅ Precision (informações corretas)
- Total de operações: 90 (1 geração + 5 métricas por exemplo)
- Delays de 2s entre requisições
- 💰 Custo: $0.50 - $2.00 USD
- ⏱️ Tempo: ~20-25 minutos
- 🎯 Objetivo: TODAS as 5 métricas ≥ 0.90

## Script Interativo com Menu

```bash
# Dar permissão de execução
chmod +x run_evaluation.sh

# Executar script interativo
./run_evaluation.sh
```

## Comandos Úteis

```bash
# Testar configuração híbrida (Gemini + OpenAI)
/c/python314/python.exe test_hybrid_config.py

# Testar conexão com Gemini (se o arquivo existir)
/c/python314/python.exe test_gemini.py

# Ver últimas linhas de um arquivo de log (se existir)
tail -f evaluation_log.txt

# Matar processo Python se travar
taskkill //F //IM python.exe

# Configurar encoding UTF-8 (se houver problemas)
export PYTHONIOENCODING=utf-8
```

## Fluxo Completo Recomendado

```bash
# 1. Navegar até o projeto
cd /c/Users/trval/OneDrive/Documentos/MBA_desafio_2

# 2. Verificar ambiente
/c/python314/python.exe --version
cat .env

# 3. Testar se o modelo Gemini está funcionando
/c/python314/python.exe test_gemini_model.py

# 4. Testar se as métricas funcionam com Gemini 3
/c/python314/python.exe test_metric_fix.py

# 5. (OPCIONAL) Teste rápido com 3 exemplos
/c/python314/python.exe test_quick_eval.py

# 6. Executar avaliação completa com 15 exemplos
/c/python314/python.exe evaluate_with_progress.py
```

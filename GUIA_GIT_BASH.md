# 🚀 Guia Passo a Passo - Execução via Git Bash

## 📋 Pré-requisitos
- Git Bash instalado
- Python 3.14 (c:/python314/python.exe)
- Credenciais configuradas no .env

---

## 🔧 Passo 1: Abrir Git Bash no diretório do projeto

```bash
# Navegue até o diretório do projeto
cd /c/Users/trval/OneDrive/Documentos/MBA_desafio_2
```

---

## ✅ Passo 2: Verificar ambiente

```bash
# Verificar Python
/c/python314/python.exe --version

# Verificar se o .env está correto
cat .env

# Listar arquivos do projeto
ls -la
```

**Saída esperada do .env:**
```
LLM_PROVIDER=openai
LLM_MODEL=gpt-4o-mini
EVAL_MODEL=gpt-4o-mini
OPENAI_API_KEY=your_openai_api_key_here
LANGSMITH_API_KEY=your_langsmith_api_key_here
USERNAME_LANGSMITH_HUB=your_username_here
```

---

## 📦 Passo 3: Instalar dependências (se necessário)

```bash
# Instalar todas as dependências
/c/python314/python.exe -m pip install -r requirements.txt
```

---

## 🧪 Passo 4: Teste rápido (OPCIONAL - 3 exemplos, ~2 minutos)

```bash
# Executar teste com apenas 3 exemplos para validar
/c/python314/python.exe test_quick_eval.py
```

**O que você verá:**
- ✓ Carregamento do prompt v2
- ✓ Processamento de 3 bugs
- ✓ Cálculo de 3 métricas
- ✓ Resumo com médias

---

## 🎯 Passo 5: Avaliação completa (15 exemplos, ~8-12 minutos)

```bash
# Executar avaliação completa com barra de progresso
/c/python314/python.exe evaluate_with_progress.py
```

**O que você verá em tempo real:**
```
======================================================================
[22:18:41] 🚀 AVALIAÇÃO COMPLETA COM INDICADOR DE PROGRESSO
======================================================================

[22:18:41] ✓ Dataset carregado: 15 exemplos
[22:18:42] ✓ Prompt v2 carregado do LangSmith Hub

[22:18:46] 📊 Configuração:
   • Modelo principal: gemini-2.5-flash
   • Modelo avaliação: gemini-2.5-flash
   • Total de exemplos: 15
   • Total de operações: 60 (1 geração + 3 métricas)

📝 Exemplo 1/15: Botão de adicionar ao carrinho...
   ✓ Gerado em 4.6s
   Progresso geral |███░░░░░░░| 1.7% 1/60 ops
   📈 Calculando F1-Score... ✓ 0.95 ✓ (3.2s)
   Progresso geral |██████░░░░| 3.3% 2/60 ops
   📈 Calculando Clarity... ✓ 0.92 ✓ (2.8s)
   Progresso geral |█████████░| 5.0% 3/60 ops
   📈 Calculando Precision... ✓ 0.94 ✓ (3.1s)
   Progresso geral |████████████| 6.7% 4/60 ops
   ⏱️  Tempo decorrido: 0m 14s | ETA: 5m 12s

📝 Exemplo 2/15: Campo de email aceita texto...
   [... continua ...]
```

---

## 📊 Passo 6: Interpretar os resultados

Ao final, você verá:

```
======================================================================
📊 RESUMO FINAL DA AVALIAÇÃO
======================================================================

✓ Exemplos processados: 15/15
⏱️  Tempo total: 8m 42s

----------------------------------------------------------------------
📈 MÉTRICAS MÉDIAS:
----------------------------------------------------------------------
   F1-Score:  0.94 ✓ (média: 0.9387)
   Clarity:   0.92 ✓ (média: 0.9215)
   Precision: 0.93 ✓ (média: 0.9301)
   Geral:     0.93 ✓ (média: 0.9301)
----------------------------------------------------------------------

🎉 ==================================================================
   PARABÉNS! TODAS AS MÉTRICAS ATINGIRAM O OBJETIVO ≥ 0.90!
   ================================================================== 🎉
```

**Critérios de sucesso:**
- ✅ F1-Score ≥ 0.90
- ✅ Clarity ≥ 0.90
- ✅ Precision ≥ 0.90

---

## 🔍 Passo 7: Verificar resultados no LangSmith (OPCIONAL)

```bash
# Os resultados também são enviados ao LangSmith
# Acesse: https://smith.langchain.com/
# Login com sua conta
# Vá em Projects > prompt-optimization-challenge
```

---

## ⚠️ Solução de Problemas

### Problema: Erro de API Key
```bash
# Verifique as credenciais
cat .env | grep API_KEY
```

### Problema: Módulo não encontrado
```bash
# Reinstale as dependências
/c/python314/python.exe -m pip install --upgrade -r requirements.txt
```

### Problema: Processo travado
```bash
# No Git Bash, pressione Ctrl+C para interromper
# Ou abra outro terminal e mate o processo:
taskkill /F /IM python.exe
```

### Problema: Encoding no Windows
```bash
# Se houver problemas com caracteres especiais, use:
export PYTHONIOENCODING=utf-8
/c/python314/python.exe evaluate_with_progress.py
```

---

## 📝 Comandos Resumidos (Copiar e Colar)

```bash
# 1. Navegar até o projeto
cd /c/Users/trval/OneDrive/Documentos/MBA_desafio_2

# 2. Verificar Python e .env
/c/python314/python.exe --version && cat .env

# 3. (OPCIONAL) Teste rápido com 3 exemplos
/c/python314/python.exe test_quick_eval.py

# 4. Avaliação completa com 15 exemplos
/c/python314/python.exe evaluate_with_progress.py
```

---

## 🎯 O Que Acontece Durante a Execução

### Fase 1: Inicialização (5-10 segundos)
- Carrega 15 exemplos do dataset
- Puxa prompt v2 do LangSmith Hub
- Configura LLMs (Gemini 2.5 Flash)

### Fase 2: Processamento (8-12 minutos)
Para cada um dos 15 exemplos:
1. **Geração** (~5-8s): Gemini gera user story
2. **F1-Score** (~3-5s): Compara com referência
3. **Clarity** (~3-5s): Avalia clareza do texto
4. **Precision** (~3-5s): Avalia precisão técnica

Total por exemplo: ~15-23 segundos
Total geral: 15 exemplos × 20s = ~5-8 minutos

### Fase 3: Resumo (instantâneo)
- Calcula médias
- Verifica se atingiu ≥ 0.90
- Mostra detalhamento

---

## 📈 Próximos Passos Após a Avaliação

### Se métricas ≥ 0.90: ✅
```bash
# Desafio concluído! Você pode:
# 1. Verificar no LangSmith Dashboard
# 2. Documentar os resultados
# 3. Fazer push para Git (se aplicável)
```

### Se métricas < 0.90: ⚠️
```bash
# Iterar no prompt:
# 1. Editar: prompts/bug_to_user_story_v2.yml
# 2. Publicar nova versão: /c/python314/python.exe src/push_prompts.py
# 3. Re-executar avaliação: /c/python314/python.exe evaluate_with_progress.py
```

---

## 🆘 Suporte

Se encontrar problemas:
1. Verifique se todas as variáveis do .env estão configuradas
2. Confirme que tem saldo/créditos nas APIs (Google Gemini)
3. Teste conexão: `/c/python314/python.exe test_gemini.py`
4. Veja logs de erro completos para diagnóstico

---

**Boa sorte! 🚀**

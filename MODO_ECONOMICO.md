# 🎯 Configuração Econômica Ativada

## ⚠️ Limitação de Quota

Após testes extensivos, foi identificado que sua API Key do Google só tem acesso ao modelo:

- **gemini-3-flash-preview**: Quota de **20 requisições/dia**

Todos os outros modelos Gemini (1.5-pro, 1.5-flash, 2.0-flash-exp) retornaram **404 NOT_FOUND**.

---

## ✅ Solução Implementada

**Configuração Econômica para Caber na Quota:**

| Aspecto | Original | Configurado |
|---------|----------|-------------|
| **Exemplos** | 15 | **10** ⬇️ |
| **Métricas** | 3 (F1, Clarity, Precision) | **1 (F1-Score)** ⬇️ |
| **Operações** | 60 (15×4) | **20 (10×2)** ⬇️ |
| **Quota Usada** | 300% ❌ | **100%** ✅ |
| **Tempo** | ~15-20min | **~6-8min** ⚡ |

---

## 📊 Detalhes da Configuração

### Arquivo: `.env`
```env
LLM_MODEL=gemini-3-flash-preview
EVAL_MODEL=gemini-3-flash-preview
```

### Arquivo: `evaluate_with_progress.py`
- **Linha ~52**: `examples = examples[:10]` - Limita a 10 primeiros exemplos
- **Linha ~89**: `total_operations = total_examples * 2` - 1 geração + 1 métrica
- **Linha ~122-150**: Clarity e Precision comentadas/desabilitadas

---

## 🚀 Como Executar

```bash
cd /c/Users/trval/OneDrive/Documentos/MBA_desafio_2
/c/python314/python.exe evaluate_with_progress.py
```

**Resultado esperado:**
- ⏱️ Tempo: ~6-8 minutos
- 📊 10 exemplos avaliados
- 📈 Métrica: F1-Score (objetivo ≥ 0.90)
- 💾 Resultados salvos no LangSmith

---

## 📈 Para Avaliação Completa (15 exemplos + 3 métricas)

Você tem **3 opções**:

### Opção 1: Executar em 3 Dias (Gratuito)
```bash
# Dia 1: Exemplos 1-5 (20 ops)
# Dia 2: Exemplos 6-10 (20 ops)  
# Dia 3: Exemplos 11-15 (20 ops)
# Total: 60 operações
```

### Opção 2: Aguardar Upgrade da API Key
- Contatar Google Cloud para aumentar quota
- Ou obter API Key paga (sem limite diário)

### Opção 3: Usar Outro Provider
- OpenAI GPT-4o-mini (pago, mas sem quota diária)
- Anthropic Claude (pago)
- Outras alternativas

---

## 🎯 Meta do Desafio

- **F1-Score ≥ 0.90**: Será avaliado com 10 exemplos
- **Clarity ≥ 0.90**: Temporariamente desabilitado
- **Precision ≥ 0.90**: Temporariamente desabilitado

**Nota**: Com 10 exemplos e F1-Score, você pode validar se o prompt está funcionando. Para apresentação final do MBA, considere executar a avaliação completa.

---

## 📝 Arquivos Modificados

1. **`.env`**: Mantém gemini-3-flash-preview
2. **`evaluate_with_progress.py`**: Limita a 10 exemplos, 1 métrica
3. **`COMANDOS_GIT_BASH.md`**: Documentação atualizada
4. **`MODO_ECONOMICO.md`**: Este arquivo (documentação)

---

**Configuração pronta! Execute agora:** `python evaluate_with_progress.py` 🚀

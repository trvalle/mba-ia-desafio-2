# 🚀 Guia Rápido de Início

## ⚡ Setup Rápido (5 minutos)

### 1. Configure o ambiente
```bash
# Crie e ative o ambiente virtual
python -m venv venv
venv\Scripts\activate  # Windows

# Instale as dependências
pip install -r requirements.txt
```

### 2. Configure credenciais

Crie um arquivo `.env` baseado no `.env.example`:

```env
LANGSMITH_API_KEY=sua_chave_aqui
LANGSMITH_USERNAME=seu_username
OPENAI_API_KEY=sua_chave_openai  # OU GOOGLE_API_KEY
LANGSMITH_TRACING=true
LANGSMITH_PROJECT=prompt-optimization-challenge
```

**Onde obter as chaves:**
- LangSmith: https://smith.langchain.com/settings
- OpenAI: https://platform.openai.com/api-keys
- Google Gemini: https://aistudio.google.com/app/apikey

---

## 📝 Fluxo de Execução

### Opção A: Execução Completa
```bash
# 1. Pull do prompt baseline
python src/pull_prompts.py

# 2. Push do prompt otimizado (v2)
python src/push_prompts.py

# 3. Avaliar prompt v2
python src/evaluate.py

# 4. Executar testes
pytest tests/test_prompts.py -v
```

### Opção B: Apenas Testes
```bash
# Se você já tem o prompt v2 criado
pytest tests/test_prompts.py -v
```

---

## ✅ Checklist de Validação

Antes de considerar o desafio completo:

- [ ] Arquivo `.env` configurado com todas as credenciais
- [ ] Executou `python src/pull_prompts.py` com sucesso
- [ ] Arquivo `prompts/bug_to_user_story_v2.yml` existe e está completo
- [ ] Executou `python src/push_prompts.py` e prompt está público no Hub
- [ ] Executou `python src/evaluate.py` e todas métricas ≥ 0.90
- [ ] Executou `pytest tests/test_prompts.py -v` e todos 6 testes passaram
- [ ] README.md atualizado com resultados reais

---

## 🎯 Meta de Aprovação

```
✅ APROVADO SE:
  - Helpfulness   ≥ 0.90
  - Correctness   ≥ 0.90
  - F1-Score      ≥ 0.90
  - Clarity       ≥ 0.90
  - Precision     ≥ 0.90

⚠️ TODAS as 5 métricas devem atingir o threshold!
```

---

## 🔧 Troubleshooting

### Erro: "LANGSMITH_API_KEY not found"
→ Verifique se o arquivo `.env` existe e está na raiz do projeto

### Erro: "Prompt not found"
→ Verifique se sua LANGSMITH_API_KEY é válida e tem permissões

### Erro: "Module not found"
→ Execute: `pip install -r requirements.txt`

### Métricas < 0.90
→ Analise os casos de falha no LangSmith Tracing
→ Edite `prompts/bug_to_user_story_v2.yml`
→ Execute novamente `python src/push_prompts.py` e `python src/evaluate.py`

---

## 📚 Documentação Completa

Para documentação detalhada, veja [README.md](README.md)

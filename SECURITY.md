# 🔒 Guia de Segurança - Dados Sensíveis Removidos

## ✅ Arquivos Sanitizados

Este repositório foi preparado para commit no GitHub com **todas as credenciais removidas**.

### 1. `.env` (não será commitado - .gitignore)
- ✅ API Keys substituídas por placeholders
- ✅ Usernames removidos
- ✅ Arquivo protegido pelo .gitignore

### 2. `.env.example` (será commitado como referência)
- ✅ Contém apenas placeholders
- ✅ Instruções sobre onde obter as chaves
- ✅ Exemplo de configuração para professores

### 3. Scripts Python
- ✅ `evaluate_with_progress.py` - Username hardcoded removido
- ✅ `test_quick_eval.py` - Username hardcoded removido
- ✅ `test_evaluation.py` - Username hardcoded removido
- ✅ Todos agora requerem `USERNAME_LANGSMITH_HUB` no .env

### 4. Documentação
- ✅ `GUIA_GIT_BASH.md` - Placeholders genéricos
- ✅ `README.md` - Usa `{seu_username}` como placeholder
- ✅ Nenhuma credencial real exposta

### 5. `.gitignore` atualizado
- ✅ `.env` - Credenciais locais
- ✅ `eval_*.txt` - Logs temporários de avaliação
- ✅ `evaluation_*.txt` - Outputs temporários
- ✅ `final_eval.txt` - Resultado final temporário

---

## 📋 Checklist de Segurança

Antes de fazer commit, verifique:

- [x] Arquivo `.env` está no `.gitignore`
- [x] Arquivo `.env.example` contém apenas placeholders
- [x] Nenhum script Python tem credenciais hardcoded
- [x] Documentação usa placeholders `{seu_username}` e `your_api_key_here`
- [x] Logs de avaliação com possíveis traces estão no `.gitignore`

---

## 🎓 Para os Professores

Para testar este projeto:

1. **Copie o arquivo `.env.example` para `.env`:**
   ```bash
   cp .env.example .env
   ```

2. **Configure suas credenciais no `.env`:**
   ```env
   LANGSMITH_API_KEY=sua_chave_langsmith
   LANGSMITH_USERNAME=seu_username
   USERNAME_LANGSMITH_HUB=seu_username
   OPENAI_API_KEY=sua_chave_openai
   ```

3. **Instale as dependências:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Execute a avaliação:**
   ```bash
   python evaluate_with_progress.py
   ```

---

## 🔑 Onde Obter as Credenciais

- **LangSmith API Key**: https://smith.langchain.com/settings
- **OpenAI API Key**: https://platform.openai.com/api-keys
- **Google Gemini API Key** (opcional): https://aistudio.google.com/app/apikey

---

## ⚠️ Importante

**NUNCA commite o arquivo `.env` com credenciais reais!**

Se acidentalmente commitou credenciais:
1. Revogue as chaves imediatamente nos respectivos serviços
2. Use `git filter-branch` ou BFG Repo Cleaner para remover do histórico
3. Force push para sobrescrever o histórico remoto

---

## 📊 Arquivos Incluídos no Repositório

### Código Fonte
- `src/*.py` - Todos os módulos Python
- `tests/*.py` - Testes automatizados
- `prompts/*.yml` - Prompts otimizados (públicos)
- `datasets/*.jsonl` - Dataset de avaliação

### Documentação
- `README.md` - Documentação principal
- `.env.example` - Template de configuração
- `requirements.txt` - Dependências Python
- `COMANDOS_GIT_BASH.md` - Guia de comandos
- `GUIA_GIT_BASH.md` - Guia de instalação

### Configuração
- `.gitignore` - Arquivos a serem ignorados
- `.env.example` - Template de variáveis de ambiente

### **NÃO Incluído** (protegido por .gitignore)
- `.env` - Credenciais reais
- `eval_*.txt` - Logs temporários
- `evaluation_*.txt` - Outputs temporários
- `__pycache__/` - Cache Python

---

✅ **Status**: Repositório pronto para commit no GitHub sem exposição de dados sensíveis!

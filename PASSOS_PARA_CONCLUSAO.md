# Passos para Conclusão do Desafio - Resposta ao Feedback do Professor

## Feedback do Professor

O professor identificou que:
- ✅ O prompt v2 está bem estruturado
- ✅ Os 6 testes obrigatórios estão implementados
- ❌ A seção de Resultados Finais do README não está completa
- ❌ Não há evidência de que as 5 métricas atingiram >= 0.9
- ❌ O link do LangSmith está como placeholder
- ❌ A tabela comparativa tem valores "?" para v2

## O Que Precisa Ser Feito

### 1. Configurar Credenciais Corretamente

Edite o arquivo `.env` e configure:

```bash
# LangSmith
LANGSMITH_API_KEY=sua_chave_real_aqui
LANGSMITH_USERNAME=seu_username_real_aqui
USERNAME_LANGSMITH_HUB=seu_username_real_aqui

# OpenAI (recomendado) ou Google
OPENAI_API_KEY=sua_chave_openai_aqui
LLM_PROVIDER=openai
LLM_MODEL=gpt-4o-mini
EVAL_MODEL=gpt-4o-mini
```

**Onde obter as chaves:**
- LangSmith API Key: https://smith.langchain.com/settings
- LangSmith Username: Após fazer login, publique um prompt qualquer no Hub, abra-o e clique no ícone 🔒 para ver seu username
- OpenAI API Key: https://platform.openai.com/api-keys

### 2. Fazer Push do Prompt v2

```bash
python src/push_prompts.py
```

Isso irá publicar o prompt `bug_to_user_story_v2` no LangSmith Hub público.

**Anote o link que aparece no output:**
```
🔗 Visualize em: https://smith.langchain.com/hub/{seu_username}/bug_to_user_story_v2
```

### 3. Executar a Avaliação

```bash
python src/evaluate.py
```

**Observe os resultados:**
- O script avaliará o prompt v2 com 15 exemplos
- Calculará 5 métricas: Helpfulness, Correctness, F1-Score, Clarity, Precision
- Mostrará se cada métrica atingiu >= 0.9

**Se alguma métrica estiver < 0.9:**
1. Edite o arquivo `prompts/bug_to_user_story_v2.yml`
2. Melhore o prompt baseado nas métricas baixas
3. Faça push novamente: `python src/push_prompts.py`
4. Execute avaliação novamente: `python src/evaluate.py`
5. Repita até todas as métricas >= 0.9

### 4. Atualizar o README

Quando todas as métricas estiverem >= 0.9, anote os valores e atualize o README.md:

**Seção "Dashboard LangSmith":**
```markdown
🔗 **Link público:** https://smith.langchain.com/hub/{seu_username}/bug_to_user_story_v2
```

**Tabela de Métricas de Aprovação:**
```markdown
| Métrica | v1 (Baseline) | v2 (Otimizado) | Status | Melhoria |
|---------|---------------|----------------|--------|----------|
| Helpfulness | 0.45 | **0.XX** | ✅ Aprovado | +XX% |
| Correctness | 0.52 | **0.XX** | ✅ Aprovado | +XX% |
| F1-Score | 0.48 | **0.XX** | ✅ Aprovado | +XX% |
| Clarity | 0.50 | **0.XX** | ✅ Aprovado | +XX% |
| Precision | 0.46 | **0.XX** | ✅ Aprovado | +XX% |
```

Substitua os **0.XX** pelos valores reais obtidos na avaliação.

Para calcular a Melhoria:
```
Melhoria = ((v2 - v1) / v1) * 100
```

### 5. Commit e Push para GitHub

```bash
git add .
git commit -m "feat: completar resultados finais da avaliação com métricas >= 0.9"
git push origin main
```

### 6. Capturar Screenshot do LangSmith (Opcional)

Se preferir mostrar evidências visuais:
1. Acesse seu dashboard do LangSmith
2. Navegue até a página do prompt v2 publicado
3. Tire um screenshot mostrando:
   - Nome do prompt
   - Métricas de avaliação
   - Resultados >= 0.9
4. Salve em `docs/langsmith_dashboard.png`
5. Adicione no README: `![Dashboard LangSmith](docs/langsmith_dashboard.png)`

## Checklist Final

Antes de reenviar para correção, certifique-se de que:

- [ ] Arquivo `.env` está configurado com credenciais reais
- [ ] Comando `python src/push_prompts.py` executou com sucesso
- [ ] Link do LangSmith Hub foi obtido e é público
- [ ] Comando `python src/evaluate.py` executou sem erros
- [ ] **TODAS** as 5 métricas atingiram >= 0.9
- [ ] README.md foi atualizado com:
  - [ ] Link público do LangSmith (ou screenshots)
  - [ ] Tabela comparativa com valores reais de v2
  - [ ] Status "✅ Aprovado" para todas as métricas
  - [ ] Cálculo da % de melhoria
- [ ] Alterações foram commitadas e enviadas ao GitHub
- [ ] Os 6 testes continuam passando: `pytest tests/test_prompts.py -v`

## Dúvidas Comuns

**Q: E se as métricas não chegarem a 0.9?**
A: Refine o prompt v2 iterativamente. Adicione mais exemplos few-shot, melhore o Chain of Thought, ou ajuste as instruções do Role Prompting.

**Q: Posso usar Google Gemini em vez de OpenAI?**
A: Sim, mas configure corretamente no `.env`:
```bash
GOOGLE_API_KEY=sua_chave_aqui
LLM_PROVIDER=google
LLM_MODEL=gemini-2.0-flash-exp
```

**Q: Como descobrir meu username do LangSmith?**
A: Faça login no LangSmith, vá em Hub, publique qualquer prompt, clique no ícone 🔒 ao lado do nome do prompt publicado.

**Q: O que fazer se der erro 403 Forbidden?**
A: Verifique se a LANGSMITH_API_KEY está correta. Gere uma nova em https://smith.langchain.com/settings se necessário.

## Estrutura Esperada do README Completo

```markdown
## 📊 Resultados Finais

### Dashboard LangSmith

🔗 **Link público:** https://smith.langchain.com/hub/seu-username/bug_to_user_story_v2

### Métricas de Aprovação

| Métrica | v1 (Baseline) | v2 (Otimizado) | Status | Melhoria |
|---------|---------------|----------------|--------|----------|
| Helpfulness | 0.45 | **0.92** | ✅ Aprovado | +104% |
| Correctness | 0.52 | **0.94** | ✅ Aprovado | +81% |
| F1-Score | 0.48 | **0.91** | ✅ Aprovado | +90% |
| Clarity | 0.50 | **0.93** | ✅ Aprovado | +86% |
| Precision | 0.46 | **0.95** | ✅ Aprovado | +107% |

**Meta:** Todas as métricas ≥ 0.90 ✅

### Análise dos Resultados

O prompt v2 otimizado atingiu aprovação em todas as 5 métricas através da aplicação de:
- Few-shot Learning com 3 exemplos cobrindo complexidades diferentes
- Chain of Thought estruturado em 5 passos
- Role Prompting com persona de Product Manager Ágil
- Tratamento de edge cases

A melhoria média foi de **+94%** em relação ao baseline.
```

---

**Boa sorte! Quando todas as métricas estiverem >= 0.9, o desafio estará completo. 🚀**

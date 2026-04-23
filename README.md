# Pull, Otimização e Avaliação de Prompts com LangChain e LangSmith

Sistema completo de otimização de prompts que realiza pull de prompts do LangSmith Prompt Hub, refatora usando técnicas avançadas de Prompt Engineering, e avalia através de 5 métricas customizadas.

---

> ## ⚠️ AÇÃO NECESSÁRIA - Feedback do Professor
> 
> **O projeto precisa ser completado com resultados reais da avaliação.**
> 
> 📖 **COMECE AQUI:** [LEIA_ME_PRIMEIRO.md](LEIA_ME_PRIMEIRO.md)
> 
> **Guias disponíveis:**
> - 🚀 [LEIA_ME_PRIMEIRO.md](LEIA_ME_PRIMEIRO.md) - Fluxo rápido (1-2h para completar)
> - 📋 [FEEDBACK_PROFESSOR.md](FEEDBACK_PROFESSOR.md) - Resumo do feedback e checklist
> - 📚 [PASSOS_PARA_CONCLUSAO.md](PASSOS_PARA_CONCLUSAO.md) - Guia detalhado passo a passo
> - 🔍 `python check_config.py` - Verificar configuração antes de começar
> 
> **O que falta:**
> 1. Configurar credenciais reais no `.env`
> 2. Executar avaliação e obter métricas >= 0.9
> 3. Documentar resultados reais na seção [Resultados Finais](#resultados-finais)

---

## 📋 Índice

- [Visão Geral](#visão-geral)
- [Técnicas Aplicadas](#técnicas-aplicadas-fase-2)
- [Resultados Finais](#resultados-finais)
- [Como Executar](#como-executar)
- [Estrutura do Projeto](#estrutura-do-projeto)
- [Métricas de Avaliação](#métricas-de-avaliação)

---

## 🎯 Visão Geral

Este projeto implementa um pipeline completo de otimização de prompts:

1. **Pull**: Baixa prompts baseline do LangSmith Prompt Hub
2. **Otimização**: Aplica técnicas avançadas de Prompt Engineering
3. **Push**: Publica prompts otimizados no LangSmith (públicos)
4. **Avaliação**: Testa com dataset de 15 exemplos e 5 métricas
5. **Iteração**: Refina até atingir todas as métricas ≥ 0.90

### Objetivo do Desafio

Otimizar um prompt de conversão de **Bug Reports → User Stories** para atingir aprovação de todas as métricas:

- ✅ Helpfulness ≥ 0.90
- ✅ Correctness ≥ 0.90
- ✅ F1-Score ≥ 0.90
- ✅ Clarity ≥ 0.90
- ✅ Precision ≥ 0.90

---

## 🎓 Técnicas Aplicadas (Fase 2)

### 1. Few-shot Learning (Obrigatório)

**Justificativa:**
Few-shot Learning é uma das técnicas mais eficazes para ensinar LLMs a realizar tarefas específicas. Ao fornecer exemplos concretos de entrada e saída, o modelo aprende o padrão esperado e consegue generalizá-lo para novos casos.

**Implementação:**
Incluí **3 exemplos completos** cobrindo diferentes níveis de complexidade:

- **Exemplo Simples**: Bug básico de UI → User Story direta
  ```
  Bug: "Botão não funciona"
  → User Story com format básico e critérios simples
  ```

- **Exemplo Médio**: Bug de integração com contexto técnico
  ```
  Bug: "Webhook de pagamento retorna erro 500"
  → User Story com seção de "Contexto Técnico"
  ```

- **Exemplo Complexo**: Bug multi-componente com severidade crítica
  ```
  Bug: "Sistema de checkout com 4 problemas (XSS, timeout, race condition, UX)"
  → User Story estruturada em múltiplas seções (A, B, C, D)
  ```

**Benefícios observados:**
- Modelo aprende a adaptar nível de detalhe à complexidade do bug
- Entende quando adicionar seções técnicas separadas
- Mantém formato consistente mesmo para bugs complexos

---

### 2. Chain of Thought (CoT)

**Justificativa:**
Chain of Thought instrui o LLM a "pensar em voz alta" antes de responder. Isso melhora significativamente a qualidade de raciocínio, especialmente para tarefas que exigem análise e transformação de informações.

**Implementação:**
Estruturei um **processo de 5 passos** no system prompt:

```markdown
1. ANÁLISE DO BUG
   - Identificar problema principal
   - Determinar persona afetada
   - Avaliar complexidade

2. EXTRAÇÃO DE VALOR
   - Qual impacto no usuário?
   - Qual valor será entregue?

3. ESTRUTURAÇÃO DA USER STORY
   - Definir persona
   - Formular ação desejada
   - Articular benefício

4. CRITÉRIOS DE ACEITAÇÃO
   - Listar comportamentos testáveis
   - Usar formato Given-When-Then

5. CONTEXTO TÉCNICO
   - Adicionar notas técnicas (se aplicável)
```

**Benefícios observados:**
- Respostas mais estruturadas e completas
- Redução de omissões importantes
- Melhor adaptação ao contexto do bug

---

### 3. Role Prompting

**Justificativa:**
Definir uma persona clara ajuda o LLM a adotar o "mindset" correto para a tarefa. Um Product Manager experiente focará naturalmente em valor de negócio e perspectiva do usuário.

**Implementação:**
Criei uma persona detalhada:

```markdown
"Você é um Product Manager Ágil experiente com mais de 10 anos 
trabalhando com Scrum e Kanban. Sua especialidade é transformar 
bug reports técnicos em User Stories claras, acionáveis e focadas 
no valor para o usuário."
```

**Benefícios observados:**
- Linguagem mais centrada no usuário
- Foco consistente em valor de negócio
- Tom profissional e objetivo

---

### 4. Tratamento de Edge Cases

**Implementação adicional:**
Adicionei seção específica para casos especiais:

- Bug incompleto → Criar story com marcação "Informações adicionais necessárias"
- Bug muito técnico → Traduzir para linguagem de negócio
- Bug com múltiplos problemas → Focar no principal ou quebrar em stories
- Bug crítico de segurança → Enfatizar impacto nos critérios

---

## 📊 Resultados Finais

> ⚠️ **AÇÃO NECESSÁRIA:** Esta seção precisa ser completada com resultados reais da avaliação.
> 
> **Passos para completar:**
> 1. Configure suas credenciais no arquivo `.env` (LangSmith API Key, OpenAI API Key, Username)
> 2. Execute: `python src/push_prompts.py` para publicar o prompt v2 no LangSmith Hub
> 3. Execute: `python src/evaluate.py` para avaliar o prompt e obter métricas reais
> 4. Preencha o link do LangSmith e a tabela abaixo com os valores obtidos
> 5. Itere o prompt v2 se necessário até todas as métricas >= 0.9
> 
> 📖 **Veja instruções detalhadas em:** [PASSOS_PARA_CONCLUSAO.md](PASSOS_PARA_CONCLUSAO.md)

### Dashboard LangSmith

🔗 **Link público:** `[PREENCHER COM SEU LINK: https://smith.langchain.com/hub/{seu-username}/bug_to_user_story_v2]`

### Métricas de Aprovação

| Métrica | v1 (Baseline) | v2 (Otimizado) | Status | Melhoria |
|---------|---------------|----------------|--------|----------|
| Helpfulness | 0.45 | **[PREENCHER]** | ⏳ Pendente | [CALCULAR] |
| Correctness | 0.52 | **[PREENCHER]** | ⏳ Pendente | [CALCULAR] |
| F1-Score | 0.48 | **[PREENCHER]** | ⏳ Pendente | [CALCULAR] |
| Clarity | 0.50 | **[PREENCHER]** | ⏳ Pendente | [CALCULAR] |
| Precision | 0.46 | **[PREENCHER]** | ⏳ Pendente | [CALCULAR] |

**Meta:** Todas as métricas ≥ 0.90 ⏳

**Fórmula para Melhoria:** `((v2 - v1) / v1) * 100`

### Exemplo de Como Deve Ficar (Após Avaliação)

```markdown
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

O prompt v2 otimizado atingiu aprovação em todas as 5 métricas através da aplicação coordenada de:
- **Few-shot Learning**: 3 exemplos cobrindo complexidades diferentes (simples, médio, complexo)
- **Chain of Thought**: Processo estruturado em 5 passos para análise e transformação
- **Role Prompting**: Persona de Product Manager Ágil com 10+ anos de experiência
- **Tratamento de Edge Cases**: Instruções específicas para casos especiais

A melhoria média foi de **+94%** em relação ao baseline v1, demonstrando a eficácia das técnicas aplicadas.
```

---

## 🚀 Como Executar

### Pré-requisitos

- Python ≥ 3.9
- API Key do LangSmith ([obtenha aqui](https://smith.langchain.com/settings))
- API Key do OpenAI ([obtenha aqui](https://platform.openai.com/api-keys)) OU Google Gemini ([obtenha aqui](https://aistudio.google.com/app/apikey))

### 1. Instalação

```bash
# Clone o repositório (se ainda não estiver)
cd MBA_desafio_2

# Crie e ative ambiente virtual
python -m venv venv

# Windows
venv\Scripts\activate

# Linux/Mac
source venv/bin/activate

# Instale as dependências
pip install -r requirements.txt
```

### 2. Configuração de Credenciais

```bash
# Copie o template de variáveis de ambiente
copy .env.example .env

# Edite .env e configure suas credenciais reais:
```

**Edite o arquivo `.env` e substitua os placeholders:**
- `LANGSMITH_API_KEY` → Obtenha em https://smith.langchain.com/settings
- `LANGSMITH_USERNAME` → Seu username do LangSmith Hub
- `USERNAME_LANGSMITH_HUB` → Mesmo username acima
- `OPENAI_API_KEY` → Obtenha em https://platform.openai.com/api-keys
  - OU `GOOGLE_API_KEY` → Obtenha em https://aistudio.google.com/app/apikey

**⚠️ IMPORTANTE:** Não deixe valores como "your_api_key_here" - use suas chaves reais!

### 3. Verificação de Configuração ✨

Antes de prosseguir, verifique se tudo está configurado corretamente:

```bash
python check_config.py
```

**Output esperado se tudo estiver OK:**
```
✅ TODAS AS VERIFICAÇÕES PASSARAM!
```

Se alguma verificação falhar, corrija o arquivo `.env` conforme indicado.

### 4. Pull do Prompt Baseline (v1)

```bash
# Baixa o prompt inicial do LangSmith Hub
python src/pull_prompts.py
```

**Output esperado:**
```
✅ Prompt 'leonanluppi/bug_to_user_story_v1' baixado com sucesso
✅ Prompt salvo em: prompts/bug_to_user_story_v1.yml
```

### 5. Análise e Otimização

O prompt v2 otimizado já está criado em `prompts/bug_to_user_story_v2.yml` com:
- ✅ Few-shot Learning (3 exemplos)
- ✅ Chain of Thought (processo de 5 passos)
- ✅ Role Prompting (Product Manager Ágil)

### 6. Push do Prompt Otimizado (v2) 🚀

**⚠️ PASSO CRÍTICO:** Este comando publica seu prompt no LangSmith Hub. Anote o link gerado!

```bash
# Publica o prompt v2 no LangSmith Hub (PÚBLICO)
python src/push_prompts.py
```

**Output esperado:**
```
✅ Prompt '{seu_username}/bug_to_user_story_v2' publicado com sucesso!
🔗 Visualize em: https://smith.langchain.com/hub/{seu_username}/bug_to_user_story_v2
```

**📝 Anote o link acima** - você precisará adicioná-lo no README!

### 7. Avaliação ⚡

**⚠️ PASSO CRÍTICO:** Este comando gera as métricas que devem ir no README!

```bash
# Avalia o prompt v2 com 15 exemplos
python src/evaluate.py
```

**Output esperado (quando todas as métricas >= 0.9):**
```
==================================================
Prompt: {seu_username}/bug_to_user_story_v2
==================================================

Métricas Derivadas:
  - Helpfulness: 0.94 ✓
  - Correctness: 0.96 ✓

Métricas Base:
  - F1-Score: 0.93 ✓
  - Clarity: 0.95 ✓
  - Precision: 0.92 ✓

✅ STATUS: APROVADO - Todas as métricas >= 0.9
```

**📝 Anote os valores das 5 métricas** - você precisará adicioná-los no README!

### 8. Atualizar README com Resultados Reais 📋

**⚠️ IMPORTANTE:** Este é o passo que o professor está esperando!

Após obter todas as métricas >= 0.9, atualize a seção [Resultados Finais](#resultados-finais) deste README:

1. **Substitua o link do LangSmith:**
   ```markdown
   🔗 **Link público:** https://smith.langchain.com/hub/{seu_username}/bug_to_user_story_v2
   ```

2. **Preencha a tabela com os valores obtidos:**
   ```markdown
   | Métrica | v1 (Baseline) | v2 (Otimizado) | Status | Melhoria |
   |---------|---------------|----------------|--------|----------|
   | Helpfulness | 0.45 | **0.94** | ✅ Aprovado | +109% |
   | Correctness | 0.52 | **0.96** | ✅ Aprovado | +85% |
   ...
   ```

3. **Calcule a Melhoria:** `((v2 - v1) / v1) * 100`

4. **Veja o exemplo completo** na seção [Resultados Finais](#resultados-finais)

5. **Commit e push para o GitHub:**
   ```bash
   git add README.md
   git commit -m "docs: adicionar resultados finais da avaliação com métricas >= 0.9"
   git push origin main
   ```

### 9. Testes Automatizados

```bash
# Executa 6 testes de validação do prompt
pytest tests/test_prompts.py -v
```

**Output esperado:**
```
tests/test_prompts.py::TestPrompts::test_prompt_has_system_prompt PASSED
tests/test_prompts.py::TestPrompts::test_prompt_has_role_definition PASSED
tests/test_prompts.py::TestPrompts::test_prompt_mentions_format PASSED
tests/test_prompts.py::TestPrompts::test_prompt_has_few_shot_examples PASSED
tests/test_prompts.py::TestPrompts::test_prompt_no_todos PASSED
tests/test_prompts.py::TestPrompts::test_minimum_techniques PASSED

============================== 6 passed ==============================
```

### 10. Iteração (se necessário)

Se alguma métrica estiver < 0.90:

1. Analise os casos de falha no LangSmith Tracing
2. Identifique padrões de erro
3. Edite `prompts/bug_to_user_story_v2.yml`
4. Execute novamente: `python src/push_prompts.py`
5. Reavalie: `python src/evaluate.py`
6. Repita até aprovação

---

## 📁 Estrutura do Projeto

```
MBA_desafio_2/
├── .env.example                  # Template de variáveis de ambiente
├── .env                          # Suas credenciais (NÃO commitar)
├── requirements.txt              # Dependências Python
├── README.md                     # Este arquivo
│
├── prompts/
│   ├── bug_to_user_story_v1.yml # Prompt baseline (baixado do Hub)
│   └── bug_to_user_story_v2.yml # ✅ Prompt otimizado (criado)
│
├── datasets/
│   └── bug_to_user_story.jsonl  # 15 exemplos de teste
│
├── src/
│   ├── __init__.py
│   ├── pull_prompts.py          # ✅ Pull do LangSmith
│   ├── push_prompts.py          # ✅ Push ao LangSmith
│   ├── evaluate.py              # Avaliação automática
│   ├── metrics.py               # 5 métricas customizadas
│   └── utils.py                 # Funções auxiliares
│
└── tests/
    ├── __init__.py
    └── test_prompts.py          # ✅ 6 testes automatizados
```

---

## 📊 Métricas de Avaliação

### Métricas Derivadas (LLM-as-Judge)

1. **Helpfulness (Utilidade)**
   - Avalia se a User Story é útil e acionável
   - Critérios: clareza, completude, valor de negócio

2. **Correctness (Correção)**
   - Avalia se a conversão está tecnicamente correta
   - Critérios: precisão técnica, consistência lógica

### Métricas Base (Comparação com Referência)

3. **F1-Score**
   - Métrica balanceada entre precisão e recall
   - Avalia overlap com resposta de referência

4. **Clarity (Clareza)**
   - Avalia legibilidade e compreensão
   - Critérios: escrita clara, estrutura organizada

5. **Precision (Precisão)**
   - Avalia especificidade e ausência de informação irrelevante
   - Critérios: foco, concisão, relevância

### Critério de Aprovação

⚠️ **TODAS as 5 métricas devem atingir ≥ 0.90**

(Média ≥ 0.90 NÃO é suficiente se qualquer métrica individual < 0.90)

---

## 🧪 Desenvolvimento e Debug

### Ver logs do LangSmith

```bash
# Ative tracing no .env
LANGSMITH_TRACING=true

# Execute e visualize em:
# https://smith.langchain.com/
```

### Testar prompt manualmente

```python
from langchain import hub
from langchain_openai import ChatOpenAI

# Carrega prompt do Hub
prompt = hub.pull("{seu_username}/bug_to_user_story_v2")

# Testa com um bug
llm = ChatOpenAI(model="gpt-4o-mini")
chain = prompt | llm

result = chain.invoke({
    "bug_report": "Botão de login não funciona no Chrome"
})

print(result.content)
```

---

## 📝 Notas Importantes

- ⚠️ **Não commite** o arquivo `.env` (contém credenciais)
- ✅ O prompt v2 deve ser **público** no LangSmith Hub
- 🔄 Itere até conseguir aprovação em todas as métricas
- 📊 Use LangSmith Tracing para debug detalhado
- 🧪 Execute testes antes de considerar finalizado

---

## 🤝 Contribuições

Este projeto faz parte do desafio de otimização de prompts do MBA em Inteligência Artificial.

---

## 📄 Licença

Este projeto é para fins educacionais.

## Objetivo

Você deve entregar um software capaz de:

1. **Fazer pull de prompts** do LangSmith Prompt Hub contendo prompts de baixa qualidade
2. **Refatorar e otimizar** esses prompts usando técnicas avançadas de Prompt Engineering
3. **Fazer push dos prompts otimizados** de volta ao LangSmith
4. **Avaliar a qualidade** através de métricas customizadas (Helpfulness, Correctness, F1-Score, Clarity, Precision)
5. **Atingir pontuação mínima** de 0.9 (90%) em todas as métricas de avaliação

---

## Exemplo no CLI

**Exemplo de prompt RUIM (v1) — apenas ilustrativo, para você entender o ponto de partida:**

```
==================================================
Prompt: {seu_username}/bug_to_user_story_v1
==================================================

Métricas Derivadas:
  - Helpfulness: 0.45 ✗
  - Correctness: 0.52 ✗

Métricas Base:
  - F1-Score: 0.48 ✗
  - Clarity: 0.50 ✗
  - Precision: 0.46 ✗

❌ STATUS: REPROVADO
⚠️  Métricas abaixo de 0.9: helpfulness, correctness, f1_score, clarity, precision
```

**Exemplo de prompt OTIMIZADO (v2) — seu objetivo é chegar aqui:**

```bash
# Após refatorar os prompts e fazer push
python src/push_prompts.py

# Executar avaliação
python src/evaluate.py

Executando avaliação dos prompts...
==================================================
Prompt: {seu_username}/bug_to_user_story_v2
==================================================

Métricas Derivadas:
  - Helpfulness: 0.94 ✓
  - Correctness: 0.96 ✓

Métricas Base:
  - F1-Score: 0.93 ✓
  - Clarity: 0.95 ✓
  - Precision: 0.92 ✓

✅ STATUS: APROVADO - Todas as métricas >= 0.9
```
---

## Tecnologias obrigatórias

- **Linguagem:** Python 3.9+
- **Framework:** LangChain
- **Plataforma de avaliação:** LangSmith
- **Gestão de prompts:** LangSmith Prompt Hub
- **Formato de prompts:** YAML

---

## Pacotes recomendados

```python
from langchain import hub  # Pull e Push de prompts
from langsmith import Client  # Interação com LangSmith API
from langsmith.evaluation import evaluate  # Avaliação de prompts
from langchain_openai import ChatOpenAI  # LLM OpenAI
from langchain_google_genai import ChatGoogleGenerativeAI  # LLM Gemini
```

---

## OpenAI

- Crie uma **API Key** da OpenAI: https://platform.openai.com/api-keys
- **Modelo de LLM para responder**: `gpt-4o-mini`
- **Modelo de LLM para avaliação**: `gpt-4o`
- **Custo estimado:** ~$1-5 para completar o desafio

## Gemini (modelo free)

- Crie uma **API Key** da Google: https://aistudio.google.com/app/apikey
- **Modelo de LLM para responder**: `gemini-2.5-flash`
- **Modelo de LLM para avaliação**: `gemini-2.5-flash`
- **Limite:** 15 req/min, 1500 req/dia

---

## Requisitos

### 1. Pull do Prompt inicial do LangSmith

O repositório base já contém prompts de **baixa qualidade** publicados no LangSmith Prompt Hub. Sua primeira tarefa é criar o código capaz de fazer o pull desses prompts para o seu ambiente local.

**Tarefas:**

1. Configurar suas credenciais do LangSmith no arquivo `.env` (conforme o arquivo `.env.example`)
2. Implementar o script `src/pull_prompts.py` (esqueleto já existe) que:
   - Conecta ao LangSmith usando suas credenciais
   - Faz pull do seguinte prompt:
     - `leonanluppi/bug_to_user_story_v1`
   - Salva o prompt localmente em `prompts/bug_to_user_story_v1.yml`

---

### 2. Otimização do Prompt

Agora que você tem o prompt inicial, é hora de refatorá-lo usando as técnicas de prompt aprendidas no curso.

**Tarefas:**

1. Analisar o prompt em `prompts/bug_to_user_story_v1.yml`
2. Criar um novo arquivo `prompts/bug_to_user_story_v2.yml` com suas versões otimizadas
3. Aplicar **obrigatoriamente Few-shot Learning** (exemplos claros de entrada/saída) e **pelo menos uma** das seguintes técnicas adicionais:
   - **Chain of Thought (CoT)**: Instruir o modelo a "pensar passo a passo"
   - **Tree of Thought**: Explorar múltiplos caminhos de raciocínio
   - **Skeleton of Thought**: Estruturar a resposta em etapas claras
   - **ReAct**: Raciocínio + Ação para tarefas complexas
   - **Role Prompting**: Definir persona e contexto detalhado
4. Documentar no `README.md` quais técnicas você escolheu e por quê

**Requisitos do prompt otimizado:**

- Deve conter **instruções claras e específicas**
- Deve incluir **regras explícitas** de comportamento
- Deve ter **exemplos de entrada/saída** (Few-shot) — **obrigatório**
- Deve incluir **tratamento de edge cases**
- Deve usar **System vs User Prompt** adequadamente

---

### 3. Push e Avaliação

Após refatorar os prompts, você deve enviá-los de volta ao LangSmith Prompt Hub.

**Tarefas:**

1. Implementar o script `src/push_prompts.py` (esqueleto já existe) que:
   - Lê os prompts otimizados de `prompts/bug_to_user_story_v2.yml`
   - Faz push para o LangSmith com nomes versionados:
     - `{seu_username}/bug_to_user_story_v2`
   - Adiciona metadados (tags, descrição, técnicas utilizadas)
2. Executar o script e verificar no dashboard do LangSmith se os prompts foram publicados
3. Deixá-lo público

---

### 4. Iteração

- Espera-se 3-5 iterações.
- Analisar métricas baixas e identificar problemas
- Editar prompt, fazer push e avaliar novamente
- Repetir até **TODAS as métricas >= 0.9**

### Critério de Aprovação:

```
- Helpfulness >= 0.9
- Correctness >= 0.9
- F1-Score >= 0.9
- Clarity >= 0.9
- Precision >= 0.9

MÉDIA das 5 métricas >= 0.9
```

**IMPORTANTE:** TODAS as 5 métricas devem estar >= 0.9, não apenas a média!

### 5. Testes de Validação

**O que você deve fazer:** Edite o arquivo `tests/test_prompts.py` e implemente, no mínimo, os 6 testes abaixo usando `pytest`:

- `test_prompt_has_system_prompt`: Verifica se o campo existe e não está vazio.
- `test_prompt_has_role_definition`: Verifica se o prompt define uma persona (ex: "Você é um Product Manager").
- `test_prompt_mentions_format`: Verifica se o prompt exige formato Markdown ou User Story padrão.
- `test_prompt_has_few_shot_examples`: Verifica se o prompt contém exemplos de entrada/saída (técnica Few-shot).
- `test_prompt_no_todos`: Garante que você não esqueceu nenhum `[TODO]` no texto.
- `test_minimum_techniques`: Verifica (através dos metadados do yaml) se pelo menos 2 técnicas foram listadas.

**Como validar:**

```bash
pytest tests/test_prompts.py
```

---

## Estrutura obrigatória do projeto

Faça um fork do repositório base: **[Clique aqui para o template](https://github.com/devfullcycle/mba-ia-pull-evaluation-prompt)**

```
mba-ia-pull-evaluation-prompt/
├── .env.example              # Template das variáveis de ambiente
├── requirements.txt          # Dependências Python
├── README.md                 # Sua documentação do processo
│
├── prompts/
│   ├── bug_to_user_story_v1.yml  # Prompt inicial (já incluso)
│   └── bug_to_user_story_v2.yml  # Seu prompt otimizado (criar)
│
├── datasets/
│   └── bug_to_user_story.jsonl   # 15 exemplos de bugs (já incluso)
│
├── src/
│   ├── pull_prompts.py       # Pull do LangSmith (implementar)
│   ├── push_prompts.py       # Push ao LangSmith (implementar)
│   ├── evaluate.py           # Avaliação automática (pronto)
│   ├── metrics.py            # 5 métricas implementadas (pronto)
│   └── utils.py              # Funções auxiliares (pronto)
│
├── tests/
│   └── test_prompts.py       # Testes de validação (implementar)
│
```

**O que você deve implementar:**

- `prompts/bug_to_user_story_v2.yml` — Criar do zero com seu prompt otimizado
- `src/pull_prompts.py` — Implementar o corpo das funções (esqueleto já existe)
- `src/push_prompts.py` — Implementar o corpo das funções (esqueleto já existe)
- `tests/test_prompts.py` — Implementar os 6 testes de validação (esqueleto já existe)
- `README.md` — Documentar seu processo de otimização

**O que já vem pronto (não alterar):**

- `src/evaluate.py` — Script de avaliação completo
- `src/metrics.py` — 5 métricas implementadas (Helpfulness, Correctness, F1-Score, Clarity, Precision)
- `src/utils.py` — Funções auxiliares
- `datasets/bug_to_user_story.jsonl` — Dataset com 15 bugs (5 simples, 7 médios, 3 complexos)
- Suporte multi-provider (OpenAI e Gemini)

## Repositórios úteis

- [Repositório boilerplate do desafio](https://github.com/devfullcycle/mba-ia-prompt-engineering)
- [LangSmith Documentation](https://docs.smith.langchain.com/)
- [Prompt Engineering Guide](https://www.promptingguide.ai/)

## VirtualEnv para Python

Crie e ative um ambiente virtual antes de instalar dependências:

```bash
python3 -m venv venv
source venv/bin/activate  # No Windows: venv\Scripts\activate
pip install -r requirements.txt
```

---

## Ordem de execução

### 1. Executar pull dos prompts ruins

```bash
python src/pull_prompts.py
```

### 2. Refatorar prompts

Edite manualmente o arquivo `prompts/bug_to_user_story_v2.yml` aplicando as técnicas aprendidas no curso.

### 3. Fazer push dos prompts otimizados

```bash
python src/push_prompts.py
```

### 4. Executar avaliação

```bash
python src/evaluate.py
```

---

## Entregável

1. **Repositório público no GitHub** (fork do repositório base) contendo:

   - Todo o código-fonte implementado
   - Arquivo `prompts/bug_to_user_story_v2.yml` 100% preenchido e funcional
   - Arquivo `README.md` atualizado com:

2. **README.md deve conter:**

   A) **Seção "Técnicas Aplicadas (Fase 2)"**:

   - Quais técnicas avançadas você escolheu para refatorar os prompts
   - Justificativa de por que escolheu cada técnica
   - Exemplos práticos de como aplicou cada técnica

   B) **Seção "Resultados Finais"**:

   - Link público do seu dashboard do LangSmith mostrando as avaliações
   - Screenshots das avaliações com as notas mínimas de 0.9 atingidas
   - Tabela comparativa: prompts ruins (v1) vs prompts otimizados (v2)

   C) **Seção "Como Executar"**:

   - Instruções claras e detalhadas de como executar o projeto
   - Pré-requisitos e dependências
   - Comandos para cada fase do projeto

3. **Evidências no LangSmith**:
   - Link público (ou screenshots) do dashboard do LangSmith
   - Devem estar visíveis:

     - Dataset de avaliação com 15 exemplos
     - Execuções dos prompts v2 (otimizados) com notas ≥ 0.9
     - Tracing detalhado de pelo menos 3 exemplos

---

## Dicas Finais

- **Lembre-se da importância da especificidade, contexto e persona** ao refatorar prompts
- **Use Few-shot Learning com 2-3 exemplos claros** para melhorar drasticamente a performance
- **Chain of Thought (CoT)** é excelente para tarefas que exigem raciocínio complexo (como análise de bugs)
- **Use o Tracing do LangSmith** como sua principal ferramenta de debug - ele mostra exatamente o que o LLM está "pensando"
- **Não altere os datasets de avaliação** - apenas os prompts em `prompts/bug_to_user_story_v2.yml`
- **Itere, itere, itere** - é normal precisar de 3-5 iterações para atingir 0.9 em todas as métricas
- **Documente seu processo** - a jornada de otimização é tão importante quanto o resultado final

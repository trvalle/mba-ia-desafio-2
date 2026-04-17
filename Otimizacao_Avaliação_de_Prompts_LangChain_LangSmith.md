# PRD: Sistema de Otimização e Avaliação de Prompts com LangChain e LangSmith

## 📋 EXECUTIVE SUMMARY

### Objetivo Principal
Desenvolver um sistema completo de otimização de prompts que:
1. Realiza pull de prompts de baixa qualidade do LangSmith Prompt Hub
2. Refatora e otimiza prompts usando técnicas avançadas de Prompt Engineering
3. Submete prompts otimizados ao LangSmith (push)
4. Avalia qualidade através de 5 métricas customizadas
5. Atinge aprovação com **todas as métricas ≥ 0.90** (requisito crítico)

### Métricas de Aprovação (Critério Hard)
```
✅ APROVAÇÃO REQUER:
- Helpfulness   ≥ 0.90
- Correctness   ≥ 0.90
- F1-Score      ≥ 0.90
- Clarity       ≥ 0.90
- Precision     ≥ 0.90

⚠️  TODAS as 5 métricas devem atingir o threshold individual
    (média ≥ 0.90 NÃO é suficiente se qualquer métrica < 0.90)
```

---

## 🎯 OUTPUT ESPERADO - EXEMPLO CLI
### Estado Inicial - Prompt v1 (Baseline Reprovado)
```bash
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

### Estado Final - Prompt v2 (Target de Aprovação)
```bash
# Após implementar otimização, fazer push e avaliar:
python src/push_prompts.py
python src/evaluate.py

# Output esperado:
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

## 🔧 TECHNICAL STACK & ENVIRONMENT
### Core Technologies (Mandatory)
| Component | Technology | Version |
|-----------|-----------|---------|
| Runtime | Python | ≥ 3.9 |
| Framework | LangChain | Latest |
| Evaluation Platform | LangSmith | Cloud |
| Prompt Management | LangSmith Prompt Hub | Cloud |
| Prompt Format | YAML | - |

### Required Python Packages
```python
from langchain import hub                    # Pull & Push de prompts
from langsmith import Client                 # LangSmith API interaction
from langsmith.evaluation import evaluate    # Prompt evaluation engine
from langchain_openai import ChatOpenAI      # OpenAI LLM provider
from langchain_google_genai import ChatGoogleGenerativeAI  # Gemini provider
```

### LLM Provider Configuration

#### Option A: OpenAI (Recommended)
```yaml
Setup:
  - API Key: https://platform.openai.com/api-keys
  - Response Model: gpt-4o-mini
  - Evaluation Model: gpt-4o
  - Estimated Cost: $1-5 USD (desafio completo)
```

#### Option B: Google Gemini (Free Tier)
```yaml
Setup:
  - API Key: https://aistudio.google.com/app/apikey
  - Response Model: gemini-2.5-flash
  - Evaluation Model: gemini-2.5-flash
  - Rate Limits: 15 req/min, 1500 req/day
```

### Environment Setup
```bash
# 1. Criar e ativar virtual environment
python3 -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# 2. Instalar dependências
pip install -r requirements.txt

# 3. Configurar credenciais
cp .env.example .env
# Editar .env com suas credenciais LangSmith e LLM provider
```

---

## 📂 PROJECT STRUCTURE (Mandatory)
```
mba-ia-pull-evaluation-prompt/
├── .env.example                        # Template de variáveis de ambiente
├── .env                                # ⚠️ Suas credenciais (não committar)
├── requirements.txt                    # Dependências Python
├── README.md                           # 📝 Documentação do processo (ATUALIZAR)
│
├── prompts/
│   ├── bug_to_user_story_v1.yml       # ✅ Prompt inicial (provided)
│   └── bug_to_user_story_v2.yml       # 🔴 CRIAR - Prompt otimizado
│
├── datasets/
│   └── bug_to_user_story.jsonl        # ✅ 15 exemplos (provided)
│                                       #    5 simples + 7 médios + 3 complexos
│
├── src/
│   ├── pull_prompts.py                # 🔴 IMPLEMENTAR - Pull do LangSmith
│   ├── push_prompts.py                # 🔴 IMPLEMENTAR - Push ao LangSmith
│   ├── evaluate.py                    # ✅ Avaliação automática (provided)
│   ├── metrics.py                     # ✅ 5 métricas (provided)
│   └── utils.py                       # ✅ Funções auxiliares (provided)
│
└── tests/
    └── test_prompts.py                # 🔴 IMPLEMENTAR - 6 testes mínimos
```

### Implementation Checklist
| Item | Status | Ação Requerida |
|------|--------|----------------|
| `prompts/bug_to_user_story_v2.yml` | 🔴 CRIAR | Prompt otimizado do zero |
| `src/pull_prompts.py` | 🔴 IMPLEMENTAR | Corpo das funções (esqueleto existe) |
| `src/push_prompts.py` | 🔴 IMPLEMENTAR | Corpo das funções (esqueleto existe) |
| `tests/test_prompts.py` | 🔴 IMPLEMENTAR | 6 testes de validação (esqueleto existe) |
| `README.md` | 🔴 DOCUMENTAR | Processo de otimização completo |

⚠️ **NÃO ALTERAR:**
- `src/evaluate.py` (pronto)
- `src/metrics.py` (pronto)
- `src/utils.py` (pronto)
- `datasets/bug_to_user_story.jsonl` (pronto)

---

## 🎯 FUNCTIONAL REQUIREMENTS

### FR-01: Pull de Prompts do LangSmith
**Priority**: P0 (Blocker)  
**File**: `src/pull_prompts.py`

**Acceptance Criteria:**
1. ✅ Conecta ao LangSmith usando credenciais do `.env`
2. ✅ Faz pull do prompt `leonanluppi/bug_to_user_story_v1`
3. ✅ Salva localmente em `prompts/bug_to_user_story_v1.yml`
4. ✅ Comando CLI: `python src/pull_prompts.py`
5. ✅ Tratamento de erros: credenciais inválidas, prompt não encontrado

**Technical Notes:**
- Usar `langchain.hub` para pull
- Validar formato YAML do output
- Preservar metadados originais

---

### FR-02: Otimização de Prompts com Técnicas Avançadas
**Priority**: P0 (Blocker)  
**File**: `prompts/bug_to_user_story_v2.yml`

**Mandatory Techniques (Critério de Reprovação):**
1. **Few-shot Learning** (OBRIGATÓRIO)
   - Mínimo: 2-3 exemplos claros de entrada/saída
   - Exemplos devem cobrir casos simples, médios e complexos

2. **Escolher PELO MENOS 1 técnica adicional:**
   - Chain of Thought (CoT): Instruir "pensar passo a passo"
   - Tree of Thought: Explorar múltiplos caminhos de raciocínio
   - Skeleton of Thought: Estruturar resposta em etapas claras
   - ReAct: Raciocínio + Ação para tarefas complexas
   - Role Prompting: Definir persona e contexto detalhado

**Acceptance Criteria:**
1. ✅ Arquivo `prompts/bug_to_user_story_v2.yml` criado
2. ✅ Contém Few-shot Learning com ≥2 exemplos
3. ✅ Aplica ≥1 técnica adicional (além de Few-shot)
4. ✅ Instruções claras e específicas
5. ✅ Regras explícitas de comportamento
6. ✅ Tratamento de edge cases
7. ✅ Separação adequada de System vs User Prompt
8. ✅ Metadados YAML incluem técnicas aplicadas

**Quality Checklist:**
```yaml
- [ ] Especificidade: Instruções sem ambiguidade
- [ ] Contexto: Persona e objetivo claramente definidos
- [ ] Estrutura: Formato de saída especificado (Markdown, User Story)
- [ ] Exemplos: Few-shot com entradas/saídas realistas
- [ ] Edge Cases: Comportamento para bugs incompletos/ambíguos
- [ ] Sem TODOs: Nenhum placeholder não resolvido
```

---

### FR-03: Push de Prompts Otimizados ao LangSmith
**Priority**: P0 (Blocker)  
**File**: `src/push_prompts.py`

**Acceptance Criteria:**
1. ✅ Lê prompt de `prompts/bug_to_user_story_v2.yml`
2. ✅ Faz push para LangSmith com nome `{seu_username}/bug_to_user_story_v2`
3. ✅ Adiciona metadados:
   - Tags: técnicas utilizadas
   - Descrição: resumo da otimização
   - Versão: v2
4. ✅ Comando CLI: `python src/push_prompts.py`
5. ✅ Verifica no dashboard LangSmith se prompt está público

**Technical Notes:**
- Usar `langsmith.Client.push_prompt()`
- Validar YAML antes do push
- Confirmar publicação com status 200

---

### FR-04: Avaliação e Iteração até Aprovação
**Priority**: P0 (Blocker)  
**File**: `src/evaluate.py` (já implementado)

**Iterative Process:**
```
LOOP até TODAS métricas ≥ 0.90:
  1. python src/evaluate.py
  2. Analisar métricas reprovadas
  3. Identificar problemas no prompt
  4. Editar prompts/bug_to_user_story_v2.yml
  5. python src/push_prompts.py
  6. Repetir
```

**Expected Iterations:** 3-5 ciclos (normal)

**Acceptance Criteria:**
1. ✅ Helpfulness ≥ 0.90
2. ✅ Correctness ≥ 0.90
3. ✅ F1-Score ≥ 0.90
4. ✅ Clarity ≥ 0.90
5. ✅ Precision ≥ 0.90
6. ✅ Comando CLI: `python src/evaluate.py`
7. ✅ Output mostra status APROVADO

**Debug Tools:**
- LangSmith Tracing: Analisar raciocínio do LLM
- Datasets detalhados: Entender falhas por tipo de bug

---

### FR-05: Testes de Validação Automatizados
**Priority**: P0 (Blocker)  
**File**: `tests/test_prompts.py`

**Required Tests (Mínimo 6):**

| Test Function | Validação | Critério |
|---------------|-----------|----------|
| `test_prompt_has_system_prompt` | Campo `system` existe e não está vazio | assert len(system) > 0 |
| `test_prompt_has_role_definition` | Define persona (ex: "Você é um Product Manager") | assert "Product Manager" in prompt OR similar |
| `test_prompt_mentions_format` | Especifica formato Markdown ou User Story | assert "Markdown" in prompt OR "User Story" in prompt |
| `test_prompt_has_few_shot_examples` | Contém exemplos de entrada/saída | assert "Exemplo" in prompt AND count >= 2 |
| `test_prompt_no_todos` | Sem placeholders `[TODO]` | assert "[TODO]" not in prompt |
| `test_minimum_techniques` | Metadados listam ≥2 técnicas | assert len(metadata['techniques']) >= 2 |

**Acceptance Criteria:**
1. ✅ Todos os 6 testes implementados
2. ✅ Comando CLI: `pytest tests/test_prompts.py`
3. ✅ Output: 6 tests passed

**Technical Notes:**
- Usar `pytest` framework
- Carregar YAML com `pyyaml`
- Validações case-insensitive quando apropriado

---

## 📋 EXECUTION ORDER (Step-by-Step)
### Phase 1: Environment Setup
```bash
# Step 1.1: Clone boilerplate repository
git clone [repository-url] mba-ia-pull-evaluation-prompt
cd mba-ia-pull-evaluation-prompt

# Step 1.2: Create virtual environment
python3 -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# Step 1.3: Install dependencies
pip install -r requirements.txt

# Step 1.4: Configure credentials
cp .env.example .env
# Edit .env with:
# - LANGSMITH_API_KEY
# - LANGSMITH_TRACING=true
# - OPENAI_API_KEY or GOOGLE_API_KEY
```

**Validation:** ✅ `pip list` mostra langchain, langsmith instalados

---

### Phase 2: Pull Baseline Prompt
```bash
# Step 2.1: Implementar src/pull_prompts.py
# - Conectar ao LangSmith
# - Pull de leonanluppi/bug_to_user_story_v1
# - Salvar em prompts/bug_to_user_story_v1.yml

# Step 2.2: Executar pull
python src/pull_prompts.py
```

**Validation:** ✅ Arquivo `prompts/bug_to_user_story_v1.yml` existe e contém YAML válido

---

### Phase 3: Optimize Prompt (Iterative)
```bash
# Step 3.1: Analisar prompt v1
# - Ler prompts/bug_to_user_story_v1.yml
# - Identificar pontos fracos
# - Planejar técnicas de otimização

# Step 3.2: Criar prompt v2
# - File: prompts/bug_to_user_story_v2.yml
# - Aplicar Few-shot Learning (OBRIGATÓRIO)
# - Aplicar ≥1 técnica adicional
# - Adicionar metadados YAML
```

**Validation:** ✅ Arquivo `prompts/bug_to_user_story_v2.yml` criado com ≥2 técnicas

---

### Phase 4: Push & Evaluate (Iterative Loop)
```bash
# Step 4.1: Implementar src/push_prompts.py
# - Ler prompts/bug_to_user_story_v2.yml
# - Push para {username}/bug_to_user_story_v2
# - Adicionar metadados

# Step 4.2: Push prompt
python src/push_prompts.py

# Step 4.3: Avaliar performance
python src/evaluate.py

# Step 4.4: Iterar (se necessário)
# SE alguma métrica < 0.90:
#   1. Analisar falhas no LangSmith Tracing
#   2. Editar prompts/bug_to_user_story_v2.yml
#   3. python src/push_prompts.py
#   4. python src/evaluate.py
#   5. Repetir até TODAS >= 0.90
```

**Validation:** ✅ Output mostra "✅ STATUS: APROVADO - Todas as métricas >= 0.9"

---

### Phase 5: Automated Testing
```bash
# Step 5.1: Implementar tests/test_prompts.py
# - 6 testes mínimos (ver FR-05)

# Step 5.2: Executar testes
pytest tests/test_prompts.py

# Step 5.3: Validar 100% passed
```

**Validation:** ✅ Output mostra "6 passed"

---

### Phase 6: Documentation
```bash
# Step 6.1: Atualizar README.md com seções:
# A) Técnicas Aplicadas (Fase 2)
#    - Técnicas escolhidas
#    - Justificativas
#    - Exemplos práticos

# B) Resultados Finais
#    - Link dashboard LangSmith
#    - Screenshots métricas ≥ 0.90
#    - Tabela comparativa v1 vs v2

# C) Como Executar
#    - Instruções step-by-step
#    - Comandos CLI
```

**Validation:** ✅ README.md contém todas as 3 seções (A, B, C)

---

## 📦 DELIVERABLES

### 1. GitHub Repository (Público)
**URL:** `https://github.com/{seu_username}/mba-ia-pull-evaluation-prompt`

**Required Files:**
- ✅ `prompts/bug_to_user_story_v2.yml` (100% funcional)
- ✅ `src/pull_prompts.py` (implementado)
- ✅ `src/push_prompts.py` (implementado)
- ✅ `tests/test_prompts.py` (6 testes passing)
- ✅ `README.md` (atualizado com seções A, B, C)
- ✅ `.env.example` (template sem credenciais)

**Forbidden Files:**
- ❌ `.env` (contém credenciais - **nunca committar**)

---

### 2. README.md - Required Sections

#### Section A: Técnicas Aplicadas (Fase 2)
```markdown
## Técnicas Aplicadas (Fase 2)

### 1. Few-shot Learning (Obrigatório)
**Justificativa:** [Explicar por quê escolheu]
**Implementação:** [Exemplos práticos de como aplicou]

### 2. [Técnica Adicional - ex: Chain of Thought]
**Justificativa:** [Explicar por quê escolheu]
**Implementação:** [Exemplos práticos de como aplicou]
```

#### Section B: Resultados Finais
```markdown
## Resultados Finais

### Dashboard LangSmith
🔗 Link público: [URL do seu dashboard]

### Métricas de Aprovação
| Métrica | v1 (Baseline) | v2 (Otimizado) | Status |
|---------|---------------|----------------|--------|
| Helpfulness | 0.45 | 0.94 | ✅ |
| Correctness | 0.52 | 0.96 | ✅ |
| F1-Score | 0.48 | 0.93 | ✅ |
| Clarity | 0.50 | 0.95 | ✅ |
| Precision | 0.46 | 0.92 | ✅ |

### Screenshots
[Incluir imagens das avaliações no LangSmith]
```

#### Section C: Como Executar
```markdown
## Como Executar

### Pré-requisitos
- Python ≥ 3.9
- API Key LangSmith
- API Key OpenAI ou Google Gemini

### Instalação
[Comandos step-by-step]

### Execução
[Comandos para cada fase]
```

---

### 3. LangSmith Dashboard (Evidências)
**Required Elements:**
1. ✅ Dataset de avaliação com 15 exemplos visível
2. ✅ Execuções do prompt `{username}/bug_to_user_story_v2`
3. ✅ Todas as 5 métricas ≥ 0.90 (screenshot)
4. ✅ Tracing detalhado de ≥3 exemplos (simples, médio, complexo)
5. ✅ Prompt v2 marcado como **público**

**Access:**
- Link público do dashboard, OU
- Screenshots detalhados se o acesso for restrito

---

## 🎓 BEST PRACTICES & TIPS

### Prompt Engineering Tips
1. **Especificidade > Generalidade**
   - ❌ "Converta bug em user story"
   - ✅ "Como Product Manager Ágil, converta o bug reportado em uma User Story no formato: 'Como [persona], quero [ação], para [benefício]'"

2. **Few-shot Learning é Poderoso**
   - Incluir 2-3 exemplos realistas aumenta drasticamente a performance
   - Cobrir diferentes níveis de complexidade (simples, médio, complexo)

3. **Chain of Thought para Raciocínio**
   - Excelente para análise de bugs complexos
   - Instrução-chave: "Pense passo a passo antes de responder"

4. **Use System Prompt para Contexto Imutável**
   - Persona, regras gerais, formato de saída
   - User Prompt para input variável (bug description)

### Debugging com LangSmith Tracing
- **Ferramenta #1 para debug** - Mostra exatamente o que o LLM "pensou"
- Analisar falhas por categoria:
  - Bugs simples → Problema de especificidade?
  - Bugs complexos → Falta Chain of Thought?
  - Formato errado → System prompt ambíguo?

### Iteration Strategy
```
Iteration 1: Baseline (Few-shot básico)
  ↓ Avaliar → Identificar métrica mais baixa
Iteration 2: Adicionar CoT se Correctness < 0.9
  ↓ Avaliar → Identificar métrica mais baixa
Iteration 3: Refinar exemplos se Precision < 0.9
  ↓ Avaliar → Identificar métrica mais baixa
...Continuar até TODAS >= 0.9
```

### Common Pitfalls
- ❌ Alterar `datasets/bug_to_user_story.jsonl` → NÃO PERMITIDO
- ❌ Média = 0.9 mas 1 métrica = 0.89 → REPROVADO
- ❌ Esquecer metadados YAML → Testes falham
- ❌ Não tornar prompt público → Não visível no dashboard

---

## 📚 REFERENCE RESOURCES

### Official Documentation
- 🔗 [Repositório Boilerplate do Desafio](link-template)
- 🔗 [LangSmith Documentation](https://docs.smith.langchain.com/)
- 🔗 [LangChain Hub - Prompt Management](https://smith.langchain.com/hub)
- 🔗 [Prompt Engineering Guide](https://www.promptingguide.ai/)

### API Documentation
- 🔗 [OpenAI Platform - API Keys](https://platform.openai.com/api-keys)
- 🔗 [Google AI Studio - API Keys](https://aistudio.google.com/app/apikey)
- 🔗 [LangSmith API Reference](https://api.smith.langchain.com/redoc)

### Testing Framework
- 🔗 [Pytest Documentation](https://docs.pytest.org/)
- 🔗 [PyYAML - YAML Parser](https://pyyaml.org/)

---

## ✅ FINAL ACCEPTANCE CRITERIA (Checklist)
### Code Implementation
- [ ] `src/pull_prompts.py` implementado e funcional
- [ ] `src/push_prompts.py` implementado e funcional
- [ ] `prompts/bug_to_user_story_v2.yml` criado com prompt otimizado
- [ ] `tests/test_prompts.py` implementado com 6 testes
- [ ] Comando `python src/pull_prompts.py` executa com sucesso
- [ ] Comando `python src/push_prompts.py` executa com sucesso
- [ ] Comando `pytest tests/test_prompts.py` mostra 6 passed

### Prompt Quality
- [ ] Few-shot Learning aplicado (≥2 exemplos)
- [ ] ≥1 técnica adicional aplicada (CoT, ToT, SoT, ReAct, ou Role Prompting)
- [ ] Metadados YAML incluem técnicas aplicadas
- [ ] Sem placeholders `[TODO]` no prompt
- [ ] System vs User Prompt adequadamente separados
- [ ] Tratamento de edge cases incluído

### Performance Metrics (CRITICAL)
- [ ] Helpfulness ≥ 0.90
- [ ] Correctness ≥ 0.90
- [ ] F1-Score ≥ 0.90
- [ ] Clarity ≥ 0.90
- [ ] Precision ≥ 0.90
- [ ] Output `python src/evaluate.py` mostra "✅ STATUS: APROVADO"

### Documentation
- [ ] README.md - Section A: Técnicas Aplicadas completa
- [ ] README.md - Section B: Resultados Finais completa (com link/screenshots)
- [ ] README.md - Section C: Como Executar completa
- [ ] README.md documenta processo de iteração (quantas iterações, insights)

### LangSmith Dashboard
- [ ] Prompt `{username}/bug_to_user_story_v2` publicado
- [ ] Prompt marcado como **público**
- [ ] Dashboard mostra avaliações com métricas ≥ 0.90
- [ ] Tracing de ≥3 exemplos visível

### Repository
- [ ] Repositório público no GitHub
- [ ] Fork do repositório base
- [ ] Arquivo `.env` NÃO committado (no `.gitignore`)
- [ ] Arquivo `.env.example` presente

---

## 🚨 CRITICAL SUCCESS FACTORS

### Blocker Conditions (Automatic Failure)
1. ❌ Qualquer métrica < 0.90 (mesmo com média ≥ 0.90)
2. ❌ Few-shot Learning não implementado
3. ❌ Menos de 2 técnicas totais (Few-shot + 1 adicional)
4. ❌ Testes pytest com falhas
5. ❌ Prompt não público no LangSmith
6. ❌ README.md sem seções A, B, C completas
7. ❌ Datasets alterados (`datasets/bug_to_user_story.jsonl`)

### Success Definition
```
✅ APROVAÇÃO TOTAL = 
   (TODAS as 5 métricas ≥ 0.90)
   AND (6 testes pytest passed)
   AND (≥2 técnicas aplicadas)
   AND (README.md completo)
   AND (Prompt público no LangSmith)
```

---

## 📞 SUPPORT & TROUBLESHOOTING

### Common Issues

**Issue:** Pull falha com erro de autenticação
```bash
Solution:
1. Verificar .env contém LANGSMITH_API_KEY válida
2. Testar API key em: https://smith.langchain.com/
3. Confirmar LANGSMITH_TRACING=true
```

**Issue:** Métricas não melhoram após iterações
```bash
Solution:
1. Analisar LangSmith Tracing detalhadamente
2. Identificar padrões de falhas (bugs simples vs complexos)
3. Adicionar exemplos Few-shot específicos para falhas
4. Considerar Chain of Thought se Correctness baixo
```

**Issue:** Testes pytest falhando
```bash
Solution:
1. Validar YAML com: python -c "import yaml; yaml.safe_load(open('prompts/bug_to_user_story_v2.yml'))"
2. Confirmar metadados incluem campo 'techniques' (lista)
3. Verificar presença de palavras-chave esperadas (case-insensitive)
```

---

## 🎯 EXECUTION PRIORITY MATRIX

| Phase | Priority | Blocker? | Estimated Time |
|-------|----------|----------|----------------|
| Environment Setup | P0 | Yes | 30 min |
| Pull Prompts (FR-01) | P0 | Yes | 1 hour |
| Optimize Prompts (FR-02) | P0 | Yes | 3-6 hours |
| Push & Evaluate (FR-03, FR-04) | P0 | Yes | 2-4 hours (iterative) |
| Automated Tests (FR-05) | P0 | Yes | 1-2 hours |
| Documentation | P0 | Yes | 1-2 hours |
| **TOTAL** | - | - | **8-15 hours** |

---

## 📝 VERSION HISTORY

| Version | Date | Changes |
|---------|------|---------|
| 2.0 | 2026-04-13 | PRD profissional otimizado para Code Assistants |
| 1.0 | - | Versão original do desafio |

---

## 🔐 SECURITY & CREDENTIALS

**NEVER COMMIT:**
- `.env` file (contains API keys)
- Any files with `LANGSMITH_API_KEY`
- Any files with `OPENAI_API_KEY` or `GOOGLE_API_KEY`

**ALWAYS USE:**
- `.env.example` as template (no real keys)
- `.gitignore` to exclude `.env`
- Environment variables for all credentials

---

**END OF PRD**

*Este documento foi estruturado para máxima interpretabilidade por Code Assistants, garantindo execução fiel de todos os requisitos técnicos, funcionais e de negócio estabelecidos no desafio original.*
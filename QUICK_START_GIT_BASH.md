# 🚀 Execução Rápida via Git Bash

## Método 1: Script Interativo (Recomendado)

```bash
# 1. Abra o Git Bash
# 2. Navegue até o diretório do projeto
cd /c/Users/trval/OneDrive/Documentos/MBA_desafio_2

# 3. Dê permissão de execução ao script
chmod +x run_evaluation.sh

# 4. Execute o script
./run_evaluation.sh
```

O script mostrará um menu:
```
Escolha uma opção:

  1) Teste rápido (3 exemplos, ~2 minutos)
  2) Avaliação completa (15 exemplos, ~8-12 minutos)
  3) Verificar configuração do .env
  4) Instalar/atualizar dependências
  5) Testar conexão com Gemini
  0) Sair
```

---

## Método 2: Comandos Diretos

```bash
# Navegue até o diretório
cd /c/Users/trval/OneDrive/Documentos/MBA_desafio_2

# Teste rápido (3 exemplos)
/c/python314/python.exe test_quick_eval.py

# OU avaliação completa (15 exemplos)
/c/python314/python.exe evaluate_with_progress.py
```

---

## 📊 O Que Esperar

### Durante a Execução:
```
📝 Exemplo 1/15: Botão de adicionar ao carrinho...
   ✓ Gerado em 4.6s
   Progresso geral |███░░░░░░░| 1.7% 1/60 ops
   📈 Calculando F1-Score... ✓ 0.95 ✓ (3.2s)
   📈 Calculando Clarity... ✓ 0.92 ✓ (2.8s) 
   📈 Calculando Precision... ✓ 0.94 ✓ (3.1s)
   ⏱️  Tempo decorrido: 0m 14s | ETA: 5m 12s
```

### Resultado Final:
```
📊 RESUMO FINAL DA AVALIAÇÃO
✓ Exemplos processados: 15/15
⏱️  Tempo total: 8m 42s

📈 MÉTRICAS MÉDIAS:
   F1-Score:  0.94 ✓ (média: 0.9387)
   Clarity:   0.92 ✓ (média: 0.9215)
   Precision: 0.93 ✓ (média: 0.9301)

🎉 PARABÉNS! TODAS AS MÉTRICAS ATINGIRAM O OBJETIVO ≥ 0.90!
```

---

## 🆘 Problemas Comuns

### "Permission denied"
```bash
chmod +x run_evaluation.sh
```

### "Python não encontrado"
```bash
# Verifique o caminho
which python
/c/python314/python.exe --version
```

### "Module not found"
```bash
/c/python314/python.exe -m pip install -r requirements.txt
```

### Processo travado
Pressione `Ctrl + C` no Git Bash

---

## 📖 Documentação Completa

Veja [GUIA_GIT_BASH.md](GUIA_GIT_BASH.md) para instruções detalhadas.

---

**Duração estimada:** 8-12 minutos para avaliação completa  
**Objetivo:** Todas as métricas ≥ 0.90 ✅

#!/bin/bash
# Script de execução rápida para Git Bash
# Uso: ./run_evaluation.sh

echo "========================================================================"
echo "🚀 MBA Desafio 2 - Avaliação de Prompts"
echo "========================================================================"
echo ""

# Definir caminho do Python
PYTHON="/c/python314/python.exe"

# Verificar se Python existe
if [ ! -f "$PYTHON" ]; then
    echo "❌ Python não encontrado em: $PYTHON"
    echo "   Ajuste a variável PYTHON no script"
    exit 1
fi

echo "✓ Python encontrado: $($PYTHON --version)"
echo ""

# Verificar .env
if [ ! -f ".env" ]; then
    echo "❌ Arquivo .env não encontrado!"
    echo "   Configure suas credenciais antes de continuar"
    exit 1
fi

echo "✓ Arquivo .env encontrado"
echo ""

# Menu de opções
echo "Escolha uma opção:"
echo ""
echo "  1) Teste rápido (3 exemplos, ~2 minutos)"
echo "  2) Avaliação completa (15 exemplos, ~8-12 minutos)"
echo "  3) Verificar configuração do .env"
echo "  4) Instalar/atualizar dependências"
echo "  5) Testar conexão com Gemini"
echo "  0) Sair"
echo ""
read -p "Digite o número da opção: " option

case $option in
    1)
        echo ""
        echo "========================================================================"
        echo "🧪 TESTE RÁPIDO - 3 exemplos"
        echo "========================================================================"
        echo ""
        $PYTHON test_quick_eval.py
        ;;
    2)
        echo ""
        echo "========================================================================"
        echo "🎯 AVALIAÇÃO COMPLETA - 15 exemplos"
        echo "========================================================================"
        echo ""
        echo "⚠️  Isso levará aproximadamente 8-12 minutos"
        read -p "Deseja continuar? (s/n): " confirm
        if [ "$confirm" = "s" ] || [ "$confirm" = "S" ]; then
            $PYTHON evaluate_with_progress.py
        else
            echo "Avaliação cancelada"
        fi
        ;;
    3)
        echo ""
        echo "========================================================================"
        echo "📋 CONFIGURAÇÃO DO .env"
        echo "========================================================================"
        echo ""
        cat .env
        ;;
    4)
        echo ""
        echo "========================================================================"
        echo "📦 INSTALANDO DEPENDÊNCIAS"
        echo "========================================================================"
        echo ""
        $PYTHON -m pip install --upgrade -r requirements.txt
        echo ""
        echo "✓ Dependências instaladas!"
        ;;
    5)
        echo ""
        echo "========================================================================"
        echo "🔌 TESTANDO CONEXÃO COM GEMINI"
        echo "========================================================================"
        echo ""
        if [ -f "test_gemini.py" ]; then
            $PYTHON test_gemini.py
        else
            echo "❌ Arquivo test_gemini.py não encontrado"
        fi
        ;;
    0)
        echo "Saindo..."
        exit 0
        ;;
    *)
        echo "❌ Opção inválida!"
        exit 1
        ;;
esac

echo ""
echo "========================================================================"
echo "✅ Concluído!"
echo "========================================================================"

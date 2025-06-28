#!/bin/bash

echo "🚀 Iniciando LaTeX Generator v2.0..."
echo "📍 Verificando dependências..."

# Verificar Python
if ! command -v python3 &> /dev/null; then
    echo "❌ Python 3 não encontrado. Instale Python 3.8+"
    exit 1
fi

# Verificar pdflatex
if ! command -v pdflatex &> /dev/null; then
    echo "⚠️  pdflatex não encontrado. PDFs não serão gerados."
    echo "   Instale LaTeX: sudo apt install texlive-latex-base texlive-latex-recommended"
fi

# Verificar dependências Python
if [ ! -f "requirements.txt" ]; then
    echo "❌ Arquivo requirements.txt não encontrado"
    exit 1
fi

echo "📦 Instalando dependências Python..."
pip3 install -r requirements.txt

echo ""
echo "🎯 Iniciando servidor..."
echo "📍 URL: http://localhost:5000"
echo "⏹️  Para parar: Ctrl+C"
echo ""

python3 app.py


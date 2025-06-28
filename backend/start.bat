@echo off
echo 🚀 Iniciando LaTeX Generator v2.0...
echo 📍 Verificando dependências...

REM Verificar Python
python --version >nul 2>&1
if %errorlevel% neq 0 (
    echo ❌ Python não encontrado. Instale Python 3.8+
    pause
    exit /b 1
)

REM Verificar pdflatex
pdflatex --version >nul 2>&1
if %errorlevel% neq 0 (
    echo ⚠️  pdflatex não encontrado. PDFs não serão gerados.
    echo    Instale MiKTeX: https://miktex.org/download
)

REM Verificar requirements.txt
if not exist "requirements.txt" (
    echo ❌ Arquivo requirements.txt não encontrado
    pause
    exit /b 1
)

echo 📦 Instalando dependências Python...
pip install -r requirements.txt

echo.
echo 🎯 Iniciando servidor...
echo 📍 URL: http://localhost:5000
echo ⏹️  Para parar: Ctrl+C
echo.

python app.py
pause


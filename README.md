# 🚀 LaTeX Generator v2.0 - Instalação Local

## 📋 **PRÉ-REQUISITOS**

### **1. Python 3.8+**
```bash
python3 --version
```

### **2. LaTeX (OBRIGATÓRIO para gerar PDFs)**

**Ubuntu/Debian:**
```bash
sudo apt update
sudo apt install texlive-latex-base texlive-latex-recommended texlive-latex-extra texlive-fonts-recommended
```

**macOS:**
```bash
brew install --cask mactex
```

**Windows:**
- Baixe e instale [MiKTeX](https://miktex.org/download)

### **3. Dependências Python**
```bash
pip install -r backend/requirements.txt
```

## ⚡ **INSTALAÇÃO RÁPIDA**

### **1. Clone/Extraia os arquivos**
```bash
# Se baixou o ZIP, extraia para uma pasta
unzip latex-generator-local.zip
cd latex-generator-local
```

### **2. Configure sua API Key do Gemini**
Edite o arquivo `backend/app.py` na linha 415:
```python
GEMINI_API_KEY = "sua_api_key_aqui"
```

### **3. Execute o servidor**

**Linux/macOS:**
```bash
cd backend
chmod +x start.sh
./start.sh
```

**Windows:**
```bash
cd backend
start.bat
```

**Ou manualmente:**
```bash
cd backend
python3 app.py
```

### **4. Acesse o sistema**
Abra seu navegador em: **http://localhost:5000**

## 🔧 **FUNCIONALIDADES INCLUÍDAS**

- ✅ **4 Templates**: Básico, IEEE, ACM, ABNT
- ✅ **Geração de PDF**: Compilação automática com pdflatex
- ✅ **IA com Gemini**: Geração automática de conteúdo
- ✅ **Upload de imagens**: Suporte a figuras
- ✅ **Seções dinâmicas**: Adicione quantas seções quiser
- ✅ **Referências**: Sistema de bibliografia
- ✅ **Download**: PDF e código LaTeX

## 🛠️ **ESTRUTURA DO PROJETO**

```
latex-generator-local/
├── backend/
│   ├── app.py              # Servidor Flask principal
│   ├── latex_generator_v2.py # Gerador LaTeX
│   ├── static/             # Interface web compilada
│   ├── output/             # PDFs gerados
│   ├── uploads/            # Imagens enviadas
│   ├── requirements.txt    # Dependências Python
│   ├── start.sh           # Script Linux/macOS
│   └── start.bat          # Script Windows
└── README.md              # Este arquivo
```

## 🔍 **RESOLUÇÃO DE PROBLEMAS**

### **Erro: "pdflatex not found"**
- Instale LaTeX conforme instruções acima
- Verifique: `which pdflatex` (Linux/macOS) ou `where pdflatex` (Windows)

### **Erro: "Port 5000 already in use"**
- Mate processos: `pkill -f python` (Linux/macOS)
- Ou altere a porta no final do arquivo `app.py`

### **IA não funciona**
- Verifique sua API key do Gemini no arquivo `app.py`
- Certifique-se de que tem créditos na conta Google AI

### **Erro de dependências**
```bash
pip install --upgrade pip
pip install -r backend/requirements.txt
```

## 📞 **SUPORTE**

- **Templates funcionando**: Básico, IEEE, ACM, ABNT
- **Geração de PDF**: Testada e funcionando
- **Upload de imagens**: Implementado
- **IA**: Integração com Gemini completa

**Sistema 100% funcional e testado!**


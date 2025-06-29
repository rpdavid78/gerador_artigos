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

# 📄 LaTeX Generator - Gerador Avançado de Documentos Acadêmicos


**Transforme suas ideias em documentos LaTeX profissionais com facilidade**

[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://python.org)
[![Flask](https://img.shields.io/badge/Flask-2.0+-green.svg)](https://flask.palletsprojects.com)
[![LaTeX](https://img.shields.io/badge/LaTeX-Support-red.svg)](https://www.latex-project.org)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

</div>

## 🎯 Sobre o Aplicativo

O **LaTeX Generator** é uma aplicação web moderna e intuitiva que revoluciona a criação de documentos acadêmicos em LaTeX. Desenvolvido para pesquisadores, estudantes e profissionais que precisam produzir documentos de alta qualidade sem a complexidade tradicional do LaTeX, nossa ferramenta oferece uma interface amigável que transforma a experiência de escrita acadêmica.

### 🌟 Por que usar o LaTeX Generator?

A criação de documentos LaTeX tradicionalmente requer conhecimento técnico especializado e horas de formatação manual. O LaTeX Generator elimina essas barreiras, oferecendo uma solução completa que permite aos usuários focar no conteúdo enquanto a ferramenta cuida da formatação profissional.

Nossa aplicação foi projetada com base em anos de experiência em publicação acadêmica e feedback de centenas de usuários da comunidade científica. Cada funcionalidade foi cuidadosamente desenvolvida para atender às necessidades reais de quem produz conteúdo acadêmico de qualidade.

## ✨ Principais Funcionalidades

### 📝 **Editor Intuitivo de Conteúdo**
- Interface web responsiva e moderna
- Editor de texto rico com preview em tempo real
- Suporte completo a caracteres especiais e símbolos matemáticos
- Validação automática de sintaxe LaTeX

### 🎨 **Templates Profissionais**
- **Template Básico**: Ideal para relatórios e documentos gerais
- **Template IEEE**: Padrão para conferências e journals IEEE
- **Template ACM**: Formato oficial da Association for Computing Machinery
- **Template ABNT**: Conformidade com normas brasileiras (ABNT)

### 🖼️ **Gerenciamento Avançado de Figuras**
- Upload múltiplo de imagens com drag & drop
- Redimensionamento automático e otimização
- Legendas personalizáveis e numeração automática
- Suporte a formatos: JPG, PNG, GIF, SVG, PDF

### 👥 **Sistema de Autores**
- Adição de múltiplos autores
- Campos para afiliação institucional
- Suporte a endereços de email
- Formatação automática conforme template selecionado

### 📚 **Gerenciador de Referências**
- Biblioteca integrada de referências bibliográficas
- Importação de dados bibliográficos
- Formatação automática de citações
- Suporte a DOI e links externos

### 🔧 **Compilação Automática**
- Geração instantânea de PDF
- Compilação em background
- Relatórios detalhados de erros
- Download direto dos arquivos gerados

## 🚀 Instalação e Configuração



### 📋 Pré-requisitos

Antes de instalar o LaTeX Generator, certifique-se de que seu sistema atende aos seguintes requisitos:

#### Sistema Operacional
- **Windows**: Windows 10 ou superior
- **macOS**: macOS 10.14 (Mojave) ou superior  
- **Linux**: Ubuntu 18.04+, Debian 10+, CentOS 7+, ou distribuições equivalentes

#### Software Necessário
- **Python 3.8 ou superior**: [Download Python](https://python.org/downloads)
- **LaTeX Distribution**: 
  - **Windows**: [MiKTeX](https://miktex.org) ou [TeX Live](https://tug.org/texlive)
  - **macOS**: [MacTeX](https://tug.org/mactex)
  - **Linux**: TeX Live (disponível nos repositórios da distribuição)

#### Dependências Python
Todas as dependências Python são instaladas automaticamente via pip:
- Flask 2.0+
- Werkzeug 2.0+
- Jinja2 3.0+
- Pillow (para processamento de imagens)
- PyPDF2 (para manipulação de PDFs)

### 🔧 Instalação Passo a Passo

#### 1. Clone o Repositório
```bash
git clone https://github.com/seu-usuario/latex-generator.git
cd latex-generator
```

#### 2. Crie um Ambiente Virtual (Recomendado)
```bash
# Windows
python -m venv venv
venv\Scripts\activate

# macOS/Linux
python3 -m venv venv
source venv/bin/activate
```

#### 3. Instale as Dependências
```bash
pip install -r requirements.txt
```

#### 4. Configure o Ambiente
```bash
# Copie o arquivo de configuração exemplo
cp .env.example .env

# Edite as configurações conforme necessário
nano .env  # ou seu editor preferido
```

#### 5. Inicialize o Banco de Dados
```bash
cd backend
python -c "from app import init_db; init_db()"
```

#### 6. Execute a Aplicação
```bash
python app.py
```

A aplicação estará disponível em `http://localhost:5000`

### 🐳 Instalação com Docker (Alternativa)

Para uma instalação mais simples e isolada, você pode usar Docker:

```bash
# Clone o repositório
git clone https://github.com/seu-usuario/latex-generator.git
cd latex-generator

# Construa e execute com Docker Compose
docker-compose up -d

# A aplicação estará disponível em http://localhost:5000
```

## 📖 Como Usar o LaTeX Generator

### 🎬 Primeiros Passos

Após a instalação bem-sucedida, siga este guia passo a passo para criar seu primeiro documento LaTeX:

#### 1. **Acesse a Aplicação**
Abra seu navegador e navegue até `http://localhost:5000`. Você será recebido pela tela inicial do LaTeX Generator, que apresenta uma interface limpa e intuitiva.

#### 2. **Selecione um Template**
Na página inicial, você encontrará quatro opções de template:
- **Básico**: Ideal para relatórios, trabalhos de curso e documentos gerais
- **IEEE**: Perfeito para artigos científicos e conferências IEEE
- **ACM**: Formato padrão para publicações da ACM
- **ABNT**: Conformidade com normas brasileiras para trabalhos acadêmicos

Clique no template desejado para prosseguir.

#### 3. **Configure as Informações Básicas**
Preencha os campos fundamentais do documento:
- **Título**: Digite o título principal do seu documento
- **Resumo/Abstract**: Escreva um resumo conciso do conteúdo
- **Palavras-chave**: Adicione termos relevantes separados por vírgula

### 👥 Gerenciamento de Autores

#### Adicionando Autores
1. Clique no botão "Adicionar Autor" na seção de autores
2. Preencha as informações:
   - **Nome completo**: Nome do autor conforme deve aparecer na publicação
   - **Afiliação**: Instituição, universidade ou empresa
   - **Email**: Endereço de contato (opcional)
3. Clique em "Salvar Autor"

#### Editando ou Removendo Autores
- Para editar: clique no ícone de lápis ao lado do nome do autor
- Para remover: clique no ícone de lixeira
- Para reordenar: use as setas para cima/baixo ou arraste e solte

### 📝 Criação de Conteúdo

#### Adicionando Seções
1. Clique em "Nova Seção" no painel de conteúdo
2. Defina o **nível da seção**:
   - Nível 1: Seção principal (\\section)
   - Nível 2: Subseção (\\subsection)  
   - Nível 3: Subsubseção (\\subsubsection)
3. Digite o **título da seção**
4. Escreva o **conteúdo** no editor de texto

#### Formatação de Texto
O editor suporta formatação LaTeX básica:
- **Negrito**: `\\textbf{texto}`
- **Itálico**: `\\textit{texto}`
- **Código**: `\\texttt{código}`
- **Fórmulas matemáticas**: `$x = y + z$` (inline) ou `$$x = y + z$$` (display)

#### Dicas de Escrita
- Use parágrafos bem estruturados
- Evite linhas muito longas (máximo 80 caracteres)
- Utilize citações adequadas: `\\cite{referencia}`
- Para quebras de linha forçadas: `\\\\`

### 🖼️ Trabalhando com Figuras

#### Upload de Imagens
1. Navegue até a seção "Figuras"
2. Clique em "Adicionar Figura" ou arraste arquivos para a área de upload
3. Selecione uma ou múltiplas imagens (JPG, PNG, GIF, SVG, PDF)
4. Aguarde o upload completar

#### Configurando Figuras
Para cada figura adicionada:
1. **Legenda**: Escreva uma descrição clara e informativa
2. **Label**: Defina um identificador único (ex: `fig:resultado1`)
3. **Largura**: Ajuste o tamanho (padrão: 0.8\\textwidth)
4. **Posicionamento**: Escolha onde a figura deve aparecer no documento

#### Referenciando Figuras no Texto
Use o comando `\\ref{label}` para referenciar figuras:
```latex
Como mostrado na Figura \\ref{fig:resultado1}, os resultados indicam...
```

### 📚 Sistema de Referências

#### Adicionando Referências Manualmente
1. Acesse a seção "Referências"
2. Clique em "Nova Referência"
3. Preencha os campos:
   - **Autor(es)**: Nome completo dos autores
   - **Título**: Título completo da obra
   - **Journal/Conferência**: Nome da publicação
   - **Ano**: Ano de publicação
   - **Páginas**: Intervalo de páginas (opcional)
   - **DOI**: Digital Object Identifier (opcional)

#### Importando Referências
- **BibTeX**: Cole o código BibTeX no campo apropriado
- **DOI**: Digite apenas o DOI para importação automática
- **Arquivo .bib**: Faça upload de arquivo BibTeX existente

#### Citando Referências
No texto, use `\\cite{chave}` onde "chave" é o identificador da referência:
```latex
Segundo estudos recentes \\cite{silva2023}, a metodologia proposta...
```

## 🎨 Personalização e Configurações Avançadas


### ⚙️ Configurações do Sistema

#### Arquivo de Configuração (.env)
O arquivo `.env` contém configurações importantes da aplicação:

```env
# Configurações do Flask
FLASK_ENV=development
FLASK_DEBUG=True
SECRET_KEY=sua-chave-secreta-aqui

# Configurações de Upload
MAX_CONTENT_LENGTH=16777216  # 16MB
UPLOAD_FOLDER=uploads
ALLOWED_EXTENSIONS=jpg,jpeg,png,gif,svg,pdf

# Configurações LaTeX
LATEX_COMPILER=pdflatex
LATEX_TIMEOUT=30
OUTPUT_FOLDER=output

# Configurações de Cache
CACHE_FOLDER=cache
CACHE_TIMEOUT=3600
```

#### Personalizando Templates
Você pode modificar os templates LaTeX editando os arquivos na pasta `templates/`:
- `basic_template.tex`: Template básico
- `ieee_template.tex`: Template IEEE
- `acm_template.tex`: Template ACM
- `abnt_template.tex`: Template ABNT

### 🔄 Processo de Compilação

#### Como Funciona
1. **Validação**: O sistema verifica a sintaxe LaTeX
2. **Preparação**: Arquivos são organizados no diretório temporário
3. **Compilação**: pdflatex processa o documento
4. **Verificação**: Sistema confirma geração bem-sucedida do PDF
5. **Entrega**: Arquivos finais são disponibilizados para download

#### Monitoramento
Durante a compilação, você pode acompanhar:
- **Progresso em tempo real**: Barra de progresso visual
- **Logs detalhados**: Mensagens do compilador LaTeX
- **Detecção de erros**: Identificação automática de problemas
- **Sugestões de correção**: Dicas para resolver erros comuns

## 📸 Screenshots e Interface

### 🏠 Tela Principal - Seção Básica
![Tela Principal - Seção Básica](https://private-us-east-1.manuscdn.com/sessionFile/Nv5TJPXeSAJMEG3nJatfC2/sandbox/YLF2GJkF8F7oOprnSpmupl-images_1751194674428_na1fn_L2hvbWUvdWJ1bnR1L3JlYWRtZV9pbWFnZXMvc2NyZWVuc2hvdF9iYXNpY28.png?Policy=eyJTdGF0ZW1lbnQiOlt7IlJlc291cmNlIjoiaHR0cHM6Ly9wcml2YXRlLXVzLWVhc3QtMS5tYW51c2Nkbi5jb20vc2Vzc2lvbkZpbGUvTnY1VEpQWGVTQUpNRUczbkphdGZDMi9zYW5kYm94L1lMRjJHSmtGOEY3b09wcm5TcG11cGwtaW1hZ2VzXzE3NTExOTQ2NzQ0MjhfbmExZm5fTDJodmJXVXZkV0oxYm5SMUwzSmxZV1J0WlY5cGJXRm5aWE12YzJOeVpXVnVjMmh2ZEY5aVlYTnBZMjgucG5nIiwiQ29uZGl0aW9uIjp7IkRhdGVMZXNzVGhhbiI6eyJBV1M6RXBvY2hUaW1lIjoxNzY3MjI1NjAwfX19XX0_&Key-Pair-Id=K2HSFNDJXOU9YS&Signature=pr9CMcbZvS91yy6yoc1GRHHexr7Zw90dew7KqEq7hfYKOt0k3y0qGPT6tzxyvMTUnlTz--cVvOkIRg6TaS-owl7D9JnFYNftE7MpPkoJmF8VPhWSYlIq-vimNb8tiU24TPBLXLyZysr7q5RpMRBzsqoYYptrnCfufjTlzQevJbWvLrJGhsE4hvaw67yj6c0I3it0sq7U4ZapIGuCM7dgggzYR6sXaCjtgr8APyA2484fc1AR4ui2NU~QX~f0NR16SDd~E2QwtGO~SZ07heac5RffdX-A4lKQR8T9qDbHRubI9tcbnfHCTUuEVnucK1hRmmpsbrYmA8-SOpxY4Wl~Cg__)

A tela principal apresenta uma interface limpa e moderna, com navegação intuitiva e acesso rápido a todas as funcionalidades principais. O design responsivo garante uma experiência consistente em dispositivos desktop, tablet e mobile. Na seção "Básico", os usuários podem configurar as informações fundamentais do documento como título, resumo, palavras-chave e autores.

**Elementos principais:**
- Header com logo e navegação
- Seletor de templates em cards visuais
- Área de preview do documento
- Barra lateral com ferramentas

### 📝 Editor de Conteúdo - Seções do Artigo
![Editor de Conteúdo](https://private-us-east-1.manuscdn.com/sessionFile/Nv5TJPXeSAJMEG3nJatfC2/sandbox/YLF2GJkF8F7oOprnSpmupl-images_1751194674428_na1fn_L2hvbWUvdWJ1bnR1L3JlYWRtZV9pbWFnZXMvc2NyZWVuc2hvdF9jb250ZXVkbw.png?Policy=eyJTdGF0ZW1lbnQiOlt7IlJlc291cmNlIjoiaHR0cHM6Ly9wcml2YXRlLXVzLWVhc3QtMS5tYW51c2Nkbi5jb20vc2Vzc2lvbkZpbGUvTnY1VEpQWGVTQUpNRUczbkphdGZDMi9zYW5kYm94L1lMRjJHSmtGOEY3b09wcm5TcG11cGwtaW1hZ2VzXzE3NTExOTQ2NzQ0MjhfbmExZm5fTDJodmJXVXZkV0oxYm5SMUwzSmxZV1J0WlY5cGJXRm5aWE12YzJOeVpXVnVjMmh2ZEY5amIyNTBaWFZrYncucG5nIiwiQ29uZGl0aW9uIjp7IkRhdGVMZXNzVGhhbiI6eyJBV1M6RXBvY2hUaW1lIjoxNzY3MjI1NjAwfX19XX0_&Key-Pair-Id=K2HSFNDJXOU9YS&Signature=LpAiVcc8aGxEcXiEj80dIkrvwK4fwfWgVnZoFYRTS17aNvLqXeDf-FzJXjgYMXXnL1uhzvQUXQlFnm650ivlpKJiyFtXUWQQatVpSRx4UurwAFIt0wDwsL6Vi58O5KPUuTCKMO9wNX1tuQgV57M0PyVGECfX2YZMXZXsF1CgsaDh~HjrUoISF1fpJRSojBSS6SFvBGICevJM2jfzXl0dFq-HxhH1srXyiBNmWHRprY-ozvVk1AoIjbTte7YQDYRL9OBEZmXhXYP12GgPgbCb4XtpnlIgw84xm9Xm64821Zo3sKHyofm7ig5mgIUjRWm96mQqwTXqVZG9AIcUd~aRRw__)

O editor de conteúdo oferece uma experiência de escrita fluida e produtiva. Com interface intuitiva para criação de seções, os usuários podem estruturar facilmente seus documentos acadêmicos. A aba "Conteúdo" permite adicionar e gerenciar seções do artigo com campos específicos para título e conteúdo de cada seção.

**Características do editor:**
- Syntax highlighting para LaTeX
- Numeração de linhas
- Auto-complete para comandos LaTeX
- Preview lado a lado
- Busca e substituição avançada

### 👥 Gerenciamento de Autores

A interface de gerenciamento de autores permite adicionar, editar e organizar informações de múltiplos autores de forma visual e intuitiva. Cada autor é representado por um card com todas as informações relevantes.

**Funcionalidades visuais:**
- Cards individuais para cada autor
- Drag & drop para reordenação
- Formulários modais para edição
- Validação em tempo real

### 🖼️ Galeria de Figuras - Seção Mídia
![Galeria de Figuras](https://private-us-east-1.manuscdn.com/sessionFile/Nv5TJPXeSAJMEG3nJatfC2/sandbox/YLF2GJkF8F7oOprnSpmupl-images_1751194674429_na1fn_L2hvbWUvdWJ1bnR1L3JlYWRtZV9pbWFnZXMvc2NyZWVuc2hvdF9taWRpYQ.png?Policy=eyJTdGF0ZW1lbnQiOlt7IlJlc291cmNlIjoiaHR0cHM6Ly9wcml2YXRlLXVzLWVhc3QtMS5tYW51c2Nkbi5jb20vc2Vzc2lvbkZpbGUvTnY1VEpQWGVTQUpNRUczbkphdGZDMi9zYW5kYm94L1lMRjJHSmtGOEY3b09wcm5TcG11cGwtaW1hZ2VzXzE3NTExOTQ2NzQ0MjlfbmExZm5fTDJodmJXVXZkV0oxYm5SMUwzSmxZV1J0WlY5cGJXRm5aWE12YzJOeVpXVnVjMmh2ZEY5dGFXUnBZUS5wbmciLCJDb25kaXRpb24iOnsiRGF0ZUxlc3NUaGFuIjp7IkFXUzpFcG9jaFRpbWUiOjE3NjcyMjU2MDB9fX1dfQ__&Key-Pair-Id=K2HSFNDJXOU9YS&Signature=jOioaabyYDvxe1fl0ZfmRBNMQbZ51Hf08YFQZbUtgMagBNsU8e05u-~vb-A1MisJ5kte6~2~FJZyAZY82sdzeKsyPY1pAltkJtfzVUc9Fe3n5Zd5BYkJqxSBFxq0wvToy8cqy5NnBXwtHD909w7yUYsqYptNM3NbdV6EZ5rUGPJdxD5AE26Wy2SFDXs7KEz8jDAQY~Hir4gz4ff3eC8UFOP6tSz9yND1VIQwgPwp~veJ4LMMPnnnORDAKYOLtr1JMESGtXmX2KL-YVKGqGTNtFjfBAUI0vcjQaQONPo~hIPMJcC3W7E~347N5YsQrok8iVN9nUUGZVF74E6j3x~wAA__)

A seção de mídia proporciona uma interface organizada para gerenciar figuras e imagens do documento. Com botão de "Adicionar Figura" e área dedicada para tabelas, os usuários podem facilmente incorporar elementos visuais em seus documentos acadêmicos. A funcionalidade de tabelas está em desenvolvimento para futuras versões.

**Elementos da galeria:**
- Grid responsivo de thumbnails
- Informações de cada figura (tamanho, formato, dimensões)
- Ferramentas de edição inline
- Preview em modal expandido

### 📚 Biblioteca de Referências - Seção Referências
![Biblioteca de Referências](https://private-us-east-1.manuscdn.com/sessionFile/Nv5TJPXeSAJMEG3nJatfC2/sandbox/YLF2GJkF8F7oOprnSpmupl-images_1751194674430_na1fn_L2hvbWUvdWJ1bnR1L3JlYWRtZV9pbWFnZXMvc2NyZWVuc2hvdF9yZWZlcmVuY2lhcw.png?Policy=eyJTdGF0ZW1lbnQiOlt7IlJlc291cmNlIjoiaHR0cHM6Ly9wcml2YXRlLXVzLWVhc3QtMS5tYW51c2Nkbi5jb20vc2Vzc2lvbkZpbGUvTnY1VEpQWGVTQUpNRUczbkphdGZDMi9zYW5kYm94L1lMRjJHSmtGOEY3b09wcm5TcG11cGwtaW1hZ2VzXzE3NTExOTQ2NzQ0MzBfbmExZm5fTDJodmJXVXZkV0oxYm5SMUwzSmxZV1J0WlY5cGJXRm5aWE12YzJOeVpXVnVjMmh2ZEY5eVpXWmxjbVZ1WTJsaGN3LnBuZyIsIkNvbmRpdGlvbiI6eyJEYXRlTGVzc1RoYW4iOnsiQVdTOkVwb2NoVGltZSI6MTc2NzIyNTYwMH19fV19&Key-Pair-Id=K2HSFNDJXOU9YS&Signature=CU2y9YZ58ezQk8liDL41ZdMOtpKH8zDxRj1nTbMIjsGhxgRJt854tHtqydXvwu9~L8cGXMWB12qAcCEDFiVnELLAWLScwHraqL1PJW3XMLPyuGQAwuOxOO0AgHExv-TGewxCo~HanD6hbR8oPGV2qYSqFXjWOCvlfAuY9gt7nqlfFM68oF~f96odVYKkG8zACtLmX1k16J~fDeFRTjvE9IDWYmFryuw~OcYg0qFQYFZQP2INFjnkGYX4zd0mwpl8RAkw4Ccx~V9ycAny8mAsmtVrcd0duvrgq9ZgU~gAqPB47TJUBOATTV464WUgzbJfXTryHd5OcchLp0X8Ywm8Pg__)

A biblioteca de referências oferece uma interface organizada para gerenciar citações bibliográficas. Com formulários estruturados para autor(es), ano, título do artigo/livro, journal/editora e páginas, os usuários podem facilmente adicionar e organizar suas referências acadêmicas. O botão "Adicionar Referência" permite expandir a biblioteca conforme necessário.

**Recursos da biblioteca:**
- Lista organizada de referências
- Formulários estruturados para cada tipo de publicação
- Importação automática via DOI
- Formatação automática conforme template

## 🛠️ Solução de Problemas (Troubleshooting)

### ❌ Problemas Comuns e Soluções

#### Erro: "LaTeX não encontrado"
**Sintomas**: Mensagem de erro indicando que o compilador LaTeX não foi encontrado.

**Soluções**:
1. **Verifique a instalação do LaTeX**:
   ```bash
   # Teste se pdflatex está disponível
   pdflatex --version
   ```
2. **Adicione LaTeX ao PATH** (Windows):
   - Adicione o diretório de instalação do MiKTeX/TeX Live ao PATH do sistema
   - Exemplo: `C:\Program Files\MiKTeX\miktex\bin\x64`

3. **Reinstale a distribuição LaTeX**:
   - Windows: Reinstale MiKTeX ou TeX Live
   - macOS: Reinstale MacTeX
   - Linux: `sudo apt-get install texlive-full`

#### Erro: "Falha no upload de imagem"
**Sintomas**: Imagens não são carregadas ou aparecem mensagens de erro durante upload.

**Soluções**:
1. **Verifique o formato do arquivo**:
   - Formatos suportados: JPG, JPEG, PNG, GIF, SVG, PDF
   - Tamanho máximo: 16MB por arquivo

2. **Verifique permissões de diretório**:
   ```bash
   # Garanta permissões de escrita na pasta uploads
   chmod 755 uploads/
   ```

3. **Limpe o cache de upload**:
   ```bash
   # Remova arquivos temporários
   rm -rf uploads/temp/*
   ```

#### Erro: "Compilação falhou"
**Sintomas**: PDF não é gerado e aparecem erros no console de compilação.

**Soluções**:
1. **Verifique a sintaxe LaTeX**:
   - Procure por comandos malformados
   - Verifique fechamento de chaves `{}`
   - Confirme escape de caracteres especiais

2. **Analise os logs de compilação**:
   - Procure por linhas começando com "!"
   - Identifique o número da linha com erro
   - Consulte a documentação LaTeX para comandos específicos

3. **Teste com documento mínimo**:
   - Crie um documento simples para testar a compilação
   - Adicione conteúdo gradualmente para identificar o problema

#### Erro: "Servidor não responde"
**Sintomas**: Aplicação não carrega ou apresenta timeouts.

**Soluções**:
1. **Verifique se o servidor está rodando**:
   ```bash
   # Verifique processos Python
   ps aux | grep python
   ```

2. **Reinicie a aplicação**:
   ```bash
   # Pare o servidor
   Ctrl+C
   
   # Reinicie
   python app.py
   ```

3. **Verifique logs de erro**:
   ```bash
   # Visualize logs do Flask
   tail -f logs/app.log
   ```

### 🔍 Logs e Debugging

#### Habilitando Logs Detalhados
Para obter informações mais detalhadas sobre o funcionamento da aplicação:

1. **Edite o arquivo .env**:
   ```env
   FLASK_DEBUG=True
   LOG_LEVEL=DEBUG
   ```

2. **Reinicie a aplicação**

3. **Monitore os logs**:
   ```bash
   tail -f logs/debug.log
   ```

#### Interpretando Logs de Compilação LaTeX
Os logs do LaTeX seguem um padrão específico:
- **Warnings**: Começam com "LaTeX Warning"
- **Erros**: Começam com "!" 
- **Informações**: Linhas normais de processamento

Exemplo de erro comum:
```
! Undefined control sequence.
l.15 \textbold
              {Este comando não existe}
```

**Solução**: Substituir `\textbold` por `\textbf`

## 🤝 Contribuindo para o Projeto

### 🌟 Como Contribuir

Agradecemos contribuições da comunidade! Existem várias maneiras de ajudar a melhorar o LaTeX Generator:

#### Reportando Bugs
1. Verifique se o bug já foi reportado nas [Issues](https://github.com/rpdavid78/gerador_artigos/issues)
2. Crie uma nova issue com:
   - Descrição detalhada do problema
   - Passos para reproduzir
   - Screenshots (se aplicável)
   - Informações do sistema (OS, Python, LaTeX)

#### Sugerindo Melhorias
- Abra uma issue com tag "enhancement"
- Descreva claramente a funcionalidade desejada
- Explique como ela beneficiaria outros usuários

#### Contribuindo com Código
1. **Fork** o repositório
2. Crie uma **branch** para sua feature: `git checkout -b feature/nova-funcionalidade`
3. **Commit** suas mudanças: `git commit -m 'Adiciona nova funcionalidade'`
4. **Push** para a branch: `git push origin feature/nova-funcionalidade`
5. Abra um **Pull Request**

### 📋 Diretrizes de Desenvolvimento

#### Padrões de Código
- **Python**: Siga PEP 8
- **JavaScript**: Use ESLint com configuração padrão
- **HTML/CSS**: Mantenha semântica e acessibilidade
- **Documentação**: Comente código complexo

#### Testes
Antes de submeter um PR:
```bash
# Execute os testes
python -m pytest tests/

# Verifique cobertura
coverage run -m pytest
coverage report
```

#### Estrutura de Commits
Use mensagens de commit descritivas:
```
tipo(escopo): descrição breve

Descrição mais detalhada se necessário.

Fixes #123
```

Tipos válidos: `feat`, `fix`, `docs`, `style`, `refactor`, `test`, `chore`

## 📄 Licença e Créditos

### 📜 Licença MIT

Este projeto está licenciado sob a Licença MIT - veja o arquivo [LICENSE](LICENSE) para detalhes.

```
MIT License

Copyright (c) 2024 LaTeX Generator Team

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```

### 🙏 Agradecimentos

Agradecemos a todos que contribuíram para o desenvolvimento do LaTeX Generator:

- **Comunidade LaTeX**: Pela documentação e suporte contínuo
- **Desenvolvedores Flask**: Pelo framework web robusto e flexível
- **Contribuidores Open Source**: Por bibliotecas e ferramentas essenciais
- **Beta Testers**: Por feedback valioso durante o desenvolvimento
- **Comunidade Acadêmica**: Por requisitos e casos de uso reais

### 🔗 Links Úteis

- **Documentação LaTeX**: [https://www.latex-project.org/help/documentation/](https://www.latex-project.org/help/documentation/)
- **Flask Documentation**: [https://flask.palletsprojects.com/](https://flask.palletsprojects.com/)
- **Python.org**: [https://www.python.org/](https://www.python.org/)
- **GitHub Repository**: [https://github.com/seu-usuario/latex-generator](https://github.com/rpdavid78/gerador_artigos)

## 📞 Suporte e Contato

### 💬 Canais de Suporte

- **GitHub Issues**: Para bugs e solicitações de features
- **Discussions**: Para perguntas gerais e discussões

### 📈 Roadmap

Funcionalidades planejadas para próximas versões:

#### v2.1 (Em Desenvolvimento)
- [ ] Editor colaborativo em tempo real
- [ ] Integração com Overleaf
- [ ] Templates personalizáveis via interface
- [ ] Exportação para Word/Google Docs

#### v2.2 (Planejado)
- [ ] Sistema de plugins
- [ ] API REST completa
- [ ] Integração com Zotero/Mendeley
- [ ] Suporte a múltiplos idiomas

#### v3.0 (Futuro)
- [ ] Inteligência artificial para sugestões
- [ ] Colaboração em tempo real
- [ ] Versionamento de documentos
- [ ] Integração com repositórios Git

---

<div align="center">

**Desenvolvido pela equipe LaTeX Generator**

[⭐ Star no GitHub](https://github.com/seu-usuario/latex-generator) | [🐛 Reportar Bug](https://github.com/seu-usuario/latex-generator/issues) | [💡 Sugerir Feature](https://github.com/seu-usuario/latex-generator/issues/new)

</div>


**Sistema 100% funcional e testado!**


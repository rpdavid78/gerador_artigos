#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Servidor Flask para Gerador de Artigos LaTeX v2.0 - VERSÃO CORRIGIDA
Autor: Manus AI
"""

import os
import json
import uuid
import time
from pathlib import Path
from flask import Flask, request, jsonify, send_file, send_from_directory
from flask_cors import CORS
from werkzeug.utils import secure_filename
import tempfile
import shutil
import logging

# Configurar logging
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

# Importar a classe do gerador
from latex_generator_v2 import LatexGeneratorV2

app = Flask(__name__)
CORS(app)

# Configurações
UPLOAD_FOLDER = Path('uploads')
CACHE_FOLDER = Path('cache')
OUTPUT_FOLDER = Path('output')

# Criar diretórios
for folder in [UPLOAD_FOLDER, CACHE_FOLDER, OUTPUT_FOLDER]:
    folder.mkdir(exist_ok=True)

# Extensões permitidas para upload
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif', 'pdf', 'eps', 'svg'}

def allowed_file(filename):
    """Verifica se o arquivo tem extensão permitida."""
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/')
def index():
    """Página inicial - serve o frontend."""
    return send_from_directory('static', 'index.html')

@app.route('/<path:path>')
def serve_static(path):
    """Servir arquivos estáticos do frontend."""
    try:
        return send_from_directory('static', path)
    except:
        # Se o arquivo não existir, serve o index.html (para SPA routing)
        return send_from_directory('static', 'index.html')

@app.route('/api/info')
def api_info():
    """Informações da API."""
    return jsonify({
        'message': 'LaTeX Generator v2.0 API - VERSÃO CORRIGIDA',
        'version': '2.0-fixed',
        'endpoints': {
            'preview': '/api/preview',
            'generate': '/api/generate',
            'upload': '/api/upload',
            'download': '/api/download/<filename>',
            'templates': '/api/templates',
            'save_project': '/api/save',
            'load_project': '/api/load/<project_id>'
        }
    })

@app.route('/api/templates', methods=['GET'])
def get_templates():
    """Retorna lista de templates disponíveis."""
    templates = {
        'basic': {
            'name': 'Básico',
            'description': 'Template básico para artigos acadêmicos',
            'features': ['Estrutura simples', 'Fácil personalização']
        },
        'ieee': {
            'name': 'IEEE Conference',
            'description': 'Template para conferências IEEE',
            'features': ['Formato IEEE', 'Duas colunas', 'Bibliografia IEEE']
        },
        'acm': {
            'name': 'ACM Article',
            'description': 'Template para artigos ACM',
            'features': ['Formato ACM', 'Layout profissional', 'Metadados completos']
        },
        'abnt': {
            'name': 'ABNT (Brasil)',
            'description': 'Template seguindo normas ABNT',
            'features': ['Normas ABNT', 'Português brasileiro', 'Formatação acadêmica']
        }
    }
    return jsonify(templates)

@app.route('/api/preview', methods=['POST'])
def generate_preview():
    """Gera prévia do código LaTeX."""
    try:
        data = request.json
        logger.debug(f"Dados recebidos para preview: {json.dumps(data, indent=2, ensure_ascii=False)}")
        
        # Criar instância do gerador
        generator = LatexGeneratorV2()
        
        # Configurar template
        if data.get('template'):
            logger.debug(f"Configurando template: {data['template']}")
            generator.set_template(data['template'])
        
        # Configurar dados básicos do documento
        generator.set_document_info(
            title=data.get('title', ''),
            abstract=data.get('abstract', ''),
            keywords=data.get('keywords', '')
        )
        logger.debug(f"Configurado: título='{data.get('title', '')}', abstract={len(data.get('abstract', ''))} chars")
        
        # Adicionar autores
        authors_count = 0
        for author in data.get('authors', []):
            if author.get('name'):
                logger.debug(f"Adicionando autor: {author['name']}")
                generator.add_author(
                    author['name'],
                    author.get('affiliation', ''),
                    author.get('email', '')
                )
                authors_count += 1
        logger.debug(f"Total de autores adicionados: {authors_count}")
        
        # Adicionar seções - PONTO CRÍTICO
        sections_count = 0
        sections_data = data.get('sections', [])
        logger.debug(f"Processando {len(sections_data)} seções recebidas")
        
        for i, section in enumerate(sections_data):
            logger.debug(f"Seção {i+1}: título='{section.get('title', '')}', conteúdo={len(section.get('content', ''))} chars")
            
            # Verificar se seção tem dados válidos
            title = section.get('title', '').strip()
            content = section.get('content', '').strip()
            
            if title and content:
                logger.debug(f"Adicionando seção válida: {title}")
                generator.add_section(
                    title,
                    content,
                    section.get('level', 1)
                )
                sections_count += 1
            else:
                logger.warning(f"Seção {i+1} ignorada - título ou conteúdo vazio (título: '{title}', conteúdo: {len(content)} chars)")
        
        logger.debug(f"Total de seções adicionadas: {sections_count}")
        
        # Adicionar figuras
        figures_count = 0
        for figure in data.get('figures', []):
            if figure.get('path'):
                logger.debug(f"Adicionando figura: {figure['path']}")
                generator.add_figure(
                    figure['path'],
                    figure.get('caption', ''),
                    figure.get('label', ''),
                    figure.get('width', '0.8\\textwidth')
                )
                figures_count += 1
        logger.debug(f"Total de figuras adicionadas: {figures_count}")
        
        # Adicionar tabelas
        tables_count = 0
        for table in data.get('tables', []):
            if table.get('data'):
                logger.debug(f"Adicionando tabela")
                generator.add_table(
                    table['data'],
                    table.get('caption', ''),
                    table.get('label', '')
                )
                tables_count += 1
        logger.debug(f"Total de tabelas adicionadas: {tables_count}")
        
        # Adicionar referências
        references_count = 0
        for ref in data.get('references', []):
            if ref.get('author') and ref.get('title'):
                logger.debug(f"Adicionando referência: {ref['author']} - {ref['title']}")
                generator.add_reference(
                    ref.get('type', 'article'),
                    author=ref.get('author', ''),
                    title=ref.get('title', ''),
                    journal=ref.get('journal', ''),
                    year=ref.get('year', ''),
                    publisher=ref.get('publisher', ''),
                    conference=ref.get('conference', '')
                )
                references_count += 1
        logger.debug(f"Total de referências adicionadas: {references_count}")
        
        # Verificar estado interno do gerador
        logger.debug(f"Estado interno do gerador:")
        logger.debug(f"  - Seções: {len(generator.sections)}")
        logger.debug(f"  - Autores: {len(generator.authors)}")
        logger.debug(f"  - Figuras: {len(generator.figures)}")
        logger.debug(f"  - Referências: {len(generator.references)}")
        
        # Gerar código LaTeX
        logger.debug("Gerando código LaTeX...")
        latex_code = generator.generate_latex()
        logger.debug(f"Código LaTeX gerado: {len(latex_code)} chars")
        
        # Verificar se seções estão no LaTeX
        for section in sections_data:
            title = section.get('title', '')
            if title and title in latex_code:
                logger.debug(f"✓ Seção '{title}' encontrada no LaTeX")
            elif title:
                logger.warning(f"✗ Seção '{title}' NÃO encontrada no LaTeX")
        
        return jsonify({
            'success': True,
            'latex_code': latex_code,
            'template': data.get('template', 'basic'),
            'debug_info': {
                'sections_received': len(sections_data),
                'sections_processed': sections_count,
                'authors_processed': authors_count,
                'figures_processed': figures_count,
                'references_processed': references_count
            }
        })
        
    except Exception as e:
        logger.error(f"Erro ao gerar prévia: {str(e)}", exc_info=True)
        return jsonify({
            'success': False,
            'message': f'Erro ao gerar prévia: {str(e)}'
        }), 500

@app.route('/api/generate', methods=['POST'])
def generate_article():
    """Gera o artigo completo (LaTeX + PDF)."""
    try:
        data = request.json
        logger.debug(f"Dados recebidos para geração: {json.dumps(data, indent=2, ensure_ascii=False)}")
        
        # Criar instância do gerador com diretório de saída
        generator = LatexGeneratorV2(output_dir=str(OUTPUT_FOLDER))
        
        # Configurar template
        if data.get('template'):
            generator.set_template(data['template'])
        
        # Configurar dados básicos do documento
        generator.set_document_info(
            title=data.get('title', ''),
            abstract=data.get('abstract', ''),
            keywords=data.get('keywords', '')
        )
        
        # Adicionar autores
        for author in data.get('authors', []):
            if author.get('name'):
                generator.add_author(
                    author['name'],
                    author.get('affiliation', ''),
                    author.get('email', '')
                )
        
        # Adicionar seções
        sections_data = data.get('sections', [])
        logger.debug(f"Processando {len(sections_data)} seções para geração")
        
        for section in sections_data:
            title = section.get('title', '').strip()
            content = section.get('content', '').strip()
            
            if title and content:
                generator.add_section(
                    title,
                    content,
                    section.get('level', 1)
                )
        
        # Adicionar figuras
        for figure in data.get('figures', []):
            if figure.get('path'):
                generator.add_figure(
                    figure['path'],
                    figure.get('caption', ''),
                    figure.get('label', ''),
                    figure.get('width', '0.8\\textwidth')
                )
        
        # Adicionar tabelas
        for table in data.get('tables', []):
            if table.get('data'):
                generator.add_table(
                    table['data'],
                    table.get('caption', ''),
                    table.get('label', '')
                )
        
        # Adicionar referências
        for ref in data.get('references', []):
            if ref.get('author') and ref.get('title'):
                generator.add_reference(
                    author=ref.get('author', ''),
                    title=ref.get('title', ''),
                    journal=ref.get('journal', ''),
                    year=ref.get('year', ''),
                    pages=ref.get('pages', ''),
                    doi=ref.get('doi', '')
                )
        
        # Gerar nome único para o documento
        doc_id = str(uuid.uuid4())[:8]
        output_name = f"article_{doc_id}"
        
        # Compilar para PDF
        success, message, files = generator.compile_to_pdf(output_name)
        
        if success:
            pdf_filename = f"{output_name}.pdf"
            latex_filename = f"{output_name}.tex"
            
            return jsonify({
                'success': True,
                'message': f'PDF gerado com sucesso! Total: {len(generator.sections)} seções processadas',
                'document_id': doc_id,
                'pdf_filename': pdf_filename,
                'latex_filename': latex_filename,
                'download_pdf_url': f'/api/download/{pdf_filename}',
                'download_latex_url': f'/api/download/{latex_filename}'
            })
        else:
            # Se falhar na compilação PDF, retornar pelo menos o LaTeX
            latex_code = generator.generate_latex()
            return jsonify({
                'success': False,
                'message': f'Erro na compilação PDF: {message}. Código LaTeX gerado.',
                'latex_code': latex_code
            }), 500
        
    except Exception as e:
        logger.error(f"Erro ao gerar artigo: {str(e)}", exc_info=True)
        return jsonify({
            'success': False,
            'message': f'Erro ao gerar artigo: {str(e)}'
        }), 500

# Manter outros endpoints iguais...
@app.route('/api/upload', methods=['POST'])
def upload_file():
    """Upload de arquivos (imagens, figuras)."""
    try:
        if 'file' not in request.files:
            return jsonify({'success': False, 'message': 'Nenhum arquivo enviado'}), 400
        
        file = request.files['file']
        if file.filename == '':
            return jsonify({'success': False, 'message': 'Nenhum arquivo selecionado'}), 400
        
        if file and allowed_file(file.filename):
            # Gerar nome único para o arquivo
            filename = secure_filename(file.filename)
            unique_filename = f"{uuid.uuid4().hex}_{filename}"
            file_path = UPLOAD_FOLDER / unique_filename
            
            # Salvar arquivo
            file.save(file_path)
            
            return jsonify({
                'success': True,
                'message': 'Arquivo enviado com sucesso',
                'file_id': unique_filename,
                'file_path': str(file_path),
                'original_name': filename
            })
        
        return jsonify({'success': False, 'message': 'Tipo de arquivo não permitido'}), 400
        
    except Exception as e:
        return jsonify({'success': False, 'message': f'Erro no upload: {str(e)}'}), 500

@app.route('/api/download/<filename>')
def download_file(filename):
    """Download de arquivos gerados."""
    try:
        file_path = OUTPUT_FOLDER / filename
        if file_path.exists():
            return send_file(file_path, as_attachment=True)
        else:
            return jsonify({'success': False, 'message': 'Arquivo não encontrado'}), 404
    except Exception as e:
        return jsonify({'success': False, 'message': f'Erro no download: {str(e)}'}), 500

# ==========================================
# FUNCIONALIDADE DE UPLOAD DE IMAGENS
# ==========================================

import os
from werkzeug.utils import secure_filename

# Configuração de upload
UPLOAD_FOLDER = os.path.join(os.path.dirname(__file__), 'uploads')
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif', 'bmp', 'svg'}

# Criar diretório de upload se não existir
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

def allowed_file(filename):
    """Verificar se o arquivo tem extensão permitida."""
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/api/upload/image', methods=['POST'])
def upload_image():
    """Upload de imagem para uso no artigo."""
    try:
        if 'image' not in request.files:
            return jsonify({'success': False, 'message': 'Nenhum arquivo enviado'}), 400
        
        file = request.files['image']
        
        if file.filename == '':
            return jsonify({'success': False, 'message': 'Nenhum arquivo selecionado'}), 400
        
        if not allowed_file(file.filename):
            return jsonify({'success': False, 'message': 'Tipo de arquivo não permitido'}), 400
        
        # Gerar nome seguro para o arquivo
        filename = secure_filename(file.filename)
        timestamp = str(int(time.time()))
        filename = f"{timestamp}_{filename}"
        
        # Salvar arquivo
        file_path = os.path.join(UPLOAD_FOLDER, filename)
        file.save(file_path)
        
        logger.debug(f"✅ Imagem salva: {file_path}")
        
        return jsonify({
            'success': True,
            'message': 'Imagem carregada com sucesso',
            'filename': filename,
            'path': file_path,
            'url': f'/api/uploads/{filename}'
        })
        
    except Exception as e:
        logger.error(f"❌ Erro no upload: {str(e)}")
        return jsonify({'success': False, 'message': f'Erro no upload: {str(e)}'}), 500

@app.route('/api/uploads/<filename>')
def uploaded_file(filename):
    """Servir arquivos de upload."""
    try:
        return send_from_directory(UPLOAD_FOLDER, filename)
    except Exception as e:
        logger.error(f"❌ Erro ao servir arquivo: {str(e)}")
        return jsonify({'success': False, 'message': 'Arquivo não encontrado'}), 404

# ==========================================
# FUNCIONALIDADE DE IA COM GEMINI
# ==========================================

import requests
import json

# Configuração da API do Gemini
GEMINI_API_KEY = "AIzaSyCS1TDbDVXjqmnGppqYsBaGt1XC_vh-bDk"
GEMINI_API_URL = "https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash:generateContent"

@app.route('/api/ai/generate', methods=['POST'])
def generate_ai_content():
    """Gerar conteúdo usando IA Gemini."""
    try:
        data = request.get_json()
        prompt = data.get('prompt', '')
        content_type = data.get('content_type', 'text')
        context = data.get('context', {})
        
        if not prompt:
            return jsonify({'success': False, 'error': 'Prompt é obrigatório'}), 400
        
        logger.debug(f"🤖 Gerando conteúdo IA - Tipo: {content_type}, Prompt: {prompt[:100]}...")
        
        # Preparar prompt baseado no tipo de conteúdo
        enhanced_prompt = prepare_prompt(prompt, content_type, context)
        
        # Fazer chamada para API do Gemini
        response = call_gemini_api(enhanced_prompt)
        
        if response['success']:
            logger.debug(f"✅ Conteúdo gerado com sucesso: {len(response['content'])} chars")
            return jsonify({
                'success': True,
                'content': response['content'],
                'type': content_type
            })
        else:
            logger.error(f"❌ Erro na API Gemini: {response['error']}")
            return jsonify({'success': False, 'error': response['error']}), 500
            
    except Exception as e:
        logger.error(f"❌ Erro na geração de IA: {str(e)}")
        return jsonify({'success': False, 'error': f'Erro interno: {str(e)}'}), 500

def prepare_prompt(user_prompt, content_type, context):
    """Preparar prompt otimizado baseado no tipo de conteúdo."""
    
    base_prompts = {
        'title': f"""
Gere um título acadêmico profissional e impactante para um artigo científico.
Prompt do usuário: {user_prompt}
Contexto: {context.get('abstract', '')}

Requisitos:
- Máximo 15 palavras
- Linguagem acadêmica formal
- Específico e descritivo
- Em português

Responda apenas com o título, sem aspas ou formatação extra.
""",
        
        'abstract': f"""
Gere um resumo/abstract acadêmico profissional.
Prompt do usuário: {user_prompt}
Título: {context.get('title', '')}

Requisitos:
- 150-250 palavras
- Estrutura: contexto, objetivo, metodologia, resultados, conclusão
- Linguagem acadêmica formal
- Em português
- Sem referências

Responda apenas com o resumo, sem formatação extra.
""",
        
        'keywords': f"""
Gere palavras-chave acadêmicas relevantes.
Prompt do usuário: {user_prompt}
Título: {context.get('title', '')}
Resumo: {context.get('abstract', '')}

Requisitos:
- 5-7 palavras-chave
- Separadas por vírgula
- Termos técnicos relevantes
- Em português

Responda apenas com as palavras-chave separadas por vírgula.
""",
        
        'section': f"""
Gere conteúdo acadêmico para uma seção de artigo científico.
Prompt do usuário: {user_prompt}
Contexto do artigo: {context.get('title', '')} - {context.get('abstract', '')}

Requisitos:
- 300-500 palavras
- Linguagem acadêmica formal
- Estrutura lógica com parágrafos
- Conteúdo substantivo e técnico
- Em português
- Sem referências numeradas

Responda apenas com o conteúdo da seção, sem título.
"""
    }
    
    return base_prompts.get(content_type, f"Gere conteúdo acadêmico sobre: {user_prompt}")

def call_gemini_api(prompt):
    """Fazer chamada para API do Gemini."""
    try:
        headers = {
            'Content-Type': 'application/json',
        }
        
        payload = {
            "contents": [{
                "parts": [{
                    "text": prompt
                }]
            }],
            "generationConfig": {
                "temperature": 0.7,
                "topK": 40,
                "topP": 0.95,
                "maxOutputTokens": 1024,
            }
        }
        
        url = f"{GEMINI_API_URL}?key={GEMINI_API_KEY}"
        
        response = requests.post(url, headers=headers, json=payload, timeout=30)
        
        if response.status_code == 200:
            result = response.json()
            
            if 'candidates' in result and len(result['candidates']) > 0:
                content = result['candidates'][0]['content']['parts'][0]['text']
                return {'success': True, 'content': content.strip()}
            else:
                return {'success': False, 'error': 'Resposta vazia da API'}
        else:
            error_msg = f"HTTP {response.status_code}: {response.text}"
            return {'success': False, 'error': error_msg}
            
    except requests.exceptions.Timeout:
        return {'success': False, 'error': 'Timeout na API do Gemini'}
    except requests.exceptions.RequestException as e:
        return {'success': False, 'error': f'Erro de conexão: {str(e)}'}
    except Exception as e:
        return {'success': False, 'error': f'Erro inesperado: {str(e)}'}

@app.route('/api/ai/status', methods=['GET'])
def ai_status():
    """Verificar status da IA."""
    return jsonify({
        'success': True,
        'ai_enabled': True,
        'provider': 'Google Gemini',
        'version': 'gemini-pro'
    })

if __name__ == '__main__':
    print("🚀 Iniciando LaTeX Generator v2.0 - VERSÃO CORRIGIDA...")
    print("📍 API: http://localhost:5000")
    print("📍 Frontend: http://localhost:5173")
    print("⏹️  Para parar: Ctrl+C")
    print()
    
    app.run(host='0.0.0.0', port=5000, debug=True)


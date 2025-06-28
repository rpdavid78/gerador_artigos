#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
LaTeX Generator v2.1 - VERSÃO COM FIGURAS CORRIGIDA
Gerador avançado de documentos LaTeX para artigos acadêmicos
CORREÇÃO: Problema das figuras com caption/filename trocados
"""

import re
import uuid
import datetime
import os
import shutil
import hashlib
import subprocess
import tempfile
from pathlib import Path
from typing import Dict, List, Optional, Any, Tuple

class LatexGeneratorV2:
    """
    Gerador LaTeX v2.1 que processa todas as seções e figuras corretamente
    CORREÇÃO PRINCIPAL: Validação robusta de dados das figuras
    """
    
    def __init__(self, output_dir: str = None, cache_dir: str = None):
        """
        Inicializa o gerador versão 2.1.
        
        Args:
            output_dir: Diretório de saída
            cache_dir: Diretório de cache
        """
        self.output_dir = Path(output_dir) if output_dir else Path.cwd() / "output"
        self.cache_dir = Path(cache_dir) if cache_dir else Path.cwd() / "cache"
        self.uploads_dir = Path.cwd() / "uploads"
        
        # Criar diretórios
        for dir_path in [self.output_dir, self.cache_dir, self.uploads_dir]:
            dir_path.mkdir(exist_ok=True)
        self.document_data = {}
        self.template_type = 'basic'
        self.sections = []
        self.authors = []
        self.references = []
        self.figures = []
        
        # Templates disponíveis
        self.templates = {
            'basic': self._get_basic_template(),
            'ieee': self._get_ieee_template(),
            'acm': self._get_acm_template(),
            'abnt': self._get_abnt_template()
        }
    
    def set_template(self, template_type: str):
        """Definir o tipo de template"""
        if template_type in self.templates:
            self.template_type = template_type
            return True
        return False
    
    def set_document_info(self, title: str, abstract: str = "", keywords: str = ""):
        """Definir informações básicas do documento"""
        self.document_data.update({
            'title': title,
            'abstract': abstract,
            'keywords': keywords
        })
    
    def set_keywords(self, keywords: str):
        """Definir palavras-chave do documento"""
        self.document_data['keywords'] = keywords
    
    def add_author(self, name: str, affiliation: str = "", email: str = ""):
        """Adicionar autor ao documento"""
        author = {
            'name': name,
            'affiliation': affiliation,
            'email': email
        }
        self.authors.append(author)
    
    def clear_authors(self):
        """Limpar lista de autores"""
        self.authors = []
    
    def add_section(self, title: str, content: str, level: int = 1):
        """Adicionar seção ao documento"""
        section = {
            'title': title,
            'content': content,
            'level': level
        }
        self.sections.append(section)
    
    def clear_sections(self):
        """Limpar lista de seções"""
        self.sections = []
    
    def add_reference(self, author: str, title: str, journal: str = "", 
                     year: str = "", pages: str = "", doi: str = ""):
        """Adicionar referência bibliográfica"""
        reference = {
            'author': author,
            'title': title,
            'journal': journal,
            'year': year,
            'pages': pages,
            'doi': doi
        }
        self.references.append(reference)
    
    def clear_references(self):
        """Limpar lista de referências"""
        self.references = []
    
    def add_figure(self, caption: str, label: str, filename: str, width: str = "0.8\\textwidth"):
        """
        Adicionar figura ao documento - VERSÃO CORRIGIDA v2.1
        
        CORREÇÃO PRINCIPAL: Validação robusta dos dados das figuras
        Detecta automaticamente se os dados estão trocados e corrige
        """
        print(f"DEBUG: add_figure recebido - caption='{caption}', label='{label}', filename='{filename}'")
        
        # CORREÇÃO: Detectar se os dados estão trocados
        corrected_caption, corrected_label, corrected_filename = self._validate_and_fix_figure_data(
            caption, label, filename
        )
        
        figure = {
            'caption': corrected_caption,
            'label': corrected_label,
            'filename': corrected_filename,
            'width': width
        }
        
        print(f"DEBUG: add_figure corrigido - caption='{corrected_caption}', label='{corrected_label}', filename='{corrected_filename}'")
        
        self.figures.append(figure)
    
    def _validate_and_fix_figure_data(self, caption: str, label: str, filename: str) -> Tuple[str, str, str]:
        """
        NOVA FUNÇÃO v2.1: Validar e corrigir dados das figuras
        
        Detecta automaticamente quando os dados estão nos campos errados:
        - Se caption contém caminho de arquivo, move para filename
        - Se filename está vazio, usa caption como filename
        - Gera caption e label padrão quando necessário
        """
        
        # Detectar se caption contém um caminho de arquivo
        is_caption_a_path = (
            caption and 
            ('/' in caption or '\\' in caption) and
            any(caption.lower().endswith(ext) for ext in ['.jpg', '.jpeg', '.png', '.gif', '.bmp', '.tiff', '.svg'])
        )
        
        # Detectar se filename está vazio ou inválido
        is_filename_empty = not filename or filename.strip() == ""
        
        # CORREÇÃO AUTOMÁTICA DOS DADOS
        if is_caption_a_path and is_filename_empty:
            # CASO 1: Caption contém o caminho, filename está vazio
            print(f"DEBUG: Detectado dados trocados - movendo '{caption}' de caption para filename")
            corrected_filename = caption
            corrected_caption = f"Figura {len(self.figures) + 1}"  # Caption padrão
            corrected_label = label if label else f"fig:{len(self.figures) + 1}"
            
        elif is_caption_a_path and not is_filename_empty:
            # CASO 2: Caption contém caminho E filename também tem valor
            print(f"DEBUG: Caption parece ser caminho, mas filename também existe - usando filename")
            corrected_filename = filename
            corrected_caption = f"Figura {len(self.figures) + 1}"
            corrected_label = label if label else f"fig:{len(self.figures) + 1}"
            
        elif not is_caption_a_path and is_filename_empty:
            # CASO 3: Caption é texto normal, mas filename está vazio
            print(f"DEBUG: Filename vazio - gerando filename padrão")
            corrected_filename = f"figura_{len(self.figures) + 1}.jpg"  # Filename padrão
            corrected_caption = caption if caption else f"Figura {len(self.figures) + 1}"
            corrected_label = label if label else f"fig:{len(self.figures) + 1}"
            
        else:
            # CASO 4: Dados parecem estar corretos
            corrected_filename = filename
            corrected_caption = caption if caption else f"Figura {len(self.figures) + 1}"
            corrected_label = label if label else f"fig:{len(self.figures) + 1}"
        
        return corrected_caption, corrected_label, corrected_filename
    
    def clear_figures(self):
        """Limpar lista de figuras"""
        self.figures = []
    
    def generate_latex(self) -> str:
        """
        Gerar código LaTeX completo - VERSÃO CORRIGIDA v2.1
        """
        template = self.templates[self.template_type]
        
        # Substituir placeholders básicos
        latex_code = template.replace('{{TITLE}}', self.document_data.get('title', ''))
        latex_code = latex_code.replace('{{ABSTRACT}}', self.document_data.get('abstract', ''))
        latex_code = latex_code.replace('{{KEYWORDS}}', self.document_data.get('keywords', ''))
        
        # Processar autores
        authors_latex = self._format_authors()
        latex_code = latex_code.replace('{{AUTHORS}}', authors_latex)
        
        # Processar seções
        sections_latex = self._format_sections()
        latex_code = latex_code.replace('{{SECTIONS}}', sections_latex)
        
        # Processar figuras - VERSÃO CORRIGIDA v2.1
        figures_latex = self._format_figures()
        latex_code = latex_code.replace('{{FIGURES}}', figures_latex)
        
        # Processar referências
        references_latex = self._format_references()
        latex_code = latex_code.replace('{{REFERENCES}}', references_latex)
        
        return latex_code
    
    def _format_authors(self) -> str:
        """Formatar autores para LaTeX"""
        if not self.authors:
            return ""
        
        authors_list = []
        for author in self.authors:
            author_str = author['name']
            if author.get('affiliation'):
                author_str += f"\\\\{author['affiliation']}"
            if author.get('email'):
                author_str += f"\\\\\\texttt{{{author['email']}}}"
            authors_list.append(author_str)
        
        return " \\and ".join(authors_list)
    
    def _format_sections(self) -> str:
        """
        Formatar seções para LaTeX - VERSÃO CORRIGIDA
        """
        if not self.sections:
            return ""
        
        sections_latex = []
        
        for i, section in enumerate(self.sections):
            if not section.get('title') or not section.get('content'):
                continue  # Pular seções vazias
                
            title = section['title'].strip()
            content = section['content'].strip()
            level = section.get('level', 1)
            
            # Determinar comando de seção baseado no nível
            if level == 1:
                section_cmd = "\\section"
            elif level == 2:
                section_cmd = "\\subsection"
            elif level == 3:
                section_cmd = "\\subsubsection"
            else:
                section_cmd = "\\paragraph"
            
            # Formatar seção
            section_latex = f"{section_cmd}{{{title}}}\n{content}\n"
            sections_latex.append(section_latex)
        
        return "\n".join(sections_latex)
    
    def _format_figures(self) -> str:
        """
        Formatar figuras para LaTeX - VERSÃO CORRIGIDA v2.1
        
        CORREÇÃO PRINCIPAL: Validação robusta e tratamento de erros
        """
        if not self.figures:
            return ""
        
        figures_latex = []
        for i, figure in enumerate(self.figures):
            try:
                # Extrair dados da figura com validação
                raw_filename = figure.get('filename', '')
                raw_caption = figure.get('caption', '')
                raw_label = figure.get('label', '')
                
                print(f"DEBUG: _format_figures processando figura {i+1}:")
                print(f"  - raw_filename: '{raw_filename}'")
                print(f"  - raw_caption: '{raw_caption}'")
                print(f"  - raw_label: '{raw_label}'")
                
                # VALIDAÇÃO ADICIONAL: Se ainda há problemas, corrigir aqui
                if not raw_filename or raw_filename.strip() == "":
                    print(f"DEBUG: Filename vazio na figura {i+1}, pulando...")
                    continue
                
                # Extrair apenas o nome do arquivo (sem caminho)
                filename = Path(raw_filename).name
                
                # Garantir que temos valores válidos
                caption = raw_caption if raw_caption and not ('/' in raw_caption or '\\' in raw_caption) else f"Figura {i+1}"
                label = raw_label if raw_label else f"fig:{i+1}"
                width = figure.get('width', '0.8\\textwidth')
                
                print(f"DEBUG: _format_figures dados finais:")
                print(f"  - filename: '{filename}'")
                print(f"  - caption: '{caption}'")
                print(f"  - label: '{label}'")
                
                # Gerar código LaTeX da figura
                figure_latex = f"""
\\begin{{figure}}[H]
\\centering
\\includegraphics[width={width}]{{{filename}}}
\\caption{{{caption}}}
\\label{{{label}}}
\\end{{figure}}
"""
                figures_latex.append(figure_latex)
                
            except Exception as e:
                print(f"DEBUG: Erro ao processar figura {i+1}: {e}")
                continue
        
        result = "\n".join(figures_latex)
        print(f"DEBUG: _format_figures resultado final:\n{result}")
        return result
    
    def _format_references(self) -> str:
        """Formatar referências para LaTeX"""
        if not self.references:
            return ""
        
        references_latex = []
        for i, ref in enumerate(self.references, 1):
            ref_str = f"\\bibitem{{ref{i}}} "
            
            if ref.get('author'):
                ref_str += f"{ref['author']}. "
            
            if ref.get('title'):
                ref_str += f"\\textit{{{ref['title']}}}. "
            
            if ref.get('journal'):
                ref_str += f"{ref['journal']}"
                
            if ref.get('year'):
                ref_str += f", {ref['year']}"
                
            if ref.get('pages'):
                ref_str += f", pp. {ref['pages']}"
                
            if ref.get('doi'):
                ref_str += f". DOI: {ref['doi']}"
            
            ref_str += "."
            references_latex.append(ref_str)
        
        return "\n".join(references_latex)
    
    def _get_basic_template(self) -> str:
        """Template básico LaTeX"""
        return """\\documentclass[12pt,a4paper]{article}
\\usepackage[utf8]{inputenc}
\\usepackage[T1]{fontenc}
\\usepackage{geometry}
\\usepackage{amsmath}
\\usepackage{amsfonts}
\\usepackage{amssymb}
\\usepackage{graphicx}
\\usepackage{cite}
\\usepackage{url}
\\usepackage{hyperref}
\\usepackage{float}

\\geometry{margin=2.5cm}

\\title{{{TITLE}}}
\\author{{{AUTHORS}}}
\\date{\\today}

\\begin{document}

\\maketitle

\\begin{abstract}
{{ABSTRACT}}
\\end{abstract}

\\textbf{Palavras-chave:} {{KEYWORDS}}

{{SECTIONS}}

{{FIGURES}}

\\begin{thebibliography}{99}
{{REFERENCES}}
\\end{thebibliography}

\\end{document}"""
    
    def _get_ieee_template(self) -> str:
        """Template IEEE LaTeX (usando classe padrão)"""
        return """\\documentclass[10pt,twocolumn]{article}
\\usepackage[utf8]{inputenc}
\\usepackage[margin=2cm]{geometry}
\\usepackage{amsmath,amssymb,amsfonts}
\\usepackage{graphicx}
\\usepackage{textcomp}
\\usepackage{xcolor}
\\usepackage{cite}
\\usepackage{float}

\\title{{{TITLE}}}
\\author{{{AUTHORS}}}
\\date{{}}

\\begin{document}

\\maketitle

\\begin{abstract}
{{ABSTRACT}}
\\end{abstract}

\\textbf{Index Terms---}{{KEYWORDS}}

{{SECTIONS}}

{{FIGURES}}

\\begin{thebibliography}{1}
{{REFERENCES}}
\\end{thebibliography}

\\end{document}"""
    
    def _get_acm_template(self) -> str:
        """Template ACM LaTeX (usando classe padrão)"""
        return """\\documentclass[11pt]{article}
\\usepackage[utf8]{inputenc}
\\usepackage[margin=2.5cm]{geometry}
\\usepackage{amsmath,amssymb,amsfonts}
\\usepackage{graphicx}
\\usepackage{cite}
\\usepackage{url}
\\usepackage{float}

\\title{{{TITLE}}}
\\author{{{AUTHORS}}}
\\date{{}}

\\begin{document}

\\maketitle

\\begin{abstract}
{{ABSTRACT}}
\\end{abstract}

\\textbf{Keywords:} {{KEYWORDS}}

{{SECTIONS}}

{{FIGURES}}

\\begin{thebibliography}{1}
{{REFERENCES}}
\\end{thebibliography}

\\end{document}"""
    
    def _get_abnt_template(self) -> str:
        """Template ABNT LaTeX (usando classe padrão)"""
        return """\\documentclass[12pt,a4paper]{article}
\\usepackage[utf8]{inputenc}
\\usepackage[brazil]{babel}
\\usepackage[T1]{fontenc}
\\usepackage[margin=3cm]{geometry}
\\usepackage{amsmath}
\\usepackage{amsfonts}
\\usepackage{amssymb}
\\usepackage{graphicx}
\\usepackage{cite}
\\usepackage{indentfirst}
\\usepackage{float}

\\title{{{TITLE}}}
\\author{{{AUTHORS}}}
\\date{\\today}

\\begin{document}

\\maketitle

\\begin{abstract}
{{ABSTRACT}}

\\textbf{Palavras-chave:} {{KEYWORDS}}
\\end{abstract}

{{SECTIONS}}

{{FIGURES}}

\\begin{thebibliography}{1}
{{REFERENCES}}
\\end{thebibliography}

\\end{document}"""

    def get_debug_info(self) -> Dict[str, Any]:
        """Obter informações de debug"""
        return {
            'template_type': self.template_type,
            'authors_count': len(self.authors),
            'sections_count': len(self.sections),
            'references_count': len(self.references),
            'figures_count': len(self.figures),
            'sections_processed': len([s for s in self.sections if s.get('title') and s.get('content')]),
            'sections_received': len(self.sections)
        }

    def _copy_figures_to_output(self) -> List[str]:
        """Copiar figuras para o diretório de output e retornar lista de nomes"""
        copied_files = []
        
        for figure in self.figures:
            source_path = Path(figure['filename'])
            
            if source_path.exists():
                # Criar nome seguro para o arquivo (sem espaços)
                safe_name = source_path.name.replace(' ', '_')
                dest_path = self.output_dir / safe_name
                
                try:
                    shutil.copy2(source_path, dest_path)
                    copied_files.append(safe_name)
                    # Atualizar o filename na figura para usar o nome seguro
                    figure['filename'] = safe_name
                except Exception as e:
                    print(f"Erro ao copiar figura {source_path}: {e}")
            else:
                print(f"Arquivo de figura não encontrado: {source_path}")
        
        return copied_files

    def compile_to_pdf(self, output_name: str = "document") -> Tuple[bool, str, Dict[str, Path]]:
        """Compila o documento para PDF."""
        try:
            # Copiar figuras para o diretório de output
            copied_figures = self._copy_figures_to_output()
            
            # Gerar código LaTeX
            latex_code = self.generate_latex()
            
            # Criar arquivo LaTeX temporário
            with tempfile.NamedTemporaryFile(mode='w', suffix='.tex', delete=False, encoding='utf-8') as f:
                f.write(latex_code)
                tex_file = f.name
            
            try:
                # Compilar com pdflatex
                result = subprocess.run([
                    'pdflatex', 
                    '-interaction=nonstopmode',
                    '-output-directory', str(self.output_dir),
                    tex_file
                ], capture_output=True, text=True, timeout=30)
                
                # Verificar se PDF foi gerado
                pdf_name = Path(tex_file).stem + '.pdf'
                pdf_path = self.output_dir / pdf_name
                
                if pdf_path.exists():
                    # Renomear para o nome desejado
                    final_pdf = self.output_dir / f"{output_name}.pdf"
                    final_tex = self.output_dir / f"{output_name}.tex"
                    
                    shutil.move(str(pdf_path), str(final_pdf))
                    shutil.copy2(tex_file, str(final_tex))
                    
                    return True, f"PDF gerado com sucesso. Figuras copiadas: {len(copied_figures)}", {
                        'latex': final_tex,
                        'pdf': final_pdf
                    }
                else:
                    return False, f"Erro na compilação: {result.stderr}", {}
                    
            except subprocess.TimeoutExpired:
                return False, "Timeout na compilação do PDF", {}
            finally:
                # Limpar arquivo temporário
                try:
                    os.unlink(tex_file)
                except:
                    pass
                    
        except Exception as e:
            return False, f"Erro inesperado: {str(e)}", {}
    
    def _get_cache_key(self, content: str) -> str:
        """Gera chave de cache baseada no conteúdo."""
        return hashlib.md5(content.encode('utf-8')).hexdigest()[:16]



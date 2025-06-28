#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
LaTeX Generator v2.0 - VERSÃO CORRIGIDA E SIMPLIFICADA
Gerador avançado de documentos LaTeX para artigos acadêmicos
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
    Gerador LaTeX v2.0 - Versão corrigida que processa todas as seções
    """
    
    def __init__(self, output_dir: str = None, cache_dir: str = None):
        """
        Inicializa o gerador versão 2.
        
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
    
    def generate_latex(self) -> str:
        """
        Gerar código LaTeX completo - VERSÃO CORRIGIDA
        """
        template = self.templates[self.template_type]
        
        # Substituir placeholders básicos
        latex_code = template.replace('{{TITLE}}', self.document_data.get('title', ''))
        latex_code = latex_code.replace('{{ABSTRACT}}', self.document_data.get('abstract', ''))
        latex_code = latex_code.replace('{{KEYWORDS}}', self.document_data.get('keywords', ''))
        
        # Processar autores
        authors_latex = self._format_authors()
        latex_code = latex_code.replace('{{AUTHORS}}', authors_latex)
        
        # CORREÇÃO PRINCIPAL: Processar seções corretamente
        sections_latex = self._format_sections()
        latex_code = latex_code.replace('{{SECTIONS}}', sections_latex)
        
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
        Esta é a correção principal do bug!
        """
        if not self.sections:
            return ""
        
        sections_latex = []
        
        # CORREÇÃO: Processar TODAS as seções, não apenas a primeira
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
            'sections_processed': len([s for s in self.sections if s.get('title') and s.get('content')]),
            'sections_received': len(self.sections)
        }


    def compile_to_pdf(self, output_name: str = "document") -> Tuple[bool, str, Dict[str, Path]]:
        """Compila o documento para PDF."""
        try:
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
                    
                    # Salvar arquivo LaTeX também
                    with open(final_tex, 'w', encoding='utf-8') as f:
                        f.write(latex_code)
                    
                    return True, "PDF gerado com sucesso", {
                        'latex': final_tex,
                        'pdf': final_pdf
                    }
                else:
                    return False, f"Erro na compilação: {result.stderr}", {}
                    
            finally:
                # Limpar arquivo temporário
                if os.path.exists(tex_file):
                    os.unlink(tex_file)
                    
        except subprocess.TimeoutExpired:
            return False, "Timeout na compilação do PDF", {}
        except Exception as e:
            return False, f"Erro inesperado: {str(e)}", {}
    
    def _get_cache_key(self, content: str) -> str:
        """Gera chave de cache baseada no conteúdo."""
        return hashlib.md5(content.encode('utf-8')).hexdigest()[:16]


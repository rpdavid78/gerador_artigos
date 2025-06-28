#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
LaTeX Generator v2.0 - VERSÃO CORRIGIDA
Arquivo principal para deployment
"""

from app import app

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=False)


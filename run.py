#!/usr/bin/env python3
# coding: utf-8
"""
    :author: MathematicusLucian ;-)
    :brief: Portfolio Data Service
"""
from portfolio_read.src.app import app

def main():
    app.run(host='0.0.0.0', port=8000, debug=True)

if __name__ == "__main__":
    main()
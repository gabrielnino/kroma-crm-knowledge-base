import os
import sqlite3
import argparse
import re
from datetime import datetime

# Archivo de base de datos en la carpeta de scripts
DB_FILE = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'kasi_knowledge.db')
# Directorio raíz del proyecto KASI para escanear
TARGET_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

def get_db():
    conn = sqlite3.connect(DB_FILE)
    conn.row_factory = sqlite3.Row
    return conn

def init_db(conn):
    cursor = conn.cursor()
    # Tabla para el registro maestro de documentos
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS documents (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            filepath TEXT UNIQUE,
            title TEXT,
            last_modified TEXT
        )
    ''')
    # Tabla virtual FTS5 para búsqueda de texto completo rápida
    cursor.execute('''
        CREATE VIRTUAL TABLE IF NOT EXISTS fts_idx USING fts5(
            filepath,
            heading,
            content,
            tokenize="unicode61"
        )
    ''')
    conn.commit()

def clear_index(conn):
    cursor = conn.cursor()
    cursor.execute("DELETE FROM documents")
    cursor.execute("DELETE FROM fts_idx")
    conn.commit()

def parse_markdown_headings(content):
    sections = []
    current_heading = "General"
    current_lines = []
    
    for line in content.splitlines():
        match = re.match(r'^(#{1,6})\s+(.*)$', line)
        if match:
            if current_lines:
                sections.append((current_heading, "\n".join(current_lines)))
                current_lines = []
            current_heading = match.group(2).strip()
        else:
            current_lines.append(line)
            
    if current_lines or current_heading:
        sections.append((current_heading, "\n".join(current_lines)))
        
    return sections

def run_indexing():
    conn = get_db()
    init_db(conn)
    clear_index(conn)
    cursor = conn.cursor()
    
    indexed_count = 0
    section_count = 0
    
    print(f"Escanenando documentos KASI en: {TARGET_DIR}")
    for root, dirs, files in os.walk(TARGET_DIR):
        # Excluir carpetas ocultas/del sistema
        dirs[:] = [d for d in dirs if not d.startswith('.')]
        
        for file in files:
            if file.endswith(('.md', '.txt')):
                filepath = os.path.join(root, file)
                rel_path = os.path.relpath(filepath, TARGET_DIR)
                
                try:
                    mtime = os.path.getmtime(filepath)
                    mtime_str = datetime.fromtimestamp(mtime).strftime('%Y-%m-%d %H:%M:%S')
                    
                    with open(filepath, 'r', encoding='utf-8', errors='ignore') as f:
                        content = f.read()
                        
                    # Guardar registro maestro
                    cursor.execute('''
                        INSERT OR REPLACE INTO documents (filepath, title, last_modified)
                        VALUES (?, ?, ?)
                    ''', (rel_path, file, mtime_str))
                    
                    # Segmentar e indexar por secciones para precisión de búsqueda
                    sections = parse_markdown_headings(content)
                    for heading, sec_content in sections:
                        if sec_content.strip():
                            cursor.execute('''
                                INSERT INTO fts_idx (filepath, heading, content)
                                VALUES (?, ?, ?)
                            ''', (rel_path, heading, sec_content))
                            section_count += 1
                            
                    indexed_count += 1
                except Exception as e:
                    print(f"Error indexando {rel_path}: {e}")
                    
    conn.commit()
    conn.close()
    print(f"Indexación finalizada: {indexed_count} archivos procesados ({section_count} secciones registradas).")

def run_search(query):
    conn = get_db()
    cursor = conn.cursor()
    
    try:
        # Búsqueda mediante MATCH con snippets resaltados usando asteriscos
        cursor.execute('''
            SELECT 
                filepath, 
                heading, 
                snippet(fts_idx, 2, '***', '***', '...', 15) as matched_snippet
            FROM fts_idx 
            WHERE fts_idx MATCH ? 
            ORDER BY rank
            LIMIT 10
        ''', (query,))
        
        results = cursor.fetchall()
        if not results:
            print(f"No se encontraron coincidencias para: '{query}'")
            return
            
        print(f"\nResultados para '{query}':\n" + "="*60)
        for idx, row in enumerate(results, 1):
            print(f"{idx}. [{row['filepath']}] > {row['heading']}")
            print(f"   Coincidencia: {row['matched_snippet'].strip()}")
            print("-" * 60)
    except sqlite3.OperationalError as e:
        print(f"Error de sintaxis en la consulta: {e}")
    finally:
        conn.close()

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="KASI CLI Search Engine (SQLite FTS5)")
    subparsers = parser.add_subparsers(dest="command", help="Comandos")
    
    subparsers.add_parser("index", help="Actualizar el índice de la base de conocimiento")
    
    search_parser = subparsers.add_parser("search", help="Buscar en la base de conocimiento")
    search_parser.add_argument("query", type=str, help="Término o frase de búsqueda")
    
    args = parser.parse_args()
    
    if args.command == "index":
        run_indexing()
    elif args.command == "search":
        run_search(args.query)
    else:
        parser.print_help()

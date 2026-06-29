import os
import sys
import json
import sqlite3
import urllib.parse
from http.server import HTTPServer, BaseHTTPRequestHandler

PORT = 8000
ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
DB_FILE = os.path.join(ROOT_DIR, 'KASI-Kroma-AI-Systems-Inc', 'scripts', 'kasi_knowledge.db')

class KasiViewerHandler(BaseHTTPRequestHandler):
    def log_message(self, format, *args):
        # Deshabilitar logs por defecto en consola para mantenerla limpia
        return

    def do_GET(self):
        parsed_url = urllib.parse.urlparse(self.path)
        path = parsed_url.path
        query_params = urllib.parse.parse_qs(parsed_url.query)

        # 1. API: Listar archivos markdown y texto
        if path == "/api/files":
            self.send_response(200)
            self.send_header("Content-Type", "application/json")
            self.send_header("Cache-Control", "no-cache, no-store, must-revalidate")
            self.end_headers()
            
            files_list = []
            for root, dirs, files in os.walk(ROOT_DIR):
                dirs[:] = [d for d in dirs if not d.startswith('.') and d != 'node_modules']
                for file in files:
                    if file.endswith(('.md', '.txt')):
                        full_path = os.path.join(root, file)
                        rel_path = os.path.relpath(full_path, ROOT_DIR)
                        files_list.append({
                            "name": file,
                            "path": rel_path.replace(os.sep, '/'),
                            "dir": os.path.dirname(rel_path).replace(os.sep, '/')
                        })
            
            files_list.sort(key=lambda x: (x['dir'], x['name']))
            self.wfile.write(json.dumps(files_list).encode('utf-8'))

        # 2. API: Leer contenido de un archivo
        elif path == "/api/read":
            file_param = query_params.get('file', [None])[0]
            if not file_param:
                self.send_error(400, "Falta el parametro 'file'")
                return
                
            # Evitar Path Traversal de seguridad
            clean_rel_path = os.path.normpath(file_param).lstrip(os.path.sep).replace('..', '')
            full_path = os.path.join(ROOT_DIR, clean_rel_path)
            
            if not os.path.exists(full_path) or os.path.isdir(full_path):
                self.send_error(404, "Archivo no encontrado")
                return
                
            self.send_response(200)
            self.send_header("Content-Type", "text/plain; charset=utf-8")
            self.send_header("Cache-Control", "no-cache, no-store, must-revalidate")
            self.end_headers()
            with open(full_path, 'r', encoding='utf-8', errors='ignore') as f:
                self.wfile.write(f.read().encode('utf-8'))

        # 3. API: Buscar en base de datos SQLite FTS5
        elif path == "/api/search":
            query_param = query_params.get('q', [None])[0]
            if not query_param:
                self.send_response(200)
                self.send_header("Content-Type", "application/json")
                self.end_headers()
                self.wfile.write(json.dumps([]).encode('utf-8'))
                return

            if not os.path.exists(DB_FILE):
                self.send_response(200)
                self.send_header("Content-Type", "application/json")
                self.end_headers()
                self.wfile.write(json.dumps([{"error": "Base de datos no indexada. Ejecuta el indexador."}]).encode('utf-8'))
                return

            try:
                conn = sqlite3.connect(DB_FILE)
                conn.row_factory = sqlite3.Row
                cursor = conn.cursor()
                cursor.execute('''
                    SELECT filepath, heading, snippet(fts_idx, 2, '<mark>', '</mark>', '...', 15) as matched_snippet
                    FROM fts_idx 
                    WHERE fts_idx MATCH ? 
                    ORDER BY rank LIMIT 12
                ''', (query_param,))
                results = cursor.fetchall()
                conn.close()

                out = []
                for row in results:
                    out.append({
                        "filepath": row['filepath'],
                        "heading": row['heading'],
                        "snippet": row['matched_snippet']
                    })
                
                self.send_response(200)
                self.send_header("Content-Type", "application/json")
                self.send_header("Cache-Control", "no-cache, no-store, must-revalidate")
                self.end_headers()
                self.wfile.write(json.dumps(out).encode('utf-8'))
            except Exception as e:
                self.send_error(500, f"Error en búsqueda: {e}")

        # 4. Servir la interfaz web principal (Single Page App HTML/CSS/JS)
        elif path == "/" or path == "/index.html":
            self.send_response(200)
            self.send_header("Content-Type", "text/html; charset=utf-8")
            self.end_headers()
            self.wfile.write(self.get_html_content().encode('utf-8'))
            
        else:
            self.send_error(404, "No encontrado")

    def get_html_content(self):
        # Retorna el HTML principal con diseño premium oscuro, fuentes Inter y marked.js
        return r"""<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>KASI CRM — Visor Inteligente</title>
    <!-- Google Fonts -->
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&family=Fira+Code:wght@400;500&display=swap" rel="stylesheet">
    <!-- Marked.js para renderizar Markdown -->
    <script src="https://cdn.jsdelivr.net/npm/marked/marked.min.js"></script>
    <style>
        :root {
            --bg-main: #0c0f16;
            --bg-sidebar: #131722;
            --bg-card: #1c2130;
            --text-primary: #f0f4f9;
            --text-muted: #94a3b8;
            --accent: #38bdf8;
            --accent-glow: rgba(56, 189, 248, 0.15);
            --border: #2e3748;
        }

        * {
            box-sizing: border-box;
            margin: 0;
            padding: 0;
        }

        body {
            font-family: 'Inter', sans-serif;
            background-color: var(--bg-main);
            color: var(--text-primary);
            display: flex;
            height: 100vh;
            overflow: hidden;
        }

        /* --- SIDEBAR --- */
        .sidebar {
            width: 320px;
            background-color: var(--bg-sidebar);
            border-right: 1px solid var(--border);
            display: flex;
            flex-direction: column;
            flex-shrink: 0;
        }

        .sidebar-header {
            padding: 24px;
            border-bottom: 1px solid var(--border);
        }

        .logo-title {
            font-size: 20px;
            font-weight: 700;
            letter-spacing: -0.5px;
            color: var(--text-primary);
            display: flex;
            align-items: center;
            gap: 8px;
        }

        .logo-title span {
            color: var(--accent);
        }

        .search-container {
            padding: 16px 24px;
            border-bottom: 1px solid var(--border);
        }

        .search-input {
            width: 100%;
            padding: 10px 14px;
            background-color: var(--bg-main);
            border: 1px solid var(--border);
            border-radius: 8px;
            color: var(--text-primary);
            font-size: 14px;
            outline: none;
            transition: all 0.2s;
        }

        .search-input:focus {
            border-color: var(--accent);
            box-shadow: 0 0 0 3px var(--accent-glow);
        }

        .files-list-container {
            flex: 1;
            overflow-y: auto;
            padding: 16px 24px;
        }

        .section-label {
            font-size: 11px;
            text-transform: uppercase;
            letter-spacing: 1.2px;
            color: var(--text-muted);
            margin-bottom: 8px;
            font-weight: 700;
            display: flex;
            align-items: center;
            justify-content: space-between;
            cursor: pointer;
            user-select: none;
            padding: 6px 8px;
            border-radius: 4px;
            transition: all 0.2s ease;
        }

        .section-label:hover {
            background-color: var(--bg-card);
            color: var(--text-primary);
        }

        .section-label::after {
            content: '▼';
            font-size: 8px;
            color: var(--text-muted);
            transition: transform 0.2s ease;
        }

        .section-label.collapsed::after {
            transform: rotate(-90deg);
        }

        .client-group-content {
            overflow: hidden;
            transition: max-height 0.2s ease-out;
        }

        .client-group-content.collapsed {
            display: none;
        }

        .file-item {
            display: flex;
            align-items: center;
            padding: 10px 12px;
            border-radius: 6px;
            font-size: 13px;
            color: var(--text-muted);
            cursor: pointer;
            transition: all 0.15s ease;
            margin-bottom: 4px;
            text-decoration: none;
            overflow: hidden;
            text-overflow: ellipsis;
            white-space: nowrap;
        }

        .file-item:hover {
            background-color: var(--bg-card);
            color: var(--text-primary);
        }

        .file-item.active {
            background-color: var(--accent-glow);
            color: var(--accent);
            font-weight: 500;
        }

        .file-icon {
            margin-right: 8px;
            flex-shrink: 0;
        }

        /* --- CONTENIDO PRINCIPAL --- */
        .main-content {
            flex: 1;
            display: flex;
            flex-direction: column;
            background-color: var(--bg-main);
            overflow: hidden;
        }

        .top-bar {
            height: 70px;
            border-bottom: 1px solid var(--border);
            display: flex;
            align-items: center;
            padding: 0 40px;
            justify-content: space-between;
        }

        .current-file-title {
            font-size: 16px;
            font-weight: 600;
            color: var(--text-primary);
        }

        .viewer-pane {
            flex: 1;
            overflow-y: auto;
            padding: 40px 60px;
        }

        /* --- ESTILOS DE RENDER MARKDOWN --- */
        .markdown-body {
            max-width: 800px;
            margin: 0 auto;
            line-height: 1.6;
            font-size: 15px;
        }

        .markdown-body h1, .markdown-body h2, .markdown-body h3 {
            margin-top: 24px;
            margin-bottom: 16px;
            font-weight: 600;
            color: var(--text-primary);
        }

        .markdown-body h1 {
            font-size: 28px;
            border-bottom: 1px solid var(--border);
            padding-bottom: 8px;
        }

        .markdown-body h2 {
            font-size: 20px;
            border-bottom: 1px solid var(--border);
            padding-bottom: 6px;
        }

        .markdown-body p {
            margin-bottom: 16px;
            color: #d1d5db;
        }

        .markdown-body ul, .markdown-body ol {
            margin-bottom: 16px;
            padding-left: 20px;
            color: #d1d5db;
        }

        .markdown-body li {
            margin-bottom: 6px;
        }

        .markdown-body blockquote {
            padding: 12px 20px;
            background-color: var(--bg-card);
            border-left: 4px solid var(--accent);
            color: var(--text-primary);
            border-radius: 4px;
            margin-bottom: 16px;
        }

        .markdown-body code {
            font-family: 'Fira Code', monospace;
            font-size: 85%;
            background-color: var(--bg-card);
            padding: 3px 6px;
            border-radius: 4px;
            color: var(--accent);
        }

        .markdown-body pre {
            background-color: var(--bg-card);
            padding: 16px;
            border-radius: 8px;
            overflow-x: auto;
            border: 1px solid var(--border);
            margin-bottom: 16px;
        }

        .markdown-body pre code {
            background-color: transparent;
            padding: 0;
            color: var(--text-primary);
            font-size: 13px;
        }

        mark {
            background-color: #f59e0b;
            color: #000;
            padding: 2px 4px;
            border-radius: 2px;
            font-weight: 500;
        }

        /* --- PANTALLA VACÍA --- */
        .empty-state {
            display: flex;
            flex-direction: column;
            align-items: center;
            justify-content: center;
            height: 100%;
            color: var(--text-muted);
            text-align: center;
        }

        .empty-icon {
            font-size: 48px;
            margin-bottom: 16px;
            color: var(--border);
        }

        /* --- RESULTADOS DE BÚSQUEDA --- */
        .search-results-panel {
            padding: 10px 0;
        }

        .search-result-item {
            padding: 12px;
            background-color: var(--bg-card);
            border-radius: 8px;
            margin-bottom: 10px;
            cursor: pointer;
            border: 1px solid var(--border);
            transition: all 0.2s;
        }

        .search-result-item:hover {
            border-color: var(--accent);
            box-shadow: 0 0 0 1px var(--accent);
        }

        .search-result-header {
            display: flex;
            justify-content: space-between;
            font-size: 12px;
            font-weight: 600;
            margin-bottom: 6px;
            color: var(--accent);
        }

        .search-result-snippet {
            font-size: 13px;
            color: var(--text-muted);
        }
    </style>
</head>
<body>
    <!-- SIDEBAR -->
    <div class="sidebar">
        <div class="sidebar-header">
            <div class="logo-title">KASI <span>CRM</span></div>
        </div>
        <div class="search-container">
            <input type="text" class="search-input" id="searchInput" placeholder="Buscar en documentos (FTS5)...">
        </div>
        <div class="files-list-container" id="sidebarList">
            <!-- Cargado por JS -->
        </div>
    </div>

    <!-- MAIN VIEW -->
    <div class="main-content">
        <div class="top-bar">
            <div class="current-file-title" id="fileTitle">Selecciona un archivo</div>
        </div>
        <div class="viewer-pane" id="viewerPane">
            <div class="empty-state">
                <div class="empty-icon">📄</div>
                <h2>Ningún documento abierto</h2>
                <p style="margin-top: 8px;">Selecciona una nota de la barra lateral o haz una búsqueda.</p>
            </div>
        </div>
    </div>

    <script>
        let currentActiveItem = null;
        const expandedGroups = new Set();
        let isRefreshing = false;

        // Cargar lista de archivos al iniciar
        async function loadFiles() {
            if (isRefreshing) return;
            isRefreshing = true;
            try {
                const res = await fetch('/api/files');
                const files = await res.json();
                const sidebar = document.getElementById('sidebarList');
                sidebar.innerHTML = '';

                // Agrupar archivos por nombre de cliente limpio
                const grouped = {};
                files.forEach(file => {
                    let clientName = "Corporativo KASI";
                    
                    // Mapeo robusto de carpeta a nombre de cliente limpio
                    const match = file.dir.match(/(?:[Cc]ustumers|[Cc]ustomers)\/([^\/]+)/);
                    if (match) {
                        clientName = match[1]
                            .replace(/-/g, ' ')
                            .replace(/_/g, ' ')
                            .replace(/\b\w/g, c => c.toUpperCase());
                    } else if (file.dir && file.dir !== '.') {
                        clientName = file.dir
                            .replace(/-/g, ' ')
                            .replace(/_/g, ' ')
                            .replace(/\b\w/g, c => c.toUpperCase());
                    }
                    
                    if (!grouped[clientName]) {
                        grouped[clientName] = [];
                    }
                    grouped[clientName].push(file);
                });

                // Renderizar los grupos en el sidebar
                let isFirst = true;
                const currentFile = document.getElementById('fileTitle').innerText;

                for (const [client, clientFiles] of Object.entries(grouped)) {
                    const groupContainer = document.createElement('div');
                    groupContainer.className = 'client-group';
                    
                    const header = document.createElement('div');
                    header.className = 'section-label';
                    header.style.marginTop = isFirst ? '0px' : '20px';
                    header.innerText = client;
                    
                    const contentWrapper = document.createElement('div');
                    contentWrapper.className = 'client-group-content';
                    
                    // Mantener el estado de colapsado/expandido
                    if (expandedGroups.has(client)) {
                        header.classList.remove('collapsed');
                        contentWrapper.classList.remove('collapsed');
                    } else {
                        header.classList.add('collapsed');
                        contentWrapper.classList.add('collapsed');
                    }
                    
                    // Evento para colapsar/expandir el grupo
                    header.onclick = () => {
                        const wasCollapsed = header.classList.contains('collapsed');
                        if (wasCollapsed) {
                            header.classList.remove('collapsed');
                            contentWrapper.classList.remove('collapsed');
                            expandedGroups.add(client);
                        } else {
                            header.classList.add('collapsed');
                            contentWrapper.classList.add('collapsed');
                            expandedGroups.delete(client);
                        }
                        // Recargar todas las opciones disponibles cada vez que abra y cierre la pestaña
                        loadFiles();
                    };

                    clientFiles.forEach(file => {
                        const item = document.createElement('a');
                        item.className = 'file-item';
                        if (file.path === currentFile) {
                            item.classList.add('active');
                            currentActiveItem = item;
                        }
                        item.innerHTML = `<span class="file-icon">📄</span> ${file.name}`;
                        item.onclick = () => openFile(file.path, item);
                        contentWrapper.appendChild(item);
                    });

                    groupContainer.appendChild(header);
                    groupContainer.appendChild(contentWrapper);
                    sidebar.appendChild(groupContainer);
                    isFirst = false;
                }
            } catch (err) {
                console.error("Error al cargar archivos:", err);
            } finally {
                isRefreshing = false;
            }
        }

        // Recargar al enfocar la pestaña del navegador o al cambiar el estado de visibilidad
        document.addEventListener('visibilitychange', () => {
            if (document.visibilityState === 'visible') {
                loadFiles();
            }
        });

        window.addEventListener('focus', () => {
            loadFiles();
        });

        // Abrir un archivo y renderizarlo
        async function openFile(filepath, element) {
            if (currentActiveItem) {
                currentActiveItem.classList.remove('active');
            }
            if (element) {
                element.classList.add('active');
                currentActiveItem = element;
            }

            document.getElementById('fileTitle').innerText = filepath;
            const pane = document.getElementById('viewerPane');
            pane.innerHTML = '<div class="empty-state">Cargando documento...</div>';

            try {
                const res = await fetch(`/api/read?file=${encodeURIComponent(filepath)}`);
                if (!res.ok) throw new Error("Error de lectura");
                const text = await res.text();
                
                // Configurar marked para renderizado de HTML seguro
                marked.setOptions({ gfm: true, breaks: true });
                const htmlContent = marked.parse(text);

                pane.innerHTML = `<div class="markdown-body">${htmlContent}</div>`;
            } catch (err) {
                pane.innerHTML = `<div class="empty-state" style="color: red;">Error al cargar el archivo.</div>`;
            }
        }

        // Buscador FTS5 integrado en tiempo real
        const searchInput = document.getElementById('searchInput');
        let searchTimeout = null;

        searchInput.addEventListener('input', (e) => {
            clearTimeout(searchTimeout);
            const query = e.target.value.trim();

            if (!query) {
                loadFiles();
                return;
            }

            searchTimeout = setTimeout(async () => {
                const res = await fetch(`/api/search?q=${encodeURIComponent(query)}`);
                const results = await res.json();
                const sidebar = document.getElementById('sidebarList');
                sidebar.innerHTML = '<div class="section-label">Resultados de Búsqueda</div>';

                if (results.length === 0) {
                    sidebar.innerHTML += '<div style="font-size: 13px; color: var(--text-muted); padding: 10px;">Sin coincidencias</div>';
                    return;
                }

                if (results[0] && results[0].error) {
                    sidebar.innerHTML += `<div style="font-size: 13px; color: red; padding: 10px;">${results[0].error}</div>`;
                    return;
                }

                results.forEach(resItem => {
                    const resultCard = document.createElement('div');
                    resultCard.className = 'search-result-item';
                    resultCard.innerHTML = `
                        <div class="search-result-header">
                            <span>${resItem.filepath.split('/').pop()}</span>
                            <span>${resItem.heading}</span>
                        </div>
                        <div class="search-result-snippet">${resItem.snippet}</div>
                    `;
                    resultCard.onclick = () => openFile(resItem.filepath);
                    sidebar.appendChild(resultCard);
                });
            }, 300);
        });

        // Inicialización
        loadFiles();
    </script>
</body>
</html>
"""

def main():
    try:
        server = HTTPServer(('0.0.0.0', PORT), KasiViewerHandler)
        print(f"============================================================")
        print(f" Visor KASI Web Local Inicializado")
        print(f" URL de Acceso: http://localhost:{PORT}/")
        print(f" Presiona Ctrl+C para apagar el servidor.")
        print(f"============================================================")
        server.serve_forever()
    except KeyboardInterrupt:
        print("\nApagando el servidor web de KASI...")
        sys.exit(0)
    except Exception as e:
        print(f"Error al iniciar el servidor en el puerto {PORT}: {e}")
        sys.exit(1)

if __name__ == '__main__':
    main()

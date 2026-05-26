"""
servidor.py — Dashboard Demo Day UBA
Corré este script y abrí http://localhost:8080 en el navegador.
Resuelve el problema de CORS que impide leer Google Sheets desde file://.

Uso:
    python servidor.py
    (o doble click en Windows si tenés Python instalado)

Requiere Python 3.6+
"""

import http.server
import socketserver
import webbrowser
import os

PORT = 8080
FOLDER = os.path.dirname(os.path.abspath(__file__))

class CORSHandler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=FOLDER, **kwargs)

    def end_headers(self):
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Cache-Control', 'no-cache')
        super().end_headers()

    def log_message(self, format, *args):
        pass  # silenciar logs

print(f"╔══════════════════════════════════════════╗")
print(f"║   🎓 Dashboard Demo Day UBA              ║")
print(f"║   Servidor corriendo en puerto {PORT}      ║")
print(f"╚══════════════════════════════════════════╝")
print(f"")
print(f"  → Abriendo http://localhost:{PORT}/index.html")
print(f"  → Ctrl+C para detener")
print(f"")

with socketserver.TCPServer(("", PORT), CORSHandler) as httpd:
    webbrowser.open(f"http://localhost:{PORT}/index.html")
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("\n  Servidor detenido.")

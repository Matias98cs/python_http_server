from http.server import BaseHTTPRequestHandler, HTTPServer
import urllib.parse


class MiServidor(BaseHTTPRequestHandler):

    def do_GET(self):
        # Obtener los parámetros de la URL
        parsed_url = urllib.parse.urlparse(self.path)
        params = urllib.parse.parse_qs(parsed_url.query)

        # Obtener los valores de los parámetros individuales
        param1_value = params.get('param1', [''])[0]
        param2_value = params.get('param2', [''])[0]

        # Devolver una respuesta
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        self.wfile.write(f"Valor de param1: {param1_value}\n".encode())
        self.wfile.write(f"Valor de param2: {param2_value}\n".encode())


def run_server(port=8000):
    server_address = ('', port)
    httpd = HTTPServer(server_address, MiServidor)
    print(f"Servidor corriendo en el puerto {port}")
    httpd.serve_forever()


if __name__ == '__main__':
    run_server()

import pytest
import socket
import threading
import time

from pyweber.utils.server import Server, Router, Template

# @pytest.fixture
# def server():
#     router = Router()
#     router.add_route('/', template=Template(template='test_template.html'))
#     server = Server(router)
#     threading.Thread(target=server.create_server, args=('localhost', 5555, '/'), daemon=True).start()
#     time.sleep(1)  # Aguardar o servidor começar
#     return server

def test_server_initialization():
    """Verifica se o servidor iniciou corretamente"""
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        client_socket.connect(('localhost', 5555))
        client_socket.sendall(b"GET / HTTP/1.1\r\nHost: localhost\r\n\r\n")
        response = client_socket.recv(1024).decode()

        print(f"\n🔍 Resposta do servidor:\n{response}")
        assert "HTTP/1.1 200 OK" in response  # Verifique se a resposta é válida
    finally:
        client_socket.close()

def test_route_response():
    """Verifica se o servidor retorna o template correto para uma rota existente"""
    
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        client_socket.connect(('localhost', 5555))
        client_socket.sendall(b"GET / HTTP/1.1\r\nHost: localhost\r\n\r\n")
        response = client_socket.recv(1024).decode()
        assert "HTTP/1.1 200 OK" in response  # Resposta de sucesso
        assert "Pytest" in response  # Verifica se o template foi carregado corretamente
    finally:
        client_socket.close()

def test_static_file_response():
    """Verifica se o servidor retorna um arquivo estático corretamente"""
    # Simula o caminho para um arquivo estático
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        client_socket.connect(('localhost', 5555))
        client_socket.sendall(b"GET /tests/static/style.css HTTP/1.1\r\nHost: localhost\r\n\r\n")
        response = client_socket.recv(1024).decode()
        assert "HTTP/1.1 200 OK" in response  # Resposta de sucesso
        assert "Content-Type: text/css" in response  # Verifica se o tipo de conteúdo está correto
    finally:
        client_socket.close()

def test_route_not_found():
    """Verifica se o servidor retorna 404 para uma rota inexistente"""
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        client_socket.connect(('localhost', 5555))
        client_socket.sendall(b"GET /unknown HTTP/1.1\r\nHost: localhost\r\n\r\n")
        response = client_socket.recv(1024).decode()
        assert "HTTP/1.1 404 Not Found" in response  # Verifica se a resposta 404 é retornada
        assert "Página não encontrada" in response  # Verifica se o template de erro foi incluído
    finally:
        client_socket.close()

def test_reload_code():
    """Verifica se o código de recarga é adicionado ao template quando recarregado"""
    
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        client_socket.connect(('localhost', 5555))
        client_socket.sendall(b"GET / HTTP/1.1\r\nHost: localhost\r\n\r\n")
        response = client_socket.recv(1024).decode()
        assert "reload" in response  # Verifica se o código de recarga foi inserido no template
    finally:
        client_socket.close()
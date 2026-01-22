import socket

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('0.0.0.0', 5555)) # Endereço e porta
server.listen()

print("Servidor aguardando conexões...")
while True:
    client, addr = server.accept()
    # Aqui você cria a lógica para receber e distribuir as mensagens

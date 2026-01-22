import socket

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('IP_DO_SERVIDOR', 5555))

while True:
    msg = input("Digite sua mensagem: ")
    client.send(msg.encode('utf-8'))
#---------
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('0.0.0.0', 5555)) # Endereço e porta
server.listen()

print("Servidor aguardando conexões...")
while True:
    client, addr = server.accept()
    # Aqui você cria a lógica para receber e distribuir as mensagens

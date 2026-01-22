import socket

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('IP_DO_SERVIDOR', 5555))

while True:
    msg = input("Digite sua mensagem: ")
    client.send(msg.encode('utf-8'))

import socket
import random

# Создаем TCP-сокет
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Подключаемся к серверу
server_address = ('localhost', 12346)
client_socket.connect(server_address)

# Отправляем сообщение серверу
message = ["Привет, сервер!", "Как дела?"]
client_socket.send(message[random.randint(0, 1)].encode())

# Получаем ответ от сервера
response = client_socket.recv(1024).decode()
print(response)

# Закрываем соединение
client_socket.close()
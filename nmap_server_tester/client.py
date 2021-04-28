#!bin/python3
import socket

SERVER_IP = 'localhost'  # Replace with server address

print("ENTER IP or HOSTNAME to scan with NMAP (ex. 192.168.0.1 or google.com):")
user_message = str(input())
print("TRYING TO SEND DATA: ", bytes(user_message, 'utf-8'))

client = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)  # открываем сокет
try:
    client.connect(SERVER_IP)  # пытаемся подключиться к серверу
    print("Waiting for server response. Please wait...")
    client.send(bytes(user_message, 'utf-8'))  # отправляем сообщение с запросом на сканирование
    from_server = client.recv(4096)  # дожидаемся ответа
    client.close()  # закрываем соединение
    print("Server response:")
    print(from_server.decode('utf-8'))  # выводим ответ
except ConnectionError:  # если соединение не удалось выводим ошибку
    print("Server Unavailable")

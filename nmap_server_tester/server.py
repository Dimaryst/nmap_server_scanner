#!bin/python3
import subprocess
import socket

IP_ADDRESS = 'localhost'  # замени на ip сервера
PORT = 9090


# подпроцесс для вызова nmap
def process(cmd):
    pr = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE)  # запуск команды которую передали в функцию
    output = pr.communicate()[0].decode('utf-8')  # вывод в дайтах поэтому после получения декодируем вывод nmap
    return output


# socket
serv = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # открываем сокет
serv.bind((IP_ADDRESS, PORT))  # привязываем сокет к ip и порту (объявлены выше)
serv.listen()  # сокет слушает порт

print(f"Server started {(IP_ADDRESS, PORT)}")

# вечный цикл с сервером
while True:
    try:
        conn, addr = serv.accept()
        from_client = ''
        while True:
            data = conn.recv(4096)  # полученные данные от клиента
            user_request = data.decode('utf-8').replace("\n", "")  # в строку перевели и убрали "\n" в конце
            print(f"Requested address to scan: ({user_request})")
            cmd = f"nmap {user_request}"  # nmap
            out = process(cmd)  # вывод nmap (вернула функция которая описана выше)
            if not data:
                break
            conn.send(out.encode('utf-8'))  # ответ клиенту
        conn.close()  # закрыли соединение
    except KeyboardInterrupt:  # выход инициирован с клавиатуры (ctrl + c)
        print("Server Stopped")
    except ConnectionResetError:
        print("Client Disconnected")

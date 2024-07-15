import socket
from dotenv import load_dotenv
import os

load_dotenv()

client_socket=socket.socket(socket.AF_INET,socket.SOCK_STREAM) #ipv4 based tcp connection

host = os.getenv("HOST_IP") #server Ip
port=8000

client_socket.connect((host,port))

while True:
        message = input("You: ")
        client_socket.send(message.encode('utf-8'))
        if message.lower() == 'exit':
                print("Connection closed by client")
                break

        response = client_socket.recv(1024).decode('utf-8')

        print(f"Server: {response}")
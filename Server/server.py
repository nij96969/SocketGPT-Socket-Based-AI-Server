import socket
import threading

from chat_bot import chat_with_gemini

#This is the function to chat with gemini and the thread terminates when user writes exit
def handle_client(client_socket, addr):
    print(f"Got a connection from {addr}")

    while True:
        message = client_socket.recv(1024).decode('utf-8')
        if message.lower() == 'exit':
            print("Connection is closed by the client")
            break

        print(f"Client {addr}: {message}")

        response = chat_with_gemini(message)
        client_socket.send(response.encode('utf-8'))

        if response.lower() == 'exit':
            print("Connection is closed by the server")
            break

    client_socket.close()

def start_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # IPv4 based
    host = '0.0.0.0'  # listen on all available interfaces
    port = 8000

    server_socket.bind((host, port))
    server_socket.listen(5)
    print(f"Server listening on {host}:{port}")

    #whenever we recieve a request to connect , the client will be assigned a thread to communicate
    while True:
        client_socket, addr = server_socket.accept()
        client_thread = threading.Thread(target=handle_client, args=(client_socket, addr))
        client_thread.start()

if __name__ == "__main__":
    start_server()

import socket
import threading
import tkinter as tk

class ChatClient:
    def __init__(self, master):
        self.master = master
        self.master.title("Chat Client")

        self.message_listbox = tk.Listbox(self.master, height=15, width=50)
        self.message_listbox.pack(pady=10)

        self.entry_message = tk.Entry(self.master, width=40)
        self.entry_message.pack(pady=10)

        self.button_send = tk.Button(self.master, text="Send", command=self.send_message)
        self.button_send.pack()

        self.username = tk.simpledialog.askstring("Username", "Enter your username:")
        self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client_socket.connect(('localhost', 12345))

        receive_thread = threading.Thread(target=self.receive_messages)
        receive_thread.start()

    def send_message(self):
        message = self.entry_message.get()
        if message:
            full_message = f"{self.username}: {message}"
            self.client_socket.send(full_message.encode())
            self.entry_message.delete(0, tk.END)

    def receive_messages(self):
        while True:
            try:
                message = self.client_socket.recv(1024).decode()
                if not message:
                    break
                self.message_listbox.insert(tk.END, message)
            except ConnectionError:
                break

        self.client_socket.close()

class ChatServer:
    def __init__(self):
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_socket.bind(('localhost', 12345))
        self.server_socket.listen()

        self.clients = []

        self.accept_connections()

    def accept_connections(self):
        while True:
            client_socket, client_address = self.server_socket.accept()
            client_thread = threading.Thread(target=self.handle_client, args=(client_socket, client_address))
            client_thread.start()

    def broadcast_message(self, message, client_socket):
        for client in self.clients:
            if client != client_socket:
                try:
                    client.send(message.encode())
                except ConnectionError:
                    self.remove_client(client)

    def handle_client(self, client_socket, client_address):
        username = client_socket.recv(1024).decode()
        self.clients.append(client_socket)
        self.broadcast_message(f"{username} joined the chat.", client_socket)

        while True:
            try:
                message = client_socket.recv(1024).decode()
                if not message:
                    break
                self.broadcast_message(message, client_socket)
            except ConnectionError:
                break

        self.remove_client(client_socket)
        client_socket.close()

    def remove_client(self, client_socket):
        if client_socket in self.clients:
            self.clients.remove(client_socket)
            self.broadcast_message("A user left the chat.", client_socket)

if __name__ == "__main__":
    server_thread = threading.Thread(target=ChatServer)
    server_thread.start()

    root = tk.Tk()
    chat_client = ChatClient(root)
    root.mainloop()

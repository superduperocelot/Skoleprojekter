import socket
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad, unpad

# Create a socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Set the server address (you can use your local IP and a port number)
server_address = ('0.0.0.0', 11113)

# Bind the socket to the server address
server_socket.bind(server_address)

# Listen for incoming connections
server_socket.listen(5)

encryption_key = get_random_bytes(16)
cipher = AES.new(encryption_key, AES.MODE_CBC)
decipher = AES.new(encryption_key, AES.MODE_CBC, iv=cipher.iv)

print("Server is listening for incoming connections...")

# Accept a connection from a client
client_socket, client_address = server_socket.accept()
print(f"Connected to {client_address}")
client_socket.send(encryption_key)
client_socket.send(cipher.iv)

#client2_socket, client2_address = server_socket.accept()
#print(f"Connected to {client2_address}")
#client2_socket.send(encryption_key)


while True:
    message = client_socket.recv(1024)
    if not message:
        break
    decrypted_message = unpad(decipher.decrypt(message), AES.block_size)
    print(f"Client1: {decrypted_message.decode()}")

    #client2_socket.send(message.encode())
    """
    message = client2_socket.recv(1024).decode()
    if not message:
        break
    print(f"Client2: {message}")
    client_socket.send(message.encode())
    """
    reply = input("You: ").encode("utf-8")
    cipher_reply = (cipher.encrypt(pad(reply, AES.block_size)))
    client_socket.send(cipher_reply)
    #client2_socket.send(reply.encode())

client_socket.close()
#client2_socket.close()
server_socket.close()

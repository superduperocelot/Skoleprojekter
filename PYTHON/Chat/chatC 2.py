import socket
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad, unpad


# Create a socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Set the server address (the server's IP and port)
server_address = ('10.171.172.128', 11113)

# Connect to the server
client_socket.connect(server_address)

encryption_key = client_socket.recv(1024)
iv = client_socket.recv(1024)
cipher = AES.new(encryption_key, AES.MODE_CBC, iv=iv)
decipher = AES.new(encryption_key, AES.MODE_CBC, iv=iv)
   

while True:
    message = input("You: ").encode("utf-8")
    cipher_message = (cipher.encrypt(pad(message, AES.block_size)))
    client_socket.send(cipher_message)

    reply = client_socket.recv(1024)
    decrypted_reply = unpad(decipher.decrypt(reply), AES.block_size)
    print(f"Server: {decrypted_reply.decode()}")

client_socket.close()
#!/usr/bin/python3
import socket

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

print('Socket created successfully.')

host = 'localhost'
door = 5432

s.bind((host, door))
message = '\nServer: Hello customer!'

while True:
    data, end = s.recvfrom(4096)

    if data:
        print('Server sending message...')
        s.sendto(data + (message.encode()), end)

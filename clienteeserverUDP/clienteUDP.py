#!/usr/bin/python3

import socket

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

print('Socket client created successfully.')

host = 'localhost'
door = 5433
message = 'Hello Server!'

try:
    print(f'Client: {message}')
    s.sendto(message.encode(), (host, 5432))

    data, server = s.recvfrom(4096)
    data = data.decode()
    print(f'Client: {data}')
finally:
    print('Client:Closing the connection!')
    s.close()

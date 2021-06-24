#!/usr/bin/python3

import socket
import sys


def main():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0)
    except socket.error as e:
        print('Connection failed.')
        print(f'Error: {e}')
        sys.exit()

    print('Socket created successfully.')

    target_host = input('Enter host or IP to connect: ')
    target_door = input('Enter the port to connect: ')

    try:
        s.connect((target_host, int(target_door)))
        print(f'TCP client successfully connected to host: {target_host} and port: {target_door}')
        s.shutdown(2)
    except socket.error as e:
        print('Connection failed')
        print(f'Error: {e}')
        sys.exit()


if __name__ == '__main__':
    main()

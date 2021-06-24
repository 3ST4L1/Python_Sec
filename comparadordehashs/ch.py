#!/usr/bin/python3

import hashlib

arch1 = 'a.txt'
arch2 = 'b.txt'

hash1 = hashlib.new('ripemd160')

hash1.update(open(arch1, 'rb').read())

hash2 = hashlib.new('ripemd160')

hash2.update(open(arch2, 'rb').read())


if hash1.digest() != hash2.digest():
    print(f'File: "{arch1}" is different from file: "{arch2}"')
    print('=' * 70)
    print(f'-The hash of file {arch1} is: {hash1.hexdigest()}')
    print(f'-The hash of file {arch2} is: {hash2.hexdigest()}')
    print('=' * 70)
else:
    print(f'File: "{arch1}" is the same as file: "{arch2}"')
    print('=' * 70)
    print(f'-The hash of file {arch1} is: {hash1.hexdigest()}')
    print(f'-The hash of file {arch2} is: {hash2.hexdigest()}')
    print('=' * 70)

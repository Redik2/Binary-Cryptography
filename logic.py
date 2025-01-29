import hashlib
from bitarray import bitarray

def hash_key(key: str) -> bitarray:
    """Хеширует ключ с использованием SHA-256 и преобразует в битовый массив"""
    hash_object = hashlib.sha256(key.encode())
    hash_bits = bitarray()
    hash_bits.frombytes(hash_object.digest())
    return hash_bits

def encrypt_decrypt_file(input_file: str, output_file: str, key: str):
    """Шифрует или расшифровывает файл методом инверсии битов с использованием хеш-ключа"""
    key_bits = hash_key(key)

    with open(input_file, "rb") as f:
        file_bits = bitarray()
        file_bits.fromfile(f)

    for i in range(len(file_bits)):
        file_bits[i] ^= key_bits[i % len(key_bits)]

    with open(output_file, "wb") as f:
        file_bits.tofile(f)
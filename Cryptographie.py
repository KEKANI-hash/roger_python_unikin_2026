# -*- coding: utf-8 -*-
"""
Created on Thu May  1 08:28:18 2025

@author: Roger MAWETE
"""

import pandas as pd
from cryptography.fernet import Fernet

# 1.Chargement du dataset à partir d'un fichier CSV
def load_dataset(file_path):
    
    try:
        df = pd.read_csv(file_path)
        return df
    except FileNotFoundError:
        print(f"Erreur: Le fichier '{file_path}' n'a pas été trouvé.")
        return None

# 2. Chiffrement de César
def cesar_cipher(text, shift):
    """Chiffre ou déchiffre un texte avec le chiffrement de César."""
    result = ''
    for char in text:
        if char.isalpha():
            start = ord('a') if char.islower() else ord('A')
            shifted_char = chr((ord(char) - start + shift) % 26 + start)
        else:
            shifted_char = char
        result += shifted_char
    return result

# 3. Chiffrement de Vigenère
def vigenere_cipher(text, key, encrypt=True):
    """Chiffre ou déchiffre un texte avec le chiffrement de Vigenère."""
    key = key.upper()
    key_length = len(key)
    key_index = 0
    result = ''
    for char in text:
        if char.isalpha():
            shift = ord(key[key_index % key_length]) - ord('A')
            if not encrypt:
                shift = -shift
            start = ord('a') if char.islower() else ord('A')
            shifted_char = chr((ord(char) - start + shift) % 26 + start)
            key_index += 1
        else:
            shifted_char = char
        result += shifted_char
    return result

# 4. Chiffrement AES (Advanced Encryption Standard)
def generate_key():
    """Génère une clé AES."""
    return Fernet.generate_key()

def encrypt_message(message: str, key: bytes) -> bytes:
    """Chiffre un message avec AES."""
    f = Fernet(key)
    encrypted_message = f.encrypt(message.encode())
    return encrypted_message

def decrypt_message(encrypted_message: bytes, key: bytes) -> str:
    """Déchiffre un message chiffré avec AES."""
    f = Fernet(key)
    decrypted_message = f.decrypt(encrypted_message).decode()
    return decrypted_message


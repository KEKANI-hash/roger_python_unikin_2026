# -*- coding: utf-8 -*-
"""
Created on Thu May  1 09:41:43 2025

@author: Roger MAWETE
"""

import numpy as np
def matrix_mod_inverse(matrix, modulus):
    """Calcule l'inverse modulaire d'une matrice."""
    det = int(np.round(np.linalg.det(matrix)))
    det_inv = pow(det, -1, modulus) #Inverse modulaire du déterminant
    adj_matrix = det_inv * np.round(np.linalg.inv(matrix) * det).astype(int) % modulus
    return adj_matrix


def hill_cipher(text, key_matrix, mode):
    """Chiffre ou déchiffre le texte en utilisant la matrice clé."""
    text = text.upper()
    
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ '"
    num_text = [alphabet.index(char) for char in text]
    num_text = np.array(num_text).reshape(-1, key_matrix.shape[0])
    
    if mode == 'encrypt':
        result = np.dot(num_text, key_matrix.T) % 28
    elif mode == 'decrypt':
        inv_key_matrix = matrix_mod_inverse(key_matrix.T, 28)
        result = np.dot(num_text, inv_key_matrix) % 28
    else:
        raise ValueError("Mode invalide. Utilisez 'encrypt' ou 'decrypt'.")

    result = result.flatten()
    decrypted_text = "".join([alphabet[i] for i in result])
    return decrypted_text

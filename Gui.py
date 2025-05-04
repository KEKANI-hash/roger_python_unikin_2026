# -*- coding: utf-8 -*-
"""
Created on Thu May  1 09:44:59 2025

@author: cdk
"""
import tkinter as tk
from tkinter import messagebox
import hill_cipher
import numpy as np
import Cryptographie
import random

def lancer():
    
    def encrypt_decrypt():
        try:
            key_matrix = np.array([[int(x) for x in row.split()] for row in key_entry.get("1.0", tk.END).strip().split('\n')])
            text = text_entry.get("1.0", tk.END).strip()
            mode = "encrypt" 

            if key_matrix.shape[0] != key_matrix.shape[1]:
                raise ValueError("La matrice doit être carrée")
            elif len(text) % key_matrix.shape[0] != 0:  
                    if key_matrix.shape[0]==2:
                            text=text+" "
                    elif key_matrix.shape[0]==3:
                                for i in range((3-len(text) % key_matrix.shape[0])):
                                        text=text+" "
            result = hill_cipher.hill_cipher(text, key_matrix, mode)
            result_label.config(text=f"Résultat codé: {result}")
            
        except ValueError as e:
            messagebox.showerror("Erreur", str(e))

        except Exception as e:
            messagebox.showerror("Erreur", f"Une erreur s'est produite : {e}")
            
    def decrypt():
            try:
                key_matrix = np.array([[int(x) for x in row.split()] for row in key_entry.get("1.0", tk.END).strip().split('\n')])
                text = text_entry.get("1.0", tk.END).strip()
                mode = "decrypt" 
                if key_matrix.shape[0] != key_matrix.shape[1]:
                    raise ValueError("La matrice doit être carrée")
                   
                elif len(text) % key_matrix.shape[0] != 0:  
                        if key_matrix.shape[0]==2:
                                text=text+" "
                        elif key_matrix.shape[0]==3:
                                    for i in range((3-len(text) % key_matrix.shape[0])):
                                            text=text+" "
                result = hill_cipher.hill_cipher(text, key_matrix, mode)
                result_label1.config(text=f"Résultat decodé: {result}")
                
                

            except ValueError as e:
                messagebox.showerror("Erreur", str(e))
               
            except Exception as e:
                messagebox.showerror("Erreur", f"Une erreur s'est produite : {e}")
    
            
    principal = tk.Tk()
    principal.title("Cryptographe fenetre")

    # Fenêtre d'accueil (à implémenter si nécessaire)


    # Fenêtre de chiffrement/déchiffrement
    frame = tk.Frame(principal)
    frame.pack(padx=40, pady=40)
    
    
    
    
    key_label = tk.Label(frame, text="Entrer le mot de passe entier  longueur 18,\nevitez les lettres et caractères ):")
    key_label.pack()
    key_entry = tk.Text(frame, height=1, width=19)
    key_entry.pack()

    text_label = tk.Label(frame, text="Texte:")
    text_label.pack()
    text_entry = tk.Text(frame, height=5, width=30)
    text_entry.pack()

    encrypt_button = tk.Button(frame, text="Crypter", command=encrypt_decrypt)
    encrypt_button.pack(pady=10)


    decrypt_button = tk.Button(frame, text="Decrypter", command=decrypt)
    decrypt_button.pack(pady=10)

    result_label = tk.Label(frame, text="Résultat cryptage:")
    result_label.pack()
    
    result_label1= tk.Label(frame, text="Résultat decryptage:")
    result_label1.pack()

def lancer2():
    
    def generer():
                chemin = 'SMSSpamCollection.csv'  
                df = Cryptographie.load_dataset(chemin)
                message=df.iloc[random.randint(0,5573)][0]
                return message
    def gen():
        msg.config(text=generer())
    
    def cesar():
                message=msg['text']
                cesar_encrypted = Cryptographie.cesar_cipher(message, 3)
                cesar_decrypted =Cryptographie.cesar_cipher(cesar_encrypted, -3)
                result_label2.config(text=f"Chiffré (César): {cesar_encrypted}")
                
    def vigenere():
                message=msg['text']
                vigenere_encrypted = Cryptographie.vigenere_cipher(message, "KEY")
                result_label2.config(text=f"Chiffré (Vigenère): {vigenere_encrypted}")
    def aes():
                message=msg['text']
                key = Cryptographie.generate_key()
                aes_encrypted = Cryptographie.encrypt_message(message, key)
                result_label2.config(text=f"Chiffré (AES): {aes_encrypted}")
    
    principal1 = tk.Tk()
    principal1.title("Cryptographe entrainnement du dataset")

    frame2 = tk.Frame(principal1)
    frame2.pack(padx=160, pady=120)
    msg=tk.Label(frame2,text="Message generé")
    msg.pack()
    VigGen=tk.Button(frame2, text="Generer un message du dataset", command=gen)
    VigGen.pack(pady=15)
    
    CesarButt=tk.Button(frame2, text="Code de Cesar", command=cesar)
    CesarButt.pack(pady=10)
            
    VigButt=tk.Button(frame2, text="Code Vigenere", command=vigenere)
    VigButt.pack(pady=10)
            
    aesbutt=tk.Button(frame2, text="Code AES", command=aes)
    aesbutt.pack(pady=10)
    result_label2=tk.Label(frame2, text="res")
    result_label2 = tk.Label(frame2, text="Résultat cryptage:")
    result_label2.pack()
   
    

# Fenêtre principale


if __name__=="__main__":
    root = tk.Tk()
    root.title("Cryptographie de MAWETE ")
    root.geometry("800x600")
    root.resizable(False,False)
    title_label=tk.Label(root, text="Bienvenue",font=("Helveca",18,"bold"))

    title_label.pack(pady=10)
    lib2=tk.Label(root, text="Lancer le traducteur en cliquant sur Commencer",font=("Helveca",11,"bold italic"))
    lib2.pack(pady=5)
    
    button_start = tk.Button(root, text="Commencer", command=lancer)
    button_start.pack(pady=10)
    lib7=tk.Label(root, text="Exercer le dataset en cliquant sur Entrainer",font=("Helveca",11,"bold italic"))
    lib7.pack(pady=5)
    button_start2 = tk.Button(root, text="Entrainer le dataset", command=lancer2)
    button_start2.pack(pady=15)
    
    
    lib4=tk.Label(root, text="Cryptographie  avec Python",font=("Helveca",20,"bold "))
    lib4.pack(pady=40)

    lib3=tk.Label(root, text="Developpé par Roger MAWETE ",font=("Helveca",20,"bold "))
    lib3.pack(pady=10)
    
    lib3=tk.Label(root, text="Université de KINHSASA 2025",font=("Helveca",20,"bold "))
    lib3.pack(side="bottom",pady=10)
    # Lancer l'interface utilisateur
    root.mainloop()


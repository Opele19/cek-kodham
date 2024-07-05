import random

def check_khodam(nama):
    khodam_list = ["ambatron", "Raja khodam", "Harimau Sigma", "Serigala Sumatra", "Ryan Aselole", "Reza Kecap", "Pesulap Hitam", "Rusdi Transformer", "Profesor.Ironi", "Khodam kamu Kabur", "Kapten Curut", "Rengginang", "Bandar Bokep"]
    
    nama_khodam = random.choice(khodam_list)
    print(f"Selamat datang! Check Khodam By naufalarkyy: {nama}")
    print(f"Nama khodam kamu adalah: {nama_khodam}")

# Cara menggunakan toolsnya
nama = input("== Tools Check Khodam By naufalarkyy ==                            Masukkan nama kamu: ")
check_khodam(nama)
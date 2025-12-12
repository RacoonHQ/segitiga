def hitung_luas_segitiga():
    """
    Kalkulator untuk menghitung luas segitiga
    Rumus: Luas = 0.5 * alas * tinggi
    """
    print("=== Kalkulator Luas Segitiga ===")
    
    try:
        # Input alas
        alas = float(input("Masukkan panjang alas (cm): "))
        
        # Input tinggi
        tinggi = float(input("Masukkan tinggi (cm): "))
        
        # Validasi input
        if alas <= 0 or tinggi <= 0:
            print("Error: Alas dan tinggi harus bernilai positif!")
            return
        
        # Hitung luas
        luas = 0.5 * alas * tinggi
        
        # Tampilkan hasil
        print(f"\nHasil Perhitungan:")
        print(f"Alas = {alas} cm")
        print(f"Tinggi = {tinggi} cm")
        print(f"Luas Segitiga = {luas} cm²")
        
    except ValueError:
        print("Error: Masukkan angka yang valid!")
    except Exception as e:
        print(f"Terjadi kesalahan: {e}")

def hitung_luas_dengan_sisi():
    """
    Menghitung luas segitiga menggunakan rumus Heron (jika diketahui 3 sisi)
    """
    print("\n=== Kalkulator Luas Segitiga (Rumus Heron) ===")
    
    try:
        # Input 3 sisi
        sisi_a = float(input("Masukkan panjang sisi a (cm): "))
        sisi_b = float(input("Masukkan panjang sisi b (cm): "))
        sisi_c = float(input("Masukkan panjang sisi c (cm): "))
        
        # Validasi segitiga
        if sisi_a <= 0 or sisi_b <= 0 or sisi_c <= 0:
            print("Error: Semua sisi harus bernilai positif!")
            return
        
        # Validasi ketentuan segitiga
        if (sisi_a + sisi_b <= sisi_c) or (sisi_a + sisi_c <= sisi_b) or (sisi_b + sisi_c <= sisi_a):
            print("Error: Panjang sisi tidak memenuhi ketentuan segitiga!")
            return
        
        # Hitung semi-perimeter
        s = (sisi_a + sisi_b + sisi_c) / 2
        
        # Hitung luas dengan rumus Heron
        luas = (s * (s - sisi_a) * (s - sisi_b) * (s - sisi_c)) ** 0.5
        
        # Tampilkan hasil
        print(f"\nHasil Perhitungan:")
        print(f"Sisi a = {sisi_a} cm")
        print(f"Sisi b = {sisi_b} cm")
        print(f"Sisi c = {sisi_c} cm")
        print(f"Luas Segitiga = {luas:.2f} cm²")
        
    except ValueError:
        print("Error: Masukkan angka yang valid!")
    except Exception as e:
        print(f"Terjadi kesalahan: {e}")

def hitung_keliling_segitiga():
    """
    Kalkulator untuk menghitung keliling segitiga
    Rumus: Keliling = sisi_a + sisi_b + sisi_c
    """
    print("=== Kalkulator Keliling Segitiga ===")
    
    try:
        # Input 3 sisi
        sisi_a = float(input("Masukkan panjang sisi a (cm): "))
        sisi_b = float(input("Masukkan panjang sisi b (cm): "))
        sisi_c = float(input("Masukkan panjang sisi c (cm): "))
        
        # Validasi input
        if sisi_a <= 0 or sisi_b <= 0 or sisi_c <= 0:
            print("Error: Semua sisi harus bernilai positif!")
            return
        
        # Validasi ketentuan segitiga
        if (sisi_a + sisi_b <= sisi_c) or (sisi_a + sisi_c <= sisi_b) or (sisi_b + sisi_c <= sisi_a):
            print("Error: Panjang sisi tidak memenuhi ketentuan segitiga!")
            return
        
        # Hitung keliling
        keliling = sisi_a + sisi_b + sisi_c
        
        # Tampilkan hasil
        print(f"\nHasil Perhitungan:")
        print(f"Sisi a = {sisi_a} cm")
        print(f"Sisi b = {sisi_b} cm")
        print(f"Sisi c = {sisi_c} cm")
        print(f"Keliling Segitiga = {keliling} cm")
        
    except ValueError:
        print("Error: Masukkan angka yang valid!")
    except Exception as e:
        print(f"Terjadi kesalahan: {e}")

def menu():
    """
    Menu utama kalkulator segitiga
    """
    while True:
        print("\n" + "="*40)
        print("KALKULATOR SEGITIGA")
        print("="*40)
        print("1. Hitung Luas (Alas x Tinggi)")
        print("2. Hitung Luas (3 Sisi - Rumus Heron)")
        print("3. Hitung Keliling")
        print("4. Keluar")
        
        pilihan = input("\nPilih metode (1-4): ")
        
        if pilihan == "1":
            hitung_luas_segitiga()
        elif pilihan == "2":
            hitung_luas_dengan_sisi()
        elif pilihan == "3":
            hitung_keliling_segitiga()
        elif pilihan == "4":
            print("Terima kasih telah menggunakan kalkulator ini!")
            break
        else:
            print("Pilihan tidak valid. Silakan coba lagi!")

if __name__ == "__main__":
    menu()
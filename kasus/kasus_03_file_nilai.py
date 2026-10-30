try:
    with open("data/nilai.txt", "r", encoding="utf-8") as file:
        for baris in file:
            nilai = float(baris.strip())

            if 0 <= nilai <= 100:
                print("Nilai:", nilai)
            else:
                print("Nilai tidak valid:", nilai)

except FileNotFoundError:
    print("File nilai.txt tidak ditemukan.")

except ValueError:
    print("Data dalam file harus berupa angka.")
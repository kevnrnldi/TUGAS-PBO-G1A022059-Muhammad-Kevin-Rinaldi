
def hitung_total_harga(belanjaan):
    total_harga = 0
      
    for item in belanjaan:
        total_harga += item["harga"]
    
    return total_harga

def hitung_diskon(total_harga):
    diskon = 0

    if total_harga >= 500000:
        diskon = total_harga * 0.1
    elif total_harga >= 20000:
        diskon = total_harga * 0.05
    
    return diskon

def hitung_total_bayar(total_harga, diskon):
    return total_harga - diskon

def tampilkan_struk_belanja(belanjaan, total_harga, diskon, total_bayar):

    print("Daftar Belanjaan:")
    for item in belanjaan:
        print(f"{item['nama']} - Rp{item['harga']}")
    
    print(f"Total Harga: Rp{total_harga}")
    
    print(f"Diskon: Rp{diskon}")

    print(f"Total Bayar: Rp{total_bayar}")

belanjaan = [
    {"nama": "Buku Tulis", "harga": 10000},
    {"nama": "Pensil", "harga": 5000},
    {"nama": "Buku Gambar", "harga": 15000},
    {"nama": "Spidol", "harga": 10000},
]

total_harga = hitung_total_harga(belanjaan)
diskon = hitung_diskon(total_harga)
total_bayar = hitung_total_bayar(total_harga, diskon)

tampilkan_struk_belanja(belanjaan, total_harga, diskon, total_bayar)

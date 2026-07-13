import pytest 
from src.kasir_toko.kasir import Produk

class TestProduk:
    def test_konstruktor(self):
        """
        SUBSTANSI: Verifikasi Alokasi Memori Konstruktor (Constructor Memory Allocation).
        Memastikan bahwa saat objek 'Produk' diinstansiasi, fungsi '__init__' berhasil
        menangkap argumen input dan menguncinya ke dalam variabel objek (self) dengan benar.
        """
        # 1. Aksi: Membuat objek produk baru (Instansiasi)
        # Kacamata PHP: $produk = new Produk("Kopi Susu", 15000.0, 10);
        produk = Produk("Kopi Susu", 15000.0, 10)

        # 2. Validasi: Memastikan data tersimpan persis di memori tanpa distorsi
        # SINKRONISASI: Memeriksa akurasi nilai literal string dan angka
        assert produk.nama == "Kopi Susu"
        assert produk.harga == 15000.0
        assert produk.stok == 10
import pytest 
from src.kasir_toko.produk import Produk
from src.kasir_toko.keranjang import KeranjangBelanja

class TestKeranjangBelanja: 
    def test_hitung_total_belanja(self):
        """
        SUBSTANSI: Verifikasi Integrasi Logika Komposisi Objek.
        Memasukkan dua objek Produk dengan variasi harga & stok, 
        lalu memastikan kalkulasi total belanja secara matematis akurat.
        """
        # 1. Arrange: Siapkan Keranjang dan 2 Objek Produk berbeda
        keranjang = KeranjangBelanja()
        produk_kopi = Produk("Kopi Susu", 15000.0, 10)
        produk_susu = Produk("Susu", 10000.0, 5)
        # 2. Act: Masukkan produk ke dalam keranjang
        keranjang.tambah_produk(produk_kopi)
        keranjang.tambah_produk(produk_susu)
        # 3. Assert: Total belanja harus (15000 * 10) + (10000 * 5) = 200000.0
        expected_total = 200000.0
        assert keranjang.hitung_total_belanja() == expected_total
    
    def test_tambah_produk_bukan_dari_inisiasi_object_class_produk(self):
        """
        TEST NEGATIF: Memastikan keranjang menolak keras jika ada pihak luar
        yang mencoba memasukkan tipe data ilegal (seperti string biasa) ke keranjang.
        """
        keranjang = KeranjangBelanja()
        with pytest.raises(TypeError) as exc_info:
            keranjang.tambah_produk("Kopi Susu")
        assert "Hanya objek dari kelas Produk yang bisa dimasukkan ke keranjang!" in str(exc_info.value)
import pytest 
from src.kasir_toko.produk_digital import ProdukDigital

class TestProdukDigital:
    def test_inheritance_produk_digital(self):
        """Memastikan properti dasar sukses diwarisi lewat fungsi super()."""
        # Act
        e_book = ProdukDigital(nama="E-Book Python Enterprise", harga=100000.0)
        # Assert: Memeriksa apakah properti dari kelas Produk terpasang sempurna
        assert e_book.nama == "E-Book Python Enterprise"
        assert e_book.harga == 100000.0
        assert e_book.stok == 9999
    
    def test_overriding_kurangi_stok(self):
        """
        SUBSTANSI: Verifikasi Keberhasilan Overriding Metode.
        Memastikan saat kurangi_stok() dipanggil berulang kali, stok ProdukDigital
        tetap konstan di angka 9999 (tidak berkurang sama sekali).
        """
        # Arrange 
        lisensi_os = ProdukDigital(nama="Lisensi OS", harga=100000.0)
        # Act: Mencoba mengurangi stok sebanyak 50 lisensi
        lisensi_os.kurangi_stok(50)
        # Assert: Stok wajib keras bertahan di angka awal (9999)
        assert lisensi_os.stok == 9999
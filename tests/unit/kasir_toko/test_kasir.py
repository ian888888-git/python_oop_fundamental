import pytest 
from src.kasir_toko.produk import Produk

class TestProduk:
    def test_konstruktor(self):
        """
        Memastikan inisialisasi awal tersimpan benar di memori.
        """
        produk = Produk(nama="Kopi Susu", harga=15000.0, stok=10)
        assert produk.nama == "Kopi Susu"
        assert produk.harga == 15000.0
        assert produk.stok == 10
    
    def test_failed_stock_minus(self):
        """Memastikan class Produk menolak stok negatif saat instansiasi."""
        # Aksi & Validasi: Kita sengaja memasukkan stok -5
        # Kita harapkan class Produk melemparkan ValueError
        with pytest.raises(ValueError) as exc_info:
            _ = Produk("Kopi Susu", 15000.0, -5)
        # Memastikan pesan error yang keluar dari class Produk sesuai ekspektasi
        assert "Gagal mengubah stok: Jumlah stok tidak boleh minus!" in str(exc_info.value)
    
    def test_failed_direct_access_to_private_property(self):
        """Memastikan proteksi Name Mangling bekerja."""
        produk = Produk("Kopi Susu", 15000.0, 10)
        with pytest.raises(AttributeError) as exc_info:
            _ = produk.__stok
        # SINKRONISASI: Cukup pastikan kata kunci esensial ini ada di dalam pesan error
        assert "has no attribute" in str(exc_info.value)
        assert "__stok" in str(exc_info.value)
    
    # -------------------------------------------------------------------------
    # CHAPTER 3: PENGUJIAN PYTHONIC GETTER & SETTER (@property)
    # -------------------------------------------------------------------------
    def test_setter_stok_positif_harus_sukses_mengubah_nilai_di_memori(self):
        """
        TEST POSITIF: Memastikan gerbang @stok.setter sukses meloloskan 
        nilai integer positif yang valid dan memperbarui brankas internal.
        """
        # Arrange
        produk = Produk(nama="Kopi Susu", harga=15000.0, stok=10)
        # Act: Mengubah nilai menggunakan gaya variabel publik biasa
        produk.stok = 28 
        # Assert: Memverifikasi lewat getter apakah nilainya berubah menjadi 28
        assert produk.stok == 28

    def test_setter_stok_negatif_angka_minus_harus_melempar_value_error(self):
        """Memastikan setter menolak angka negatif saat update data."""
        produk = Produk(nama="Kopi Susu", harga=15000.0, stok=10)
        with pytest.raises(ValueError) as exc_info:
            produk.stok = -5
        # SINKRONISASI: Menggunakan kata 'negatif' agar konsisten dengan test_failed_stock_minus
        assert "Gagal mengubah stok: Jumlah stok tidak boleh minus!" in str(exc_info.value)
    
    def test_setter_stok_tipe_data_string_salah_harus_melempar_type_error(self):
        """Memastikan setter menolak tipe data string."""
        produk = Produk(nama="Kopi Susu", harga=15000.0, stok=10)
        with pytest.raises(TypeError) as exc_info:
            produk.stok = "10"
        assert "Tipe data stok harus berupa angka bulat" in str(exc_info.value)


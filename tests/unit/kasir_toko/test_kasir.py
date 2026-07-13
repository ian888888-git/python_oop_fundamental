import pytest 
from src.kasir_toko.produk import Produk

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
        # assert produk.stok == 10
    
    def test_failed_stock_minus(self):
        """
        SUBSTANSI: Verifikasi Validasi Internal Kelas (Business Rule Invariant Test).
        Memastikan bahwa class Produk secara mandiri mampu menolak data ilegal (minus)
        dan melemparkan ValueError dari dalam tubuh kelasnya sendiri.
        """
        # Aksi & Validasi: Kita sengaja memasukkan stok -5
        # Kita harapkan class Produk melemparkan ValueError
        with pytest.raises(ValueError) as exc_info:
            produk_paduan = Produk("Kopi Susu", 15000.0, -5)
        # Memastikan pesan error yang keluar dari class Produk sesuai ekspektasi
        assert "Jumlah stok tidak boleh negatif!" in str(exc_info.value)
    
    def test_failed_direct_access_to_private_property(self):
        """
        BENTENG 1 (PROTEKSI LUAR): Memastikan pihak luar tidak bisa mengintip
        atau memanggil 'produk.__stok' secara langsung akibat Name Mangling.
        """
        produk = Produk("Kopi Susu", 15000.0, 10)
        with pytest.raises(AttributeError) as exc_info:
            baca_stok_illegal = produk.__stok
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
        """
        TEST NEGATIF (ATURAN BISNIS): Memastikan gerbang @stok.setter menolak
        angka minus dan melemparkan ValueError dengan pesan literal yang tepat.
        """
        produk = Produk(nama="Kopi Susu", harga=15000.0, stok=10)
        with pytest.raises(ValueError) as exc_info:
            produk.stok = -5
        assert "Jumlah stok tidak boleh negatif!" in str(exc_info.value)
    
    def test_setter_stok_tipe_data_string_salah_harus_melempar_type_error(self):
        """
        TEST NEGATIF (TYPE ASSURANCE): Memastikan gerbang @stok.setter menolak
        jika diberi tipe data teks (string) dan melemparkan TypeError.
        """
        produk = Produk(nama="Kopi Susu", harga=15000.0, stok=10)
        with pytest.raises(TypeError) as exc_info:
            produk.stok = "10"
        assert "stok must be an integer" in str(exc_info.value)


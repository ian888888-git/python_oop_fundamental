import pytest 
from src.kasir_toko.produk import Produk

class TestProduk:
    # =========================================================================
    # 1. PENGUJIAN POSITIF (HAPPY PATH)
    # =========================================================================
    def test_konstruktor(self):
        """
        SUBSTANSI: Memastikan alur normal (Happy Path) berjalan mulus.
        Objek berhasil lahir, dan nilainya bisa diubah dengan angka valid.
        """
        # Test Instansiasi Awal
        produk = Produk(nama="Kopi Susu", harga=15000.0, stok=10)
        assert produk.nama == "Kopi Susu"
        assert produk.harga == 15000.0
        assert produk.stok == 10

        # Test Mutasi Data (Setter)
        produk.stok = 28
        assert produk.stok == 28
    
    # =========================================================================
    # 2. BENTENG PERTAHANAN GANDA (ANTI-MUTASI ILEGAL)
    # =========================================================================
    def test_akses_langsung_ke_variabel_privat_harus_melempar_attribute_error(self):
        """Memastikan pihak luar tidak bisa menembus gembok Name Mangling (__stok)."""
        produk = Produk("Kopi Susu", 15000.0, 10)
        with pytest.raises(AttributeError, match="has no attribute"):
            _ = produk.__stok

    def test_failed_stock_minus(self):
        """Memastikan class Produk menolak stok negatif saat instansiasi."""
        # Aksi & Validasi: Kita sengaja memasukkan stok -5
        # Kita harapkan class Produk melemparkan ValueError
        with pytest.raises(ValueError) as exc_info:
            _ = Produk("Kopi Susu", 15000.0, -5)
        # Memastikan pesan error yang keluar dari class Produk sesuai ekspektasi
        assert "Gagal mengubah stok: Jumlah stok tidak boleh minus!" in str(exc_info.value)
    
    # =========================================================================
    # 3. REFACTORING ENTERPRISE: PARAMETRIZED NEGATIVE TESTING
    # =========================================================================
    @pytest.mark.parametrize(
        "scenario, action, error_type, error_message",
        [
            (
                "Lahir dengan stok minus",
                lambda: Produk("Kopi Susu", 15000.0, -8),
                ValueError,
                "Gagal mengubah stok: Jumlah stok tidak boleh minus!"
            ),
            (
                "Update data menjadi minus",
                lambda: setattr(Produk("Kopi Susu", 15000.0, 10), "stok", -8),
                ValueError,
                "Gagal mengubah stok: Jumlah stok tidak boleh minus!"
            ),
            (
                "Update data menjadi tipe data string",
                lambda: setattr(Produk("Kopi Susu", 15000.0, 10), "stok", "10"),
                TypeError,
                "Gagal mengubah stok: Tipe data stok harus berupa angka bulat (Integer)!"
            )
        ]
    )

    def test_parametrize_execution(self, scenario, action, error_type, error_message):
        """
        SUBSTANSI: Satu pintu pengujian untuk semua skenario buruk (Negative Path).
        Menjamin semua input ilegal diblokir dengan Exception dan pesan literal yang tepat.
        """
        # PyTest akan menjalankan fungsi ini sebanyak 3 kali secara dinamis
        with pytest.raises(error_type) as exc_info:
            action()
        assert error_message in str(exc_info.value)
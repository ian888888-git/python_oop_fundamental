from src.kasir_toko.produk import Produk

class ProdukDigital(Produk):
    """
    SUBSTANSI: Implementasi Pewarisan (Inheritance) & Overriding.
    KACAMATA PHP NATIVE:
    --------------------
    class ProdukDigital extends Produk {
        public function kurangiStok($jumlah) {
            // Overridden: Tidak melakukan apa pun
        }
    }
    """

    def __init__(self, nama: str, harga: float):
        # KACAMATA PHP: parent::__construct($nama, $harga, 9999);
        # Produk digital secara bawaan diatur memiliki stok melimpah di awal
        super().__init__(nama, harga, 9999)
    
    def kurangi_stok(self, jumlah) -> None:
        # KACAMATA PHP: parent::kurangiStok($jumlah);
        """
        [OVERRIDING]
        Menimpa fungsi kurangi_stok() milik kelas Produk.
        Karena produk digital bersifat infinit (e-book/lisensi), panggilan fungsi ini
        sengaja dilewati (bypass) tanpa mengurangi isi brankas memori internal.
        """
        pass
        
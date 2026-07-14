from typing import List
from src.kasir_toko.produk import Produk

class KeranjangBelanja:
    """
    SUBSTANSI: Implementasi Object Composition (Komposisi Objek).
    Kelas ini bertindak sebagai kontainer makro yang menyimpan kumpulan objek Produk.
    KACAMATA PHP NATIVE:
    --------------------
    class KeranjangBelanja {
        private $items = [];
        public function tambahProduk(Produk $product) {
            $this->items[] = $product;
        }
    }
    """
    def __init__(self):
        # Menyimpan kumpulan objek Produk di dalam list privat __daftar_item
        self.__daftar_item: List[Produk] = []
    
    def tambah_produk(self, produk: Produk) -> None:
        """
        Memasukkan objek kelas Produk ke dalam list privat.
        Type Hinting ': Produk' memastikan hanya objek Produk (atau turunannya) 
        yang diizinkan masuk.
        """
        # Type Guard tambahan untuk keamanan runtime
        if not isinstance(produk, Produk):
            raise TypeError("Hanya objek dari kelas Produk yang bisa dimasukkan ke keranjang!")
        self.__daftar_item.append(produk)
    
    @property
    def daftar_item(self) -> List[Produk]:
        """Getter untuk melihat daftar item di dalam keranjang."""
        return self.__daftar_item

    def hitung_total_belanja(self) -> float:
        """
        Mengiterasi seluruh objek Produk di dalam list privat, 
        mengambil properti harga & stok dari masing-masing produk, 
        lalu menjumlahkannya.
        """
        total: float = 0.0
        for item in self.__daftar_item:
            # Mengalikan harga produk dengan sisa stok yang ada
            total += item.harga * item.stok
        return total 

class Produk:
    """
    SUBSTANSI: Implementasi Getter & Setter menggunakan gaya Pythonic (@property).
    KACAMATA PHP NATIVE:
    --------------------
    class Produk {
        private $stok;
        public function getStok() { return $this->stok; }
        public function setStok($jumlah) { ... }
    }
    """
    def __init__(self, nama: str, harga:float, stok:int):
        """
        Konstruktor utama untuk mengalokasikan data produk ke dalam memori.
        'self' di sini bertindak persis seperti '$this' di PHP.
        """
        # Mendaftarkan properti secara langsung ke dalam memori objek
        self.nama = nama 
        self.harga = harga 

        # REVISI KETERANGAN:
        # Melempar stok ke gerbang @setter di bawah untuk divalidasi dulu.
        # Jika lolos validasi angka minus/teks, baru aman disimpan ke memori.
        self.stok: int = stok
    
    @property 
    def stok(self) -> int:
        """
        GERBANG GETTER (BACA DATA)
        Mengizinkan pihak luar membaca variabel privat __stok tanpa kurung ().
        Sintaksis penggunaan: produk.stok
        """
        return self.__stock
    
    @stok.setter
    def stok(self, jumlah:int) -> None:
        """
        GERBANG SETTER (TULIS DATA)
        Memvalidasi setiap upaya pengisian nilai ke 'produk.stok = jumlah'.
        """
        # 1. Type Guard: Memastikan input bukan string atau tipe data ilegal lainnya
        if not isinstance(jumlah, int):
            raise TypeError("Gagal mengubah stok: Tipe data stok harus berupa angka bulat (Integer)!")
        
        # 2. Business Rule Guard: Memastikan stok tidak minus
        if jumlah < 0:
            raise ValueError("Gagal mengubah stok: Jumlah stok tidak boleh minus!")
        
        # Jika lolos semua barikade, simpan ke brankas privat
        self.__stok = jumlah
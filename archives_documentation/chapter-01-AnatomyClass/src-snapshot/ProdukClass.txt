class Produk:
    """
    SUBSTANSI: Anatomi kelas paling dasar untuk memetakan data Produk Fisik.
    KACAMATA PHP NATIVE:
    --------------------
    class Produk {
        public $nama;
        public $harga;
        public $stok;
        
        public function __construct($nama, $harga, $stok) {
            $this->nama = $nama;
            ...
        }
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
        self.stok = stok
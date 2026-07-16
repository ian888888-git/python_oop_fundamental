from src.kasir_toko.produk import Produk
from src.kasir_toko.produk_digital import ProdukDigital
from src.kasir_toko.keranjang import KeranjangBelanja
from src.kasir_toko.pipeline_kasir import PipelineKasir

class Pipeline:
    """
    SUBSTANSI: Master Orchestrator (Dirigen Utama).
    Bertanggung jawab mensimulasikan penangkapan data (Extract), 
    mengalirkannya ke sub-pipeline (Transform), dan siap mengirim ke Lake (Load).
    """
    def __init__(self):
        # Inisialisasi sub-pipeline kasir
        self.sub_pipeline_kasir = PipelineKasir()
    
    def starting_pipeline(self) -> dict:
        # ---------------------------------------------------------
        # 1. EXTRACT STAGE (Simulasi data masuk dari CDC / Sensor)
        # ---------------------------------------------------------
        keranjang = KeranjangBelanja()  
        # Menginstansiasi objek Produk di sini (seolah-olah data baru masuk)
        produk_kopi = Produk("Kopi Susu", 15000.0, 10)
        produk_digital = ProdukDigital("E-Book Python Enterprise", 100000.0)
        # Dimasukkan ke dalam komposer objek
        keranjang.tambah_produk(produk_kopi)
        keranjang.tambah_produk(produk_digital)
        # ---------------------------------------------------------
        # 2. TRANSFORM STAGE (Mengalirkan air data ke dalam pipa)
        # ---------------------------------------------------------
        payload_keranjang = self.sub_pipeline_kasir.transform_keranjang_belanja_to_payload(keranjang)
        print("[Master Pipeline] ✅ Data berhasil ditransformasi!")
        return payload_keranjang
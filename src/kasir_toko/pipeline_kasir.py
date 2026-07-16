from src.kasir_toko.keranjang import KeranjangBelanja

class PipelineKasir:
    """
    SUBSTANSI: Sub-Pipeline / Data Transformer.
    Kelas ini tidak membuat data, melainkan menerima data (KeranjangBelanja) 
    lalah memproses dan mengubah formatnya (Transform) agar siap di-stream.
    """
    def transform_keranjang_belanja_to_payload(self, keranjang: KeranjangBelanja) -> dict:
        """
        Mengekstrak informasi dari objek KeranjangBelanja dan objek-objek Produk 
        di dalamnya menjadi satu payload dictionary standar.
        """
        # Proteksi runtime jika data yang masuk kosong/salah tipe
        if not isinstance(keranjang, KeranjangBelanja):
            raise TypeError("PipelineKasir hanya menerima objek bertipe KeranjangBelanja!")

        daftar_item_terproses= [] 
        # Ekstrak data dari setiap objek Produk yang ada di dalam komposisi keranjang
        for item in keranjang.daftar_item:
            daftar_item_terproses.append({
                "nama_item": item.nama,
                "harga_item": item.harga,
                "jumlah_item": item.stok,
                # Menentukan tipe produk berdasarkan karakteristik objek
                "tipe_produk": "DIGITAL" if item.stok == 9999 else "FISIK"
            })
        # Mengembalikan data matang siap stream
        return {
            "total_nilai_transaksi": keranjang.hitung_total_belanja(),
            "total_jenis_barang": len(keranjang.daftar_item),
            "detail_barang": daftar_item_terproses,
            "status_data": "CLEANED_AND_READY"
        }

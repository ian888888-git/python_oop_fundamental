# OOP Pyhton Fundamental: From PHP Native to Modern Python OOP Transition Guide
Repositori ini dirancang sebagai panduan praktis dan dokumentasi arsitektur untuk memahami konsep **Object-Oriented Programming (OOP) Modern di Python** dengan menggunakan pendekatan serta komparasi langsung dari perspektif **PHP Native (Old-School)**. 
Seluruh kode dalam proyek ini telah terintegrasi dengan pipeline **CI/CD (GitHub Actions)** untuk memastikan kepatuhan tipe data (*Type Assurance*) dan keberhasilan pengujian otomatis sebelum masuk ke lingkungan produksi.

## 🏛️ Arsitektur & Aliran Orkestrasi Data
Sistem ini menerapkan prinsip *Separation of Concerns* (SoC) dan *Domain-Driven Design* (DDD) modular. Aliran eksekusi data pada mode produksi (*Production Run*) berjalan secara linear sebagai berikut:
main.py (Docker Entry) ──> pipeline.py (Master Orchestrator) ──> src/kasir_toko/pipeline_kasir.py ──> Objek Bisnis (Produk/Keranjang)

## Arsitektur Folder Kerja
oop_python_fundamental/
│
├── src/                               # 📁 KODE AKTIF (Versi Terkini & Siap Produksi)
│   ├── __init__.py
│   └── kasir_toko/                    # 📦 Modul Mandiri: Kasir & Inventori
│       ├── __init__.py
│       ├── produk.py                  # Aturan Objek: Produk Fisik
│       ├── produk_digital.py          # Aturan Objek: Produk Digital
│       ├── keranjang.py               # Aturan Objek: Komposisi & Interaksi Objek
│       └── pipeline_kasir.py          # 🏃‍♂️ Runner Internal Modul (Data Pipeline)
│
├── tests/                             # 📁 TES OTOMATIS AKTIF
│   ├── __init__.py
│   └── unit/
│       └── kasir_toko/                # 📂 Folder Tes Khusus Modul Kasir
│           ├── __init__.py
│           └── test_kasir.py          # Unit Testing (PyTest Suite)
│
├── archives_documentation/            # 📦 DOKUMENTASI EVOLUSI KODE PER CHAPTER
│   ├── chapter_01_anatomy/            # Pembekuan Kode setelah Chapter 1 Selesai
│   │   ├── src_snapshot/              
│   │   └── tests_snapshot/            
│   ├── chapter_02_encapsulation/      # Pembekuan Kode setelah Chapter 2 Selesai
│   └── ...                            # Bab Selanjutnya
│
├── main.py                            # 🚀 Titik Masuk Utama Aplikasi (Docker Trigger)
├── pipeline.py                        # 🎛️ Orchestrator Utama Master
├── requirements.txt                   # 📄 Dependensi Framework (PyTest, dll)
└── Dockerfile                         # 📄 Kontainerisasi Lingkungan Kerja Docker


import json 
from pipeline import Pipeline

if __name__ == "__main__": 
    # Eksekusi pipeline oleh Docker trigger
    orchestrator = Pipeline()
    hasil_akhir = orchestrator.starting_pipeline()
    # Cetak hasil akhir dalam format JSON indah untuk pembuktian
    print("\n[Main Result Output to Data Lake Stream]:")
    print(json.dumps(hasil_akhir, indent=4))
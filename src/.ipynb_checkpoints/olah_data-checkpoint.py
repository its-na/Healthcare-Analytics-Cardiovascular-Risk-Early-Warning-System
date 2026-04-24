import pandas as pd

def load_and_preprocess():
    """
    Fungsi ini berfungsi sebagai tahap awal dalam Data Pipeline:
    1. Mengambil data mentah (Extract)
    2. Melakukan pembersihan data (Cleaning)
    3. Membuat fitur baru (Feature Engineering)
    """
    
    # 1. TAHAP LOAD DATA (EXTRACT)
    # Membaca dataset penyakit jantung dari folder data. 
    # Penggunaan path "../" berarti kita naik satu tingkat dari folder 'src' ke folder utama proyek.
    df = pd.read_csv("../data/heart.csv")
    
    # 2. TAHAP DATA CLEANING
    # Menghapus baris yang identik (duplikat) agar tidak terjadi bias dalam analisis statistik.
    # Data kesehatan sering kali memiliki entri ganda yang bisa merusak hasil akurasi model.
    df = df.drop_duplicates()
    
    # 3. TAHAP FEATURE ENGINEERING
    # Membuat fungsi internal untuk menghitung skor risiko berdasarkan kriteria medis sederhana.
    def hitung_risiko(row):
        score = 0
        # Memberikan poin risiko jika usia di atas 50 tahun
        if row['age'] > 50: score += 1
        # Memberikan poin risiko jika kadar kolesterol (chol) di atas 240 mg/dl (batas tinggi)
        if row['chol'] > 240: score += 1
        # Memberikan poin risiko jika tekanan darah (trestbps) di atas 140 mmHg (hipertensi)
        if row['trestbps'] > 140: score += 1
        
        # Jika pasien memiliki 2 atau lebih faktor risiko di atas, dikategorikan sebagai 'High'
        return 'High' if score >= 2 else 'Low'
    
    # Menerapkan fungsi 'hitung_risiko' ke setiap baris dalam dataframe.
    # Kolom 'Risk_Level' ini nantinya sangat berguna untuk visualisasi di Power BI.
    df['Risk_Level'] = df.apply(hitung_risiko, axis=1)
    
    # Mengembalikan data yang sudah rapi dan siap untuk dianalisis lebih lanjut.
    return df
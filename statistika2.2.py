import pandas as pd

# Buat DataFrame dari data yang disediakan
data = {
    'Provinsi': ['KALIMANTAN BARAT', 'KALIMANTAN TENGAH', 'KALIMANTAN SELATAN', 'KALIMANTAN TIMUR', 'KALIMANTAN UTARA'],
    'DU-2018': [14, 20, 18, 29, 33],
    'DU-2017': [16, 20, 19, 29, 37],
    'DU-2016': [14, 21, 18, 25, 32],
    'DG-2018': [3, 4, 5, 8, 6],
    'DG-2017': [4, 4, 5, 8, 9],
    'DG-2016': [3, 4, 4, 7, 8],
    'P-2018': [160, 222, 151, 217, 238],
    'P-2017': [142, 199, 118, 207, 300],
    'P-2016': [90, 156, 100, 187, 211],
    'B-2018': [81, 131, 107, 96, 137],
    'B-2017': [73, 99, 53, 84, 126],
    'B-2016': [41, 57, 47, 65, 73],
    'FR-2018': [15, 22, 23, 33, 33],
    'FR-2017': [18, 17, 16, 26, 26],
    'FR-2016': [12, 15, 13, 21, 19],
    'KM-2018': [8, 13, 11, 11, 26],
    'KM-2017': [10, 12, 18, 7, 42],
    'KM-2016': [11, 26, 21, 6, 33],
    'KL-2018': [10, 10, 8, 7, 11],
    'KL-2017': [10, 10, 8, 7, 11],
    'KL-2016': [6, 9, 7, 6, 6],
    'GZ-2018': [12, 15, 11, 9, 14],
    'GZ-2017': [12, 15, 11, 9, 14],
    'GZ-2016': [8, 15, 10, 7, 9]
}

df = pd.DataFrame(data)

# Menghilangkan kolom 'Provinsi' karena bukan data numerik
df = df.drop(columns=['Provinsi'])

# Mengganti nilai yang hilang dengan 0
df = df.fillna(0)

# Menghitung matriks korelasi
corr_matrix = df.corr()

# Mencetak matriks korelasi dengan format yang rapi
print("Matriks Korelasi:")
print(corr_matrix)

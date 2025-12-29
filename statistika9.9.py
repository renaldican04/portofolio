import pandas as pd

# Dataframe yang sama seperti sebelumnya
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

# Menghitung mean, median, dan mode untuk setiap variabel
mean_values = df.drop('Provinsi', axis=1).mean().to_dict()
median_values = df.drop('Provinsi', axis=1).median().to_dict()
mode_values = df.drop('Provinsi', axis=1).mode().iloc[0].to_dict()

# Membuat DataFrame hasil
summary_df = pd.DataFrame({
    'Mean': mean_values,
    'Median': median_values,
    'Mode': mode_values
}).transpose()

print(summary_df)

# Interpretasi hasil
print("\nInterpretasi hasil:")
print("1. Nilai Mean (rata-rata) memberikan gambaran umum tentang nilai tengah dari data, tetapi bisa dipengaruhi oleh nilai ekstrem.")
print("2. Nilai Median memberikan nilai tengah dari data yang telah diurutkan, dan lebih tahan terhadap nilai ekstrem.")
print("3. Nilai Mode adalah nilai yang paling sering muncul dalam data.")

print("\nAnalisis kecenderungan data:")
for col in summary_df.columns:
    print(f"\n{col}:")
    print(f"Mean: {summary_df.at['Mean', col]}")
    print(f"Median: {summary_df.at['Median', col]}")
    print(f"Mode: {summary_df.at['Mode', col]}")
    if summary_df.at['Mean', col] == summary_df.at['Median', col] == summary_df.at['Mode', col]:
        print("  Semua nilai cenderung sama, menunjukkan distribusi data yang simetris.")
    elif summary_df.at['Mean', col] > summary_df.at['Median', col] > summary_df.at['Mode', col]:
        print("  Data cenderung memiliki skewed ke kanan (positif skew).")
    elif summary_df.at['Mean', col] < summary_df.at['Median', col] < summary_df.at['Mode', col]:
        print("  Data cenderung memiliki skewed ke kiri (negatif skew).")
    else:
        print("  Tidak ada kecenderungan yang jelas.")

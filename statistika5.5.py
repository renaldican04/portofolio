import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

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

plt.figure(figsize=(15, 15))  # increase figure size
sns.set_style("whitegrid")
sns.heatmap(df.set_index('Provinsi').T, annot=True, cmap='coolwarm', square=True, linewidths=0.5, linecolor='black', cbar_kws={'shrink': 0.5}, fmt='.0f')  # add fmt to format numbers
plt.title('Heatmap Distribusi Data', fontsize=18)
plt.xlabel('Provinsi', fontsize=14)
plt.ylabel('Tahun dan Kategori', fontsize=14)
plt.xticks(rotation=45, ha='center', fontsize=12)  # increase font size
plt.yticks(rotation=0, ha='right', fontsize=12)  # increase font size
plt.tight_layout()
plt.subplots_adjust(left=0.2, bottom=0.2)  # adjust layout to center the heatmap
plt.show()

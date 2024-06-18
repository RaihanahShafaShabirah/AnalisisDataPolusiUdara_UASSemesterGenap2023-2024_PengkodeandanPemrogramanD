import pandas as pd

# Membaca data dari file CSV
df = pd.read_csv('polusi_udara.csv')
print(df.head())

# Melakukan deskripsi statistik
print(df.describe())

import matplotlib.pyplot as plt
import seaborn as sns

# Plot hubungan antara PM2.5 dan Emisi Pabrik CO2
plt.figure(figsize=(10, 6))
sns.scatterplot(x='PM2.5 (µg/m³)', y='Emisi Pabrik CO2 (ton)', data=df)
plt.title('Hubungan antara PM2.5 dan Emisi Pabrik CO2')
plt.xlabel('PM2.5 (µg/m³)')
plt.ylabel('Emisi Pabrik CO2 (ton)')
plt.show()

# Plot hubungan antara PM2.5 dan Emisi Kendaraan CO2
plt.figure(figsize=(10, 6))
sns.scatterplot(x='PM2.5 (µg/m³)', y='Emisi Kendaraan CO2 (g/km)', data=df)
plt.title('Hubungan antara PM2.5 dan Emisi Kendaraan CO2')
plt.xlabel('PM2.5 (µg/m³)')
plt.ylabel('Emisi Kendaraan CO2 (g/km)')
plt.show()

import statsmodels.api as sm

# Variabel independen
X = df[['Emisi Pabrik CO2 (ton)', 'Emisi Pabrik NOx (ton)', 'Emisi Pabrik SO2 (ton)',
        'Emisi Kendaraan CO2 (g/km)', 'Emisi Kendaraan NOx (g/km)', 'Emisi Kendaraan SO2 (g/km)']]
# Variabel dependen
y = df['PM2.5 (µg/m³)']

# Menambahkan konstanta (intercept) ke model
X = sm.add_constant(X)

# Membuat model regresi
model = sm.OLS(y, X).fit()

# Melihat ringkasan hasil regresi
print(model.summary())

from statsmodels.graphics.regressionplots import plot_partregress_grid

# Membuat plot partial regression
fig = plt.figure(figsize=(12, 8))
plot_partregress_grid(model, fig=fig)
plt.tight_layout()
plt.show()
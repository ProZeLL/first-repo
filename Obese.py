import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
import matplotlib.pyplot as plt
from scipy.stats import f_oneway
from scipy.stats import chi2_contingency
import seaborn as sns


df = pd.read_csv('D:/kuliah/kuliah/Sem 5/Pengantar DS/tugas/04-Regresi data obesitas/ObesityDataSet_raw_and_data_sinthetic.csv')

# Membulatkan umur ke bawah (floor)
df['Age'] = np.floor(df['Age'])

# Membuat height menjadi 2 angka di belakang koma
df['Height'] = df['Height'].round(2)

# Membulatkan FCVC ke bilangan bulat terdekat
df['FCVC'] = df['FCVC'].round()

# Membulatkan NCP ke bilangan bulat terdekat
df['NCP'] = df['NCP'].round()

# Membulatkan CH2O ke bilangan bulat terdekat
df['CH2O'] = df['CH2O'].round()

# Membulatkan TUE ke bilangan bulat terdekat
df['TUE'] = df['TUE'].round()

df['FAF'] = df['FAF'].round()

#----------------------------------------------------------------------------------
#Transformasi atribut jadi ordinal FAVC, FCVC, NCP, CAEC, CH2O, SCC, CALC, AGE
#Yang bagus, angkanya makin besar
df['family_history_with_overweight'] = df['family_history_with_overweight'].map({'yes': 0, 'no': 1})
df['SMOKE'] = df['SMOKE'].map({'yes':0, 'no':1})
df['FAVC'] = df['FAVC'].map({'yes': 0, 'no': 1})
df['NCP'] = df['NCP'].map({1:4, 2:3, 3:2, 4:1})
df['CAEC'] = df['CAEC'].map({'no':4, 'Sometimes':3, 'Frequently':2, 'Always':1})
df['SCC'] = df['SCC'].map({'yes':1, 'no':0})
df['CALC'] = df['CALC'].map({'no':4, 'Sometimes':3, 'Frequently':2, 'Always':1})

# Membuat kolom BMI berdasarkan Weight dan Height dengan rumus: 
#        Weight
# BMI = --------
#       (Height)^2
df['BMI'] = df['Weight'] / (df['Height'] ** 2)

# Bulatkan BMI menjadi hanya 2 angka di belakang koma untuk memudahkan perhitungan
df['BMI'] = df['BMI'].round(2)

df.to_excel("Data bersih.xlsx", index=False)

# -------------- ANOVA TEST --------------

# Buat Tes ANOVA untuk FAVC
# Pisahkan data berdasarkan kategori
groups = [df[df['FAVC'] == category]['BMI'] for category in df['FAVC'].unique()]
# Hitung ANOVA
f_stat, p_value = f_oneway(*groups)
print(f"P-value BMI-FAVC: {p_value}")

# Buat Tes ANOVA untuk FCVC
# Pisahkan data berdasarkan kategori
groups = [df[df['FCVC'] == category]['BMI'] for category in df['FCVC'].unique()]
# Hitung ANOVA
f_stat, p_value = f_oneway(*groups)
print(f"P-value BMI-FCVC: {p_value}")

# Buat Tes ANOVA untuk NCP
# Pisahkan data berdasarkan kategori
groups = [df[df['NCP'] == category]['BMI'] for category in df['NCP'].unique()]
# Hitung ANOVA
f_stat, p_value = f_oneway(*groups)
print(f"P-value BMI-NCP: {p_value}")

# Buat Tes ANOVA untuk CAEC
# Pisahkan data berdasarkan kategori
groups = [df[df['CAEC'] == category]['BMI'] for category in df['CAEC'].unique()]
# Hitung ANOVA
f_stat, p_value = f_oneway(*groups)
print(f"P-value BMI-CAEC: {p_value}")

# Buat Tes ANOVA untuk CH2O
# Pisahkan data berdasarkan kategori
groups = [df[df['CH2O'] == category]['BMI'] for category in df['CH2O'].unique()]
# Hitung ANOVA
f_stat, p_value = f_oneway(*groups)
print(f"P-value BMI-CH2O: {p_value}")

# Buat Tes ANOVA untuk SCC
# Pisahkan data berdasarkan kategori
groups = [df[df['SCC'] == category]['BMI'] for category in df['SCC'].unique()]
# Hitung ANOVA
f_stat, p_value = f_oneway(*groups)
print(f"P-value BMI-SCC: {p_value}")

# Buat Tes ANOVA untuk CALC
# Pisahkan data berdasarkan kategori
groups = [df[df['CALC'] == category]['BMI'] for category in df['CALC'].unique()]
# Hitung ANOVA
f_stat, p_value = f_oneway(*groups)
print(f"P-value BMI-CALC: {p_value}")


# -------------- CHI-SQUARE TEST --------------
# Buat tabel kontingensi untuk FAVC
contingency_table = pd.crosstab(df['NObeyesdad'], df['FAVC'])
# Lakukan uji Chi-Square
chi2, p_value, dof, expected = chi2_contingency(contingency_table)
print(f"P-value Nobeyesdad-FAVC: {p_value}")

# Buat tabel kontingensi untuk FCVC
contingency_table = pd.crosstab(df['NObeyesdad'], df['FCVC'])
# Lakukan uji Chi-Square
chi2, p_value, dof, expected = chi2_contingency(contingency_table)
print(f"P-value Nobeyesdad-FCVC: {p_value}")

# Buat tabel kontingensi untuk NCP
contingency_table = pd.crosstab(df['NObeyesdad'], df['NCP'])
# Lakukan uji Chi-Square
chi2, p_value, dof, expected = chi2_contingency(contingency_table)
print(f"P-value Nobeyesdad-NCP: {p_value}")

# Buat tabel kontingensi untuk CAEC
contingency_table = pd.crosstab(df['NObeyesdad'], df['CAEC'])
# Lakukan uji Chi-Square
chi2, p_value, dof, expected = chi2_contingency(contingency_table)
print(f"P-value Nobeyesdad-CAEC: {p_value}")

# Buat tabel kontingensi untuk CH2O
contingency_table = pd.crosstab(df['NObeyesdad'], df['CH2O'])
# Lakukan uji Chi-Square
chi2, p_value, dof, expected = chi2_contingency(contingency_table)
print(f"P-value Nobeyesdad-CH2O: {p_value}")
 
# Buat tabel kontingensi untuk SCC
contingency_table = pd.crosstab(df['NObeyesdad'], df['SCC'])
# Lakukan uji Chi-Square
chi2, p_value, dof, expected = chi2_contingency(contingency_table)
print(f"P-value Nobeyesdad-SCC: {p_value}")

# Buat tabel kontingensi untuk CALC
contingency_table = pd.crosstab(df['NObeyesdad'], df['CALC'])
# Lakukan uji Chi-Square
chi2, p_value, dof, expected = chi2_contingency(contingency_table)
print(f"P-value Nobeyesdad-CALC: {p_value}")


#------------ VISUALISASI REGRESI LINEAR -------------
# Plotting FAVC
# Ubah Yes menjadi 1 dan No menjadi 0
# # Buat scatter plot
# sns.lmplot(x='Weight', y='BMI', data=df, hue='FAVC', markers=['o', 's'], aspect=1.5, ci=None)
# # Labeling
# plt.title('Hubungan antara BMI, Berat, dan Sering atau tidaknya mengkonsumsi makanan berkalori tinggi')
# plt.xlabel('Weight')
# plt.ylabel('BMI')
# # Menampilkan plot
# plt.show()


# Plotting FCVC
# # Buat scatter plot
# sns.lmplot(x='Height', y='BMI', data=df, hue='FCVC', markers=['o', 's', 'p'], aspect=1.5, ci=None)
# # Labeling
# plt.title('Hubungan antara BMI, Tinggi, dan Sering atau tidaknya mengkonsumsi sayuran')
# plt.xlabel('Height')
# plt.ylabel('BMI')
# # Menampilkan plot
# plt.show()


# Plotting NCP
# # Buat scatter plot
# sns.lmplot(x='Age', y='BMI', data=df, hue='NCP', markers=['o', 's', 'p', '^'], aspect=1.5, ci=None)
# # Labeling
# plt.title('Hubungan antara BMI, Usia, dan Sering atau tidaknya mengkonsumsi sayuran')
# plt.xlabel('Age')
# plt.ylabel('BMI')
# # Menampilkan plot
# plt.show()



# Plotting CAEC
# # Buat scatter plot
# sns.lmplot(x='Age', y='BMI', data=df, hue='CAEC', markers=['o', 's', 'p', '^'], aspect=1.5, ci=None)
# # Labeling
# plt.title('Hubungan antara BMI, Usia, dan Frekuensi ngemil')
# plt.xlabel('Age')
# plt.ylabel('BMI')
# # Menampilkan plot
# plt.show()


# Buat scatter plot CH2O
# sns.lmplot(x='Age', y='BMI', data=df, hue='CH2O', markers=['o', 's', 'p'], aspect=1.5, ci=None)
# # Labeling
# plt.title('Hubungan antara BMI, Usia, dan Konsumsi Air Minum Harian')
# plt.xlabel('Age')
# plt.ylabel('BMI')
# # Menampilkan plot
# plt.show()


# Buat scatter plot SCC
# sns.lmplot(x='Age', y='BMI', data=df, hue='SCC', markers=['o', 's'], aspect=1.5, ci=None)
# # Labeling
# plt.title('Hubungan antara BMI, Usia, dan Kebiasaan mengontrol kalori makanan')
# plt.xlabel('Age')
# plt.ylabel('BMI')
# # Menampilkan plot
# plt.show()


# Buat scatter plot CALC
# sns.lmplot(x='Age', y='BMI', data=df, hue='CALC', markers=['o', 's', 'p', '^'], aspect=1.5, ci=None)
# # Labeling
# plt.title('Hubungan antara BMI, Usia, dan Frekuensi mengkonsumsi alkohol')
# plt.xlabel('Age')
# plt.ylabel('BMI')
# # Menampilkan plot
# plt.show()

#------------------------------------------
#pearson BUAT LIAT HUBUNGAN ANTARA NUMERIKAL DAN NUMERIKAL
def correlation_heatmap(li):
    correlations = li.corr()

    fig, ax = plt.subplots(figsize=(13,13))
    sns.heatmap(correlations, vmax=1.0, center=0, fmt='.2f',
                square=True, linewidths=.5, annot=True, cbar_kws={"shrink": .70})
    plt.show();
    
correlation_heatmap(df[['Age', 'Height', 'Weight', 'BMI']])

print(df.columns)

#-------------------------------------------

# Memilih kolom-kolom yang relevan untuk analisis korelasi
columns_of_interest = ['Age', 'Height', 'Weight', 'family_history_with_overweight',
       'FAVC', 'FCVC', 'NCP', 'CAEC', 'SMOKE', 'CH2O', 'SCC', 'FAF', 'TUE',
       'CALC', 'BMI']

# Menghitung korelasi Spearman antar atribut
spearman_correlation = df[columns_of_interest].corr(method='spearman')

#HASIL SPEARMAN = FAVC, FCVC, CAEC, SCC, AGE
#FAVC = BMI, FAMILY, SCC
#FCVC = BMI
#CAEC = BMI, FAMILY, FAVC
#SCC = BMI, FAMILY, FAVC

#------------------------------------------------
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

# Definisikan fitur (X) dan target (y)
X = df[['family_history_with_overweight', 'SCC']]  # Contoh fitur
y = df['FAVC']  # Target

# Bagi data menjadi training dan testing set
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Model regresi
model = LinearRegression()
model.fit(X_train, y_train)

# Prediksi konsumsi sayuran numerik
df['FAVC_predicted'] = model.predict(X)
df[['FAVC', 'FAVC_predicted']].head()

#----------------------------------------------
# Definisikan fitur (X) dan target (y)
X = df[['BMI']]  # Contoh fitur
y = df['FCVC']  # Target

# Bagi data menjadi training dan testing set
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Model regresi
model = LinearRegression()
model.fit(X_train, y_train)

# Prediksi konsumsi sayuran numerik
df['FCVC_predicted'] = model.predict(X)
df[['FCVC', 'FCVC_predicted']].head()

#----------------------------------------------
# Definisikan fitur (X) dan target (y)
X = df[['family_history_with_overweight', 'FAVC']]  # Contoh fitur
y = df['CAEC']  # Target

# Bagi data menjadi training dan testing set
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Model regresi
model = LinearRegression()
model.fit(X_train, y_train)

# Prediksi konsumsi sayuran numerik
df['CAEC_predicted'] = model.predict(X)
df[['CAEC', 'CAEC_predicted']].head()

#----------------------------------------------
# Definisikan fitur (X) dan target (y)
X = df[['family_history_with_overweight', 'FAVC']]  # Contoh fitur
y = df['SCC']  # Target

# Bagi data menjadi training dan testing set
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Model regresi
model = LinearRegression()
model.fit(X_train, y_train)

# Prediksi konsumsi sayuran numerik
df['SCC_predicted'] = model.predict(X)
df[['SCC', 'SCC_predicted']].head()


#------------------------------------------
columns_of_interest2 = ['FAVC_predicted',
'CAEC_predicted', 'SCC_predicted', 'Age', 'BMI']

# Menghitung korelasi Spearman antar atribut
spearman_correlation2 = df[columns_of_interest2].corr(method='spearman')

#FAVC, CAEC, SCC, AGE

#----------------------------------------------------------
# Pilih atribut sebagai fitur (X) dan target (y)
X = df[['FAVC_predicted', 'CAEC_predicted', 'SCC_predicted', 'Age']]  # Fitur
y = df['BMI']  # Target

# Bagi data menjadi data latih dan uji (80% latih, 20% uji)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Inisialisasi model regresi linear
model = LinearRegression()

# Latih model menggunakan data latih
model.fit(X_train, y_train)

# Prediksi data uji
y_pred = model.predict(X_test)

# Evaluasi model
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

# Output hasil evaluasi
# Menghitung nilai rata-rata y_test
y_mean = np.mean(y_test)

# Menghitung SSTO (Total Sum of Squares)
SSTO = np.sum((y_test - y_mean) ** 2)

# Menghitung SSR (Regression Sum of Squares)
SSR = np.sum((y_pred - y_mean) ** 2)

# Menghitung SSE (Error Sum of Squares)
SSE = np.sum((y_test - y_pred) ** 2)

# Menghitung R-squared
R_squared = SSR / SSTO

# Output hasil perhitungan
print(f"SSTO (Total Sum of Squares): {SSTO:.2f}")
print(f"SSR (Regression Sum of Squares): {SSR:.2f}")
print(f"SSE (Error Sum of Squares): {SSE:.2f}")
print(f"R-squared (R^2): {R_squared:.2f}")

# Membuat scatter plot antara nilai aktual dan prediksi
plt.figure(figsize=(10, 6))
plt.scatter(y_test, y_pred, alpha=0.6, color='blue')
plt.plot([y_test.min(), y_test.max()], [y_test.min(), y_test.max()], color='red', linewidth=2, label='Ideal Fit')

# Menambahkan judul dan label
plt.title('Prediksi vs Nilai Aktual (BMI)', fontsize=16)
plt.xlabel('Nilai Aktual (y_test)', fontsize=14)
plt.ylabel('Nilai Prediksi (y_pred)', fontsize=14)
plt.legend()
plt.grid(True)

# Menampilkan plot
plt.show()
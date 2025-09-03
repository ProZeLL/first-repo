# -*- coding: utf-8 -*-
"""
Created on Sat Nov 16 14:41:49 2024

@author: ASUS
"""
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

data_raw = pd.read_csv("C:/Users/azrie/OneDrive/UNPAR/Materi Pembelajaran Informatika/Semester 5/Pengantar dan Aplikasi Data Science/Tugas/T03-1-09/Absenteeism_at_work.csv")

#buang kolom yang menurut kita ga kepakai
#   buang Id (cuman tanda pengenal), 
#   disciplinary failure (setelah difilter semua jadi 0, jadi ga guna), 
#   Weight dan height (karena sudah tergambar di BMI)

hasil_hapus_kolom = data_raw.drop(columns=['ID', 'Disciplinary failure', 'Weight', 'Height'])

#filter 1 (hilangin absenteeism time == 0)
hasil_filter_1 = hasil_hapus_kolom[hasil_hapus_kolom["Absenteeism time in hours"] > 0]

#cek yang ada NaN
print(hasil_filter_1.isna().sum())

#yang ada NaN cuman di transportation expense
#isi dengan class central tendency
hasil_isi_nan = hasil_filter_1.copy()
hasil_isi_nan.loc[:, "Transportation expense"] = hasil_isi_nan["Transportation expense"].fillna(
    hasil_isi_nan.groupby("Reason for absence")["Transportation expense"].transform("mean"))


#ubah penulisan workload jadi float
hasil_isi_nan["Work load Average/day "] = hasil_isi_nan["Work load Average/day "].str.replace(',', '.').astype(float)

#ubah kolom numerikal jadi kategorikal
#kolom yang lain dibagi berdasarkan median, BMI ikutin standard
median_semua = hasil_isi_nan.median()

#transportation expense (0 = value < 225, 1 = value >= 225)
hasil_isi_nan['Transportation expense'] = hasil_isi_nan['Transportation expense'].apply(lambda x: 0 if x < 225 else 1)

#distance (0 = value < 26, 1 = value >= 26)
hasil_isi_nan['Distance from Residence to Work'] = hasil_isi_nan['Distance from Residence to Work'].apply(lambda x: 0 if x < 26 else 1)

#service time (0 = value < 13, 1 = value >= 13)
hasil_isi_nan['Service time'] = hasil_isi_nan['Service time'].apply(lambda x: 0 if x < 13 else 1)

#age (0 = value < 37, 1 = value >= 37)
hasil_isi_nan['Age'] = hasil_isi_nan['Age'].apply(lambda x: 0 if x < 37 else 1)

#workload (0 = value < 264.249, 1 = value >= 264.249)
hasil_isi_nan['Work load Average/day '] = hasil_isi_nan['Work load Average/day '].apply(lambda x: 0 if x < 264.249 else 1)

#hit target (0 = value < 95, 1 = value >= 95)
hasil_isi_nan['Hit target'] = hasil_isi_nan['Hit target'].apply(lambda x: 0 if x < 95 else 1)

#son (0 = value < 1, 1 = value >= 1)
hasil_isi_nan['Son'] = hasil_isi_nan['Son'].apply(lambda x: 0 if x < 1 else 1)

#pet (0 = value <= 0, 1 = value > 0)
hasil_isi_nan['Pet'] = hasil_isi_nan['Pet'].apply(lambda x: 0 if x <= 0 else 1)

#BMI (  0 = value < 18.5, 
#       1 = 18.5 <= value <= 22.9,
#       2 = 23 <= value <= 24.9,
#       3 = 25 <= value <= 29.9,)
#       4 = value >= 30)
hasil_isi_nan['Body mass index'] = hasil_isi_nan['Body mass index'].apply(
    lambda x: 0 if x < 18.5 
    else 1 if 18.5 <= x <= 22.9 
    else 2 if 23 <= x <= 24.9 
    else 3 if 25 <= x <= 29.9 
    else 4
)

#absenteeism time in hours (0 = value < 3, 1 = value >= 3)
#hasil_isi_nan['Absenteeism time in hours'] = hasil_isi_nan['Absenteeism time in hours'].apply(lambda x: 0 if x < 3 else 1)

#hasil_isi_nan.to_excel("data final.xlsx", index=False)

# month, day, seasons, transportatiom, distance, service time


#-------------------------------------------------------------------

#coba ubah reason jadi kategorikal
# hasil_isi_nan['Reason for absence'] = hasil_isi_nan['Reason for absence'].apply(lambda x: 0 if 1 <= x <= 21 else 1)

# hasil_isi_nan.to_excel("data final2.xlsx", index=False)

print(hasil_isi_nan.columns)


#pearson
def correlation_heatmap(li):
    correlations = li.corr()

    fig, ax = plt.subplots(figsize=(13,13))
    sns.heatmap(correlations, vmax=1.0, center=0, fmt='.2f',
                square=True, linewidths=.5, annot=True, cbar_kws={"shrink": .70})
    plt.show()
    
correlation_heatmap(hasil_isi_nan[['Reason for absence', 'Month of absence', 'Day of the week', 'Seasons',
       'Transportation expense', 'Distance from Residence to Work',
       'Service time', 'Age', 'Work load Average/day ', 'Hit target',
       'Education', 'Son', 'Social drinker', 'Social smoker', 'Pet',
       'Body mass index', 'Absenteeism time in hours']])

#correlation_heatmap(non_ICD[['Transportation expense','Distance from Residence to Work','Service time','Age','Work load Average/day ','Hit target','Son','Pet','Weight','Height','Body mass index','Absenteeism time in hours']])

# 
# 
# #heatmap 2 variabel
# # Function to create and display the heatmap for a given group
# def plot_heatmap(group, title, variabel1, variabel2):
#     plt.figure(figsize=(12, 6))  # Adjust figure size as needed
#     heatmap_data = pd.crosstab(group[variabel1], group[variabel2])
#     sns.heatmap(heatmap_data, annot=True, fmt='d', cmap='viridis')
#     plt.title(title)
#     plt.show()
# 
# # Plot heatmaps for both groups
# plot_heatmap(isi_nan, 'Semua, Reason, ID', "Reason for absence", "ID")
# plot_heatmap(non_ICD, 'Non ICD, Reason, ID', "Reason for absence", "ID")
# plot_heatmap(ICD, 'ICD, Reason, ID', "Reason for absence", "ID")
# 
# correlation_heatmap(isi_nan[['Transportation expense','Distance from Residence to Work','Service time','Age','Work load Average/day ','Hit target','Son','Pet','Weight','Height','Body mass index','Absenteeism time in hours']])
# 
# 
#

# Create features for modelling
features = ['Absenteeism time in hours', 'Distance from Residence to Work', 'Work load Average/day ', 'Day of the week', 'Social drinker', 'Body mass index', 'Education']
X = hasil_isi_nan[features]
y = hasil_isi_nan['Reason for absence']

from sklearn.model_selection import train_test_split

# Splitting data into train data and test data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)



#########################################################

#MACHINE LEARNING


# Importing necessary libraries
from sklearn.ensemble import RandomForestClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report, precision_score, recall_score


# Assuming X_train, X_test, y_train, and y_test are already defined

### Random Forest
# Create Random Forest model
model1 = RandomForestClassifier(n_estimators=100, random_state=42)
model1.fit(X_train, y_train)

# Predictions
y_pred1 = model1.predict(X_test)

# Evaluation
print("Random Forest - Classification Report:")
print(classification_report(y_test, y_pred1))

# Confusion Matrix for Random Forest
conf_matrix1 = confusion_matrix(y_test, y_pred1)
print("Confusion Matrix:")
print(conf_matrix1)

# Visualization of Confusion Matrix with heatmap
fig, ax = plt.subplots(figsize=(10, 10))
sns.heatmap(conf_matrix1, annot=True, fmt='d', cmap='Blues')
plt.xlabel('Predicted')
plt.ylabel('Actual')
plt.title('Random Forest Confusion Matrix')
plt.show()

# Accuracy
accuracy1 = accuracy_score(y_test, y_pred1)
print(f"Random Forest Accuracy: {accuracy1:.2f}")

# Precision and Recall
precision_macro = precision_score(y_test, y_pred1, average='macro', zero_division=0)
recall_macro = recall_score(y_test, y_pred1, average='macro', zero_division=0)
precision_weighted = precision_score(y_test, y_pred1, average='weighted', zero_division=0)
recall_weighted = recall_score(y_test, y_pred1, average='weighted', zero_division=0)

print(f"Macro-Average Precision: {precision_macro:.2f}")
print(f"Macro-Average Recall: {recall_macro:.2f}")
print(f"Weighted-Average Precision: {precision_weighted:.2f}")
print(f"Weighted-Average Recall: {recall_weighted:.2f}")

### Decision Tree
# Create Decision Tree model
model2 = DecisionTreeClassifier(random_state=42)
model2.fit(X_train, y_train)

# Predictions
y_pred2 = model2.predict(X_test)

# Evaluation
print("\nDecision Tree - Classification Report:")
print(classification_report(y_test, y_pred2))

# Confusion Matrix for Decision Tree
conf_matrix2 = confusion_matrix(y_test, y_pred2)
print("Confusion Matrix:")
print(conf_matrix2)

# Visualization of Confusion Matrix with heatmap
fig, ax = plt.subplots(figsize=(10,10))
sns.heatmap(conf_matrix2, annot=True, fmt='d', cmap='Greens')
plt.xlabel('Predicted')
plt.ylabel('Actual')
plt.title('Decision Tree Confusion Matrix')
plt.show()

# Accuracy
accuracy2 = accuracy_score(y_test, y_pred2)
print(f"Decision Tree Accuracy: {accuracy2:.2f}")


# Precision and Recall
precision_macro = precision_score(y_test, y_pred1, average='macro', zero_division=0)
recall_macro = recall_score(y_test, y_pred1, average='macro', zero_division=0)
precision_weighted = precision_score(y_test, y_pred1, average='weighted', zero_division=0)
recall_weighted = recall_score(y_test, y_pred1, average='weighted', zero_division=0)

print(f"Macro-Average Precision: {precision_macro:.2f}")
print(f"Macro-Average Recall: {recall_macro:.2f}")
print(f"Weighted-Average Precision: {precision_weighted:.2f}")
print(f"Weighted-Average Recall: {recall_weighted:.2f}")

### Logistic Regression
# Create Logistic Regression model
model3 = LogisticRegression(random_state=42, max_iter=1000)
model3.fit(X_train, y_train)

# Predictions
y_pred3 = model3.predict(X_test)

# Evaluation
print("\nLogistic Regression - Classification Report:")
print(classification_report(y_test, y_pred3))

# Confusion Matrix for Logistic Regression
conf_matrix3 = confusion_matrix(y_test, y_pred3)
print("Confusion Matrix:")
print(conf_matrix3)

# Visualization of Confusion Matrix with heatmap
fig, ax = plt.subplots(figsize=(10,10))
sns.heatmap(conf_matrix3, annot=True, fmt='d', cmap='Oranges')
plt.xlabel('Predicted')
plt.ylabel('Actual')
plt.title('Logistic Regression Confusion Matrix')
plt.show()

# Accuracy
accuracy3 = accuracy_score(y_test, y_pred3)
print(f"Logistic Regression Accuracy: {accuracy3:.2f}")

# Precision and Recall
precision_macro = precision_score(y_test, y_pred1, average='macro', zero_division=0)
recall_macro = recall_score(y_test, y_pred1, average='macro', zero_division=0)
precision_weighted = precision_score(y_test, y_pred1, average='weighted', zero_division=0)
recall_weighted = recall_score(y_test, y_pred1, average='weighted', zero_division=0)

print(f"Macro-Average Precision: {precision_macro:.2f}")
print(f"Macro-Average Recall: {recall_macro:.2f}")
print(f"Weighted-Average Precision: {precision_weighted:.2f}")
print(f"Weighted-Average Recall: {recall_weighted:.2f}")

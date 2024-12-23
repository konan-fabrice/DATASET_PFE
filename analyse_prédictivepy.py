# -*- coding: utf-8 -*-
"""Analyse prédictive.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1h4i17vBrvBUViJifUlHbficO4ehWvdrI
"""



#Importation des bibliothèques
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
#Implémentation du modèle
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score, mean_absolute_error
from sklearn.preprocessing import LabelEncoder
#Normalissation
from sklearn.preprocessing import MinMaxScaler
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, confusion_matrix

#Chargement du dataset
df = pd.read_excel('/content/Ecriturecompte.xlsx')

df.head(5)

df_copie = df.copy()

df = df.iloc[2:]
# Réinitialiser l'index
df = df.reset_index(drop=True)
df.head()
#Renommer les colonnes
df=df.rename(columns={f'{df.columns.values[1]}': 'PRODUIT'})
df=df.rename(columns={f'{df.columns.values[2]}': 'PERIODE'})
df=df.rename(columns={f'{df.columns.values[4]}': 'QUANTITE'})
df['QUANTITE']=df['QUANTITE'].astype(float)
df.head(5)

#Sélection des colones
df=df[['PRODUIT','PERIODE','QUANTITE']]
df.head(5)

#Rendre les quantité positives
df['QUANTITE'] = np.abs(df['QUANTITE'])
df.head(5)

df.info()
print(df.isnull().sum())
df.describe()

df.head(5)

df['PERIODE']=pd.to_datetime(df['PERIODE'])
df['PERIODE']=df['PERIODE'].dt.month
df.head(5)

label_encoder = LabelEncoder()
df['PRODUIT_ENCODED'] = label_encoder.fit_transform(df['PRODUIT'])

df.head(5)

df = df[['PRODUIT_ENCODED','PERIODE','QUANTITE']]
df.head(5)

scaler = MinMaxScaler()
df_normalized = scaler.fit_transform(df)
df_normalized = pd.DataFrame(df_normalized, columns=df.columns)
df_normalized.head(5)

df_normalized.shape

a = scaler.inverse_transform(df_normalized)
a = pd.DataFrame(a, columns=df_normalized.columns)
a.head(5)

a.shape

#Séparation des données de train et test
X=df_normalized.drop('QUANTITE',axis=1)
y=df_normalized['QUANTITE']
x_train,x_test,y_train,y_test=train_test_split(X,y,test_size=0.2,random_state=42)

#print(x_train)
y_test



#Implémentation du modlèle
model=LinearRegression()
model.fit(x_train,y_train)
predictions=model.predict(x_test)

#Evaluation du modèle
mse=mean_squared_error(y_test,predictions)
mae=mean_absolute_error(y_test,predictions)
r2=r2_score(y_test,predictions)

print(f'mse:{mse}')
print(f'mae:{mae}')
print(f'r2:{r2}')

x_test.head(5)

#Resultat
resultats = pd.DataFrame({
    'PRODUIT_ENCODED': x_test['PRODUIT_ENCODED'],
    'PERIODE': x_test['PERIODE'],
    'QUANTITE': y_test,
    'predictions': predictions
})
resultats.head(5)

"""## Evaluation des performances du modèle"""

accuracy_score = accuracy_score(y_test, predictions, normalize=Fals)

precision_score = precision_score(y_test, predictions)
recall_score = recall_score(y_test, predictions)
f1_score = f1_score(y_test, predictions)
confusion_matrix = confusion_matrix(y_test, predictions)
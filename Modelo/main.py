from sklearn.pipeline import Pipeline
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
import pandas as pd
from libSub import preprocessar
from joblib import dump

df = pd.read_csv("master\Dados.csv")


frases = [preprocessar(f) for f in df['Frase']]
comandos = df['Comando']

modelo = Pipeline([
    ("vetorizador", TfidfVectorizer()),
    ("classificador", LogisticRegression())
])

modelo.fit(frases, comandos)


entrada_usuario = "HOJE TEM PREVISÃO DE CHUVA?"
entrada_usuario_processada = preprocessar(entrada_usuario)


resultado = modelo.predict([entrada_usuario_processada])[0]

print(resultado)

dump(modelo, 'modelo.joblib')
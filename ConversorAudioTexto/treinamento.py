import speech_recognition as sr
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics import classification_report
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import Pipeline, make_pipeline

recognizer = sr.Recognizer()
data = pd.read_csv('2019-05-28_portuguese_hate_speech_hierarchical_classification.csv')
X_train, X_test, y_train, y_test = train_test_split(data['text'], data['label'], test_size=0.2, random_state=42)

model = make_pipeline(TfidfVectorizer(), MultinomialNB())
model.fit(X_train, y_train)
y_pred = model.predict(X_test)
print(classification_report(y_test, y_pred))

def identificar_frases_pejorativas(text):
    prediction = model.predict(text)
    return "Conteúdo pejorativo detectado." if prediction == 1 else "Conteúdo adequado."

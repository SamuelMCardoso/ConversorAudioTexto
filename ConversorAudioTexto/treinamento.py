import speech_recognition as sr
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics import classification_report
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import Pipeline, make_pipeline

def main():

    recognizer = sr.Recognizer()
    data = pd.read_csv('2019-05-28_portuguese_hate_speech_hierarchical_classification.csv')
    X_train, X_test, y_train, y_test = train_test_split(data['text'], data['label'], test_size=0.2, random_state=42)

    model = make_pipeline(TfidfVectorizer(), MultinomialNB())
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)
    print(classification_report(y_test, y_pred))

    def filtrar_frases_pejorativas(text):
        prediction = model.predict([text])
        return "Conteúdo pejorativo detectado." if prediction == 1 else "Conteúdo adequado."

    audio_file = sr.AudioFile('audio_file.wav')
    with audio_file as source:
    audio = recognizer.record(source)

    try:



       text = recognizer.recognize_google(audio, language='pt-BR')
       print(f"Transcrição: {text}")
       resultado_filtrado = filtrar_frases_pejorativas(text)
       print("Resultado final: {resultado_filtrado}")
    except sr.UnknownValueError:
       print("Não foi possível entender o áudio.")
    except sr.RequestError:
       print("Erro ao se comunicar com o serviço de reconecimento da fala.")

if __name__ == '__main__':
  main()


from io import BytesIO

import requests
import speech_recognition as sr
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics import classification_report
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import Pipeline, make_pipeline


class AudioSegment:
    @classmethod
    def from_mp3(cls, audio_data):
        pass


def main():

    recognizer = sr.Recognizer()
    csv_path= r"C:\Users\samir\OneDrive\Documents\Python\2019-05-28_portuguese_hate_speech_hierarchical_classification.csv"
    data = pd.read_csv(csv_path)
    X_train, X_test, y_train, y_test = train_test_split(data['text'], data['label'], test_size=0.2, random_state=42)

    model = make_pipeline(TfidfVectorizer(), MultinomialNB())
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)
    print(classification_report(y_test, y_pred))

    def filtrar_frases_pejorativas(text):
        prediction = model.predict([text])
        return "Conteúdo pejorativo detectado." if prediction == 1 else "Conteúdo adequado."

    audio_url = 'https://www.orangefreesounds.com/wp-content/uploads/2021/02/Ambient-music-loop.mp3'
    response = requests.get(audio_url)
    audio_data = BytesIO(response.content)

    # Converte o áudio de MP3 para WAV usando pydub
    audio_segment = AudioSegment.from_mp3(audio_data)
    audio_wav = BytesIO()
    audio_segment.export(audio_wav, format="wav")
    audio_wav.seek(0)

    with sr.AudioFile(audio_wav) as source:
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


import speech_recognition as sr
import pandas as pd
import requests
from io import BytesIO
from pydub import AudioSegment
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics import classification_report
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import Pipeline, make_pipeline
import os


def main():
    recognizer = sr.Recognizer()
    # Use uma string bruta para o caminho do arquivo CSV
    csv_path = r'C:\Users\samir\OneDrive\Documents\Python\frases.csv'
    data = pd.read_csv(csv_path)

    # Imprime as colunas e as primeiras linhas do DataFrame
    print("Colunas do DataFrame:", data.columns)
    print("Primeiras linhas do DataFrame:\n", data.head())

    # Verifica se as colunas 'text' e 'label' existem
    if 'text' not in data.columns or 'label' not in data.columns:
        print("Erro: O DataFrame não contém as colunas 'text' e/ou 'label'")
        return

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
        print(f"Resultado final: {resultado_filtrado}")
    except sr.UnknownValueError:
        print("Não foi possível entender o áudio.")
    except sr.RequestError:
        print("Erro ao se comunicar com o serviço de reconhecimento da fala.")


if __name__ == '__main__':
    main()

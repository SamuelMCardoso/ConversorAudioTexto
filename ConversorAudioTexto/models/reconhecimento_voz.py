import speech_recognition as sr
from tkinter import messagebox

def reconhecer_audio():
    funcionar_mic = sr.Recognizer()
    with sr.Microphone() as source:
        funcionar_mic.adjust_for_ambient_noise(source)
        print("Encaminhe seu áudio:")
        try:
            audio = funcionar_mic.listen(source, timeout=5)  # Adicione um timeout para evitar espera indefinida
            frase = funcionar_mic.recognize_google(audio, language='pt-BR')
            print("Tradução: " + frase)
            messagebox.showinfo("Tradução", "Tradução: " + frase)
        except sr.WaitTimeoutError:
            messagebox.showerror("Erro", "Tempo de espera esgotado.")
        except sr.UnknownValueError:
            messagebox.showerror("Erro", "Não consegui reconhecer o conteúdo no áudio.")
        except sr.RequestError:
            messagebox.showerror("Erro", "Não foi possível conectar ao serviço de reconhecimento.")

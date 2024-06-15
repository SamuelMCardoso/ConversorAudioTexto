import tkinter as tk
from reconhecimento_voz import reconhecer_audio  # Importa a função de reconhecimento de áudio

# Função que será chamada quando o botão "Enviar áudio" for clicado
def on_send_audio_button_click():
    tk.messagebox.showinfo("Ação", "Botão 'Enviar áudio' clicado!")

# Configuração da janela principal
root = tk.Tk()
root.title("Interface com Botões")
root.geometry("300x200")

# Criar o botão "Falar"
speak_button = tk.Button(root, text="Falar", command=reconhecer_audio)
speak_button.pack(pady=10)

# Criar o botão "Enviar áudio"
send_audio_button = tk.Button(root, text="Enviar áudio", command=on_send_audio_button_click)
send_audio_button.pack(pady=10)

# Executar a aplicação
root.mainloop()

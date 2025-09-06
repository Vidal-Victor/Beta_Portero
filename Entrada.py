import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "lib"))
import pyttsx3
import speech_recognition as sr

def Portero_speak_entrada(placa):
    from BDcalls import Portero_entrada
    speaker = pyttsx3.init()
    recognizer = sr.Recognizer()
    tentativas = 0 

    while tentativas < 3:
        mensagem = "Olá. Por favor, informe a quilometragem do veículo."
        speaker.say(mensagem)
        speaker.runAndWait()

        with sr.Microphone() as source:
            print("Aguardando resposta...")
            recognizer.adjust_for_ambient_noise(source)
            try:
                audio = recognizer.listen(source, timeout=5)
                frase = recognizer.recognize_google(audio, language='pt-BR')
                print(f"Resposta recebida: {frase}")

                try:
                    km = int(frase)
                    print(f"Quilometragem informada: {km}")
                    
                    if Portero_entrada(placa, km):  
                        speaker.say("Quilometragem registrada com sucesso.")
                        speaker.runAndWait()
                        print("Registro bem-sucedido.")
                        return
                    else:
                        speaker.say("Erro ao registrar a quilometragem no sistema.")
                        speaker.runAndWait()
                        print("Erro ao registrar a quilometragem.")
                
                except ValueError:
                    print("Erro: Resposta não é um número válido.")
                    speaker.say("A quilometragem informada não é um número válido.")
                    speaker.runAndWait()
            
            except sr.UnknownValueError:
                print("Não foi possível compreender a resposta.")
                speaker.say("Desculpe, não entendi a resposta.")
                speaker.runAndWait()
            except sr.WaitTimeoutError:
                print("Tempo de espera excedido.")
                speaker.say("Tempo de espera excedido.")
                speaker.runAndWait()

        tentativas += 1
        print(f"Tentativa {tentativas} de 3.")
        if tentativas < 3:
            mensagem = "Por favor, tente novamente."
            speaker.say(mensagem)
            speaker.runAndWait()

    speaker.say("Número máximo de tentativas atingido. Encerrando.")
    speaker.runAndWait()
    print("Número máximo de tentativas atingido. Função encerrada.")

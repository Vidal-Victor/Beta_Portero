import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "lib"))
import pyttsx3
import speech_recognition as sr

def Portero_speak_saida(placa):
    from BDcalls import Portero_saida
    speaker = pyttsx3.init()
    recognizer = sr.Recognizer()
    tentativas = 0

    while tentativas < 3:
        speaker.say("Olá. Informe o código do motorista.")
        speaker.runAndWait()

        with sr.Microphone() as source:
            print("Aguardando resposta do código...")
            recognizer.adjust_for_ambient_noise(source)
            try:
                audio = recognizer.listen(source, timeout=5)
                frase = recognizer.recognize_google(audio, language='pt-BR')
                print(f"Resposta recebida: {frase}")

                try:
                    mot = int(frase)
                    print(f"Motorista informado: {mot}")
                    speaker.say("Informe o destino do veículo.")
                    speaker.runAndWait()

                    print("Aguardando resposta do destino...")
                    audio2 = recognizer.listen(source, timeout=5)
                    frase2 = recognizer.recognize_google(audio2, language='pt-BR')
                    mot2 = frase2
                    print(f"Destino informado: {frase2}")

                    if Portero_saida(placa, mot, mot2):
                        speaker.say("Saída registrada com sucesso.")
                        speaker.runAndWait()
                        print("Resposta processada com sucesso.")
                        return
                    else:
                        print("Houve um problema ao processar a saída.")
                        speaker.say("Erro ao registrar saída.")
                        speaker.runAndWait()

                except ValueError:
                    print("Erro: Resposta não é um número válido.")
                    speaker.say("Código inválido. Tente novamente.")
                    speaker.runAndWait()

            except sr.UnknownValueError:
                print("Não foi possível compreender a resposta.")
                speaker.say("Desculpe, não entendi.")
                speaker.runAndWait()
            except sr.WaitTimeoutError:
                print("Tempo de espera excedido.")
                speaker.say("Tempo excedido.")
                speaker.runAndWait()

        tentativas += 1
        print(f"Tentativa {tentativas} de 3.")
        if tentativas < 3:
            speaker.say("Por favor, tente novamente.")
            speaker.runAndWait()

    speaker.say("Número máximo de tentativas atingido. Encerrando.")
    speaker.runAndWait()
    print("Número máximo de tentativas atingido. Função encerrada.")

    
def Saida_erro():
    speaker = pyttsx3.init()
    speaker.say("O veículo já apresenta uma saída registrada. Para registar uma nova saída, é necessário registrar a sua entrada.")
    speaker.runAndWait()
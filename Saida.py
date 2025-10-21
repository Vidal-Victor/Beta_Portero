import sys
import os
import pyttsx3
import speech_recognition as sr
import time

# ...existing code...
# mover inicialização para o módulo (reusar)
_engine = pyttsx3.init()
_recognizer = sr.Recognizer()
# ...existing code...

def Portero_speak_saida(placa):
    from BDcalls import Portero_saida
    tentativas = 0

    while tentativas < 3:
        try:
            _engine.say("Olá. Informe o código do motorista.")
            _engine.runAndWait()
        except Exception as e:
            print("TTS error:", e)

        # pequena espera para garantir que o dispositivo de áudio termine
        time.sleep(0.2)

        with sr.Microphone() as source:
            print("Aguardando resposta do código...")
            _recognizer.adjust_for_ambient_noise(source)
            try:
                audio = _recognizer.listen(source, timeout=5)
                frase = _recognizer.recognize_google(audio, language='pt-BR')
                print(f"Resposta recebida: {frase}")

                try:
                    mot = int(frase)
                    print(f"Motorista informado: {mot}")

                    try:
                        _engine.say("Informe o destino do veículo.")
                        _engine.runAndWait()
                    except Exception as e:
                        print("TTS error:", e)
                    time.sleep(0.2)

                    print("Aguardando resposta do destino...")
                    audio2 = _recognizer.listen(source, timeout=5)
                    frase2 = _recognizer.recognize_google(audio2, language='pt-BR')
                    mot2 = frase2
                    print(f"Destino informado: {frase2}")

                    if Portero_saida(placa, mot, mot2):
                        try:
                            _engine.say("Saída registrada com sucesso.")
                            _engine.runAndWait()
                        except Exception as e:
                            print("TTS error:", e)
                        print("Resposta processada com sucesso.")
                        return
                    else:
                        print("Houve um problema ao processar a saída.")
                        try:
                            _engine.say("Erro ao registrar saída.")
                            _engine.runAndWait()
                        except Exception as e:
                            print("TTS error:", e)

                except ValueError:
                    print("Erro: Resposta não é um número válido.")
                    try:
                        _engine.say("Código inválido. Tente novamente.")
                        _engine.runAndWait()
                    except Exception as e:
                        print("TTS error:", e)

            except sr.UnknownValueError:
                print("Não foi possível compreender a resposta.")
                try:
                    _engine.say("Desculpe, não entendi.")
                    _engine.runAndWait()
                except Exception as e:
                    print("TTS error:", e)
            except sr.WaitTimeoutError:
                print("Tempo de espera excedido.")
                try:
                    _engine.say("Tempo excedido.")
                    _engine.runAndWait()
                except Exception as e:
                    print("TTS error:", e)

        tentativas += 1
        print(f"Tentativa {tentativas} de 3.")
        if tentativas < 3:
            try:
                _engine.say("Por favor, tente novamente.")
                _engine.runAndWait()
            except Exception as e:
                print("TTS error:", e)

    try:
        _engine.say("Número máximo de tentativas atingido. Encerrando.")
        _engine.runAndWait()
    except Exception as e:
        print("TTS error:", e)
    print("Número máximo de tentativas atingido. Função encerrada.")

    
def Saida_erro():
    try:
        _engine.say("O veículo já apresenta uma saída registrada. Para registar uma nova saída, é necessário registrar a sua entrada.")
        _engine.runAndWait()
    except Exception as e:
        print("TTS error:", e)
# ...existing code...
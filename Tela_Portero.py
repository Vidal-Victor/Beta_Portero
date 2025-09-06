import sys
import os
from Cam_Portero import Portero_cam
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "lib"))
import cv2 
import ttkbootstrap as tb
import json
from ttkbootstrap.constants import *
from ttkbootstrap.style import Style
from pygrabber.dshow_graph import FilterGraph

script_dir = os.path.dirname(os.path.abspath(__file__))
Dados = os.path.join(script_dir, "disp.json")
with open(Dados, "r") as f:
    dados = json.load(f)

def portero():
    app = tb.Window(themename="solar")
    app.title("Portero")
    app.geometry("800x600")
    
    label = tb.Label(app, text="Reconhecimento de Placas", font=("Helvetica", 20))
    label.pack(pady=10)
    
    def iniciar_entrada():
        janelaE()

    def iniciar_saida():
        janelaS()

    pergunta_label = tb.Label(app, text="Deseja registrar entrada ou saída?", font=("Arial", 14))
    pergunta_label.pack(pady=20)

    botao_entrada = tb.Button(app, text="Entrada", command=iniciar_entrada, bootstyle="info", width=15)
    botao_entrada.pack(pady=10)

    botao_saida = tb.Button(app, text="Saída", command=iniciar_saida, bootstyle="danger", width=15)
    botao_saida.pack(pady=10)

    info_label = tb.Label(app, text="Escolher câmera padrão", font=("Arial", 14))
    info_label.pack(pady=10)
    
    botao_s = tb.Button(app, text="Câmeras", command=janela2, bootstyle="danger, outline", width=15)
    botao_s.pack(pady=10)

    botao_r = tb.Button(app, text="Redimensionar", command=janelaR, bootstyle="info, outline", width=15)
    botao_r.pack(pady=10)

    app.mainloop()

def janela2():
    graph = FilterGraph()
    devices = graph.get_input_devices()

    def selecionar():
        escolhaE = lista.get()
        escolhaS = listaS.get()
        if escolhaE:
            indiceE = devices.index(escolhaE)
            dados["cam"]["dispositivoE"] = indiceE
        if escolhaS:
            indiceS = devices.index(escolhaS)
            dados["cam"]["dispositivoS"] = indiceS
        with open(Dados, "w") as f:
            json.dump(dados, f, indent=4)

    janela = tb.Toplevel()
    janela.title("Portero - Câmera")
    janela.geometry("400x300")
    lE = tb.Label(janela, text="Selecione a câmera para entrada", font=("Arial", 14))
    lE.pack(pady=10)
    lista = tb.Combobox(janela, values=devices, state="readonly")
    lista.pack(pady=10)
    idxE = dados["cam"].get("dispositivoE", 0)
    if 0 <= idxE < len(devices):
        lista.current(idxE)

    lS = tb.Label(janela, text="Selecione a câmera para saída", font=("Arial", 14))
    lS.pack(pady=10)
    listaS = tb.Combobox(janela, values=devices, state="readonly")
    listaS.pack(pady=10)
    idxS = dados["cam"].get("dispositivoS", 0)
    if 0 <= idxS < len(devices):
        listaS.current(idxS)

    botao_selecionar = tb.Button(janela, text="Selecionar", command=selecionar, bootstyle="info")
    botao_selecionar.pack(pady=10)
    botao_fechar = tb.Button(janela, text="Fechar", command=janela.destroy, bootstyle="danger")
    botao_fechar.pack(pady=10)

def janelaS():
    janela = tb.Toplevel()
    janela.title("Portero - Saída")
    janela.geometry("700x500")
    camera_frame = tb.Label(janela, relief="sunken", anchor="center", text="Vídeo")
    camera_frame.pack(fill="both", expand=True)
    video = cv2.VideoCapture(dados["cam"]["dispositivoS"])
    if not video.isOpened():
        print("Erro ao abrir a câmera")
        return
    Portero_cam(camera_frame, video, dados["cam"]["placa_coords"], 2)

def janelaE():
    janela = tb.Toplevel()
    janela.title("Portero - Entrada")
    janela.geometry("700x500")
    camera_frame = tb.Label(janela, relief="sunken", anchor="center", text="Vídeo")
    camera_frame.pack(fill="both", expand=True)
    video = cv2.VideoCapture(dados["cam"]["dispositivoE"])
    if not video.isOpened():
        print("Erro ao abrir a câmera")
        return
    Portero_cam(camera_frame, video, dados["cam"]["placa_coords"], 1)

def janelaR():
    dimensao = None

    def selecionar_area():
        nonlocal dimensao
        cap = cv2.VideoCapture(0)
        ret, frame = cap.read()
        cap.release()

        if ret:
            cv2.putText(frame, "Selecione a area e pressione ENTER ou aperte C para cancelar",
                        (20, 40), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 255, 255), 2, cv2.LINE_AA)

            dimensao = cv2.selectROI("Redimensionar", frame, False, False)
            cv2.destroyAllWindows()
            if any(dimensao):
                label_status.config(text=f"Área selecionada: {dimensao}")
            else:
                label_status.config(text="Nenhuma área selecionada")

    def salvarD():
        if dimensao and any(dimensao):
            x, y, w, h = dimensao
            dados["cam"]["placa_coords"] = [int(x), int(y), int(w), int(h)]
            with open(Dados, "w") as f:
                json.dump(dados, f, indent=4)
            janela.destroy()
        else:
            tb.Messagebox.show_error("Selecione uma área antes de salvar.", title="Erro")

    janela = tb.Toplevel()
    janela.title("Portero - Redimensionar Placa")
    janela.geometry("700x500")

    label_instrucao = tb.Label(janela, text="Selecione a área da placa e pressione ENTER ou ESPAÇO", font=("Arial", 12))
    label_instrucao.pack(pady=10)

    botao_area = tb.Button(janela, text="Selecionar Área", command=selecionar_area, bootstyle="info")
    botao_area.pack(pady=10)

    label_status = tb.Label(janela, text="Nenhuma área selecionada", font=("Arial", 12))
    label_status.pack(pady=10)

    botao_salvar = tb.Button(janela, text="Salvar", command=salvarD, bootstyle="success")
    botao_salvar.pack(pady=10)

    botao_cancelar = tb.Button(janela, text="Cancelar", command=janela.destroy, bootstyle="danger")
    botao_cancelar.pack(pady=10)


if __name__ == "__main__":
    portero()

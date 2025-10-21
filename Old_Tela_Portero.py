import cv2 
import ttkbootstrap as tb
import json
import os
from Cam_Portero import Portero_cam
from ttkbootstrap.constants import *
from ttkbootstrap.style import Style
script_dir = os.path.dirname(os.path.abspath(__file__))
Dados = os.path.join(script_dir, "disp.json")
with open(Dados, "r") as f:
    dados = json.load(f)

def portero():
    app = tb.Window(themename="solar")
    app.title("Portero")
    app.geometry("800x600")
    
    label = tb.Label(app, text="Reconhecimento de Placas", font=("Helvetica", 16))
    label.pack(pady=10)

    # Frame com tamanho fixo
    frame_container = tb.Frame(app, width=320, height=240, bootstyle="secondary")
    frame_container.pack_propagate(False)
    frame_container.pack(pady=0)

    # Label do vídeo dentro do frame
    camera_frame = tb.Label(frame_container, relief="sunken", anchor="center", text="Vídeo")
    camera_frame.pack(fill="both", expand=True)

    def iniciar_entrada():
        video = cv2.VideoCapture(0)
        if not video.isOpened():
            print("Erro ao abrir a câmera")
            return
        Portero_cam(camera_frame, video, dados["cam"]["placa_coords"], 1)

    def iniciar_saida():
        video = cv2.VideoCapture(0)
        if not video.isOpened():
            print("Erro ao abrir a câmera")
            return
        Portero_cam(camera_frame, video, dados["cam"]["placa_coords"], 2)

    pergunta_label = tb.Label(app, text="Deseja registrar entrada ou saída?", font=("Arial", 14))
    pergunta_label.pack(pady=20)

    botao_entrada = tb.Button(app, text="Entrada", command=iniciar_entrada, bootstyle="success", width=15)
    botao_entrada.pack(pady=10)

    botao_saida = tb.Button(app, text="Saída", command=iniciar_saida, bootstyle="danger", width=15)
    botao_saida.pack(pady=10)

    app.mainloop()



if __name__ == "__main__":
    portero()

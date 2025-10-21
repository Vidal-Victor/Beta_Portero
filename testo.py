import ttkbootstrap as tb
import json
import os
from ttkbootstrap.constants import *
from pygrabber.dshow_graph import FilterGraph

# Caminho do arquivo de configuração
script_dir = os.path.dirname(os.path.abspath(__file__))
Dados = os.path.join(script_dir, "disp.json")
with open(Dados, "r") as f:
    dados = json.load(f)

# Dispositivos de captura
graph = FilterGraph()
devices = graph.get_input_devices()

def selecionar():
    escolha = lista.get()
    if escolha:
        indice = devices.index(escolha)
        print(f"Você selecionou: {escolha} (índice {indice})")

# Criar janela principal
janela = tb.Window(themename="solar")
janela.title("Selecione a Câmera")

# Criar Canvas + Scrollbar
canvas = tb.Canvas(janela)
scrollbar = tb.Scrollbar(janela, orient="vertical", command=canvas.yview)
scrollbar.pack(side="right", fill="y")
canvas.pack(side="left", fill="both", expand=True)

# Configuração do frame rolável
frame_principal = tb.Frame(canvas)
canvas.create_window((0, 0), window=frame_principal, anchor="nw")
canvas.configure(yscrollcommand=scrollbar.set)

# Função para atualizar tamanho do canvas
def atualizar_scroll(event):
    canvas.configure(scrollregion=canvas.bbox("all"))

frame_principal.bind("<Configure>", atualizar_scroll)

# --- CONTEÚDO ---
lista = tb.Combobox(frame_principal, values=devices, state="readonly")
lista.pack(pady=10)
lista.current(dados["cam"]["dispositivo"])

botao = tb.Button(frame_principal, text="Selecionar", command=selecionar, style="TFrame")
botao.pack(pady=10)

# (Exemplo para forçar muito conteúdo e testar scroll)
for i in range(30):
    tb.Label(frame_principal, text=f"Item extra {i+1}").pack()

janela.mainloop()

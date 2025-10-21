import sys
import os
import cv2 
import numpy as np
import pytesseract
from PIL import Image, ImageTk
from BDcalls import Portero_verif

def Portero_cam(frame_widget, video, placa_coords, e_s):
    ret, frame = video.read()
    if not ret:
        print("Erro ao capturar o frame da câmera.")
        return

    x, y, w, h = placa_coords
    imgCinza = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    imgTh = cv2.adaptiveThreshold(imgCinza, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY_INV, 25, 16)
    imgBlur = cv2.medianBlur(imgTh, 5)
    kernel = np.ones((3, 3), np.uint8)
    imgDil = cv2.dilate(imgBlur, kernel)

    recorte = imgDil[y:y + h, x:x + w]
    cut = frame[y:y + h, x:x + w]
    qtpxbranco = cv2.countNonZero(recorte)

    if qtpxbranco > 6500:
        resize_img_roi = cv2.resize(cut, None, fx=4, fy=4, interpolation=cv2.INTER_CUBIC)
        Portero_read(resize_img_roi, e_s)

    cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

    # Conversão de BGR (OpenCV) para RGB (PIL)
    img_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    img_pil = Image.fromarray(img_rgb)
    img_tk = ImageTk.PhotoImage(image=img_pil)

    # Atualiza o widget do Tkinter
    frame_widget.imgtk = img_tk
    frame_widget.configure(image=img_tk)

    # Chama essa função novamente após 30ms
    frame_widget.after(30, Portero_cam, frame_widget, video, placa_coords, e_s)

def Portero_read(placa, e_s):
    cinza = cv2.cvtColor(placa, cv2.COLOR_BGR2GRAY)
    _, bin = cv2.threshold(cinza, 90, 255, cv2.THRESH_BINARY)
    desfoque = cv2.GaussianBlur(bin, (5, 5), 0)
    config = r'-c tessedit_char_whitelist=ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789 --psm 6'
    if e_s == 1:
        cv2.imwrite('Entrada.jpg', desfoque)
    if e_s == 2:
        cv2.imwrite('Saida.jpg', desfoque)
    text = pytesseract.image_to_string(desfoque, config=config)
    text = ''.join(filter(str.isalnum, text)).upper()
    print(f"Texto OCR reconhecido: {text}")
    
    Portero_verif(text, e_s)
    return 
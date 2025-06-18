import tkinter as tk
from tkinter import ttk, filedialog, messagebox

import cv2
from PIL import Image, ImageTk
import os
from core.detectors.placa_detector import PlacaDetector
from core.detectors.rosto_detector import RostoDetector
from core.utils.image_utils import desenhar_retangulos, borrar_nao_selecionados, carregar_imagem

class PrivisioApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Privisio")
        self.root.geometry("1000x600")
        self.root.resizable(False, False)

        # Inicializa variáveis
        self.imagem_path = None
        self.imagem_original = None
        self.imagem_exibida = None
        self.detections = []
        self.checkbox_vars = []

        # Inicializa detectores
        self.placa_detector = PlacaDetector()
        self.rosto_detector = RostoDetector()

        # Frame principal
        self.main_frame = ttk.Frame(self.root)
        self.main_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

        # Frame de imagem
        self.img_frame = ttk.Frame(self.main_frame)
        self.img_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        self.img_label = ttk.Label(self.img_frame)
        self.img_label.pack()

        # Frame lateral para checkboxes
        self.sidebar_frame = ttk.Frame(self.main_frame, width=300)
        self.sidebar_frame.pack(side=tk.RIGHT, fill=tk.Y, padx=(10, 0))

        self.checkbox_container = ttk.LabelFrame(self.sidebar_frame, text="Selecione os objetos que serão visíveis:")
        self.checkbox_container.pack(fill=tk.BOTH, expand=True, pady=5)

        # Botões de controle
        self.btn_frame = ttk.Frame(self.root)
        self.btn_frame.pack(fill=tk.X, pady=10)

        self.btn_carregar = ttk.Button(self.btn_frame, text="Carregar Imagem", command=self.carregar_imagem)
        self.btn_carregar.pack(side=tk.LEFT, padx=5)

        self.btn_analisar = ttk.Button(self.btn_frame, text="Analisar", command=self.analisar)
        self.btn_analisar.pack(side=tk.LEFT, padx=5)
        self.btn_analisar['state'] = tk.DISABLED

        self.btn_resultado = ttk.Button(self.btn_frame, text="Gerar Resultado", command=self.gerar_resultado)
        self.btn_resultado.pack(side=tk.LEFT, padx=5)
        self.btn_resultado['state'] = tk.DISABLED

        self.btn_refazer = ttk.Button(self.btn_frame, text="Refazer", command=self.refazer)
        self.btn_refazer.pack(side=tk.RIGHT, padx=5)

        self.btn_sair = ttk.Button(self.btn_frame, text="Sair", command=self.root.quit)
        self.btn_sair.pack(side=tk.RIGHT, padx=5)

    def carregar_imagem(self):
        caminho = filedialog.askopenfilename(filetypes=[('Imagens', '*.jpg *.png *.jpeg')], initialdir=r"imagens\inputs")
        if not caminho:
            return

        imagem = carregar_imagem(caminho)
        if imagem is None:
            messagebox.showerror("Erro", "Não foi possível carregar a imagem.")
            return

        self.imagem_path = caminho
        self.imagem_original = imagem
        self.mostrar_imagem(imagem)
        self.btn_analisar['state'] = tk.NORMAL
        self.limpar_checkboxes()

    def mostrar_imagem(self, img_bgr):
        img_rgb = cv2.cvtColor(img_bgr, cv2.COLOR_BGR2RGB)
        img_pil = Image.fromarray(img_rgb)
        img_pil.thumbnail((640, 480))
        self.imagem_exibida = ImageTk.PhotoImage(img_pil)
        self.img_label.config(image=self.imagem_exibida)

    def analisar(self):
        if self.imagem_original is None:
            return

        img = self.imagem_original.copy()
        self.detections = []

        try:
            self.detections += self.placa_detector.detectar(img)
            self.detections += self.rosto_detector.detectar(img)
        except Exception as e:
            messagebox.showerror("Erro na detecção", str(e))
            return

        img_com_caixas = desenhar_retangulos(img.copy(), self.detections)
        self.mostrar_imagem(img_com_caixas)
        self.btn_resultado['state'] = tk.NORMAL

        self.limpar_checkboxes()
        for i, (tipo, x1, y1, x2, y2) in enumerate(self.detections):
            var = tk.IntVar(value=0)
            chk = ttk.Checkbutton(self.checkbox_container, text=f"{i}: {tipo}", variable=var)
            chk.pack(anchor=tk.W)
            self.checkbox_vars.append(var)

    def gerar_resultado(self):
        selecionados = [i for i, var in enumerate(self.checkbox_vars) if var.get() == 1]
        borrada = borrar_nao_selecionados(self.imagem_original.copy(), self.detections, selecionados)

        self.mostrar_imagem(borrada)

        caminho = filedialog.asksaveasfilename(defaultextension=".jpg", filetypes=[("JPEG", "*.jpg")], initialdir=r"imagens\outputs")
        if caminho:
            cv2.imwrite(caminho, borrada)
            messagebox.showinfo("Sucesso", f"Imagem salva em: {caminho}")

    def limpar_checkboxes(self):
        for widget in self.checkbox_container.winfo_children():
            widget.destroy()
        self.checkbox_vars = []

    def refazer(self):
        self.imagem_path = None
        self.imagem_original = None
        self.detections = []
        self.checkbox_vars = []
        self.img_label.config(image='')
        self.btn_analisar['state'] = tk.DISABLED
        self.btn_resultado['state'] = tk.DISABLED
        self.limpar_checkboxes()

def iniciar_ui():
    root = tk.Tk()
    app = PrivisioApp(root)
    root.mainloop()

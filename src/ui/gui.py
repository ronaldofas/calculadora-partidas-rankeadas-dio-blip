import tkinter as tk
from tkinter import messagebox
from tkinter import font as tkfont
from PIL import Image
import os


class RankedGUI:
    """
    Responsável pela interface gráfica do usuário.
    """

    def __init__(self, calculator):
        self.calculator = calculator
        self.root = tk.Tk()
        self.setup_ui()

    def setup_ui(self):
        self.root.title("Calculadora de partida rankeada")
        self.root.geometry("500x700")
        self.root.configure(bg="#f0f0f0")

        # Fonts
        self.title_font = tkfont.Font(
            family="Old English Text MT", size=24, weight="bold")
        if "Old English Text MT" not in tkfont.families():
            self.title_font = tkfont.Font(
                family="Times New Roman", size=24, weight="bold")
        self.label_font = tkfont.Font(family="Times New Roman", size=12)

        # Header
        tk.Label(self.root, text="Calculadora de partida rankeada",
                 font=self.title_font, bg="#f0f0f0", fg="#333").pack(pady=20)

        # Image
        self.load_image()

        # Input Form
        form_frame = tk.Frame(self.root, bg="#f0f0f0")
        form_frame.pack(pady=20)

        tk.Label(form_frame, text="Vitórias:", font=self.label_font,
                 bg="#f0f0f0").grid(row=0, column=0, padx=5, pady=5)
        self.entry_vitorias = tk.Entry(form_frame, font=self.label_font)
        self.entry_vitorias.grid(row=0, column=1, padx=5, pady=5)

        tk.Label(form_frame, text="Derrotas:", font=self.label_font,
                 bg="#f0f0f0").grid(row=1, column=0, padx=5, pady=5)
        self.entry_derrotas = tk.Entry(form_frame, font=self.label_font)
        self.entry_derrotas.grid(row=1, column=1, padx=5, pady=5)

        # Result Frame (Bordered)
        result_frame = tk.LabelFrame(
            self.root, text="Resultado", font=self.label_font, bg="#f0f0f0", fg="#333", padx=10, pady=10)
        result_frame.pack(pady=20, padx=20, fill="x")

        self.result_var = tk.StringVar()
        tk.Label(result_frame, textvariable=self.result_var,
                 font=self.title_font, bg="#f0f0f0", fg="#555", wraplength=450).pack()

        # Buttons
        btn_frame = tk.Frame(self.root, bg="#f0f0f0")
        btn_frame.pack(pady=10)

        tk.Button(btn_frame, text="Calcular", command=self.calcular,
                  font=self.label_font, bg="#d4d4d4").pack(side=tk.LEFT, padx=10)
        tk.Button(btn_frame, text="Limpar", command=self.limpar,
                  font=self.label_font, bg="#d4d4d4").pack(side=tk.LEFT, padx=10)

    def load_image(self):
        try:
            # Correct path relative to src/ui/gui.py -> ../../assets/medieval_shield.png
            script_dir = os.path.dirname(os.path.abspath(__file__))
            # Go up two levels (ui -> src -> root) then into assets
            image_path = os.path.join(
                script_dir, "..", "..", "assets", "medieval_shield.png")
            # Resolve to absolute path to be safe
            image_path = os.path.abspath(image_path)

            print(f"Tentando carregar imagem de: {image_path}")

            if os.path.exists(image_path):
                pil_image = Image.open(image_path)

                # Resize
                base_width = 300
                w_percent = (base_width / float(pil_image.size[0]))
                h_size = int((float(pil_image.size[1]) * float(w_percent)))
                pil_image = pil_image.resize(
                    (base_width, h_size), Image.Resampling.LANCZOS)

                # Save as temp GIF
                # Save temp file in the same directory as image to avoid cluttering source
                self.temp_gif = os.path.join(
                    os.path.dirname(image_path), "temp_shield.gif")
                pil_image.save(self.temp_gif, "GIF")

                self.image = tk.PhotoImage(file=self.temp_gif)

                image_label = tk.Label(
                    self.root, image=self.image, bg="#f0f0f0")
                image_label.pack(pady=10)
                print("Imagem carregada com sucesso (GIF convertido).")
            else:
                print("Arquivo de imagem não encontrado.")
                tk.Label(self.root, text="(Imagem não encontrada)",
                         bg="#f0f0f0").pack()
        except Exception as e:
            print(f"Erro ao carregar imagem: {e}")
            tk.Label(
                self.root, text=f"(Erro ao carregar imagem: {e})", bg="#f0f0f0").pack()

    def calcular(self):
        try:
            v_str = self.entry_vitorias.get()
            d_str = self.entry_derrotas.get()

            if not v_str or not d_str:
                messagebox.showwarning(
                    "Aviso", "Por favor, preencha ambos os campos.")
                return

            v = int(v_str)
            d = int(d_str)
            saldo, nivel = self.calculator.calculate_level(v, d)
            self.result_var.set(
                f"O Herói tem de saldo de {saldo} está no nível de {nivel}")
        except ValueError:
            messagebox.showerror("Erro", "Por favor, insira números válidos.")

    def limpar(self):
        self.entry_vitorias.delete(0, tk.END)
        self.entry_derrotas.delete(0, tk.END)
        self.result_var.set("")

    def run(self):
        self.root.mainloop()

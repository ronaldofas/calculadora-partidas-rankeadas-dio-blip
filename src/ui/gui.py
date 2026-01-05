import tkinter as tk
from tkinter import messagebox
from tkinter import font as tkfont
from PIL import Image
import os
import platform


class RankedGUI:
    """
    Responsável pela interface gráfica do usuário.
    """

    def __init__(self, calculator):
        self.calculator = calculator
        self.root = tk.Tk()
        self.setup_ui()

    def get_font_family(self):
        """
        Determina a fonte baseada no sistema operacional.
        """
        os_name = platform.system()
        family = "Times New Roman"  # Default fallback

        if os_name == "Windows":
            preferred = "Lucida Blackletter"
        elif os_name == "Darwin":
            preferred = "Apple Chancery"
        else:  # Linux and others
            preferred = "FreeSerif"

        # Check if preferred is available
        available_fonts = tkfont.families()
        if preferred in available_fonts:
            return preferred

        # Fallback loop
        fallbacks = ["Times New Roman", "DejaVu Serif",
                     "Liberation Serif", "Serif"]
        for f in fallbacks:
            if f in available_fonts:
                return f

        return family  # Final fallback

    def setup_ui(self):
        self.root.title("Calculadora de partida rankeada")
        self.root.geometry("500x700")
        self.root.configure(bg="#f0f0f0")

        # Fonts
        font_family = self.get_font_family()
        self.title_font = tkfont.Font(
            family=font_family, size=24, weight="bold")
        self.label_font = tkfont.Font(family="Times New Roman", size=12)

        # Header
        self.header_label = tk.Label(
            self.root, text="Calculadora de partida rankeada", font=self.title_font, bg="#f0f0f0", fg="#333")
        self.header_label.pack(pady=20)

        # Bind resize event to handle dynamic title wrapping
        self.root.bind("<Configure>", self.on_window_resize)

        # Image
        self.load_image()

        # Input Form
        form_frame = tk.Frame(self.root, bg="#f0f0f0")
        form_frame.pack(pady=10)

        tk.Label(form_frame, text="Vitórias:", font=self.label_font,
                 bg="#f0f0f0").grid(row=0, column=0, padx=5, pady=5)
        self.entry_vitorias = tk.Entry(form_frame, font=self.label_font)
        self.entry_vitorias.grid(row=0, column=1, padx=5, pady=5)

        tk.Label(form_frame, text="Derrotas:", font=self.label_font,
                 bg="#f0f0f0").grid(row=1, column=0, padx=5, pady=5)
        self.entry_derrotas = tk.Entry(form_frame, font=self.label_font)
        self.entry_derrotas.grid(row=1, column=1, padx=5, pady=5)

        # Buttons - Moved to bottom pack to ensure stability
        btn_frame = tk.Frame(self.root, bg="#f0f0f0")
        btn_frame.pack(side=tk.BOTTOM, pady=30)

        tk.Button(btn_frame, text="Calcular", command=self.calcular,
                  font=self.label_font, bg="#d4d4d4", width=10).pack(side=tk.LEFT, padx=10)
        tk.Button(btn_frame, text="Limpar", command=self.limpar,
                  font=self.label_font, bg="#d4d4d4", width=10).pack(side=tk.LEFT, padx=10)

        # Result Frame (Bordered) - Packed after inputs, fills remaining space but doesn't push buttons off
        result_frame = tk.LabelFrame(
            self.root, text="Resultado", font=self.label_font, bg="#f0f0f0", fg="#333", padx=10, pady=10)
        result_frame.pack(pady=10, padx=20, fill="x")

        self.result_var = tk.StringVar()
        self.result_label = tk.Label(result_frame, textvariable=self.result_var,
                                     font=self.title_font, bg="#f0f0f0", fg="#555", wraplength=450)
        self.result_label.pack()

    def on_window_resize(self, event):
        """
        Adjusts title and result wrapping based on window width.
        """
        # Ensure we are handling the root window resize (event.widget is the widget that triggered event)
        if event.widget == self.root:
            new_width = event.width
            # Subtract some padding (e.g., 40px for title, 60px for result to account for frame)
            if hasattr(self, 'header_label'):
                self.header_label.config(wraplength=new_width - 40)
            if hasattr(self, 'result_label'):
                self.result_label.config(wraplength=new_width - 60)

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

                # Resize (Reduced by 30% from 300 -> ~210)
                base_width = 210
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

import argparse
import tkinter as tk
from tkinter import messagebox
from tkinter import font as tkfont
from PIL import Image
import os


def calcular_nivel(vitorias, derrotas):
    """
    Calcula o saldo de vitórias e determina o nível do jogador.
    """
    saldo_vitorias = vitorias - derrotas

    if saldo_vitorias < 10:
        nivel = "Ferro"
    elif 11 <= saldo_vitorias <= 20:
        nivel = "Bronze"
    elif 21 <= saldo_vitorias <= 50:
        nivel = "Prata"
    elif 51 <= saldo_vitorias <= 80:
        nivel = "Ouro"
    elif 81 <= saldo_vitorias <= 90:
        nivel = "Diamante"
    elif 91 <= saldo_vitorias <= 100:
        nivel = "Lendário"
    else:  # saldo_vitorias >= 101
        nivel = "Imortal"

    return saldo_vitorias, nivel


def run_cli():
    print("--- Calculadora de Partidas Rankeadas (CLI) ---")
    try:
        vitorias = int(input("Digite a quantidade de vitórias: "))
        derrotas = int(input("Digite a quantidade de derrotas: "))

        saldo, nivel = calcular_nivel(vitorias, derrotas)

        print(
            f"O Herói tem de saldo de **{saldo}** está no nível de **{nivel}**")
    except ValueError:
        print("Erro: Por favor, insira apenas números inteiros para vitórias e derrotas.")


def run_gui():
    root = tk.Tk()
    root.title("Calculadora de partida rankeada")
    root.geometry("500x700")
    root.configure(bg="#f0f0f0")

    # Fonts
    # Attempt to use "Old English Text MT" or fallback to Times bold
    title_font = tkfont.Font(
        family="Old English Text MT", size=24, weight="bold")
    if "Old English Text MT" not in tkfont.families():
        title_font = tkfont.Font(
            family="Times New Roman", size=24, weight="bold")

    label_font = tkfont.Font(family="Times New Roman", size=12)

    # Header Title
    header_label = tk.Label(root, text="Calculadora de partida rankeada",
                            font=title_font, bg="#f0f0f0", fg="#333")
    header_label.pack(pady=20)

    # Image
    try:
        # Load the image relative to the script
        script_dir = os.path.dirname(os.path.abspath(__file__))
        image_path = os.path.join(script_dir, "medieval_shield.png")
        print(f"Tentando carregar imagem de: {image_path}")  # Debug print

        if os.path.exists(image_path):
            # Using PIL to resize and convert to GIF (since ImageTk might be missing and PNG support variable)
            pil_image = Image.open(image_path)

            # Resize
            base_width = 300
            w_percent = (base_width / float(pil_image.size[0]))
            h_size = int((float(pil_image.size[1]) * float(w_percent)))
            pil_image = pil_image.resize(
                (base_width, h_size), Image.Resampling.LANCZOS)

            # Save as temp GIF
            temp_gif = os.path.join(script_dir, "temp_shield.gif")
            pil_image.save(temp_gif, "GIF")

            image = tk.PhotoImage(file=temp_gif)

            image_label = tk.Label(root, image=image, bg="#f0f0f0")
            image_label.image = image  # Keep reference
            image_label.pack(pady=10)
            print("Imagem carregada com sucesso (GIF convertido).")

            # Note: We keep the temp file. Cleaning it up is tricky while app runs.
            # We could use base64 encoding to avoid temp file but this is simpler.
        else:
            print("Arquivo de imagem não encontrado.")
            tk.Label(root, text="(Imagem não encontrada)", bg="#f0f0f0").pack()
    except Exception as e:
        print(f"Erro ao carregar imagem: {e}")
        tk.Label(
            root, text=f"(Erro ao carregar imagem: {e})", bg="#f0f0f0").pack()

    # Form Frame
    form_frame = tk.Frame(root, bg="#f0f0f0")
    form_frame.pack(pady=20)

    tk.Label(form_frame, text="Vitórias:", font=label_font,
             bg="#f0f0f0").grid(row=0, column=0, padx=5, pady=5)
    entry_vitorias = tk.Entry(form_frame, font=label_font)
    entry_vitorias.grid(row=0, column=1, padx=5, pady=5)

    tk.Label(form_frame, text="Derrotas:", font=label_font,
             bg="#f0f0f0").grid(row=1, column=0, padx=5, pady=5)
    entry_derrotas = tk.Entry(form_frame, font=label_font)
    entry_derrotas.grid(row=1, column=1, padx=5, pady=5)

    # Result Frame (Bordered)
    result_frame = tk.LabelFrame(root, text="Resultado", font=label_font,
                                 bg="#f0f0f0", fg="#333", padx=10, pady=10)  # Added LabelFrame with text
    result_frame.pack(pady=20, padx=20, fill="x")

    result_var = tk.StringVar()
    result_label = tk.Label(result_frame, textvariable=result_var,
                            font=title_font, bg="#f0f0f0", fg="#555", wraplength=450)
    result_label.pack()

    def calcular():
        try:
            v_str = entry_vitorias.get()
            d_str = entry_derrotas.get()

            if not v_str or not d_str:
                messagebox.showwarning(
                    "Aviso", "Por favor, preencha ambos os campos.")
                return

            v = int(v_str)
            d = int(d_str)
            saldo, nivel = calcular_nivel(v, d)
            result_var.set(
                f"O Herói tem de saldo de {saldo} está no nível de {nivel}")
        except ValueError:
            messagebox.showerror("Erro", "Por favor, insira números válidos.")

    def limpar():
        entry_vitorias.delete(0, tk.END)
        entry_derrotas.delete(0, tk.END)
        result_var.set("")

    # Buttons Frame
    btn_frame = tk.Frame(root, bg="#f0f0f0")
    btn_frame.pack(pady=10)

    btn_calc = tk.Button(btn_frame, text="Calcular",
                         command=calcular, font=label_font, bg="#d4d4d4")
    btn_calc.pack(side=tk.LEFT, padx=10)

    btn_clear = tk.Button(btn_frame, text="Limpar",
                          command=limpar, font=label_font, bg="#d4d4d4")
    btn_clear.pack(side=tk.LEFT, padx=10)

    root.mainloop()


def main():
    parser = argparse.ArgumentParser(
        description="Calculadora de Partidas Rankeadas")
    parser.add_argument("-c", "--cli", action="store_true",
                        help="Executar em modo CLI (linha de comando)")

    args = parser.parse_args()

    if args.cli:
        run_cli()
    else:
        run_gui()


if __name__ == "__main__":
    main()

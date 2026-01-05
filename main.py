import argparse
import tkinter as tk
from tkinter import messagebox
from tkinter import font as tkfont
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

        if os.path.exists(image_path):
            # Using PhotoImage for PNG support (Tkinter 8.6+)
            original_image = tk.PhotoImage(file=image_path)

            # Simple resizing isn't available in raw PhotoImage without PIL,
            # so we assume the asset is reasonably sized or we sub-sample.
            # If the image is large, we can subsample (scale down).
            # Let's try to subsample if it's huge, but for now display as is.
            # Ideally we would use PIL here but aiming for zero-dep if possible.
            # The generated images are usually 1024x1024 which is too big.
            # Let's subsample by 3 (approx 340px).
            image = original_image.subsample(3, 3)

            image_label = tk.Label(root, image=image, bg="#f0f0f0")
            image_label.image = image  # Keep reference
            image_label.pack(pady=10)
        else:
            tk.Label(root, text="(Imagem não encontrada)", bg="#f0f0f0").pack()
    except Exception as e:
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

    # Result Label
    result_var = tk.StringVar()
    result_label = tk.Label(root, textvariable=result_var,
                            font=title_font, bg="#f0f0f0", fg="#555", wraplength=480)

    def calcular():
        try:
            v = int(entry_vitorias.get())
            d = int(entry_derrotas.get())
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
    btn_frame.pack(pady=20)

    btn_calc = tk.Button(btn_frame, text="Calcular",
                         command=calcular, font=label_font, bg="#d4d4d4")
    btn_calc.pack(side=tk.LEFT, padx=10)

    btn_clear = tk.Button(btn_frame, text="Limpar",
                          command=limpar, font=label_font, bg="#d4d4d4")
    btn_clear.pack(side=tk.LEFT, padx=10)

    result_label.pack(pady=20)

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

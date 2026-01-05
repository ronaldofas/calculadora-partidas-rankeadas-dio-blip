class RankedCLI:
    """
    Responsável pela interface de linha de comando.
    """

    def __init__(self, calculator):
        self.calculator = calculator

    def run(self):
        print("--- Calculadora de Partidas Rankeadas (CLI) ---")
        try:
            vitorias = int(input("Digite a quantidade de vitórias: "))
            derrotas = int(input("Digite a quantidade de derrotas: "))

            saldo, nivel = self.calculator.calculate_level(vitorias, derrotas)

            print(
                f"O Herói tem de saldo de **{saldo}** está no nível de **{nivel}**")
        except ValueError:
            print(
                "Erro: Por favor, insira apenas números inteiros para vitórias e derrotas.")

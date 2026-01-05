class RankedCalculator:
    """
    Responsável pela lógica de cálculo de nível.
    """

    def calculate_level(self, vitorias, derrotas):
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

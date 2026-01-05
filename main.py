from src.ui.gui import RankedGUI
from src.ui.cli import RankedCLI
from src.logic.calculator import RankedCalculator
import argparse
import sys
import os

# Add the project root to sys.path to ensure imports work correctly
sys.path.append(os.path.dirname(os.path.abspath(__file__)))


def main():
    parser = argparse.ArgumentParser(
        description="Calculadora de Partidas Rankeadas")
    parser.add_argument("-c", "--cli", action="store_true",
                        help="Executar em modo CLI (linha de comando)")

    args = parser.parse_args()

    calculator = RankedCalculator()

    if args.cli:
        app = RankedCLI(calculator)
        app.run()
    else:
        app = RankedGUI(calculator)
        app.run()


if __name__ == "__main__":
    main()

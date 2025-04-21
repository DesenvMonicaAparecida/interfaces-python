import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton, QHBoxLayout
import requests

def obter_taxa(moeda='USD-BRL'):
    url = f"https://economia.awesomeapi.com.br/last/{moeda}"
    resposta = requests.get(url)
    if resposta.status_code == 200:
        dados = resposta.json()
        return float(dados[moeda.replace("-", "")]["bid"])
    return 5.0

class ConversorApp(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Conversor de Moedas")
        self.setGeometry(100, 100, 400, 200)

        self.layout = QVBoxLayout()

        self.valor_input = QLineEdit(self)
        self.valor_input.setPlaceholderText("Digite o valor em Reais (R$)")
        self.layout.addWidget(self.valor_input)

        self.converter_button = QPushButton("Converter", self)
        self.converter_button.clicked.connect(self.converter)
        self.layout.addWidget(self.converter_button)

        self.resultado_label = QLabel("Resultado:", self)
        self.layout.addWidget(self.resultado_label)

        self.setLayout(self.layout)

    def converter(self):
        try:
            valor = float(self.valor_input.text())
            resultado = ""
            for moeda in ["USD", "EUR", "GBP"]:
                taxa = obter_taxa(moeda)
                convertido = valor / taxa
                resultado += f"{moeda}: {convertido:.2f}\n"
            self.resultado_label.setText(resultado)
        except ValueError:
            self.resultado_label.setText("Digite um valor numérico válido!")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    app_window = ConversorApp()
    app_window.show()
    sys.exit(app.exec_())

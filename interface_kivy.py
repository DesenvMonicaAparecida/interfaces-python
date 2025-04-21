from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
import requests

def obter_taxa(moeda='USD-BRL'):
    url = f"https://economia.awesomeapi.com.br/last/{moeda}"
    resposta = requests.get(url)
    if resposta.status_code == 200:
        dados = resposta.json()
        return float(dados[moeda.replace("-", "")]["bid"])
    return 5.0

class ConversorApp(App):
    def build(self):
        layout = BoxLayout(orientation="vertical", padding=10, spacing=10)

        self.valor_input = TextInput(hint_text="Digite o valor em Reais (R$)", multiline=False)
        layout.add_widget(self.valor_input)

        self.resultado_label = Label(text="Resultado:")
        layout.add_widget(self.resultado_label)

        converter_button = Button(text="Converter")
        converter_button.bind(on_press=self.converter)
        layout.add_widget(converter_button)

        return layout

    def converter(self, instance):
        try:
            valor = float(self.valor_input.text)
            resultado = ""
            for moeda in ["USD", "EUR", "GBP"]:
                taxa = obter_taxa(moeda)
                convertido = valor / taxa
                resultado += f"{moeda}: {convertido:.2f}\n"
            self.resultado_label.text = resultado
        except ValueError:
            self.resultado_label.text = "Digite um valor numérico válido!"

if __name__ == "__main__":
    ConversorApp().run()

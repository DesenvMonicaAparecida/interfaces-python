import dearpygui.dearpygui as dpg
import requests

def obter_taxa(moeda='USD-BRL'):
    url = f"https://economia.awesomeapi.com.br/last/{moeda}"
    resposta = requests.get(url)
    if resposta.status_code == 200:
        dados = resposta.json()
        return float(dados[moeda.replace("-", "")]["bid"])
    return 5.0

def converter_callback(sender, app_data):
    try:
        valor = float(dpg.get_value("valor_input"))
        resultado = ""
        for moeda in ["USD", "EUR", "GBP"]:
            taxa = obter_taxa(moeda)
            convertido = valor / taxa
            resultado += f"{moeda}: {convertido:.2f}\n"
        dpg.set_value("resultado_label", resultado)
    except ValueError:
        dpg.set_value("resultado_label", "Digite um valor numérico válido!")

dpg.create_context()

# Corrigido: remover a parte do key handler (usando a abordagem atual)
with dpg.handler_registry():
    dpg.add_key_press_handler(callback=lambda sender, app_data: dpg.stop_dearpygui())

with dpg.window(label="Conversor de Moedas"):
    dpg.add_input_text(label="Valor em Reais (R$):", tag="valor_input")
    dpg.add_button(label="Converter", callback=converter_callback)
    dpg.add_text("Resultado:", tag="resultado_label")

dpg.create_viewport(title='Conversor de Moedas', width=400, height=200)
dpg.setup_dearpygui()
dpg.show_viewport()
dpg.start_dearpygui()
dpg.destroy_context()

import tkinter as tk
from tkinter import ttk, messagebox
import requests

# Taxas de conversão
#TAXAS = {
#    "Dólar (USD)": 5.81,
#   "Euro (EUR)": 6.68,
#    "Libra (GBP)": 7.76,
#}

# Função para obter a taxa da API
def obter_taxa(moeda):
    try:
        url = f"https://economia.awesomeapi.com.br/last/{moeda}-BRL"
        resposta = requests.get(url)
        resposta.raise_for_status()
        dados = resposta.json()
        return float(dados[f"{moeda}BRL"]["bid"])
    except Exception as e:
        messagebox.showerror("Erro de conexão", f"Não foi possível buscar a cotação de {moeda}.\n\n{e}")
        return None

# Função de conversão
def converter():
    try:
        valor = float(entrada_valor.get())
        resultado = ""

        for moeda in ["USD", "EUR", "GBP"]:
            taxa = obter_taxa(moeda)
            if taxa:
                convertido = valor / taxa
                resultado += f"{moeda}: {convertido:.2f}\n"

        resultado_texto.set(resultado)
    except ValueError:
        messagebox.showerror("Erro", "Digite um valor numérico válido.")

# Configuração da janela/Interface
janela = tk.Tk()
janela.title("💱 Conversor de Moedas (Tempo Real)")
janela.geometry("400x400")
janela.configure(bg="#eef4f8")

# Estilo moderno
style = ttk.Style()
style.theme_use("clam")
style.configure("TLabel", background="#f0f4f7", font=("Segoe UI", 10))
style.configure("TButton", font=("Segoe UI", 10, "bold"))
style.configure("TEntry", font=("Segoe UI", 10))

# Layout
frame = ttk.Frame(janela, padding=20)
frame.pack(expand=True)

ttk.Label(frame, text="Valor em Reais (R$):").pack(pady=5)
entrada_valor = ttk.Entry(frame)
entrada_valor.pack(pady=5)

ttk.Button(frame, text="Converter", command=converter).pack(pady=10)

ttk.Label(frame, text="Resultado:", font=("Segoe UI", 10, "bold")).pack(pady=(20, 5))
resultado_texto = tk.StringVar()
ttk.Label(frame, textvariable=resultado_texto, foreground="#1a73e8", font=("Consolas", 10)). pack()


# Iniciar interface
janela.mainloop()

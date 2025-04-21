import customtkinter as ctk
import tkinter.messagebox as messagebox  # Importando o messagebox do Tkinter
import requests  # Importando a biblioteca requests para realizar as requisições HTTP

def obter_taxa(moeda='USD-BRL'):
    try:
        url = f"https://economia.awesomeapi.com.br/last/{moeda}"
        resposta = requests.get(url)
        resposta.raise_for_status()  # Levanta um erro se a resposta for uma falha (erro HTTP)
        dados = resposta.json()
        return float(dados[moeda.replace("-", "")]["bid"])  # Retorna a taxa de câmbio
    except (requests.exceptions.RequestException, KeyError, ValueError) as e:
        print(f"Erro ao obter taxa: {e}")
        return None  # Retorna None se houver erro

def converter():
    try:
        # Captura o valor inserido pelo usuário e substitui vírgula por ponto
        valor = float(entrada_valor.get().replace(',', '.'))  # Substitui vírgula por ponto
        if valor <= 0:
            raise ValueError("O valor deve ser maior que zero.")
        
        resultado = ""
        moedas = ["USD", "EUR", "GBP"]
        for moeda in moedas:
            taxa = obter_taxa(f"{moeda}-BRL")  # Exemplo: USD-BRL
            if taxa is not None:
                convertido = valor / taxa
                resultado += f"{moeda}: {convertido:.2f}\n"
            else:
                resultado += f"Erro ao obter taxa para {moeda}.\n"
        
        resultado_texto.set(resultado)
    except ValueError:
        messagebox.showerror("Erro", "Digite um valor numérico válido!")  # Mostra erro se a conversão falhar
    except Exception as e:
        messagebox.showerror("Erro", f"Ocorreu um erro: {e}")  # Captura qualquer outro erro inesperado

# Interface CustomTkinter
ctk.set_appearance_mode("dark")
janela = ctk.CTk()
janela.title("Conversor de Moedas")
janela.geometry("380x380")

ctk.CTkLabel(janela, text="Valor em Reais (R$):").pack(pady=10)
entrada_valor = ctk.CTkEntry(janela)
entrada_valor.pack(pady=10)

ctk.CTkButton(janela, text="Converter", command=converter).pack(pady=10)

resultado_texto = ctk.StringVar()
ctk.CTkLabel(janela, textvariable=resultado_texto, font=("Arial", 12)).pack(pady=10)

janela.mainloop()


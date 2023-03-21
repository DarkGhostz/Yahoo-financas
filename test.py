import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt
import datetime

tabela_empresas = pd.read_excel("Empresas.xlsx")
print(tabela_empresas)

for empresa in tabela_empresas['Empresas'].tolist():
    print(empresa)
    
    if '.' in empresa:
        empresa = empresa.split('.')[0]
    
    try:
        start_date = datetime.datetime(2022, 1, 1)
        end_date = datetime.datetime(2023, 3, 20)
    
        cotacao = yf.download(empresa, start=start_date, end=end_date)
        cotacao["Adj Close"].plot()
        plt.show()
    except:
        print("Erro ao processar a empresa", empresa)
        continue

    
    


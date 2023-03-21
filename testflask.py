import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt
import datetime
import base64
import os
from io import BytesIO
from flask import Flask, render_template

app = Flask(__name__, template_folder='templates')


    


def fig_to_base64(fig):
    img_bytes = BytesIO()
    fig.savefig(img_bytes, format='png')
    img_bytes.seek(0)
    return base64.b64encode(img_bytes.getvalue()).decode()

@app.route('/')
def home():
    tabela_empresas = pd.read_excel("Empresas.xlsx")
    empresas = []
    
    for empresa in tabela_empresas['Empresas'].tolist():
        print(empresa)

        if '.' in empresa:
            empresa = empresa.split('.')[0]

        try:
            start_date = datetime.datetime(2022, 1, 1)
            end_date = datetime.datetime(2023, 3, 20)

            cotacao = yf.download(empresa, start=start_date, end=end_date)
            fig = plt.figure()
            cotacao["Adj Close"].plot()
            img = fig_to_base64(fig)
            empresas.append((empresa, img))
        except:
            print("Erro ao processar a empresa", empresa)
            continue
    return render_template(os.path.join(app.template_folder, 'index.html'), empresas=empresas)


if __name__ == '__main__':
    app.run(debug=True)
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
def classe(x):
    if x in ["Açougue", "Mercado", "Padaria"]:
        y = "Açougue/Mercado/Padaria" # espaço em branco na linha em branco por bug do ob-python; senão dá erro de indentação
 
    elif x in ["Restaurante", "Cafeteria"]:
        y = "Restaurante/Cafeteria"
 
    elif x in ["Combustível"]:
        y = "Transporte"
 
    elif x in ["Aluguel", "Condomínio", "Energia", "Internet"]:
        y = "Moradia"
 
    elif x[:6] == "Cartão":
        y = "Fatura do cartão"
 
    elif x in ["Cashback", "Dividendos", "Juros", "Trade"]:
        y = "Renda extra"
 
    else:
        y = "Outro"
 
    return y

saldo = 3472.72

outubro = pd.read_csv("outubro.csv")
n = len(outubro)
data = pd.Series(["2022-10-" for i in range(n)]) #prefixos para datas
data = data.str.cat(outubro.Data.astype("string")) #data com prefixo mas ainda como string
outubro.Data = data.astype("datetime64") #data como datetime64
outubro = outubro.sort_values(by="Data")
outubro

forma = outubro.groupby("Forma").sum() #Valor envolvido em cada forma de pagamento
forma

forma.plot(kind="bar", title="Valor por forma de pagamento", ylabel="R$", xlabel="", legend=False)
plt.tick_params(labelrotation=0)
fname = "outubro-forma.png"
plt.savefig(fname)
plt.close()
fname # retorna ao org

outubro["Classe"] = outubro.Descrição.apply(classe) #Aplica função classe à Descrição
classifica = outubro.groupby(by="Classe").sum() #Valor envolvido em cada classe
classifica

classifica.drop(["Renda extra", "Fatura do cartão"]).plot(kind="barh", title="Valor gasto por classe", legend=False)
plt.xlabel("R$")
plt.ylabel("")
plt.tight_layout()
fname = "outubro-classe.png"
plt.savefig(fname)
plt.close()
fname

saldo = saldo + forma.Valor["Depósito"] - forma.Valor["Débito"]
saldo

if saldo<0:
    alerta = "ATENÇÃO! Há gastos futuros que ainda precisam ser pagos."
    alerta

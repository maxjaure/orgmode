import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from tabulate import tabulate
def classe(x):
    if x in ["Açougue", "Mercado", "Padaria"]:
        y = "Açougue/Mercado/Padaria" # espaço em branco na linha em branco por bug do ob-python; senão dá erro de indentação
 
    elif x in ["Restaurante", "Cafeteria"]:
        y = "Restaurante/Cafeteria"
 
    elif x in ["Combustível", "Seguro do carro"]:
        y = "Transporte"
 
    elif x in ["Aluguel", "Condomínio", "Celular", "Energia", "Internet"]:
        y = "Moradia"
 
    elif x in ["Medicamentos"]:
        y = "Saúde"
 
    elif "Plano de saúde" in x:
        y = "Saúde"
 
    elif x in ["Cabeleireiro", "Natura"]:
        y = "Cuidado pessoal"
 
    elif x[:6] == "Cartão":
        y = "Fatura do cartão"
 
    elif x in ["DARF", "IRRF"]:
        y = "Impostos"
 
    elif x == "Salário":
        y = "Salário"
 
    elif x in ["Cashback", "Dividendos", "Juros", "Nota Paraná", "Trade"]:
        y = "Renda extra"
 
    elif x[:7] == "Resgate":
        y = "Renda extra"
 
    else:
        y = "Outro"
 
    return y

nomemes = "outubro"
saldo = 3472.72

mes = pd.read_csv(nomemes + ".csv")
n = len(mes)
data = pd.Series(["2022-10-" for i in range(n)]) #prefixos para datas
data = data.str.cat(mes.Data.astype("string")) #data com prefixo mas ainda como string
mes.Data = data.astype("datetime64") #data como datetime64
mes = mes.sort_values(by="Data")
mes2 = mes
mes2.Data = mes2.Data.astype("string")
tabulate(mes2,headers=mes2.columns,showindex=False,floatfmt=".2f",tablefmt="orgtbl")

forma = mes.groupby("Forma").sum() #Valor envolvido em cada forma de pagamento
tabulate(forma,headers=forma.columns,floatfmt=".2f",tablefmt="orgtbl")

forma.plot(kind="bar", title="Valor por forma de pagamento", ylabel="R$", xlabel="", legend=False)
plt.tick_params(labelrotation=0)
fname = nomemes + "-forma.png"
plt.savefig(fname)
plt.close()
fname # retorna ao org

mes["Classe"] = mes.Descrição.apply(classe) #Aplica função classe à Descrição
classifica = mes.groupby(by="Classe").sum() #Valor envolvido em cada classe
tabulate(classifica,headers=classifica.columns,floatfmt=".2f",tablefmt="orgtbl")

classifica2 = classifica
if "Fatura do cartão" in classifica.index:
    classifica2 = classifica2.drop("Fatura do cartão")

if "Renda extra" in classifica.index:
    classifica2 = classifica2.drop("Renda extra")

if "Salário" in classifica.index:
    classifica2 = classifica2.drop("Salário")

classifica2.plot(kind="barh", title="Valor gasto por classe", legend=False)
plt.xlabel("R$")
plt.ylabel("")
plt.tight_layout()
fname = nomemes + "-classe.png"
plt.savefig(fname)
plt.close()
fname

if "Depósito" in forma.index:
    saldo += forma.Valor["Depósito"]

if "Débito" in forma.index:
    saldo -= forma.Valor["Débito"]

if "Salário" in classifica.index:
    saldo += classifica.Valor["Salário"]
saldo

if saldo<0:
    alerta = "*ATENÇÃO!* Há gastos futuros que ainda precisam ser pagos."
    alerta

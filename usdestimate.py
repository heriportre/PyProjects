import pandas as pd
import numpy as np
import seaborn as sns
from matplotlib import pyplot as plt

data = pd.read_csv(r"D:\python_workspace\project11\USD_TRY_Verileri.csv")

#data = data.iloc[:, 1:2]
data = data["Simdi"]

def conv(st:str):
    st=st.split(",")
    st.insert(1,".")
    st="".join(st)
    return float(st)
data = np.flipud(data.apply(conv))
x=np.arange(522)

m,b= np.polyfit(x,data,1)

plt.scatter(x,data)
plt.plot(m*x+b)
plt.show()

#sns.regplot(x=x,y=data)

plt.show()
import pandas as pd
from matplotlib import pyplot as plt

plt.style.use('ggplot')

smartphone = pd.read_csv('data_smartphone.csv')

oppo = smartphone[smartphone.Brand == 'OPPO']
realme = smartphone[smartphone.Brand == 'REALME']
iphone = smartphone[smartphone.Brand == 'APPLE']
vivo = smartphone[smartphone.Brand == 'VIVO']

rev_oppo = oppo['Reviewer'].mean() 
rev_realme = realme['Reviewer'].mean() 
rev_iphone = iphone['Reviewer'].mean() 
rev_vivo = vivo['Reviewer'].mean()

brand = ['Oppo', 'Realme', 'Vivo', 'Iphone']
review = [rev_oppo, rev_realme, rev_vivo, rev_iphone]

x_pos = [i for i, _ in enumerate(brand)]

plt.bar(x_pos, review)
plt.xlabel("Brand Smartphone")
plt.ylabel("Rata-rata Review")
plt.title("Analisis Perbandingan Rata-rata Review Brand Smartphone Pada Website blibli")

plt.xticks(x_pos, brand)

plt.show()
#importação das bibliotecas
import pandas as pd
import matplotlib.pyplot as plt

#carregamento dos dados
base = pd.read_csv('trees.csv')
base.head()

#girth com volume
plt.scatter(base.Girth, base.Volume)

#girth com height
plt.scatter(base.Girth, base.Height)

#height com volume
plt.scatter(base.Height, base.Volume, marker='*')

#histograma volume
plt.hist(base.Volume)

#imprimindo juntos
#criação de figura, no qual os gráficos serão posicionados
plt.figure(1)
plt.subplot(2, 2, 1)
plt.scatter(base.Girth, base.Volume)
plt.subplot(2, 2, 2)
plt.scatter(base.Girth, base.Height)
plt.subplot(2, 2, 3)
plt.scatter(base.Height, base.Volume, marker='*')
plt.subplot(2, 2, 4)
plt.hist(base.Volume)

base.plot.bar(color='red')

base.plot.bar(color = ['red', 'yellow', 'black', 'gray', 'blue', 'pink', 'orange', 'green'])


https://colab.research.google.com/drive/1wqUZyVogLcz4fwD2cEhkGYUiIZaMu6rR#scrollTo=RfJORR4MA7d4


print(df.plot.scatter('chuva','casos-confirmados'))
print(df.plot.scatter('chuva','temperatura-media'))
print(df.plot.scatter('chuva','temperatura-mininima'))
print(df.plot.scatter('chuva','temperatura-maxima'))
plt.show()

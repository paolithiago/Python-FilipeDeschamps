https://colab.research.google.com/drive/1wqUZyVogLcz4fwD2cEhkGYUiIZaMu6rR#scrollTo=IMiEZa7DC2lh



corr = df[['chuva','temperatura-media']].corr()
display(corr)

corr = df[['chuva','temperatura-mininima']].corr()
display(corr)

corr = df[['chuva','temperatura-maxima']].corr()
display(corr)

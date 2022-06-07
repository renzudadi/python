import pandas as pd
import ssl
ssl._create_default_https_context = ssl._create_unverified_context

df = pd.read_html("https://www.boc.cn/sourcedb/whpj/")

del df[0]
del df[1]
del df[1]
df = df[0]
currency = df.loc[7]
text = str(currency)
text = text.split()
cny_currency  = "中国银行英镑"+"汇率"+" "+str(float(text[9])/100)
print(cny_currency)

import pandas as pd
from urllib.request import urlopen
import re

df = pd.read_html("https://www.boc.cn/sourcedb/whpj/")
del df[0]
del df[1]
del df[1]
df = df[0]
currency = df.loc[7]
text = str(currency)
text = text.split()
cny_currency  = "英镑"+"境内汇率"+" "+str(float(text[11])/100)

URL = urlopen("https://www.bing.com/search?q=1%20GBP%20%E5%88%B0%20CNH&FORM=S00037&filter=ufn:%22GBP%22%20aid:%22de79675229366a3bf9c00cb0b4f461a4%22%20sid:%22CNH1%22%20cpair:%22CNH1%22%20dstr:%22%22%20currency:%221%22")
URL = URL.read()
URL = str(URL)
pos = re.search("CNH - Chinese Yuan Offshore",URL).span()
URL = URL[pos[0]:(pos[0]+500)]
pos_value = re.search("value=",URL).span()
currency2 = URL = URL[(pos_value[0]+7):(pos_value[0]+11)]
cnh_currency = "英镑"+"离岸汇率"+" "+currency2
time_of_result = text[12]+" "+text[13]+" "+text[14]
message = cny_currency +"\n"+ cnh_currency +"\n"+ time_of_result
print(message)
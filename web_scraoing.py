import requests
from bs4 import BeautifulSoup
import pandas as pd 
import time



code = ['DIA_IA_TS','DIA_DEV_TS','DIA_DES_TS','DIA_ID_TS','THR_MH_TS','THR_MT_TS','AGRI_TA_TS','AGRI_MA_TS','GE_GE_TS','MTI_GI_TS','GC_GE_TS']
FillièresT = []
descriptionT = []
titresT =[]
for i in code:
    url = f"https://www.myway.ac.ma/fr/filiere/{i}"
    time.sleep(6)
    response = requests.get(url)
    soup = BeautifulSoup(response.content,"html.parser")
    Fillières = [h3.text for h3 in soup.find_all('h3')]
    titres = []
    tittres =[titres.append(i) for c in range(len(Fillières))]
        
    description = [p.text for p in soup.find_all('div', class_='nl-wrap')]
    NVdescription = []
    for des in description:
        nvfil = des.strip('</p>')
        NVdescription.append(nvfil)
    for f in Fillières:
        FillièresT.append(f)

    for d in NVdescription:
        descriptionT.append(d)

    for t in titres:
        titresT.append(t)
  
dic = {"Filières" :titresT, "Spétialitée,":FillièresT,"description":descriptionT}
df = pd.DataFrame(dic)
# print(df)
df.to_csv('web_scraping.csv')
# print(df)





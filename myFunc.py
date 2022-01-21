import urllib.request as req
import bs4
import json

def fetch(country):
    with open("covid_country_condition.txt","r",encoding="utf-8") as file:
        a=json.load(file)
    key_country=a.keys()
    for item in key_country:
        if country in item:
            str_country="在 "+country+"\n確診人數為: "+a[country][0]+"\n死亡人數為: "+a[country][1]+"\n康復人數為: "+a[country][2]
            return str_country
        
    return "你查詢的國家並不存在!請重新嘗試~"



def update():
    url="https://www.thenewslens.com/interactive/129422"
    request=req.Request(url,headers={"user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.163 Safari/537.36"})
    with req.urlopen(request) as response:
        data=response.read().decode("utf-8")
    root=bs4.BeautifulSoup(data,'html.parser')

    countries=root.find_all("div",class_='country-name svelte-1quy94t')
    confirmed_number=root.find_all("div",class_='confirmed number svelte-1quy94t')
    death_number=root.find_all("div",class_='death number svelte-1quy94t')
    recovered_number=root.find_all("div",class_='recovered number svelte-1quy94t')

    total=len(countries)
    a={}
    file=open("covid_country_condition.txt",mode="w",encoding="utf-8")
    for n in range(total):
        a[countries[n].text.strip()] = [confirmed_number[n].text.strip(), death_number[n].text.strip(), recovered_number[n].text.strip()]
    js=json.dumps(a, ensure_ascii=False)
    file.write(js)
    file.close()

    return "資料更新完成!"



    




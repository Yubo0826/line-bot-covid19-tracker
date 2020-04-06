import urllib.request as req
import bs4

def covid(country):
    url="https://www.thenewslens.com/interactive/129422"
    request=req.Request(url,headers={"user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.163 Safari/537.36"})
    with req.urlopen(request) as response:
        data=response.read().decode("utf-8")
    root=bs4.BeautifulSoup(data,'html.parser')

    countries=root.find_all("div",class_='country-name svelte-1quy94t')
    confirmed_number=root.find_all("div",class_='confirmed number svelte-1quy94t')
    death=root.find_all("div",class_='death number svelte-1quy94t')
    recovered=root.find_all("div",class_='recovered number svelte-1quy94t')

    total=len(countries)
    count_dic={}
    for n in range(total):
        count_dic[countries[n].text]=confirmed_number[n].text + death[n].text + recovered[n].text

    return count_dic[country]
        


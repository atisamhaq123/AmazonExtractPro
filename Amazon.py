#Python program to scrape website
#and save quotes from website
import requests
from bs4 import BeautifulSoup
import csv 
headers = {
        'dnt': '1',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.61 Safari/537.36',
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'sec-fetch-site': 'same-origin',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-user': '?1',
        'sec-fetch-dest': 'document',
        'referer': 'https://www.amazon.com/',
        'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
        'authority': 'www.amazon.com',
        'pragma': 'no-cache',
        'cache-control': 'no-cache',
        'dnt': '1',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (X11; CrOS x86_64 8172.45.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.64 Safari/537.36',
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'sec-fetch-site': 'none',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-dest': 'document',
        'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
    }
    

    

URL = "https://www.amazon.com/-/es/Los-m%C3%A1s-vendidos-Health-Personal-Care-Suplementos-Vitam%C3%ADnicos-Individuales/zgbs/hpc/6936790011/ref=zg_bs_nav_hpc_2_3764441"
r = requests.get(URL, headers=headers)

soup = BeautifulSoup(r.content, 'html5lib')


table = soup.find("div", attrs = {'id':'zg-center-div'}).find("ol",attrs={'class':"a-ordered-list a-vertical"})

array=[]
count=1
for row in table.findAll("li",attrs={'class':"zg-item-immersion"}):
    print(count)
    gg={}
    net=row.span.div
    title=row.span.a.text
    if(count==30 or count==40 or count==18 or count==23):
        reviews=""
    else:
        reviews=net.find("a",attrs={'class':"a-size-small a-link-normal"}).text
    price=net.find("span",attrs={'class':"p13n-sc-price"}).text
    image=row.span.div.img['src']
    link=row.span.div.a["href"]
    ###Adding values
    gg['Title']=title.strip()
    gg['Reviews']=reviews
    gg['Price']=price
    gg['Image']=image
    gg['href']=link
    gg["index"]=count
    array.append(gg)
    count+=1
    
##Make CSV file
filename = 'Amazon.csv'
with open(filename, 'w', newline='') as f:
    w = csv.DictWriter(f,['index','Title','Price','Reviews','Image','href'])
    w.writeheader()
    for quote in array:
        w.writerow(quote)

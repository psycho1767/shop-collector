from requests import get
from bs4 import *
from convertpersianhelp import *
import openpyxl
# links = [f"https://balad.ir/city-gorgan/cat-coffee-shop?page={i}#12.43/36.82633/54.47032" for i in range(1,7)]

links = [f"https://balad.ir/city-gorgan/cat-clothing-store?page={i}#12.34/36.83237/54.4759" for i in range(1,11)]

num = 0
for link in links:
    document = get(link,timeout=5)

    bs = BeautifulSoup(document.content,'html.parser')

    items = bs.findAll('div',class_='BundleItem_item__texts__2l15O')

    book = openpyxl.load_workbook('lebas.xlsx')
    sheet = book.active
    for item in items: 
        try:
            number = item.find("a").attrs['href']
            number = number[6:]
        except:
            number = ''
        try:
            title = item.find("h2")
        except:
            title = ''
        try:
            typ = item.findAll("div")
            typ = typ[-1]
        except:
            typ = ''
        try:
            addres = item.find('p',class_='BundleItem_item__subtitle__2a2IA BundleItem_ellipsis__2lMRx')
        except:
            addres = ''
        if not number == '':
            itemdata = [title.text,typ.text,addres.text,number]
            sheet.append(itemdata)
            num += 1
            print(num)
        
    book.save("shop.xlsx")
    

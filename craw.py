#얘덜아 이거 20개만 크롤링 되는 코드야
#왜 20개만 되는지 모르겠어
#포문 돌려서 여러번 하면 똑같은 20개가 여러번 저장된닥...

import requests
import urllib.request
 
from scrapy.selector import Selector

#이거 count바꾸면 알아서 20개 count된다

count = 2040

#inputSearch에 검색어 넣으면 돼 그니까 장미면 장미 넣고 장미꽃 넣고
#rose , roseficture 이렇게 여러번 넣으면 여러경우 나오겠지,,?
#1000/20이면 50이니까 검색어 50개만 해봐..
#근데 중간에 쓸모없는것도 저장되니까 그거ㅓ 걸러줘야해
#어디에 저장되냐면 코드있는 경로에 저장된다

inputSearch = "백합"
base_url = "https://www.google.co.kr/search?biw=1597&bih=925&" \
             "tbm=isch&sa=1&btnG=%EA%B2%80%EC%83%89&q=" + inputSearch
 
 
def img_url_from_page(url):
    html = requests.get(url).text  
 
    sel = Selector(text=html)
 
    img_names = sel.css('td a img::attr(src)').extract()
 
    img_names = [img_name for img_name in img_names]
 
    return img_names
 
 
def img_from_url(image_names):
    global count
    count += 1
    name = count
 
    full_name = str(name) + ".jpg"
 
    urllib.request.urlretrieve(image_names, full_name)
 
 
for i in img_url_from_page(base_url):
    img_from_url(i)

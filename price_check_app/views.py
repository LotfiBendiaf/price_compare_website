
import requests
import random
from math import ceil
from varname import nameof
from requests.compat import quote_plus
from django.shortcuts import render
from bs4 import BeautifulSoup
from django.shortcuts import render
from . import models

# Create your views here.

AMAZON_URL = 'https://www.amazon.fr/s?k={}'

EBAY_URL = "https://www.ebay.fr/sch/i.html?_from=R40&_trksid=p2380057.m570.l1311&_nkw={}"

ALIBABA_URL = "https://www.alibaba.com/trade/search?fsb=y&IndexArea=product_en&CatId=&SearchText={}"

FNAC_URL = "https://www.fnac.com/SearchResult/ResultList.aspx?SCat=0%211&Search={}"

FLIPKART_URL = "https://www.flipkart.com/search?q={}"

BASE_URL = 'https://losangeles.craigslist.org/search/?query={}'

BASE_IMAGE_URL = 'https://images.craigslist.org/{}_300x300.jpg'

def home(request):
    return render(request, 'price_check_app/home.html')

def results(request):

    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.135 Safari/537.36'}

    #Search User data 
    search = request.POST.get('search')
    models.Search.objects.create(search=search)

    #Amazon Data
    #amazon_postings = []
    final_amazon_url = AMAZON_URL.format(quote_plus(search))
    amazon_page = requests.get(final_amazon_url, headers=headers)
    amazon_data = amazon_page.text
    amazon_soup = BeautifulSoup(amazon_data, features='html.parser')
    #amazon_post = amazon_soup.find_all(class_='a-section a-spacing-medium')

    #Ebay Data
    #ebay_postings = []
    final_ebay_url = EBAY_URL.format(quote_plus(search))
    ebay_page = requests.get(final_ebay_url, headers=headers)
    ebay_data = ebay_page.text
    ebay_soup = BeautifulSoup(ebay_data, features='html.parser')
    #ebay_post = ebay_soup.find_all('span', {'class': 's-item__price'})

    #Alibaba Data
    #flipkart_postings = []
    final_alibaba_url = ALIBABA_URL.format(quote_plus(search))
    alibaba_page = requests.get(final_alibaba_url, headers=headers)
    alibaba_data = alibaba_page.text
    alibaba_soup = BeautifulSoup(alibaba_data, features='html.parser')
    #flipkart_post = flipkart_soup.find_all('div', {'class': '_3liAhj'})

    #Fnac Data
    #flipkart_postings = []
    final_fnac_url = FNAC_URL.format(quote_plus(search))
    fnac_page = requests.get(final_fnac_url, headers=headers)
    fnac_data = fnac_page.text
    fnac_soup = BeautifulSoup(fnac_data, features='html.parser')
    #flipkart_post = flipkart_soup.find_all('div', {'class': '_3liAhj'})

    #Flipkart Data
    #flipkart_postings = []
    final_flipkart_url = FLIPKART_URL.format(quote_plus(search))
    flipkart_page = requests.get(final_flipkart_url, headers=headers)
    flipkart_data = flipkart_page.text
    flipkart_soup = BeautifulSoup(flipkart_data, features='html.parser')
    #flipkart_post = flipkart_soup.find_all('div', {'class': '_3liAhj'})

    #Final Data
    final_postings = []
    final_craigslist_url = BASE_URL.format(quote_plus(search))
    print(final_craigslist_url)
    response = requests.get(final_craigslist_url, headers=headers)
    data = response.text
    soup = BeautifulSoup(data, features='html.parser')
    post_listings = soup.find_all('li', {'class': 'result-row'})

    #URL List
    urls_list = [final_craigslist_url, final_amazon_url, final_alibaba_url, final_ebay_url, final_fnac_url, final_flipkart_url]

    #Data Process
    for post in post_listings[:75]:
        post_titles = post.find(class_='result-title').text
        post_url = post.find('a').get('href')

        if post.find(class_='result-price'):
            post_price = post.find(class_='result-price').text
        else:
            post_price = 'N/A'

        if post.find(class_='result-image').get('data-ids'):
            post_image_id = post.find(
                class_='result-image').get('data-ids').split(',')[0].split(':')[1]
            post_image_url = BASE_IMAGE_URL.format(post_image_id)

        else:
            post_image_url = "https://piotrkowalski.pw/assets/camaleon_cms/image-not-found-4a963b95bf081c3ea02923dceaeb3f8085e1a654fc54840aac61a57a60903fef.png"

        craigslist_price = '$' + str(float(post_price.split('$')[1]))

        #Exceptions
        if post_price.split('$')[1] == '0':
            post_price = '$1'

        #Retrieve prices
        delta_price = int(ceil(float(post_price.split('$')[1])/10))
        amazon_price = '$' + str(float(post_price.split('$')[1]) + random.randrange(-delta_price, delta_price))
        delta_price = int(ceil(float(post_price.split('$')[1])/10))
        ebay_price = '$' + str(float(post_price.split('$')[1]) + random.randrange(-delta_price, delta_price))
        delta_price = int(ceil(float(post_price.split('$')[1])/10))
        alibaba_price = '$' + str(float(post_price.split('$')[1]) + random.randrange(-delta_price, delta_price))
        delta_price = int(ceil(float(post_price.split('$')[1])/10))
        fnac_price = '$' + str(float(post_price.split('$')[1]) + random.randrange(-delta_price, delta_price))
        delta_price = int(ceil(float(post_price.split('$')[1])/10))
        flipkart_price = '$' + str(float(post_price.split('$')[1]) + random.randrange(-delta_price, delta_price))

        best_price = '$' + str(min(float(craigslist_price.split('$')[1]), float(amazon_price.split('$')[1]), float(ebay_price.split('$')[1]), float(alibaba_price.split('$')[1]), float(fnac_price.split('$')[1]), float(flipkart_price.split('$')[1])))

        prices_list = [amazon_price, ebay_price, alibaba_price, fnac_price, flipkart_price, craigslist_price]

        final_postings.append(
            (post_titles, post_url, 
            craigslist_price, amazon_price, ebay_price, alibaba_price, fnac_price, flipkart_price,
            post_image_url, best_price,
            final_craigslist_url, final_amazon_url, final_alibaba_url, final_ebay_url, final_fnac_url, final_flipkart_url)
            
            )

    stuff = {
        'search': search,
        'final_postings': final_postings,
    }
    return render(request, 'price_check_app/results.html', stuff)

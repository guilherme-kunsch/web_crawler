import requests
from bs4 import BeautifulSoup
from concurrent.futures import ThreadPoolExecutor


# def scrape_promotions(url):
#     try:
#         headers = {
#             'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}
#         response = requests.get(url, headers=headers)
#         if response.status_code == 200:
#             soup = BeautifulSoup(response.text, 'html.parser')
#             promotions = soup.find_all(class_="promotion-class")
#             return [promo.get_text() for promo in promotions]
#         else:
#             return f"Erro ao acessar {url}: {response.status_code}"
#     except Exception as e:
#         return f"Falha ao acessar {url}: {str(e)}"

# urls = [
#     "https://www.precopopular.com.br",
#     "https://www.paguemenos.com.br",
#     "https://www.santaluciadrogarias.com.br"
# ]


# def scrape_multiple_sites(urls):
#     with ThreadPoolExecutor() as executor:
#         results = executor.map(scrape_promotions, urls)
#     return list(results)


# results = scrape_multiple_sites(urls)

# for url, promotions in zip(urls, results):
#     print(f"Promoções de {url}:\n", promotions)

response = requests.get("https://www.paguemenos.com.br")
content = response.content

site = BeautifulSoup(content, 'html.parser')

promocoes = site.find('a', attrs={'class': 'vtex-rich-text-0-x-link vtex-rich-text-0-x-link--menu-item_desktop vtex-rich-text-0-x-link--menu-item-1_desktop'})


print(promocoes.prettify())
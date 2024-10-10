import requests;

url = requests.get("https://www.google.com.br/?hl=pt-BR")

if url.status_code == 200:
    print("ola")
else:
    print("erro")
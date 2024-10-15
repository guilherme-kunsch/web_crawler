import requests
from bs4 import BeautifulSoup

def extrair_previsao(dia_classe):
    previsao = {}
    #aqui eu estou pegando toda class que tenha grid-item dia
    dia_elemento = previsoes.find('li', class_=f'grid-item dia {dia_classe}')
    if dia_elemento:
        #aqui estou pegando as informações de cada li dentro do elemento pai que no caso é o UL
        #para cada LI estou pegando a class específica que vai me trazer os dados
        previsao['dia_semana'] = dia_elemento.find('span', class_='text-0').text.strip()
        previsao['data'] = dia_elemento.find('span', class_='subtitle-m').text.strip()
        
        prob_chuva_elem = dia_elemento.find('span', class_='txt-strng probabilidad center')
        previsao['prob_chuva'] = prob_chuva_elem.text.strip() if prob_chuva_elem else "N/A"

        precipitacao_elem = dia_elemento.find('span', class_='changeUnitR')
        previsao['precipitacao'] = precipitacao_elem.text.strip() if precipitacao_elem else "N/A"

        temp_max_elem = dia_elemento.find('span', class_='max changeUnitT')
        previsao['temp_max'] = temp_max_elem.text.strip() if temp_max_elem else "N/A"

        temp_min_elem = dia_elemento.find('span', class_='min changeUnitT')
        previsao['temp_min'] = temp_min_elem.text.strip() if temp_min_elem else "N/A"

        velocidades = dia_elemento.find_all('span', class_='changeUnitW')
        previsao['velocidade_min'] = velocidades[0].text.strip() if len(velocidades) > 0 else "N/A"
        previsao['velocidade_max'] = velocidades[1].text.strip() if len(velocidades) > 1 else "N/A"
        
    return previsao

response = requests.get("https://www.tempo.com/vitoria_espirito-santo-l13010.htm")
content = response.content

site = BeautifulSoup(content, 'html.parser')

previsoes = site.find('ul', attrs={'class': 'grid-container-7 dias_w'})
with open('previsoes_tempo.txt', 'w', encoding='utf-8') as file:
    if previsoes:
        dias_classes = ['d1 activo', 'd2', 'd3', 'd4', 'd5', 'd6', 'd7']

        for dia_classe in dias_classes:
            previsao = extrair_previsao(dia_classe)
            if previsao:
                # Escreve a previsão no arquivo
                file.write(f"Dia: {previsao['dia_semana']}\n")
                file.write(f"Data: {previsao['data']}\n")
                file.write(f"Probabilidade de chuva: {previsao['prob_chuva']}\n")
                file.write(f"Precipitação: {previsao['precipitacao']}\n")
                file.write(f"Temperatura Máxima: {previsao['temp_max']}\n")
                file.write(f"Temperatura Mínima: {previsao['temp_min']}\n")
                file.write(f"Velocidade do vento: {previsao['velocidade_min']} - {previsao['velocidade_max']} km/h\n")
                file.write('---\n')
    else:
        file.write("Elemento <ul> não encontrado.\n")

print("Previsões salvas no arquivo 'previsoes_tempo.txt'.")

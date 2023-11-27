import requests
import pandas as pd
import xml.etree.cElementTree as ET

r = requests.get('http://servicos.cptec.inpe.br/XML/listaCidades')

if r.status_code == 200:
    # Parse do XML
    root = ET.fromstring(r.text)

    # função para imprimir as tags recursivamente
    def imprime_tags(element, indent=""):
            print(f'{element}Tag: {element.tag}')
            for child in element:
                imprime_tags(child, indent + " ")

    #imprime_tags(root)

    data = []

    for cidade in root.findall('.//cidade'):
         # Obtém os valores dos elemente: id, nome e uf
         id_cidade = cidade.find('id').text
         nome_cidade = cidade.find('nome').text
         uf_cidade = cidade.find('uf').text

         # Adcionamento os valores a uma lista com tupla
         data.append((id_cidade, nome_cidade, uf_cidade))

    # Criando um DataFrame pandas com os resultados
    df = pd.DataFrame(data, columns=['Id', 'Nome', 'UF'])

    print(df)

else:
     print('erro ao acessar a api')
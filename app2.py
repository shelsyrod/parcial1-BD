import json
import datetime
import boto3
import csv
from bs4 import BeautifulSoup
  
  
  
def poner_datos(event, context):
    nuevo = event['Records'][0]['s3']['object']['key']
    bucket = boto3.resource('s3').Bucket('daticosparcial')
    obj = bucket.Object(nuevo)
    
    print('llego')
    obj = obj.get()['Body'].read().decode('utf-8')
    soup = BeautifulSoup(obj, 'html.parser')
    a = soup.find_all('script', {'type': 'application/ld+json'})
    a_lines = str(str(a).splitlines()[1:-1])
    a_lista_casas = [casa for casa in a_lines.split('image')[1:]]
    diccionario_casas = {}
    lista_info = []
    for casa in a_lista_casas:
        diccionario_casas['imagen'] ='https://' + casa.split('jpg')[0].split('https://')[1] + 'jpg'
        diccionario_casas['titulo'] = casa.split('"name": ')[1].split('"description": ')[0]
        diccionario_casas['descripcion'] = casa.split('"description": ')[1].split('",')[0]
        lista_info.append(diccionario_casas)

    #poner la info en un bucket de s3
    actual = datetime.datetime.now()
    nombre = f"{actual.year}-{actual.strftime('%m')}-{actual.strftime('%d')}.txt"
    client = boto3.client('s3')
    client.put_object(Body=str(lista_info), Bucket='casasfinalparcial', Key=nombre)


    return {
        'statusCode': 200,
        'body': json.dumps('Finisimo')
    }

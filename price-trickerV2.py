#𝑭𝒆𝒊𝒕𝒐 𝒑𝒐𝒓 𝑽𝒊𝒏𝒊𝒄𝒊𝒖𝒔 𝑺𝒂𝒏𝒕𝒐𝒔-𝑻𝒆𝒄𝒉
#𝑴𝒐𝒏𝒊𝒕𝒐𝒓𝒂𝒎𝒆𝒏𝒕𝒐 𝒅𝒆 𝑷𝒓𝒆𝒄̧𝒐𝒔V2 - 𝑰𝑷𝑯𝑶𝑵𝑬 16-𝒆

import requests
import pandas as pd
from bs4 import BeautifulSoup
import time
import streamlit as st
import plotly.express as px  

Loja1 = Loja2 = Loja3 = Loja4 = Loja5 = ''
VPreço1 = VPreço2 = VPreço3 = VPreço4 = VPreço5 = ''
Preços = [VPreço1, VPreço2, VPreço3, VPreço4, VPreço5]

def Preço1():
    global Loja1, VPreço1
    Loja1 = 'AMAZON'
    
    url1 = 'https://www.amazon.com.br/Smartphone-Samsung-Galaxy-C%C3%A2mera-Recursos/dp/B0DYVMWMNM/ref=asc_df_B0DYVMWMNM?mcid=fb95d6a7da5c368ebb4a0ff4e9bc6cd5&tag=googleshopp00-20&linkCode=df0&hvadid=709964503151&hvpos=&hvnetw=g&hvrand=2347465545261026696&hvpone=&hvptwo=&hvqmt=&hvdev=c&hvdvcmdl=&hvlocint=&hvlocphy=9100965&hvtargid=pla-2448309485204&language=pt_BR&gad_source=1&th=1'

    response = requests.get(url1)
    soup = BeautifulSoup(response.text,'html.parser')
    todo_texto = soup.get_text()
    
    if "R$" in todo_texto:
        posiçao = todo_texto.find("R$")
        VPreço1 = todo_texto[posiçao:posiçao+10]
    else:
        VPreço1 = "Preço não encontrado"
        print("Preço nao encontrado")

def Preço2():
    global Loja2, VPreço2
    Loja2 = 'ZOOM'
    
    url2 = 'https://www.zoom.com.br/celular/smartphone-apple-iphone-16-128gb-camera-dupla?og=18000&gad_source=1&gad_campaignid=23017617316&gbraid=0AAAAADlBCe7GxkVylcqwGHu_zt-b8-wSx&gclid=CjwKCAjwx-zHBhBhEiwA7Kjq62g8ksFm9JZ_9ekChWNm9h62e-hLOiJYczVESlT1N_AotrYxnCGhvhoCCiYQAvD_BwE'
    response = requests.get(url2)
    soup = BeautifulSoup(response.text, 'html.parser')
    todo_texto = soup.get_text()
    
    if "R$" in todo_texto:
        posiçao = todo_texto.find("R$")
        VPreço2 = todo_texto[posiçao:posiçao+11]

    else:
        VPreço2 = "Preço não encontrado"
        print("nao encontrado")

def Preço3():
    global Loja3, VPreço3
    Loja3 = 'CARREFOUR'
    
    url3 = 'https://www.carrefour.com.br/apple-iphone-16e-de-128gb-tecnologia-5g-mp951194184/p?utm_medium=sem&utm_source=google_pmax_3p&utm_campaign=3p_performancemax_Eletro_Apostas3p&gad_source=1&gad_campaignid=21012471034&gbraid=0AAAAADjinolo-4cHBQ6uYWmNV1FXT0Fbw&gclid=CjwKCAjwx-zHBhBhEiwA7Kjq6-Scf8LxSgV2hk0V_yAg4iRtgjk56k6jO-aRCEeP1umG-QV1pT_-lBoC4LIQAvD_BwE'
    response = requests.get(url3)
    soup = BeautifulSoup(response.text, 'html.parser')
    texto_todo = soup.get_text()
    if "R$" in texto_todo:
        posiçao = texto_todo.find("R$")
        VPreço3 = texto_todo[posiçao:posiçao+11]
    else:
        VPreço3 = "Preço não encontrado"
        print("Nao encontrado")

def Preço4():
    global Loja4, VPreço4
    Loja4 = 'BUSCAPE'
    url4 = 'https://www.buscape.com.br/offer?oid=1453934288&sortorder=-1&pagesize=-1&feed_only_mkp=true&pla=2025-10-24T21:49:48.309213508&og=19221&gad_source=1&gad_campaignid=22735399328&gbraid=0AAAAAD-OhXbNIICmsFATvsM8l5fMFxmmt&gclid=CjwKCAjwx-zHBhBhEiwA7Kjq6weYg4wVRYotcFdpE38qrqdFJEhZt_G95-TiFZWpeqSFPjqfzZUGUBoCuh4QAvD_BwE'
    response = requests.get(url4)
    soup = BeautifulSoup(response.text, 'html.parser')
    todo_texto = soup.get_text()
    
    if "R$" in todo_texto:
        Find = todo_texto.find("R$")
        VPreço4 = todo_texto[Find:Find+11]

    else:
        VPreço4 = "Preço não encontrado"
        print("Not Found")

def Preço5():
    global Loja5, VPreço5
    Loja5 = 'LIVELO' 
    
    url5 = 'https://www.livelo.com.br/shopping/apple-iphone-16e-de-128gb-branco/produto/PRD3987447?skuId=SKU4946730&gad_source=1&gad_campaignid=21895551570&gbraid=0AAAAAC73hNXP_C4xkmZ3Q7K0kIxfhMznb&gclid=CjwKCAjwx-zHBhBhEiwA7Kjq6_wTulX_zEl-37kF5FEx9qEV0IXeKr1ZYDqmsybDLHQtIcS2dcy9fRoCVc8QAvD_BwE'
    response = requests.get(url5)
    soup = BeautifulSoup(response.text, 'html.parser')
    texto_todo = soup.get_text()
    
    if "R$" in texto_todo:
        posiçao = texto_todo.find("R$")
        VPreço5 = texto_todo[posiçao:posiçao+11]

    else:
        VPreço5 = "Preço não encontrado"
Preço1()
Preço2()
Preço3()
Preço4()
Preço5()

def converter_preco(preco_texto):
    try:
        preco_limpo = preco_texto.replace('R$', '').replace('.', '').replace(',', '.').strip()
        partes = preco_limpo.split()
        if partes:
            return float(partes[0])
        return 0.0
    except:
        return 0.0
precos_float = [
    converter_preco(VPreço1) if VPreço1 != "Preço não encontrado" else 0.0,
    converter_preco(VPreço2) if VPreço2 != "Preço não encontrado" else 0.0,
    converter_preco(VPreço3) if VPreço3 != "Preço não encontrado" else 0.0,
    converter_preco(VPreço4) if VPreço4 != "Preço não encontrado" else 0.0,
    converter_preco(VPreço5) if VPreço5 != "Preço não encontrado" else 0.0
]

st.set_page_config(
    page_title='Preços Iphone em Lojas Diferentes',
    page_icon='📱',
    layout='centered',
    initial_sidebar_state='expanded'
)

st.title("Preços Iphone")
st.header("Um simples Grafico De Preços")
st.text("Uma tabela mostrando os preços de um item de 5 lojas ")
dados_originais = {
    'Nome': ['AMAZON', 'ZOOM', 'CARREFOUR', 'BUSCAPE', 'LIVELO'],
    'Preços': [VPreço1, VPreço2, VPreço3, VPreço4, VPreço5]
}
df_original = pd.DataFrame(dados_originais)
st.dataframe(df_original)

dados_grafico = {
    'Nome': ['AMAZON', 'ZOOM', 'CARREFOUR', 'BUSCAPE', 'LIVELO'],
    'Preços': precos_float
}
df_grafico = pd.DataFrame(dados_grafico)

fig = px.bar(df_grafico, x='Nome', y='Preços', 
             title='Preços do Iphone 16e em Diferentes Lojas',
             color='Preços',
             color_continuous_scale='blues'
)
Maior = max(df_grafico['Preços'])
Menor = min(df_grafico['Preços'])
st.text(f'Maior valor: {Maior}')
st.text(f'Menor valor: {Menor}')

st.plotly_chart(fig)

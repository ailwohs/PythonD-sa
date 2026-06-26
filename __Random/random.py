
#calculando a cotação do dolar com streamlit e requests
import streamlit as st
import requests
def converter_dolar_para_real(valor_em_dolar):
    url = "https://api.bcb.gov.br/dados/serie/bcdata.sgs.1/dados/ultimos/1?formato=json"
    response = requests.get(url)
    data = response.json()
    cotacao_dolar = float(data[0]['valor'])
    valor_em_real = valor_em_dolar * cotacao_dolar
    return valor_em_real, cotacao_dolar
st.title("Conversor de Dólar para Real 💵")
valor_em_dolar = st.number_input("Digite o valor em dólares:", min_value=0.0, step=0.01)
if st.button("Converter"):
    valor_em_real, cotacao_dolar = converter_dolar_para_real(valor_em_dolar)
    st.write(f"A cotação atual do dólar é: R$ {cotacao_dolar:.2f}")
    st.write(f"O valor em reais é: R$ {valor_em_real:.2f}")

    #mudando o icon do streamlit para o do dolar
    st.set_page_config(page_title="Conversor de Dólar para Real", page_icon="💵")


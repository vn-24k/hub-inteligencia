import requests
import json
from datetime import datetime
import pytz

def buscar_clima(lat, lon):
    # API pública que não exige chave de acesso
    url = f"https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lon}&current_weather=true"
    try:
        resposta = requests.get(url).json()
        return resposta['current_weather']['temperature']
    except:
        return "--"

def gerar_sincronizacao():
    # 1. Calculando os Fusos Horários Exatos
    fuso_br = pytz.timezone('America/Sao_Paulo')
    fuso_th = pytz.timezone('Asia/Bangkok')
    
    hora_br = datetime.now(fuso_br).strftime('%H:%M')
    hora_th = datetime.now(fuso_th).strftime('%H:%M')
    
    # 2. Buscando a Temperatura (São Paulo e Bangkok)
    temp_br = buscar_clima(-23.55, -46.63)
    temp_th = buscar_clima(13.75, 100.50)
    
    # 3. A Mensagem do Dia
    mensagem_pt = "O sistema está online e conectado."
    mensagem_th = "ระบบออนไลน์และเชื่อมต่อแล้ว" # Tradução exata
    
    # 4. Estruturando os Dados Complexos
    dados = {
        "brasil": {
            "cidade": "São Paulo, BR",
            "horario": hora_br,
            "temperatura": f"{temp_br}°C"
        },
        "tailandia": {
            "cidade": "Bangkok, TH",
            "horario": hora_th,
            "temperatura": f"{temp_th}°C"
        },
        "comunicacao": {
            "pt": mensagem_pt,
            "th": mensagem_th
        },
        "ultima_atualizacao": datetime.now(fuso_br).strftime('%d/%m/%Y - %H:%M')
    }
    
    # 5. Salvando o arquivo com suporte a caracteres especiais (para o Tailandês)
    with open("dados_ia.json", "w", encoding='utf-8') as f:
        json.dump(dados, f, indent=4, ensure_ascii=False)
    
    print("Sincronização Intercontinental Concluída!")

if __name__ == "__main__":
    gerar_sincronizacao()


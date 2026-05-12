import requests, json, datetime

def buscar_telemetria():
    api_url = "https://api.open-meteo.com/v1/forecast"
    params_sp = {"latitude": -23.55, "longitude": -46.63, "current_weather": True}
    params_th = {"latitude": 13.75, "longitude": 100.50, "current_weather": True}

    try:
        temp_sp = requests.get(api_url, params=params_sp).json()['current_weather']['temperature']
        temp_th = requests.get(api_url, params=params_th).json()['current_weather']['temperature']
    except:
        temp_sp, temp_th = "--", "--"

    dados = {
        "brasil": {
            "cidade": "São Paulo, BR",
            "timeZone": "America/Sao_Paulo",
            "temperatura": f"{temp_sp}°C"
        },
        "tailandia": {
            "cidade": "Bangkok, TH",
            "timeZone": "Asia/Bangkok",
            "temperatura": f"{temp_th}°C"
        },
        "mensagem": {
            "pt": "Sistemas Sincronizados",
            "th": "ระบบออนไลน์และเชื่อมต่อแล้ว"
        }
    }

    with open("dados_ia.json", "w", encoding='utf-8') as f:
        json.dump(dados, f, indent=4, ensure_ascii=False)
    print("Dados de telemetria atualizados!")

if __name__ == "__main__":
    buscar_telemetria()



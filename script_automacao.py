import requests, json, datetime

def buscar_telemetria():
    url = "https://api.open-meteo.com/v1/forecast"
    # Coordenadas: SP (-23.55, -46.63) | Bangkok (13.75, 100.50)
    p_sp = {"latitude": -23.55, "longitude": -46.63, "current_weather": True}
    p_th = {"latitude": 13.75, "longitude": 100.50, "current_weather": True}

    try:
        t_sp = requests.get(url, params=p_sp).json()['current_weather']['temperature']
        t_th = requests.get(url, params=p_th).json()['current_weather']['temperature']
    except:
        t_sp, t_th = "--", "--"

    dados = {
        "brasil": {
            "nome": "Vinícius Silva",
            "timeZone": "America/Sao_Paulo",
            "temp": f"{t_sp}°C"
        },
        "tailandia": {
            "nome": "Tawan Kannika",
            "timeZone": "Asia/Bangkok",
            "temp": f"{t_th}°C"
        },
        "status": "Sincronização Ativa"
    }

    with open("dados_ia.json", "w", encoding='utf-8') as f:
        json.dump(dados, f, indent=4, ensure_ascii=False)
    print("Telemetria concluída com sucesso!")

if __name__ == "__main__":
    buscar_telemetria()

import os
from flask import Flask
import requests
import threading
import time

app = Flask(__name__)

USERNAME = 'loboofc123'
PASSWORD = '1144818722'

def ligar_aternos():
    print("A iniciar ligação com o painel do Aternos...")
    session = requests.Session()
    
    session.headers.update({
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
        'Accept-Language': 'pt-BR,pt;q=0.9,en-US;q=0.8,en;q=0.7',
        'Origin': 'https://aternos.org',
        'Referer': 'https://aternos.org/'
    })

    try:
        session.get('https://aternos.org/')
        time.sleep(1)
        
        session.get('https://aternos.org/go/')
        time.sleep(1)
        
        login_res = session.post('https://aternos.org/panel/ajax/account/login.php', data={
            'username': USERNAME,
            'password': PASSWORD
        })
        print(f"Estado do Login: {login_res.status_code}")

        session.get('https://aternos.org/panel/ajax/servers.php')
        time.sleep(1)

        start_res = session.get('https://aternos.org/panel/ajax/start.php')
        print(f"Resposta do comando Ligar: {start_res.status_code}")
        print("Comando disparado com sucesso para o Aternos!")

    except Exception as e:
        print(f"Erro crítico na execução: {e}")

@app.route('/')
def home():
    return "Bot Aternos online e a funcionar!"

if __name__ == '__main__':
    # Dispara o comando para ligar o Aternos em segundo plano
    threading.Thread(target=ligar_aternos).start()
    
    # Sobe o servidor Flask na porta que o Render exige de graça
    port = int(os.environ.get('PORT', 10000))
    app.run(host='0.0.0.0', port=port)

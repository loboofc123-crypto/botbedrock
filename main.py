import requests
import time

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
        # Passo 1: Obter cookies iniciais de segurança
        session.get('https://aternos.org/')
        time.sleep(1)
        
        session.get('https://aternos.org/go/')
        time.sleep(1)
        
        # Passo 2: Efetuar o login
        login_res = session.post('https://aternos.org/panel/ajax/account/login.php', data={
            'username': USERNAME,
            'password': PASSWORD
        })
        print(f"Estado do Login: {login_res.status_code}")

        # Passo 3: Aceder à página de servidores para carregar o token de sessão
        session.get('https://aternos.org/panel/ajax/servers.php')
        time.sleep(1)

        # Passo 4: Disparar o comando para ligar o servidor
        start_res = session.get('https://aternos.org/panel/ajax/start.php')
        print(f"Resposta do comando Ligar: {start_res.status_code}")
        print("Comando disparado com sucesso para o Aternos!")

    except Exception as e:
        print(f"Erro crítico na execução: {e}")

if __name__ == '__main__':
    ligar_aternos()
    # Mantém o Render acordado para não gerar erro de saída antecipada
    while True:
        time.sleep(3600)

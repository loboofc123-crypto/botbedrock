from python_aternos import Client

USERNAME = 'loboofc123'
PASSWORD = '1144818722'

def iniciar_bot():
    print("Iniciando conexão com a API do Aternos...")
    try:
        aternos = Client.from_credentials(USERNAME, PASSWORD)
        
        # Acede diretamente ao primeiro servidor associado à conta
        servidor = aternos.user.servers[0]
        print(f"Servidor localizado: {servidor.domain}")

        servidor.fetch()
        print(f"Estado atual: {servidor.status}")

        if servidor.status == 'offline':
            print("O servidor está offline. A enviar comando para ligar...")
            servidor.start()
            print("Comando enviado com sucesso!")
        elif servidor.status == 'queue':
            print("O servidor já está na fila de espera.")
        else:
            print(f"O servidor encontra-se no estado: {servidor.status}")

    except Exception as e:
        print(f"Ocorreu um erro ao interagir com o Aternos: {e}")

if __name__ == '__main__':
    iniciar_bot()

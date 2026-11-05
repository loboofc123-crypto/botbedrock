from python_aternos import Client

# Insira seus dados reais do Aternos
USERNAME = 'loboofc123'
PASSWORD = '1144818722'
SERVER_ADDRESS = 'loboofc123.aternos.me'

def iniciar_bot():
    print("Iniciando conexão com o Aternos...")
    try:
        aternos = Client.from_credentials(USERNAME, PASSWORD)
        servidores = aternos.list_servers()

        if not servidores:
            print("Nenhum servidor encontrado na conta.")
            return

        # Tenta encontrar o servidor pelo endereço ou pega o primeiro da lista
        servidor = None
        for s in servidores:
            if SERVER_ADDRESS in s.address:
                servidor = s
                break
        
        if not servidor:
            servidor = servidores[0]

        print(f"Servidor selecionado: {servidor.address}")

        # Atualiza o estado
        servidor.fetch()
        status = servidor.status
        print(f"Status atual: {status}")

        if status == 'offline':
            print("Servidor desligado! Enviando comando de inicialização...")
            servidor.start()
            print("Comando enviado com sucesso!")
        elif status == 'queue':
            print("O servidor já está na fila de espera.")
        else:
            print(f"O servidor está no estado: {status}")

    except Exception as e:
        print(f"Erro ao interagir com o Aternos: {e}")

if __name__ == '__main__':
    iniciar_bot()

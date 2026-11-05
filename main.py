from python_aternos import Client

# Coloque seus dados reais do Aternos entre as aspas
USERNAME = 'loboofc123'
PASSWORD = '1144818722'

def iniciar_bot():
    print("Iniciando conexão com o Aternos...")
    try:
        aternos = Client.from_credentials(USERNAME, PASSWORD)
        servidores = aternos.list_servers()

        if not servidores:
            print("Nenhum servidor encontrado.")
            return

        servidor = servidores[0]
        print(f"Monitorando servidor: {servidor.address}")

        # Atualiza os dados do servidor
        servidor.fetch()
        status = servidor.status
        print(f"Status atual do servidor: {status}")

        if status == 'offline':
            print("Servidor desligado! Enviando comando para ligar...")
            servidor.start()
            print("Comando de ligar enviado com sucesso!")
        elif status == 'queue':
            print("O servidor está na fila do Aternos.")
        else:
            print("O servidor já está online ou a ligar.")

    except Exception as e:
        print(f"Erro ao gerenciar o servidor: {e}")

if __name__ == '__main__':
    iniciar_bot()

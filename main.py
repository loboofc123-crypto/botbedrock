from python_aternos import Client, AtWs

# Insira seus dados reais do Aternos
USERNAME = 'loboofc123'
PASSWORD = '1144818722'

def iniciar_bot():
    print("Conectando à conta Aternos...")
    try:
        aternos = Client.from_credentials(USERNAME, PASSWORD)
        servidores = aternos.list_servers()

        if not servidores:
            print("Nenhum servidor encontrado na conta.")
            return

        # Pega o primeiro servidor disponível na conta
        servidor = servidores[0]
        print(f"Servidor encontrado: {servidor.domain}")

        # Força a atualização e envia o start
        servidor.fetch()
        print(f"Status atual: {servidor.status}")

        if servidor.status != 'online' and servidor.status != 'queue':
            print("Enviando comando para ligar o servidor...")
            servidor.start()
            print("Comando de inicialização enviado com sucesso!")
        else:
            print(f"O servidor já está no estado: {servidor.status}")

    except Exception as e:
        print(f"Erro ao conectar ou ligar o servidor: {e}")

if __name__ == '__main__':
    iniciar_bot()

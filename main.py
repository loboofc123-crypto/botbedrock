import time
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

        while True:
            try:
                servidor.fetch()
                status = servidor.status
                print(f"[{time.strftime('%H:%M:%S')}] Status atual: {status}")

                if status == 'offline':
                    print("Servidor desligado! Enviando comando para ligar...")
                    servidor.start()
                elif status == 'queue':
                    print("Na fila do Aternos...")

            except Exception as e:
                print(f"Erro na checagem: {e}")

            # Espera 60 segundos antes de checar de novo
            time.sleep(60)

    except Exception as e:
        print(f"Erro ao autenticar: {e}")

if __name__ == '__main__':
    iniciar_bot()
import requests

NOME_DO_SEU_CANAL = "minha_obrigacoes_Carlos_Guaxe"

def enviar_notificacao(mensagem):
    url = f"https://ntfy.sh/{NOME_DO_SEU_CANAL}"
    try:
        response = requests.post(
            url,
            data=mensagem.encode('utf-8'),
            headers={"Title": "Alerta de Tarefa!"}
        )
        print(f"Status do envio: {response.status_code}")
    except Exception as e:
        print(f"Erro: {e}")

if __name__ == "__main__":
    enviar_notificacao("Teste Ntfy: O robô na nuvem está funcionando!")

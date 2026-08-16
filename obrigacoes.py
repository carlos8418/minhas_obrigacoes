import datetime
import requests

NOME_DO_SEU_CANAL = "minha_obrigacoes_Carlos_Guaxe"

def enviar_notificacao(mensagem):
    url = f"https://ntfy.sh/{NOME_DO_SEU_CANAL}"
    try:
        requests.post(
            url,
            data=mensagem.encode('utf-8'),
            headers={"Title": "Alerta de Tarefa!"}
        )
    except Exception as e:
        print(f"Erro: {e}")

def verificar_obrigacoes():
    hoje = datetime.date.today()
    dia_semana = hoje.weekday()  # 0=Segunda, 1=Terça, 2=Quarta, 3=Quinta, 4=Sexta, 5=Sábado, 6=Domingo

    # --- TESTE PARA HOJE ---
    if dia_semana == 5:
        enviar_notificacao("Teste Ntfy: O robô na nuvem está funcionando!")

    # --- SUAS OBRIGAÇÕES SEMANAIS ---
    elif dia_semana == 0:
        enviar_notificacao("Hoje é dia de: Verificar diário de obras")
    
    elif dia_semana == 3:
        enviar_notificacao("Hoje é dia de: Preencher planilhas de terceiros")

if __name__ == "__main__":
    verificar_obrigacoes()

    # --- SUAS OBRIGAÇÕES SEMANAIS ---
    if dia_semana == 0:
        enviar_notificacao("Hoje é dia de: Verificar diário de obras")
    
    elif dia_semana == 3:
        enviar_notificacao("Hoje é dia de: Preencher planilhas de terceiros")

if __name__ == "__main__":
    verificar_obrigacoes()

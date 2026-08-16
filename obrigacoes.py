import datetime
import requests
import zoneinfo

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
    # Obtém a data exata no fuso horário do Brasil (São Paulo)
    fuso_br = zoneinfo.ZoneInfo("America/Sao_Paulo")
    hoje = datetime.datetime.now(fuso_br).date()
    dia_semana = hoje.weekday()  # 0=Segunda, 1=Terça, 2=Quarta, 3=Quinta, 4=Sexta, 5=Sábado, 6=Domingo

    # --- SUAS OBRIGAÇÕES SEMANAIS ---
    if dia_semana == 0:
        enviar_notificacao("Hoje é dia de: Verificar diário de obras")
    
    elif dia_semana == 3:
        enviar_notificacao("Hoje é dia de: Preencher planilhas de terceiros")

if __name__ == "__main__":
    verificar_obrigacoes()

name: Disparar Alerta Ntfy

on:
  schedule:
    # Executa todos os dias às 11:00 UTC (08:00 no horário de Brasília)
    - cron: '0 11 * * *'
  workflow_dispatch:

jobs:
  run-script:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      - name: Configurar Python
        uses: actions/setup-python@v4
        with:
          python-version: '3.x'
      - name: Instalar bibliotecas
        run: pip install requests
      - name: Executar script
        run: python obrigacoes.py

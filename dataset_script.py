import csv
import random
from datetime import datetime, timedelta

# Parâmetros simulados
chaves = ['CPF', 'Celular', 'Email', 'Aleatória']
dispositivos = ['Android', 'iOS', 'Windows']
cidades = ['São Paulo - SP', 'Niterói - RJ', 'Recife - PE', 'Salvador - BA', 'Manaus - AM',
           'Curitiba - PR', 'Belo Horizonte - MG', 'Porto Alegre - RS', 'Fortaleza - CE',
           'Campinas - SP', 'Florianópolis - SC', 'Vitória - ES', 'João Pessoa - PB',
           'Teresina - PI', 'Aracaju - SE', 'Uberlândia - MG', 'Campo Grande - MS',
           'Londrina - PR', 'Joinville - SC', 'Santos - SP']

def horario_aleatorio():
    base = datetime(2025, 9, 1)
    delta = timedelta(minutes=random.randint(0, 43200))  # até 30 dias
    return (base + delta).strftime('%Y-%m-%d %H:%M:%S')  # formato datetime padrão

# Configuração
total_linhas = 200
fraude_alvo = int(total_linhas * 0.3)  # 30% de fraudes
fraudes = 0

with open('fraude_pix.csv', mode='w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(['id_transacao', 'valor', 'horario', 'tipo_chave', 'dispositivo', 'localizacao', 'suspeita_fraude', 'fraude_pix'])

    for i in range(1, total_linhas + 1):
        valor = round(random.uniform(10, 5000), 2)
        horario = horario_aleatorio()
        tipo_chave = random.choice(chaves)
        dispositivo = random.choice(dispositivos)
        localizacao = random.choice(cidades)

        # Regras para suspeita
        suspeita = 'Sim' if valor > 1000 or dispositivo == 'Windows' or '23:' in horario or '02:' in horario else 'Não'

        # Definir fraude com base na meta
        if fraudes < fraude_alvo and suspeita == 'Sim' and valor > 500:
            fraude = 'Sim'
            fraudes += 1
        else:
            fraude = 'Não'
            # Ajustar suspeita para coerência se necessário
            if suspeita == 'Sim' and valor > 500:
                suspeita = random.choice(['Sim', 'Não'])

        writer.writerow([i, valor, horario, tipo_chave, dispositivo, localizacao, suspeita, fraude])

import pandas as pd

df = pd.read_csv('fraude_pix.csv')
print(df['fraude_pix'].value_counts())
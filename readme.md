# 📝 Relatório de Experimento AutoML — Detecção de Fraudes PIX

## 📘 Contextualização do Projeto

Este projeto, feito para o bootcamp da DIO, tem como finalidade a aplicação de técnicas de aprendizado de máquina para a detecção de fraudes em transações realizadas via PIX. A proposta envolve a construção de um modelo de classificação binária capaz de prever, com base em atributos transacionais, se uma determinada operação possui características associadas a comportamento fraudulento.

A iniciativa se insere em um cenário de crescente digitalização dos meios de pagamento, onde a agilidade das transações exige mecanismos automatizados de monitoramento e prevenção de fraudes. O uso de modelos preditivos permite antecipar riscos e apoiar decisões operacionais em tempo real.

---

## 🧪 Geração e Estrutura do Dataset

Como não foi utilizado um conjunto de dados real, optou-se pela criação de um **dataset sintético** por meio de um **script Python**, disponível neste repositório. O script foi desenvolvido para simular transações PIX com características variadas, incorporando elementos que poderiam influenciar o risco de fraude.

O arquivo gerado (`fraude_pix.csv`) também está incluído no repositório e contém **200 registros**, com aproximadamente **30% de transações classificadas como fraudulentas**. As variáveis incluídas foram:

- `valor`: valor da transação em reais
- `horario`: data e hora da transação
- `tipo_chave`: tipo de chave PIX utilizada (CPF, telefone, e-mail, aleatória)
- `dispositivo`: sistema operacional do dispositivo (Android, iOS, Windows, etc.)
- `localizacao`: cidade onde a transação foi realizada
- `suspeita_fraude`: variável auxiliar gerada com base em regras simples
- `fraude_pix`: variável alvo indicando se a transação foi fraudulenta

O script utiliza bibliotecas como `pandas`, `numpy`, `random` e `datetime` para gerar os dados com distribuição controlada e lógica simulada de risco. A estrutura do dataset foi pensada para representar cenários plausíveis, como transações em horários incomuns, valores elevados em dispositivos menos seguros e uso de chaves aleatórias.

Apesar da limitação de volume, o conjunto de dados permitiu a execução de um experimento AutoML completo, servindo como base para avaliação de modelos e análise de desempenho preditivo.

---

## 1. Objetivo

O experimento teve como objetivo construir um modelo de classificação binária capaz de identificar transações fraudulentas no sistema PIX, utilizando dados simulados com atributos como valor, horário, tipo de chave, dispositivo e localização.

---

## 2. Descrição do Dataset

- **Total de linhas**: 200
- **Proporção de fraudes**: ~30% (`fraude_pix = "Sim"`)
- **Atributos utilizados**:
  - `valor`: valor da transação
  - `horario`: data e hora da transação
  - `tipo_chave`: tipo de chave PIX usada
  - `dispositivo`: sistema operacional do dispositivo
  - `localizacao`: cidade da transação
  - `suspeita_fraude`: marcação auxiliar
  - `fraude_pix`: rótulo alvo (Sim/Não)

> Observação: o volume reduzido de dados e a baixa variabilidade entre os exemplos limitaram a capacidade de generalização dos modelos.

---

## 3. Configuração do AutoML

- **Plataforma**: Azure Machine Learning Studio
- **Tarefa**: Classificação binária
- **Métrica principal**: AUCWeighted
- **Tempo limite**: 15 minutos
- **Modelos habilitados**: XGBoost, LightGBM, RandomForest, ExtremeRandomTrees
- **Ensemble stacking**: Ativado

---

## 4. Resultados Obtidos

| Modelo             | AUCWeighted | Duração | Observações                              |
| ------------------ | ----------- | ------- | ---------------------------------------- |
| VotingEnsemble     | 0.58872     | 2m 56s  | Melhor resultado, mas abaixo do esperado |
| XGBoostClassifier  | 0.56690     | 28s     | Desempenho próximo ao ensemble           |
| LightGBM           | 0.53911     | 33s     | Resultado fraco                          |
| RandomForest       | ~0.51       | ~30s    | Baixo poder de separação                 |
| LogisticRegression | ~0.45       | ~30s    | Baseline simples, desempenho limitado    |

> Nenhum modelo superou a marca de 0.60 em AUCWeighted, o que indica baixa capacidade de distinguir entre transações legítimas e fraudulentas.

---

## 5. Análise Crítica

Apesar da execução correta do pipeline AutoML, os resultados foram **insatisfatórios** para o objetivo proposto. Os principais fatores que contribuíram para isso foram:

- **Volume insuficiente de dados**: 200 linhas não são suficientes para treinar modelos complexos.
- **Pouca variabilidade entre os exemplos**: padrões de fraude não estavam bem definidos.
- **Tempo de execução limitado**: 15 minutos pode ter interrompido etapas como explicação de modelo e RAI Insights.

---

## 6. Próximos Passos Recomendados

- Gerar um novo dataset com pelo menos **1.000 linhas**, mantendo coerência entre atributos e rótulo.
- Criar **variáveis derivadas** (ex: hora do dia, dia da semana, faixa de valor).
- Executar o AutoML com **tempo estendido** (≥ 45 minutos) e foco em métricas como **Recall** e **F1-score**.
- Testar modelos manualmente com **validação cruzada** e fine tuning.

---

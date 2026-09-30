# 🌳 Algoritmo de Árvore de Decisão (ID3) em Python

Este projeto é uma implementação do zero do algoritmo de aprendizado de máquina **ID3 (Iterative Dichotomiser 3)**, criado para fins de estudo em Inteligência Artificial.

## 🎯 Objetivo
O algoritmo constrói uma Árvore de Decisão capaz de classificar dados categóricos. Ele utiliza cálculos matemáticos de **Entropia** (para medir a incerteza dos dados) e **Ganho de Informação** para decidir qual atributo divide melhor o conjunto de dados a cada etapa.

## 🛠️️ Tecnologias Utilizadas
* **Python 3**
* **Pandas:** Para manipulação e leitura do dataset.
* **NumPy:** Para operações matemáticas otimizadas (logaritmos para cálculo de entropia).
* **OpenPyXL:** Para leitura direta de arquivos `.xlsx`.

## 🚀 Como executar
1. Clone este repositório.
2. Instale as dependências: `pip install pandas numpy openpyxl`
3. Certifique-se de que o arquivo `dataset.xlsx` (contendo os dados de treinamento) está na mesma pasta.
4. Execute o arquivo principal: `python trabalho_id3.py`

## 🧠 Lógica Implementada
O algoritmo funciona de forma recursiva:
1. Avalia a Entropia do conjunto atual.
2. Calcula o Ganho de Informação para cada coluna.
3. Escolhe a coluna com maior ganho para ser o nó da árvore.
4. Divide os dados e repete o processo até que todos os dados de um ramo pertençam à mesma classe (Entropia = 0).
# ==============================================================================
# TRABALHO DE APRENDIZADO DE MÁQUINA - ÁRVORE DE DECISÃO (ID3)
# ==============================================================================


import pandas as pd
import numpy as np
from pprint import pprint

def calcular_entropia(coluna_alvo):
   
    elementos, contagens = np.unique(coluna_alvo, return_counts=True)
    entropia = 0
    
    for i in range(len(elementos)):
        probabilidade = contagens[i] / np.sum(contagens)
        entropia -= probabilidade * np.log2(probabilidade)
        
    return entropia

def calcular_ganho_informacao(dados, nome_atributo, nome_alvo="classe"):
    
    entropia_total = calcular_entropia(dados[nome_alvo])
    
    valores_atributo, contagens = np.unique(dados[nome_atributo], return_counts=True)
    entropia_ponderada = 0
    
    for i in range(len(valores_atributo)):
        subconjunto = dados.where(dados[nome_atributo] == valores_atributo[i]).dropna()
        probabilidade_subconjunto = contagens[i] / np.sum(contagens)
        entropia_ponderada += probabilidade_subconjunto * calcular_entropia(subconjunto[nome_alvo])
        
    ganho_informacao = entropia_total - entropia_ponderada
    return ganho_informacao

def algoritmo_id3(dados, dados_originais, atributos, nome_alvo="classe", classe_pai=None):
   
    if len(np.unique(dados[nome_alvo])) <= 1:
        return np.unique(dados[nome_alvo])[0]
    
    elif len(dados) == 0:
        classes_unicas, contagens = np.unique(dados_originais[nome_alvo], return_counts=True)
        indice_mais_frequente = np.argmax(contagens)
        return classes_unicas[indice_mais_frequente]
    
    elif len(atributos) == 0:
        return classe_pai
    
    else:
        classes_unicas, contagens = np.unique(dados[nome_alvo], return_counts=True)
        classe_pai = classes_unicas[np.argmax(contagens)]
        
        valores_ganho = [calcular_ganho_informacao(dados, atributo, nome_alvo) for atributo in atributos]
        
        indice_melhor_atributo = np.argmax(valores_ganho)
        melhor_atributo = atributos[indice_melhor_atributo]
        
        arvore = {melhor_atributo: {}}
        
        atributos_restantes = [i for i in atributos if i != melhor_atributo]
        
        for valor in np.unique(dados[melhor_atributo]):
            subconjunto = dados.where(dados[melhor_atributo] == valor).dropna()
            
            sub_arvore = algoritmo_id3(subconjunto, dados_originais, atributos_restantes, nome_alvo, classe_pai)
            
            arvore[melhor_atributo][valor] = sub_arvore
            
        return arvore

def prever(instancia, arvore):
   
    for chave in arvore.keys():
        valor = instancia[chave]
        arvore_seguinte = arvore[chave].get(valor)
        
        if isinstance(arvore_seguinte, dict):
            return prever(instancia, arvore_seguinte)
        else:
            return arvore_seguinte

# ==============================================================================
# BLOCO PRINCIPAL (EXECUÇÃO)
# ==============================================================================


if __name__ == "__main__":
    
    caminho_arquivo = 'dataset.xlsx'
    
    try:
        dataset = pd.read_excel(caminho_arquivo)
        print(f"Dataset '{caminho_arquivo}' carregado com sucesso!\n")
        
        print("Amostra dos dados:")
        print(dataset.head(), "\n")
        
        nome_alvo = dataset.columns[-1]
        
        atributos = list(dataset.columns[:-1])
        
        print("Treinando a Árvore de Decisão (ID3)...")
        arvore_gerada = algoritmo_id3(dados=dataset, 
                                      dados_originais=dataset, 
                                      atributos=atributos, 
                                      nome_alvo=nome_alvo)
        
        print("\n=== ÁRVORE DE DECISÃO GERADA ===")
        pprint(arvore_gerada)
        
    except FileNotFoundError:
        print(f"ERRO: O arquivo '{caminho_arquivo}' não foi encontrado.")
        print("Por favor, certifique-se de que o arquivo .xlsx está na mesma pasta do script ou insira o caminho completo.")
    except Exception as e:
        print(f"Ocorreu um erro ao processar os dados: {e}")
#!/usr/bin/env python3
import sys


# função que faz a checagem da repetição no fim da palavra e 
# a reescreve sem o sufixo errado
def checar_duplicacao(palavra): 
  numero_letras = len(palavra)

  if numero_letras == 2: # rotina para palavras de 2 caracteres
    if(palavra[0] == palavra[1]):
      return True, palavra[0] 

  if numero_letras == 3: # rotina para palavras de 3 caracteres
    if(palavra[1] == palavra[2]):
      return True, palavra[:2] 

  tamanho_maximo = 0

  posicao_final = len(palavra) - 1
  if numero_letras > 3: # rotina para palavras com 4 ou mais caracteres

    for letras_sufixo in range(1, posicao_final):
      if letras_sufixo == 1: letras_sufixo = 2

      sufixo = palavra[(posicao_final - letras_sufixo) + 1 : (posicao_final + 1)] 
      if sufixo in palavra[0: (numero_letras - letras_sufixo)]:
        tamanho_maximo = letras_sufixo
    

    return True, palavra[0:(posicao_final-tamanho_maximo)+1]

  
  return False, palavra  # se não houver repetição, retorna false e a palavra
                         # original

#################### Fim da função e início do programa ####################

frase_original = str(input()) # input da string
frase_array = frase_original.split(" ") # transforma string num array
numero_duplicadas = 0 # contador de palavras com duplicação

numero_palavras = len(frase_array) # contador de palavras totais na frase
resposta = "" # variável de saída

for item in frase_array:
  check, palavra = checar_duplicacao(item) # executa a função para cada palavra
  resposta = resposta + " " + palavra      # na frase
  if(check):
    numero_duplicadas = numero_duplicadas + 1 # faz a contagem de palavras com duplicação
  
resposta = resposta + "."

# se o número de palavras com duplicação for igual ao número de palavras totais, 
# retorna a frase totalmente corrigida. Se houver alguma palavra sem duplicação, 
# retorna a frase original com um ponto final
if(numero_duplicadas == numero_palavras): 
  print(resposta.lstrip())
else:
  print(frase_original.strip()+".")


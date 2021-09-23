#!/usr/bin/env python3
import sys

def checar_duplicacao(palavra):
  numero_letras = len(palavra)

  if numero_letras == 2:
    if(palavra[0] == palavra[1]):
      return True, palavra[0] 

  if numero_letras == 3:
    if(palavra[1] == palavra[2]):
      return True, palavra[:2] 

  tamanho_maximo = 0

  posicao_final = len(palavra) - 1
  if numero_letras >= 3:

    for letras_sufixo in range(1, posicao_final):
      if letras_sufixo == 1: letras_sufixo = 2

      sufixo = palavra[(posicao_final - letras_sufixo) + 1 : (posicao_final + 1)] 
      if sufixo in palavra[0: (numero_letras - letras_sufixo)]:
        tamanho_maximo = letras_sufixo
    

    return True, palavra[0:(posicao_final-tamanho_maximo)+1]

  
  return False, palavra  

#################### Fim da função e início do programa ####################

frase_original = str(input())
frase_array = frase_original.split(" ")
numero_duplicadas = 0

numero_palavras = len(frase_array)
resposta = ""

for item in frase_array:
  check, palavra = checar_duplicacao(item)
  resposta = resposta + " " + palavra
  if(check):
    numero_duplicadas = numero_duplicadas + 1
  
resposta = resposta + "."

if(numero_duplicadas == numero_palavras):
  print(resposta.lstrip())
else:
  print(frase_original.strip()+".")


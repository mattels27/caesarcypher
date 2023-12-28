# Cifra de César/Cifra Afim
Este algorítmo escrito em Python codifica e decodifica palavras utilizando o funcionamento da cifra de César.

Um alfabeto de 119 caracteres está disponível para uso.

Além do mais, há um gerador de chaves aleatórias com base no número de letras do alfabeto que o usuário fornecer.

# Como funciona a cifra afim?
Basicamente, vistando os estudos sobre funções, para que uma função admita uma função inversa, a mesma deve ser bijetora. 
Na criptografia, a função polinomial que será a chave deve ser bijetora pois sua inversa será a chave de decodificação. 

# Aritmética modular
Poderíamos deixar somente a função e calcular as letras novas normalmente? Sim, mas isso não permitiria gerar a mensagem codificada, já que poderiamos ter números maiores do que o índice do último caractere do alfabeto utilizado, impossibilitando a escrita da mensagem codificada.

Então fazemos uso de aritmética modular para ter acesso às letras que formam a mensagem codificada.

# Valores permitidos da variável 'a':
2, 3, 4, 5, 6, 8, 9, 10, 11, 12, 13, 15, 16, 18, 19, 20, 22, 23, 24, 25, 26, 27, 29, 30, 31, 32, 33, 36, 37, 38, 39, 40, 41, 43, 44, 45, 46, 47, 48, 50, 52, 53, 54, 55, 57, 58, 59, 60, 61, 62, 64, 65, 66, 67, 69, 71, 72, 73, 74, 75, 76, 78, 79, 80, 81, 82, 83, 86, 87, 88, 89, 90, 92, 93, 94, 95, 96, 97, 99, 100, 101, 103, 104, 106, 107, 108, 109, 110, 111, 113, 114, 115, 116, 117, 118.

# Cifra de César/Cifra Afim
Este algorítmo escrito em Python codifica e decodifica palavras utilizando a cifra de César, mais especificamente no modelo de chave afim.

Um alfabeto de 116 caracteres está disponível para uso. 

# Como funciona a cifra afim?
Basicamente, vistando os estudos sobre funções, para que uma função admita uma função inversa, a mesma deve ser bijetora. 
Na criptografia, a função polinomial que será a chave deve ser bijetora pois sua inversa será a chave de decodificação. 

# Aritmética modular
Poderíamos deixar somente a função e calcular as letras novas normalmente? Sim, mas isso não permitiria ler a mensagem codificada, já que poderiamos ter números maiores do que o índice do último caractere do alfabeto utilizado, impossibilitando a escrita da mensagem codificada.

Então fazemos uso de aritmética modular para ter acesso às letras que formam a mensagem codificada.

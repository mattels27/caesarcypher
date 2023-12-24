from random import *
from math import *
from sympy import mod_inverse

alphabet=['A','Á','À','Â','Ã','B','C','Ç','D','E','É','Ê','F','G','H','I','Í','J','K','L','M','N','O','Õ','Ó','Ô','P',
          'Q','R','S','T','U','Ú','Û','V','W','X','Y','Z','a','á','à','â','ã','b','c','ç','d','e','é','ê','f','g',
          'h','i','í','j','k','l','m','n','o','õ','ó','ô','p','q','r','s','t','u','ú','v','w','x','y','z','1','2','3',
          '4','5','6','7','8','9','0',' ','"','!','@','#','$','%','¨','&','*','(',')','-','_','=','+','[',']','{',
          '}','?',',','.','|','/','<','>',';',':','ª','º','§']
menu=True


while menu:
    print('Caesar Cypher')
    print('1. Criptografar')
    print('2. Descriptografar')
    print('3. Gerador de Chaves')
    print('4. Sair')
    a=input('Digite: ')

    if a==('1'):
        while True:
            var_a= int(input('Escolha sua variável a: '))
            var_b= int(input('Escolha sua variável b (entre 0 e 118): '))

            if gcd(var_a, 119)!= 1:
                print (' Chave inválida.')
                break

            msg_index=[]
            new_msg_=[]
            msg=input('Digite sua mensagem: ')

            for k in msg:
                msg_index.append(alphabet.index(k))

            for j in msg_index:
                x=((var_a*(j+1)+var_b)%119)-1
                new_msg_.append(alphabet[x])

            print(''.join(new_msg_))
            print()
            print('1. Continuar criptografando')
            print('2. Voltar ao menu')
            b=input('Digite: ')

            if b==('1'):
                True
            if b==('2'):
                break
    
    if a==('2'):
        while True:
            var_a= int(input('Escolha sua variável a: '))
            var_b= int(input('Escolha sua variável b (entre 0 e 118): '))

            alt_key_a= mod_inverse(var_a, 119)
            alt_key_b= 119 - int(var_b) * alt_key_a

            msg=input('Digite sua mensagem codificada: ')
            msg_index=[]
            new_msg_=[]
            
            for l in msg:
                msg_index.append(alphabet.index(l))

            
            for i in msg_index:
                x=((alt_key_a *(i+1)+alt_key_b)%119)-1
                new_msg_.append(alphabet[x])

            print(''.join(new_msg_))
            print()
            print('1. Continuar descriptografando')
            print('2. Voltar ao menu')
            c=input('Digite: ')

            if c==('1'):
                True
            if c==('2'):
                break

    if a==('3'):
        while True:
            a= int(input('Quantos caracteres tem seu alfabeto?: '))   
            a_variables=[]

            for k in range(2, a):
               if gcd(k, a)==1:
                    a_variables.append(k)

            print('Os valores de "a" disponíveis são:')
            print()
            print(a_variables)
            print()
            print('1. Gerar mais chaves')
            print('2. Voltar ao menu')
            choice=input('Digite: ')
            if choice==('1'):
                True
            if choice==('2'):
                break
              
    if a==('4'):
        break   

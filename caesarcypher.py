alphabet=['A','Á','À','Â','Ã','B','C','Ç','D','E','É','Ê','F','G','H','I','Í','J','K','L','M','N','O','Ó','Ô','P',
          'Q','R','S','T','U','Ú','Û','V','W','X','Y','Z','a','á','à','â','ã','b','c','ç','d','e','é','ê','f','g',
          'h','i','í','j','k','l','m','n','o','ó','ô','p','q','r','s','t','u','ú','v','w','x','y','z','1','2','3',
          '4','5','6','7','8','9','0',' ','"','!','@','#','$','%','¨','&','*','(',')','-','_','=','+','[',']','{',
          '}','?',',','.','|','/','<','>',';',':','ª','º']
menu=True


while menu:
    print('Caesar Cypher')
    print('1. Criptografar')
    print('2. Descriptografar')
    print('3. Sair')
    a=input('Digite: ')

    if a==('1'):
        while True:
            msg=input('Digite sua mensagem: ')
            msg_index=[]
            new_msg_=[]
            
            for k in msg:
                msg_index.append(alphabet.index(k))

            for j in msg_index:
                x=((9*(j+1)+13)%116)-1
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
            msg=input('Digite sua mensagem codificada: ')
            msg_index=[]
            new_msg_=[]
            
            for l in msg:
                msg_index.append(alphabet.index(l))

            
            for i in msg_index:
                x=((13*(i+1)+1339)%116)-1
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
        break   

        

   
    
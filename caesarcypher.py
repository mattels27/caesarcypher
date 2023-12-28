from math import *
import random
from sympy import mod_inverse
import tkinter as tk

#Eu sei que o tkinter é uma desgraça, mas deixa quieto.
#O alfabeto fica ao gosto do dev. Eu fiz o meu com os 118 caracteres disponíveis no alfabeto + o espaço.
#Não incluí o 'U' com trema. Se tentar criptografar palavras em alemão, não vai dar certo (não é o único impeditivo aliás).



alphabet=['A','Á','À','Â','Ã','B','C','Ç','D','E','É','Ê','F','G','H','I','Í','J','K','L','M','N','O','Õ','Ó','Ô','P',
          'Q','R','S','T','U','Ú','Û','V','W','X','Y','Z','a','á','à','â','ã','b','c','ç','d','e','é','ê','f','g',
          'h','i','í','j','k','l','m','n','o','õ','ó','ô','p','q','r','s','t','u','ú','v','w','x','y','z','1','2','3',
          '4','5','6','7','8','9','0',' ','"','!','@','#','$','%','¨','&','*','(',')','-','_','=','+','[',']','{',
          '}','?',',','.','|','/','<','>',';',':','ª','º','§']

#Aqui, o algorítmo de cifragem do texto fornecido pelo usuário.

def encrypting_algorithm(text, variable_a, variable_b):

    #'line_length' fica ao critério de quem for editar. esse é o valor limite para o programa quebrar o texto.
     
    new_msg=''
    current_line_length= 0
    line_length= 20

    #Tira o MDC da variável escolhida pelo user e o tamanho do alfabeto.
    #gdc = Greatest Common Divisor.

    if gcd(variable_a, len(alphabet))!= 1:
        return 'Chave Inválida. Precisa ser coprimo de 119.'
    
    #Vai obter a indexação ds letras, já cifradas.

    for letter in text:
        if letter == ' ':
            new_msg += ' '
            current_line_length += 1
        else:
            new_index = ((variable_a*(alphabet.index(letter) + 1) + variable_b) % len(alphabet)) - 1
            new_msg += alphabet[new_index]
            current_line_length += 1
        if current_line_length == line_length:
            new_msg += '\n'
            current_line_length = 0
    
    return new_msg

#O processo de decifragem de uma mensagem.

def decrypting_algorithm(text, variable_a, variable_b):
    #Nada de novo por aqui, o processo é o mesmo só que ao contrário.
    new_msg=''
    current_line_length= 0
    line_length= 20

    if gcd(variable_a, len(alphabet))!= 1:
        return 'Chave Inválida. Precisa ser coprimo de 119.'
    
    for letter in text:
        if letter == ' ':
            new_msg += ' '
            current_line_length += 1
        else:
            alt_key_a= mod_inverse(variable_a, len(alphabet))
            alt_key_b= (len(alphabet) - int(variable_b)) * alt_key_a
            new_index = ((alt_key_a*(alphabet.index(letter) + 1) + alt_key_b) % len(alphabet)) - 1
            new_msg += alphabet[new_index]
            current_line_length += 1
        if current_line_length == line_length:
            new_msg += '\n'
            current_line_length = 0
    
    return new_msg

#Não precisava, mas fiz um gerador de chaves baseado no tamanho do alfabeto que o usuário fornece.

def key_generate_algorithm(alphabet_length):
    a_variables=[]

    for k in range(2, alphabet_length):
        if gcd(k, alphabet_length) == 1:
            a_variables.append(k)
            
    def random_a_key_choose(a_variables):
        return random.choice(a_variables)
            
    def random_b_key_choose(alphabet_length):
        return random.randint(1, alphabet_length)

    a_key= random_a_key_choose(a_variables)
    b_key= random_b_key_choose(alphabet_length)

    return f'{a_key}x + {b_key}'
    
#Pra cada um dos procedimentos, tem uma função que faz o tratamento dos dados fornecidos no programa.

def encrypting_process():
    #Esse procedimento trata a mensagem e as variáveis que o user deu. Se ele passar
    #qualquer coisa que não for um número, o programa pede para fornecer um valor válido.

    try:
        message = entry.get()
        variable_a = int(shift_a_entry.get())
        variable_b = int(shift_b_entry.get())
    except ValueError:
        result_text.delete(1.0, tk.END)
        result_text.insert(tk.END, "Erro: Valor inválido, por favor insira um valor válido.")
        return
    
    encrypted_text = encrypting_algorithm(message, variable_a, variable_b)
    result_text.delete(1.0, tk.END)  #Limpa o que tiver na caixa. Para colocar a nova info que o programa der.
    result_text.insert(tk.END, encrypted_text)

    
def decrypting_process():
    #Mesma ação do processo anterior.

    try:
        message = entry.get()
        variable_a = int(shift_a_entry.get())
        variable_b = int(shift_b_entry.get())
    except ValueError:
        result_text.delete(1.0, tk.END)
        result_text.insert(tk.END, "Erro: Valor inválido, por favor insira um valor válido.")
        return
    
    decrypted_text = decrypting_algorithm(message, variable_a, variable_b)
    result_text.delete(1.0, tk.END)  #Mesma coisa.
    result_text.insert(tk.END, decrypted_text)


def key_generate_process():
    #Mesma coisa...

    try:
        len_alphabet = int(entry_alphabet_length.get())
    except ValueError:
        key_text.delete(1.0, tk.END)
        key_text.insert(tk.END, "Erro: Valor inválido.")
        return
    
    generated_key= key_generate_algorithm(len_alphabet)
    key_text.delete(1.0, tk.END) #Mesma coisa.
    key_text.insert(tk.END, generated_key)

#Resumidamente, 'root' é a janela, com 'title' sendo o nome na barra; 'Label' são os textinhos como "Insira seu texto"; 
#'Entry' é a caixa onde inserimos a info pedida; 'Button' são os botões em que iremos chamar o processo.
#'mainloop' é o que vai manter a janela aberta.

root = tk.Tk()
root.title("Codificador César")

label = tk.Label(root, text="Insira seu texto:")
label.grid(row=0, column=0,padx=10, pady=10)

label_key_generate = tk.Label(root, text="Insira o número de caracteres do seu alfabeto.")
label_key_generate.grid(row=0, column=5, padx=10, pady=10)

entry = tk.Entry(root, width=80)
entry.grid(row=2, column=0, padx=10, pady=10)

entry_alphabet_length = tk.Entry(root, width=80)
entry_alphabet_length.grid(row=2, column=5, padx=10, pady=10)

shift_label_a = tk.Label(root, text="Insira a variável 'a':")
shift_label_a.grid(row=4, column=0, padx=0,pady=0)

shift_label_b = tk.Label(root, text="Insira a variável 'b':")
shift_label_b.grid(row=6, column=0, padx=0,pady=0)

shift_a_entry = tk.Entry(root, width=5)
shift_a_entry.grid(row=4, column=1, padx=0,pady=0)

shift_b_entry = tk.Entry(root, width=5)
shift_b_entry.grid(row=6, column=1, padx=0,pady=0)

encrypt_button = tk.Button(root, text="Criptografar", command=encrypting_process)
encrypt_button.grid(row=8, column=0, padx=10,pady=10)

decrypt_button = tk.Button(root, text="Descriptografar", command=decrypting_process)
decrypt_button.grid(row=9, column=0, columnspan=1, pady=10)

random_key_generate_button= tk.Button(root, text="Gerar chave aleatória", command=key_generate_process)
random_key_generate_button.grid(row=3, column=5, columnspan=1, pady=10)

result_label = tk.Label(root, text="Texto cifrado:")
result_label.grid(row=10, column=0, padx=10, pady=10)

result_text = tk.Text(root, height=40, width=80)
result_text.grid(row=14, column=0, padx=10, pady=10)

result_key_label = tk.Label(root, text="Sua chave aleatória é:")
result_key_label.grid(row=4, column=5, padx=10, pady=10)

key_text = tk.Text(root, height=1, width=21)
key_text.grid(row=5, column=5, padx=10, pady=10)

root.mainloop()

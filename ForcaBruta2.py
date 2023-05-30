import string
import hashlib
import time

caracteres=string.ascii_letters+string.digits

def autenticar(senha):
    global user,total
    with open('usuarios.txt','r') as arquivo:
        usuarios=arquivo.readlines()
        total = len(usuarios)
        for linha in usuarios:
            usuario_info=linha.split(';')
            if senha == usuario_info[1].replace('\n',"").strip():
                user=usuario_info[0]
                return True

start_time=time.time()
count=0
for a in caracteres:
    for b in caracteres:
        for c in caracteres:
            for d in caracteres:
                senha= a+b+c+d
                senha_md5=hashlib.md5(senha.encode()).hexdigest()
                if autenticar(senha_md5)==True:
                    count+=1
                    print(f'{user} senha: {senha}')
                    elapsed_time=time.time()-start_time
                    print(elapsed_time)
                if count==total:
                    break
            if count==total:
                break            
        if count==total:
            break
    if count==total:
        break
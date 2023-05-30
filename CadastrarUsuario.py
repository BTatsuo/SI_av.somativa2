import hashlib

def cadastrar_usuario(nome, senha):
    # Realiza o hash da senha utilizando o algoritmo MD5
    senha_hash = hashlib.md5(senha.encode()).hexdigest()

    # Verifica se o arquivo de usuários já existe
    try:
        with open('usuarios.txt', 'r') as arquivo:
            usuarios = arquivo.readlines()
    except FileNotFoundError:
        usuarios = []

    # Verifica se o usuário já está cadastrado
    for usuario in usuarios:
        usuario_info = usuario.split(';')
        if usuario_info[0] == nome:
            print('Usuário já cadastrado.')
            return

    # Adiciona o novo usuário à lista
    novo_usuario = f'{nome};{senha_hash}\n'
    usuarios.append(novo_usuario)

    # Salva a lista de usuários no arquivo
    with open('usuarios.txt', 'w') as arquivo:
        arquivo.writelines(usuarios)

    print('Usuário cadastrado com sucesso.')

def autenticar_usuario(nome, senha):
    # Realiza o hash da senha fornecida para comparação
    senha_hash = hashlib.md5(senha.encode()).hexdigest()

    # Verifica se o arquivo de usuários existe
    try:
        with open('usuarios.txt', 'r') as arquivo:
            usuarios = arquivo.readlines()
    except FileNotFoundError:
        print('Nenhum usuário cadastrado.')
        return

    # Verifica se as credenciais estão corretas
    for usuario in usuarios:
        usuario_info = usuario.split(';')
        if usuario_info[0] == nome:
            if usuario_info[1].strip() == senha_hash:
                print('Usuário autenticado com sucesso.')
            else:
                print('Senha incorreta.')
            return

    print('Usuário não encontrado.')

# Usuarios
cadastrar_usuario('Thales', 'aaaa')
cadastrar_usuario('Tiago', 'aaab')
cadastrar_usuario('Gabriel', 'aaac')
cadastrar_usuario('Brunno', 'aaad')
cadastrar_usuario('GOIT', 'aaae')


autenticar_usuario('Thales', 'T123')
autenticar_usuario('Tiago', 'TT12')
autenticar_usuario('Gabriel', 'B18O')
autenticar_usuario('Brunno', 'BT82')
autenticar_usuario('GOIT', 'G01T')

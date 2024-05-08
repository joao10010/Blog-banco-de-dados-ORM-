from conexao_orm import Base, engine, session
from User import User
from Post import Post

# Cria as tabelas
Base.metadata.create_all(engine) 

# Funcao para exibir o menu de op;oes

def show_menu():
    print('Menu de Opçoes: ')
    print('1 - Adicionar Usuario')
    print('2 - Adicionar Post')
    print('3. consultar usuarios e seus posts')
    print('4. sair')

# funcao para adicionar usuario
def add_user():
    print('adicionar novo usuario')
    name = input('nome: ')
    email = input('Email: ')
    user = User(name, email)
    session.add(user) # para adionar  usuario. substitu toda aquela query para adicionar 
    session.commit()
    print('usuario adicionado com sucesso!')

# funcao para adicionar novo post
def add_post():
    print('adicionar novo post')
    title = input('titulo: ')
    content = input('conteudo: ')
    author_id = int(input('id do autor: ')) 
    user = session.query(User).filter_by(id=author_id).first()# filtanmdo o id do audor com o id da postagem
    if user:
        post = Post(title, content, user)
        session.add(post)
        session.commit()
        print('post adicionado com sucesso!')
    else:
        print('usuario nao encontrado')
        
# funcao para consultar usuarios e post
def query_users_posts():
    users = session.query(User).join(User.posts).order_by(User.name.all())
    for user in users:
        print(f'User: {user.name}, Email: {user.email}')
        for post in user.posts:
            print(f'post:{post.title}, Content: {post.content}')


   
generos = ["Ficção Científica", "Aventura", "Ação"]
class Produto:
    def __init__(self, imposto, valor_de_compra, valor_de_venda, descricao):
        self.imposto = imposto
        self.valor_de_compra = valor_de_compra
        self.valor_de_venda = valor_de_venda
        self.descricao = descricao

class Imposto:
    def __init__(self, categoria, valor):
        self.categoria = categoria
        self.valor = valor
def calcular_imposto(categoria, valor_de_compra, valor_de_venda):
    if categoria == "Livro - " + generos[0]:
        return 0.1*(valor_de_venda - valor_de_compra)
    else:
        return 0.15 * (valor_de_venda - valor_de_compra)


class Livro(Produto):
    def __init__(self, imposto, valor_de_compra, valor_de_venda, descricao, titulo, edicao, editora):
        super().__init__(imposto, valor_de_compra, valor_de_venda, descricao)
        self.titulo = titulo
        self.edicao = edicao
        self.editora = editora

class Titulo:
    def __init__(self, autor, nome_livro, genero):
        self.autor = autor
        self.nome_livro = nome_livro
        self.genero = genero

class Pessoa:
    def __init__(self, nome, email):
        self.nome = nome
        self.email = email

class Autor(Pessoa):
    def __init__(self, nome, email, titulos_publicados):
        super().__init__(nome, email)
        self.titulos_publicados = titulos_publicados
    def publicar_titulo(self, nome_livro, genero):
        titulo = Titulo(self, nome_livro, genero)
        self.titulos_publicados.append(titulo)

class Cliente(Pessoa):
    def __init__(self, nome, email, lista_de_compras):
        super().__init__(nome, email)
        self.lista_de_compras = lista_de_compras
    def realizar_compra(self, lista_de_produtos, lista_quantidades):
        valor_total = 0
        lista_produtos_adquiridos = []
        for i in range(len(lista_de_produtos)):
            lista_produtos_adquiridos.append(ProdutoAdquirido(lista_de_produtos[i], lista_quantidades[i]))
        for produto in lista_de_produtos:
            valor_total += produto.valor_de_venda
        compra = Compra(lista_produtos_adquiridos, self, valor_total)
        self.lista_de_compras.append(compra)

class Compra:
    def __init__(self, lista_de_produtos, cliente, valor_total):
        self.lista_de_produtos = lista_de_produtos
        self.cliente = cliente
        self.valor_total = valor_total
    def imprimir_lista(self):
        for item in self.lista_de_produtos:
            print(f'{item.produto.descricao}  ({item.quantidade}) -  {item.produto.valor_de_venda*item.quantidade}')

class ProdutoAdquirido:
    def __init__(self, produto, quantidade):
        self.produto = produto
        self.quantidade = quantidade


class DBLivros:
    def __init__(self, lista_livros):
        self.lista_livros = lista_livros
    def inserir(self, nome_livro, nome_autor, genero, edicao, editora, valor_de_compra, valor_de_venda):
        autor = DBAutores([]).consultar(nome_autor)
        if not autor:
            autor = Autor(nome_autor, "", [])
        titulo = DBTitulos([]).consultar(nome_livro)
        if not titulo: #checar pra ver se preciso criar titulo
            titulo = Titulo(autor, nome_livro, genero)
        autor.titulos_publicados.append(titulo)
        categoria = "Livro - " + genero
        imposto = Imposto(categoria,calcular_imposto(categoria, valor_de_compra, valor_de_venda))
        livro = Livro(imposto, valor_de_compra, valor_de_venda, nome_livro, titulo, edicao, editora)
        self.lista_livros.append(livro)
    def atualizar(self, nome_livro, edicao, editora, novo_valor_compra, novo_valor_venda):
        for livro in self.lista_livros:
            if livro.descricao == nome_livro and edicao == livro.edicao and editora == livro.editora:
                livro.valor_de_compra = novo_valor_compra
                livro.valor_de_venda = novo_valor_venda
                livro.imposto.valor = livro.imposto.calcular_valor(livro.imposto.categoria, novo_valor_compra, novo_valor_venda)
                continue
    def deletar(self, nome_livro, edicao, editora):
        for livro in self.lista_livros:
            if livro.descricao == nome_livro and edicao== livro.edicao and editora == livro.editora:
                self.lista_livros.remove(livro)
                continue
    def consultar(self, nome_autor):
        lista = []
        for livro in self.lista_livros:
            if livro.titulo.autor.nome == nome_autor:
                lista.append(livro.descricao)
        return lista
    def consultar_livro(self, nome_livro, edicao, editora):
        for livro in self.lista_livros:
            if livro.descricao == nome_livro and edicao== livro.edicao and editora == livro.editora:
                return livro

class DBClientes:
    def __init__(self, lista_clientes):
        self.lista_clientes = lista_clientes
    def inserir(self, nome_cliente, email):
        lista_de_compras = []
        cliente = Cliente(nome_cliente, email, lista_de_compras)
        self.lista_clientes.append(cliente)
    def atualizar(self, nome_cliente, novo_email):
        for cliente in self.lista_clientes:
            if cliente.nome == nome_cliente:
                cliente.email = novo_email
                continue
    def deletar(self, nome_cliente):
        for cliente in self.lista_clientes:
            if cliente.nome == nome_cliente:
                self.lista_clientes.remove(cliente)
    def consultar(self, nome_cliente):
        for cliente in self.lista_clientes:
            if cliente.nome == nome_cliente:
                return cliente
        return False

class DBCompras:
    def __init__(self, lista_compras):
        self.lista_compras = lista_compras
    def inserir(self, compra):
        self.lista_compras.append(compra)
    def atualizar(self, compra):
        pass
    def deletar(self, compra):
        self.lista_compras.remove(compra)
    def consultar(self, nome_cliente):
        for compra in self.lista_compras:
            if compra.cliente.nome == nome_cliente:
                return compra

class DBAutores:
    def __init__(self, lista_autores):
        self.lista_autores = lista_autores
    def inserir(self, nome_autor, email, titulos_publicados):
        autor = Autor(nome_autor, email, titulos_publicados)
        self.lista_autores.append(autor)
    def atualizar(self, nome_autor, novo_email):
        for autor in self.lista_autores:
            if autor.nome == nome_autor:
                autor.email = novo_email
                continue
    def deletar(self, nome_autor):
        for autor in self.lista_autores:
            if autor.nome == nome_autor:
                self.lista_autores.remove(autor)
    def consultar(self, nome_autor):
        for autor in self.lista_autores:
            if autor.nome == nome_autor:
                return autor
        return False

class DBTitulos:
    def __init__(self, lista_titulos):
        self.lista_titulos = lista_titulos
    def inserir(self, nome_autor, nome_livro, genero):
        titulo = Titulo("", nome_livro, genero)
        autor = DBAutores([]).consultar(nome_autor)
        if not autor:
            autor = Autor(nome_autor, "", [titulo])
        titulo.autor = autor
        self.lista_titulos.append(titulo)
    def deletar(self, titulo):
        self.lista_titulos.remove(titulo)
    def consultar(self, nome_livro):
        for titulo in self.lista_titulos:
            if titulo.nome_livro == nome_livro:
                return titulo
        return False
import implementation
DB_livros = implementation.DBLivros([])
DB_titulos = implementation.DBTitulos([])
DB_compras = implementation.DBCompras([])
DB_autores = implementation.DBAutores([])
DB_clientes = implementation.DBClientes([])

DB_autores.inserir("Rick Riordan", "rick@gmail.com", []) #cadastro de autor
DB_titulos.inserir("Rick Riordan", "Percy Jackson", implementation.generos[1]) #cadastro de título
DB_livros.inserir("Percy Jackson", "Rick Riordan", implementation.generos[1], 3, "Intrinseca", 15, 30) #cadastro de livro
DB_livros.inserir("Percy Jackson", "Rick Riordan", implementation.generos[1], 4, "Intrinseca", 20, 35) #cadastro de livro
DB_livros.inserir("O nome do Vento", "Patrick Rothfuss", implementation.generos[1], 4, "Arqueiro", 20, 40) #cadastro de livro, título e autor
DB_livros.inserir("O temor do Sábio", "Patrick Rothfuss", implementation.generos[1], 3, "Arqueiro", 20, 40) # cadastro de livro
DB_autores.atualizar("Patrick Rothfuss", "patrick_rtfs@gmail.com") #atualização de autor
DB_livros.inserir("A música do silêncio", "Patrick Rothfuss", implementation.generos[1], 2, "Arqueiro", 15, 25) #cadastro de livro
DB_livros.inserir("A crônica dos Kane", "Rick Riordan",implementation.generos[1],1, "Intrinseca", 15, 30) #cadastro de livro
DB_clientes.inserir("Luis Zuin", "luiszuinruiz@gmail.com") #cadastro de cliente
DB_clientes.inserir("Ana Laura Souza", "anasouza@gmail.com") #cadastro de cliente
DB_clientes.consultar("Luis Zuin").realizar_compra([DB_livros.consultar_livro("Percy Jackson", 4, "Intrinseca"), DB_livros.consultar_livro("O nome do Vento", 4, "Arqueiro")], [1, 1]) #realizo compra
print(DB_livros.consultar("Patrick Rothfuss")) #consulto livros por autor
print(DB_livros.consultar("Rick Riordan")) #consulto livros por autor
print(DB_clientes.consultar("Luis Zuin").lista_de_compras[0].valor_total) #consulta ao valor total de compra
DB_clientes.consultar("Luis Zuin").lista_de_compras[0].imprimir_lista() #imprimir pedido

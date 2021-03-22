"""
Metodos Magicos

Metodos que utilizam dunder

dunder init -> __init__

Dunder > Double Undersocre


    def __repr__(self):  # Retorna a representacao do objeto
        return f'{self.titulo}, escrito por {self.autor}'

    def __str__(self):{
        return self.titulo
 """


class Livro:

    def __init__(self, titulo, autor, paginas):
        self.titulo = titulo
        self.autor = autor
        self.paginas = paginas

    def __str__(self):
        return self.titulo


livro1 = Livro('Livro 1', 'Autor 1', 400)
livro2 = Livro('Livro 2', 'Autor 2', 600)

print(livro1)

class Livro:
    def __init__ (self, titulo, autor):
        self.titulo = titulo
        self.autor = autor
    
    def detalhes(self):
        print(f"Título......: {self.titulo}\nAutor.......: {self.autor}")
        

livro = Livro("As Crônicas de Nárnia", "C. S. Lewis")

livro.detalhes()
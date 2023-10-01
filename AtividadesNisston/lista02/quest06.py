class Produto:
    def __init__ (self, nome, preco, quantidade):
        self.nome = nome
        self.preco = preco
        self.quantidade = quantidade
    
    def calcular_total(self):
        valor_total = self.preco * self.quantidade
        return f"Produto......: {self.nome}\nQuantidade...: {self.quantidade}\nValor total..: R${valor_total:.2f}"


prod1 = Produto("Lápis", 1.5, 7)

print(prod1.calcular_total())
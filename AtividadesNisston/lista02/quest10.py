class Funcionario:
    def __init__ (self, nome, salario, cargo):
        self.nome = nome
        self.salario = salario
        self.cargo = cargo   
    def aumentar_salario(self, percentual):
        self.salario = self.salario + (self.salario * (percentual/100))
        return self.salario


func1 = Funcionario("Seu Cebola", 5000, "Contador")
print(func1.salario)

func1.aumentar_salario(20)
print(func1.salario)
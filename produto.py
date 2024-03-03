class produto:
    def __init__(self, nome, preco, estoque):
        self.nome = nome
        self.preco = preco
        self.estoque = int(estoque)
    def informacoes(self):
        print(f"Produto: {self.nome}")
        print(f"Preço: {self.preco}")
        print(f"Quantidade em estoque: {self.estoque}")
    
    def vender(self, quantidade):
        if self.estoque >= quantidade:
            self.estoque -= quantidade
            print(f"{quantidade} unidades de {self.nome} foram vendidas.")
        else:
            print("produto em falta!")

class pImportado(produto):
    def __init__(self, nome, preco, PaisOrigem, estoque):
        super().__init__(nome, preco, estoque)
        self.PaisOrigem = PaisOrigem
   
    def informacoes(self):
        super().informacoes()
        print(f"Pais de Origem: {self.PaisOrigem}")
        
p = produto("Notebook", 2500.0, 10)
p.informacoes()
p.vender(3)

pI = pImportado("Chá", 20.0, "China", 50)
pI.informacoes()
pI.vender(3)
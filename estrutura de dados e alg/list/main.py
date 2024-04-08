class NO():
    def __init__(self, data):
        self.data = data
        self.next = None
        
class Lista():
    def __init__(self):
       self.ini = None
       
       
    def append(self,element):

        if self.ini == None:
            self.ini = NO(element)
            
           
        else:
            atual = self.ini
           
            while atual.next != None:
                atual = atual.next

            atual.next = NO(element)

    def update(self,element,novo):
        if self.ini is None:
            print("Lista vazia!")
            return

        if self.ini.data == element:
            self.ini = novo
            return
        else:
            atual = self.ini
            while atual is not None and atual.data != element:
                atual = atual.next
            
            if atual.data == element:
                atual.data = novo
                return
        
        print("elemento não encontradao!")

    def delet(self, element):
        if self.ini is None:
            print("Lista vazia!")
            return

        if self.ini.data == element:
            self.ini = self.ini.next
            return
        else:
            atual = self.ini
            anterior = None
            while atual is not None and atual.data != element:
                anterior = atual
                atual = atual.next
            
            if atual is not None and atual.data == element:
                anterior.next = atual.next
                atual = None
                return
        
        print("Elemento não encontrado!")

                    
        
    def imprime(self):
        atual = self.ini
        while atual is not None:
            print(atual.data)
            print("\n")
            atual = atual.next


            

titulos = (
    "Dom Quixote", "O Senhor dos Anéis", "O Pequeno Príncipe", "Harry Potter e a Pedra Filosofal",
    "Cem Anos de Solidão", "1984", "Orgulho e Preconceito", "Crime e Castigo", "A Montanha Mágica",
    "O Conde de Monte Cristo", "A Metamorfose", "A Divina Comédia", "O Alquimista", "A Revolução dos Bichos",
    "O Apanhador no Campo de Centeio", "O Nome da Rosa", "O Hobbit", "Lolita", "O Código Da Vinci",
    "As Crônicas de Nárnia", "Os Miseráveis", "Guerra e Paz", "Ensaio Sobre a Cegueira", "O Estrangeiro",
    "O Lobo da Estepe", "O Retrato de Dorian Gray", "Os Irmãos Karamazov", "Memórias Póstumas de Brás Cubas",
    "O Grande Gatsby", "A Insustentável Leveza do Ser", "A Menina que Roubava Livros", "A Redoma de Vidro",
    "O Velho e o Mar", "O Morro dos Ventos Uivantes", "A Sangue Frio", "A Estrada", "O Cemitério",
    "O Homem Invisível", "Duna", "O Iluminado", "O Médico e o Monstro", "O Prisioneiro de Zenda",
    "O Poderoso Chefão", "A Guerra dos Tronos", "As Vinhas da Ira", "A Cor Púrpura", "O Sol é para Todos",
    "Moby Dick", "O Velho Homem e o Mar", "A Máquina do Tempo", "O Senhor das Moscas", "A Casa dos Espíritos",
    "O Conto da Aia", "Os Pilares da Terra", "O Sol Também se Levanta", "A Peste", "A Náusea",
    "A Longa Viagem a Um Pequeno Planeta Hostil", "Neuromancer", "O Pintassilgo", "O Amor nos Tempos do Cólera",
    "O Apanhador no Campo de Centeio", "O Mestre e Margarida", "A Revolta de Atlas", "1984", "Fahrenheit 451",
    "Admirável Mundo Novo", "O Estrangeiro", "O Processo", "A Revolução dos Bichos", "O Velho e o Mar",
    "A Metamorfose", "Cem Anos de Solidão", "O Retrato de Dorian Gray", "O Lobo da Estepe", "O Médico e o Monstro",
    "O Grande Gatsby", "Crime e Castigo", "Os Miseráveis", "Dom Quixote", "A Divina Comédia", "O Hobbit",
    "A Sangue Frio", "O Nome da Rosa", "O Apanhador no Campo de Centeio", "Guerra e Paz", "Ensaio Sobre a Cegueira",
    "O Alquimista", "A Insustentável Leveza do Ser", "A Menina que Roubava Livros", "O Código Da Vinci", "Duna",
    "O Prisioneiro de Zenda", "O Conto da Aia", "O Sol é para Todos", "O Senhor dos Anéis", "O Pequeno Príncipe",
    "1984", "O Poderoso Chefão", "As Crônicas de Nárnia", "O Sol Também se Levanta", "A Máquina do Tempo",
    "O Velho Homem e o Mar", "O Amor nos Tempos do Cólera", "A Guerra dos Tronos", "O Processo", "Fahrenheit 451",
    "A Náusea", "A Revolta de Atlas"
)


lista = Lista()

lista.append("ana")
lista.append("fabricio")
lista.append("ana")


lista.imprime()

lista.delet("fabricio")
lista.imprime()
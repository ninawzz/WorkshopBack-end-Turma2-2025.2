class animal:
    def init(self,idade,nome):
        self.nome = nome
        self.idade = idade
    def falar(self):
        return 'Som generico de animal'
    def apresentar(self):
        return f'Olá meu nome é {self.nome} e tenho {self.idade} anos !'

class gato(animal):
    def init(self, idade, nome):
        super().init(idade,nome)

    def falar(self):
        return 'miau'

class cachorro(animal):
    def init(self, idade, nome):
        super().init(idade, nome)

    def falar(self):
        return 'auau'

class zoologico():
    def init(self):
        self.animais = []

    def adicionar_animal(self,animal):
        self.animais.append(animal)

    def listar_animais(self):
        resultado = []
        for a in self.animais:
           resultado.append(f'{a.apresentar()} - {a.falar()}')

        return '\n'.join(resultado)

    def filtrar_por_tipo(self,tipo):
         return [animal.nome for animal in self.animais if isinstance(animal, tipo)]

zoo = zoologico()
gato1 = gato(2,'mingau')
gato2 = gato( 20,'mariana')
cachorro1 = cachorro(17,'caua')

zoo.adicionar_animal(gato1)
zoo.adicionar_animal(gato2)
zoo.adicionar_animal(cachorro1)
print(zoo.listar_animais())
print(zoo.filtrar_por_tipo(gato))
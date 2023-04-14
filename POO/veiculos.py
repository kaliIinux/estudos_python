class Veiuculo():
    def __init__(self, ) -> None:
        self.nivel_tanque = 0
    
    def abastecer(self, litros):
        self.nivel_tanque = litros
    
    def verificar_ar_condicionado(self):
        return "NÃO POSSUO AR CONDICIONADO"
        
class Carro(Veiuculo):
    def __init__(self, ) -> None:
        super().__init__() # super() invoca a classe Veiculo que seria a classe principal
                            #posso utilizat Veiculo().__init__ também
    def verificar_ar_condicionado(self):
        return "EU TENHO AR CONDICIONADO" 
    

class Moto(Veiuculo):
    def __init__(self) -> None:
        super().__init__() 
                            
                            
if __name__ == "__main__":
    palio = Carro()
    cg160 = Moto()
    palio.abastecer(20)
    cg160.abastecer(10)
    print(palio.nivel_tanque)
    print(cg160.nivel_tanque)
    print("CG160: ", cg160.verificar_ar_condicionado())
    print("Palio: ", palio.verificar_ar_condicionado())
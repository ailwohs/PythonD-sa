'''def apresentacao (nome,idade):
    print("nome", nome, "idade", idade)
apresentacao(20, "Julia")'''

def meu_decorador(func):
    def wrapper():
        print("Antes da função ser chamada.")
        func()
        print("Depois da função ser chamada.")
    return wrapper
@meu_decorador
def saudacao():
    print("Olá, mundo!")
saudacao()  

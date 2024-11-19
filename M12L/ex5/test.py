'''Crie uma classe de Test com o método main. Neste método:
a. Crie um assistente administrativo e um técnico. Imprima os dados de cada um
deles.
b. Crie um animal do tipo cachorro e faça-o latir. Crie um gato e faça-o miar. Faça
os dois animais caminharem. Acrescente em cada classe um método que
retorne de forma sobreposta o que cada animal come.
c. Crie um ingresso. Peça para o usuário digitar 1 para normal e 2 para VIP.
Conforme a escolha do usuário, diga se o ingresso é do tipo normal ou VIP. Se
for VIP, peça para ele digitar 1 para camarote superior e 2 para camarote
inferior. Conforme a escolha do usuário, diga se que o VIP é camarote superior
ou inferior. Imprima o valor do ingresso.
d. Crie um imóvel. Peça para o usuário digitar 1 para novo e 2 para velho.
Conforme a definição do usuário, imprima o valor final do imóvel de maneira
sobreposta.'''
from assistenteAdministrativo import AssistenteAdministrativo
from tecnico import Tecnico
from cachorro import Cachorro
from gato import Gato
from ingresso import Ingresso
from imovel import Imovel

def main():
    # a. Criar assistente administrativo e técnico
    assistente = AssistenteAdministrativo("Maria", 30)
    tecnico = Tecnico("José", 25)
    print(assistente)
    print(tecnico)

    print()
    # b. Criar animais
    cachorro = Cachorro()
    gato = Gato()
    print(cachorro.emitir_som())
    print(gato.emitir_som())
    print()

    print(cachorro.caminhar())
    print(gato.caminhar())
    print()

    print(cachorro.comer())
    print(gato.comer())

    print()

    # c. Criar ingresso
    tipo_ingresso = int(input("Digite 1 para ingresso normal ou 2 para VIP: "))
    ingresso = Ingresso(tipo_ingresso)
    print(f'O ingresso é do tipo: {ingresso.tipo_ingresso()} e custa R${ingresso.valor()}')
    if tipo_ingresso == 2:
        camarote = int(input("Digite 1 para camarote superior ou 2 para camarote inferior: "))
        if camarote == 1:
            print("VIP - Camarote Superior")
        elif camarote == 2:
            print("VIP - Camarote Inferior")

    # d. Criar imóvel
    estado_imovel = int(input("\nDigite 1 para imóvel novo ou 2 para imóvel velho: "))
    imovel = Imovel(estado_imovel)
    print(f'\nO valor do imóvel é R${imovel.valor()}')

if __name__ == "__main__":
    main()
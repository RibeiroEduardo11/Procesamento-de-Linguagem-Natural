class Aluno:
    def __init__(self,nome,n1,n2,n3,media):
        self.nome = nome
        self.n1 = n1
        self.n2 = n2
        self.n3 = n3
        self.media = media

alunos = []
while True:
    nome = input("Digite o nome do aluno: ")
    n1 =int(input("Digite a primeira nota: "))
    n2 =int(input("Digite a segunda nota: "))
    n3 =int(input("Digite a terceira nota: "))

    media = n1+n2+n3/3

    aluno = Aluno(nome,n1,n2,n3,media)


    alunos.append(aluno)



    saida = input("Digite sair para sair e continuar para continuar: ")

    if saida == "sair":
        for i in range(len(alunos)):
            print(f"Nome: {alunos[i].nome}, Média: {alunos[i].media}")
            if media >= 7:
                print("Aprovado")
            else:
                print("Reprovado")
        break


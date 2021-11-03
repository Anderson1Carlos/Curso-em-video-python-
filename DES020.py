# O mesmo professor do desafio anterior quer sortear a ordem de apresentação de trabalhos dos alunos. Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada.
import random
al1 = input('Aluno (a): ')
al2 = input('Aluno (a): ')
al3 = input('Aluno (a): ')
al4 = input('Aluno (a): ')
alunos = [al1,al4,al3,al2]
random.shuffle(alunos)
print(f'{alunos}')
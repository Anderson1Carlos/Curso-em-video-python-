# Crie um programa que leia o nome de uma cidade e diga se ela começa ou não com o nome 'SANTO'.
city = input('Em qual cidade você mora? ').upper().strip()
print(f'{"SANTO" in city[:5]}') # Ou ''SANTO'' == city[:5]

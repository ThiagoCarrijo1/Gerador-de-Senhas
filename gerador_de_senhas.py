from random import choice
import string

def gera_senha(quantidade_caracteres = 25):
    # Define os caracteres permitidos para a senha, incluindo letras, dígitos e algumas pontuações
    caracteres_aleatorio = string.ascii_letters + string.digits + '!@#$%^&*'

    # Gera a senha aleatoriamente, escolhendo caracteres da lista caracteres_aleatorios
    senha = ''.join(choice(caracteres_aleatorio) for _ in range(quantidade_caracteres))

    # Retorna a senha gerada
    return senha

def main():
    # Solicita ao usuário que pressione Enter para gerar a senha
    input('Pressione Enter para gerar sua senha')

    # Gera a senha usando a função gerar_senha
    senha_gerada = gera_senha()

    # Exibe a senha gerada para o usuário
    print(f'Sua senha gerada aleatoriamente é: {senha_gerada}')

if __name__ == '__main__': # Chame a função principal se o script estiver sendo executado diretamente
    main()

input() # Espera um input do usuário para não fechar
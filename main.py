# Program......: EFF Dice-Generated Passphrases
# Author.......: Renato Andalik (renato@andalik.com.br)
# Version......: 1.0.0 (22/04/2021)
# Description..: Implementação via software do conceito de geração de frase-senha
#                proposto pela EFF em https://www.eff.org/dice

import random
passphrase = []

reset_color = "\033[0m"
red = "\033[1;31;10m"
green = "\033[1;32;10m"
yellow = "\033[1;33;10m"
blue = "\033[1;34;10m"
magenta = "\033[1;35;10m"
cyan = "\033[1;36;10m"

# banner
print("{0}EFF Dice-Generated Passphrases{1}".format(blue, reset_color))
print("{0}https://www.eff.org/dice\n{1}".format(blue, reset_color))

# popular variavel wordlist com conteudo do arquivo de texto 
file = open("wordlist/eff_large_wordlist.txt", "r")
wordlist = file.read().splitlines()
file.close()

# corra Forrest, corra!!!
print("Sorteando palavras...")
# sortear 6 palavras
for prize in range(6):
    # rolar dado 5 vezes para compor numero de 5 digitos
    num = ""
    for roll_dice in range(5):
        num = num + str(random.randint(1,6))

    # obter palavra correspondente ao numero sorteado
    for word in wordlist:
        if(num in word):
            print("> palavra {0}: {1} = {2}".format(str(prize+1), num, word[6:]))
            passphrase.append(word[6:])

passphrase_str = ' '.join(passphrase)

chars = len(passphrase_str)
print("")
print("-" * chars)
print("Passphrase (totalizando {0} caracteres):".format(str(chars)))
print("{0}{1}{2}".format(yellow, passphrase_str, reset_color))
print("-" * chars)

print("\nEsta senha é uma das 221.073.919.720.733.357.899.776 (ou 2⁷⁷) alternativas que poderiam ter sido escolhidas por este método.")

# rodape
# emoji unicode tables (https://apps.timwhitlock.info/emoji/tables/unicode)
print("{0}\nCriado com {1} e {2} na Andalik Industries{3}".format(blue, u"\U00002764", u"\U00002615", reset_color))
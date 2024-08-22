import random

def jogo_da_forca():
    palavras = ["aids", "facao", "aureo", "chimia", "caroço"]
    palavra_secreta = random.choice(palavras)
    palavra_revelada = ["_"] * len(palavra_secreta)
    tentativas_restantes = 6
    letras_erradas = []

    print("Bem-vindo ao jogo da forca!")
    print("Adivinhe a palavra em até 6 tentativas.")

    while True:
        print("\nPalavra: " + " ".join(palavra_revelada))
        print("Tentativas restantes: " + str(tentativas_restantes))
        print("Letras erradas: " + ", ".join(letras_erradas))

        palpite = input("Digite uma letra: ").lower()

        if len(palpite) != 1:
            print("Por favor, digite apenas uma letra.")
            continue

        if palpite in letras_erradas or palpite in palavra_revelada:
            print("Você já tentou essa letra antes. Parece burro.")
            continue

        if palpite in palavra_secreta:
            for i in range(len(palavra_secreta)):
                if palavra_secreta[i] == palpite:
                    palavra_revelada[i] = palpite
        else:
            letras_erradas.append(palpite)
            tentativas_restantes -= 1

        if "_" not in palavra_revelada:
            print("\nParabéns! Você acertou a palavra " + "".join(palavra_revelada))
            break

        if tentativas_restantes == 0:
            print("\nVocê perdeu! A palavra era: " + palavra_secreta)
            break

jogo_da_forca()
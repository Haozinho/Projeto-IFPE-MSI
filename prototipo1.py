print("BATALHA NAVAL IFPE - CAMPUS PAULISTA \n")
print("=====  EQUIPE  ====== \n")
print("Pedro Hao Tavares")
print("Gleiciane Bezerra")
print("Vinicius Felipe\n\n\n")


def ver_tiro(palpite):

    ok = "n"
    while ok == "n":
        try:
            tiro = input("Adicione suas coordenadas: ")
            tiro = int(tiro)
            if tiro < 0 or tiro > 99:
                print("Digite uma coordenada valida, tente novamente.")
            elif tiro in palpite:
                print("Digite uma coordenada valida, tente novamente depois.")
            else:
                ok = "y"
                break
        except:
            print("Valor incorreto, por favor jogue novamente")

    return tiro


def batalha(acerto, erro, completo):
    print("BATALHA NAVAL VIOLENCIA PURA")
    print("     0  1  2  3  4  5  6  7  8  9")

    local = 0
    for x in range(10):
        linha = ""
        for y in range(10):
            area = " ▢ "
            if local in erro:
                area = " ❖ "
            elif local in acerto:
                area = " ✦ "
            elif local in completo:
                area = " * "

            linha = linha + area
            local = local + 1
        print(x, " ", linha)


def verificar_tiro(tiro, barco1, barco2, acerto, erro, completo):

    if tiro in barco1:
        barco1.remove(tiro)
        if len(barco1) > 0:
            acerto.append(tiro)
        else:
            completo.append(tiro)
    elif tiro in barco2:
        barco2.remove(tiro)
        if len(barco2) > 0:
            acerto.append(tiro)
        else:
            completo.append(tiro)
    else:
        erro.append(tiro)

    return barco1, barco2, acerto, erro, completo


barco1 = [45, 46, 47]
barco2 = [6, 16, 26]

acerto = []
erro = []
completo = []

for i in range(10):
    palpite = acerto + erro + completo
    tiro = ver_tiro(palpite)
    barco1, barco2, acerto, erro, completo = verificar_tiro(
        tiro, barco1, barco2, acerto, erro, completo)
    batalha(acerto, erro, completo)

    if len(barco1) < 1 and len(barco2) < 1:
        print("Você venceu !")
        break
print("Fim de jogo.")

def inicializar():
    tab = []
    for i in range(3):
        linha = []
        for j in range(3):
            linha.append(".")
        tab.append(linha)
    retunr tab

def main():
    jogo = inicializar()
    print(jogo)

if __name__=="__main__":
    main()

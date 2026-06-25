boletim = []
while True:
    print('menu')
    print('1. adicionar nota')
    print('2. ver media')
    print('3. sair')

    opcao = int(input('escolha uma opcao'))

    if opcao == 3:
        print('saindo...')
        break
    elif opcao == 1:
        nota = float(input('digite a nota: '))
        if nota < 0 or nota > 10:
            print('nota invalida')
        else:
            boletim.append(nota)
            print('nota adicionada')
    elif opcao == 2:
        print('calculando media')
        if len(boletim) == 0:
            print('nenhuma nota cadastrada')
        else :
            media = sum(boletim) / len(boletim)
            print(f'media: {media:.2f}')
            if media >= 7:
                print('aprovado')
            else:
                print('reprovado')
    else:
        print('opcao invalida')
from os import argv

nomeFicheiro = None

def filtrarLixo(delta, step, dist):
    if dist >= step:
        print('dist maior')
        return 0
    if delta < dist:
        print('delta maior')
        return 0
    return 1


def veiculoPontoInicial(veiculo, x, y):
    return abs(veiculo[0]-x) + abs(veiculo[1] - y)

def imprimeEmFicheiro(carros):
    with open(nomeFicheiro + '.out', 'w') as fout:
        for carro in carros:
            #Carro n tem biagem alocada
            if carro[2] == False:
                continue

            fout.write(str(len(carro[3])) + ' ')
            for indiceDaViagemAlocada in range(len(carro[3])):
                if indiceDaViagemAlocada == (len(carro[3]) - 1):
                    fout.write(str(carro[3][indiceDaViagemAlocada]))
                else:
                    fout.write(str(carro[3][indiceDaViagemAlocada]) + ' ')
            #if i != (len(carros) - 1):
            fout.write('\n')

def main():
    with open(nomeFicheiro) as file:
        ficheiro = file.readlines()
        rows, columns, vehicles, rides, bonus, steps = tuple(map(int, ficheiro[0].split()))

        viagem = []
        for trip in range(1, len(ficheiro)):
            viagem.append(list(map(int, ficheiro[trip].split())))

        #Prioridades
        #Bonus
        #distancia

        #distancias
        distancias = []
        for trip in viagem:
            distancias.append(abs(trip[2] - trip[0]) + abs(trip[3] - trip[1]))

        #deltas
        deltas = []
        for trip in viagem:
            deltas.append(trip[-1] - trip[-2])

        fleet = [[0,0, False, [], 0] for y in range(vehicles)]

        #filtrar viagens
        for i in range(len(viagem)):
            print('Viagem ' + str(i))
            if filtrarLixo(deltas[i], steps, distancias[i]) == 0:
                print('lixo')
                viagem[i] = 0

        viagensOcupadas = []
        if vehicles >= rides:
            print('AINDA NAO FIX')
            return
        else:
            for car in fleet:
                if car[2] == True:
                    continue
                for viagem_index in range(len(viagem)):
                    if type(viagem[viagem_index]) is int:
                        continue
                    if viagem_index in viagensOcupadas:
                        continue
                    
                    if (distancias[viagem_index] + veiculoPontoInicial(car, viagem[viagem_index][0],viagem[viagem_index][1])) < steps:   
                        car[3].append(viagem_index)
                        car[2] = True
                        car[4] = (distancias[viagem_index] + veiculoPontoInicial(car, viagem[viagem_index][0],viagem[viagem_index][1]))
                        viagensOcupadas.append(viagem_index)
                        break

            imprimeEmFicheiro(fleet)    
            return

if __name__ == "__main__":
    for nome in argv:
        nomeFicheiro = nome
        main()


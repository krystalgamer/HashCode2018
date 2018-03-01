

def main():
    with open('a_example.in') as file:
        ficheiro = file.readlines()
        rows, columns, vehicles, rides, bonus, steps = tuple(ficheiro[0])
        matrix = [[0 for x in range(rows)] for y in range(columns)]





if __name__ == "__main__":
    main()

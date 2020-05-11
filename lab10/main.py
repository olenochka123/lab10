from lawn_mower import Lawn_mower


def main():
    Taras = Lawn_mower(200, 5, "USA", 5.26, 10, 6, 32)
    Gazonokosila = Lawn_mower(201, 6, "Emerald", 5.27, 11, 7, 33)
    Travos_rubakus = Lawn_mower(202, 7, "Bogdan", 5.28, 12, 8)
    kosilki = [Taras, Gazonokosila, Travos_rubakus]
    [print(kosilka) for kosilka in kosilki]
    print("Count of sells: {0}".format(Lawn_mower.staticmethod()))

if __name__ =="__main__":
    main()
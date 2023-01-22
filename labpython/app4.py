
def main(nome, fn):

    def obter_idade():
        
        print(fn())

        if nome == "José":

            return 22

        elif nome == "Maria":

            return 20

    return obter_idade

if __name__ == "__main__":

    def calc_valor():
        return 2 * 5

    fn = main("José", calc_valor)

    print("idade:", fn())
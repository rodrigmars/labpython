import time
from collections import Counter

def test_criando_uma_matriz():


    try:

        compositores = [
            "Johann Sebastian Bach (1685-1750)",
            "Ludwing Van Beethowen (1770-1827)",
            "Wolfgang Amadeus Mozart (1756-1791)",
            "Frederic Chopin (1810-1849)",
            "Richard Wagner (1813-1883)",
            "Antonio Vivaldi (1678-1741)",
            "Franz Schubert (1797-1828)",
            "Johannes Brahms (1833-1897)"]


        compositores = """
            Johann Sebastian Bach (1685-1750)
            Ludwing Van Beethowen (1770-1827)
            Wolfgang Amadeus Mozart (1756-1791)
            Frederic Chopin (1810-1849)
            Richard Wagner (1813-1883)
            Antonio Vivaldi (1678-1741)
            Franz Schubert (1797-1828)
            Johannes Brahms (1833-1897)"""

        
        
        
        palavras = list(compositores.replace(" ","").replace("\n",""))
        print()
        print()

        print(palavras)

        print()

        palavras = dict(Counter(palavras))

        print(palavras)

        print()

        # print("1 - processo:", palavras)

        # print("2 - processo:",palavras)

        for d in sorted(palavras.items(), key=lambda x: x[1]):
            print(f"{d[0]}={d[1]}")


        palavras = []

        # for c in compositores:
        #     palavras.append(list(c))

        # print(palavras[0])

        # print("fin")
    
    except Exception as ex:
    
        print("ERRO>>>>>>", ex)

    # assert type(compositores) == list
    # assert len(compositores) >= 8
    # assert not compositores[0] is None
    # assert len(compositores[0]) > 0

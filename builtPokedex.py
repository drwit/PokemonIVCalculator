#builtPokedex.py  by Wuch

import pickle

Pokedex = {}

def main():
    Pokedex['001'] = ['Bulbasaur', 45, 49, 49, 65, 65, 45]
    Pokedex['002'] = ['Ivysaur', 60, 62, 63, 80, 80, 60]
    Pokedex['003'] = ['Venusaur', 80, 82, 83, 100, 100, 80]
    Pokedex['004'] = ['Charmander', 39, 52, 43, 60, 50, 65]
    Pokedex['005'] = ['Charmeleon', 58, 64, 58, 80, 65, 80]
    Pokedex['006'] = ['Charizard', 78, 84, 78, 109, 85, 100]
    Pokedex['007'] = ['Squirtle', 44, 48, 65, 50, 64, 43]
    Pokedex['008'] = ['Wartortle', 59, 63, 80, 65, 80, 58]
    Pokedex['009'] = ['Blastoise', 79, 83, 100, 85, 105, 78]
    Pokedex['010'] = ['Caterpie', 45, 30, 35, 20, 20, 45]
    Pokedex['011'] = ['Metapod', 50, 20, 55, 25, 25, 30]
    Pokedex['012'] = ['Butterfree', 60, 45, 50, 90, 80, 70]

    Pokedex['013'] = ['Weedle', 40, 35, 30, 20, 20, 50]
    Pokedex['014'] = ['Kakuna', 45, 25, 50, 25, 25, 35]
    Pokedex['015'] = ['Beedrill', 65, 90, 40, 45, 80, 75]

    print Pokedex
    fileobj = open('./data/Pokedex.pkl','wb')
    pickle.dump(Pokedex, fileobj)
    fileobj.close()

if __name__ == '__main__':
    main()

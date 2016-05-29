# -*- coding: utf-8 -*-

import os
import pickle

Pokedexdic = {}
NatureModify = {'Lonely': [1.1, 0.9, 1, 1, 1],
                'Adamant':[1.1, 1, 0.9, 1, 1],
                'Naughty':[1.1, 1, 1, 0.9, 1],
                'Brave':  [1.1, 1, 1, 1, 0.9],
                'Bold':   [0.9, 1.1, 1, 1, 1],
                'Impish': [1, 1.1, 0.9, 1, 1],
                'Lax':    [1, 1.1, 1, 0.9, 1],
                'Relaxed':[1, 1.1, 1, 1, 0.9],
                'Modest':[0.9, 1, 1.1, 1, 1],
                'Mild':  [1, 0.9, 1.1, 1, 1],
                'Rash':  [1, 1, 1.1, 0.9, 1],
                'Quiet': [1, 1, 1.1, 1, 0.9],
                'Calm':   [0.9, 1, 1, 1.1, 1],
                'Gentle': [1, 0.9, 1, 1.1, 1],
                'Careful':[1, 1, 0.9, 1.1, 1],
                'Sassy':  [1, 1, 1, 1.1, 0.9],
                'Timid':[0.9, 1, 1, 1, 1.1],
                'Hasty':[1, 0.9, 1, 1, 1.1],
                'Jolly':[1, 1, 0.9, 1, 1.1],
                'Naive':[1, 1, 1, 0.9, 1.1],
                'Docile':[1, 1, 1, 1, 1],
                'Bashful':[1, 1, 1, 1, 1],
                'Serious':[1, 1, 1, 1, 1],
                'Hardy':[1, 1, 1, 1, 1],
                'Quirky':[1, 1, 1, 1, 1]
                }

#load Pokedex data from file
fileobj = open('./data/Pokedex.pkl', 'rb')
Pokedexdic = pickle.load(fileobj)
fileobj.close()

class Pokemon(object):
    '''a Pokemon's info'''
    def __init__(self, ID='001', level=50, nature='Serious'):
        self.ID = ID
        self.level = level
        #nature check
        try:
            self.setNature(nature)
        except NatureError as e:
            print e.value
        

        #load stats data to obj
        self.name = Pokedexdic[self.ID][0]
        self.StatsValues = StatsValues(Pokedexdic[self.ID][1],
                                       Pokedexdic[self.ID][2],
                                       Pokedexdic[self.ID][3],
                                       Pokedexdic[self.ID][4],
                                       Pokedexdic[self.ID][5],
                                       Pokedexdic[self.ID][6])
        
        #load done

        #EV default set
        self.setEffortValues(0,0,0,0,0,0)

        #IV default set
        self.setIndividualValues(0,0,0,0,0,0)

        #ActualValues calculate
        self.ActualValues = ActualValues()
        self.calcActualValues()

        print 'generate done'

    def setNature(self,nature):
        if nature not in ['Lonely','Adamant', 'Naughty', 'Brave',\
                          'Bold', 'Impish', 'Lax', 'Relaxed',\
                          'Modest', 'Mild', 'Rash', 'Quiet',\
                          'Calm', 'Gentle', 'Careful', 'Sassy',\
                          'Timid', 'Hasty', 'Jolly', 'Naive',\
                          'Docile', 'Bash', 'Serious', 'Hardy'\
                          'Quirky']:
            raise NatureError('Invalid nature type')
        else:
            self.nature = nature
        

    def setEffortValues(self, HP=0, Att=0, Def=0, SpAtt=0, SpDef=0, Speed=0):
        self.EffortValues = EffortValues(HP, Att, Def, SpAtt, SpDef, Speed)

    def setIndividualValues(self, HP=0, Att=0, Def=0, SpAtt=0, SpDef=0, Speed=0):
        self.IndividualValues = IndividualValues(HP, Att, Def, SpAtt, SpDef, Speed)

    def calcActualValues(self):
        self.ActualValues.HP = (self.StatsValues.HP*2 +
                                self.EffortValues.HP/4 +
                                self.IndividualValues.HP) * self.level /100 + self.level + 10

        self.ActualValues.Att = (self.StatsValues.Att*2 +
                                self.EffortValues.Att/4 +
                                self.IndividualValues.Att) * self.level /100 + 5

        self.ActualValues.Def = (self.StatsValues.Def*2 +
                                self.EffortValues.Def/4 +
                                self.IndividualValues.Def) * self.level /100 + 5

        self.ActualValues.SpAtt = (self.StatsValues.SpAtt*2 +
                                self.EffortValues.SpAtt/4 +
                                self.IndividualValues.SpAtt) * self.level /100 + 5

        self.ActualValues.SpDef = (self.StatsValues.SpDef*2 +
                                self.EffortValues.SpDef/4 +
                                self.IndividualValues.SpDef) * self.level /100 + 5

        self.ActualValues.Speed = (self.StatsValues.Speed*2 +
                                self.EffortValues.Speed/4 +
                                self.IndividualValues.Speed) * self.level /100 + 5

        #性格修正 todo
        # +Attack
        if self.nature == 'Lonely':
            self.ActualValues.Att *= 1.1
            self.ActualValues.Def *= 0.9
        elif self.nature == 'Adamant':
            self.ActualValues.Att *= 1.1
            self.ActualValues.SpAtt *= 0.9
        elif self.nature == 'Naughty':
            self.ActualValues.Att *= 1.1
            self.ActualValues.SpDef *= 0.9
        elif self.nature == 'Brave':
            self.ActualValues.Att *= 1.1
            self.ActualValues.Speed *= 0.9
        # +Defence
        elif self.nature == 'Bold':
            self.ActualValues.Def *= 1.1
            self.ActualValues.Att *= 0.9
        elif self.nature == 'Impish':
            self.ActualValues.Def *= 1.1
            self.ActualValues.SpAtt *= 0.9
        elif self.nature == 'Lax':
            self.ActualValues.Def *= 1.1
            self.ActualValues.SpDef *= 0.9
        elif self.nature == 'Relaxed':
            self.ActualValues.Def *= 1.1
            self.ActualValues.Speed *= 0.9
        # +Sp.Attack
        elif self.nature == 'Modest':
            self.ActualValues.SpAtt *= 1.1
            self.ActualValues.Att *= 0.9
        elif self.nature == 'Mild':
            self.ActualValues.SpAtt *= 1.1
            self.ActualValues.Def *= 0.9
        elif self.nature == 'Rash':
            self.ActualValues.SpAtt *= 1.1
            self.ActualValues.SpDef *= 0.9
        elif self.nature == 'Quiet':
            self.ActualValues.SpAtt *= 1.1
            self.ActualValues.Speed *= 0.9
        # +Sp.Defence
        elif self.nature == 'Calm':
            self.ActualValues.SpDef *= 1.1
            self.ActualValues.Att *= 0.9
        elif self.nature == 'Gentle':
            self.ActualValues.SpDef *= 1.1
            self.ActualValues.Def *= 0.9
        elif self.nature == 'Careful':
            self.ActualValues.SpDef *= 1.1
            self.ActualValues.SpAtt *= 0.9
        elif self.nature == 'Sassy':
            self.ActualValues.SpDef *= 1.1
            self.ActualValues.Speed *= 0.9
        # +Speed
        elif self.nature == 'Timid':
            self.ActualValues.Speed *= 1.1
            self.ActualValues.Att *= 0.9
        elif self.nature == 'Hasty':
            self.ActualValues.Speed *= 1.1
            self.ActualValues.Def *= 0.9
        elif self.nature == 'Jolly':
            self.ActualValues.Speed *= 1.1
            self.ActualValues.SpAtt *= 0.9
        elif self.nature == 'Naive':
            self.ActualValues.Speed *= 1.1
            self.ActualValues.Spdef *= 0.9

    def calcActualValues(self):
        #print type(self.EffortValues.HP)
        self.IndividualValues.HP = (self.ActualValues.HP - self.level - 10)*100/self.level -\
                                    self.EffortValues.HP/4 - self.StatsValues.HP*2

        self.IndividualValues.Att = (self.ActualValues.Att/NatureModify[self.nature][0] - 5 )*\
                                     100 / self.level - self.EffortValues.Att/4 -\
                                     self.StatsValues.Att*2
        self.IndividualValues.Def = (self.ActualValues.Def/NatureModify[self.nature][0] - 5 )*\
                                     100 / self.level - self.EffortValues.Def/4 -\
                                     self.StatsValues.Def*2
        self.IndividualValues.SpAtt = (self.ActualValues.SpAtt/NatureModify[self.nature][0] - 5 )*\
                                     100 / self.level - self.EffortValues.SpAtt/4 -\
                                     self.StatsValues.SpAtt*2
        self.IndividualValues.SpDef = (self.ActualValues.SpDef/NatureModify[self.nature][0] - 5 )*\
                                     100 / self.level - self.EffortValues.SpDef/4 -\
                                     self.StatsValues.SpDef*2
        self.IndividualValues.Speed = (self.ActualValues.Speed/NatureModify[self.nature][0] - 5 )*\
                                     100 / self.level - self.EffortValues.Speed/4 -\
                                     self.StatsValues.Speed*2                                     
        
              
class PokemonAbilities(object):
    def __init__(self, HP=0, Att=0, Def=0, SpAtt=0, SpDef=0, Speed=0):
        self.HP = HP
        self.Att = Att
        self.Def = Def
        self.SpAtt = SpAtt
        self.SpDef = SpDef
        self.Speed = Speed

class StatsValues(PokemonAbilities):
    pass

class EffortValues(PokemonAbilities):
    def __init__(self, HP=0, Att=0, Def=0, SpAtt=0, SpDef=0, Speed=0):
        if HP+Att+Def+SpAtt+SpDef+Speed > 510 or\
            Att not in range(0,252) or\
            Def not in range(0,252) or\
            SpAtt not in range(0,252) or\
            SpDef not in range(0,252) or\
            Speed not in range(0,252):
            raise EVError('Effort Value error')
        self.HP = HP
        self.Att = Att
        self.Def = Def
        self.SpAtt = SpAtt
        self.SpDef = SpDef
        self.Speed = Speed


class IndividualValues(PokemonAbilities):
    def __init__(self, HP=0, Att=0, Def=0, SpAtt=0, SpDef=0, Speed=0):
        if HP not in range(0,30) or\
            Att not in range(0,30) or\
            Def not in range(0,30) or\
            SpAtt not in range(0,30) or\
            SpDef not in range(0,30) or\
            Speed not in range(0,30):
            raise IVError('IV value error')
        self.HP = HP
        self.Att = Att
        self.Def = Def
        self.SpAtt = SpAtt
        self.SpDef = SpDef
        self.Speed = Speed

class ActualValues(PokemonAbilities):
    pass

class IVError(Exception):
    def __init__(self, value):
        self.value = value
    def __str__(self):
       return repr(self.value)

class EVError(Exception):
    def __init__(self, value):
        self.value = value
    def __str__(self):
       return repr(self.value)

class NatureError(Exception):
    def __init__(self, value):
        self.value = value
    def __str__(self):
       return repr(self.value)

def test():
    #pass
    print type(Pokeobj.EffortValues.Att)
        
if __name__ == '__main__':
    Pokeobj = Pokemon('001', 50, 'Timid')
    #test()



# -*- coding: utf-8 -*-

import sys
from PyQt4 import QtGui, QtCore
import Pokemons
import re

#Pokemons.Pokemondir = {}

natureList = ['Lonely','Adamant', 'Naughty', 'Brave',\
              'Bold', 'Impish', 'Lax', 'Relaxed',   \
              'Modest', 'Mild', 'Rash', 'Quiet',    \
              'Calm', 'Gentle', 'Careful', 'Sassy', \
              'Timid', 'Hasty', 'Jolly', 'Naive',   \
              'Docile', 'Bash', 'Serious', 'Hardy', \
              'Quirky']

class IVCalcWin(QtGui.QWidget):
    def __init__(self):
        #关联Pokemon对象
        self.currentPokemon = Pokemons.Pokemon()
        
        #窗体基本设置
    
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap('./img/ICON.ico'))
        
        
        super(IVCalcWin, self).__init__()
        self.setWindowTitle("Pokemon IV Calculator")
        self.setWindowIcon(icon)
        self.resize(120, 350)
        
        #上部标签
        LabelID = QtGui.QLabel(self.tr("ID:"))
        LabelNature = QtGui.QLabel(self.tr("Nature:"))
        LabelLevel = QtGui.QLabel(self.tr("Level:"))

        #上部组件：
        #Pokemon图片以及标签
        self.imgLabel = QtGui.QLabel()
        img = QtGui.QPixmap('./img/egg.gif')
        self.imgLabel.setPixmap(img)
        self.imgLabel.resize(img.width(),img.height())
        #ID
        ComboBoxID = QtGui.QComboBox()
        self.builtComboBoxID(ComboBoxID)
        #Nature
        ComboBoxNature = QtGui.QComboBox()
        ComboBoxNature.setSizeAdjustPolicy(1)
        self.builtComboBoxNature(ComboBoxNature)
        #Level
        LineEditLevel = QtGui.QLineEdit()
        self.builtLineEditLevel(LineEditLevel)

        #img layout
        imgLayout = QtGui.QHBoxLayout()
        imgLayout.addWidget(self.imgLabel)

        #mid-up layout
        textID = QtGui.QLabel(self.tr("ID    :"))
        textNature = QtGui.QLabel(self.tr("Nature:"))
        textLevel = QtGui.QLabel(self.tr("Level :"))
        midupLayout = QtGui.QVBoxLayout()
        midupLayout.addWidget(textID)
        midupLayout.addWidget(textNature)
        midupLayout.addWidget(textLevel)
        textID.setText = 'xxx'
        
        #right-up layout
        rightupLayout = QtGui.QVBoxLayout()
        rightupLayout.addWidget(ComboBoxID)
        rightupLayout.addWidget(ComboBoxNature)
        rightupLayout.addWidget(LineEditLevel)
        
        #bottom layout
        col0Layout = QtGui.QVBoxLayout()
        col1Layout = QtGui.QVBoxLayout()
        col2Layout = QtGui.QVBoxLayout()
        col3Layout = QtGui.QVBoxLayout()
        col4Layout = QtGui.QVBoxLayout()

        self.fillCol0(col0Layout)
        self.statsList = self.fillCol1(col1Layout)  #index 0 不可用
        self.EVList = self.fillCol2(col2Layout)     #index 0 不可用
        self.ACList = self.fillCol3(col3Layout)     #index 0 不可用
        self.IVList = self.fillCol4(col4Layout)     #index 0 不可用
        
        bottomLayout = QtGui.QGridLayout()
        bottomLayout.addLayout(col0Layout,0,0)
        bottomLayout.addLayout(col1Layout,0,1)
        bottomLayout.addLayout(col2Layout,0,2)
        bottomLayout.addLayout(col3Layout,0,3)
        bottomLayout.addLayout(col4Layout,0,4)
       
        #main layout
        mainLayout = QtGui.QGridLayout(self)
        mainLayout.addLayout(imgLayout,0,0)
        mainLayout.addLayout(midupLayout,0,1)
        mainLayout.addLayout(rightupLayout,0,2)
        mainLayout.addLayout(bottomLayout,1,0)

    def fillCol0(self,col0Layout):
        label0 = QtGui.QLabel(self.tr("   "))
        label1 = QtGui.QLabel(self.tr("HP:     "))
        label2 = QtGui.QLabel(self.tr("Att:    "))
        label3 = QtGui.QLabel(self.tr("Def:    "))
        label4 = QtGui.QLabel(self.tr("Sp.Att: "))
        label5 = QtGui.QLabel(self.tr("Sp.Def: "))
        label6 = QtGui.QLabel(self.tr("Speed:  "))
        col0Layout.addWidget(label0)
        col0Layout.addWidget(label1)
        col0Layout.addWidget(label2)
        col0Layout.addWidget(label3)
        col0Layout.addWidget(label4)
        col0Layout.addWidget(label5)
        col0Layout.addWidget(label6)

    def fillCol1(self,col1Layout):
        label0 = QtGui.QLabel(self.tr("Stats"))
        label1 = QtGui.QLineEdit(self.tr("  ?  "))
        label2 = QtGui.QLineEdit(self.tr("  ?  "))
        label3 = QtGui.QLineEdit(self.tr("  ?  "))
        label4 = QtGui.QLineEdit(self.tr("  ?  "))
        label5 = QtGui.QLineEdit(self.tr("  ?  "))
        label6 = QtGui.QLineEdit(self.tr("  ?  "))
        label1.setReadOnly(True)
        label2.setReadOnly(True)
        label3.setReadOnly(True)
        label4.setReadOnly(True)
        label5.setReadOnly(True)
        label6.setReadOnly(True)
        col1Layout.addWidget(label0)
        col1Layout.addWidget(label1)
        col1Layout.addWidget(label2)
        col1Layout.addWidget(label3)
        col1Layout.addWidget(label4)
        col1Layout.addWidget(label5)
        col1Layout.addWidget(label6)
        return [label0,label1,label2,label3,label4,label5,label6]

    def fillCol2(self,col2Layout):
        label0 = QtGui.QLabel(self.tr("  EV"))
        label1 = QtGui.QLineEdit('0')
        label2 = QtGui.QLineEdit('0')
        label3 = QtGui.QLineEdit('0')
        label4 = QtGui.QLineEdit('0')
        label5 = QtGui.QLineEdit('0')
        label6 = QtGui.QLineEdit('0')
        EXReg = QtGui.QIntValidator(0,31,self)
        label1.setValidator(EXReg)
        label2.setValidator(EXReg)
        label3.setValidator(EXReg)
        label4.setValidator(EXReg)
        label5.setValidator(EXReg)
        label6.setValidator(EXReg)

        self.builtLineEditEV(label1, 'HP')
        self.builtLineEditEV(label2, 'Att')
        self.builtLineEditEV(label3, 'Def')
        self.builtLineEditEV(label4, 'SpAtt')
        self.builtLineEditEV(label5, 'SpDef')
        self.builtLineEditEV(label6, 'Speed')
        
        col2Layout.addWidget(label0)
        col2Layout.addWidget(label1)
        col2Layout.addWidget(label2)
        col2Layout.addWidget(label3)
        col2Layout.addWidget(label4)
        col2Layout.addWidget(label5)
        col2Layout.addWidget(label6)
        return [label0,label1,label2,label3,label4,label5,label6]

    def fillCol3(self,col3Layout):
        label0 = QtGui.QLabel(self.tr("Actual"))
        label1 = QtGui.QLineEdit('0')
        label2 = QtGui.QLineEdit('0')
        label3 = QtGui.QLineEdit('0')
        label4 = QtGui.QLineEdit('0')
        label5 = QtGui.QLineEdit('0')
        label6 = QtGui.QLineEdit('0')
        ACReg = QtGui.QIntValidator(0,252,self)
        label1.setValidator(ACReg)
        label2.setValidator(ACReg)
        label3.setValidator(ACReg)
        label4.setValidator(ACReg)
        label5.setValidator(ACReg)
        label6.setValidator(ACReg)

        self.builtLineEditActual(label1, 'HP')
        self.builtLineEditActual(label2, 'Att')
        self.builtLineEditActual(label3, 'Def')
        self.builtLineEditActual(label4, 'SpAtt')
        self.builtLineEditActual(label5, 'SpDef')
        self.builtLineEditActual(label6, 'Speed')
        
        col3Layout.addWidget(label0)
        col3Layout.addWidget(label1)
        col3Layout.addWidget(label2)
        col3Layout.addWidget(label3)
        col3Layout.addWidget(label4)
        col3Layout.addWidget(label5)
        col3Layout.addWidget(label6)
        return [label0,label1,label2,label3,label4,label5,label6]
        
    def fillCol4(self,col4Layout):
        label0 = QtGui.QLabel(self.tr("  IV"))
        label1 = QtGui.QLineEdit(self.tr("  ?  "))
        label2 = QtGui.QLineEdit(self.tr("  ?  "))
        label3 = QtGui.QLineEdit(self.tr("  ?  "))
        label4 = QtGui.QLineEdit(self.tr("  ?  "))
        label5 = QtGui.QLineEdit(self.tr("  ?  "))
        label6 = QtGui.QLineEdit(self.tr("  ?  "))
        label1.setReadOnly(True)
        label2.setReadOnly(True)
        label3.setReadOnly(True)
        label4.setReadOnly(True)
        label5.setReadOnly(True)
        label6.setReadOnly(True)
        col4Layout.addWidget(label0)
        col4Layout.addWidget(label1)
        col4Layout.addWidget(label2)
        col4Layout.addWidget(label3)
        col4Layout.addWidget(label4)
        col4Layout.addWidget(label5)
        col4Layout.addWidget(label6)
        return [label0,label1,label2,label3,label4,label5,label6] 
        
    def builtComboBoxID(self, ComboBoxID): 
        x = 1
        ComboBoxID.insertItem(0, '--select--')
        for x in sorted(Pokemons.Pokedexdic):
            ComboBoxID.addItem(self.intToID(x)+' '+Pokemons.Pokedexdic[self.intToID(x)][0])
        
        #signal ID
        w = QtGui.QWidget()
        w.connect(ComboBoxID, QtCore.SIGNAL("currentIndexChanged(QString)"),\
                  self.catchIDChanged)
        
    def builtComboBoxNature(self, ComboBoxNature):
        #构建ComboBox
        for i,x in enumerate(natureList):
            ComboBoxNature.insertItem(i, self.tr(x))

        #signal nature
        w = QtGui.QWidget()
        w.connect(ComboBoxNature, QtCore.SIGNAL("currentIndexChanged(QString)"),\
                  self.catchNatureChanged)
            

    def builtLineEditLevel(self, LineEditLevel):
        LineEditLevel.setValidator(QtGui.QIntValidator(1,100,self))
        w = QtGui.QWidget()
        w.connect(LineEditLevel, QtCore.SIGNAL("textChanged(QString)"),\
                  self.catchLineEditTextchanged)

    def catchIDChanged(self, QString):
        #初始图片
        if QString == '--select--':
            img = QtGui.QPixmap('./img/egg.gif')
            self.imgLabel.setPixmap(img)
            return

        #装载图片
        IDstr = QString.split(' ')[0]
        self.currentPokemon.ID = IDstr
        img = QtGui.QPixmap('./img/' + IDstr + '.gif')
        self.imgLabel.setPixmap(img)

        #改Stats值
        self.currentPokemon.ID = IDstr
        self.currentPokemon.StatsValues = Pokemons.StatsValues(Pokemons.Pokedexdic[str(IDstr)][1],
                                                               Pokemons.Pokedexdic[str(IDstr)][2],
                                                               Pokemons.Pokedexdic[str(IDstr)][3],
                                                               Pokemons.Pokedexdic[str(IDstr)][4],
                                                               Pokemons.Pokedexdic[str(IDstr)][5],
                                                               Pokemons.Pokedexdic[str(IDstr)][6])
        self.statsList[1].setText(str(self.currentPokemon.StatsValues.HP))
        self.statsList[2].setText(str(self.currentPokemon.StatsValues.Att))
        self.statsList[3].setText(str(self.currentPokemon.StatsValues.Def))
        self.statsList[4].setText(str(self.currentPokemon.StatsValues.SpAtt))
        self.statsList[5].setText(str(self.currentPokemon.StatsValues.SpDef))
        self.statsList[6].setText(str(self.currentPokemon.StatsValues.Speed))
        
    def catchNatureChanged(self, QString):
        self.currentPokemon.nature = QString
        print self.currentPokemon.nature

    
    def catchLineEditTextchanged(self, QString):
        if re.compile(r'[0]*').match(QString):
            self.currentPokemon.level = 50
        else:
            self.currentPokemon.level = int(QString)
        print self.currentPokemon.level

    #-----下部组件信号与槽

    def builtLineEditEV(self, LineEditEV, Attribute):
        LineEditEV.textChanged.connect(lambda: self.catchEVChanged(LineEditEV, Attribute))
        

    def builtLineEditActual(self, LineEditActual, Attribute):
        LineEditActual.textChanged.connect(lambda: self.catchACChanged(LineEditActual, Attribute))

    def catchEVChanged(self, LineEditEV, Attribute):
        print Attribute, LineEditEV.text()
        if Attribute == 'HP':
            self.currentPokemon.EffortValues.HP = int(LineEditEV.text())
        elif Attribute == 'Att':
            self.currentPokemon.EffortValues.Att = int(LineEditEV.text())
        elif Attribute == 'Def':
            self.currentPokemon.EffortValues.Def = int(LineEditEV.text())
        elif Attribute == 'SpAtt':
            self.currentPokemon.EffortValues.SpAtt = int(LineEditEV.text())
        elif Attribute == 'SpDef':
            self.currentPokemon.EffortValues.SpDef = int(LineEditEV.text())
        elif Attribute == 'Speed':
            self.currentPokemon.EffortValues.Speed = int(LineEditEV.text())

        self.currentPokemon.calcActualValues()

        if Attribute == 'HP':
            self.IVList[1].setText(str(self.currentPokemon.IndividualValues.HP))
        elif Attribute == 'Att':
            self.IVList[2].setText(str(self.currentPokemon.IndividualValues.Att))
        elif Attribute == 'Def':
            self.IVList[3].setText(str(self.currentPokemon.IndividualValues.Def))
        elif Attribute == 'SpAtt':
            self.IVList[4].setText(str(self.currentPokemon.IndividualValues.SpAtt))
        elif Attribute == 'SpDef':
            self.IVList[5].setText(str(self.currentPokemon.IndividualValues.SpDef))
        elif Attribute == 'Speed':
            self.IVList[6].setText(str(self.currentPokemon.IndividualValues.Speed))
        #test
        print self.currentPokemon.EffortValues

    def catchACChanged(self, LineEditActual, Attribute):
        print Attribute, LineEditActual.text()
        
        if Attribute == 'HP':
            self.currentPokemon.ActualValues.HP = int(LineEditActual.text())
        elif Attribute == 'Att':
            self.currentPokemon.ActualValues.Att = int(LineEditActual.text())
        elif Attribute == 'Def':
            self.currentPokemon.ActualValues.Def = int(LineEditActual.text())
        elif Attribute == 'SpAtt':
            self.currentPokemon.ActualValues.SpAtt = int(LineEditActual.text())
        elif Attribute == 'SpDef':
            self.currentPokemon.ActualValues.SpDef = int(LineEditActual.text())
        elif Attribute == 'Speed':
            self.currentPokemon.ActualValues.Speed = int(LineEditActual.text())

        self.currentPokemon.calcActualValues()

        if Attribute == 'HP':
            self.IVList[1].setText(str(self.currentPokemon.IndividualValues.HP))
        elif Attribute == 'Att':
            self.IVList[2].setText(str(self.currentPokemon.IndividualValues.Att))
        elif Attribute == 'Def':
            self.IVList[3].setText(str(self.currentPokemon.IndividualValues.Def))
        elif Attribute == 'SpAtt':
            self.IVList[4].setText(str(self.currentPokemon.IndividualValues.SpAtt))
        elif Attribute == 'SpDef':
            self.IVList[5].setText(str(self.currentPokemon.IndividualValues.SpDef))
        elif Attribute == 'Speed':
            self.IVList[6].setText(str(self.currentPokemon.IndividualValues.Speed))
    
        #test
        print self.currentPokemon.ActualValues

    def intToID(self, x):
        if x < 10:
            return '00'+str(x)
        elif x < 100:
            return '0'+str(x)
        else:
            return str(x)
            
def main():
    app = QtGui.QApplication(sys.argv)
    root = IVCalcWin()
    root.show()
    app.exec_()

def test():
    p = Pokemons.Pokemon()

if __name__ == '__main__':
    main()
    #test()

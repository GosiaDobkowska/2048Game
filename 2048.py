#ładowanie pakietow
from PyQt4 import QtGui
from PyQt4 import QtCore
import random
import sys
import numpy as np
 
 
 

#Klasa Gra_2048
class Gra_2048(QtGui.QMainWindow):
    def __init__(self):
        super(Gra_2048, self).__init__()
        self.kolory_numerki={
			0:(224, 239, 149),
			2:(217, 235, 53),
			4:(65, 189, 65),
			8:(87, 182, 160),
			16:(87, 90, 182),
			32:(200, 116, 242),
			64:(216, 101, 205),
			128:(216, 101, 139),
			256:(198, 177, 184),
			512:(243, 175, 130),
			1024:(166, 176, 201),
			2048:(222, 80, 70),
                 4096: (166, 80, 130),
                 8192: (216, 189, 235),
                 16384:(243, 177, 65)
		}
        self.wymiary1 = [10+i*120 for i in range(0, 4) for j in range(0, 4)]
        self.wymiary2 = [110+j*120 for i in range(0, 4) for j in range(0,4)]
        self.rodzaj_wymiaru = 2
        self.wielkosc_x = 500
        self.wielkosc_y = 500
        self.r = 110
        self.score = 0
        self.ustawien = 0
        self.kolor = QtGui.QBrush(QtGui.QColor(0xbbada0))
        self.initUI()




#metoda inicjująca
    def initUI(self):
        self.resize(self.wielkosc_x, self.wielkosc_y+100)
        self.setWindowTitle('2048')
        self.setWindowIcon(QtGui.QIcon('logo_2048.png'))        
        self.center()
        self.show()
        self.statusBar().showMessage('I want to play with You!')
        self.poczatek()
        self.menu = self.menuBar().addMenu('&Menu')
        self.menu.addAction('Ustawienia', self.ustawienia)
        self.menuBar().addSeparator()
        self.menu.addAction('Nowa gra', self.nowa_gra)
        self.menuBar().addSeparator()
        self.menu.addAction('Zamknij', QtGui.qApp.quit)
        self.menuBar().addSeparator()
        self.help = self.menuBar().addMenu('&Help')
        self.help.addAction('Instrukcja', self.instrukcja)
 
    


#łączenie z klasą ustawienia    
    def ustawienia(self):
        if self.ustawien == 0:
            self.ustawien = Ustaw()        
        if self.ustawien.exec_():
            self.zmien_rozmiar(self.ustawien.rozmiar)
            self.kolor = self.ustawien.col
            self.update()




#zmien rozmiar puzzli            
    def zmien_rozmiar(self, x):
        if x == 2:
            z = 120
        elif x == 1:
            z = 100
        elif x == 3:
            z = 140
        self.rodzaj_wymiaru = x
        self.wymiary1 = [10+i*z for i in range(0, 4) for j in range(0, 4)]
        self.wymiary2 = [110+j*z for i in range(0, 4) for j in range(0,4)]
        self.wielkosc_x = 4*z + 20
        self.wielkosc_y = 4*z + 20
        self.r = z - 10
        self.resize(self.wielkosc_x, self.wielkosc_y+100)
        self.update()
            
    


#metoda wyświetlająca instrukcje    
    def instrukcja(self):
        QtGui.QMessageBox.about(self, 'Instrukcja', 
        ' Możesz używać klawiszy Up, Down, Left i Right. \n Twoim celem jest łączenie pol z taka sama liczba, \n az do uzyskania liczby 2048. \n Powodzenia!')



  
#rozpoczyna nową grę        
    def nowa_gra(self):
        self.score = 0
        self.poczatek()
        self.statusBar().showMessage('I want to play with You!')



        
#sprawdzenie czy ktorys z puzzli jest rowny 2048        
    def czy_wygrales(self):

                    
        czy_2048 = 0
        for i in range(0, 4):
            for j in range(0, 4):
                if self.tablica[i, j]==2048:
                    czy_2048 = 1
        if czy_2048 == 1:
            QtGui.QMessageBox.information(self,'Gratulacje!','Wygrałeś! Naciśnij Escape, aby rozpocząć nową grę lub proboj zebrac wieksza liczbe. :)')
     
     
     
     
#Sprawdzenie czy mozna wykonac jakis ruch     
    def czy_mozna_sie_ruszyc(self):
         czy = 0
         for i in range(0, 4):
             for j in range(0, 4):
                 if self.tablica[i, j]==0:
                     czy = 1

         for i in range(0, 4):
            for j in range(0, 4):
                if i<=2 and self.tablica[i, j]==self.tablica[i+1, j]:
                    czy = 1
                if j <=2 and self.tablica[i, j] == self.tablica[i, j+1]:
                    czy =1
         if czy == 0:
             QtGui.QMessageBox.information(self,'Koniec gry!','Nie możesz wykonać żadnego ruchu :(. Naciśnij Escape, aby rozpocząć nową grę.')
                
            
     

#Poczatek gry - czyszczenie planszy        
    def poczatek(self):
        self.tablica= np.zeros((4, 4))
        self.napisy = ['' for i in range(0, 16)]
        self.kolory1 = [self.kolory_numerki[0][0] for i in range(0, 16)] 
        self.kolory2 = [self.kolory_numerki[0][1] for i in range(0, 16)]
        self.kolory3 = [self.kolory_numerki[0][2] for i in range(0, 16)]
        self.nowy()
        self.zmiana()
        self.nowy()
        self.zmiana()
        self.statusBar().showMessage(':)')



       
#Zmienianie wygladu planaszy     
    def zmiana(self):
         
        self.kolory1 = [self.kolory_numerki[self.tablica[i, j]][0] for i in range(0, 4) for j in range(0,4)] 
        self.kolory2 = [self.kolory_numerki[self.tablica[i, j]][1] for i in range(0, 4) for j in range(0,4)]
        self.kolory3 = [self.kolory_numerki[self.tablica[i, j]][2] for i in range(0, 4) for j in range(0,4)]
        
        for i in range(0, 4):
            for j in range(0, 4):
                if self.tablica[i, j]!=0:
                    self.napisy[4*i+j]=str(int(self.tablica[i, j]))
                else: self.napisy[4*i+j]=''

        self.update()
        

        
     
#Wstawianie nowego puzzla     
    def nowy(self):
        z = []
        for i in range(0, 4):
            for j in range(0, 4):
                if self.tablica[i,j]==0:
                    z.append(4*i+j)
        if len(z)>=1:

            n = random.sample(z, 1)
            u = random.uniform(0, 1)
        
            if (u>=0.8): 
                self.tablica[int(n[0]/4), n[0]-4*int(n[0]/4)]=4
            else: 
                self.tablica[int(n[0]/4), n[0]-4*int(n[0]/4)]=2




#Definicja ruchu w gore        
    def w_gore(self):
        czy_mozna_sie_ruszyc=0
        for i in range(0, 4):
            for j in range(1, 4):
                if self.tablica[i, j]!=0:
                    k = j
                    while k-1>=0 and self.tablica[i, k-1]==0:
                        k=k-1
                    if k-1>=0 and self.tablica[i, k-1]==self.tablica[i, j]:
                        self.tablica[i, k-1]*=2
                        self.tablica[i, j]=0
                        self.score=self.score+self.tablica[i, k-1]
                        czy_mozna_sie_ruszyc=1
                        
                    elif k<j:
                        self.tablica[i, k]=self.tablica[i, j]
                        self.tablica[i, j]=0
                        czy_mozna_sie_ruszyc=1
        if czy_mozna_sie_ruszyc:
            self.zmiana()
            self.nowy()
            self.zmiana()
        self.czy_wygrales()
        self.czy_mozna_sie_ruszyc()
        
        


#Definicja ruchu w dol
    def w_dol(self):
          czy_mozna_sie_ruszyc=0
          for i in range(0,4) :
              for j in [2, 1, 0]:
                  if self.tablica[i, j]!=0:
                      k=j
                      while k+1<=3 and self.tablica[i, k+1]==0:
                          k=k+1
                      if k+1<=3 and self.tablica[i, k+1]==self.tablica[i, j]:
                              self.tablica[i, k+1]*=2
                              self.tablica[i, j]=0
                              self.score=self.score+self.tablica[i, k+1]
                              czy_mozna_sie_ruszyc=1
                      elif k>j:
                              self.tablica[i, k]=self.tablica[i, j]
                              self.tablica[i, j]=0
                              czy_mozna_sie_ruszyc=1
          if czy_mozna_sie_ruszyc:
            self.zmiana()
            self.nowy()
            self.zmiana()

            self.czy_wygrales()
            self.czy_mozna_sie_ruszyc()




#Definicja ruchu w lewo
    def w_lewo(self):
        czy_mozna_sie_ruszyc=0
        for i in range(1,4):
            for j in range(0,4):
                if self.tablica[i, j]!=0:
                    k=i
                    while k-1>=0 and self.tablica[k-1, j]==0:
                        k=k-1
                    if k-1>=0 and self.tablica[k-1, j]==self.tablica[i, j]:
                        self.tablica[k-1, j]*=2
                        self.tablica[i, j]=0
                        self.score = self.score + self.tablica[k-1, k]
                        czy_mozna_sie_ruszyc=1
                    elif k<i:
                        self.tablica[k, j]=self.tablica[i, j]
                        self.tablica[i, j]=0
                        czy_mozna_sie_ruszyc=1
        if czy_mozna_sie_ruszyc==1:
            self.zmiana()
            self.nowy()
            self.zmiana()
        self.czy_wygrales()
        self.czy_mozna_sie_ruszyc()




#Definicja ruchu w prawo            
    def w_prawo(self):
        czy_mozna_sie_ruszyc=0
        for i in [2, 1, 0]:
            for j in range(0,4):
                if self.tablica[i, j]!=0:
                    k=i
                    while k+1<=3 and self.tablica[k+1, j]==0:
                        k=k+1
                    if k+1<=3 and self.tablica[k+1, j]==self.tablica[i, j]:
                        self.tablica[k+1, j]*=2
                        self.tablica[i, j]=0
                        self.score = self.score+self.tablica[k+1, j]
                        czy_mozna_sie_ruszyc=1
                    elif k>i:
                        self.tablica[k, j]=self.tablica[i, j]
                        self.tablica[i, j]=0
                        czy_mozna_sie_ruszyc=1
        if czy_mozna_sie_ruszyc==1:
            self.zmiana()
            self.nowy()
            self.zmiana()   
        self.czy_wygrales()
        self.czy_mozna_sie_ruszyc()




#metoda do przesuwania głownego okna do centrum ekranu
    def center(self):
        qr = self.frameGeometry()
        cp = QtGui.QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())
    
    
    
    
#metoda do rysowania jednego puzla
    def drawRectangle(self, qp,r,b,g,x,y,text):

        qp.setBrush(QtGui.QColor(r, b, g))
        rect = QtCore.QRectF(x, y, self.r, self.r)
        qp.drawRect(rect)
        pen = QtGui.QPen(QtCore.Qt.darkMagenta, 4, QtCore.Qt.SolidLine)
        
        qp.setPen(pen)
        qp.drawLine(x, y, x+self.r, y)
        qp.drawLine(x, y+self.r, x+self.r, y+self.r)
        qp.drawLine(x, y, x, y+self.r)
        qp.drawLine(x+self.r, y, x+self.r, y+self.r)
        
        qp.setPen(QtGui.QColor(0, 0, 0))
        qp.setFont(QtGui.QFont('Britannic Bold', 25))
        qp.drawText(rect, QtCore.Qt.AlignCenter, text) 
        



#Rysowanie aktualnego wyniku        
    def drawScore(self, qp,r,b,g,x,y,z, w, text):

        qp.setBrush(QtGui.QColor(r, b, g))
        rect = QtCore.QRectF(x, y, z, w)
        qp.drawRect(rect)
        pen = QtGui.QPen(QtCore.Qt.darkMagenta, 4, QtCore.Qt.SolidLine)
        
        qp.setPen(pen)
        qp.drawLine(x, y, x+z, y)
        qp.drawLine(x, y+w, x+z, y+w)
        qp.drawLine(x, y, x, y+w)
        qp.drawLine(x+z, y, x+z, y+w)
        
        qp.setPen(QtGui.QColor(0, 0, 0))
        qp.setFont(QtGui.QFont('Britannic Bold', 25))
        qp.drawText(rect, QtCore.Qt.AlignCenter, text)   
        



#Definicja wciskania klawiszy        
    def keyPressEvent(self,e):
        if e.key()==QtCore.Qt.Key_Up:
            self.w_gore()
            self.update()
        elif e.key()==QtCore.Qt.Key_Down:
            self.w_dol()
            self.update()
        elif e.key()==QtCore.Qt.Key_Right:
            self.w_prawo()
            self.update()
        elif e.key()==QtCore.Qt.Key_Left:
            self.w_lewo()
            self.update()
        elif e.key()==QtCore.Qt.Key_Escape:
            self.nowa_gra()




#rysowanie planszy
    def paintEvent(self, e):
        
        qp = QtGui.QPainter()
        qp.begin(self)
        qp.setBrush(self.kolor)
        qp.drawRect(self.rect())

        for i in range(0, 16):
            self.drawRectangle(qp, self.kolory1[i], self.kolory2[i], self.kolory3[i], self.wymiary1[i], self.wymiary2[i],  self.napisy[i])
        
        self.drawScore(qp, 222, 170, 170, 105, 27, 280, 75, 'Result: '+ str(int(self.score)))
        qp.end()




#zamkniecie aplikacji        
    def closeEvent(self, e):
        
        reply = QtGui.QMessageBox.question(self, 'Message',
            "Are you sure to quit?", QtGui.QMessageBox.Yes | 
            QtGui.QMessageBox.No, QtGui.QMessageBox.No)

        if reply == QtGui.QMessageBox.Yes:
            e.accept()
        else:
            e.ignore()        




#Klasa ustawien
class Ustaw(QtGui.QDialog):

    def __init__(self):
        super(Ustaw, self).__init__()
        self.initUI()
        
    def initUI(self):      
        
         self.rozmiar = 2
         self.col = QtGui.QColor(0xbbada0)
#        
         rozmiarPlanszy = QtGui.QLabel('Rozmiar planszy')
         kolor = QtGui.QLabel('Kolor tla')

#
         rozmiarPlanszyEdit = QtGui.QComboBox(self)
         rozmiarPlanszyEdit.addItem('1')
         rozmiarPlanszyEdit.addItem('2')
         rozmiarPlanszyEdit.addItem('3')
         rozmiarPlanszyEdit.activated[str].connect(self.wymiary)
         
         self.btn = QtGui.QPushButton('Zmien kolor tablicy', self)
         self.btn.clicked.connect(self.zmien_kolor)



         self.frm = QtGui.QFrame(self)
         self.frm.setStyleSheet("QWidget { background-color: %s }" % self.col.name())
         self.frm.setGeometry(130, 22, 100, 100)          
         
         
         
         self.buttonBox = QtGui.QDialogButtonBox(QtGui.QDialogButtonBox.Ok | QtGui.QDialogButtonBox.Cancel)
         self.buttonBox.accepted.connect(self.accept)
         self.buttonBox.rejected.connect(self.reject)           
         
         
         grid = QtGui.QGridLayout()
         grid.setSpacing(10)
         grid.addWidget(rozmiarPlanszy, 1, 0)
         grid.addWidget(rozmiarPlanszyEdit, 1, 1)
         grid.addWidget(kolor, 2, 0)
         grid.addWidget(self.frm, 2, 1)
         grid.addWidget(self.btn, 3, 1)
         grid.addWidget(self.buttonBox,4,1)
         self.setLayout(grid) 




#Opcja zmiany koloru tła        
    def zmien_kolor(self):
        col = QtGui.QColorDialog.getColor()
        if col.isValid():
            self.frm.setStyleSheet("QWidget { background-color: %s }"
                % col.name())
            self.col = col
 
            
            
            
#Zmiana rozmiaru puzzli            
    def wymiary(self, text):
        self.rozmiar = int(text[0])
    



    
    def center(self):
        qr = self.frameGeometry()
        cp = QtGui.QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())
        
        



def main():
    
    app = QtGui.QApplication(sys.argv)
    ex = Gra_2048()
    sys.exit(app.exec_())




if __name__ == '__main__':
    main()    
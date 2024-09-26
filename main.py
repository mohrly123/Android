# main.py
from kivymd.app import MDApp
from kivy.lang import Builder
from kivymd.uix.screenmanager import MDScreenManager
from kivymd.uix.screen import MDScreen
import random

class FirstWindow(MDScreen):
    def __init__(self,**kwargs):
        super(FirstWindow, self).__init__(**kwargs)
        self.counter = 0
        self.counter_falsch = 0
        self.correct_answer = None
        
# Abschnitt für Tab Plus Minus Rechner
    # Methode zum deaktivieren des btn und navbar
    def button_opacity(self):
        self.ids.startbtn.opacity = 0 # Startbtn unsichtbar
        self.ids.startbtn.disabled = True # Startbtn deaktivieren
        self.ids.startseite.disabled = True # Navbar ausschalten
        self.ids.close_btn.opacity = 1 # Close Button anzeigen
        self.ids.rechnung.opacity = 1 # Rechnung auf 1 setzen
        self.ids.btn1.opacity = 1
        self.ids.btn1.disabled = False
        self.ids.btn2.opacity = 1
        self.ids.btn2.disabled = False
        self.ids.btn3.opacity = 1
        self.ids.btn3.disabled = False
        self.ids.counter_richtig.opacity =1
        self.ids.counter_falsch.opacity =1
        self.rechnung_erzeugen()
      
        
    # Methode für den Schließen btn. Setzt den Closebtn auf 0, Den Tab Startseite auf wählbar, und den Startbtn auf Sichtbar
    def close_btn(self):
        self.ids.close_btn.opacity = 0 # Close Btn ausblenden
        self.ids.startseite.disabled = False # Navbar freischalten
        self.ids.startbtn.opacity = 1 # Startbtn anzeigen
        self.ids.startbtn.disabled = False
        self.ids.rechnung.opacity = 0 # Rechnung ausblenden
        self.ids.btn1.opacity = 0 
        self.ids.btn1.disabled = True
        self.ids.btn2.opacity = 0
        self.ids.btn2.disabled = True
        self.ids.btn3.opacity = 0
        self.ids.btn3.disabled = True
        self.ids.counter_richtig.opacity =0
        self.ids.counter_falsch.opacity =0
        
      
        
    #Erstellen der Random Rechnungen
    def rechnung_erzeugen(self):
        try:
            rnum1 = random.randint(6,45)
            rnum2 = random.randint(1,45)
            nummin = min(rnum1,rnum2)
            nummax = max(rnum1, rnum2)
            oper = random.choice(['+','-'])
            if oper == '+':
                self.correct_answer = nummin + nummax
                self.ids.rechnung.text = f'{rnum1} + {rnum2}'
 
            elif oper == '-':
                self.correct_answer = nummax - nummin
                self.ids.rechnung.text = f'{rnum2} - {rnum1}'
         
                
            falsch1 = self.correct_answer + random.randint(1,6) 
            falsch2 = self.correct_answer - random.randint(1,6)
            while falsch1 == self.correct_answer:
                falsch1 = self.correct_answer + random.randint(1,6)
            while falsch2==self.correct_answer or falsch2==falsch1:
                falsch2 = self.correct_answer-random.randint(1,6)
            ergebnisse = [self.correct_answer, falsch1,falsch2]
            random.shuffle(ergebnisse)
            self.ids.btn1.text = str(ergebnisse[0])
            self.ids.btn2.text = str(ergebnisse[1])
            self.ids.btn3.text = str(ergebnisse[2])
             
            
        except ValueError:
            print('Error')
            
    def check_answer(self, btn_text):
        if self.correct_answer == int(btn_text):
            self.counter += 1
            self.ids.counter_richtig.text = f'Richtige: {self.counter}'
            
            self.rechnung_erzeugen()
            
        else:
            self.counter_falsch += 1
            self.ids.counter_falsch.text = f'Falsch: {self.counter_falsch}'
            
            
            

    
class WindowManager(MDScreenManager):
    pass
    
    
class MyApp(MDApp):
    def build(self):
        self.theme_cls.theme_style ="Dark"
        self.theme_cls.primary_palette ="Red"
        return Builder.load_file("selber.kv")
        
if __name__ == "__main__":
    MyApp().run()
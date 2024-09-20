from kivymd.app import MDApp 
from kivy.lang import Builder 
from kivymd.uix.screenmanager import MDScreenManager
from kivymd.uix.screen import MDScreen
import random as rnd

class FirstWindow(MDScreen):
    pass
    
class SecondWindow(MDScreen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.counter_right = 0
        self.counter_false = 0
    def rechnung(self):
        self.ids.btn_start.opacity = 0 # setzt den Btn nach klicken auf unsichtbar
        if self.ids.btn_start.opacity == 0:
            self.rechnung_erzeugen()
            self.button_ergebnis()
            
    def rechnung_erzeugen(self):
        #Das Label in der Card sichtbar machen
        self.ids.label_ueberschrift.opacity = 1
        self.ids.rechnung.opacity = 1
        self.ids.btn1.opacity = 1
        self.ids.btn2.opacity = 1
        self.ids.btn3.opacity = 1
        self.ids.counter.opacity = 1
        self.ids.counterf.opacity = 1
        #Random Nummern erzeugen
        self.num1 = int(rnd.randint(1,50))
        self.num2 = int(rnd.randint(1,50))
        self.nummin = min(self.num1,self.num2)
        self.nummax = max(self.num1,self.num2)
        self.operator = rnd.choice(['+', '-'])
        if self.operator == '+':
            
            self.ergebnis = self.nummin + self.nummax
            self.ids.rechnung.text = f"{self.nummin} {self.operator} {self.nummax}"
            
        elif self.operator == "-":
            self.ergebnis = self.nummax - self.nummin
            self.ids.rechnung.text = f"{self.nummax} {self.operator} {self.nummin}"
            
    def button_ergebnis(self):
            
            self.btnl = self.ids.btn1
            self.btnm = self.ids.btn2
            self.btnr = self.ids.btn3
            falsche1 =self.ergebnis + rnd.randint(1,5)
            falsche2 = self.ergebnis - rnd.randint(1,5)
            antworten=[self.ergebnis, falsche1,falsche2]
            rnd.shuffle(antworten)
            self.btnl.text = str(antworten[0])
            self.btnm.text = str(antworten[1])
            self.btnr.text = str(antworten[2])
            
    def check_answer(self, instance):
      
        ergebnis = str(self.ergebnis)  # Das Ergebnis in einen String umwandeln
        if instance.text == ergebnis:
            self.ids.label_ergebnis.text = 'Richtig!'
            self.counter_right += 1
            self.rechnung_erzeugen()
            self.button_ergebnis()
            self.ids.counter.text = f'Richtige {self.counter_right}'
        else:
            self.ids.label_ergebnis.text = 'Falsch!'
            self.counter_false += 1
            self.ids.counterf.text = f'Falsche : {self.counter_false}'
        self.ids.label_ergebnis.opacity = 1  # Label sichtbar machen
            
            

            
            
            
            
        
    
class WindowManager(MDScreenManager):
        pass
        
class MainApp(MDApp):
    def build(self):
        self.theme_cls.primary_palette = "Cyan"
        self.theme_cls.accent_palette = "Yellow"
        
        self.theme_cls.theme_style ="Dark"
        return Builder.load_file("selber.kv")
        
MainApp().run()
import tkinter as tk

class App(tk.Frame):
    def __init__(self, parent=None, operando1=0, operando2=0, operador="", resultado=0):
        tk.Frame.__init__(self, parent)
        self.parent     = parent
        self.operando1  = operando1
        self.operando2  = operando2
        self.operador   = operador
        self.resultado  = resultado
        self.display    = tk.Entry(self.parent, text="Display", justify=tk.RIGHT)
        self.init_ui()

    def init_ui(self):
        self.parent.title("Calc")
        self.parent.resizable(width=False, height=False)
        # Definiendo el display ("Pantalla")
        self.display.place(x = 2, y = 0, width = 294, height = 40)
        # Definiendo los botones
        #!PRIMERA FILA
        boton_c             = tk.Button(self.parent, text="C", command = lambda: self.limpiaDisplay())
        boton_mas_menos     = tk.Button(self.parent, text="+/-", command = lambda: self.cambiaSigno())
        boton_porcentaje    = tk.Button(self.parent, text="%", command = lambda: self.porcentaje())
        boton_division      = tk.Button(self.parent, text="÷", command = lambda: self.operadorPulsado("÷"))
        #!SEGUNDA FILA
        boton_siete         = tk.Button(self.parent, text="7", command = lambda: self.addNumber("7"))
        boton_ocho          = tk.Button(self.parent, text="8", command = lambda: self.addNumber("8"))
        boton_nueve         = tk.Button(self.parent, text="9", command = lambda: self.addNumber("9"))
        boton_multiplica    = tk.Button(self.parent, text="x", command = lambda: self.operadorPulsado("x"))
        #!TERCERA FILA
        boton_cuatro        = tk.Button(self.parent, text="4", command = lambda: self.addNumber("4"))
        boton_cinco         = tk.Button(self.parent, text="5", command = lambda: self.addNumber("5"))
        boton_seis          = tk.Button(self.parent, text="6", command = lambda: self.addNumber("6"))
        boton_restar        = tk.Button(self.parent, text="-", command = lambda: self.operadorPulsado("-"))
        #!CUARTA FILA
        boton_uno           = tk.Button(self.parent, text="1", command = lambda: self.addNumber("1"))
        boton_dos           = tk.Button(self.parent, text="2", command = lambda: self.addNumber("2"))
        boton_tres          = tk.Button(self.parent, text="3", command = lambda: self.addNumber("3"))
        boton_suma          = tk.Button(self.parent, text="+", command = lambda: self.operadorPulsado("+"))
        #!QUINTA FILA
        boton_cero          = tk.Button(self.parent, text="0", command = lambda: self.addNumber("0"))
        boton_coma          = tk.Button(self.parent, text=",", command = lambda: self.display.insert(tk.END, "."))
        boton_igual         = tk.Button(self.parent, text="=", command = lambda: self.opera())

        # Colocando los widgets
        #!PRIMERA FILA
        boton_c.place(x = 13, y = 60, width=60, height=56)
        boton_mas_menos.place(x = 85, y = 60, width=60, height=56)
        boton_porcentaje.place(x = 157, y = 60, width=60, height=56)
        boton_division.place(x = 227, y = 60, width=60, height=56)
        #!SEGUNDA FILA
        boton_siete.place(x = 13, y = 122, width=60, height=56)
        boton_ocho.place(x = 85, y = 122, width=60, height=56)
        boton_nueve.place(x = 157, y = 122, width=60, height=56)
        boton_multiplica.place(x = 227, y = 122, width=60, height=56)
        #!TERCERA FILA
        boton_cuatro.place(x = 13, y = 184, width=60, height=56)
        boton_cinco.place(x = 85, y = 184, width=60, height=56)
        boton_seis.place(x = 157, y = 184, width=60, height=56)
        boton_restar.place(x = 227, y = 184, width=60, height=56)
        #!QUINTA FILA
        boton_uno.place(x = 13, y = 246, width=60, height=56)
        boton_dos.place(x = 85, y = 246, width=60, height=56)
        boton_tres.place(x = 157, y = 246, width=60, height=56)
        boton_suma.place(x = 227, y = 246, width=60, height=56)
        #!SEXTA FILA
        boton_cero.place(x = 13, y = 308, width = 132, height = 56)
        boton_coma.place(x = 157, y = 308, width=60, height=56)
        boton_igual.place(x = 227, y = 308, width=60, height=56)

    def addNumber(self, n):
        if self.resultado != 0:
            self.resultado = 0
            self.display.delete(0, "end")
        self.display.insert(tk.END, n)

    def operadorPulsado(self, operador):
        #Primero leemos el primer operando que tenemos
        self.operando1 = float(self.display.get())
        # Asignamos el operador
        self.operador = operador;
        # Borramos lo que hay en el display
        self.display.delete(0, "end")

    def cambiaSigno(self):
        self.operando1 = float(self.display.get())
        self.resultado = -self.operando1
        self.display.delete(0, "end")
        self.display.insert(0, str(self.resultado))
        self.operando1 = 0

    def limpiaDisplay(self):
        self.display.delete(0, "end")
        self.operando1 = 0
        self.operando2 = 0
        self.resultado = 0

    def porcentaje(self):
        if self.resultado != 0:
            self.resultado = 0
            self.display.delete(0, "end")
        self.operador1 = int(self.display.get())
        self.resultado = self.operando1 / 100
        resultado = str(self.resultado)
        self.display.insert(0, resultado)
        self.operando1 = 0
        self.operando2 = 0
        self.resultado = 0

    def opera(self):
        self.operando2 = float(self.display.get())
        self.display.delete(0, "end")
        if self.operador == "+":
            self.resultado = self.operando1 + self.operando2
            resultado = str(self.resultado)
            self.display.insert(0, resultado)
        elif self.operador == "-":
            self.resultado = self.operando1 - self.operando2
            resultado = str(self.resultado)
            self.display.insert(0, resultado)
        elif self.operador == "÷":
            self.resultado = self.operando1 / self.operando2
            resultado = str(self.resultado)
            self.display.insert(0, resultado)
        elif self.operador == "x":
            self.resultado = self.operando1 * self.operando2
            resultado = str(self.resultado)
            self.display.insert(0, resultado)

        self.operando1 = 0
        self.operando2 = 0


if __name__ == "__main__":
    root = tk.Tk()
    root.geometry("300x400")
    app = App(root)
    app.mainloop()

import tkinter as tk

#définition des constantes pour le style 
LARGE_FONT_STYLE = ("Arial", 40, "bold")
SMALL_FONT_STYLE = ("Arial", 16 )
DIGIT_FONT_STYLE = ("Arial", 24, "bold")
DEFAULT_FONT_STYLE =("Arial", 20)

OFF_WHITE = "#F8FAFF"
LIGHT_GRAY = "#F5F5F5"
LABEL_COLOR = "#25265E"
WHITE = "#FFFFFF"
LIGHT_BLUE = "#CCEDFF"

#création de la class calculatrice et de l'interface graphique utilisant tk 
class Calculator:
    def __init__(self):
        self.window = tk.Tk()
        self.window.geometry("375x667")
        self.window.resizable(0, 0)
        self.window.title("Calculatrice")
        
        self.total_expression = ""
        self.current_expression = ""
        self.display_frame = self.create_display_frame()
        self.total_label, self.label = self.create_display_labels()
        
        self.digits = {
            7:(1,1), 8:(1,2), 9:(1,3),
            4:(2,1), 5:(2,2), 6:(2,3),
            1:(3,1), 2:(3,2), 3:(3,3),
            0:(4,2),'.':(4,1)
        }
        self.operations = {"/":"\u00F7", "*":"\u00D7", "-":"-", "+":"+"
        }
        self.buttons_frame = self.create_buttons_frame()
        
        self.buttons_frame.rowconfigure(0, weight=1)
  
        for x in range(1, 5):
            self.buttons_frame.rowconfigure(x, weight=1)
            self.buttons_frame.columnconfigure(x, weight=1)

        self.create_digit_buttons()
        self.create_operators_buttons()
        self.create_special_buttons()
        
        #opérandes spéciales, nécessitants des ajustements spécifique
    def create_special_buttons(self):
        self.create_clear_button()
        self.create_equals_button()
        self.create_square_button()
        self.create_sqrt_button()
        
        #crée les étiquettes d'affichage pour l'expression totale et l'expression actuelle en créant deux objets tk.label 
        #qui afficheront les expressions, proprotions couleurs etc...
    def create_display_labels(self):
        total_label = tk.Label(self.display_frame, text = self.total_expression, anchor = tk.E, bg=LIGHT_GRAY, 
                               fg=  LABEL_COLOR, padx=24, font=SMALL_FONT_STYLE)
        total_label.pack(expand=True, fill="both")
        
        label = tk.Label(self.display_frame, text = self.current_expression, anchor = tk.E, bg=LIGHT_GRAY, 
                               fg=  LABEL_COLOR, padx=24, font=LARGE_FONT_STYLE)
        label.pack(expand=True, fill="both")
        
        return total_label, label
    # contient les étiquettes d'affichage, proportions couleurs etc...
    def create_display_frame(self):
        frame = tk.Frame(self.window, height=221, bg=LIGHT_GRAY)
        frame.pack(expand=True, fill ="both")
        return frame
    
    #ajoute des caracteres a l'expression en cour, prend en entrée nombre ou opérations, met a jour 'affichage avec update label
    def add_to_expression(self, value):
        self.current_expression += str(value)
        self.update_label()
    
    #créations des boutons pour les chiffres
    def create_digit_buttons(self):
        for digit, grid_value in self.digits.items():
            button = tk.Button(self.buttons_frame, text=str(digit), bg= WHITE, fg=LABEL_COLOR, font=DIGIT_FONT_STYLE,
                               borderwidth=0, command=lambda x=digit: self.add_to_expression(x))
            button.grid(row=grid_value[0], column=grid_value[1], sticky=tk.NSEW)
           
    #rajoute opérateur  a l'expression actuelle puis l'expression actuelle a l'expression totale
    #puis met a jour les affichages 
    def append_operator(self, operator):
        self.current_expression += operator
        self.total_expression += self.current_expression
        self.current_expression = ""
        self.update_total_label()
        self.update_label
        
    #création des boutons pour les opérandes, les définit en tant que commande
    def create_operators_buttons(self):
        i = 0
        for operator, symbol in self.operations.items():
            button = tk.Button(self.buttons_frame, text=symbol, bg=OFF_WHITE, fg=LABEL_COLOR, font=DEFAULT_FONT_STYLE,
                               borderwidth=0, command=lambda x=operator: self.append_operator(x))
            button.grid(row = i, column=4, sticky=tk.NSEW)
            i += 1
    #bouton clear qui permet d'effacer l'affichage
    def clear(self):
        self.current_expression = ""
        self.total_expression = ""
        self.update_label()
        self.update_total_label()
        
    def create_clear_button(self):
        button = tk.Button(self.buttons_frame, text="C", bg=OFF_WHITE, fg=LABEL_COLOR, font=DEFAULT_FONT_STYLE,
                               borderwidth=0, command=self.clear)
        button.grid(row = 0, column=1, sticky=tk.NSEW)
        
    #défini le carré
    def square(self):
        self.current_expression = str(eval(f"{self.current_expression}**2"))
        self.update_label()
           
    
    def create_square_button(self):
        button = tk.Button(self.buttons_frame, text="x\u00b2", bg=OFF_WHITE, fg=LABEL_COLOR, font=DEFAULT_FONT_STYLE,
                               borderwidth=0, command=self.square)
        button.grid(row = 0, column=2,  sticky=tk.NSEW)
    
    #défini la racine carrée
    def sqrt(self):
        self.current_expression = str(eval(f"{self.current_expression}**0.5"))
        self.update_label()
    
    def create_sqrt_button(self):
        button = tk.Button(self.buttons_frame, text="x\u221a", bg=OFF_WHITE, fg=LABEL_COLOR, font=DEFAULT_FONT_STYLE,
                               borderwidth=0, command=self.sqrt)
        button.grid(row = 0, column=3,  sticky=tk.NSEW)
        
    
    #évalue l'expression mathématique dans la calcultraice, utilise la fonction built-in-eval
    # gère l'erreur 
    # actualise
    def evaluate(self):
        self.total_expression += self.current_expression
        self.update_label()
        try: 
            self.current_expression = str(eval(self.total_expression))
         
            self.total_expression = ""
        except Exception as e:
            self.current_expression = "Error"
        finally:
            self.update_label()
            
    #boutons égal
    def create_equals_button(self):
        button = tk.Button(self.buttons_frame, text="=", bg=LIGHT_BLUE, fg=LABEL_COLOR, font=DEFAULT_FONT_STYLE,
                               borderwidth=0, command=self.evaluate)
        button.grid(row = 4, column=3, columnspan=2, sticky=tk.NSEW)
        
    def create_buttons_frame(self):
        frame = tk.Frame(self.window)
        frame.pack(expand = True, fill = "both")
        return frame 
        
    #met a jour l'affichage des opératons 
    def update_total_label(self):
        expression = self.total_expression
        for operator, symbol in self.operations.items():
            expression = expression.replace(operator, f' {symbol} ')
        self.total_label.config(text=expression)
        
    #limite le nombre d'affichage des chiffres afin de rester cohérent avec l'interface graphique
    def update_label(self):
        self.label.config(text=self.current_expression[:11])
        
        
    def run(self):
        self.window.mainloop()
        
if __name__ == "__main__":
    calc = Calculator()
    calc.run()
       
 
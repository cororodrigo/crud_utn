import vista
import tkinter as tk
import observa  

  

class inicio():
    def __init__ (self,root):
        self.root = vista.home_app(root)
        self.observer = observa.ConcreteObserverA(
            self.root.dbase_operativo
            )

if __name__ == "__main__":
    root = tk.Tk()
    vista = inicio(root)
      
    root.mainloop()

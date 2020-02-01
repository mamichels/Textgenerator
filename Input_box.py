import tkinter as tk
from tkinter import ttk


def formular_window():
    window = tk.Tk()  # hier ist das reine fenster
    window.title('Genereller Überblick')
    window.geometry("960x480")  # Fenster Größe: Breite x Höhe

    generalInput = {}  # der Beginn vom Input

    tab_parent = ttk.Notebook(window)
    head = ttk.Frame(tab_parent)
    body = ttk.Frame(tab_parent)
    lung = ttk.Frame(tab_parent)
    recommendation = ttk.Frame(tab_parent)
    result = ttk.Frame(tab_parent)

    tab_parent.add(head, text="Kopf")
    tab_parent.add(body, text="Rumpf")
    tab_parent.add(lung, text="Lunge")
    tab_parent.add(recommendation, text="Empfehlungen")
    tab_parent.add(result, text="Ergebnis")

    # here widgets for Tab 1
    text1_1_2 = tk.Label(head, text="Allgemeinzustand:")
    text1_1_2.grid(row=0, column=0, padx=15, pady=15)

    text1_1_3 = tk.Label(head, text="Ernährungszustand:")
    text1_1_3.grid(row=0, column=2, padx=15, pady=15)

    # erster Radiobutton --> Allgemeinzustande
    generalConditionValue = tk.IntVar()
    generalConditionValue.set(3)  # intialisierung der allgemeinzustandsvariabeln
    generalConditionInput = [("gutem", 0), ("reduzierten", 1), ("leicht reduziertem", 2), ("leer", 3)]
    generateRadiobutton(generalConditionInput, head, generalConditionValue, 0, 1)
    generalInput.update({"Allgemeinzustand" : generalConditionValue})

    nutritionalStateValue = tk.IntVar()
    nutritionalStateValue.set(3)
    nutritionalStateInput = [("eutrophen", 0), ("dystrophen", 1), ("adipösen", 2), ("leer", 3)]
    generateRadiobutton(nutritionalStateInput, head, nutritionalStateValue, 0, 3)
    generalInput.update({"Ernaehrungszustand": nutritionalStateValue})

    txt1_2_1 = tk.Label(head, text="Mundschleimhäute:")
    txt1_2_1.grid(row=4, column=0, padx=15, pady=15)
    moistDryValue = tk.IntVar()
    moistDry = [("feucht", 1), ("trocken", 2)]
    generateRadiobutton(moistDry, head, moistDryValue, 4, 0)

    # here widgets for Tab 2

    # here widgets for Tab 3

    # here widgets for Tab 4

    # here widgets for Tab 5 = result and generated output based on previously selected options
    #resultString = str(generalConditionValue) + " " + str(nutritionalStateValue)
    resultValue = tk.StringVar()
    resultValue.set('')
    e1 = tk.Entry(result)
    resultBox = tk.Text(result, "", height=20, width=40).grid(row=2, column=2, padx=10, pady=5, sticky=tk.W)
    #generalInput.update({"Zusätzliche Ergebnisse" : resultValue})

    #generalInput.update({"ErgebnisZusatz" : resultValue})
    # buttons
    next1 = tk.Button(head, text="Next", command=next)
    next1.grid(row=4, column=8, padx=10, pady=10)


    back2 = tk.Button(body, text="Back")
    back2.grid(row=4, column=1, padx=10, pady=10)
    next2 = tk.Button(body, text="Next")
    next2.grid(row=4, column=8, padx=10, pady=10)

    back3 = tk.Button(lung, text="Back")
    back3.grid(row=4, column=1, padx=10, pady=10)
    next3 = tk.Button(lung, text="Next")
    next3.grid(row=4, column=8, padx=10, pady=10)

    back4 = tk.Button(recommendation, text="Back")
    back4.grid(row=4, column=1, padx=10, pady=10)
    next4 = tk.Button(recommendation, text="Next")
    next4.grid(row=4, column=8, padx=10, pady=10)

    button_OK = tk.Button(result, text="OK", command=lambda: ok(generalInput))
    button_OK.grid(row=4, column=8, padx=10, pady=10)
    back5 = tk.Button(result, text="Back")
    back5.grid(row=4, column=1, padx=10, pady=10)

    tab_parent.pack(expand=1, fill="both")

    window.mainloop()

def ok(generalInput):
    generalInput["Allgemeinzustand"] = generalInput["Allgemeinzustand"].get()
    generalInput["Ernaehrungszustand"] = generalInput["Ernaehrungszustand"].get()
    #generalInput["Zusätzliche Ergebnisse"] = generalInput["Zusätzliche Ergebnisse"].get("1.0","end-1c")
    return print(generalInput)

def generateRadiobutton(InputArray, tabName, variable, row, column):
    if column == 0:
        for text, val in InputArray:
            tk.Radiobutton(tabName, text=text, padx=5, variable=variable, value=val).grid(row=row, column=val, padx=5,
                                                                                          pady=5, sticky=tk.W)
    elif row == 0:
        for text, val in InputArray:
            tk.Radiobutton(tabName, text=text, padx=5, variable=variable, value=val).grid(row=val, column=column, padx=5,
                                                                                          pady=5, sticky=tk.W)

def next():
    #tabID = notebook.select(tab_id)
    print("you pressed next?")

#    print("new content will be available soon :D")


if __name__ == '__main__':
    formular_window()
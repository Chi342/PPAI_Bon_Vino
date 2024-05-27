import tkinter as tk

ventana = tk.Tk()
ventana.title('conversor')
ventana.geometry('400x550+700+100')
ventana.minsize(width=400, height=550)
ventana.configure(bg='wheat')


def enviar():
    pizza_elegida = opcion_seleccionada.get()
    if pizza_elegida == 1:
        resultado = 'Margarita'
    elif pizza_elegida == 2:
        resultado = 'Napolitana'
    else:
        resultado = 'No hay eleccion'
    rotulo_resultado.config(text=f'su pizza:\n{resultado}')
    boton_enviar['state']='disabled'

rotulo_titulo = tk.Label(ventana,
                        text='selector pizzas',
                        bg='wheat', fg='black',
                        font= 'consolas 20 bold',
                        relief = tk.GROOVE, bd=2,
                        width= 18, pady=10,)
rotulo_titulo.grid(row=0, column=0)

cuadro1 = tk.LabelFrame(ventana,
                        bg='wheat',
                        text='variedades',
                        font='arial 14 underline')

opcion_seleccionada = tk.IntVar()

opcion1 = tk.Radiobutton(cuadro1,
                         text='margarita',
                         bg='wheat',
                         font='consolas 16',
                         width=20, anchor=tk.W,
                         variable=opcion_seleccionada,
                         value=1)
opcion1.grid(row=1, column=0)

opcion2 = tk.Radiobutton(cuadro1,
                         text='barbacoa',
                         bg='wheat',
                         font='consolas 16',
                         width=20, anchor=tk.W,
                         variable=opcion_seleccionada,
                         value=1)
opcion2.grid(row=1, column=0)

print(opcion_seleccionada.get())
opcion_seleccionada.set(1)
print(opcion_seleccionada.get())
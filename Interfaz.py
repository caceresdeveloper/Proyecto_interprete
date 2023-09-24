import tkinter as tk
from tkinter import scrolledtext
import subprocess

def compilar():

     # Obtener el texto del cuadro editable
    codigo = cuadro_editable.get("1.0", tk.END)
    
    # Verificar si el código contiene la palabra clave "def" (indicativo de Ruby)
    if "def" in codigo:
        ejecutar_codigo_ruby(codigo)
    elif "function" in codigo:
        ejecutar_codigo_julia(codigo)
    else:
        ejecutar_codigo_perl(codigo)

# Función a ejecutar si se detecta código Ruby
def ejecutar_codigo_ruby(codigo):
     # Nombre del archivo
    archivo_nombre = "Codigo.txt"

    # Abrir el archivo en modo escritura para borrar el contenido anterior
    with open(archivo_nombre, "w") as archivo:
        archivo.write("")  # Borra todo el contenido del archivo

    # Luego, abre el archivo en modo escritura y agrega el nuevo contenido
    with open(archivo_nombre, "a") as archivo:
        archivo.write(codigo)
        
    # Ejecutar el archivo ruby_Interprete.py
    try:
        subprocess.run(["python", "ruby_Interprete.py"], check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error al ejecutar ruby_Interprete.py: {e}")
    else:
        print("Ejecución exitosa de ruby_Interprete.py")
        
    # Nombre del archivo
    salida = "Analizador_Lexico.txt"
    try:
        with open(salida, "r", encoding="utf-8") as archivo:
            contenido = archivo.read()
            cuadro_no_editable1.config(state="normal")  # Hacer que el cuadro no editable sea editable temporalmente
            cuadro_no_editable1.delete("1.0", tk.END)  # Limpiar el cuadro no editable
            cuadro_no_editable1.insert(tk.END, "Resultado de la compilación:\n")
            cuadro_no_editable1.insert(tk.END, f"Código compilado:\n{contenido}")
            cuadro_no_editable1.config(state="disabled")  # Deshabilitar el cuadro no editable nuevamente
            
    except FileNotFoundError:
        print(f"El archivo {salida} no se encontró.")
    except Exception as e:
        print("Ocurrió un error:", str(e))
        
        
    # Nombre del archivo
    salida2 = "Sintaxico.txt"
    try:
        with open(salida2, "r", encoding="utf-8") as archivo2:
            contenido1 = archivo2.read()
            cuadro_no_editable2.config(state="normal")  # Hacer que el cuadro no editable sea editable temporalmente
            cuadro_no_editable2.delete("1.0", tk.END)  # Limpiar el cuadro no editable
            cuadro_no_editable2.insert(tk.END, "Resultado de la compilación:\n")
            cuadro_no_editable2.insert(tk.END, f"Código compilado:\n{contenido1}")
            cuadro_no_editable2.config(state="disabled")  # Deshabilitar el cuadro no editable nuevamente
    except FileNotFoundError:
        print(f"El archivo {salida2} no se encontró.")
    except Exception as e:
        print("Ocurrió un error:", str(e))
        
    salida3 = "Semantico.txt"
    try:
        with open(salida3, "r", encoding="utf-8") as archivo3:
            contenido2 = archivo3.read()
            cuadro_no_editable3.config(state="normal")  # Hacer que el cuadro no editable sea editable temporalmente
            cuadro_no_editable3.delete("1.0", tk.END)  # Limpiar el cuadro no editable
            cuadro_no_editable3.insert(tk.END, "Resultado de la compilación:\n")
            cuadro_no_editable3.insert(tk.END, f"Código compilado:\n{contenido2}")
            cuadro_no_editable3.config(state="disabled")  # Deshabilitar el cuadro no editable nuevamente
    except FileNotFoundError:
        print(f"El archivo {salida3} no se encontró.")
    except Exception as e:
        print("Ocurrió un error:", str(e))


    salida4 = "salida.txt"
    try:
        with open(salida4, "r", encoding="utf-8") as archivo4:
            contenido3 = archivo4.read()
            cuadro_ejecucion.config(state="normal")  # Hacer que el cuadro no editable sea editable temporalmente
            cuadro_ejecucion.delete("1.0", tk.END)  # Limpiar el cuadro no editable
            cuadro_ejecucion.insert(tk.END, "Resultado de la compilación:\n")
            cuadro_ejecucion.insert(tk.END, f"Código compilado:\n{contenido3}")
            cuadro_ejecucion.config(state="disabled")  # Deshabilitar el cuadro no editable nuevamente
    except FileNotFoundError:
        print(f"El archivo {salida4} no se encontró.")
    except Exception as e:
        print("Ocurrió un error:", str(e))


# Función a ejecutar si se detecta código Perl
def ejecutar_codigo_perl(codigo):
     # Nombre del archivo
    archivo_nombre = "CodigoP.txt"

    # Abrir el archivo en modo escritura para borrar el contenido anterior
    with open(archivo_nombre, "w") as archivo:
        archivo.write("")  # Borra todo el contenido del archivo

    # Luego, abre el archivo en modo escritura y agrega el nuevo contenido
    with open(archivo_nombre, "a") as archivo:
        archivo.write(codigo)
        
    # Ejecutar el archivo ruby_Interprete.py
    try:
        subprocess.run(["python", "perl_Interprete.py"], check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error al ejecutar perl_Interprete.py: {e}")
    else:
        print("Ejecución exitosa de perl_Interprete.py")
        
    # Nombre del archivo
    salida = "Analizador_LexicoP.txt"
    try:
        with open(salida, "r", encoding="utf-8") as archivo:
            contenido = archivo.read()
            cuadro_no_editable1.config(state="normal")  # Hacer que el cuadro no editable sea editable temporalmente
            cuadro_no_editable1.delete("1.0", tk.END)  # Limpiar el cuadro no editable
            cuadro_no_editable1.insert(tk.END, "Resultado de la compilación:\n")
            cuadro_no_editable1.insert(tk.END, f"Código compilado:\n{contenido}")
            cuadro_no_editable1.config(state="disabled")  # Deshabilitar el cuadro no editable nuevamente
            
    except FileNotFoundError:
        print(f"El archivo {salida} no se encontró.")
    except Exception as e:
        print("Ocurrió un error:", str(e))
        
        
    # Nombre del archivo
    salida2 = "SintaxicoP.txt"
    try:
        with open(salida2, "r", encoding="utf-8") as archivo2:
            contenido1 = archivo2.read()
            cuadro_no_editable2.config(state="normal")  # Hacer que el cuadro no editable sea editable temporalmente
            cuadro_no_editable2.delete("1.0", tk.END)  # Limpiar el cuadro no editable
            cuadro_no_editable2.insert(tk.END, "Resultado de la compilación:\n")
            cuadro_no_editable2.insert(tk.END, f"Código compilado:\n{contenido1}")
            cuadro_no_editable2.config(state="disabled")  # Deshabilitar el cuadro no editable nuevamente
    except FileNotFoundError:
        print(f"El archivo {salida2} no se encontró.")
    except Exception as e:
        print("Ocurrió un error:", str(e))
        
    salida3 = "SemanticoP.txt"
    try:
        with open(salida3, "r", encoding="utf-8") as archivo3:
            contenido2 = archivo3.read()
            cuadro_no_editable3.config(state="normal")  # Hacer que el cuadro no editable sea editable temporalmente
            cuadro_no_editable3.delete("1.0", tk.END)  # Limpiar el cuadro no editable
            cuadro_no_editable3.insert(tk.END, "Resultado de la compilación:\n")
            cuadro_no_editable3.insert(tk.END, f"Código compilado:\n{contenido2}")
            cuadro_no_editable3.config(state="disabled")  # Deshabilitar el cuadro no editable nuevamente
    except FileNotFoundError:
        print(f"El archivo {salida3} no se encontró.")
    except Exception as e:
        print("Ocurrió un error:", str(e))


    salida4 = "salidaP.txt"
    try:
        with open(salida4, "r", encoding="utf-8") as archivo4:
            contenido3 = archivo4.read()
            cuadro_ejecucion.config(state="normal")  # Hacer que el cuadro no editable sea editable temporalmente
            cuadro_ejecucion.delete("1.0", tk.END)  # Limpiar el cuadro no editable
            cuadro_ejecucion.insert(tk.END, "Resultado de la compilación:\n")
            cuadro_ejecucion.insert(tk.END, f"Código compilado:\n{contenido3}")
            cuadro_ejecucion.config(state="disabled")  # Deshabilitar el cuadro no editable nuevamente
    except FileNotFoundError:
        print(f"El archivo {salida4} no se encontró.")
    except Exception as e:
        print("Ocurrió un error:", str(e))
        
def ejecutar_codigo_julia(codigo):
     # Nombre del archivo
    archivo_nombre = "CodigoJ.txt"

    # Abrir el archivo en modo escritura para borrar el contenido anterior
    with open(archivo_nombre, "w") as archivo:
        archivo.write("")  # Borra todo el contenido del archivo

    # Luego, abre el archivo en modo escritura y agrega el nuevo contenido
    with open(archivo_nombre, "a") as archivo:
        archivo.write(codigo)
        
    # Ejecutar el archivo ruby_Interprete.py
    try:
        subprocess.run(["python", "julia_interprete.py"], check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error al ejecutar julia_interprete.py: {e}")
    else:
        print("Ejecución exitosa de julia_interprete.py")
        
    # Nombre del archivo
    salida = "Analizador_Lexicoj.txt"
    try:
        with open(salida, "r", encoding="utf-8") as archivo:
            contenido = archivo.read()
            cuadro_no_editable1.config(state="normal")  # Hacer que el cuadro no editable sea editable temporalmente
            cuadro_no_editable1.delete("1.0", tk.END)  # Limpiar el cuadro no editable
            cuadro_no_editable1.insert(tk.END, "Resultado de la compilación:\n")
            cuadro_no_editable1.insert(tk.END, f"Código compilado:\n{contenido}")
            cuadro_no_editable1.config(state="disabled")  # Deshabilitar el cuadro no editable nuevamente
            
    except FileNotFoundError:
        print(f"El archivo {salida} no se encontró.")
    except Exception as e:
        print("Ocurrió un error:", str(e))
        
        
    # Nombre del archivo
    salida2 = "Sintaxicoj.txt"
    try:
        with open(salida2, "r", encoding="utf-8") as archivo2:
            contenido1 = archivo2.read()
            cuadro_no_editable2.config(state="normal")  # Hacer que el cuadro no editable sea editable temporalmente
            cuadro_no_editable2.delete("1.0", tk.END)  # Limpiar el cuadro no editable
            cuadro_no_editable2.insert(tk.END, "Resultado de la compilación:\n")
            cuadro_no_editable2.insert(tk.END, f"Código compilado:\n{contenido1}")
            cuadro_no_editable2.config(state="disabled")  # Deshabilitar el cuadro no editable nuevamente
    except FileNotFoundError:
        print(f"El archivo {salida2} no se encontró.")
    except Exception as e:
        print("Ocurrió un error:", str(e))
        
    salida3 = "Semanticoj.txt"
    try:
        with open(salida3, "r", encoding="utf-8") as archivo3:
            contenido2 = archivo3.read()
            cuadro_no_editable3.config(state="normal")  # Hacer que el cuadro no editable sea editable temporalmente
            cuadro_no_editable3.delete("1.0", tk.END)  # Limpiar el cuadro no editable
            cuadro_no_editable3.insert(tk.END, "Resultado de la compilación:\n")
            cuadro_no_editable3.insert(tk.END, f"Código compilado:\n{contenido2}")
            cuadro_no_editable3.config(state="disabled")  # Deshabilitar el cuadro no editable nuevamente
    except FileNotFoundError:
        print(f"El archivo {salida3} no se encontró.")
    except Exception as e:
        print("Ocurrió un error:", str(e))


    salida4 = "salidaJ.txt"
    try:
        with open(salida4, "r", encoding="utf-8") as archivo4:
            contenido3 = archivo4.read()
            cuadro_ejecucion.config(state="normal")  # Hacer que el cuadro no editable sea editable temporalmente
            cuadro_ejecucion.delete("1.0", tk.END)  # Limpiar el cuadro no editable
            cuadro_ejecucion.insert(tk.END, "Resultado de la compilación:\n")
            cuadro_ejecucion.insert(tk.END, f"Código compilado:\n{contenido3}")
            cuadro_ejecucion.config(state="disabled")  # Deshabilitar el cuadro no editable nuevamente
    except FileNotFoundError:
        print(f"El archivo {salida4} no se encontró.")
    except Exception as e:
        print("Ocurrió un error:", str(e))


def limpiar():
    cuadro_editable.delete("1.0", tk.END)  # Limpiar el cuadro editable


def limpiar_todo():
    # Nombre del archivo
    archivo_nombre = "Codigo.txt"
    
    with open(archivo_nombre, "w") as archivo:
        archivo.write("")  # Borra todo el contenido del archivo
        
    archivo_nombre = "Analizador_Lexico.txt"
    
    with open(archivo_nombre, "w") as archivo:
        archivo.write("")  # Borra todo el contenido del archivo
        
    salida2 = "Sintaxico.txt"
    with open(salida2, "w") as archivo:
        archivo.write("")  # Borra todo el contenido del archivo
        
    salida3 = "Semantico.txt"
    with open(salida3, "w") as archivo:
        archivo.write("")  # Borra todo el contenido del archivo
        
    salida4 = "salida.txt"
    with open(salida4, "w") as archivo:
        archivo.write("")  # Borra todo el contenido del archivo
    
    with open("codigo_ruby.rb", "w") as archivo:
        # Escribe una cadena vacía para eliminar el contenido
        archivo.write("")
        
    # Nombre del archivo
    archivo_nombre = "CodigoP.txt"
    
    with open(archivo_nombre, "w") as archivo:
        archivo.write("")  # Borra todo el contenido del archivo
        
    archivo_nombre = "Analizador_LexicoP.txt"
    
    with open(archivo_nombre, "w") as archivo:
        archivo.write("")  # Borra todo el contenido del archivo
        
    salida2 = "SintaxicoP.txt"
    with open(salida2, "w") as archivo:
        archivo.write("")  # Borra todo el contenido del archivo
        
    salida3 = "SemanticoP.txt"
    with open(salida3, "w") as archivo:
        archivo.write("")  # Borra todo el contenido del archivo
        
    salida4 = "salidaP.txt"
    with open(salida4, "w") as archivo:
        archivo.write("")  # Borra todo el contenido del archivo
    
    with open("codigo_perl.pl", "w") as archivo:
        # Escribe una cadena vacía para eliminar el contenido
        archivo.write("")
        
    cuadro_editable.delete("1.0", tk.END)
    cuadro_no_editable1.config(state="normal")
    cuadro_no_editable1.delete("1.0", tk.END)
    cuadro_no_editable1.config(state="disabled")
    cuadro_no_editable2.config(state="normal")
    cuadro_no_editable2.delete("1.0", tk.END)
    cuadro_no_editable2.config(state="disabled")
    cuadro_no_editable3.config(state="normal")
    cuadro_no_editable3.delete("1.0", tk.END)
    cuadro_no_editable3.config(state="disabled")
    cuadro_ejecucion.config(state="normal")
    cuadro_ejecucion.delete("1.0", tk.END)
    cuadro_ejecucion.config(state="disabled")

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Compilador")
ventana.geometry("1300x700")  # Tamaño de la ventana

# Configurar el fondo de la ventana en azul claro
ventana.configure(bg="#314c53")

# Dividir la ventana en dos secciones usando Frames
frame_izquierda = tk.Frame(ventana, bg="#49708a")
frame_izquierda.grid(row=0, column=0, padx=10, pady=10, rowspan=5)

frame_derecha = tk.Frame(ventana, bg="#49708a")
frame_derecha.grid(row=0, column=1, padx=10, pady=10, rowspan=5)

# Cuadros de texto en la sección izquierda (2 arriba, 2 abajo)
etiqueta_editable = tk.Label(frame_izquierda, text="Ingresa Tu Codigo" ,bg="#49708a", fg="white")
etiqueta_editable.grid(row=0, column=0, padx=10, pady=(10, 5), sticky="w")

cuadro_editable = scrolledtext.ScrolledText(frame_izquierda, wrap=tk.WORD, height=20, width=50)
cuadro_editable.grid(row=1, column=0, padx=10, pady=5)

etiqueta_no_editable1 = tk.Label(frame_izquierda, text="Analizador Lexico" ,bg="#49708a", fg="white")
etiqueta_no_editable1.grid(row=0, column=1, padx=10, pady=(10, 5), sticky="w")

cuadro_no_editable1 = scrolledtext.ScrolledText(frame_izquierda, wrap=tk.WORD, height=20, width=50, state="disabled")
cuadro_no_editable1.grid(row=1, column=1, padx=10, pady=5)

etiqueta_no_editable2 = tk.Label(frame_izquierda, text="Analizador Sintáctico" ,bg="#49708a", fg="white")
etiqueta_no_editable2.grid(row=2, column=0, padx=10, pady=(10, 5), sticky="w")

cuadro_no_editable2 = scrolledtext.ScrolledText(frame_izquierda, wrap=tk.WORD, height=20, width=50, state="disabled")
cuadro_no_editable2.grid(row=3, column=0, padx=10, pady=5)

etiqueta_no_editable3 = tk.Label(frame_izquierda, text="Analizador Semántico" ,bg="#49708a", fg="white")
etiqueta_no_editable3.grid(row=2, column=1, padx=10, pady=(10, 5), sticky="w")

cuadro_no_editable3 = scrolledtext.ScrolledText(frame_izquierda, wrap=tk.WORD, height=20, width=50, state="disabled")
cuadro_no_editable3.grid(row=3, column=1, padx=10, pady=5)

# Cuadro de ejecución en la sección derecha
etiqueta_ejecucion = tk.Label(frame_derecha, text="Ejecución" ,bg="#49708a", fg="white")
etiqueta_ejecucion.grid(row=0, column=0, padx=10, pady=(10, 5), sticky="w")

# Botones en la sección izquierda
boton_limpiar = tk.Button(frame_derecha, text="Limpiar", command=limpiar_todo, bg="#2c71b6", fg="white", height=3, width=20)
boton_limpiar.grid(row=4, column=0, padx=(0,5), pady=10, sticky="w")

boton_ejecutar = tk.Button(frame_derecha, text="Ejecutar", command=compilar, bg="#16770b", fg="white", height=3, width=20)
boton_ejecutar.grid(row=4, column=0, padx=(5,0), pady=10, sticky="e")


cuadro_ejecucion = scrolledtext.ScrolledText(frame_derecha, wrap=tk.WORD, height=40, width=65, state="disabled")
cuadro_ejecucion.grid(row=1, column=0, padx=10, pady=(10, 5))


# Iniciar el bucle principal de la aplicación
ventana.mainloop()
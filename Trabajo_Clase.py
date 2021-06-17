#PEDIMOS QUE INGRESE EL TEXTO
texto=input(str("Ingrese una cadena de texto: "))
#PEDIMOS QUE SE ENLISTEN LAS PALABRAS Y SE BUSQUEN LAS PALABRAS

listaPalabras = texto.split()
palabraBuscar= input(str("Ingresa la palabra que deseas ver su ocurrencias: "))
ocurrencias = texto.count(palabraBuscar)

#ESTE LISTA EN LISTA TODAS LAS PALABRAS QUE TIENE EL TEXTO
cantidadPalabras=[]
for j in listaPalabras:
    cantidadPalabras.append(listaPalabras.count(j))

print("Cantidad de palabras: \n" + (str(listaPalabras)) + "\n")
print(" ")
print("Las palabras que tienen ocurrencia son : ", "(", palabraBuscar ,",", ocurrencias, ")")
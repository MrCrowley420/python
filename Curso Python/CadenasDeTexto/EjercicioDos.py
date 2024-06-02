''' Crear un programa que tenga una variable con la cadena “Separado” y un carácter de coma (,); e inserte el carácter entre cada letra de la cadena. Ej: separar y , debería devolver s,e,p,a,r,a,r

Pista: Debes utilizar un método de las cadenas llamado “Replace”, recuerda que la posición de los caracteres empieza en 0. ''' 

palabra = "eparado"

cadena = "Este el uso del metodo Replace"

print(cadena)
reemplazar = cadena.replace("e" , "E")
print (reemplazar)

print(palabra)

reemplazarPalabra = palabra.replace("" , ",")

print(reemplazarPalabra)

print("S",reemplazarPalabra)
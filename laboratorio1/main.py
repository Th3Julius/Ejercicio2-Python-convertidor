print("CONVERTIDOR")

items = ['1 = Longitud','2 = Monedas','3 = Temperatura']
print()
print(items[0])
print(items[1])
print(items[2])
print()
unidad = input("¿Que deseas convertir?:")


if unidad == "1":
    items = ['1 = Kilometros a Millas','2 = Millas a Kilometros']
    print()
    print(items[0])
    print(items[1])
    print()
    und = input("¿Que deseas convertir?:")
    if und == "1":
        print("Kilometros a Millas")
        km = input("Kilometros:")
        km_a_millas = (float(km) * 0.621)/1
        print(km,"Kilometros son",round(km_a_millas,3),"Millas")
    elif und == "2":
        print("Millas a Kilometros")
        millas = input("Euros:")
        millas_a_kilometros = (float(millas) * 1.61)/1
        print(millas,"MIllas son",round(millas_a_kilometros,3),"Kilometros")
    else:
        print("Inserta un número de las anteriores opciones")


elif unidad == "2":
    items = ['1 = Usd a Euros','2 = Euros a Usd']
    print()
    print(items[0])
    print(items[1])
    print()
    und = input("¿Que deseas convertir?:")
    if und == "1":
        print("Usd a Euros")
        usd = input("usd:")
        usd_a_euros = (float(usd) * 0.83)/1
        print(usd,"Dolares son",round(usd_a_euros,3),"Euros")
    elif und == "2":
        print("Euros a Usd")
        euros = input("Euros:")
        euros_a_usd = (float(euros) * 1.21)/1
        print(euros,"Euros son",round(euros_a_usd,3),"Dolares")
    else:
        print("Inserta un número de las anteriores opciones")


elif unidad == "3":
    items = ['1 = fahrenheit a celsius','2 = celsius a farenheit']
    print()
    print(items[0])
    print(items[1])
    print()
    und = input("¿Que deseas convertir?:")
    if und == "1":
        print("Grados Fahrenheit a Grados Celsius")
        fahrenheit = input("Fahrenheit:")
        fahrenheit_a_celsius = (float(fahrenheit) - 32) * 5/9
        print(fahrenheit,"grados fahrenheit son",round(fahrenheit_a_celsius,3),"grados celsius")
    elif und == "2":
        print("Grados Celsius a Grados Fahrenheit")
        celsius = input("Celsius:")
        celsius_a_fahrenheit = (float(celsius) * 9/5) + 32
        print(celsius,"grados celsius son",round(celsius_a_fahrenheit,3),"grados fahrenheit")
    else:
        print("Inserta un número de las anteriores opciones")
else:
    print("Inserta un número de las siguientes opcioes")






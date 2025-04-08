#se le da el valor a la contraseña
cont_corr = "quepasachaval"

#se inicia un bucle
while True:
    for i in range(5):
        cont_use = input("Dame la contraseña  ")
        if cont_corr == cont_use:
            print("Contraseña correcta")
            break #se rompe el bucle cuando se pone la contraseña correcta
        print(f"Contraseña incorrecta, intentos,{i + 1}")
    else: 
        print("Contraseña incorrecta")
        print("Has alcanzado el limite de intentos")
    break # se rompe el bucle cuando se te acaban los intentos

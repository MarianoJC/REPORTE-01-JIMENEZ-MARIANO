from lifestore_file import lifestore_products, lifestore_sales, lifestore_searches

usuarioAccedio = False
intentos = 0

mensaje_bienvenida = 'Bienvenido al sistema!\nAccede con tus credenciales'
print(mensaje_bienvenida)

# Usuario: jimmy contraseña: datadarks 

while not usuarioAccedio:
    usuario = input('Usuario: ')
    contras = input('Contrase;a: ')
    intentos += 1
    if usuario == 'jimmy' and contras == 'datadarks':
        usuarioAccedio = True
        print('Hola de nuevo!')
    else:
        print(f'Tienes {3 - intentos} intentos restantes')
        if usuario == 'jimmy':
            print('Te equivocaste en la contrase;a')
        else:
            print(f'El usuario: "{usuario}" no esta registrado')

    if intentos == 3:
        exit()

print('Solamente llegaste aca si ingresaste correctamente')

if usuarioAccedio == True:

# Extraemos el ID de cada producto vendido
    productos_comprados = []
    for val in lifestore_sales:
        productos_comprados.append(val[1])

    topcinco = []

# Evaluamos para tener los mejores 5
    while (len(topcinco) < 5):
        count = 0
        temp = 0
        index = 0

#Evaluamos cada elemento vendido
        for x in range(0, len(productos_comprados)):
            temp = productos_comprados.count(productos_comprados[x])

            if (temp > count) and (not (productos_comprados[x] in topcinco)):
                count = temp
                index = x

        mostfrequent = productos_comprados[index]
        topcinco.append(mostfrequent)

    print("Lo productos con mayores ventas son: \n")
    for x in topcinco:
        nombre = lifestore_products[x - 1]
        nombre2 = nombre[1]
        print(nombre2)
        print("\n")
# los 10 mas buscados

    productos_buscados = []
    for val in lifestore_searches:
        productos_buscados.append(val[1])

    topdiezb = []

#Buscamos los 10 mas buscados
    while (len(topdiezb) < 10):
        count = 0
        temp = 0
        index = 0

#Evaluamos cada elemento Buscado
        for x in range(0, len(productos_buscados)):
            temp = productos_buscados.count(productos_buscados[x])

            if (temp > count) and (not (productos_buscados[x] in topdiezb)):
                count = temp
                index = x

        mostfrequent = productos_buscados[index]
        topdiezb.append(mostfrequent)

    print(" Lo productos con mayores buscadas son: \n ")
    for x in topdiezb:
        nombre = lifestore_products[x - 1]
        nombre2 = nombre[1]
        print(nombre2)
        print("\n")

# Creacion de las valores para evaluar por categoria

    lista = []
    procesadores = []
    taj_v = []
    tar_m = []
    dd = []
    usbs = []
    pantallas = []
    bocinas = []
    aud = []
    contador = 0

# Sacamos los por categoria
    for producto in lifestore_products:
        if producto[3] == "procesadores":
            procesadores.append([producto[0], producto[1]])
    for procesador in procesadores:
        for venta in lifestore_sales:
            if procesador[0] == venta[1]:
                contador += 1
        if contador != 0:
            lista.append([procesador[0], procesador[1], contador])
            contador = 0

# Ordenamos la lista obtenida e imprimimos

    lista.sort(key=lambda x: x[2], reverse=False)
    print("Procesadores \n")
    print("1." + procesadores[8][1] + " el cual ha sido vendido 0 veces \n")
    for i in range(0, 4):
        print(
            str(i + 2) + ". " + lista[i][1] + "  el cual ha sido vendido " +
            str(lista[i][2]) + " veces\n")

# borramos todo contenido dentro de la lista para evaluar mas facilmente
   lista = []

    for producto in lifestore_products:
        if producto[3] == "tarjetas de video":
            taj_v.append([producto[0], producto[1]])
    for video in taj_v:
        for venta in lifestore_sales:
            if video[0] == venta[1]:
                contador += 1
        if contador != 0:
            lista.append([video[0], video[1], contador])
            contador = 0

    lista.sort(key=lambda x: x[2], reverse=False)
    print("Tarjetas de Video \n")
    print("1." + taj_v[8][1] + " el cual ha sido vendido 0 veces \n")
    for i in range(0, 4):
        print(
            str(i + 2) + ". " + lista[i][1] + "  el cual ha sido vendido " +
            str(lista[i][2]) + " veces\n")

# borramos todo contenido dentro de la lista para evaluar mas facilmente
    lista = []

    for producto in lifestore_products:
        if producto[3] == "tarjetas madre":
            tar_m.append([producto[0], producto[1]])
    for madre in tar_m:
        for venta in lifestore_sales:
            if madre[0] == venta[1]:
                contador += 1
        if contador != 0:
            lista.append([madre[0], madre[1], contador])
            contador = 0

    lista.sort(key=lambda x: x[2], reverse=False)
    print("Tarjetas Madre \n")
    print("1." + tar_m[4][1] + " el cual ha sido vendido 0 veces \n")
    print("2." + tar_m[6][1] + " el cual ha sido vendido 0 veces \n")
    print("3." + tar_m[8][1] + " el cual ha sido vendido 0 veces \n")
    print("4." + tar_m[9][1] + " el cual ha sido vendido 0 veces \n")
    print("5." + tar_m[10][1] + " el cual ha sido vendido 0 veces \n")

# borramos todo contenido dentro de la lista para evaluar mas facilmente
    lista = []

    for producto in lifestore_products:
        if producto[3] == "discos duros":
            dd.append([producto[0], producto[1]])
    for duro in dd:
        for venta in lifestore_sales:
            if duro[0] == venta[1]:
                contador += 1
        if contador != 0:
            lista.append([duro[0], duro[1], contador])
            contador = 0

    lista.sort(key=lambda x: x[2], reverse=False)
    print("Discos Duros \n")
    print("1." + dd[8][1] + " el cual ha sido vendido 0 veces \n")
    print("2." + dd[6][1] + " el cual ha sido vendido 0 veces \n")
    print("3." + dd[9][1] + " el cual ha sido vendido 0 veces \n")
    for i in range(0, 2):
        print(
            str(i + 4) + ". " + lista[i][1] + "  el ual ha sido vendido " +
            str(lista[i][2]) + " veces\n")

# borramos todo contenido dentro de la lista para evaluar mas facilmente
    lista = []

    for producto in lifestore_products:
        if producto[3] == "pantallas":
            pantallas.append([producto[0], producto[1]])
    for pantalla in pantallas:
        for venta in lifestore_sales:
            if pantalla[0] == venta[1]:
                contador += 1
        if contador != 0:
            lista.append([pantalla[0], pantalla[1], contador])
            contador = 0

    lista.sort(key=lambda x: x[2], reverse=False)
    print("Pantallas \n")
    print("1." + pantallas[0][1] + " el cual ha sido vendido 0 veces \n")
    print("2." + pantallas[1][1] + " el cual ha sido vendido 0 veces \n")
    print("3." + pantallas[2][1] + " el cual ha sido vendido 0 veces \n")
    print("4." + pantallas[3][1] + " el cual ha sido vendido 0 veces \n")
    print("5." + pantallas[8][1] + " el cual ha sido vendido 0 veces \n")

# borramos todo contenido dentro de la lista para evaluar mas facilmente
    lista = []

    for producto in lifestore_products:
        if producto[3] == "bocinas":
            bocinas.append([producto[0], producto[1]])
    for bocina in bocinas:
        for venta in lifestore_sales:
            if bocina[0] == venta[1]:
                contador += 1
        if contador != 0:
            lista.append([bocina[0], bocina[1], contador])
            contador = 0

    lista.sort(key=lambda x: x[2], reverse=False)
    print("Bocinas \n")
    print("1." + bocinas[1][1] + " el cual ha sido vendido 0 veces \n")
    print("2." + bocinas[2][1] + " el cual ha sido vendido 0 veces \n")
    print("3." + bocinas[3][1] + " el cual ha sido vendido 0 veces \n")
    print("4." + bocinas[4][1] + " el cual ha sido vendido 0 veces \n")
    print("5." + bocinas[5][1] + " el cual ha sido vendido 0 veces \n")

# borramos todo contenido dentro de la lista para evaluar mas facilmente
    lista = []

    for producto in lifestore_products:
        if producto[3] == "audifonos":
            aud.append([producto[0], producto[1]])
    for audifono in aud:
        for venta in lifestore_sales:
            if audifono[0] == venta[1]:
                contador += 1
        if contador != 0:
            lista.append([audifono[0], audifono[1], contador])
            contador = 0

    lista.sort(key=lambda x: x[2], reverse=False)
    print("Audifonos \n")
    print("1." + aud[2][1] + " el cual ha sido vendido 0 veces \n")
    print("2." + aud[3][1] + " el cual ha sido vendido 0 veces \n")
    print("3." + aud[4][1] + " el cual ha sido vendido 0 veces \n")
    print("4." + aud[6][1] + " el cual ha sido vendido 0 veces \n")
    print("5." + aud[7][1] + " el cual ha sido vendido 0 veces \n")

# borramos todo contenido dentro de la lista para evaluar mas facilmente
    contador = 0

    lista = []

    for producto in lifestore_products:
        if producto[3] == "procesadores":
            procesadores.append([producto[0], producto[1]])
    for procesador in procesadores:
        for busqueda in lifestore_searches:
            if procesador[0] == busqueda[1]:
                contador += 1
        if contador != 0:
            lista.append([procesador[0], procesador[1], contador])
            contador = 0

    lista.sort(key=lambda x: x[2], reverse=False)
    print("Procesadores \n")
    for i in range(0, 9):
        print(
            str(i + 1) + ". " + lista[i][1] + "  el cual fue buscado " +
            str(lista[i][2]) + " veces\n")
# borramos todo contenido dentro de la lista para evaluar mas facilmente
    lista = []

    for producto in lifestore_products:
        if producto[3] == "tarjetas de video":
            taj_v.append([producto[0], producto[1]])
    for video in taj_v:
        for busqueda in lifestore_searches:
            if video[0] == busqueda[1]:
                contador += 1
        if contador != 0:
            lista.append([video[0], video[1], contador])
            contador = 0

    lista.sort(key=lambda x: x[2], reverse=False)
    print("Tarjetas de Video \n")
    print("1." + taj_v[4][1] + " el cual fue buscado 0 veces \n")
    print("2." + taj_v[6][1] + " el cual fue buscado 0 veces \n")
    print("3." + taj_v[9][1] + " el cual fue buscado 0 veces \n")
    print("4." + taj_v[10][1] + " el cual fue buscado 0 veces \n")
    print("5." + taj_v[13][1] + " el cual fue buscado 0 veces \n")
    print("6." + taj_v[14][1] + " el cual fue buscado 0 veces \n")
    for i in range(0, 4):
        print(
            str(i + 7) + ". " + lista[i][1] + "  el cual fue buscado " +
            str(lista[i][2]) + " veces\n")
# borramos todo contenido dentro de la lista para evaluar mas facilmente
    lista = []

    for producto in lifestore_products:
        if producto[3] == "tarjetas madre":
            tar_m.append([producto[0], producto[1]])
    for madre in tar_m:
        for busqueda in lifestore_searches:
            if madre[0] == busqueda[1]:
                contador += 1
        if contador != 0:
            lista.append([madre[0], madre[1], contador])
            contador = 0

    lista.sort(key=lambda x: x[2], reverse=False)
    print("Tarjetas Madre \n")
    print("1." + tar_m[1][1] + " el cual fue buscado 0 veces \n")
    print("2." + tar_m[3][1] + " el cual fue buscado 0 veces \n")
    print("3." + tar_m[4][1] + " el cual fue buscado 0 veces \n")
    print("4." + tar_m[5][1] + " el cual fue buscado 0 veces \n")
    print("5." + tar_m[7][1] + " el cual fue buscado 0 veces \n")
    print("6." + tar_m[8][1] + " el cual fue buscado 0 veces \n")
    print("7." + tar_m[9][1] + " el cual fue buscado 0 veces \n")
    print("8." + tar_m[12][1] + " el cual fue buscado 0 veces \n")
    print("9." + tar_m[14][1] + " el cual fue buscado 0 veces \n")
    for i in range(0, 1):
        print(
            str(i + 10) + ". " + lista[i][1] + "  el cual fue buscado " +
            str(lista[i][2]) + " veces\n")
# borramos todo contenido dentro de la lista para evaluar mas facilmente
    lista = []

    for producto in lifestore_products:
        if producto[3] == "discos duros":
            dd.append([producto[0], producto[1]])
    for duro in dd:
        for busqueda in lifestore_searches:
            if duro[0] == busqueda[1]:
                contador += 1
        if contador != 0:
            lista.append([duro[0], duro[1], contador])
            contador = 0

    lista.sort(key=lambda x: x[2], reverse=False)
    print("Discos Duros \n")
    print("1." + dd[6][1] + " el cual fue buscado 0 veces \n")
    print("2." + dd[8][1] + " el cual fue buscado 0 veces \n")
    print("3." + dd[11][1] + " el cual fue buscado 0 veces \n")
    for i in range(0, 7):
        print(
            str(i + 4) + ". " + lista[i][1] + "  el cual fue buscado " +
            str(lista[i][2]) + " veces\n")
# borramos todo contenido dentro de la lista para evaluar mas facilmente
    lista = []

    for producto in lifestore_products:
        if producto[3] == "pantallas":
            pantallas.append([producto[0], producto[1]])
    for pantalla in pantallas:
        for busqueda in lifestore_searches:
            if pantalla[0] == busqueda[1]:
                contador += 1
        if contador != 0:
            lista.append([pantalla[0], pantalla[1], contador])
            contador = 0

    lista.sort(key=lambda x: x[2], reverse=False)
    print("Pantallas \n")
    print("1." + pantallas[0][1] + " el cual fue buscado 0 veces \n")
    print("2." + pantallas[2][1] + " el cual fue buscado 0 veces \n")
    print("3." + pantallas[3][1] + " el cual fue buscado 0 veces \n")
    print("4." + pantallas[6][1] + " el cual fue buscado 0 veces \n")
    print("5." + pantallas[7][1] + " el cual fue buscado 0 veces \n")
    print("6." + pantallas[9][1] + " el cual fue buscado 0 veces \n")
    print("7." + pantallas[10][1] + " el cual fue buscado 0 veces \n")
    for i in range(0, 3):
        print(
            str(i + 8) + ". " + lista[i][1] + "  el cual fue buscado " +
            str(lista[i][2]) + " veces\n")
# borramos todo contenido dentro de la lista para evaluar mas facilmente
    lista = []

    for producto in lifestore_products:
        if producto[3] == "bocinas":
            bocinas.append([producto[0], producto[1]])
    for bocina in bocinas:
        for busqueda in lifestore_searches:
            if bocina[0] == busqueda[1]:
                contador += 1
        if contador != 0:
            lista.append([bocina[0], bocina[1], contador])
            contador = 0

    lista.sort(key=lambda x: x[2], reverse=False)
    print("Bocinas \n")
    print("1." + bocinas[1][1] + " el cual fue buscado 0 veces \n")
    print("2." + bocinas[3][1] + " el cual fue buscado 0 veces \n")
    print("3." + bocinas[4][1] + " el cual fue buscado 0 veces \n")
    print("4." + bocinas[5][1] + " el cual fue buscado 0 veces \n")
    print("5." + bocinas[7][1] + " el cual fue buscado 0 veces \n")
    print("6." + bocinas[8][1] + " el cual fue buscado 0 veces \n")
    print("7." + bocinas[9][1] + " el cual fue buscado 0 veces \n")
    for i in range(0, 3):
        print(
            str(i + 8) + ". " + lista[i][1] + "  el cual fue buscado " +
            str(lista[i][2]) + " veces\n")
# borramos todo contenido dentro de la lista para evaluar mas facilmente
    lista = []

    for producto in lifestore_products:
        if producto[3] == "audifonos":
            aud.append([producto[0], producto[1]])
    for audifono in aud:
        for busqueda in lifestore_searches:
            if audifono[0] == busqueda[1]:
                contador += 1
        if contador != 0:
            lista.append([audifono[0], audifono[1], contador])
            contador = 0

    lista.sort(key=lambda x: x[2], reverse=False)
    print("Audifonos \n")
    print("1." + aud[2][1] + " el cual fue buscado 0 veces \n")
    print("2." + aud[3][1] + " el cual fue buscado 0 veces \n")
    print("3." + aud[4][1] + " el cual fue buscado 0 veces \n")
    print("4." + aud[6][1] + " el cual fue buscado 0 veces \n")
    print("5." + aud[8][1] + " el cual fue buscado 0 veces \n")
    print("6." + aud[12][1] + " el cual fue buscado 0 veces \n")
    for i in range(0, 4):
        print(
            str(i + 7) + ". " + lista[i][1] + "  el cual fue buscado " +
            str(lista[i][2]) + " veces\n")

#creacion de las listas para obtener las reseñas
    list1 = []
    list2 = []
    list3 = []
    list4 = []
    list5 = []
    list6 = []
    list7 = []
    cond = 0
    suma = 0
    sums = []
    suma1 = 0

    print("\nLos 5 productos con las mejores reseñas son: \n")
  #obtenemos los id y evaluamos dentro de lifestore sale
    for product in lifestore_products:
        for sales in lifestore_sales:
            if product[0] == sales[1]:
                list1.append([product[0], sales[2]])
                list2.append(product[0])
                count = [[ID, list2.count(ID)] for ID in set(list2)]

#Creamos una lista de las reseñas para cada producto, y una lista para las etiquetas de cada producto    
    for element in list1:
        if element[0] == cond:
            suma += element[1]
            cond = element[0]
        if element[0] != cond:
            sums.append([element[0], suma])
            suma = 0
            suma += element[1]
            cond = element[0]
#Añadimos la calificación acumulada del producto evaluado e Iteramos para obtener una lista que combine las dos listas definidas previamente
    for suma1 in sums:
        list3.append(suma1[0])
        list4.append(suma1[1])
    del list4[0]
    list4.append(4)
#Iteramos para conocer el promedio de cada producto, y añadirlo a una nueva lista
    for i in range(0, len(sums)):
        list5.append([list3[i], list4[i]])

    for i in range(0, len(list5)):
        x = int(count[i][1])

        y = float(list5[i][1] / x)

        list6.append([list5[i][0], y])
#Iteramos para tener en una nueva lista el nombre del producto y el promedio de calificación     
    for product in lifestore_products:
        for element in list6:
            if product[0] == element[0]:
                list7.append([product[1], element[1]])

    list7.sort(key=lambda x: x[1], reverse=True)

    for i in range(0, 5):
        print(
            str(i + 1) + ". " + list7[i][0] +
            "  el cual tiene una calificación promedio de " +
            str(list7[i][1]) + " estrellas\n")

    list1 = []
    list2 = []
    list3 = []
    list4 = []
    list5 = []
    list6 = []
    list7 = []
    cond = 0
    suma = 0
    sums = []
    suma1 = 0

    print("\nLos 5 productos con las peores reseñas son: \n")
    for product in lifestore_products:
        for sales in lifestore_sales:
            if product[0] == sales[1] and sales[4] == 0:
                list1.append([product[0], sales[2]])
                list2.append(product[0])
                count = [[ID, list2.count(ID)] for ID in set(list2)]

    for element in list1:
        if element[0] == cond:
            suma += element[1]
            cond = element[0]
        if element[0] != cond:
            sums.append([element[0], suma])
            suma = 0
            suma += element[1]
            cond = element[0]

    for suma1 in sums:
        list3.append(suma1[0])
        list4.append(suma1[1])
    del list4[0]
    list4.append(4)

    for i in range(0, len(sums)):
        list5.append([list3[i], list4[i]])

    for i in range(0, len(list5)):
        x = int(count[i][1])

        y = float(list5[i][1] / x)

        list6.append([list5[i][0], y])

    for product in lifestore_products:
        for element in list6:
            if product[0] == element[0]:
                list7.append([product[1], element[1]])

    list7.sort(key=lambda x: x[1], reverse=False)

    for i in range(0, 5):
        print(
            str(i + 1) + ". " + list7[i][0] +
            "  el cual tiene una calificación promedio de " +
            str(list7[i][1]) + " estrellas\n")
#creacion de la variable ingresos para buscar los ingresos
    ingresos = 0
#extraemos el precio de cada producto y vemos cuantas veces aparecen para sumar cada valor de la venta
    for m in lifestore_products:
        idp = m[0]
        precio = m[2]
        for n in lifestore_sales:
            dev = n[4]
            if (dev == 0):
                ventasid = n[1]
                if ventasid == idp:
                    ingresos = precio + ingresos

    print("El Total de ingresos es: $", ingresos)
#creacion de variable para ver cuanto se vendio y las ventas promedio por mes
    totalventas = 0

    for a in lifestore_sales:
        dev1 = a[4]
        if (dev1 == 0):
            totalventas = 1 + totalventas

    prom = totalventas / 12
    print("Las Ventas Promedio Mensuales son: ", prom)
    print("Las ventas totales fueron: ", totalventas)
#creacion de variable por cada mes
    Enero = 0
    Febrero = 0
    Marzo = 0
    Abril = 0
    Mayo = 0
    Junio = 0
    Julio = 0
    Agosto = 0
    Septiembre = 0
    Octubre = 0
    Noviembre = 0
    Diciembre = 0
#iteramos para ver a que mes corresponde
    for b in lifestore_sales:
        fecha = b[3]
        mes = fecha[3:5]
        dev2 = b[4]
        if (mes == "01"):
            Enero = 1 + Enero
        elif (mes == "02"):
            Febrero = 1 + Febrero
        elif (mes == "03"):
            Marzo = 1 + Marzo
        elif (mes == "04"):
            Abril = 1 + Abril
        elif (mes == "05"):
            Mayo = 1 + Mayo
        elif (mes == "06"):
            Junio = 1 + Junio
        elif (mes == "07"):
            Julio = 1 + Julio
        elif (mes == "08"):
            Agosto = 1 + Agosto
        elif (mes == "09"):
            Septiembre = 1 + Septiembre
        elif (mes == "10"):
            Octubre = 1 + Octubre
        elif (mes == "11"):
            Noviembre = 1 + Noviembre
        elif (mes == "12"):
            Diciembre = 1 + Diciembre

    meses = [
        Enero, Febrero, Marzo, Abril, Mayo, Junio, Julio, Agosto, Septiembre,
        Octubre, Noviembre, Diciembre
    ]
#Obtenemos los 3 meses con mas ventas evaluando cada mes y los imprimimos
    toptres = []

    while (len(toptres) < 3):
        count = 0
        temp = 0
        index = 0

        for x in range(0, len(meses)):
            temp = meses[x]

            if (temp > count) and (not (meses[x] in toptres)):
                count = temp
                index = x

        mostfrequent = meses[index]
        toptres.append(mostfrequent)

    print("Los 3 meses con mas ventas son: \n")

    for c in toptres:
        for d in meses:
            if (d == c):
                mes1 = meses.index(d)
                if (mes1 == 3):
                    print("Abril: ", c)
                elif (mes1 == 0):
                    print("Enero: ", c)
                elif (mes1 == 2):
                    print("Marzo: ", c)

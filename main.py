import collections
from sys import _clear_type_cache
from types import SimpleNamespace
from typing import Counter
from lifestore_file import lifestore_products, lifestore_sales, lifestore_searches

#Se realiza el ingreso del usuario o creación de cuenta para ingresar a Lifestore
usuario_directorio = ['']
contraseña_directorio = ['']

print ('BIENVENIDO A LIFESTORE')
verificacion = input ('¿Ya tienes cuenta? (SI/NO): ')
respuestasi = ['SI','si','Si','Sí']
respuestano = ['No','NO','no']

if verificacion in respuestano :
    print ('''\nPara crear tu nueva cuenta deberas escribir tu usuario y contraseña.
Posteriormente deberas iniciar sesión para acceder a la central de Lifestore.''')
usuario = input ('Escribe tu usuario: ')
contraseña = input ('Escribe tu contraseña: ')
usuario_directorio.append (usuario)
contraseña_directorio.append (contraseña)
print ('Listo, ya eres parte de la comunidad de Lifestore Central, ahora deberas iniciar sesión para acceder a Lifestore. ')
respuestano == 'listo'


#if verificacion in respuestasi or respuestano == 'listo':
#	intentos = 3
#	while intentos > 0 :
 #  		usuario = input ('Ingresa tu usuario: ')
 # #  	contraseña = input ('Ingresa tu contraseña: ')
#   		if usuario in usuario_directorio and contraseña if contraseña_directorio :
#      		print ('\nBienvenido a la central de Lifestore \n' ) 
#				break
#  	else :	
#    print ('El usuario/contraseña no existe o no está correcto')
#    intentos = intentos - 1
    
#if intentos == 0 :
#    print ('''\nLo sentimos, por seguridad de la empresa hemos bloqueado el acceso a la central de Lifestore.
#Por favor, mande un correo a data@lifestore.com\n''')
            
print ('Se darán datos sobre el reporte y variables analizadas')             
ventasproducto = [] #lista vacía
cantidadproductos = len (lifestore_products)

#Clasificación de categorías 
productos = lifestore_products[:cantidadproductos]
categorias = []
for categoria in productos:
    categoria = categoria[3]
    categorias.append(categoria)

categoriasunic = []
for i in categorias :
	if i not in categoriasunic :
		categoriasunic.append (i)	
#print (categoriasunic)

#UNION DE LISTAS SALES AND PRODUCT, NOS PERMITE VER LOS PRODUCTOS QUE COMPRARON CON PRECIO, SCORE, DATE, CATEGORIA, STOCK.
#listamaestra = [id_sale, id_product, score (from 1 to 5), date, refund (1 for true or 0 to false), id_product, name, price, category, stock]

indice = 0
longitud = len (lifestore_sales)
listamaestra = []

while indice < cantidadproductos :
	id1 = lifestore_products [indice] [0]
	indice2 = 0
	while indice2 < longitud :
		id2 = lifestore_sales [indice2][1]
		if id1 == id2 :
			list = lifestore_sales [indice2]
			list2 = lifestore_products [indice]
			listamaestra.append(list + list2 )
		indice2 +=1
	indice += 1
#print (listamaestra)


#LISTA DE PRODUCTOS BUSCADOS
# lista bp = [id_search, id product, id_product, name, price, category, stock]

indiceb = 0
longitudb = len (lifestore_searches)
lproductosbuscados = []

while indiceb < cantidadproductos :
	busq = lifestore_products [indiceb] [0]
	indiceb2 = 0
	while indiceb2 < longitudb :
		busq2 = lifestore_searches [indiceb2][1]
		if busq == busq2 :
			listb1 = lifestore_searches [indiceb2]
			listb2 = lifestore_products [indiceb]
			lproductosbuscados.append(listb1 + listb2)
		indiceb2 +=1
	indiceb += 1
#print (lproductosbuscados)

#LISTA DE PRODUCTOS NO COMPRADOS
productos = lifestore_sales[:longitud]
comprados = []
for comprado in productos:
    comprado = comprado[1]
    comprados.append(comprado)

productost = lifestore_products[:cantidadproductos]
productostotales = []
for productototal in productost:
    productototal = productototal[0]
    productostotales.append(productototal)
#print (productostotales)

nocomprados = []
for n in productostotales :
	if n not in comprados :
		nocomprados.append (n)
#print (nocomprados)


indicenoc = 0
longitudnoc = len (nocomprados)
nocompradosid = []

while indicenoc < longitudnoc :
	idbus = nocomprados [indicenoc] 
	indicenoc2 = 0
	while indicenoc2 < cantidadproductos :
		idbus2= lifestore_products [indicenoc2] [0]
		if idbus == idbus2 :
			listanoc2 = lifestore_products [indicenoc2]
			nocompradosid.append(listanoc2)
		indicenoc2 += 1
	indicenoc += 1
print ('Los productos no comprados fueron: ', nocompradosid)

#LISTA DE PRODUCTOS NO BUSCADOS
busquedas = lifestore_searches[:longitudb]
buscados = []
for buscado in busquedas:
    buscado = buscado[1]
    buscados.append(buscado)

nobuscados = []
for b in productostotales :
	if b not in buscados :
		nobuscados.append (b)

indicenob = 0
longitudnob = len (nobuscados)
nobuscadosid = []

while indicenob < longitudnob :
	idnobus = nobuscados [indicenob] 
	indicenob2 = 0
	while indicenob2  < cantidadproductos :
		idnobus2= lifestore_products [indicenob2] [0]
		if idnobus == idnobus2 :
			listanob2 = lifestore_products [indicenob2]
			nobuscadosid.append(listanob2)
		indicenob2 += 1
	indicenob += 1
print ('Los productos no buscados son: ', nobuscadosid)

numventas = len (listamaestra)
ingre = 0
ingresototal = []
while ingre < numventas :
	precio = listamaestra [ingre] [7]
	ingresototal. append (precio)
	ingre +=1
#print (sum(ingresototal))
#Devolución total
dev = 0
devtotal = []

while dev < numventas :
	dev1 = listamaestra [dev] [7] #columna de precios
	dev2 = listamaestra[dev] [4] #columna de devoluciones
	if dev2 > 0 :
		devolu = dev1
		devtotal.append(devolu)
	dev += 1
#print (sum (devtotal))
ingresofinal = sum(ingresototal) - sum (devtotal)
print ('El ingreso total vendido es de $', (ingresofinal))


#MAYOR BÚSQUEDA Y MENOR BÚSQUEDA
productosbusq = lproductosbuscados[:longitudb]
producbs = []
for producb in productosbusq:
    producb = producb[3]
    producbs.append(producb)
#print (producbs)

import collections
cuenta1 = collections.Counter(producbs)
#print(cuenta1)

masbuscados = cuenta1.most_common (5)
#print (masbuscados)

n=10
menosbuscados = cuenta1.most_common()[:-n-1:-1]
#print (menosbuscados)

#MÁS VENTAS Y MENOS VENTAS
long = len (listamaestra)
productosventas = listamaestra[:long]
productventas = []
for productv in productosventas:
    productv = productv[6]
    productventas.append(productv)
#print (productventas )


venta1 = collections.Counter(productventas )


masvendidos = venta1.most_common (5)
print ('Los productos con más ventas son: ',masbuscados)

n=10
menosvendidos = venta1.most_common()[:-n-1:-1]
print ('Los productos con menos ventas son: ', menosbuscados)


#productos con mayor acumulación en inventario
acumulacion = sorted (lifestore_products, reverse = True, key= lambda tupla:tupla[4])
top10= acumulacion[:5]
print('Los 5 productos con mayor acumulación en stock son: ', '\n', top10,)

#total de ventas mensual
totalventasmensual = longitud // 12
print ('El total de ventas promedio mensual es de :', totalventasmensual)

git remoto agregar origen https://github.com/ElisaTC/ElisaTosca.git
 rama git -M principal 
git push -u origen principal

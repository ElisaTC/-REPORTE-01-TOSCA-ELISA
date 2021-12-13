import collections
from sys import _clear_type_cache
from types import SimpleNamespace
from typing import Counter
from lifestore_file import lifestore_products, lifestore_sales, lifestore_searches
import sys


#Se realiza el ingreso del usuario o creación de cuenta para ingresar a Lifestore
usuario_directorio = ['Jimmy']
contraseña_directorio = ['Jimmy']
respuestasi = ['SI','si','Si','Sí']
respuestano = ['No','NO','no']

print ('BIENVENIDO A LIFESTORE')

int = 0
verificacion = input ('¿Ya tienes cuenta? (SI/NO): ')


if verificacion not in respuestasi and respuestano :
	print ('Error en respuesta, escribe nuevamente')
	verificacion = input ('¿Ya tienes cuenta? (SI/NO): ')
		

if verificacion in respuestano :
	print ('''\nPara crear tu nueva cuenta deberas escribir tu usuario y contraseña.
Posteriormente deberas iniciar sesión para acceder a la central de Lifestore.''')
	usuario = input ('Escribe tu usuario: ')
	contraseña = input ('Escribe tu contraseña: ')
	usuario_directorio.append (usuario)
	contraseña_directorio.append (contraseña)
	print ('Listo, ya eres parte de la comunidad de Lifestore Central, ahora deberas iniciar sesión para acceder a Lifestore. ')	
	respuestano = 'listo'
	
if verificacion in respuestasi or respuestano == 'listo':
	intentos = 3
	while intentos > 0 :
		usuario = input ('Ingresa tu usuario: ')
		contraseña = input ('Ingresa tu contraseña: ')
		if usuario in usuario_directorio and contraseña in contraseña_directorio :
			print ('\nBienvenido a la central de Lifestore \n' ) 
			break
		else :	
			print ('El usuario/contraseña no existe o no está correcto')
			intentos = intentos - 1

	if intentos == 0 :
		print ('''\nLo sentimos, por seguridad de la empresa hemos bloqueado el acceso a la central de Lifestore. Por favor, mande un correo a data@lifestore.com\n''')
		sys.exit ()

	
            
print ('Se darán datos sobre el reporte y variables analizadas')             
ventasproducto = [] #lista vacía
cantidadproductos = len (lifestore_products)

#Clasificación de categorías 
#Ésta nos iba a servir para la realización del menú, calculados las distintas categorías que tenemos en total
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
print ('\n > Los productos nunca comprados en la página web durante el ejercicio del informe son: \n')
for productonocomprados in nocompradosid :
	print (productonocomprados[1])


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

print ('\n > Los productos nunca buscados en la página web durante el ejercicio del presente informe son: \n')
for nobuscadoid in nobuscadosid :
	print (nobuscadoid[1])


# 								>>>> DATOS DE INGRESOS TOTALES Y MENSUALES <<<<
#listamaestra = [id_sale, id_product, score (from 1 to 5), date, refund (1 for true or 0 to false), id_product, name, price, category, stock]

#Ventas realizadas eliminando aquellas con reembolso
numventas = len (listamaestra)
ventastotal = []
for ventas in listamaestra:
	refund = ventas [4]
	if refund == 1 :
		continue
	else: 
		ventastotal.append (ventas)
#print (ventastotal)

meses= ['/01/','/02/','/03/','/04/','/05/','/06/','/07/','/08/','/09/','/10/','/11/','/12/']
ventaspormes = []
#Crear lista vacía por cada mes, para luego anexar datos de ventas y fechas
for mes in meses:
	lista = []
	ventaspormes.append(lista)
#print (ventaspormes)

#A partir de mis ventas cerradas, se realiza una lista con todas las ventas que me permitirá calcular mi ganancia total y definir variables
ganancianual = []
for venta in ventastotal:
	precio = venta [7]
	fecha = venta [3]
	conteomeses= 0
	ganancianual.append (precio)

#Por cada mes del año, si pertenece al mes se anexa el precio de cada producto vendido, para guardarlo en la lista vacía creada por mes
	for mes in meses:
		if mes in fecha :
			ventaspormes[conteomeses].append(precio)
			continue
		conteomeses += 1
#print (ventaspormes)
print ('>>> Ganancias y ventas menesuales ')
print (f'\n La ganancia de ventas total es de ${sum(ganancianual)}.00\n')

conteomes = 0
for cadames in ventaspormes :
	if sum(cadames) == 0:
		continue
	else:
		print (f'En el mes de {meses[conteomes]} se dieron {len(cadames)} ventas en total con un total de ganancia de ${sum(cadames)}.00')
		conteomes += 1

# >>>>> OTRA FORMA DE CALCULAR EL INGRESO TOTAL VENDIDO <<<<
#while ingre < numventas :
#	precio = listamaestra [ingre] [7]
#	ingresototal. append (precio)
#	ingre +=1
#print (sum(ingresototal))
#Devolución total
#dev = 0
#devtotal = []
#while dev < numventas :
#	dev1 = listamaestra [dev] [7] #columna de precios
#	dev2 = listamaestra[dev] [4] #columna de devoluciones
#	if dev2 > 0 :
#		devolu = dev1
#		devtotal.append(devolu)
#	dev += 1
#print (sum (devtotal))
#ingresofinal = sum(ingresototal) - sum (devtotal)
#print ('El ingreso total vendido es de $',(ingresofinal))


#									>>>> CATEGORIZACIÓN <<<<
#listamaestra = [id_sale, id_product, score (from 1 to 5), date, refund (1 for true or 0 to false), id_product, name, price, category, stock]
#Categorías por meses
categoriaspormes = []
for mes in meses:
	lista = []
	categoriaspormes.append(lista)

for venta in ventastotal:
	categoria = venta [-2],venta [-4]
	fecha = venta [3]
	conteomeses= 0
#Por cada mes del año, si pertenece al mes se anexa [nombreproducto,precio,categoria] de cada producto vendido en para guardarlo en la lista vacía creada por mes
	for mes in meses:
		if mes in fecha :
			categoriaspormes[conteomeses].append(categoria)
			continue
		conteomeses +=1
print (categoriaspormes)

#conteomes = 0
#for i in categoriaspormes :
	#print (f'En el mes de {meses[conteomes]} {i}')
#	conteomes+=1

# >>>>>> RESEÑAS
	
reseñaproduc =[]		
for prod in lifestore_products :
	idprodu = prod [0]
	nombreventa = prod [1]
	sublista = [idprodu, nombreventa, 0, 0]
	reseñaproduc.append (sublista)

for venta in listamaestra :
	idventaprod = venta [1]
	reseña = venta [2]
	indice = idventaprod - 1
	reseñaproduc [indice] [2] += reseña
	reseñaproduc [indice] [3] += 1

for indice, lista in enumerate (reseñaproduc):
	suma = lista [2]
	num = lista[3]
	if num > 0 :
		califprom = suma / num
		reseñaproduc [indice][2] = califprom

#solo aquellos reseñados/comprados
reseñados = []
for rev in reseñaproduc :
	sublista =[rev[1], rev[2], rev[3]]
	if rev[2] > 0 :
		reseñados.append (sublista)

# Los 5 mejores reseñados
calificacion = []
for lista in reseñados:
	listareseñas = [lista[1], lista [0]]
	calificacion.append (listareseñas)

calificacion.sort (reverse=True)
print ('\nDe acuerdo a sus reseñas, este es el top 5 de productos mejores reseñados')
for reseña,producto in calificacion [:5]:
	print (f'Con una calificación de {reseña}, el producto {producto}')

calificacion.sort ()
print ('\nDe acuerdo a sus reseñas, este es el top 5 de productos peores reseñados')
for malareseña, producto in calificacion [:5]:
	print (f'Con una calificación de {malareseña}, el producto {producto}')


#  >>>>>>>>>><MAYOR BÚSQUEDA Y MENOR BÚSQUEDA Y VENTA EN GENERAL (EL EJERCICIO) <<<<<<<<<<<<<<<<
productosbusq = lproductosbuscados[:longitudb]
producbs = []
for producb in productosbusq:
    producb = producb[3]
    producbs.append(producb)
#print (producbs)

cuenta1 = collections.Counter(producbs)
#print(cuenta1)

masbuscados = cuenta1.most_common (5)
print (f'\n > En total del ejercicio fiscal del presente informe, los cinco productos con mayor búsqueda en la página web son:\n')
for producto, numbusquedas in masbuscados :
	print (f'Con un total de {numbusquedas} búsqueda(s), el producto: {producto}')


n=10
menosbuscados = cuenta1.most_common()[:-n-1:-1]
print (f'\n> En total del ejercicio fiscal del presente informe, los diez productos con menor búsqueda en la página web son: \n')
for mproducto,mnumbusquedas in menosbuscados :
	print (f'Con un total de {mnumbusquedas} búsqueda(s), el producto: {mproducto}')

#MÁS VENTAS Y MENOS VENTAS
long = len (listamaestra)
productosventas = listamaestra[:long]
productventas = []
for productv in productosventas:
    productv = productv[6]
    productventas.append(productv)
#print (productventas )

venta1 = collections.Counter(productventas)

masvendidos = venta1.most_common (5)
print (f'\n > En total del ejercicio fiscal del presente informe, los cinco productos con mayor venta de manera general son:\n')
for productov, masventa in masvendidos :
	print (f'Con un total de {masventa} venta(s), el producto: {productov}')

n=10
menosvendidos = venta1.most_common()[:-n-1:-1]
print (f'\n > En total del ejercicio fiscal del presente informe, los diez productos con menor venta de manera general son:\n')
for productomv, menosventa in menosvendidos :
	print (f'Con un total de {menosventa} venta(s), el producto: {productomv}')


#productos con mayor acumulación en inventario
acumulacion = sorted (lifestore_products, reverse = True, key= lambda tupla:tupla[4])
top5= acumulacion[:5]
print (f'\n > En total del ejercicio fiscal del presente informe, los 5 productos con mayor acumulación en stock son:\n')
for productostock in top5 :
	print (f'Con un total de {productostock[-1]} productos en stock, el producto: {productostock[1]}.')



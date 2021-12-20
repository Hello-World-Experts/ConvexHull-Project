class Mining:
    #...
    def __init__(self, x, y, name):
        self.x = x
        self.y = y
        self.name = name

'Encontrar el punto más a la izquierda'
def Left_index(points):
    p_min = 0
    for i in range(1,len(points)):
        if points[i].x < points[p_min].x:
            p_min = i
    return p_min

'''
    Para encontrar la orientación del triplete ordenado (p, q, r).
    La función devuelve los siguientes valores
    0 -> p, q y r son colineales
    1 -> en sentido horario
    2 -> en sentido antihorario
'''
def orientation(p, q, r):
    val = (q.y - p.y) * (r.x - q.x) - (q.x - p.x) * (r.y - q.y)
    return val

def convexHull(points, n):
     
    # Debe haber al menos 3 puntos
    if n < 3:
        return
 
    # Encuentra el punto más a la izquierda
    l = Left_index(points)
 
    hull = []
     
    '''
    Comience desde el punto más a la izquierda, siga moviéndose en sentido antihorario
    hasta llegar de nuevo al punto de inicio. Este bucle corre O (h)
    veces donde h es el número de puntos en el resultado o la salida.
    '''
    p = l
    q = 0

    while(True):
         
        # Agregar el punto actual al resultado
        hull.append(p)
 
        '''
        Busque un punto 'q' tal que la orientación (p, q,
        x) es en sentido antihorario para todos los puntos 'x'. La idea
        es realizar un seguimiento de la última visita más contrarreloj-
        sabio punto en q. Si algún punto 'i' es más antihorario-
        más sabio que q, luego actualice q.
        '''
        r = (p + 1) % n

        for i in range(n):
             
            # Si i es más en sentido antihorario
            # que la q actual, luego actualice q
            #print(p,'  ',i,'  ',r)
            if(orientation(points[p], points[i], points[r]) < 0):
                r = i
 
        '''
        Ahora q es el más en sentido antihorario con respecto a p
        Establezca p como q para la siguiente iteración, de modo que q se agregue a
        resultado 'hull'
        '''
        p = r

        if(p == l):
            break
 

    for each in hull:
        print(points[each].name,points[each].x, points[each].y)


points = []
#Minas Superficiales
''' 
points.append(Mining(-78.685577, -6.732915, 'Tantahuatay'))
points.append(Mining(-78.625576, -6.760399, 'Cerro Corona'))
points.append(Mining(-78.910953, -6.848597, 'La Zanja'))
points.append(Mining(-78.521325, -6.989249, 'Yanacocha'))
points.append(Mining(-78.445816, -6.992365, 'Chaquicocha'))
points.append(Mining(-78.217445, -7.604548, 'Shahuindo'))
points.append(Mining(-78.299139, -7.889347, 'Alto Chicama'))
points.append(Mining(-78.135419, -7.895645, 'La Arena'))
points.append(Mining(-78.058088, -7.975328, 'La Virgen'))
points.append(Mining(-77.458447, -8.04125, 'Retamas'))
points.append(Mining(-77.586584, -9.427746, 'Pierina'))
points.append(Mining(-75.045, -11.369, 'Antamina'))
points.append(Mining(-76.263414, -10.68877, 'Cerro de Pasco'))

points.append(Mining(-76.273, -10.779, 'Colquijirca'))
points.append(Mining(-76.451271, -11.21673, 'Alpamarca'))
points.append(Mining(-76.143973, -11.607061, 'Toromocho'))
points.append(Mining(-75.562948, -12.570439, 'Corihuarmi'))
points.append(Mining(-76.146862, -11.596737, 'Antapite'))
points.append(Mining(-72.335570, -14.089333, 'Las Bambas'))
points.append(Mining(-72.445343, -14.195356, 'Anama'))
points.append(Mining(-72.284965, -14.441184, 'Anabi'))
points.append(Mining(-71.768614, -14.456192, 'Constancia'))
points.append(Mining(-71.386177, -14.963872, 'Antapaccay'))
points.append(Mining(-70.842099, -15.277586, 'Apumayo'))
points.append(Mining(-73.688106, -15.055361, 'Breapampa'))
points.append(Mining(-70.77731, -15.093469, 'Las Aguilas'))

points.append(Mining(-71.856156, -15.164604, 'San Cristobal'))
points.append(Mining(-75.124649, -15.202603, 'Relaves Shouxin'))
points.append(Mining(-75.222943, -15.269746, 'Marcona'))
points.append(Mining(-70.842099, -15.277586, 'Andres'))
points.append(Mining(-74.266, -15.36, 'Santa Filomena'))
points.append(Mining(-70.727258, -15.627999, 'Tacaza'))
points.append(Mining(-74.248, -15.803, 'Veta Dorada'))
points.append(Mining(-71.570247, -16.534078, 'Cerro Verde'))
points.append(Mining(-70.162167, -16.644044, 'Mariela'))
points.append(Mining(-70.785977, -17.067197, 'Cuajone'))
points.append(Mining(-70.614679, -17.24351, 'Toquepala'))
points.append(Mining(-69.813377, -17.818876, 'Pucamarca'))
'''

#Minas Subterraneas
'''
points.append(Mining(-77.624517, -7.687404, 'Poderosa'))
points.append(Mining(-77.570993, -7.765597, 'Maria Antioneta'))
points.append(Mining(-77.561, -7.775, 'San Benito'))
points.append(Mining(-77.579045, -7.763368, 'Libertad'))
points.append(Mining(-77.557159, -8.033611, 'Parcoy'))
points.append(Mining(-78.318439, -8.003906, 'Quiruvilca'))
points.append(Mining(-76.644953, -11.136961, 'Santa Rosa'))
points.append(Mining(-77.856, -8.151, 'Sauco'))
points.append(Mining(-77.068134, -9.499548, 'Contonga'))
points.append(Mining(-77.531, -9.753, 'Huancapeti'))
points.append(Mining(-77.040085, -9.823863, 'El Recuerdo'))
points.append(Mining(-77.000369, -9.878114, 'Santa Luisa'))
points.append(Mining(-76.755245, -10.449452, 'Raura'))
points.append(Mining(-76.216735, -10.575373, 'Atacocha'))
points.append(Mining(-76.675513, -10.616787, 'Uchucchacua'))
points.append(Mining(-76.213095, -10.625513, 'El porvenir'))
points.append(Mining(-76.860033, -10.692203, 'Mallay'))
points.append(Mining(-76.428345, -11.007897, 'Huaron'))
points.append(Mining(-76.431686, -11.029021, 'Animon'))
points.append(Mining(-75.377619, -11.1975, 'Palmpata'))
points.append(Mining(-76.520676, -11.193873, 'Santander'))
points.append(Mining(-75.38943, -11.229181, 'San Vicente'))
points.append(Mining(-77.270982, -11.491858, 'María Teresa'))
points.append(Mining(-76.186123, -11.57004, 'Ticlio'))
points.append(Mining(-76.146862, -11.596737, 'Austria Duvaz'))
points.append(Mining(-76.171596, -11.637246, 'Anticona'))
points.append(Mining(-76.096077, -11.628891, 'Manuelita'))
points.append(Mining(-76.137712, -11.625547, 'Morococha'))
points.append(Mining(-76.199576, -11.698612, 'Casapalca'))
points.append(Mining(-76.009072, -11.690606, 'Morada'))
points.append(Mining(-76.199576, -11.698612, 'Americana'))
points.append(Mining(-76.644953, -11.136961, 'Colombia y S. Santa Rosa'))
points.append(Mining(-76.070389, -11.740413, 'Carahuacra'))
points.append(Mining(-76.026687, -11.79278, 'Andaychagua'))
points.append(Mining(-71.856156, -15.164604, 'San Cristobal'))
points.append(Mining(-75.704212, -12.329177, 'Yauricocha'))
points.append(Mining(-75.684, -12.41, 'San Pedro'))
points.append(Mining(-74.3972, -12.565994, 'Cobriza'))
points.append(Mining(-76.590548, -12.604568, 'Condestable'))
points.append(Mining(-74.810641, -12.946424, 'Julcani'))
points.append(Mining(-75.97849, -13.079805, 'Cerro Lindo'))
points.append(Mining(-74.984397, -13.069512, 'Huachocolpa'))
points.append(Mining(-73.935247, -13.981952, 'Catalina Huanca'))
points.append(Mining(-70.4916, -14.1335, 'San Rafael'))
points.append(Mining(-69.2257, -14.2858, 'Cori Riqueza'))
points.append(Mining(-69.367, -14.588, 'Qori Untuca'))
points.append(Mining(-73.179717, -14.747029, 'Pallancata'))
points.append(Mining(-73.248832, -14.950542, 'Inmaculada'))
points.append(Mining(-72.320719, -14.980069, 'Arcata'))
points.append(Mining(-71.74813, -15.072096, 'Suyckutambo'))
points.append(Mining(-72.351576, -15.27263, 'Orcopampa'))
points.append(Mining(-71.8298268, -15.1727649459291, 'El Santo'))
points.append(Mining(-74.033242, -15.624255, 'Capitana'))
points.append(Mining(-73.944196, -15.622676, 'Tambojasa'))
points.append(Mining(-74.076, -15.644, 'Chacchuille'))
points.append(Mining(-73.864818, -15.741468, 'Doble D'))
points.append(Mining(-71.914662, -15.47118, 'Tambomayo'))
points.append(Mining(-73.045546, -15.897427, 'San Juan'))
points.append(Mining(-74.244911, -15.826292, 'Belen'))
points.append(Mining(-74.411041, -14.5722616, 'Los Incas'))
'''

#Unidades mineras no metálicas
'''
points.append(Mining(-81.075005, -5.203232, 'Lucita'))
points.append(Mining(-80.540553, -5.573904, 'Fospac'))
points.append(Mining(-80.765537, -5.922773, 'Virrila'))
points.append(Mining(-80.592, -5.979, 'Bayovar 12'))
points.append(Mining(-80.837945, -6.103152, 'Bayovar 2'))
points.append(Mining(-77.322369, -5.950679, 'Cem. Selva'))
points.append(Mining(-77.017, -6.064, 'Moyobamba'))
points.append(Mining(-79.718, -6.629, 'Tres tomas'))
points.append(Mining(-76.267, -6.742, 'Pilluana'))
points.append(Mining(-78.471, -6.927, 'China Linda'))
points.append(Mining(-79.124, -7.247, 'Tembladera'))
points.append(Mining(-79.553, -7.383, 'Pacasmayo'))
points.append(Mining(-78.63, -8.88, 'Adolfo'))
points.append(Mining(-76.699, -10.748, 'Oyon'))
points.append(Mining(-77.561088, -11.279766, 'Quimpac'))
points.append(Mining(-75.813437, -11.374854, 'Cem. Andino'))
points.append(Mining(-75.045, -11.369, 'Silical'))
points.append(Mining(-75.450134, -11.431366, 'Chacapalpa'))
points.append(Mining(-76.139792, -11.656098, 'Tunshuruco'))
points.append(Mining(-76.931698, -11.785591, 'Yerba Buena'))
points.append(Mining(-77.037156, -11.815306, 'Comicsa'))
points.append(Mining(-76.890794, -11.951853, 'Unicon'))
points.append(Mining(-76.876884, -12.188936, 'Atocongo'))
points.append(Mining(-76.90882285, -12.19216514, 'Unacem'))
points.append(Mining(-76.43173, -12.435866, 'Concremax'))
points.append(Mining(-76.30297, -12.452594, 'San Lorenzo'))
points.append(Mining(-76.530467, -12.73648, 'Promesa'))
points.append(Mining(-76.16, -13.64, 'Las dunas'))
points.append(Mining(-76.234211, -14.005146, 'Otuma'))
points.append(Mining(-71.34, -15.44, 'Calquipa'))
points.append(Mining(-70.136523, -15.609905, 'Puno'))
points.append(Mining(-71.778723, -16.206498, 'Yura'))
points.append(Mining(-71.12869674, -16.41033235, 'Incabor'))
'''

#Fundiciones y Refinerías
points.append(Mining(-75.922555, -11.518649, 'La oroya'))
points.append(Mining(-76.881772, -11.966871, 'Cajamarquilla'))
points.append(Mining(-76.174081, -13.779953, 'Funsur'))
points.append(Mining(-71.21915, -17.343, 'Ilo'))

convexHull(points, len(points))
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

convexHull(points, len(points))
# Este archivo corresponde al Ejercicio 1 de la guía práctica sobre Clases.
# Aquí deberás implementar la clase Camion y resolver los puntos a, b, c, d y f según las consignas

class Camion:
    patentes=[]
    camiones=[]
    def __init__(self, patente: str, marca: str,carga: int, anio: int):
        self.patente = patente
        self.marca = marca
        self.carga = carga
        self.anio = anio
        if self.patente in Camion.patentes:
            raise ValueError ('La patente del camión que se quiere registrar, ya existe. Intente con otra patente.')
        else:
            Camion.patentes.append(self.patente)
            Camion.camiones.append(self)
        

    def __str__(self):
        return f"Camión: #{self.patente} \nCarga: {self.carga} \nMarca: {self.marca} \nAño: {self.anio}"
    
    def __eq__(self,other):
        if isinstance(other,Camion):
            return (self.patente==other.patente)
        return False
    
    def getter_pat(self):
        return self.patente
    
    def getter_carga(self):
        return self.carga
    
    def getter_marca(self):
        return self.marca
    
    def getter_anio(self):
        return self.anio
    
    def setter_pat(self,patente: str):
        self.patente=patente
        
    def setter_carga(self,carga: int):
        self.carga=carga
    
    
        
        
    
furgon1 = Camion("ABC123", "Mercedes", 1000, 2020)
furgon2 = furgon1
furgones = [
    ("AAA111", "Mercedes", 1200, 2018),
    ("BBB222", "Volvo", 1500, 2019),
    ("CCC333", "Scania", 1800, 2020),
    ("DDD444", "Iveco", 1000, 2017),
    ("EEE555", "Renault", 1300, 2021),
    ("FFF666", "Ford", 1100, 2016),
    ("GGG777", "MAN", 2000, 2022),
    ("HHH888", "Peugeot", 900, 2015),
    ("III999", "Toyota", 1400, 2023),
    ("JJJ000", "Hyundai", 1600, 2024),
]
for pat, marca, carga, anio in furgones:
    Camion(pat, marca, carga, anio)

# furgon3 = Camion("DEF456", "Volvo", 2000, 2021)
# furgon4 = Camion("ABC123", "Mercedes", 1000, 2020)


# print(furgon1 == furgon2) #Como no hay eq definido, se fija si ambos elementos tienen
# #la misma dirección de memoria. Como esto es cierto, devuelve True.
# print(furgon1 is furgon2) #Debería dar true ya que el is se fija en la dirección de memoria y en este caso son iguales.
# print(furgon3 == furgon4) #Son distintos, da False.
# print(furgon3 is furgon4) # Son distintos, da False.
# print(furgon1 == furgon4) #Como no hay eq definido, se fija la direc de memoria. Son distintas, por lo tanto da false.
# print(furgon2)

def regi_nuev_camion():
    check=False
    while check==False:
        check=True
        npat=input('Ingrese la patente del camión:')
        nmarca=input('Ingrese la marca del camión:')
        ncarga=input('Ingrese la carga del camión:')
        nanio=input('Ingrese el anio del camión:')
        for i in range(len(nanio)):
            if not nanio[i].isdigit():
                check=False
                print('El año ingresado es inváido.')
        for i in range(len(ncarga)):
            if not ncarga[i].isdigit():
                check=False
                print('El valor de carga ingresado es inválido.')
        if check:
            nanio=int(nanio)
            ncarga=int(ncarga)
            Camion(npat,nmarca,ncarga,nanio)
            print(f'El camión con patente {npat}, marca {nmarca}, carga {ncarga} y año {nanio} fue registrado con éxito.')
        
def modificar_carga():
    check=False
    while not check:
        check=True
        pat=input('Ingrese la patente del camión el cual quiere modificar la carga:')
        if pat not in Camion.patentes:
            check=False
            print('La patente ingresada no está registrada, vuelva a intentarlo.')
    check=False
    while not check:
        check=True
        carga=(input('Ingrese la nueva carga del camión:'))
        for i in range(len(carga)):
            if not carga[i].isdigit():
                check=False
                print('El valor de carga ingresado no es válido. Vuelva a intentarlo.') 
        if check:
            if int(carga)<=0:
                check=False
                print('El valor de carga ingresado no es válido. Vuelva a intentarlo.') 
    for cam in Camion.camiones:
        if cam.patente==pat:
            furgon=cam            
    furgon.setter_carga(int(carga))
    print(f'Se modificó con éxito el valor de la carga a {carga}.')
    
def mostrar_lista_camiones():
    lanios=[]
    lcam=[]
    lista=[]
    for cam in Camion.camiones:
        lanios.append((cam.getter_anio(),cam))
    lanios=sorted(lanios, key=lambda x: x[0])
    for i in range(len(lanios)):
        lcam.append((lanios[i])[1])
    for cam in lcam:
        lista.append(cam.__str__())
    print (lista)
    
def mostrar_marca_moda():
    lmarcas=[]
    for furgon in Camion.camiones:
        lmarcas.append(furgon.getter_marca())
    marca_moda=max(lmarcas, key=lmarcas.count)
    print(f'La marca con más camiones registrados es: {marca_moda}.')
            
    
        

def menu():
    check=False
    while not check:
        opc=input('1. Registrar un nuevo camión.\n2. Modificar la carga de un camión.\n3. Mostrar por terminal la lista de camiones registrados, del más antiguo al más moderno.\n4. Mostrar por terminal la marca que más veces fue registrada.\nElija una de las anteriores opciones:')
        if  opc in ['1','2','3','4']:
            check=True
        else:
            print('El valor ingresado no se encuentra dentro de las opciones válidas.')
    if opc=='1':
        regi_nuev_camion()
    if opc=='2':
        modificar_carga()
    if opc=='3':
        mostrar_lista_camiones()
    if opc=='4':
        mostrar_marca_moda()
          
menu()




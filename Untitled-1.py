#Herencia: Sivre unicamente para reutilizar código.
from ejercicio2 import Computadora # para que me deje hacer esto debo tener ambos archivos en la misma carpeta.

#Super computodara hereda de Computadora todos los atributos y métodos propios.
#A su vez agrega sus atributos y métodos propios.

class Supercomputadora(Computadora):
    def __init__(self, id:int, marca: str, modelo:str, cpu: str,  gpu: str, so: str,IA_adoptada:str, generacion:str, pais_origen='Israel' ,ram_gb= 32,  almacenamiento_gb=256):
        super().__init__(id, marca, modelo, cpu, gpu, so, ram_gb, almacenamiento_gb) #Directamenete usa el init anterior
        #Otra forma de hacerlo sería:
        #Computadora.__init__(self, marca, modelo, cpu, gpu, so, ram_gb, almacenamiento_gb)
        self.id=id
        self.marca= marca
        self.modelo=modelo
        self.cpu=cpu
        self.gpu=gpu
        self.so=so
        self.ram_gb=ram_gb
        self.almacenamiento_gb=almacenamiento_gb
        self.IA_adoptada=IA_adoptada
        self.generacion=generacion
        self.pais_origen=pais_origen
        
    def __str__(self): #Polimorfismo, puedo modificar un método acá. 
        frase_saludo=super().__str__()
        if not self.IA_adoptada:
            IA_adoptada='Chat GPT'
        
        return f'{frase_saludo} Esta es una super-computadora con {self.IA_adoptada} IA adoptada, de generación {self.generacion} originada en {self.pais_origen}.'
try:
    supercompu=Supercomputadora(5,'Bangho','X6','Intel_i9_2022', 'Nvidia_xp2344', 'Windows 11','Deep_Seek','5.0')
    print(supercompu)
except Exception as e:
    print ('El error es:',e)
    
    
    
#Herencia multiple: 2 clases padres, 1 clase hija. NO se puede usar super() para el __init__

#El objeto que creo a la izquierda es la clase predominante. 
# Esto significa que ante cualquier decisión que tenga que tomar el 
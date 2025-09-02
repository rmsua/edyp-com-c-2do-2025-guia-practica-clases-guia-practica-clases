# Ejercicio 2: Modelar una computadora
# 
# En este archivo debés crear la clase Computadora siguiendo las consignas del README.
# Recordá:
# - Definir atributos relevantes en el constructor (__init__), con valores por defecto.
# - Implementar el método __str__ para mostrar la información esencial.
# - Instanciar al menos 3 computadoras con distintos valores.
# - Llevar la cuenta de computadoras creadas (usar variable de clase).
# - Implementar al menos 2 métodos de los sugeridos (updateOS, PM, addRAM, getCapacity).
# - Crear otra clase para un componente (ej: Disco, RAM, etc.) con su propio __init__, __str__ y al menos un método.
# 
# ¡No olvides probar todos los métodos y comentar tu criterio para los valores

class Computadora:
    cantidad=0 #Atributo de clase
    computadoras=[] #Atributo de clase
    def __init__(self, id:int, marca: str, modelo:str, cpu: str,  gpu: str, so: str, ram_gb= 32, almacenamiento_gb=256,):
        id
        self.id=id
        self.marca = marca #Atributos de instancia
        self.modelo = modelo #Atributos de instancia
        self.cpu = cpu
        self.ram_gb = ram_gb
        self.almacenamiento_gb = almacenamiento_gb
        self.gpu = gpu
        self.so = so
        Computadora.computadoras.append(self)
        Computadora.cantidad+=1
    #cada vez que creo un método de clase, es necesario que yo llame al decorador @classmethod.  
    
    
    # Importante: Los métodos de instancias son funciones dentro de una clase que usan a los atributos de instancias
    # Los métodos de instancia usan SELF como parametro de entrada.
    #Los métodos de clase, usan atributos de clase. Requieren usar el decorador de @classmethod antes de definir el método
    #Dentro de la definicón del método reciben como atributos
    @classmethod
    def mostrar_contador_libros(cls): #como es un método de clase, le agrego 
        print(f'Hasta el momento se registaron {cls.cantidad} computadoras.')
        
    def __str__(self):
        return f'Esta computadora tiene id {self.id}, es de marca {self.marca}, modelo {self.modelo} con cpu {self.cpu}. Tiene RAM={self.ram_gb} y almacenamiento={self.almacenamiento_gb}.'
    def getter_id(self):
        return self.id    
    def getter_ram_gb(self):
        return self.ram_gb
    def getter_cpu(self):
        return self.cpu 
    def getter_gpu(self):
        return self.gpu 
    def getter_almacenamiento_gb(self):
        return self.almacenamiento_gb
    
    def addRAM (self,new_ram:int):#Instala un nuevo módulo de RAM en la computadora.
        if isinstance (new_ram, int) and new_ram>0:
            self.ram_gb=new_ram
            print(f'Se ha actualizado la memoria ram de la computadora a {self.ram_gb} GygaBytes.')
        else:
            print ('La ram ingresada no es válida.')
            
    def getCapacity (self, hard:str):
        hard=hard.lower()
        capacidad=''
        if hard not in ['cpu','gpu','ram_gb','almacenamiento_gb']:
            print('El elemento de hardware ingresado no es válido.Intente nuevamente.')
        else:
            if hard=='cpu':
                capacidad= self.getter_cpu()
            if hard=='gpu':
                capacidad= self.getter_gpu()
            if hard=='ram_gb':
                capacidad= self.getter_ram_gb()
            if hard=='almacenamiento_gb':
                capacidad= self.getter_almacenamiento_gb()
        print (f'El componente de hardware elgido es {hard} y su capacidad es {capacidad}.')
            
if __name__=='__main__': #Esto verifica que seamos nostros los que estemos queriendo correr el código. Si no somos nostros corriendolo, no se corre.
    compu1=Computadora(1,'Bangho','X6','Intel_i9_2022', 'Nvidia_xp2344', 'Windows 11')
    compu2=Computadora(2,'Apple','Mac Pro 2016','MA2300','Nvidia_100', 'IOS_15',64,1000)
    compu3=Computadora(3,'HP','Sonic_3','Intel_i11','Wolf234','Windows 14',36)
    cantidad_computadoras=Computadora.cantidad
    Computadora.mostrar_contador_libros()
    print(compu1)
    compu1.addRAM(26)
    compu2.getCapacity('almacenamiento_gb')
    
    
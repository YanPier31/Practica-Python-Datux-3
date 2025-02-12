class Conductor:
    def __init__(self, nombre, codigo):
        self.nombre = nombre
        self.codigo = codigo
        self.horarios = set()

    def asignar_horario(self, hora):
        if hora in self.horarios:
            print(f"El conductor {self.nombre} ya tiene asignado el horario {hora}.")
            return False
        self.horarios.add(hora)
        return True


class Bus:
    def __init__(self, placa):
        self.placa = placa
        self.ruta = None
        self.horarios = set()
        self.conductor = None
    
    def asignar_ruta(self, ruta):
        self.ruta = ruta
    
    def registrar_horario(self, hora):
        self.horarios.add(hora)
    
    def asignar_conductor(self, conductor):
        if self.horarios.intersection(conductor.horarios):
            self.conductor = conductor
            print(f"Conductor {conductor.nombre} asignado al bus {self.placa}.")
        else:
            print(f"No se puede asignar a {conductor.nombre} al bus {self.placa} debido a conflictos de horario.")


class Admin:
    def __init__(self):
        self.buses = []
        self.conductores = []
    
    def agregar_bus(self, placa):
        self.buses.append(Bus(placa))
    
    def agregar_conductor(self, nombre, codigo):
        self.conductores.append(Conductor(nombre, codigo))
    
    def mostrar_menu(self):
        while True:
            print("\n1. Agregar Bus\n2. Agregar Ruta a Bus\n3. Registrar Horario a Bus\n4. Agregar Conductor\n5. Asignar Horario a Conductor\n6. Asignar Bus a Conductor\n7. Salir")
            opcion = input("Seleccione una opción: ")
            
            if opcion == "1":
                placa = input("Ingrese la placa del bus: ").upper()
                bus = next((b for b in self.buses if b.placa == placa), None)
                if bus:
                    print("El bus ya está registrado.")
                else:
                    self.agregar_bus(placa)
                    print("El bus ha sido agregado con éxito.")
            elif opcion == "2":
                placa = input("Ingrese la placa del bus: ").upper()
                bus = next((b for b in self.buses if b.placa == placa), None)
                if bus:
                    if bus.ruta:  
                        print(f"Este bus ya tiene una ruta asignada: {bus.ruta}.")
                    else:
                        ruta = input("Ingrese la ruta: ")
                        bus.asignar_ruta(ruta)  
                        print("Ruta asignada con éxito.")
                else:
                    print("El bus no se encuentra registrado.")
            elif opcion == "3":
                placa = input("Ingrese la placa del bus: ").upper()
                bus = next((b for b in self.buses if b.placa == placa), None)
                if bus:
                    if bus.horarios:
                        print(f"Este bus ya tiene un horario asignado: {bus.horarios}.")
                    else:
                        hora = input("Ingrese horario (horas:minutos): ")
                        bus.registrar_horario(hora)
                        print("Horario registrado con éxito.")
                else:
                    print("Bus no encontrado.")
            elif opcion == "4":
                nombre = input("Ingrese el nombre del conductor: ")
                codigo = input("Ingrese el código del conductor: ")
                conductor = next((c for c in self.conductores if c.codigo == codigo), None)
                if not conductor:
                    self.agregar_conductor(nombre, codigo)
                    print(f"Conductor {nombre} agregado con éxito.")
                else:
                    print(f"El conductor con código {codigo} ya está registrado.")
            elif opcion == "5":
                codigo = input("Ingrese el código del conductor: ")
                hora = input("Ingrese horario (horas:minutos): ")
                conductor = next((c for c in self.conductores if c.codigo == codigo), None)
                if conductor:
                    if hora not in conductor.horarios:  
                        conductor.horarios.add(hora) 
                        print("Horario asignado con éxito.")
                    else: 
                        print(f"El conductor {conductor.nombre} ya tiene un horario asignado: {conductor.horarios}.")
                else:
                    print("El conductor no está registrado.")
            elif opcion == "6":
                placa = input("Ingrese la placa del bus: ").upper()
                codigo = input("Ingrese el código del conductor: ")
                bus = next((b for b in self.buses if b.placa == placa), None)
                conductor = next((c for c in self.conductores if c.codigo == codigo), None)
                if bus and conductor:
                    if bus.conductor:
                        print(f"El bus {bus.placa} ya tiene asignado al conductor {bus.conductor.nombre}.")
                    else:
                        bus.asignar_conductor(conductor)
            elif opcion == "7":
                break
            else:
                print("Eliga una opción correcta (1-7).")


if __name__ == "__main__":
    admin = Admin()
    admin.mostrar_menu()
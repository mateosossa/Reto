from collections import deque

class Turno:
    def __init__(self, id, categoria):
        self.id = id
        self.categoria = categoria

    def __repr__(self):
        return f"{self.id}\ncategoria: {self.categoria}\n"

class SistemaDeTurnos:
    def __init__(self):
        self.prioritario = deque()
        self.buena_gente = deque()
        self.cliente_normal = deque()
        self.contador_buena_gente = 0
        self.contador_cliente_normal = 0

    def agregar_turno(self, turno):
        if turno.categoria == 'Prioritario':
            self.prioritario.append(turno)
        elif turno.categoria == 'Buena Gente':
            self.buena_gente.append(turno)
        elif turno.categoria == 'Cliente Normal':
            self.cliente_normal.append(turno)
        else:
            raise ValueError("Categoría de turno no válida")

    def llamar_turno(self):
        if self.prioritario:
            return self.prioritario.popleft()

        if self.buena_gente and self.cliente_normal:
            if self.contador_buena_gente < 3:
                self.contador_buena_gente += 1
                return self.buena_gente.popleft()
            else:
                self.contador_cliente_normal += 1
                if self.contador_cliente_normal == 2:
                    self.contador_buena_gente = 0
                    self.contador_cliente_normal = 0
                return self.cliente_normal.popleft()

        if self.buena_gente:
            return self.buena_gente.popleft()

        if self.cliente_normal:
            return self.cliente_normal.popleft()

# Ejemplo de uso
if __name__ == "__main__":
    sistema = SistemaDeTurnos()

    turnos = [
        Turno(1, 'Prioritario'),
        Turno(2, 'Buena Gente'),
        Turno(3, 'Cliente Normal'),
        Turno(4, 'Buena Gente'),
        Turno(5, 'Cliente Normal'),
        Turno(6, 'Buena Gente'),
        Turno(7, 'Prioritario'),
        Turno(8, 'Cliente Normal'),
        Turno(9, 'Prioritario'),
        Turno(10, 'Buena Gente'),
        Turno(11, 'Cliente Normal'),
        Turno(12, 'Buena Gente'),
        Turno(13, 'Cliente Normal'),
        Turno(14, 'Buena Gente'),
        Turno(15, 'Cliente Normal'),
        Turno(16, 'Buena Gente'),
        Turno(17, 'Cliente Normal')
    ]

    for turno in turnos:
        sistema.agregar_turno(turno)

    while any([sistema.prioritario, sistema.buena_gente, sistema.cliente_normal]):
        input("Para llamar turno, presiona la tecla Enter.")
        turno_llamado = sistema.llamar_turno()
        if turno_llamado:
            print(f"Turno llamado: {turno_llamado}")
        else:
            print("No hay más turnos disponibles.")

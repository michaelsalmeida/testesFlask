from datetime import datetime


def get_current_datetime():
    """Returns the current date and time."""
    return datetime.datetime.now()



def format_datetime(dt):
    """Formats a datetime object into a string."""
    return dt.strftime("%Y-%m-%d %H:%M:%S")

def cargaHoraria(horario_entrada: str, horario_saida: str):
    """Calculates the workload between two time strings."""

    entrada = datetime.strptime(horario_entrada, "%H:%M")
    saida = datetime.strptime(horario_saida, "%H:%M")

    carga_horaria = saida - entrada
    return carga_horaria

a = '-08:00'

b = a.split(':')

print(b)
from datetime import date, datetime
import re

def rut_valido(rut: str) -> bool:
    """
    Valida un RUT chileno (con o sin puntos y guion).
    Retorna True si es válido y False en caso contrario.
    """
    # Limpiar el RUT: eliminar puntos, guiones y llevar 'k' a mayúscula
    rut_limpio = rut.upper().replace(".", "").replace("-", "").strip()
    
    if len(rut_limpio) < 2:
        return False
        
    cuerpo = rut_limpio[:-1]
    dv = rut_limpio[-1]
    
    # El cuerpo debe ser numérico y el DV debe ser número o 'K'
    if not cuerpo.isdigit() or dv not in "0123456789K":
        return False
        
    # Algoritmo Módulo 11
    suma = 0
    multiplicador = 2
    
    for digito in reversed(cuerpo):
        suma += int(digito) * multiplicador
        multiplicador += 1
        if multiplicador > 7:
            multiplicador = 2
            
    resto = suma % 11
    esperado = 11 - resto
    
    if esperado == 11:
        dv_calculado = "0"
    elif esperado == 10:
        dv_calculado = "K"
    else:
        dv_calculado = str(esperado)
        
    return dv == dv_calculado


def formatear_rut(rut: str) -> str:
    limpio = rut.upper().replace(".", "").replace("-", "").strip()
    cuerpo, dv = limpio[:-1], limpio[-1]
    return f'{int(cuerpo):,}'.replace(',', '.') + '-' + dv


def correo_valido(correo: str) -> bool:
    patron = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(patron, correo) is not None


def fecha_nacimiento_valida(texto: str):
    if not re.match(r'^\d{2}/\d{2}/\d{4}$', texto):
        return None
    try:
        fecha = datetime.strptime(texto, '%d/%m/%Y').date()
    except ValueError:
        return None
    if fecha > date.today() or fecha.year < 1900:
        return None
    return fecha


def errores_contrasenia(contrasenia: str) -> list:
    errores = []
    if len(contrasenia) < 8:
        errores.append('Debe tener al menos 8 caracteres.')
    if len(contrasenia) > 60:
        errores.append('No puede superar los 60 caracteres.')
    if not any(c.isdigit() for c in contrasenia):
        errores.append('Debe tener al menos 1 número.')
    if not any(c.islower() for c in contrasenia):
        errores.append('Debe tener al menos 1 minúscula.')
    if not any(c.isupper() for c in contrasenia):
        errores.append('Debe tener al menos 1 mayúscula.')
    if not any(c in '@$#!*&' for c in contrasenia):
        errores.append('Debe tener al menos 1 carácter especial: @ $ # ! * &')
    return errores
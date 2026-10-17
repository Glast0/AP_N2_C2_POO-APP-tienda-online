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
from presentacion import menu_principal
from presentacion.presentacion_usuario import iniciar_sesion

if iniciar_sesion():
    menu_principal()
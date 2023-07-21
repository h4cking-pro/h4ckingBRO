# h4ckingBRO
Bot para el servidor de Discord de h4ckingPRO

## Instalación
1. Clonar el repositorio
2. Instalar las dependencias con `pip install -r requirements.txt`
3. Crear el archivo de configuracion con el siguiente contenido:
```json
{
    "TOKEN": "",
    "PREFIX": "/",
    "OWNER_ID": "",
    "APPLICATION_ID": ""
}
```
Donde:
- `TOKEN` es el token del bot
- `PREFIX` es el prefijo del bot
- `OWNER_ID` es el ID del dueño del bot
- `APPLICATION_ID` es el ID de la aplicación del bot

Estos datos se pueden obtener en el [portal de desarrolladores de Discord](https://discord.com/developers/applications) en la sección de aplicaciones.


4. Ejecutar el bot con `python3 h4ckingBRO.py`
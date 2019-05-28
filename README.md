# GSONIC

## Descarga 
  * [Soni.md](https://drive.google.com/file/d/1Re4AMED8gcfD2M02xjKh6Ex-G91a8pYb/view)<br>
  * [sonic.py](https://drive.google.com/file/d/1-kHaBaKDEFAGSO1p1t6I0DA1GyCC1TBs/view)
  
## Procedimiento de instalacion :
 * Creen una carpeta y dentro de ella ejecutar:
   ```console
       virtualenv -p python3 env
        source env/bin/activate
       pip3 install gym-retro  
	```

 * Creen una carpeta llamada roms dentro de la carpeta que se creó y colocar el archivo md de sonic. 
   Ejecutar:
    ``` console
      python3 -m retro.import roms
   ```

* Colocar el archivo controlador (sonic.py) dentro de la carpeta ya creada, y ejecutar
    ``` console
       python sonic.py
   ```
### Si sonic se mueve, entonces ya funciona.

## Instruciones del controlador.
Para aprovechar el uso del controlador, basta con copiar o descargar el archivo sonic.py de este repositorio
pegarlo en la carpeta de instalacion, reemplazar y listo.

Para correrlo: 
```Console
  source env/bin/activate
  python sonic.py
  ``` 
  
El controlador de sonic consiste en 4 teclas las cuales se detallaran su funcionamiento:
 * movimiento de saltar
 * correr
 * retroceder 
 * abajo

Teniendo en cuenta que el controlador de sonic esta desarrollado para que avance hasta completar el nivel 1, en el cual estas pasadas se proceden a guardar en un archivo csv para una recoleccion de data.

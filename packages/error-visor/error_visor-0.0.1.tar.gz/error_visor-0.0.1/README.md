# Error Visor

## Que es?
Es un proyecto destinado a guardar registros personalizados en un archivo json que será utilizado
más tarde para visualizarse en una app web de forma localizada y ordenada. Solo es necesaria una
sentencia y listo, ya tienes el registro del error en tu app.

## Cómo funciona?

Primero importamos el módulo:

```python
import error_visor as EV
```

Luego localizamos el lugar desde donde queremos mandar el log. Por ejemplo un bloque `exception` y
colocamos el siguiente código:

```python
except Exception as ex:

	EV.Logger.err(
		EV.Error(
			description='Error de muestra',
			priority=EV.Priority.HIGH,
			ex=ex
		)
	)

```

Y listo, tendremos el registro en un json!

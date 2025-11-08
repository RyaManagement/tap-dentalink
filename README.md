# tap-dentalink

`tap-dentalink` es un tap de Singer para Healthatom Dentalink.

Un proyecto de [R&A Management](https://ryamanagement.com/).
Síguenos en nuestra página de Instagram [@rya_management](https://www.instagram.com/rya_management/).

Construido con [Meltano Tap SDK](https://sdk.meltano.com) para Taps de Singer.
Inspirado en [Dentalink Client](https://github.com/Keviinplz/dentalink) por @Keviinplz

## Qué puede hacer el usuario con este tap

Con `tap-dentalink` puedes extraer los datos de Dentalink y volcarlos a **cualquier formato soportado por los taps de Singer**, tales como:

- **CSV** – para análisis rápido en hojas de cálculo o herramientas de BI.
- **JSON / JSONL** – ideal para procesamiento programático o carga en data lakes.
- **PostgreSQL** – inserta directamente los datos en una base de datos relacional para consultas avanzadas.
- **Otros destinos compatibles** – por ejemplo, Snowflake, BigQuery, Redshift, etc., mediante los *targets* de Singer correspondientes.

En resumen, el tap permite **bajar los datos de Dentalink** y enviarlos a la herramienta o almacenamiento que prefieras, facilitando la integración de tu información clínica con pipelines de ELT, análisis de datos o visualizaciones personalizadas.

## Instalación

Instalar desde Github con pip/pipx:

```bash
pipx install git+https://github.com/RyaManagement/tap-dentalink.git@main
```

## Configuracion

### Configuraciones disponibles

- **Nombre:** auth_token  
  **Tipo:** ['string']  
  **Variable de Entorno:** TAP_DENTALINK_AUTH_TOKEN  
  **Descripción:** Token de autenticación para acceder a la API de Dentalink.

- **Nombre:** api_url  
  **Tipo:** ['string', 'null']  
  **Variable de Entorno:** TAP_DENTALINK_API_URL  
  **Descripción:** URL base de la API de Dentalink. Si no se especifica, se usará la URL por defecto.

- **Nombre:** backoff_retries  
  **Tipo:** ['integer', 'null']  
  **Variable de Entorno:** TAP_DENTALINK_BACKOFF_RETRIES  
  **Descripción:** Número de reintentos en caso de fallos temporales en la API.

- **Nombre:** start_date  
  **Tipo:** ['string']  
  **Variable de Entorno:** TAP_DENTALINK_START_DATE  
  **Descripción:** Fecha inicial para la extracción de datos (formato ISO YYYY-MM-DD).

- **Nombre:** end_date  
  **Tipo:** ['string', 'null']  
  **Variable de Entorno:** TAP_DENTALINK_END_DATE  
  **Descripción:** Fecha final para la extracción de datos (formato ISO YYYY-MM-DD). Opcional.


La lista completa de configuraciones disponibles para este tap se obtiene ejecutando:

```bash
tap-dentalink --about
```

El tap se puede configurar a través de un archivo ´config.json´ o a través de variables de entorno.

## Uso

Una vez configurado 
Es posible ejecutar este tap directamente con `tap-dentalink` o como parte de un pipeline usando [Meltano](https://meltano.com/).

### Ejecutando el tap directamente

Extraer información

```bash
tap-dentalink --version
tap-dentalink --help
```

Extraer datos de la API de Dentalink a través del tap:

```bash
tap-dentalink --config CONFIG > datos_dentalink.singer.json
```

Este archivo de datos se puede transformar a otros formatos utilizando otros Singer taps.

Se puede utilizar un catálogo para con el fin de elegir recursos para extraer:

```bash
tap-dentalink --config config.json --discover > catalog.json
tap-dentalink --config config.json --catalog catalog.json
```
En este caso, se puede modificar la opción "selected" de cada stream (´true´ o ´false´) para incluir o excluir un stream.

Es posible redirigir las salida de un tap en la entrada de otro. Por ejemplo, el siguiente comando redirige el contenido
de la API de Dentalink a un archivo CSV a través de [tap-csv](https://github.com/MeltanoLabs/tap-csv):

```bash
# Extraer datos y enviarlos a target-csv
tap-dentalink --config config.json --catalog catalog.json | target-csv --output ./csv_output
```

## Instrucciones para desarrolladores

Sigue las siguientes instrucciones para contribuir a este proyecto.

### Inicializa un entorno de desarrollo

Prerequisitos:

- Python 3.9+
- [uv](https://docs.astral.sh/uv/)

```bash
uv sync
```

### Crear y ejecutar tests

Crea tests demtro del subdirectorio `tests` y luego ejecuta:

```bash
uv run pytest
```

Tambien puedes probar la interfaz de commandos del tap `tap-dentalink` directamente utilizando `uv run`:

```bash
uv run tap-dentalink --help
```

### Ejecución con [Meltano](https://www.meltano.com)

**Nota:** 
Este tap funciona con cualquier entorno de Singer y no require Meltano para su uso. Los siguientes ejemplos muestran maneras convenientes de realizar orquestación end-to-end.

Instala Meltano (si aún no lo realizas) y las dependencias de plugins:

```bash
# Instalar meltano
pipx install meltano
# Inicializar meltano dentro de este directorio
cd tap-dentalink
meltano install
```

Ahora puedes orquestar con Meltano:

```bash
# Invocar meltano:
meltano invoke tap-dentalink --version

# O ejecutar un pipeline ELT de prueba:
meltano run tap-dentalink target-jsonl
```

### Guia de desarrollo SDK

Visita la [guía de desarrollo](https://sdk.meltano.com/en/latest/dev_guide.html) para más instrucciones de como utilizar el SDK y desarrollar tus propios taps y targets.

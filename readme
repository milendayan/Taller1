# Taller Google GenAI - Inteligencia Artificial

## Descripción

Este proyecto implementa tres ejercicios en Python utilizando la librería **Google GenAI (`google-genai`)** para realizar peticiones a modelos de Gemini, procesar textos y gestionar conversaciones interactivas.

Los ejercicios desarrollados son:

1. **Conexión y Petición Básica:** consulta sobre el concepto de Inferencia en Inteligencia Artificial.
2. **Procesador de Textos Inteligente:** resumen ejecutivo y profesionalización de textos mediante una función.
3. **Chat de Soporte con Historial (Few-Shot):** simulación de un vendedor de una tienda de tecnología utilizando un historial de ejemplos y manteniendo el contexto de la conversación.

---

## Requisitos

Antes de ejecutar el proyecto se necesita tener instalado:

* Python 3.10 o superior.
* Una API Key de Gemini.
* La librería `google-genai`.
* La librería `python-dotenv`.

---

## Instalación

### 1. Clonar el repositorio

Desde una terminal:

```bash
git clone URL_DEL_REPOSITORIO
```

Luego ingresar a la carpeta del proyecto:

```bash
cd NOMBRE_DEL_REPOSITORIO
```

### 2. Crear un entorno virtual

Se recomienda utilizar un entorno virtual para instalar las dependencias del proyecto:

```bash
python -m venv env
```

Activar el entorno virtual en Windows:

```powershell
.\env\Scripts\activate
```

### 3. Instalar las dependencias

Instalar `google-genai`:

```bash
pip install google-genai
```

Instalar `python-dotenv`:

```bash
pip install python-dotenv
```

---

## Configuración de la API Key

Para utilizar Gemini es necesario configurar una API Key.

Crear un archivo llamado:

```text
.env
```

En la raíz del proyecto y agregar:

```text
GENAI_API_KEY=TU_API_KEY_AQUI
```

El código obtiene la API Key mediante:

```python
API_KEY = os.getenv("GENAI_API_KEY")
```

### Seguridad

El archivo `.env` contiene información privada y **no debe subirse al repositorio de GitHub**.

Por esta razón, el proyecto debe incluir un archivo `.gitignore` con:

```text
.env
env/
__pycache__/
*.pyc
```

También se puede incluir un archivo `.env.example` como referencia:

```text
GENAI_API_KEY=TU_API_KEY_AQUI
```

---

# Ejercicio 1: Conexión y Petición Básica

## Descripción

El primer ejercicio inicializa el cliente de Gemini y realiza una petición utilizando `client.models.generate_content()`.

El modelo recibe una instrucción para explicar qué es la **Inferencia en Inteligencia Artificial** en menos de 50 palabras.

Además, el programa permite realizar consultas desde la consola hasta que el usuario escriba `salir`.

## Archivo

```text
ejercicio_1.py
```

## Ejecución

Ejecutar:

```powershell
py ejercicio_1.py
```

El programa mostrará:

```text
--- Ejercicio 1: Conexión y Petición Básica ---
(Escribe 'salir' para terminar)

Estudiante:
```

Se puede ingresar:

```text
¿Qué es la Inferencia en IA?
```

El modelo generará una explicación breve sobre el concepto.

Para terminar:

```text
salir
```

---

# Ejercicio 2: Procesador de Textos Inteligente

## Descripción

El segundo ejercicio implementa la función:

```python
procesar_articulo(texto, tarea)
```

Esta función recibe:

* `texto`: contenido que se desea procesar.
* `tarea`: operación que se desea realizar.

Las tareas disponibles son:

### Resumir

Si la tarea es:

```text
resumir
```

el modelo genera un **resumen ejecutivo** identificando las ideas principales del texto.

### Profesionalizar

Si la tarea es:

```text
profesionalizar
```

el modelo modifica la redacción para utilizar un tono **formal, técnico y profesional**, conservando las ideas originales.

## System Instruction

Para este ejercicio se utiliza una instrucción de sistema que define al modelo como:

```text
Editor Editorial de prestigio
```

Esta instrucción indica que debe procesar los textos de manera clara, formal, técnica y profesional.

## Archivo

```text
ejercicio_2.py
```

## Ejecución

Ejecutar:

```powershell
py ejercicio_2.py
```

El programa solicitará:

```text
--- Procesador de Textos Inteligente ---
(Escribe 'salir' para terminar)

Texto:
```

Ingresar el texto que se desea procesar.

Después seleccionar una de las tareas:

```text
Tarea (resumir/profesionalizar):
```

Ejemplo:

```text
Tarea (resumir/profesionalizar): resumir
```

Para profesionalizar un texto:

```text
Tarea (resumir/profesionalizar): profesionalizar
```

Para finalizar:

```text
salir
```

---

# Ejercicio 3: Chat de Soporte con Historial (Few-Shot)

## Descripción

El tercer ejercicio implementa un sistema de chat para una **tienda de tecnología**.

El modelo recibe una `system_instruction` que define su rol como:

```text
vendedor amable y profesional de una tienda de tecnología
```

El vendedor debe responder de forma clara y cordial y proporcionar especificaciones de los productos cuando sean solicitadas.

## Historial Few-Shot

El programa inicia con un historial que contiene dos ejemplos de interacción entre usuario y modelo.

### Ejemplo 1

```text
Usuario:
¿Qué especificaciones tiene el portátil TechBook Pro?

Modelo:
El TechBook Pro cuenta con procesador Intel Core i7,
16 GB de RAM, almacenamiento SSD de 512 GB y pantalla
de 15,6 pulgadas.
```

### Ejemplo 2

```text
Usuario:
¿Qué características tiene el teléfono SmartPhone X?

Modelo:
El SmartPhone X cuenta con pantalla AMOLED de 6,5 pulgadas,
8 GB de RAM, 128 GB de almacenamiento y cámara principal
de 50 MP.
```

Estos ejemplos permiten utilizar la técnica **Few-Shot**, proporcionando al modelo ejemplos del tipo de interacción y respuesta esperada.

## Mantener el historial

Además de los ejemplos iniciales, cada pregunta realizada por el usuario y cada respuesta generada por Gemini se agregan a:

```python
conversation_history
```

De esta forma, el modelo puede recibir el historial de la conversación y mantener el contexto durante la ejecución.

## Archivo

```text
ejercicio_3.py
```

## Ejecución

Ejecutar:

```powershell
py ejercicio_3.py
```

El programa mostrará:

```text
--- Chat de Soporte - Tienda de Tecnología ---
(Escribe 'salir' para terminar)

Cliente:
```

Se pueden realizar preguntas relacionadas con productos tecnológicos.

Por ejemplo:

```text
Cliente: ¿Qué computador me recomiendas para programación?
```

Después se puede continuar la conversación:

```text
Cliente: ¿Qué características debería tener?
```

El programa mantiene las interacciones anteriores en el historial.

Para finalizar el chat se debe escribir:

```text
finalizar
```

---

# Estructura del proyecto

La estructura recomendada del repositorio es:

```text
Taller-Google-GenAI/
│
├── ejercicio_1.py
├── ejercicio_2.py
├── ejercicio_3.py
├── README.md
├── .env.example
├── .gitignore
└── evidencias/
    ├── ejercicio_1.png
    ├── ejercicio_2_resumir.png
    ├── ejercicio_2_profesionalizar.png
    └── ejercicio_3.png
```

El archivo `.env` debe permanecer únicamente de forma local y no debe subirse a GitHub.

---

# Tecnologías utilizadas

* **Python**
* **Google GenAI (`google-genai`)**
* **Gemini**
* **python-dotenv**

---

# Evidencias

En la carpeta `evidencias/` se incluyen capturas de pantalla que muestran la ejecución y los resultados obtenidos en cada ejercicio.

Las evidencias incluyen:

* Ejecución del Ejercicio 1 y respuesta sobre Inferencia en IA.
* Ejecución del Ejercicio 2 utilizando la tarea `resumir`.
* Ejecución del Ejercicio 2 utilizando la tarea `profesionalizar`.
* Ejecución del Ejercicio 3 mostrando la conversación con el vendedor y el mantenimiento del historial.

---

# Conclusión

El proyecto demuestra el uso de la librería `google-genai` para:

* Inicializar y utilizar un cliente de Gemini.
* Realizar peticiones mediante `generate_content`.
* Utilizar `system_instruction` para definir el comportamiento del modelo.
* Procesar textos mediante diferentes instrucciones.
* Implementar las tareas de resumen y profesionalización.
* Crear conversaciones interactivas.
* Mantener un historial de conversación.
* Utilizar ejemplos Few-Shot con los roles `user` y `model`.

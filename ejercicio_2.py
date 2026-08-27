import os
from dotenv import load_dotenv
from google import genai
from google.genai import types


load_dotenv()  # Load environment variables from .env file

API_KEY = os.getenv("GENAI_API_KEY")

# Inicializar el cliente
client = genai.Client(api_key=API_KEY)

configuration = types.GenerateContentConfig(
    max_output_tokens=2048,
    temperature=0,
    system_instruction="""Eres un Editor Editorial de prestigio.
Tu función es procesar textos de manera clara, formal, técnica y profesional.
Debes mantener las ideas principales del texto original y no inventar información."""
)

MODEL = "gemini-3.5-flash-lite"

# Función para procesar artículos
def procesar_articulo(texto, tarea):

    if tarea.lower() == "resumir":
        instruccion = """Realiza un resumen ejecutivo del siguiente texto.
Identifica y presenta las ideas principales de forma clara, concisa y profesional."""

    elif tarea.lower() == "profesionalizar":
        instruccion = """Edita el siguiente texto para que tenga un tono formal,
técnico y profesional. Conserva las ideas originales y mejora la redacción."""

    else:
        return "Error: la tarea debe ser 'resumir' o 'profesionalizar'."

    # Envío del texto a Gemini
    response = client.models.generate_content(
        model=MODEL,
        config=configuration,
        contents=f"""
        {instruccion}

        Texto:
        {texto}
        """
    )

    return response.text

print("--- Procesador de Textos Inteligente ---")
print("(Escribe 'salir' para terminar)\n")

while True:

        user_input = input("Texto: ")
        
        if user_input.lower() in ["salir", "exit", "quit"]:
            print("Procesador: ¡Hasta pronto!")
            break
        
        tarea = input("Tarea (resumir/profesionalizar): ")

        try:
           resultado = procesar_articulo(user_input, tarea)
           
           print(f"\nResultado:\n{resultado}\n")

        except Exception as e:
            # Es recomendable implementar reintentos con backoff exponencial en producción
            print(f"Error al procesar la solicitud: {e}")
               

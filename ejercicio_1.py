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
    system_instruction="""Eres un asistente de estudio especializado en Inteligencia Artificial.
Explica qué es la Inferencia en Inteligencia Artificial en menos de 50 palabras.
Tu respuesta debe ser concisa y educativa, teniendo presente que el usuario es un estudiante de Ingeniería de Sistemas."""
)

print("--- Ejercicio 1: Conexión y Petición Básica ---")
print("(Escribe 'salir' para terminar)\n")

while True:
        user_input = input("Estudiante: ")
        
        if user_input.lower() in ["salir", "exit", "quit"]:
            print("Asistente: ¡Hasta pronto! Sigue practicando.")
            break

        try:
            # Realizar la petición            
            response = client.models.generate_content(
            model="gemini-3.5-flash-lite",
            contents=user_input,
            config=configuration
        )
            
            # En el nuevo SDK, el acceso al texto es response.text
            print(f"\nAsistente: {response.text}\n")

        except Exception as e:
            # Es recomendable implementar reintentos con backoff exponencial en producción
            print(f"Error al procesar la solicitud: {e}")

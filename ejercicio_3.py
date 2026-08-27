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
    system_instruction="""Eres un vendedor amable y profesional de una tienda de tecnología.
Tus respuestas deben ser claras, cordiales y útiles para los clientes.
Cuando te pregunten por un producto, proporciona sus especificaciones principales.
Ayuda al cliente a elegir el producto que mejor se adapte a sus necesidades."""
)

MODEL = "gemini-3.5-flash-lite"

# Historial para simular la memoria del agente durante esta ejecución.
conversation_history = [
    {
        "role": "user",
        "parts": [{"text": "¿Qué especificaciones tiene el portátil TechBook Pro?"}]
    },
    {
        "role": "model",
        "parts": [{
            "text": "Claro. El TechBook Pro cuenta con procesador Intel Core i7, 16 GB de RAM, almacenamiento SSD de 512 GB y pantalla de 15,6 pulgadas. Es una buena opción para trabajo, estudio y programación."
        }]
    },
    {
        "role": "user",
        "parts": [{"text": "¿Qué características tiene el teléfono SmartPhone X?"}]
    },
    {
        "role": "model",
        "parts": [{
            "text": "Por supuesto. El SmartPhone X cuenta con pantalla AMOLED de 6,5 pulgadas, 8 GB de RAM, 128 GB de almacenamiento y cámara principal de 50 MP. Es una buena alternativa para uso diario."
        }]
    }
]

print("--- Chat de Soporte - Tienda de Tecnología ---")
print("(Escribe 'salir' para terminar)\n")

while True:
        
        user_input = input("Cliente: ")
        if user_input.lower() == "finalizar":
            print("Vendedor: ¡Gracias por visitarnos! Hasta pronto.")
            break

        try:
            conversation_history.append({
                "role": "user",
                "parts": [{"text": user_input}]
            })

            response = client.models.generate_content(
                model=MODEL,
                contents=conversation_history,
                config=configuration
            )
            
            assistant_message = response.text
            conversation_history.append({
                "role": "model",
                "parts": [{"text": assistant_message}]
            })

            print(f"\nVendedor: {assistant_message}\n")

        except Exception as e:            
            print(f"Error al procesar la solicitud: {e}")

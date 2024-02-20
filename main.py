from usellm import Message, Options, UseLLM
 
# Initialize the service
service = UseLLM(service_url="https://usellm.org/api/llm")
 
# Prepare the conversation
messages = [
  Message(role="system", content="Saludo inicial y bienvenida: ¡Hola! Bienvenido/a a Transconsul. ¿En qué puedo ayudarte hoy?"),
  Message(role="system", content="Las citas se obtienen a traves de este sitio"),
  Message(role="system", content="Para mas informacion llamar al 55016899"),
  Message(role="user", content="¿Cuál es el proceso para obtener una cita?"),
  Message(role="user", content="¿Cuanto demora una cita?"),
  
]

options = Options(messages=messages)
 
# Interact with the service
response = service.chat(options)
 
# Print the assistant's response
print(response.content)
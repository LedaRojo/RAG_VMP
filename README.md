# RAG_VMP
MVP de RAG para Gestión de riesgos informáticos
🤖 Sistema RAG - Asistente Inteligente de Documentos

Este proyecto implementa un sistema RAG (Retrieval-Augmented Generation) que permite interactuar con documentos de manera conversacional. El asistente responde preguntas en lenguaje natural basándose únicamente en el contenido de los documentos cargados, garantizando respuestas relevantes, concisas y específicas.

🚀 Características principales

Carga de documentos en múltiples formatos:

📄 PDF

📝 Word (.docx, .doc)

📋 Texto plano (.txt)

Procesamiento inteligente:

Segmentación de textos en chunks con solapamiento para preservar contexto.

Creación de embeddings con OpenAI Embeddings (text-embedding-ada-002).

Almacenamiento vectorial con ChromaDB para búsquedas semánticas.

Motor de consulta:

Recupera los pasajes más relevantes del vector store.

Genera respuestas con GPT-4o-mini (ajustable a otros modelos OpenAI).

Mantiene un historial de conversación estilo chat.

Interfaz amigable en Gradio:

Subida de archivos y configuración inicial.

Chat interactivo para hacer preguntas y obtener respuestas inmediatas.

Botones para limpiar conversación y reiniciar el sistema.

⚙️ Flujo de trabajo

Carga tus documentos desde la interfaz.

Inicializa el sistema RAG → se procesan los documentos, se generan embeddings y se crea el índice vectorial.

Haz preguntas en lenguaje natural.

El asistente responde basándose en los fragmentos de texto más relevantes de los documentos cargados.

🛠️ Tecnologías utilizadas

LangChain
 – orquestación de RAG.

ChromaDB
 – almacenamiento vectorial.

OpenAI API
 – embeddings y generación de respuestas.

Gradio
 – interfaz gráfica web.

tiktoken
 – tokenización eficiente.

▶️ Ejecución

Clonar el repositorio.

Configurar tu clave de OpenAI en un archivo .env:

OPENAI_API_KEY=tu_api_key_aqui


Instalar dependencias:

pip install -r requirements.txt


Ejecutar la aplicación:

python app.py


Abrir en tu navegador: http://localhost:7860

💡 Ejemplos de uso

"¿Cuál es el resumen del documento?"

"¿Qué se menciona sobre el área de finanzas?"

"Enumera los puntos principales de la propuesta."

👉 Este proyecto es ideal para empresas, estudiantes o investigadores que necesitan extraer conocimiento rápidamente de grandes volúmenes de documentos de forma simple e intuitiva.

¿Quieres que te lo arme ya en formato Markdown completo con emojis y secciones listas para pegar en tu README.md?

# RAG_VMP
<strong>Proyecto RAG para Gestión de riesgos informáticos.</strong>

<strong>Resumen Ejecutivo</strong>
En el marco de nuestra iniciativa de transformación digital, proponemos el desarrollo de un asistente virtual inteligente especializado en seguridad de la información (BISO Virtual), basado en la tecnología OpenAI Este asistente estará diseñado para brindar soporte a los equipos de seguridad de la información, facilitando la gestión de políticas, regulaciones y riesgos de ciberseguridad.
El BISO Virtual permitirá:
●	Automatizar tareas clave: Responderá de manera automática a consultas frecuentes, generará reportes de cumplimiento y hará seguimiento continuo de incidentes de seguridad.
●	Mejorar la eficiencia operativa: Proporcionará acceso inmediato y actualizado a normativas, mejores prácticas y tendencias de seguridad, optimizando el tiempo de los equipos.
●	Capacitar al personal: Ofrecerá formación continua y acceso instantáneo a conocimientos especializados para fortalecer las capacidades del equipo de seguridad.

<strong>El presente modelo es el Producto Mínimo Viable usado de este proyecto para probar el funcionamiento de los modelos de OPenAI para el Chat conversacional, los modelos de embbeddings,  el tokenizador y el de la base de datos vectorial, permitiendo inicialmente la carga en tiempo real de los docuementos. El siguiente paso del rpoyecto (que no está consignado aquí) fue mantener todos los documentos en una memoria persistente en producción, a la cuál sólo se cargarán documentos nuevos.</strong>

🤖 Sistema RAG - Asistente Inteligente de Documentos

Este proyecto implementa un sistema RAG (Retrieval-Augmented Generation) que permite interactuar con documentos de manera conversacional. El asistente responde preguntas en lenguaje natural basándose únicamente en el contenido de los documentos cargados, garantizando respuestas relevantes, concisas y específicas.

🚀 <strong>Características principales</strong>

Carga de documentos en múltiples formatos:

📄 PDF

📝 Word (.docx, .doc)

📋 Texto plano (.txt)

Procesamiento inteligente:

Segmentación de textos en chunks con solapamiento para preservar contexto.

Creación de embeddings con OpenAI Embeddings (text-embedding-ada-002).

Almacenamiento vectorial (No persistente) con ChromaDB para búsquedas semánticas.

Motor de consulta:

Recupera los pasajes más relevantes del vector store.

Genera respuestas con GPT-4o-mini (ajustable a otros modelos OpenAI).

Mantiene un historial de conversación estilo chat.

Interfaz amigable en Gradio:

Subida de archivos y configuración inicial.

Chat interactivo para hacer preguntas y obtener respuestas inmediatas.

Botones para limpiar conversación y reiniciar el sistema.

⚙️ <strong>Flujo de trabajo</strong>

Carga tus documentos desde la interfaz.

Inicializa el sistema RAG → se procesan los documentos, se generan embeddings y se crea el índice vectorial.

Haz preguntas en lenguaje natural.

El asistente responde basándose en los fragmentos de texto más relevantes de los documentos cargados.

🛠️ <strong>Tecnologías utilizadas</strong>

<strong>LangChain</strong>
 – orquestación de RAG.

<strong>ChromaDB</strong>
 – almacenamiento vectorial.

<strong>OpenAI API</strong>
 – embeddings y generación de respuestas.

<strong>Gradio</strong>
 – interfaz gráfica web.

<strong>tiktoken</strong>
 – tokenización eficiente.

▶️ <strong>Ejecución</strong>

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


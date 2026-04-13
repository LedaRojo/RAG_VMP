###Rag para ciberseguridad
import os
import gradio as gr
from langchain_chroma import Chroma
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnablePassthrough
from langchain.embeddings import OpenAIEmbeddings
from langchain_openai import ChatOpenAI
from langchain_community.document_loaders import UnstructuredFileLoader
from langchain_core.prompts import ChatPromptTemplate
from langchain_text_splitters import CharacterTextSplitter
import tiktoken
from dotenv import load_dotenv
import tempfile


##cargo variables de entorno desde un archivo .env

# Configuración
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
if not OPENAI_API_KEY:
    raise ValueError("OPENAI_API_KEY no encontrada en variables de entorno")

# Inicializar componentes (se cargarán después de subir archivos)
vectorstore = None
retriever = None
chain = None
xxx = None


def initialize_rag_system(files):
    """Inicializa el sistema RAG con los archivos subidos"""
    global vectorstore, retriever, chain
    
    try:
        # Cargar documentos
        docs_list = []
        for file_info in files:
            file_path = file_info.name
            loader = UnstructuredFileLoader(file_path)
            documents = loader.load()
            docs_list.extend(documents)
        
        # Split de documentos
        encoding = tiktoken.encoding_for_model("gpt-3.5-turbo")
        text_splitter = CharacterTextSplitter.from_tiktoken_encoder(
            chunk_size=1000,
            chunk_overlap=200
        )
        doc_splits = text_splitter.split_documents(docs_list)
        
        # Crear embeddings y vector store
        embedding_model = OpenAIEmbeddings(
            model="text-embedding-ada-002", 
            api_key=OPENAI_API_KEY
        )
        
        vectorstore = Chroma.from_documents(
            documents=doc_splits,
            collection_name="rag-chroma",
            embedding=embedding_model
        )
        
        retriever = vectorstore.as_retriever(
            search_type="similarity",
            search_kwargs={"k": 3}
        )
        
        # Template del prompt
        template = """Eres un asistente útil que responde preguntas basándose ÚNICAMENTE en el contexto proporcionado.

Contexto:
{context}

Pregunta: {question}

Instrucciones:
- Responde de manera clara y concisa
- Si la información no está en el contexto, di "No encontré información sobre esto en los documentos"
- Usa el mismo lenguaje que la pregunta
- Sé específico y evita información irrelevante

Respuesta:"""
        
        prompt = ChatPromptTemplate.from_template(template)
        
        # Configurar modelo
        model = ChatOpenAI(
            api_key=OPENAI_API_KEY,
            temperature=0,
            model="gpt-4o-mini"
        )
        
        # Crear chain
        chain = (
            {"context": retriever, "question": RunnablePassthrough()}
            | prompt
            | model
            | StrOutputParser()
        )
        
        return f"✅ Sistema RAG inicializado exitosamente con {len(docs_list)} documentos y {len(doc_splits)} chunks."
    
    except Exception as e:
        return f"❌ Error inicializando el sistema: {str(e)}"

def ask_question(question, history):
    """Función para hacer preguntas al sistema RAG"""
    if chain is None:
        return "⚠️ Primero debes subir archivos e inicializar el sistema.", history
    
    if not question.strip():
        return "❌ Por favor ingresa una pregunta.", history
    
    try:
        # Obtener respuesta
        respuesta = chain.invoke(question)
        
        # Actualizar historial
        history.append((question, respuesta))
        
        return "", history
    
    except Exception as e:
        error_msg = f"❌ Error procesando la pregunta: {str(e)}"
        history.append((question, error_msg))
        return "", history

def clear_chat():
    """Limpiar el historial del chat"""
    return []

# Interfaz de Gradio
with gr.Blocks(theme=gr.themes.Soft(), title="Sistema RAG - Asistente de Documentos") as demo:
    gr.Markdown(
        """
        # 🤖 Sistema RAG - Asistente Inteligente de Información Empresarial
        **Carga tus documentos y haz preguntas sobre su contenido**
        """
    )
    
    with gr.Row():
        with gr.Column(scale=1):
            gr.Markdown("### 📁 Configuración")
            file_input = gr.File(
                label="Sube tus documentos",
                file_types=[".txt", ".pdf", ".docx", ".doc"],
                file_count="multiple",
                type="filepath"
            )
            init_button = gr.Button("🚀 Inicializar Sistema RAG", variant="primary")
            init_status = gr.Textbox(label="Estado del Sistema", interactive=False)
        
        with gr.Column(scale=2):
            gr.Markdown("### 💬 Consulta la información que necesitas")
            chatbot = gr.Chatbot(
                label="Conversación",
                height=500,
                show_copy_button=True
            )
            question_input = gr.Textbox(
                label="Escribe tu pregunta",
                placeholder="¿Qué información buscas en los documentos?",
                lines=2
            )
            
            with gr.Row():
                submit_btn = gr.Button("📤 Enviar Pregunta", variant="primary")
                clear_btn = gr.Button("🗑️ Limpiar Chat", variant="secondary")
    
    # Event handlers
    init_button.click(
        fn=initialize_rag_system,
        inputs=[file_input],
        outputs=[init_status]
    )
    
    submit_btn.click(
        fn=ask_question,
        inputs=[question_input, chatbot],
        outputs=[question_input, chatbot]
    ).then(
        lambda: "",  # Clear input
        outputs=[question_input]
    )
    
    question_input.submit(
        fn=ask_question,
        inputs=[question_input, chatbot],
        outputs=[question_input, chatbot]
    ).then(
        lambda: "",  # Clear input
        outputs=[question_input]
    )
    
    clear_btn.click(
        fn=clear_chat,
        outputs=[chatbot]
    )
    
    gr.Markdown(
        """
        ---
        ### 📝 Formatos soportados:
        - 📄 PDF
        - 📝 Word (.docx, .doc)
        - 📋 Texto (.txt)
        
        ### 💡 Ejemplos de preguntas:
        - "¿Cuál es el resumen del documento?"
        - "¿Qué se menciona sobre [tema específico]?"
        - "Lista los puntos principales"
        """
    )

if __name__ == "__main__":
    demo.launch(
        server_name="0.0.0.0",
        server_port=7860,
        share=False
    )
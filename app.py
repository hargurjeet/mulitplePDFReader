import streamlit as st 
from PyPDF2 import PdfReader
from langchain.text_splitter import RecursiveCharacterTextSplitter
import os
from langchain_google_genai import GoogleGenerativeAIEmbeddings
import google.generativeai as genai
from langchain.vectorstores import FAISS
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.chains.question_answering import load_qa_chain
from langchain.prompts import PromptTemplate
from dotenv import load_dotenv



load_dotenv()
genai.configure(api_key=os.getenv('GOOGLE_API_KEY'))

def get_pdf_text(pdf_docs):
    text=""
    for pdf in pdf_docs:
        reader=PdfReader(pdf)
        for page in reader.pages:
            text+=page.extract_text()
            
    return text

def get_text_chunks(text):
    text_splitter=RecursiveCharacterTextSplitter(
        chunk_size=10000,
        chunk_overlap=1000,
        # length_function=len
    )
    chunks=text_splitter.split_text(text)
    return chunks

def get_embeddings(chunks):
    embeddings=GoogleGenerativeAIEmbeddings(model="models/embedding-001")
    docsearch=FAISS.from_texts(chunks,embedding=embeddings)
    docsearch.save_local("docsearch.pkl")
    return docsearch

def get_conversational_chain():
    prompt_template="""
    Answer the question as detailed as possible using the provided context. Make sure to provide all the details. If the answer is not \n
    provided for the context just say, "answer is not avalaible in the context", dont provide the wrong answer \n
    Context: {context} \n
    Question: {question} \n
    
    Answer:
    """
    
    model=ChatGoogleGenerativeAI(model="gemini-pro", temperature=0.7)
    prompt = PromptTemplate(template=prompt_template, input_variables=["context","question"])
    chain=load_qa_chain(model, chain_type="stuff", prompt=prompt)
    return chain

def user_input(user_question):
    embeddings = GoogleGenerativeAIEmbeddings(model="models/embedding-001")     
    new_db = FAISS.load_local("docsearch.pkl", embeddings=embeddings)
    docs=new_db.similarity_search(user_question, k=3)
    chain=get_conversational_chain()
    
    response=chain(
        {"input_documents":docs, "question": user_question},
         return_only_outputs=True 
         )
    print(response)
    st.write("Reply :", response["output_text"])
    
    
def main():
    st.set_page_config(page_title="Chat with Multiple PDFs", page_icon=":book:", layout="wide")
    st.header("Chat with Multiple PDFs using Gemini")
    
    user_question=st.text_input("Ask a question from the PDF files")
    
    if user_question:
        user_input(user_question)   
        
    with st.sidebar:
        st.title("Menu")
        st.info("This is a demo app to chat with multiple PDF files using Gemini")
        st.info("Built with Streamlit")
        st.info("By : Hargurjeet")
        
        pdf_docs=st.file_uploader("Upload PDF files", type="pdf", accept_multiple_files=True)
        if st.button ("submit and process"):
            with st.spinner("Processing..."):
                text=get_pdf_text(pdf_docs)
                chunks=get_text_chunks(text)
                get_embeddings(chunks)
                st.success("Processing Completed")
                
if __name__=="__main__":
    main()

    
import os
import sys
from langchain_ollama import OllamaLLM
from langchain_community.document_loaders import WebBaseLoader
from langchain.chains.summarize import load_summarize_chain
from langchain.prompts import PromptTemplate

def set_model():
    def _get_prompt():
        PROMPT = PromptTemplate(
            input_variables=["text"],
            template="以下のWEBページの本文部分を日本語で要約してください:\n\n{text}\n\n要約:"
        )
        return PROMPT
    PROMPT = _get_prompt()
    MODEL = "llama3.2"
    # 環境変数からOLLAMA_HOSTを取得（未設定の場合はlocalhostを使用）
    ollama_host = os.getenv("OLLAMA_HOST", "localhost")
    # LLMモデルの設定
    llm = OllamaLLM(model=MODEL, base_url=f"http://{ollama_host}:11434")
    chain = load_summarize_chain(llm, chain_type="stuff", prompt=PROMPT)
    return chain

def summarize_text(docs):
    chain = set_model()
    result = chain.invoke(docs)
    return result['output_text']

def main(args):
    url = args[1]    
    # Webページの内容をロード
    loader = WebBaseLoader(url)
    docs = loader.load()
    # 要約の実行
    result = summarize_text(docs)
    print(result)

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python script.py <URL>")
        sys.exit(1)
    args = sys.argv
    main(args)
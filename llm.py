import os


from langchain.llms import OpenAI, AzureOpenAI

from langchain.chat_models import ChatOpenAI, AzureChatOpenAI

from langchain.embeddings import OpenAIEmbeddings

from dotenv import load_dotenv

load_dotenv()

# Configure Azure OpenAI Service API

## load the API key from the environment variable
openai_api_key = os.getenv("OPENAI_API_KEY")


llm = OpenAI(openai_api_key=openai_api_key)
chat_llm = ChatOpenAI(openai_api_key=openai_api_key, temperature=0.4)
embeddings = OpenAIEmbeddings(openai_api_key=openai_api_key)




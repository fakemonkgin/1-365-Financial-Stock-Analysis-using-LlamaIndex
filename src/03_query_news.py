import os
import openai
from dotenv import load_dotenv
from llama_index.core import StorageContext, load_index_from_storage

load_dotenv()

openai.api_key = os.getenv("OPEN_API_KEY")

storage_context = StorageContext.from_defaults(persist_dir="./storage")
index = load_index_from_storage(storage_context)

# as_query_engine()直译就是把索引转成查询引擎，封装检索逻辑（从向量索引找相关文档），和 LLM 结合生成自然语言答案
query_engine = index.as_query_engine()

response = query_engine.query("Tell me about some trading info related to microsoft")
print(response)
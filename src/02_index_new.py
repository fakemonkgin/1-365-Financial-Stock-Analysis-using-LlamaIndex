import os
import openai
from dotenv import load_dotenv
from llama_index.core import VectorStoreIndex, SimpleDirectoryReader

load_dotenv()
openai.api_key = os.getenv("OPEN_API_KEY")

documents = SimpleDirectoryReader("articles").load_data()

# 这一步把文档生成了向量索引，但 存在内存里（runtime memory）
index = VectorStoreIndex.from_documents(documents)

# 把内存里的索引保存到磁盘（默认在 ./storage 目录或你设置的目录）
# index.storage_context 是 索引的存储上下文（Storage Context）,可以理解为：索引的“磁盘/数据库接口”，知道索引存在哪、怎么序列化、怎么加载
# persist() 直译是 “持久化”,意思就是 把内存里的索引状态写入到磁盘或持久存储
index.storage_context.persist()
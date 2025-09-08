# 1-365-Financial-Stock-Analysis-using-LlamaIndex

```bash
streamlit run app.py
```

### 在app.py里
'''
老版本：
from llama_index import LLMPredictor, ServiceContext
from langchain.llms import OpenAI

llm_predictor = LLMPredictor(llm=OpenAI())
service_context = ServiceContext.from_defaults(llm_predictor=llm_predictor)

新版本：
from llama_index.core import Settings
from llama_index.llms.openai import OpenAI

# 直接使用LLM对象,不需要LLMPredictor包装
Settings.llm = OpenAI(model="gpt-3.5-turbo")
'''

symbols of stock = ["MSFT","NVDA","GOOG","META","AAPL","TSM"]
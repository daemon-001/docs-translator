import os 
from openai import OpenAI
open_api_key="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"
os.environ["OPENAI_API_KEY"]=open_api_key

## Basic Prompt Summarization
from langchain.chat_models import ChatOpenAI
from langchain.schema import(
    AIMessage,
    HumanMessage,
    SystemMessage
)

speech="""
People across the country, involved in government, political, and social activities, are dedicating their time to make the ‘Viksit Bharat Sankalp Yatra’ (Developed India Resolution Journey) successful. Therefore, as a Member of Parliament, it was my responsibility to also contribute my time to this program. So, today, I have come here just as a Member of Parliament and your ‘sevak’, ready to participate in this program, much like you.
In our country, governments have come and gone, numerous schemes have been formulated, discussions have taken place, and big promises have been made. However, my experience and observations led me to believe that the most critical aspect that requires attention is ensuring that the government’s plans reach the intended beneficiaries without any hassles. If there is a ‘Pradhan Mantri Awas Yojana’ (Prime Minister’s housing scheme), then those who are living in jhuggis and slums should get their houses. And he should not need to make rounds of the government offices for this purpose. The government should reach him. Since you have assigned this responsibility to me, about four crore families have got their ‘pucca’ houses. However, I have encountered cases where someone is left out of the government benefits. Therefore, I have decided to tour the country again, to listen to people’s experiences with government schemes, to understand whether they received the intended benefits, and to ensure that the programs are reaching everyone as planned without paying any bribes. We will get the real picture if we visit them again. Therefore, this ‘Viksit Bharat Sankalp Yatra’ is, in a way, my own examination. I want to hear from you and the people across the country whether what I envisioned and the work I have been doing aligns with reality and whether it has reached those for whom it was meant.
It is crucial to check whether the work that was supposed to happen has indeed taken place. I recently met some individuals who utilized the Ayushman card to get treatment for serious illnesses. One person met with a severe accident, and after using the card, he could afford the necessary operation, and now he is recovering well. When I asked him, he said: “How could I afford this treatment? Now that there is the Ayushman card, I mustered courage and underwent an operation. Now I am perfectly fine.”  Such stories are blessings to me.
The bureaucrats, who prepare good schemes, expedite the paperwork and even allocate funds, also feel satisfied that 50 or 100 people who were supposed to get the funds have got it. The funds meant for a thousand villages have been released. But their job satisfaction peaks when they hear that their work has directly impacted someone’s life positively. When they see the tangible results of their efforts, their enthusiasm multiplies. They feel satisfied. Therefore, ‘Viksit Bharat Sankalp Yatra’ has had a positive impact on government officers. It has made them more enthusiastic about their work, especially when they witness the tangible benefits reaching the people. Officers now feel satisfied with their work, saying, “I made a good plan, I created a file, and the intended beneficiaries received the benefits.” When they find that the money has reached a poor widow under the Jeevan Jyoti scheme and it was a great help to her during her crisis, they realise that they have done a good job. When a government officer listens to such stories, he feels very satisfied.
There are very few who understand the power and impact of the ‘Viksit Bharat Sankalp Yatra’. When I hear people connected to bureaucratic circles talking about it, expressing their satisfaction, it resonates with me. I’ve heard stories where someone suddenly received 2 lakh rupees after the death of her husband, and a sister mentioned how the arrival of gas in her home transformed her lives. The most significant aspect is when someone says that the line between rich and poor has vanished. While the slogan ‘Garibi Hatao’ (Remove Poverty) is one thing, but the real change happens when a person says, “As soon as the gas stove came to my house, the distinction between poverty and affluence disappeared.
"""



# chat_messages=[
#     SystemMessage(content='You are an expert assistant with expertize in summarizing speeches'),
#     HumanMessage(content=f'Please provide a short and concise summary of the following speech:\n TEXT: {speech}')
# ]

# # llm=ChatOpenAI(model_name='gpt-3.5-turbo', base_url="https://openrouter.ai/api/v1")
# # llm=ChatOpenAI(model_name='gpt-4o-mini', base_url="https://openrouter.ai/api/v1")

llm = ChatOpenAI(
  base_url="https://openrouter.ai/api/v1",
  api_key=open_api_key,
  model="gpt-3.5-turbo",
)




##total tokens
# llm.get_num_tokens(speech)



# print(llm(chat_messages).content)


###################################################################################

from langchain.chains import LLMChain
from langchain import PromptTemplate

from PyPDF2 import PdfReader
from langchain.docstore.document import Document
from typing_extensions import Concatenate


# provide the path of  pdf file/files.
pdfreader = PdfReader('D:/Workspace/Project/doc-translator/new/demo.pdf')

# read text from pdf
text = ''

for i, page in enumerate(pdfreader.pages):
    content = page.extract_text()
    if content:
        text += content

print("\n",text,"\n")

# generic_template='''
# `{text}` Write a precise detailed summary of the following text in {language}
# '''
# prompt=PromptTemplate(
#     input_variables=['text','language'],
#     template=generic_template
# )

# prompt.format(speech=speech,language='Hindi')

# print(prompt.format(speech=speech,language='Hindi'))

# complete_prompt=prompt.format(speech=speech,language='Hindi')

# llm.get_num_tokens(complete_prompt)


# llm_chain=LLMChain(llm=llm,prompt=prompt)
# summary=llm_chain.run({'text':text,'language':'hindi'})

# print(summary)

#______________________________________________________________________________

# from PyPDF2 import PdfReader
# from langchain.docstore.document import Document
# from typing_extensions import Concatenate


# # provide the path of  pdf file/files.
# pdfreader = PdfReader('D:/Workspace/Project/doc-translator/new/chatbot.pdf')

# # read text from pdf
# text = ''

# for i, page in enumerate(pdfreader.pages):
#     content = page.extract_text()
#     if content:
#         text += content


# docs = [Document(page_content=text)]

# llm = ChatOpenAI(
#   base_url="https://openrouter.ai/api/v1",
#   api_key=open_api_key,
#   model="gpt-3.5-turbo",
# )


# from langchain import PromptTemplate
# from langchain.chat_models import ChatOpenAI
# from langchain.chains.summarize import load_summarize_chain
# from langchain.docstore.document import Document


# template = '''
# `{text}` , Write a precise detailed summary of the following text in {language}
# '''
# prompt = PromptTemplate(
#     input_variables=['text', 'language'],
#     template=template
# )



# chain = load_summarize_chain(
#     llm,
#     chain_type='stuff',
#     prompt=prompt,
#     verbose=False
# )
# output_summary = chain.run(docs, {'language':'urdu'})



# print(output_summary)

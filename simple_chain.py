import os
from API_key import openai_key
os.environ['OPENAI_API_KEY'] = openai_key
from langchain.chains import LLMChain
from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate


if __name__ == '__main__':

    template = """List some of the job titles that uses {job}"""

    prompt = PromptTemplate(template=template, input_variables=['job'])
    llm = OpenAI(openai_api_key=openai_key)
    prompt.format(job='Wireless Communications and AI')

    question = "List some of the job titles that uses {job}"
    llm_chain = LLMChain(prompt=prompt, llm=llm)
    print(llm_chain.run('AI and LLM'))

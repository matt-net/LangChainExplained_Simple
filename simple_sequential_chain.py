import os
from API_key import openai_key
from langchain.chains import SequentialChain

os.environ['OPENAI_API_KEY'] = openai_key
from langchain.chains import LLMChain
from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate

if __name__ == '__main__':
    llm = OpenAI(openai_api_key=openai_key)

    template_1 = """List just one job title that uses {tech} """
    prompt_1 = PromptTemplate(template=template_1, input_variables=['tech'])

    llm_chain_tech = LLMChain(prompt=prompt_1, llm=llm, output_key='job')

    template_2 = """List the salary for {job} in £ """
    prompt_2 = PromptTemplate(template=template_2, input_variables=['job'])
    llm_chain_job = LLMChain(prompt=prompt_2, llm=llm, output_key='salary')

    chain = SequentialChain(chains=[llm_chain_tech, llm_chain_job],
                            input_variables=["tech"],
                            output_variables=['job', "salary"]
                            )
    response = chain({"tech": "Wireless Communications and AI"})

    print(response)

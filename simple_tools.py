from langchain.agents import AgentType, initialize_agent, load_tools
from langchain.llms import OpenAI
import os
from API_key import openai_key, serpapi_key
from langchain.chains import SequentialChain

os.environ['OPENAI_API_KEY'] = openai_key
os.environ['SERPAPI_API_KEY'] = serpapi_key

if __name__ == '__main__':
    llm = OpenAI(openai_api_key=openai_key)
    # tools = load_tools(["wikipedia", "llm-math"], llm=llm)
    tools = load_tools(["serpapi", "llm-math"], llm=llm)

    agent = initialize_agent(
        tools,
        llm,
        agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
        verbose=True
    )
    response = agent.run("Who was Steve Jobs and what is his age plus 5")
    print(response)



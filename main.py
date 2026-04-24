from dotenv import load_dotenv
from langchain.agents import create_agent
from langchain_core.messages.human import HumanMessage


def main():

    load_dotenv()

    FINANCIAL_MODEL = "openrouter:google/gemma-4-31b-it"

    agent = create_agent(
        model=FINANCIAL_MODEL, system_prompt="You are an financial expert agent"
    )

    result = agent.invoke(
        {"messages": [HumanMessage(content="Can you help me buy an car? Give me tips")]}
    )

    print(result["messages"][-1].content)


if __name__ == "__main__":
    main()

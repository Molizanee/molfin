from dotenv import load_dotenv
from langchain.agents import create_agent
from langchain_core.messages.human import HumanMessage
from langfuse import get_client
from langfuse.langchain import CallbackHandler


def main():
    load_dotenv()

    langfuse = get_client()
    if langfuse.auth_check():
        print("Langfuse client is authenticated and ready!")
    else:
        print("Authentication failed. Please check your credentials and host.")

    langfuse_handler = CallbackHandler()

    FINANCIAL_MODEL = "openrouter:google/gemma-4-31b-it"

    agent = create_agent(
        model=FINANCIAL_MODEL, system_prompt="You are an financial expert agent"
    )

    result = agent.invoke(
        {
            "messages": [
                HumanMessage(content="Can you help me buy an car? Give me tips")
            ]
        },
        config={"callbacks": [langfuse_handler]},
    )

    print(result["messages"][-1].content)


if __name__ == "__main__":
    main()

import os
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate
from langchain.chains import LLMChain
from langchain.chains import SequentialChain

# Load environment variables
load_dotenv()

# Initialize LLM
llm = ChatGroq(
    model="llama3-70b-8192",
    temperature=0.7,
    groq_api_key=os.getenv("GROQ_API_KEY")
)

def generate_restaurant_name(cuisine):

    # Prompt 1: Restaurant name
    prompt1 = PromptTemplate(
        input_variables=["cuisine"],
        template = """
            Suggest ONLY ONE creative restaurant name for a {cuisine} restaurant.

            Return only the restaurant name.
            Do not explain anything.
            Do not give multiple options.
            Remove Bullet points if there are any.
            """
    )

    chain1 = LLMChain(
        llm=llm,
        prompt=prompt1,
        output_key="restaurant_name"
    )

    # Prompt 2: Menu items
    prompt2 = PromptTemplate(
        input_variables=["restaurant_name", "cuisine"],
        template = """
            Generate exactly 5 menu items for the restaurant {restaurant_name}.
            Cuisine: {cuisine}

            Return only the menu items as a simple list.
            Do not add explanations.
            Remove bullet points and numbers.
            """
    )

    chain2 = LLMChain(
        llm=llm,
        prompt=prompt2,
        output_key="menu_items"
    )

    # Sequential chain
    chain = SequentialChain(
        chains=[chain1, chain2],
        input_variables=["cuisine"],
        output_variables=["restaurant_name", "menu_items"]
    )

    response = chain({"cuisine": cuisine})

    return response
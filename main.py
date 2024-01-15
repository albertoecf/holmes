import click
from langchain.llms import Ollama
from langchain.prompts import ChatPromptTemplate
from langchain.chat_models import ChatOpenAI
from langchain.schema.output_parser import StrOutputParser


@click.command()
@click.option(
    "--person_name",
    prompt="Enter the name of the person",
    default="Albert Einstein",
    help="Name of the person",
)
def main(person_name):
    prompt_template = ChatPromptTemplate.from_template(
        "Provide a short description about {person}"
    )
    model = Ollama(base_url="http://localhost:11434", model="llama2")
    chain = prompt_template | model

    result = chain.invoke({"person": person_name})
    print(result)


if __name__ == "__main__":
    main()

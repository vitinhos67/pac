
from crewai import Task


def reviewer(Agent):

    write_task = Task(
    description = (
        "Correção do conteudo dizendo se e um conteudo valido, ou não"
    ),
    expected_output='Um pequeno texto explicativo formato txt, mostrando o conteudo gerado pelo agente e logo em seguida a correção, tudo em português e separado em topicos.',
    agent = Agent,
    output_file = './src/reviews/artigo.txt'
    
    )

    return write_task;

from crewai import Crew

from agents.reviewer import reviewer
from agents.teacher import Teacher


history = "Você é um ótimo escritor para descrever adequadamente qualquer assunto fornecido de forma clara e objetiva"
agent_teacher = Teacher(history=history) 
agent_revisor = reviewer(Agent=agent_teacher)

crew = Crew(agents=[agent_teacher], tasks=[agent_revisor], verbose = True)
result = crew.kickoff(inputs={'topic': 'Inteligência Artificial'})
#print(result)
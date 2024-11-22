import os
import json
import pandas as pd
import traceback

from dotenv import load_dotenv
from langchain_community.llms import OpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from langchain.chains import SequentialChain
from langchain_community.callbacks.manager import get_openai_callback
from langchain_openai import ChatOpenAI

from src.mcqgenerator.utils import readFile
from src.mcqgenerator.logger import logging

# Load environment variables
load_dotenv()

# Access the API key
OPENAI_KEY=os.getenv("OPENAI_API_KEY")
llm=ChatOpenAI(openai_api_key=OPENAI_KEY,model_name="gpt-3.5-turbo", temperature=0.5)

# Log the initialization
logging.info("MCQ Generation Application Started")

TEMPLATE="""
Text:{text}
You are an expert MCQ maker. Given the above text, it is your job to \
create a quiz  of {number} multiple choice questions for {subject} students in {language} language and in {tone} tone. 
Make sure the questions are not repeated and check all the questions to be conforming the text as well.
Make sure to format your response like  RESPONSE_JSON below  and use it as a guide. \
Ensure to make {number} MCQs
Ensure gramatical correctness of the questions and answers in the respective language.

### RESPONSE_JSON ###
{response_json}
"""

quiz_generation_prompt = PromptTemplate(
    input_variables=["text", "number", "subject", "language", "tone", "response_json"],
    template=TEMPLATE
    )

quiz_chain = LLMChain(llm=llm, prompt=quiz_generation_prompt, output_key="quiz", verbose=True)

TEMPLATE2="""
You are an expert english grammarian and writer. Given a Multiple Choice Quiz for {subject} students.\
You need to evaluate the complexity of the question and give a complete analysis of the quiz. Only use at max 50 words for complexity analysis. 
Translate both questions and answers into Polish.
Quiz_MCQs:
{quiz}

"""

quiz_evaluation_prompt=PromptTemplate(input_variables=["subject", "quiz"], template=TEMPLATE2)
review_chain = LLMChain(llm=llm, prompt=quiz_evaluation_prompt, output_key="review", verbose=True)
generate_evaluate_chain = SequentialChain(chains=[quiz_chain, review_chain], input_variables=["text", "number", "subject", "language", "tone", "response_json"], output_variables=["quiz", "review"], verbose=True)






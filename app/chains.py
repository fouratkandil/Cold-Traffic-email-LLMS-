import os
from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import JsonOutputParser
from langchain_core.exceptions import OutputParserException
from dotenv import load_dotenv

load_dotenv()

class Chain:
    def __init__(self):
        self.llm = ChatGroq(temperature=0, groq_api_key=os.getenv("GROQ_API_KEY"), model_name="llama-3.3-70b-versatile")

    def extract_jobs(self, cleaned_text):
        prompt_extract = PromptTemplate.from_template(
            """
            ### SCRAPED TEXT FROM WEBSITE:
            {page_data}
            ### INSTRUCTION:
            The scraped text is from the career's page of a website.
            Your job is to extract the job postings and return them in JSON format containing the following keys: `role`, `experience`, `skills` and `description`.
            Only return the valid JSON.
            ### VALID JSON (NO PREAMBLE):
            """
        )
        chain_extract = prompt_extract | self.llm
        res = chain_extract.invoke(input={"page_data": cleaned_text})
        try:
            json_parser = JsonOutputParser()
            res = json_parser.parse(res.content)
        except OutputParserException:
            raise OutputParserException("Context too big. Unable to parse jobs.")
        return res if isinstance(res, list) else [res]

    def write_mail(self, job, links):
        prompt_email = PromptTemplate.from_template(
            """
            ### JOB DESCRIPTION:
            {job_description}

            ### INSTRUCTION:
            You are Fourat, a Business Development Executive at Nexora — an AI and Software Consulting company specializing in
            developing intelligent, scalable, and data-driven solutions that empower businesses to innovate faster and operate smarter.
            Nexora helps companies streamline operations, automate workflows, and unlock new efficiencies through advanced software 
            engineering, AI integration, and process optimization.

            Based on the job description above, write a **personalized cold email** to the company that posted the job. 
            The goal of the email is to:
            - Demonstrate Nexora’s expertise and ability to provide solutions that align with the company’s hiring needs.
            - Position Nexora as a strategic technology partner (not a recruitment agency).
            - Highlight relevant projects or portfolio examples from the following links: {link_list}.
            - Maintain a professional yet approachable tone — concise, confident, and tailored to the specific job context.

            Avoid generic marketing talk. Focus on how Nexora can help the company achieve its objectives faster and more efficiently
            through its technology expertise.

            Do not include any preamble or explanation outside the email body.

            ### EMAIL (NO PREAMBLE):
            """
        )

        chain_email = prompt_email | self.llm
        res = chain_email.invoke({"job_description": str(job), "link_list": links})
        return res.content

if __name__ == "__main__":
    print(os.getenv("GROQ_API_KEY"))
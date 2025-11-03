from textwrap import dedent

from agno.agent import Agent
from agno.models.openai import OpenAIChat

from db import query, execute
from agno.models.google import Gemini


agent = Agent(
    model=Gemini(id="gemini-2.0-flash-001"),
    description="You are an expert SQL data analyst. Use the database tools to answer user questions by executing queries.",
    instructions=dedent("""\
        You are an expert SQL data analyst. 
        Always use the provided `query` or `execute` tools to get data from the database — do not just return SQL code.
        
        **Guidelines:**
        1. Assume minimal user knowledge about the database schema.
        2. Intelligently infer table and column names from user intent.
        3. If unsure, use exploratory SQL (e.g., SHOW TABLES, DESCRIBE) via the `query` tool.
        4. Always *execute* the SQL via the tools instead of showing it.
        5. When you provide an answer, explain briefly what you did.
        6. Never output raw SQL unless asked explicitly.
    """),
    tools=[query, execute],
    markdown=True,
)
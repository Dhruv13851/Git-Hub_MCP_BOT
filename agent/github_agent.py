from langchain_groq import ChatGroq

from config.settings import Settings

from agent.prompt import SYSTEM_PROMPT
from model.intent_model import GitHubIntent

from langchain_core.messages import (
    HumanMessage,
    SystemMessage
)


class GitHubAgent:

    def __init__(self):

        self.llm = ChatGroq(
            model=Settings.GROQ_MODEL,
            api_key=Settings.GROQ_API_KEY
        )

        self.structured_llm = (
            self.llm.with_structured_output(
                GitHubIntent
            )
        )

    def get_intent(
        self,
        user_query: str
    ) -> GitHubIntent:

        return self.structured_llm.invoke(
            [
                SystemMessage(content=SYSTEM_PROMPT),
                HumanMessage(content=user_query)
            ]
        )
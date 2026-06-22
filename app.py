import asyncio

from services.intent_service import IntentService
from services.execution_service import ExecutionService

from model.github_tools import GitHubTools
from model.client import MCPClient


async def main():

    query = input("Ask Something: ")

    intent_service = IntentService()

    intent = intent_service.extract_intent(query)

    print("\nIntent:")
    print(intent)

    client = MCPClient()

    print("\nConnecting to MCP...")
    await client.connect()

    github_tools = GitHubTools(
        client.session
    )

    execution_service = ExecutionService(
        github_tools
    )

    result = await execution_service.execute(
        intent
    )

    print("\nResult:")
    print(result)

    await client.disconnect()


if __name__ == "__main__":
    asyncio.run(main())
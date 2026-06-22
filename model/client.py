from mcp import ClientSession
from mcp.client.stdio import stdio_client, StdioServerParameters


class MCPClient:

    def __init__(self):
        self.session = None
        self.stdio_context = None

    async def connect(self):

        server_params = StdioServerParameters(
            command="python",
            args=["github_server.py"]
        )

        self.stdio_context = stdio_client(
            server_params
        )

        read, write = await self.stdio_context.__aenter__()

        self.session = ClientSession(
            read,
            write
        )

        await self.session.__aenter__()

        await self.session.initialize()

    async def disconnect(self):

        if self.session:
            await self.session.__aexit__(
                None,
                None,
                None
            )

        if self.stdio_context:
            await self.stdio_context.__aexit__(
                None,
                None,
                None
            )
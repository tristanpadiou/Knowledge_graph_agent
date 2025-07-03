from agent import MCP_Agent
import os
from dotenv import load_dotenv
load_dotenv()

api_keys={'openai_api_key':os.getenv('openai_api_key')}
mpc_server_stdio={'command': 'npx', 'args': ["-y", "@modelcontextprotocol/server-memory"]}



agent=MCP_Agent(api_keys=api_keys, mpc_stdio_commands=[mpc_server_stdio])

async def main():
    print(await agent.connect())
    while True:
        result = await agent.chat('what tools are available?')
        print(result)
        user_input = input('Enter a prompt: ')
        result = await agent.chat(user_input)
        print(result)

if __name__ == "__main__":
    import asyncio
    asyncio.run(main())
from agent import MCP_Agent
import os
from dotenv import load_dotenv
load_dotenv()

api_keys={'openai_api_key':os.getenv('openai_api_key')}
mpc_server_stdio={'command': 'npx', 'args': ["-y", "@modelcontextprotocol/server-memory"]}



class agent_cache:
    def __init__(self):
        self.agent=None

    async def get_agent(self):
        if self.agent is None:
            self.agent=MCP_Agent(api_keys=api_keys, mpc_stdio_commands=[mpc_server_stdio])
            await self.agent.connect()
        return self.agent
    
    async def reset(self):
        if self.agent is not None:
            await self.agent.reset()


knowledge_graph_agent=agent_cache()
knowledge_graph_agent.get_agent()








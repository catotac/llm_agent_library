"""
Base agent implementation
"""

from typing import Any, Dict, List, Optional
from pydantic import BaseModel
from ..tools import Tool
from ..memory import Memory

class Agent(BaseModel):
    """Base class for all agents"""
    
    name: str
    tools: List[Tool]
    memory: Optional[Memory] = None
    config: Optional[Dict[str, Any]] = None
    
    def __init__(self, **data):
        super().__init__(**data)
        self.state = {}
        
    async def run(self, input_data: Any) -> Any:
        """Run the agent with the given input"""
        # Process input using tools and memory
        result = await self._process(input_data)
        
        # Update memory if available
        if self.memory:
            await self.memory.update(self.state)
            
        return result
    
    async def _process(self, input_data: Any) -> Any:
        """Process the input data using available tools"""
        # Implementation would go here
        pass
    
    def add_tool(self, tool: Tool) -> None:
        """Add a tool to the agent"""
        self.tools.append(tool)
        
    def remove_tool(self, tool_name: str) -> None:
        """Remove a tool from the agent"""
        self.tools = [t for t in self.tools if t.name != tool_name]
        
    def get_state(self) -> Dict[str, Any]:
        """Get the current state of the agent"""
        return self.state.copy()
        
    def set_state(self, state: Dict[str, Any]) -> None:
        """Set the state of the agent"""
        self.state = state.copy() 
"""
Base graph implementation using LangGraph
"""

from typing import Any, Dict, List, Optional
from langgraph.graph import Graph
from ..agents import Agent

class AgentGraph:
    """Class for managing agent workflows using LangGraph"""
    
    def __init__(self, config: Optional[Dict[str, Any]] = None):
        self.config = config or {}
        self.graph = Graph()
        self.nodes = {}
        
    def add_node(self, agent: Agent) -> None:
        """Add an agent node to the graph"""
        self.nodes[agent.name] = agent
        self.graph.add_node(agent.name, agent.run)
        
    def add_edge(self, from_agent: str, to_agent: str, 
                 condition: Optional[Any] = None) -> None:
        """Add an edge between two agents"""
        self.graph.add_edge(from_agent, to_agent, condition)
        
    def compile(self) -> None:
        """Compile the graph"""
        self.graph = self.graph.compile()
        
    async def run(self, input_data: Any, start_node: str) -> Any:
        """Run the graph starting from the specified node"""
        if not self.graph.is_compiled:
            self.compile()
            
        result = await self.graph.arun(
            input_data,
            start_node=start_node
        )
        return result
    
    def get_node(self, name: str) -> Optional[Agent]:
        """Get an agent node by name"""
        return self.nodes.get(name)
        
    def remove_node(self, name: str) -> None:
        """Remove a node from the graph"""
        if name in self.nodes:
            del self.nodes[name]
            self.graph.remove_node(name)
            
    def get_config(self) -> Dict[str, Any]:
        """Get the graph configuration"""
        return self.config.copy()
        
    def set_config(self, config: Dict[str, Any]) -> None:
        """Set the graph configuration"""
        self.config = config.copy() 
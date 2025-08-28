# LLM Agent Library

A library for building stateful, multi-actor LLM applications using LangGraph patterns.

## Directory Structure

```
llm_agent_library/
├── agents/          # Agent implementations and interfaces
├── graphs/          # LangGraph workflow definitions
├── states/          # State management and persistence
├── tools/           # Tool definitions and implementations
├── memory/          # Memory and context management
├── utils/           # Utility functions and helpers
├── tests/           # Unit tests and integration tests
└── docs/            # Documentation and examples
```

## Installation

```bash
pip install -e .
```

## Usage

```python
from llm_agent_library.agents import Agent
from llm_agent_library.graphs import AgentGraph
from llm_agent_library.tools import Tool

# Create an agent
agent = Agent(
    name="research_agent",
    tools=[Tool("search"), Tool("summarize")]
)

# Create a graph
graph = AgentGraph()
graph.add_node(agent)

# Run the graph
result = graph.run("Research quantum computing")
```

## Features

- Agent Management: Create and manage different types of agents
- Graph Workflows: Define complex agent interactions using LangGraph
- State Management: Handle agent state and persistence
- Tool Integration: Easy integration of custom tools and functions
- Memory Systems: Context and memory management for agents
- Utilities: Helper functions and common tools

## Dependencies

- langgraph
- langchain
- pydantic
- typing-extensions

## Contributing

Please read CONTRIBUTING.md for details on our code of conduct and the process for submitting pull requests.

## License

This project is licensed under the MIT License - see the LICENSE file for details. 
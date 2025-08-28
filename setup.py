from setuptools import setup, find_packages

setup(
    name="llm_agent_library",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "langgraph>=0.0.10",
        "langchain>=0.1.0",
        "pydantic>=2.0.0",
        "typing-extensions>=4.5.0",
        "openai>=1.0.0",
        "python-dotenv>=1.0.0",
    ],
    author="Your Name",
    author_email="your.email@example.com",
    description="A library for building stateful, multi-actor LLM applications using LangGraph",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/yourusername/llm_agent_library",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
    ],
    python_requires=">=3.9",
) 
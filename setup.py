from setuptools import setup, find_packages

setup(
    name="langchain-agentic-learning",
    version="0.1.0",
    description="Deep learning repository for agentic systems architecture with LangChain",
    author="Vishal",
    python_requires=">=3.12",
    packages=find_packages(),
    install_requires=[
        "langchain>=1.2.17",
        "langchain-anthropic>=0.1.46",
        "langchain-core>=0.1.50",
        "anthropic>=0.25.0",
        "python-dotenv>=1.0.0",
        "pydantic>=2.5.0",
    ],
    extras_require={
        "dev": [
            "pytest>=7.4.0",
            "pytest-cov>=4.1.0",
            "black>=23.12.0",
            "ruff>=0.1.11",
            "mypy>=1.7.0",
            "jupyter>=1.0.0",
        ]
    },
)

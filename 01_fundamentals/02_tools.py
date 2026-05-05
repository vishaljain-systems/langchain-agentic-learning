#!/usr/bin/env python3
"""
01_fundamentals/02_tools.py

Understanding the @tool Decorator and Tool Design

Key Concepts:
- Tools are the BOUNDARY between agent reasoning and external execution
- @tool decorator turns functions into LLM-callable tools
- Tool signature includes TYPE HINTS and DOCSTRINGS (LLM reads these)
- Tools must VALIDATE input before execution
- Tools must FAIL GRACEFULLY and return useful error messages

This module demonstrates tool design principles.
"""

from langchain.tools import tool
from typing import Annotated
import inspect

def main():
    """Run tools examples."""
    
    print("=" * 70)
    print("02. Tools: The Agent's Interface to the World")
    print("=" * 70)
    
    # Example 1: Simple tools
    print("\n" + "─" * 70)
    print("Example 1: Creating Simple Tools")
    print("─" * 70)
    
    @tool
    def add(a: int, b: int) -> int:
        """Add two numbers together."""
        return a + b
    
    @tool
    def multiply(x: int, y: int) -> int:
        """Multiply two numbers."""
        return x * y
    
    @tool
    def divide(numerator: int, denominator: int) -> float:
        """Divide two numbers. Handles division by zero."""
        if denominator == 0:
            return "Error: Cannot divide by zero"
        return numerator / denominator
    
    print(f"\nTool: {add.name}")
    print(f"Description: {add.description}")
    print(f"Args: {add.args}")
    print(f"Result: add(2, 3) = {add(2, 3)}")
    
    print(f"\nTool: {multiply.name}")
    print(f"Description: {multiply.description}")
    print(f"Result: multiply(4, 5) = {multiply(4, 5)}")
    
    print(f"\nTool: {divide.name}")
    print(f"Description: {divide.description}")
    print(f"Result: divide(10, 2) = {divide(10, 2)}")
    print(f"Result: divide(10, 0) = {divide(10, 0)}")
    
    # Example 2: Tools with validation
    print("\n" + "─" * 70)
    print("Example 2: Tools with Input Validation")
    print("─" * 70)
    
    @tool
    def search_database(
        query: Annotated[str, "SQL query string"],
        limit: Annotated[int, "Maximum number of results (1-100)"]
    ) -> str:
        """
        Search a database. 
        IMPORTANT: Only accepts SELECT queries. Rejects INSERT, UPDATE, DELETE.
        """
        # Validation: only allow SELECT
        if not query.upper().startswith("SELECT"):
            return "Error: Only SELECT queries are allowed"
        
        # Validation: limit range
        if not 1 <= limit <= 100:
            return f"Error: limit must be between 1 and 100, got {limit}"
        
        # Validation: length
        if len(query) > 1000:
            return "Error: Query too long (max 1000 chars)"
        
        # Simulate successful query
        return f"Executed: {query} LIMIT {limit}"
    
    print(f"\nValid query:")
    result = search_database("SELECT * FROM users WHERE age > 18", limit=10)
    print(f"  {result}")
    
    print(f"\nInvalid query (UPDATE):")
    result = search_database("UPDATE users SET age=18", limit=10)
    print(f"  {result}")
    
    print(f"\nInvalid limit:")
    result = search_database("SELECT * FROM users", limit=200)
    print(f"  {result}")
    
    # Example 3: Tools as building blocks
    print("\n" + "─" * 70)
    print("Example 3: Creating a Tool Registry")
    print("─" * 70)
    
    tools = {
        "add": add,
        "multiply": multiply,
        "divide": divide,
        "search_database": search_database,
    }
    
    print(f"\nAvailable tools ({len(tools)}):")
    for name, tool_obj in tools.items():
        print(f"  • {name}: {tool_obj.description}")
    
    # Example 4: Tool inspection (what the LLM sees)
    print("\n" + "─" * 70)
    print("Example 4: Tool Schema (What LLM Sees)")
    print("─" * 70)
    
    print(f"\nTool: {search_database.name}")
    print(f"Description: {search_database.description}")
    print(f"Args schema: {search_database.args}")
    
    # Example 5: Error handling in tools
    print("\n" + "─" * 70)
    print("Example 5: Graceful Error Handling")
    print("─" * 70)
    
    @tool
    def external_api_call(endpoint: str) -> str:
        """Call an external API endpoint."""
        try:
            # Simulate validation
            if not endpoint.startswith("http"):
                raise ValueError("Endpoint must be a valid URL")
            
            if "dangerous" in endpoint:
                return "Error: Access denied to this endpoint"
            
            # Simulate API call
            if endpoint == "http://example.com/data":
                return '{"status": "success", "data": [1, 2, 3]}'
            
            return f"Called {endpoint} successfully"
        
        except ValueError as e:
            return f"Validation error: {e}"
        except Exception as e:
            return f"Unexpected error: {str(e)[:100]}"
    
    print(f"\nValid endpoint:")
    print(f"  {external_api_call('http://example.com/data')}")
    
    print(f"\nInvalid endpoint:")
    print(f"  {external_api_call('/local/path')}")
    
    print(f"\nBlocked endpoint:")
    print(f"  {external_api_call('http://example.com/dangerous')}")
    
    # Summary
    print("\n" + "=" * 70)
    print("Key Takeaways")
    print("=" * 70)
    print("""
1. @tool decorator makes functions callable by agents
2. TYPE HINTS and DOCSTRINGS are critical (LLM reads them)
3. Always VALIDATE input before executing
4. Return ERROR MESSAGES that help the agent understand what went wrong
5. Tools are BOUNDARIES between agent and world
6. Tool design is PLATFORM ENGINEERING, not ML
    """)

if __name__ == "__main__":
    main()

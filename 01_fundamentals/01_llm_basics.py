#!/usr/bin/env python3
"""
01_fundamentals/01_llm_basics.py - Simple working version

Understanding the LLM as a Text Generator, Not an Oracle
"""

from langchain_anthropic import ChatAnthropic
from langchain_core.messages import HumanMessage
import os
from dotenv import load_dotenv

load_dotenv()

def main():
    print("=" * 70)
    print("01. LLM Basics: Text Generation")
    print("=" * 70)
    
    api_key = os.getenv("ANTHROPIC_API_KEY")
    if not api_key:
        print("\n⚠️  ANTHROPIC_API_KEY not set.")
        print("   Set it with: export ANTHROPIC_API_KEY=sk-ant-...")
        return
    
    # Initialize model with correct name
    model = ChatAnthropic(
        model="claude-opus-4-1-20250805",
        api_key=api_key,
        temperature=0,
        max_tokens=500,
    )
    
    # Example 1: Simple question
    print("\n" + "─" * 70)
    print("Example 1: Simple Text Generation")
    print("─" * 70)
    
    prompt = "What is 2 + 2?"
    print(f"\nPrompt: {prompt}")
    
    response = model.invoke([HumanMessage(content=prompt)])
    print(f"\nResponse: {response.content}")
    
    if hasattr(response, 'usage_metadata'):
        usage = response.usage_metadata
        print(f"\nToken Usage:")
        print(f"  Input: {usage.get('input_tokens', 'N/A')}")
        print(f"  Output: {usage.get('output_tokens', 'N/A')}")
    
    # Example 2: Multi-turn conversation
    print("\n" + "─" * 70)
    print("Example 2: Multi-turn Conversation")
    print("─" * 70)
    
    messages = [
        HumanMessage(content="What is the capital of France?"),
    ]
    
    response = model.invoke(messages)
    print(f"\nQ1: What is the capital of France?")
    print(f"A1: {response.content}")
    
    from langchain_core.messages import AIMessage
    messages.append(AIMessage(content=response.content))
    messages.append(HumanMessage(content="How many people live there?"))
    
    response = model.invoke(messages)
    print(f"\nQ2: How many people live there?")
    print(f"A2: {response.content}")
    
    # Example 3: Understanding temperature
    print("\n" + "─" * 70)
    print("Example 3: Temperature (Determinism vs Randomness)")
    print("─" * 70)
    
    prompt = "Complete: The future of AI is..."
    
    print(f"\nPrompt: {prompt}")
    print(f"\nWith temperature=0 (deterministic):")
    
    model_deterministic = ChatAnthropic(
        model="claude-opus-4-1-20250805",
        api_key=api_key,
        temperature=0,
        max_tokens=30,
    )
    
    r1 = model_deterministic.invoke([HumanMessage(content=prompt)])
    print(f"  Response 1: {r1.content}")
    
    r2 = model_deterministic.invoke([HumanMessage(content=prompt)])
    print(f"  Response 2: {r2.content}")
    print(f"  → Both identical (temperature=0)")
    
    # Summary
    print("\n" + "=" * 70)
    print("Key Takeaways")
    print("=" * 70)
    print("""
1. LLMs generate text TOKEN BY TOKEN
2. Each call has INPUT and OUTPUT tokens (different costs)
3. Context window is FINITE (can't pass infinite tokens)
4. TEMPERATURE controls randomness (0=same, 1=varied)
5. CONVERSATION HISTORY = previous messages (you re-send them)
6. Cost scales with tokens; budget management is critical
    """)

if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""
01_fundamentals/01_llm_basics.py

Understanding the LLM as a Text Generator, Not an Oracle

Key Concepts:
- LLMs predict the next token given all previous tokens
- They generate text sequentially, one token at a time
- "Prompts" are just input text; "responses" are generated text
- Cost = (input_tokens + output_tokens) × price_per_token
- Context window is finite (limited tokens it can see at once)

This module demonstrates these core concepts with working examples.
"""

from langchain_anthropic import ChatAnthropic
from langchain_core.messages import HumanMessage
import os

def main():
    """Run LLM basics examples."""
    
    print("=" * 70)
    print("01. LLM Basics: Text Generation, Not Reasoning")
    print("=" * 70)
    
    # Initialize the model
    # This requires ANTHROPIC_API_KEY environment variable
    api_key = os.getenv("ANTHROPIC_API_KEY")
    if not api_key:
        print("\n⚠️  ANTHROPIC_API_KEY not set.")
        print("   Set it with: export ANTHROPIC_API_KEY=sk-ant-...")
        return
    
    model = ChatAnthropic(
        model="claude-opus-4-20250514",
        api_key=api_key,
        temperature=0,  # Deterministic output
        max_tokens=1000,  # Limit output length
    )
    
    # Example 1: Simple text generation
    print("\n" + "─" * 70)
    print("Example 1: Simple Text Generation")
    print("─" * 70)
    
    prompt_1 = "What is 2 + 2?"
    print(f"\nPrompt: {prompt_1}")
    
    response_1 = model.invoke([HumanMessage(content=prompt_1)])
    print(f"\nResponse:\n{response_1.content}")
    
    # Show token usage
    if hasattr(response_1, 'usage_metadata'):
        usage = response_1.usage_metadata
        print(f"\nToken Usage:")
        print(f"  Input tokens: {usage.get('input_tokens', 'N/A')}")
        print(f"  Output tokens: {usage.get('output_tokens', 'N/A')}")
        total = usage.get('input_tokens', 0) + usage.get('output_tokens', 0)
        print(f"  Total: {total}")
    
    # Example 2: Multi-turn conversation
    print("\n" + "─" * 70)
    print("Example 2: Conversation History (Multi-turn)")
    print("─" * 70)
    
    messages = [
        HumanMessage(content="What is the capital of France?"),
    ]
    
    print(f"\nTurn 1 - User: What is the capital of France?")
    response_2a = model.invoke(messages)
    print(f"Assistant: {response_2a.content}")
    
    # Add assistant response to history
    from langchain_core.messages import AIMessage
    messages.append(AIMessage(content=response_2a.content))
    
    # Continue conversation
    messages.append(HumanMessage(content="How many people live there?"))
    print(f"\nTurn 2 - User: How many people live there?")
    response_2b = model.invoke(messages)
    print(f"Assistant: {response_2b.content}")
    
    # Example 3: Token counting (approximate)
    print("\n" + "─" * 70)
    print("Example 3: Understanding Token Economy")
    print("─" * 70)
    
    prompt_3 = """Explain quantum computing in one sentence."""
    
    print(f"\nPrompt: {prompt_3}")
    print(f"Estimated tokens: ~{len(prompt_3.split()) * 1.3:.0f}")
    
    response_3 = model.invoke([HumanMessage(content=prompt_3)])
    print(f"\nResponse: {response_3.content}")
    
    if hasattr(response_3, 'usage_metadata'):
        usage = response_3.usage_metadata
        input_tokens = usage.get('input_tokens', 0)
        output_tokens = usage.get('output_tokens', 0)
        
        # Anthropic pricing (as of 2026)
        # Claude Opus: $15/M input, $75/M output
        input_cost = (input_tokens / 1_000_000) * 15
        output_cost = (output_tokens / 1_000_000) * 75
        total_cost = input_cost + output_cost
        
        print(f"\nToken Economics:")
        print(f"  Input: {input_tokens} tokens → ${input_cost:.6f}")
        print(f"  Output: {output_tokens} tokens → ${output_cost:.6f}")
        print(f"  Total: ${total_cost:.6f}")
    
    # Example 4: Temperature and determinism
    print("\n" + "─" * 70)
    print("Example 4: Temperature Effects (Determinism vs Randomness)")
    print("─" * 70)
    
    prompt_4 = "Complete this: The future of AI is..."
    
    print(f"\nPrompt: {prompt_4}")
    print(f"\nWith temperature=0 (deterministic):")
    
    model_deterministic = ChatAnthropic(
        model="claude-opus-4-20250514",
        api_key=api_key,
        temperature=0,
        max_tokens=50,
    )
    
    response_4a = model_deterministic.invoke([HumanMessage(content=prompt_4)])
    print(f"  Response 1: {response_4a.content}")
    
    response_4b = model_deterministic.invoke([HumanMessage(content=prompt_4)])
    print(f"  Response 2: {response_4b.content}")
    print(f"  → Both identical (temperature=0)")
    
    print(f"\nWith temperature=1 (more variation):")
    
    model_random = ChatAnthropic(
        model="claude-opus-4-20250514",
        api_key=api_key,
        temperature=1,
        max_tokens=50,
    )
    
    response_4c = model_random.invoke([HumanMessage(content=prompt_4)])
    print(f"  Response 1: {response_4c.content}")
    
    response_4d = model_random.invoke([HumanMessage(content=prompt_4)])
    print(f"  Response 2: {response_4d.content}")
    print(f"  → May differ (temperature=1)")
    
    # Summary
    print("\n" + "=" * 70)
    print("Key Takeaways")
    print("=" * 70)
    print("""
1. LLMs generate text TOKEN BY TOKEN, not all at once
2. Every call has INPUT and OUTPUT tokens with separate costs
3. CONTEXT WINDOW is limited (you can only pass so many tokens)
4. TEMPERATURE controls determinism (0 = same always, 1 = varied)
5. CONVERSATION HISTORY is just previous messages; you append and re-send
6. Cost scales with token usage; budget management is critical
    """)

if __name__ == "__main__":
    main()

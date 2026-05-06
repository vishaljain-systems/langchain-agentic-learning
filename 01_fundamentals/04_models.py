#!/usr/bin/env python3
"""
01_fundamentals/04_models.py

Understanding Models, Configuration, and Trade-offs

Key Concepts:
- Different Claude models have different capabilities
- Model selection is a trade-off: speed vs capability vs cost
- Configuration options (temperature, max_tokens) affect behavior
- Same prompt on different models = different results
- For production, you need to choose the right model for the job

This module demonstrates model selection and configuration.
"""

from langchain_anthropic import ChatAnthropic
from langchain_core.messages import HumanMessage
import os
from dotenv import load_dotenv

load_dotenv()

def main():
    """Run models examples."""
    
    print("=" * 70)
    print("04. Models: Choosing the Right Tool for the Job")
    print("=" * 70)
    
    api_key = os.getenv("ANTHROPIC_API_KEY")
    if not api_key:
        print("\n⚠️  ANTHROPIC_API_KEY not set.")
        return
    
    # Example 1: Model comparison
    print("\n" + "─" * 70)
    print("Example 1: Available Claude Models (as of May 2026)")
    print("─" * 70)
    
    models = {
        "claude-3-5-sonnet-20241022": {
            "speed": "Fast",
            "capability": "Good",
            "cost": "Low",
            "use_case": "General tasks, learning, prototyping"
        },
        "claude-opus-4-1-20250805": {
            "speed": "Slower",
            "capability": "Excellent",
            "cost": "Higher",
            "use_case": "Complex reasoning, production systems"
        },
    }
    
    print("\nAvailable models:")
    for model_name, info in models.items():
        print(f"\n  {model_name}")
        print(f"    Speed: {info['speed']}")
        print(f"    Capability: {info['capability']}")
        print(f"    Cost: {info['cost']}")
        print(f"    Best for: {info['use_case']}")
    
    # Example 2: Same prompt, same model (determinism)
    print("\n" + "─" * 70)
    print("Example 2: Determinism (Same Input = Same Output)")
    print("─" * 70)
    
    model = ChatAnthropic(
        model="claude-opus-4-1-20250805",
        api_key=api_key,
        temperature=0,  # Deterministic
        max_tokens=100,
    )
    
    prompt = "Explain causality in one sentence."
    
    print(f"\nPrompt: {prompt}")
    print(f"Temperature: 0 (deterministic)")
    
    print(f"\nRun 1:")
    r1 = model.invoke([HumanMessage(content=prompt)])
    print(f"  {r1.content}")
    
    print(f"Run 2 (same prompt):")
    r2 = model.invoke([HumanMessage(content=prompt)])
    print(f"  {r2.content}")
    
    print(f"\n→ Same output both times (temperature=0)")
    
    # Example 3: Temperature effects
    print("\n" + "─" * 70)
    print("Example 3: Temperature Effects (Randomness Control)")
    print("─" * 70)
    
    prompt = "Write a creative one-sentence description of AI."
    
    print(f"\nPrompt: {prompt}")
    
    print(f"\nWith temperature=0 (very deterministic):")
    model_cold = ChatAnthropic(
        model="claude-opus-4-1-20250805",
        api_key=api_key,
        temperature=0,
        max_tokens=50,
    )
    r1 = model_cold.invoke([HumanMessage(content=prompt)])
    print(f"  {r1.content}")
    
    print(f"\nWith temperature=1 (more creative):")
    model_warm = ChatAnthropic(
        model="claude-opus-4-1-20250805",
        api_key=api_key,
        temperature=1,
        max_tokens=50,
    )
    r2 = model_warm.invoke([HumanMessage(content=prompt)])
    print(f"  {r2.content}")
    
    # Example 4: Max tokens (output length control)
    print("\n" + "─" * 70)
    print("Example 4: Max Tokens (Control Output Length)")
    print("─" * 70)
    
    prompt = "What is machine learning?"
    
    print(f"\nPrompt: {prompt}")
    
    print(f"\nWith max_tokens=30 (short):")
    model_short = ChatAnthropic(
        model="claude-opus-4-1-20250805",
        api_key=api_key,
        temperature=0,
        max_tokens=30,
    )
    r1 = model_short.invoke([HumanMessage(content=prompt)])
    print(f"  {r1.content}")
    print(f"  Length: {len(r1.content)} chars")
    
    print(f"\nWith max_tokens=500 (longer):")
    model_long = ChatAnthropic(
        model="claude-opus-4-1-20250805",
        api_key=api_key,
        temperature=0,
        max_tokens=500,
    )
    r2 = model_long.invoke([HumanMessage(content=prompt)])
    print(f"  {r2.content[:100]}...")
    print(f"  Length: {len(r2.content)} chars")
    
    # Example 5: Configuration strategy
    print("\n" + "─" * 70)
    print("Example 5: Choosing Configuration for Different Tasks")
    print("─" * 70)
    
    configs = {
        "Deterministic task (code generation)": {
            "temperature": 0,
            "max_tokens": 2000,
            "reason": "Need same output every time, allow long responses"
        },
        "Creative task (brainstorming)": {
            "temperature": 1,
            "max_tokens": 1000,
            "reason": "Want variety, moderate length"
        },
        "Question answering": {
            "temperature": 0.5,
            "max_tokens": 500,
            "reason": "Slightly creative but consistent, concise"
        },
        "Agent reasoning": {
            "temperature": 0,
            "max_tokens": 1000,
            "reason": "Need consistent decisions, allow for explanation"
        },
    }
    
    print("\nConfiguration recommendations:")
    for task, config in configs.items():
        print(f"\n  {task}:")
        print(f"    temperature: {config['temperature']}")
        print(f"    max_tokens: {config['max_tokens']}")
        print(f"    Why: {config['reason']}")
    
    # Example 6: Cost implications
    print("\n" + "─" * 70)
    print("Example 6: Cost Implications")
    print("─" * 70)
    
    print("""
Cost model: (input_tokens + output_tokens) × price_per_token

Example: 5-step agent using Opus
  Step 1: 100 input + 50 output = 150 tokens
  Step 2: 200 input + 75 output = 275 tokens
  Step 3: 300 input + 100 output = 400 tokens
  Step 4: 400 input + 125 output = 525 tokens
  Step 5: 500 input + 50 output = 550 tokens
  ─────────────────────────────────
  Total: 2300 tokens per agent run
  
Cost at Opus pricing: ~$0.10-0.15 per run

For 100 agent runs/day: $10-15/day
For production (10,000 runs/day): $1000-1500/day

This is why model selection matters!
    """)
    
    # Summary
    print("\n" + "=" * 70)
    print("Key Takeaways")
    print("=" * 70)
    print("""
1. DIFFERENT MODELS have different trade-offs (speed/cost/capability)
2. TEMPERATURE controls creativity (0 = deterministic, 1 = creative)
3. MAX_TOKENS limits response length (saves tokens = saves money)
4. CONFIGURATION is task-specific (agent ≠ brainstorming)
5. COST SCALES with tokens (need to choose model carefully for production)
6. SAME PROMPT on different models = different results
    """)

if __name__ == "__main__":
    main()

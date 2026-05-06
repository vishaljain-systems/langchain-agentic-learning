#!/usr/bin/env python3
"""
01_fundamentals/03_prompts.py

Understanding Prompts and PromptTemplate

Key Concepts:
- Prompts are instructions you send to the LLM
- PromptTemplate lets you create reusable prompt patterns with variables
- Good prompts = better LLM responses
- System prompts guide behavior, user prompts ask questions
- Few-shot examples teach the LLM by example

This module demonstrates prompt design patterns.
"""

from langchain_core.prompts import PromptTemplate, ChatPromptTemplate
from langchain_anthropic import ChatAnthropic
from langchain_core.messages import HumanMessage, SystemMessage
import os
from dotenv import load_dotenv

load_dotenv()

def main():
    """Run prompts examples."""
    
    print("=" * 70)
    print("03. Prompts: How to Talk to LLMs Effectively")
    print("=" * 70)
    
    api_key = os.getenv("ANTHROPIC_API_KEY")
    if not api_key:
        print("\n⚠️  ANTHROPIC_API_KEY not set.")
        return
    
    model = ChatAnthropic(
        model="claude-opus-4-1-20250805",
        api_key=api_key,
        temperature=0,
        max_tokens=500,
    )
    
    # Example 1: Simple prompt vs structured prompt
    print("\n" + "─" * 70)
    print("Example 1: Simple Prompt vs Structured Prompt")
    print("─" * 70)
    
    print("\nSimple prompt (unstructured):")
    simple_prompt = "Tell me about Python"
    response = model.invoke([HumanMessage(content=simple_prompt)])
    print(f"Response length: {len(response.content)} chars")
    
    print("\nStructured prompt (better):")
    structured_prompt = """You are a Python expert.
Explain Python in exactly 2 sentences.
Focus on: what it is and why it's useful."""
    
    response = model.invoke([HumanMessage(content=structured_prompt)])
    print(f"Response: {response.content}")
    
    # Example 2: PromptTemplate (reusable templates)
    print("\n" + "─" * 70)
    print("Example 2: PromptTemplate (Reusable Patterns)")
    print("─" * 70)
    
    # Create a reusable template
    template = """You are a {role}.
Your task is to explain {topic} in {style}.
Be concise and clear."""
    
    prompt_template = PromptTemplate(
        input_variables=["role", "topic", "style"],
        template=template
    )
    
    # Use it multiple times with different values
    print("\nTemplate example 1:")
    prompt_1 = prompt_template.format(
        role="Software Engineer",
        topic="API design",
        style="one paragraph"
    )
    print(f"Prompt: {prompt_1}\n")
    response = model.invoke([HumanMessage(content=prompt_1)])
    print(f"Response: {response.content}\n")
    
    print("Template example 2 (same template, different values):")
    prompt_2 = prompt_template.format(
        role="Data Scientist",
        topic="Machine Learning",
        style="3 bullet points"
    )
    print(f"Prompt: {prompt_2}\n")
    response = model.invoke([HumanMessage(content=prompt_2)])
    print(f"Response: {response.content}")
    
    # Example 3: System prompts (guide behavior)
    print("\n" + "─" * 70)
    print("Example 3: System Prompts (Guide LLM Behavior)")
    print("─" * 70)
    
    print("\nWithout system prompt:")
    response = model.invoke([
        HumanMessage(content="What is 2+2?")
    ])
    print(f"Response: {response.content}")
    
    print("\nWith system prompt (strict):")
    response = model.invoke([
        SystemMessage(content="You are a math tutor. Always explain your reasoning step by step."),
        HumanMessage(content="What is 2+2?")
    ])
    print(f"Response: {response.content}")
    
    # Example 4: Few-shot examples (teach by example)
    print("\n" + "─" * 70)
    print("Example 4: Few-Shot Examples (Teach by Example)")
    print("─" * 70)
    
    few_shot_prompt = """You are a classification expert. Classify the sentiment as POSITIVE, NEGATIVE, or NEUTRAL.

Examples:
"I love this product!" → POSITIVE
"This is terrible." → NEGATIVE
"The weather is cloudy." → NEUTRAL

Now classify: "This code is really elegant and efficient"
"""
    
    print(f"\nPrompt with examples:\n{few_shot_prompt}\n")
    response = model.invoke([HumanMessage(content=few_shot_prompt)])
    print(f"Response: {response.content}")
    
    # Example 5: ChatPromptTemplate (multi-turn conversations)
    print("\n" + "─" * 70)
    print("Example 5: ChatPromptTemplate (Structured Multi-turn)")
    print("─" * 70)
    
    chat_template = ChatPromptTemplate.from_messages([
        ("system", "You are a helpful Python expert. You answer questions concisely."),
        ("user", "I have a question about {topic}: {question}")
    ])
    
    formatted = chat_template.format_messages(
        topic="list comprehensions",
        question="How do I filter a list?"
    )
    
    print(f"\nFormatted messages:")
    for msg in formatted:
        print(f"  {msg.type}: {msg.content}")
    
    response = model.invoke(formatted)
    print(f"\nResponse: {response.content}")
    
    # Summary
    print("\n" + "=" * 70)
    print("Key Takeaways")
    print("=" * 70)
    print("""
1. SIMPLE prompts often get simple answers
2. STRUCTURED prompts get better results (give format, style, constraints)
3. REUSABLE templates save time (use PromptTemplate)
4. SYSTEM prompts guide LLM behavior (role, instructions)
5. FEW-SHOT examples teach by example (best for complex tasks)
6. GOOD PROMPTS = critical for agentic systems (agent needs to be clear)
    """)

if __name__ == "__main__":
    main()

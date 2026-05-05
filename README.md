# LangChain Agentic Systems - Deep Learning Repository

A comprehensive, hands-on learning repository for understanding agentic systems architecture, ReAct loops, tool design, and platform engineering with LangChain.

**Author:** Vishal (Platform Engineer, 25 years distributed systems)  
**Goal:** Master agentic systems from first principles, not shortcuts.

---

## Repository Structure

```
langchain-agentic-learning/
├── 01_fundamentals/          # Core LangChain concepts
│   ├── 01_llm_basics.py      # LLM as text generator, tokens, prompts
│   ├── 02_tools.py           # @tool decorator, tool design
│   ├── 03_prompts.py         # PromptTemplate, prompt engineering
│   └── 04_models.py          # ChatAnthropic, model configuration
│
├── 02_react_loop/            # Understanding the ReAct pattern
│   ├── 01_phases.py          # Five phases: check, invoke, parse, execute, observe
│   ├── 02_format_check.py    # Phase 1 implementation
│   ├── 03_llm_invocation.py  # Phase 2 with instrumentation
│   ├── 04_output_parsing.py  # Phase 3 robust parsing
│   ├── 05_tool_execution.py  # Phase 4 safe execution
│   ├── 06_observation.py     # Phase 5 state management
│   └── 07_full_loop.py       # Complete ReAct loop
│
├── 03_tools_design/          # Tool framework and patterns
│   ├── 01_tool_registry.py   # Managing multiple tools
│   ├── 02_validation.py      # Input validation
│   ├── 03_error_handling.py  # Graceful failures
│   ├── 04_rate_limiting.py   # Rate limit enforcement
│   ├── 05_permissions.py     # Authorization checks
│   └── 06_sandbox.py         # Safe execution environment
│
├── 04_state_management/      # Persistent state and memory
│   ├── 01_conversation_history.py
│   ├── 02_working_memory.py
│   ├── 03_session_state.py
│   ├── 04_concurrency.py
│   └── 05_persistence.py
│
├── 05_platform_engineering/  # Production concerns
│   ├── 01_token_tracking.py
│   ├── 02_cost_control.py
│   ├── 03_observability.py
│   ├── 04_error_recovery.py
│   └── 05_horizontal_scaling.py
│
├── tests/                    # Test suite
│   ├── test_fundamentals.py
│   ├── test_react.py
│   └── test_tools.py
│
├── notebooks/               # Jupyter notebooks for exploration
│   ├── 01_exploration.ipynb
│   └── 02_architecture.ipynb
│
├── docs/                    # Documentation
│   ├── ARCHITECTURE.md
│   ├── LEARNING_PATH.md
│   └── CONCEPTS.md
│
├── requirements.txt         # Python dependencies
├── setup.py                # Package setup
├── pyproject.toml          # Modern Python project config
├── .gitignore              # Git ignore rules
├── .env.example            # Environment variables template
└── Makefile                # Common commands
```

---

## Learning Path

### **Phase 1: Fundamentals (Week 1)**
- [ ] Understand LLM as text generator, not oracle
- [ ] Learn token counting and context windows
- [ ] Master the `@tool` decorator
- [ ] Understand PromptTemplate
- [ ] Make your first API call to Claude

**Deliverable:** Execute 5 simple tools, understand cost per call

### **Phase 2: ReAct Architecture (Week 2)**
- [ ] Implement each phase manually
- [ ] Parse LLM output robustly
- [ ] Handle parsing errors gracefully
- [ ] Build a complete single-iteration loop
- [ ] Execute a full multi-step agent

**Deliverable:** Working agent that calls multiple tools

### **Phase 3: Tool Design (Week 3)**
- [ ] Design a tool registry system
- [ ] Implement validation framework
- [ ] Add rate limiting and authorization
- [ ] Error handling patterns
- [ ] Sandbox/safety measures

**Deliverable:** Production-ready tool framework

### **Phase 4: State Management (Week 4)**
- [ ] Persistent conversation history
- [ ] Working memory patterns
- [ ] Session isolation and recovery
- [ ] Concurrent access handling
- [ ] Serialization/deserialization

**Deliverable:** Multi-user, multi-session agent platform

### **Phase 5: Platform Engineering (Week 5)**
- [ ] Token tracking and budgeting
- [ ] Cost attribution per user/org
- [ ] Observability (logging, tracing, metrics)
- [ ] Failure recovery patterns
- [ ] Horizontal scaling

**Deliverable:** Production platform for 10,000+ concurrent agents

---

## Getting Started

### Prerequisites
- Python 3.12+
- git
- An Anthropic API key (from console.anthropic.com)
- VS Code (or any editor)

### Setup

1. **Clone and navigate:**
   ```bash
   git clone <your-repo>
   cd langchain-agentic-learning
   ```

2. **Create virtual environment:**
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # or `venv\Scripts\activate` on Windows
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up environment:**
   ```bash
   cp .env.example .env
   # Edit .env and add your ANTHROPIC_API_KEY
   export ANTHROPIC_API_KEY=<your-key>
   ```

5. **Run first example:**
   ```bash
   python3 01_fundamentals/01_llm_basics.py
   ```

6. **Run tests:**
   ```bash
   pytest tests/
   ```

---

## Running Examples

Each module is self-contained and runnable:

```bash
# Fundamentals
python3 01_fundamentals/01_llm_basics.py
python3 01_fundamentals/02_tools.py

# ReAct loop
python3 02_react_loop/01_phases.py
python3 02_react_loop/07_full_loop.py

# Tools design
python3 03_tools_design/01_tool_registry.py

# Run all tests
make test
```

---

## Architecture Overview

### The Five Phases of ReAct

1. **Format Check** — Guard clauses, budget enforcement, limits
2. **LLM Invocation** — API call with instrumentation, error handling
3. **Parse Output** — Extract structured intent from text
4. **Execute Tool** — Safe invocation with timeouts and auth
5. **Observe Result** — Append to state, prepare next iteration

### Token Economy

- Input tokens: Context + user prompt
- Output tokens: LLM generation
- Cost = (input + output) × price_per_token
- Platform must track and enforce budgets per user/org

### State Architecture

- **Session**: One conversation, one user
- **Working Memory**: Current task state
- **Conversation History**: All turns so far
- **Persistent Store**: Database for recovery

---

## Key Concepts

### Agentic vs Orchestration
- **Traditional**: You define the DAG, framework executes it
- **Agentic**: LLM decides the path based on intermediate results
- **Implication**: You can't pre-validate; must be resilient to emergent behavior

### Why Platform Engineering Matters
1. **Unpredictable compute**: 3 steps or 30?
2. **Cost is variable**: Each step costs tokens
3. **Cascading failures**: Error in step 1 cascades downstream
4. **Observability is hard**: Can't pre-instrument emergent paths

### Tool Design Philosophy
- Tools are **permission boundaries**
- Every tool must **validate input**
- Tools must **enforce rate limits**
- Tools must **time out gracefully**
- Tools must **return structured feedback**

---

## Resources

- **LangChain Docs**: https://python.langchain.com/
- **Anthropic API Docs**: https://docs.anthropic.com/
- **Papers**: ReAct (Yao et al., 2022), Chain-of-Thought (Wei et al., 2022)

---

## Development Workflow

### Running Tests
```bash
make test                  # Run all tests
make test-fast            # Fast subset
make coverage             # Generate coverage report
```

### Code Quality
```bash
make lint                 # Check code style
make format               # Auto-format code
make type-check           # Type checking with mypy
```

### Creating a New Module
1. Create `XX_topic/YY_concept.py`
2. Include docstring explaining the concept
3. Include runnable example with output
4. Add corresponding test in `tests/`
5. Update this README with learnings

### Commit Strategy
- Commit after each working example
- Use descriptive messages: "01_fundamentals: Implement tool decorator example"
- Push daily
- Reflect on learnings in commit messages

---

## Notes

**As of:** May 2026  
**Python:** 3.12+  
**LangChain:** 1.2.17+  
**Claude Model:** claude-opus-4-20250514

This repository is a learning journal. Expect:
- Repeated implementations (to internalize concepts)
- Incremental complexity
- Working code at every step
- Deep dives into failure modes

Not a production library. Don't use these patterns as-is in production; instead, understand the tradeoffs and adapt to your requirements.

---

## Contact

Created as part of a serious deep dive into agentic systems architecture for platform engineers.

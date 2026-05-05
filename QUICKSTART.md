# Quick Start (5 Minutes)

Follow these steps to get up and running immediately.

## 1. Copy the Repository

```bash
# If you're starting from the local version:
cp -r /home/claude/langchain-agentic-learning ~/my-learning-repo
cd ~/my-learning-repo

# If you're cloning from GitHub:
git clone https://github.com/YOUR-USERNAME/langchain-agentic-learning.git
cd langchain-agentic-learning
```

## 2. Set Up Environment (2 minutes)

```bash
# Create virtual environment
python3 -m venv venv

# Activate it
source venv/bin/activate  # or: venv\Scripts\activate on Windows

# Install dependencies
pip install -r requirements.txt
```

## 3. Set Your API Key (1 minute)

```bash
# Copy the example
cp .env.example .env

# Edit .env and add your API key
nano .env  # or use your editor
# Change: ANTHROPIC_API_KEY=sk-ant-v0-...
```

## 4. Run Your First Example (1 minute)

```bash
# Fundamentals: LLM basics
python3 01_fundamentals/01_llm_basics.py

# Or: Tools
python3 01_fundamentals/02_tools.py
```

## 5. Initialize Git (Optional, 1 minute)

```bash
# If you haven't already
git init
git config user.email "your-email@example.com"
git config user.name "Your Name"

# Add remote (replace YOUR-USERNAME)
git remote add origin https://github.com/YOUR-USERNAME/langchain-agentic-learning.git

# First commit
git add .
git commit -m "Initial setup: fundamentals module"
git branch -M main
git push -u origin main
```

---

## Next: Open in VS Code

```bash
code .
```

Then:
1. Install Python extension (Ctrl+Shift+X, search "Python")
2. Select Python interpreter (Ctrl+Shift+P → "Python: Select Interpreter")
3. Open terminal in VS Code (Ctrl+`)
4. Run: `source venv/bin/activate`
5. Run: `python3 01_fundamentals/01_llm_basics.py`

---

## That's It!

You now have:
- ✅ A learning repository
- ✅ Python environment with LangChain installed
- ✅ First working examples
- ✅ Git initialized (optional)
- ✅ Ready to start learning

**Next:** Read `01_fundamentals/01_llm_basics.py` to understand LLM basics, then move to the ReAct loop examples.

---

## Helpful Commands

```bash
make test              # Run tests
make format            # Auto-format code
make lint              # Check code style
python3 02_react_loop/01_phases.py   # Run next module
git log --oneline      # View commits
git add . && git commit -m "msg"     # Commit changes
```

Enjoy your learning journey! 🚀

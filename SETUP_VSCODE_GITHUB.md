# VS Code + GitHub Setup Guide

## Prerequisites

- **VS Code** installed (download from code.visualstudio.com)
- **Git** installed (git-scm.com)
- **Python 3.12+** installed
- **GitHub account** (github.com)
- **Anthropic API key** (console.anthropic.com)

---

## Step 1: Clone the Repository Locally

### Option A: Clone an Existing GitHub Repository

```bash
# Replace YOUR-USERNAME with your GitHub username
git clone https://github.com/YOUR-USERNAME/langchain-agentic-learning.git
cd langchain-agentic-learning
```

### Option B: Create a New GitHub Repository

1. Go to https://github.com/new
2. Create a repo named `langchain-agentic-learning`
3. **Do NOT initialize with README** (we have one)
4. Click "Create repository"
5. Follow the instructions to push existing repository:

```bash
cd /home/claude/langchain-agentic-learning

# Configure origin (replace YOUR-USERNAME)
git remote add origin https://github.com/YOUR-USERNAME/langchain-agentic-learning.git
git branch -M main
git push -u origin main
```

---

## Step 2: Set Up VS Code

### Open the Project

```bash
# From the repository directory
code .
```

Or in VS Code: `File → Open Folder → Select langchain-agentic-learning`

### Recommended Extensions

Install these extensions in VS Code (Ctrl+Shift+X):

1. **Python** (Microsoft)
   - ID: ms-python.python
   - Provides IntelliSense, debugging, linting

2. **Pylance** (Microsoft)
   - ID: ms-python.vscode-pylance
   - Better type checking and autocomplete

3. **Git Graph** (mhutchie)
   - ID: mhutchie.git-graph
   - Visualize git history

4. **GitHub Copilot** (GitHub)
   - ID: github.github-copilot
   - AI-powered code suggestions (optional, requires subscription)

5. **Better Comments** (Aaron Bond)
   - ID: aaron-bond.better-comments
   - Color-code comments

6. **Pylint** (Microsoft)
   - ID: ms-python.pylint
   - Real-time linting

### Configure Python Interpreter

1. Open Command Palette: `Ctrl+Shift+P` (or `Cmd+Shift+P` on Mac)
2. Search for "Python: Select Interpreter"
3. Choose the interpreter (should show `.venv` if it exists)

### Set Up Virtual Environment in VS Code

```bash
# In the VS Code terminal (Ctrl+`)
python3 -m venv venv
source venv/bin/activate  # or `venv\Scripts\activate` on Windows
pip install -r requirements.txt
```

---

## Step 3: Configure Environment Variables

1. Copy `.env.example` to `.env`:
   ```bash
   cp .env.example .env
   ```

2. Edit `.env` in VS Code and add your API key:
   ```
   ANTHROPIC_API_KEY=sk-ant-v0-...
   ```

3. **Important:** `.env` is in `.gitignore` — it won't be committed

### VS Code `.env` Support

Add this to `.vscode/settings.json`:

```json
{
    "python.envFile": "${workspaceFolder}/.env",
    "python.linting.enabled": true,
    "python.linting.pylintEnabled": true,
    "python.formatting.provider": "black"
}
```

Create `.vscode/settings.json` if it doesn't exist.

---

## Step 4: Run Your First Example

### In VS Code Terminal

```bash
# Make sure venv is activated
source venv/bin/activate

# Run an example
python3 01_fundamentals/01_llm_basics.py
```

### Or Use the Makefile

```bash
make install          # Install dependencies
make example EXAMPLE=01_fundamentals/01_llm_basics.py
```

### Or Debug in VS Code

1. Open `01_fundamentals/01_llm_basics.py`
2. Click the play button (▶) in the top right
3. Or press `F5` to start debugging
4. VS Code will run the script and show output in the "Debug Console"

---

## Step 5: Daily Development Workflow

### Create a New Learning Module

1. Create a new file: `02_react_loop/01_phases.py`
2. Write your code with docstrings and examples
3. Run it: `python3 02_react_loop/01_phases.py`
4. Debug if needed (set breakpoints with `F9`)

### Commit Your Work

```bash
# Stage changes
git add 02_react_loop/01_phases.py

# Or stage everything
git add .

# Commit with a descriptive message
git commit -m "02_react_loop: Implement phase 1 - format check and budget enforcement"

# Push to GitHub
git push origin main
```

### Or Use VS Code Git UI

1. Open the Source Control panel (Ctrl+Shift+G)
2. Stage files by clicking the "+" icon
3. Write a commit message
4. Click "Commit"
5. Click "Sync" to push

---

## Step 6: Push to GitHub

### One-Time Setup (if using HTTPS)

```bash
# Configure git to cache credentials
git config --global credential.helper store
```

### Push Changes

```bash
git push origin main
```

Or in VS Code:
1. Source Control panel (Ctrl+Shift+G)
2. Click "Sync"

---

## Step 7: Debugging and Running Tests

### Run Tests in VS Code

```bash
# In terminal
pytest tests/ -v

# Or use VS Code Test Explorer (if installed)
# Extensions → Install "Test Explorer UI" extension
```

### Debug a Specific Test

1. Open the test file
2. Set a breakpoint (F9)
3. Right-click on the test function
4. "Debug Test"

### View Test Coverage

```bash
make coverage
# Open htmlcov/index.html in browser
```

---

## Step 8: Code Quality Checks

### Format Your Code

```bash
make format    # Auto-format with black
make lint      # Check style with ruff
make type-check  # Type checking with mypy
```

### Run All Checks

```bash
make format && make lint && make type-check && make test
```

### Set Up Pre-commit Hooks (Optional)

This automatically runs checks before each commit:

```bash
pip install pre-commit
pre-commit install
```

Create `.pre-commit-config.yaml`:

```yaml
repos:
  - repo: https://github.com/psf/black
    rev: 23.12.1
    hooks:
      - id: black
  - repo: https://github.com/charliermarsh/ruff-pre-commit
    rev: v0.1.11
    hooks:
      - id: ruff
```

---

## Step 9: Collaborating on GitHub (Optional)

### Create a Branch for New Work

```bash
git checkout -b feature/react-loop
# Make changes, commit
git push origin feature/react-loop
```

Then on GitHub: Create a Pull Request → Review → Merge

### Pull Changes

```bash
git pull origin main
```

---

## Quick Reference

| Command | Purpose |
|---------|---------|
| `code .` | Open VS Code in current directory |
| `source venv/bin/activate` | Activate virtual environment |
| `python3 01_fundamentals/01_llm_basics.py` | Run a module |
| `make test` | Run all tests |
| `git status` | Check what changed |
| `git add .` | Stage all changes |
| `git commit -m "message"` | Commit with message |
| `git push origin main` | Push to GitHub |
| `git log --oneline` | View commit history |
| `git diff` | See changes before committing |

---

## Troubleshooting

### "Python not found"
```bash
# Check if Python 3.12+ is installed
python3 --version

# Or use
which python3
```

### "ModuleNotFoundError: No module named 'langchain'"
```bash
# Make sure venv is activated and requirements installed
source venv/bin/activate
pip install -r requirements.txt
```

### "ANTHROPIC_API_KEY not set"
```bash
# Set in .env file (don't commit this!)
echo "ANTHROPIC_API_KEY=sk-ant-..." > .env

# Or set in terminal
export ANTHROPIC_API_KEY=sk-ant-...
```

### "Git remote not configured"
```bash
git remote add origin https://github.com/YOUR-USERNAME/langchain-agentic-learning.git
git branch -M main
git push -u origin main
```

### "Merge conflicts"
```bash
# View conflicts
git status

# After resolving in VS Code, stage and commit
git add .
git commit -m "Resolve merge conflicts"
```

---

## Next Steps

1. ✅ Clone/initialize the repository
2. ✅ Set up VS Code with extensions
3. ✅ Create virtual environment and install dependencies
4. ✅ Run the first example: `python3 01_fundamentals/01_llm_basics.py`
5. ✅ Make your first commit: `git add . && git commit -m "First run"`
6. ✅ Push to GitHub: `git push origin main`
7. **Next:** Start Phase 1 of the learning path (fundamentals)

---

## Resources

- **VS Code Python Setup:** https://code.visualstudio.com/docs/python/python-tutorial
- **Git Basics:** https://git-scm.com/book/en/v2
- **GitHub Docs:** https://docs.github.com
- **LangChain Docs:** https://python.langchain.com

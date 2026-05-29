# 🚀 Setup Checklist - Python + DSA + GenAI Roadmap

## ✅ Initial Setup

### 1. Development Environment

- [ ] Install **Python 3.11+** ([Download](https://www.python.org/downloads/))
- [ ] Install **VS Code** ([Download](https://code.visualstudio.com/))
- [ ] Install **Git** ([Download](https://git-scm.com/downloads))

### 2. VS Code Extensions

- [ ] Python (Microsoft)
- [ ] Pylance (Microsoft)
- [ ] Python Debugger
- [ ] Jupyter
- [ ] GitLens
- [ ] GitHub Copilot (Optional, recommended)
- [ ] Thunder Client (for API testing)

### 3. Python Setup

```bash
# Verify Python installation
python --version

# Create virtual environment
python -m venv venv

# Activate virtual environment
# Windows
venv\Scripts\activate
# Mac/Linux
source venv/bin/activate

# Install essential packages
pip install --upgrade pip
pip install jupyter notebook ipython
```

### 4. Git Configuration

```bash
# Configure Git
git config --global user.name "Your Name"
git config --global user.email "your.email@example.com"

# Initialize repository
git init
git add .
git commit -m "Initial commit - Python DSA GenAI Roadmap"

# Connect to GitHub
git remote add origin <your-repo-url>
git push -u origin main
```

---

## 📚 Phase-Specific Setup

### Phase 1: Python Foundations (Weeks 1-4)

- [ ] Python installed and working
- [ ] VS Code configured
- [ ] First "Hello World" program

**No additional setup needed**

---

### Phase 2: Intermediate Python (Weeks 5-8)

- [ ] Install PostgreSQL ([Download](https://www.postgresql.org/download/))
- [ ] Install database GUI (pgAdmin or DBeaver)
- [ ] Install FastAPI and dependencies:

```bash
pip install fastapi uvicorn sqlalchemy psycopg2-binary pydantic
```

---

### Phase 3: DSA + Interview Prep (Weeks 9-16)

- [ ] Create LeetCode account ([LeetCode](https://leetcode.com/))
- [ ] Create HackerRank account (optional)
- [ ] Install data structure visualization tools (optional)

```bash
pip install matplotlib  # For visualizing algorithms
```

---

### Phase 4: GenAI + Agentic AI (Weeks 17-22)

- [ ] Create OpenAI account ([OpenAI](https://platform.openai.com/))
- [ ] Get OpenAI API key
- [ ] Install GenAI packages:

```bash
pip install openai langchain chromadb faiss-cpu tiktoken
pip install langchain-community langchain-openai
pip install python-dotenv  # For environment variables
```

- [ ] Create `.env` file for API keys:

```
OPENAI_API_KEY=your_api_key_here
```

- [ ] Add `.env` to `.gitignore`

---

## 🗂️ Folder Structure Verification

Run this command to verify your folder structure:

```bash
tree /F  # Windows
tree    # Mac/Linux
```

Expected structure:

```
python-genai-roadmap/
├── phase1-python-foundations/
│   ├── week01-python-basics/
│   ├── week02-strings-collections/
│   ├── week03-functions-problem-solving/
│   └── week04-file-exception-handling/
├── phase2-intermediate-python/
│   ├── week05-oop/
│   ├── week06-advanced-python/
│   ├── week07-sql-databases/
│   └── week08-apis-backend/
├── phase3-dsa-interview-prep/
│   └── [8 weeks]
├── phase4-genai-agentic-ai/
│   └── [6 weeks]
├── projects/
├── interview-prep/
├── daily-notes/
├── resources/
└── tracker/
```

---

## 🎯 Progress Tracker Setup

- [ ] Open `tracker/python-dsa-genai-tracker.html` in browser
- [ ] Bookmark the tracker
- [ ] Test the checkbox functionality
- [ ] Verify progress calculation works

---

## 📝 Daily Workflow Setup

### Morning Routine

1. Open VS Code
2. Activate virtual environment
3. Open tracker HTML
4. Review yesterday's notes
5. Plan today's learning

### Evening Routine

1. Push code to GitHub
2. Update tracker
3. Write daily notes
4. Plan tomorrow

---

## 🔧 Useful Commands

### Python Virtual Environment

```bash
# Create venv
python -m venv venv

# Activate (Windows)
venv\Scripts\activate

# Activate (Mac/Linux)
source venv/bin/activate

# Deactivate
deactivate

# Install from requirements
pip install -r requirements.txt

# Generate requirements
pip freeze > requirements.txt
```

### Git Commands

```bash
# Daily workflow
git status
git add .
git commit -m "Day X: Completed topic Y"
git push

# Create new branch
git checkout -b feature/new-topic

# Merge branch
git checkout main
git merge feature/new-topic
```

### Running Python

```bash
# Run Python file
python filename.py

# Interactive Python
python

# Run Jupyter Notebook
jupyter notebook
```

---

## 📦 Essential Python Packages

### Phase 1-2

```bash
pip install requests beautifulsoup4
pip install pandas numpy
pip install pytest  # Testing
```

### Phase 3

```bash
pip install matplotlib seaborn  # Visualization
```

### Phase 4

```bash
pip install openai langchain chromadb
pip install streamlit  # For building AI UIs
pip install gradio    # Alternative UI framework
```

---

## 🛠️ Troubleshooting

### Python not found

- Verify installation: `python --version`
- Add Python to PATH (Windows)
- Reinstall if needed

### Virtual environment issues

- Delete `venv` folder
- Recreate: `python -m venv venv`

### Package installation fails

- Update pip: `pip install --upgrade pip`
- Use `pip3` instead of `pip`
- Check internet connection

### Git push fails

- Verify remote URL: `git remote -v`
- Check credentials
- Generate SSH key if needed

---

## ✅ Final Checklist

Before starting Phase 1:

- [ ] All software installed
- [ ] VS Code extensions active
- [ ] Git configured
- [ ] Virtual environment working
- [ ] Tracker HTML opens in browser
- [ ] GitHub repository created
- [ ] First commit pushed
- [ ] README.md looks good on GitHub

---

## 🚀 Ready to Start!

Once all checkboxes are complete, you're ready to begin:

**Start with**: [Phase 1 Week 1 - Python Basics](phase1-python-foundations/week01-python-basics/)

---

**Last Updated**: May 29, 2026  
**Status**: Setup Complete ✅  
**Next**: Begin Phase 1!

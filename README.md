# Solar Challenge Week 1

## ?? Setup Instructions

### 1. Clone the repository

\\\powershell
git clone https://github.com/your-username/solar-challenge-week1.git
cd solar-challenge-week1
\\\

### 2. Set up virtual environment

\\\powershell
python -m venv venv
.\venv\Scripts\Activate.ps1
pip install -r requirements.txt
\\\

### 3. Run CI

Push to any branch or open a PR to main to trigger GitHub Actions.

## ?? Project Structure

\\\
solar-challenge-week1/
+-- .vscode/
¦   +-- settings.json
+-- .github/
¦   +-- workflows/
¦       +-- ci.yml
+-- .gitignore
+-- requirements.txt
+-- README.md
+-- src/
+-- notebooks/
¦   +-- __init__.py
¦   +-- README.md
+-- tests/
¦   +-- __init__.py
+-- scripts/
    +-- __init__.py
    +-- README.md
\\\

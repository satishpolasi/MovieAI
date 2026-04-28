# Movie AI System

A system that leverages the prepared movie data and LLMs to generate outputs like personalized movie recommendations, user preference summaries, & comparative analyses (e.g., comparing movies based on budget, revenue, or runtime).

## Setup Instructions

```bash
#1. Install
uv python list #List all available python versions. 
uv venv venv --python cpython-3.14.2-macos-aarch64-none

#2. Activate Environment
source venv/bin/activate #Command is for mac. It will be deferent for windows. You need to point to activate.bat 

#3. Install requirement packages
uv pip install -r requirements.txt

#4. Install ipykernel to run the experiments
uv pip install ipykernel

#5. Configure github to commit the code
uv init #To initialile local git in our project folder
git config --global user.name "<your_user_name>" # you need this command only if you are configure git for the first time in this machine
git config user.email "<your_github_account_email>" # you need this command only if you are configure git for the first time in this machine

#6. experiments.ipynb all the experiments with outputs
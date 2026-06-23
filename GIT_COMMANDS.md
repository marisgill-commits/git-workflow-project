# Step-by-Step Commands to Build This Workflow Yourself

## Step 1: Initialize repo and push base code
git init
git add .
git commit -m "chore: initial project setup with app and tests"
git branch -M main
git remote add origin https://github.com/<your-username>/git-workflow-project.git
git push -u origin main

## Step 2: Create develop branch
git checkout -b develop
git push -u origin develop

## Step 3: Feature branch — logging
git checkout -b feature/logging develop
# app.py mein logging function add karo
git add app.py
git commit -m "feat: add logging function for calculator operations"
git push -u origin feature/logging
# GitHub par PR open karo: feature/logging → develop → Merge

## Step 4: Feature branch — square
git checkout develop
git pull origin develop
git checkout -b feature/square
# app.py mein square() function add karo
git add app.py
git commit -m "feat: add square function"
git push -u origin feature/square
# GitHub par PR open karo: feature/square → develop → Merge

## Step 5: Conflict create + resolve
git checkout develop
git pull origin develop
git checkout -b feature/cube
# app.py mein same jagah cube() function add karo
git add app.py
git commit -m "feat: add cube function"
git push -u origin feature/cube
git fetch origin
git merge origin/develop
# Conflict aayega -> app.py manually edit kar ke dono functions rakho
git add app.py
git commit -m "fix: resolve merge conflict between square and cube functions"
git push -u origin feature/cube
# GitHub par PR open karo: feature/cube → develop → Merge

## Step 6: Release to main
git checkout main
git pull origin main
git merge develop
git tag -a v1.0.0 -m "Release v1.0.0"
git push origin main --tags

## Step 7: Verify
python3 -m unittest test_app.py -v
python3 app.py
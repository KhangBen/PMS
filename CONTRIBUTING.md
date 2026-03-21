# Project GitHub Workflow Guide
## Initial Setup (Do This First)

#### Step 1: Clone the Repository**
```bash
git clone https://github.com/KhangBen/PMS.git
cd PMS
```

#### Step 2: Make Sure You’re on main**
```bash
git checkout main
```

#### Step 3: Pull Latest Changes**
```bash
git pull origin main
```

**2. Creating a New Branch (IMPORTANT)**
⚠️ NEVER work directly on main
Create a branch using your initials + feature name:
```bash
git checkout -b ab-feature-name
```

Examples:
git checkout -b kh-features
git checkout -b kh-parking-boundaries
git checkout -b kh-object-detection


**3. Working on Your Code**
Make changes → then save your progress:
```bash
git add .
git commit -m "Describe what you did"
```

Example:
git commit -m "Added ROI detection for bottom half of frame"


**4. Push Your Branch to GitHub**
First time pushing:
```bash
git push -u origin ab-feature-name
```

Examples:
git push -u origin kh-parking-boundaries
git push -u origin kh-object-detection

After that:
```bash
git push
```

**5. Creating a Pull Request (PR)**
Go to GitHub
Click "Compare & Pull Request"
Base: main
Compare: your branch
Add description of what you did
Submit PR

**6. Keeping Your Branch Updated**
Before continuing work:
```bash
git checkout main
git pull origin main
git checkout ab-feature-name
git rebase main
```

**7. Handling Conflicts**
If conflicts happen:
Fix code manually
Then:
```bash
git add .
git rebase --continue
```


**8. After PR is Merged**
Delete your branch:
Local:
```bash
git branch -d ab-feature-name
```

Remote:
```bash
git push origin --delete ab-feature-name
```


🚫 RULES (VERY IMPORTANT)
❌ Do NOT push directly to main
❌ Do NOT reuse old branches
❌ Do NOT commit random changes without messages

✅ BEST PRACTICES
✔ 1 branch = 1 feature
✔ Commit often (small changes)
✔ Use clear commit messages
✔ Always pull before starting work

🧠 Workflow Summary
main → create branch → work → commit → push → PR → merge → delete branch → repeat


🎯 Goal
Keep the code:
Clean
Organized
Easy to collaborate on

💬 If You’re Stuck
Message me on discord and I can help 


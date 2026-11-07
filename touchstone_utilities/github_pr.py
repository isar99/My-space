from git import Repo, GitConfigParser
from datetime import datetime
import os
import random

# === Configuration ===
pat_token = "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"
REPO_PATH = "/Users/isarahmad/Documents/rough/touchstone-api-automation"  # <- Change this
BRANCH_PREFIX = "auto-branch"
repo_url = (f'https://{pat_token}@github.com/VoerEirAB/touchstone-api-automation.git')

# # === Clone Repo ===
if not os.path.isdir(REPO_PATH):
  Repo.clone_from(repo_url, REPO_PATH)
  print(f'✅ Touchstone API automation project is cloned at: {REPO_PATH}')

repo = Repo(REPO_PATH)
config = repo.config_reader()

username = config.get_value("user", "name")
email = config.get_value("user", "email")

print(username, email)

updated_repo_url = (f'https://{username}:{pat_token}@github.com/VoerEirAB/touchstone-api-automation.git')
print(updated_repo_url)

# # === Initialize Repo ===
# repo = Repo(REPO_PATH)
# assert not repo.bare
# os.chdir(REPO_PATH)

# # === checkout to main ===
# main = repo.heads['main']
# main.checkout()
# #verify checked out to main
# current_branch = repo.active_branch.name
# print(f"✅ Checkout to main {current_branch}")

# # === Create and checkout branch ===
# timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
# branch_name = f"{BRANCH_PREFIX}-{timestamp}"
# new_branch = repo.create_head(branch_name)
# print(f"✅ New created branch is {new_branch}")
# new_branch.checkout()
# # verify checked out to new branch
# current_branch = repo.active_branch.name
# print(f"✅ Checked out branch: {current_branch}")


# # === Do some change ===
# os.chdir(REPO_PATH)
# rand_int = random.randint(1,1000)
# filename = f"sample_{rand_int}"
# filepath = os.path.join(REPO_PATH, filename)
# # Generate random content
# content = f"good morning {random.randint(1,1000)}" 

# # Write to file
# with open(filepath, 'w') as f:
#     f.write(content)

# print(f"✅ {filepath}")

# # === Stage all changes ===
# repo.git.add([filepath])  # A=True = all changes (staged + unstaged)

# # === Commit ===
# commit_msg = f"Auto commit on branch {branch_name}"
# repo.index.commit(commit_msg)
# print(f"✅ Committed changes with message: '{commit_msg}'")

# # === Push to origin ===
# origin = repo.remote(name='origin')
# origin.push(refspec=f"{branch_name}:{branch_name}")
# print(f"✅ Pushed branch '{branch_name}' to remote 'origin'")


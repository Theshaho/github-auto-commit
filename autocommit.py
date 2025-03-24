import github
import time
import os

# GitHub credentials
username = "your-username"
password = "your-password"
repo_name = "your-repo-name"

# Create a GitHub object
g = github.Github(username, password)

try:
    # Get the repository object
    repo = g.get_repo(repo_name)
except github.UnknownObjectException:
    print(f"Repository {repo_name} not found")
    exit(1)

# Define the commit message pattern
commit_message = "Commit {}"

# Make 500 commits
for i in range(500):
    # Create a new file
    file_name = f"file_{i}.txt"
    with open(file_name, "w") as f:
        f.write(f"File {i}")

    try:
        # Add the file to the repository
        repo.create_file(file_name, f"Create file {i}", f"File {i}", branch="main")
    except github.GithubException as e:
        print(f"Error creating file {file_name}: {e}")
        continue

    # Commit the file
    try:
        repo.create_commit(f"Commit {i}", [file_name], branch="main")
    except github.GithubException as e:
        print(f"Error committing file {file_name}: {e}")

    # Remove the file
    os.remove(file_name)

    # Wait for 10 minute
    time.sleep(600)

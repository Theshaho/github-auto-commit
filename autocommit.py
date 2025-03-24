import github
import time
import os

# GitHub credentials
username = "your-username"
password = "your-password"
repo_name = "your-repo-name"

# Create a GitHub object
g = github.Github(username, password)

# Get the repository object
repo = g.get_repo(f"{username}/{repo_name}")

# Define the commit message pattern
commit_message = "Commit {}"

# Make 500 commits
for i in range(500):
    # Create a new file
    file_name = f"file_{i}.txt"
    with open(file_name, "w") as f:
        f.write(f"File {i}")

    # Add the file to the repository
    repo.create_file(file_name, f"Create file {i}", f"File {i}", branch="main")

    # Commit the file
    repo.create_commit(f"Commit {i}", [file_name], branch="main")

    # Remove the file
    os.remove(file_name)

    # Wait for 10 minute
    time.sleep(600)

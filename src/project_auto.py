import git
import subprocess

path = input("Please insert the path of the project folder :")

#initialize, add and commit 
new_repo = git.Repo.init(path)
new_repo.index.add('*')
new_repo.index.commit('Initial commit.')

print("The repo has been correctly initialized.")

# Launch the git bash
subprocess.Popen('C:\\Program Files\\Git\\git-bash.exe')

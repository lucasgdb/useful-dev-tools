# Useful Commands

| Command | Description |
| ------- | ----------- |
Git |
`git clone <url copied from github>` | for creating a clone of your repository on your local machine
`git remote add upstream <original repository url>` | for setting the original as the upstream remote
`git status` | for getting the status of the cloned repository folder to see what changes have been made, if any
`git checkout -b <new-branch-name> upstream/master` | for creating a new branch from the latest upstream version
`git add <filepath>` | for adding your changes to the <filepath>
`git add --interactive` or `git add -i` | add modified contents in the working tree interactively to the index
`git commit -m "<description of changes>"` | for committing your changes to github
`git push origin <your-branch-name>` | for pushing your changes to your github repo clone
`git branch` | for listing, creating, or deleting branches.
`git pull origin <branch-name>` | downloads the most recent changes to a branch (very useful when working as a team) 
`git merge <branch-name>` | merges branch-name into your current branch
`git push --set-upstream <remote> <name-of-your-branch>` or `git push -u origin <branch_name>` | upload newly created branch to remote 
`git log` | Show commit logs 
`git show [ commit id ]` | This command is used to list the metadata for the specified commit 
`git revert <commit id>` | Reverts changes made by specified commit 
`git cherry-pick <commmit id(s)>` | This command will apply the changes of the listed git commit hashes in the current branch.
`git stash` | Stores the current working changes so they can be restored at a later time if desired.
`git stash pop` | Restores the most recently stashed changes.
`git reset --hard` | Resets the current branch to the latest commit.
`git rebase <branch-name>` | Reapply commits from <branch-name> on top of branch that is currently in, help to sync between branch to avoid "n commit behind master"
Terminal |
`cd <file path name>` | for setting the directory inside the cmd window to the desired path name
Other |
`npx add-gitignore` | for adding a git ignore file to your project for a specific language
`ssh <username>@<some address> (-p <port number>)` | Remotely connect to different server/computer for those that doesn't want to use additional file (e.g. PuTTY)
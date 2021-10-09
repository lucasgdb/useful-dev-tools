# Useful Commands

| Command | Description |
| ------- | ----------- |
| **Git** |
`git add <filepath>` | for adding your changes to the <filepath>
`git add --interactive` or `git add -i` | add modified contents in the working tree interactively to the index
`git branch` | for listing, creating, or deleting branches.
`git checkout -b <new-branch-name> upstream/master` | for creating a new branch from the latest upstream version
`git cherry-pick <commmit id(s)>` | This command will apply the changes of the listed git commit hashes in the current branch.
`git clone <url copied from github>` | for creating a clone of your repository on your local machine
`git commit -m "<description of changes>"` | for committing your changes to github
`git log` | Show commit logs 
`git merge <branch-name>` | merges branch-name into your current branch
`git pull origin <branch-name>` | downloads the most recent changes to a branch (very useful when working as a team) 
`git push origin <your-branch-name>` | for pushing your changes to your github repo clone
`git push --set-upstream <remote> <name-of-your-branch>` or `git push -u origin <branch_name>` | upload newly created branch to remote 
`git rebase <branch-name>` | Reapply commits from <branch-name> on top of branch that is currently in, help to sync between branch to avoid "n commit behind master"
`git remote add upstream <original repository url>` | for setting the original as the upstream remote
`git reset --hard` | Resets the current branch to the latest commit.
`git revert <commit id>` | Reverts changes made by specified commit 
`git show [ commit id ]` | This command is used to list the metadata for the specified commit 
`git stash pop` | Restores the most recently stashed changes.
`git stash push -m <stash_message> <file_path>` | Save a specific file to the stash
`git reset --hard` | Resets the current branch to the latest commit.
`git rebase <branch-name>` | Reapply commits from <branch-name> on top of branch that is currently in, help to sync between branch to avoid "n commit behind master"
| **Windows Terminal** | 
`attrib` | display file attributes
`cd <file path name>` | For setting the directory inside the cmd window to the desired path name.
`chkdsk` | check volumes
`chkntfs` | display/change volume check at startup
`cls` | The command line screen will be cleared.
`defrag` | defragment media
`diskpart`| volume management
`driverquery` | display installed devices and their properties
`format` | format volumes
`ipconfig` | display IP network settings
`ls –option directory_name` | The output will be the listing of the directory contents.
`label` | change volume name
`mode` | configure interfaces/devices
`mountvol` | assign/delete drive mountpoints
`move` | move/rename files
`mkdir new_directory_name` | The user running this command must have suitable rights over the parent directory to create a directory or they will receive an error.
`touch` | The touch command is used to create a file
`rmdir directory_name`| The user running this command must have suitable rights over the parent directory to remove a directory or they will receive an error
`rename` | rename files
`replace` |	replace files
`tree` | display folder structure graphically
`type` | display content of text files
`verify` | monitoring whether volumes are written correctly
`vol` | show volume description and serial numbers of the HDDs
| **Linux Terminal** |
`cat filename` | Displays the file content
`cd <file path name>` | For setting the directory inside the cmd window to the desired path name
`clear` | The command line screen will be cleared.
`echo $VARIABLE` | To display value of a variable
`env` | Displays all environment variables
`export Variable=value` | To set a value of the environment variable
`history` | Display or manipulate the history list
`less <filename>` | Show files in some page
`locate <filename>` | Show the directory where the file is located
`lsblk` | lists information about all available or the specified block devices
`man <comman_name>` | Display user mannual of the command
`mkdir new_directory_name` | The user running this command must have suitable rights over the parent directory to create a directory or they will receive an error.
`mv Source_File_name Destination_File_Name` | Move file from source to destination.
`pwd` | The current working directory will be displayed.
`rmdir directory_name`| The user running this command must have suitable rights over the parent directory to remove a directory or they will receive an error
`rm file_name` | Remove files from the directory.
`rmdir /S <folder name>` | Remove a directory (folder) along with all the files in it
`touch` | The touch command is used to create a file
| **Docker** |
`docker build -t myimage:latest .` | Build an image called myimage using the Dockerfile in the same folder where the command was executed.
`docker build -t [username/]<image-name>[:tag] <dockerfile-path>` | Build an image.
`docker exec -it mywildfly bash` |  Execute and access bash inside a WildFly container.
`docker --help` | List of commands in Docker
`docker history [username/]<image-name>[:tag]` | Check the history of an image.
`docker images` | List the images.
`docker login` | Login to docker hub registry
`docker ps -a` |  List all containers.
`docker ps` |  List only active containers.
`docker push [registry/][username/]<image-name>[:tag]` | Push an image to a registry.
`docker rm $(docker ps -q -f “status=exited”)` | Remove all stopped containers.
`docker rm [container-name/container-id]` |  Remove a stopped container.
`docker rm -f $(docker ps-aq)` |  Remove all containers.
`docker rm -f [container-name/container-id]` | Force stop and remove a container.
`docker rmi [username/]<image-name>[:tag]` | Remove an image from the local registry.
`docker stop [container-name/container-id]` |  Stop a container.
`docker stop -t1` | Stop a container (timeout = 1 second).
`docker system prune` | Remove unused data
`docker tag <image-name> <new-image-name>` | Creates a new image with the latest tag.
`docker tag <image-name>[:tag][username/] <new-image-name>.[:new-tag]` | Creates a new image specifying the “new tag” from an existing image and tag.
`docker version` | Get docker version information
| **Other** |
`mongodump --db database_name --collection collection_name` | Dump your database for backup
`mongorestore --db database_name path_to_bson_file` | To import your backup file to mongodb
`npx add-gitignore` | For adding a git ignore file to your project for a specific language
`scp <username>@<some address><source file> (-p <port number>) <username>@<some address><target file>` | Secure copy protocol (SCP) is a means of securely transferring computer files between a local host and a remote host or between two remote hosts
`ssh <username>@<some address> (-p <port number>)` | Remotely connect to different server/computer for those that doesn't want to use additional file (e.g. PuTTY)

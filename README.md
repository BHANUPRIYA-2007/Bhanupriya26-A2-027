# Bhanupriya26-A2-027
## CREATING MY FIRST GITHUB REPOSITORY : (27 August 2026}
## started at 9:00am;
I'm learning about this from a Youtube video by the channel called " Tech with Tim"
{https://youtu.be/DVRQoVRzMIY?si=AUfhZrsICELsAsWo}

*cd = change directory 
*mkdir name = creates a folder named "name"
*git init = makes the folder inside which we are a git repository
once we initialize a folder as git, we can use all sorts of git commands on that folder

*cd..(back) = goes to the previous directory 
*git add filename = adds the file to the staging area, meaning this file is ready to be commited
*git add . = adds all file to the staging area
*git status = shows the states of the repository
*git commit -m"a message that explains the change you made"
*git checkout -b branch_name = creates a new branch and switches to it from the master branch
*git checkout branch_name = changes to the branch

*git merge branch_name = merges the change from the branch_name and the branch that you are inside
*git remote add remote_name https://yourremoteurl = adds a new remote with the remote_name of the link
*git push -u remote_name branch_name = push changes to a remote repository
*git pull remote_name branch_name = pull changes from a remote repository

1. Rename your local 'master' branch to 'main'
git branch -m master main

2. Pull the existing files from the remote 'main' branch to sync them
git pull origin main --rebase

3. Push your newly renamed local 'main' branch to the remote server
git push -u origin main

4. you can safely delete the accidental remote master branch
git push origin --delete master

## Done at 11:27 am 


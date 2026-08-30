# Bhanupriya26-A2-027
## CREATING MY FIRST GITHUB REPOSITORY : (27 August 2026}
## started at 9:00am;
I'm learning about this from a Youtube video by the channel called " Tech with Tim"
{https://youtu.be/DVRQoVRzMIY?si=AUfhZrsICELsAsWo}

* cd = change directory 
* mkdir name = creates a folder named "name"
* git init = makes the folder inside which we are a git repository
once we initialize a folder as git, we can use all sorts of git commands on that folder

* cd..(back) = goes to the previous directory 
* git add filename = adds the file to the staging area, meaning this file is ready to be commited
* git add . = adds all file to the staging area
* git status = shows the states of the repository
* git commit -m"a message that explains the change you made"
* git checkout -b branch_name = creates a new branch and switches to it from the master branch
* git checkout branch_name = changes to the branch

* git merge branch_name = merges the change from the branch_name and the branch that you are inside
* git remote add remote_name https://yourremoteurl = adds a new remote with the remote_name of the link
* git push -u remote_name branch_name = push changes to a remote repository
* git pull remote_name branch_name = pull changes from a remote repository

1. Rename your local 'master' branch to 'main'
  * git branch -m master main

2. Pull the existing files from the remote 'main' branch to sync them
  * git pull origin main --rebase

3. Push your newly renamed local 'main' branch to the remote server
  * git push -u origin main

4. you can safely delete the accidental remote master branch
  * git push origin --delete master

## Done at 11:27 am 

# STARTED WITH THE SECOND TASK
## 2:15 pm

### just learned how to display an image in opencv 
img = cv2.imread('ugv_r3_task2/1.png', 1)
here ,
* IMREAD_COLOR(or 1): Default behavior. Loads the image as a 3-channel BGR color image and discards any transparency/alpha channel.cv2.
* IMREAD_GRAYSCALE (or 0): Converts and loads the image strictly in 1-channel grayscale.cv2.
* IMREAD_UNCHANGED (or -1): Loads the image exactly as it is, preserving transparency alpha channels if it is a PNG.

TWO WAYS TO RESIZE AN IMAGE:
* img = cv2.resize(img, (1280,720))
img = cv2.resize(img, (0,0), fx=0.5,fy = 0.5)

WAY TO ROTATE THE IMAGE:
* img = cv2.rotate(img, cv2.ROTATE_90_CLOCKWISE)

WAY TO SAVE THE IMAGE:
* cv2.imwrite('IMAGE1.jpeg' , img)

* learning how to add certain shapes on the image
like rectangle ,arrowed lines, circle , lines etc.

# at 8:56pm:

* learned how to add text on the image
* learning about region of interest
* learning Canny edge detection from the youtube channel "programming knowledge"
* removing noise reduction(using gaussian filter) --> gradient calculation(sobel kernel) --> non - maximum supression -- > double thresholding and edge tracking by hystersis.

* i had a very hard time understanding area of interest , because what works for one image may not work for the other.
but it is very interesting to learn, so i have finally completed the second task also .



## DONE WITH THE SECOND AND THIRD TASK NOW!! 

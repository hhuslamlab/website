Things to sort out and be aware of before doing this:
- [ ] Where do you plan on using git? On Windows? On your WSL? You have to install git where you plan on saving all of your repositories. You cannot switch between terminals as you wish to once you install git on one system ~~(You can, if you know how to and enjoy chaos, but don't go open an issue if you do)~~
- [ ] This tutorial is written for Linux users and Windows users who use a Linux subsystem, which allows them to access Linux via the `ubuntu` terminal. Consider looking into the [WSL](https://docs.slam.phil.hhu.de/#/wsl) guide first, if you use neither.  
- [ ] Know, that one of the authors only learnt 70% of this all 3 hours prior to writing this documentation

# Getting started with git
There are some things to do first before working with git. That is, you need to register to the website, so do [that first on github](https://github.com/).  
### Step 1: Setting up git on your computer
Once you are done, you need to download git to your Linux sub system. There is an executable `git bash` terminal for windows out there, but the commands for that one have not been tested by me yet. If you use WSL, do not install `git bash` for windows, instead, open `ubuntu` and run this line  
```shell=
git --version
```
If you get something that reads 
```shell=
git version <someNumberHere>
```
You already have git installed! Skip to Step 2!  
Else, run this command
```shell=
sudo apt install git
```
After it's done installing, the next step is to configure your name and your email, so all of your files can be traced back to you.  
```
git config --global user.name "YourNameAsYouLike
git config --global user.email "youremail@hhu.deOrWhatever"
```
At this point you can decide whether you want to create a designated folder where you store all of your repositories and git related files. This will make your life easier later, since you are still at the beginning, but that is up to you.

Take a breath. Here comes the second step.

### Step 2: Linking your `local` with your `remote`
Whenever you see the terms local and remote, know that they refer to your `local machine` (the computer you are using right now) and a `remote server` (the servers on github that store all of your data). In order to push and pull files to and from the correct accounts, you need a key that attests that the account on github you just created is indeed connected to your own computer. Github uses `SSH keys` for this task. You will have to generate a key in your terminal and add it to your profile on their website. You only have to do this entire step once.  

1. In your terminal, type the line below to create a key. Make sure the email is the same you used to sign up to github as that will be the used as the label for the key.
```shell=
ssh-keygen -t ed25519 -C "youremail@hhu.deOrWhatever"
``` 
2. The key will be saved on your default directory in a hidden folder called `.ssd`. If you don't really know what you are doing, press enter when you see these two messages
```shell=
Enter a file in which to save the key (/<yourDefaultDirectory>/.ssh/id_ed25519):
Enter passphrase (empty for no passphrase): 
```
3. The key's `fingerprint` is displayed on your screen along with a cute randomart image. Locate the key files in your file explorer. You should be able to find two files named `id_ed25519` and `id_ed25519.pub` in the `.ssd` folder. Right-click the file that has the `.pub` extension and copy its content
4. Back on browser, hop over to `profile > settings > SSH and GPG` click new `SSH key` and select `authentification key`. You can name it whatever you like, if you use multiple devices, call it after the machine you are using, so you know where the edits are coming from. Paste the info you copied into the box below and `add SSH key`.
6. *Voila!* You should know see the `fingerprint` of your key under the name you gave it. Lastly, to make sure you don't have to input the key everytime you do anything, you can pass on your key to an `ssh-agent` who will manage your key automatically. Execute the following lines
```shell= 
eval "$(ssh-agent -s)"
ssh-add ~/.ssh/id_ed25519
```

You are done, when you see
```
Identity added: /<yourDirectory>/.ssh/id_ed25519 (youremail@hhu.deOrWhatever)
```

# Making your own repository, commit things, and push them
You have created something and are ready to push it to github. Your first step is to create a repository.

### Step 1: Make a repository and get its SSH address
In your browser, go to your Github profile and click the little [+] next to your icon to create a new repository. Follow the instructions on the screen. For now you don't need to add a `READ.ME` or a`.gitignore` or a license. Make sure your repository name uses underbars _ instead of `spaces`. Create a repository.

A new page will show up, click on the `SSH Key` tab and check the address that is shown there. It should look like this

```shell=
git@github.com:<YourName>/<YourRepository'sName>.git
```
Keep the tab open, we will need this later.

### Step 2: Committing your files

At this point, make sure the files you want to push are in a non-compressed/non-zipped folder somewhere on your computer. You may want to move your files to a folder that you can easily access with your terminal.

In your terminal, navigate to that folder, go inside it and type the following line.

```shell=
git init -b main 
```
This will show the following message 
```shell=
Initialized empty Git repository in <YourFolder'sPath>
```
You have initialised, that is created, a new branch (`-b`) which you called  `main`.
Check your status.

```shell=
git status
```
Check the info:
```shell=
On branch main

No commits yet

Untracked files:
  (use "git add <file>..." to include in what will be committed)
                <TheNamesOfYourFilesButInRed>
nothing added to commit but untracked files present (use "git add" to track)
```
The files are listed in red, meaning they are on your locale. Next, type

```shell=
git add .
```

This (.) will add all prior shown files for pushing. The files should show in green now, when you check `git status` again.
```shell=
On branch main

No commits yet

Changes to be committed:
  (use "git rm --cached <file>..." to unstage)
              <YourFilesButNowInGreen>
```
If all is fine, you are ready to commit. Type a message(`-m`) so you know what this commit is about. The quotation marks are necessary.
```shell=
git commit -m "First commit!" 
```
### Step 3: Pushing your files

Now go back to the open tab from Step 1 and copy the `SSH address` of your repository. Execute these lines:

```shell=
git remote add origin <theRepo'sSSHkey>
```

```shell=
git remote -v 
```
And finally, push everything with this line:

```shell=
git push origin main 
```


### Step 4: Authenticate yourself in the eyes of github after August 2021

Github has removed password authentification when using `git push origin main`. Upon pushing, the console will ask for the `Username` and the `Password`, but will not accept the password that you have set when you signed up for github.

```shell=
remote: Support for password authentication was removed on August 13, 2021.
remote: Please see https://docs.github.com/en/get-started/getting-started-with-git/about-remote-repositories#cloning-with-https-urls for information on currently recommended modes of authentication.
fatal: Authentication failed for <YourNameOnGithub>
```

So what you have to do now is using a so called `access token` instead of your password.

1. On Browser, visit your github profile, go to `settings > developer settings > personal access tokens` and choose `tokens (classic)`
2. Name your token in a way that you can recognise it and set an expiration date, a 7 day window is fine
3. Select your permissions for the token, it is suggested that you select as little as possible, but I had no time looking into [all of them](https://docs.github.com/en/developers/apps/building-oauth-apps/scopes-for-oauth-apps) so I just selected all for now
4. Copy the generated access token that is shown on the screen into your clipboard and save it in some file that only you can access. It's your new password for the next 7 days.
5. Go back to your console, navigate back into your folder  try this again
```shell=
git push origin main
```
It will ask for your `Username`, so provide that and enter.
When it asks for your `Password`, paste your `access token` and confirm. 
This should push your files to your repository.

### Step 5: Rinse and Repeat
When you make changes to your files and wish to update your files, this is how you push changes to your repository.

In your terminal, navigate to the file you wish to update.
```shell=
git add <nameOfYourFile>
```
```shell=
git commit -m "messageThatSummarisesWhatChangesYouMade"
```
```shell=
git push
```

# Cloning repository
In case you want to work on 





# How to delete branches
1. Be on the masterbranch
2. Execute this
```shell=
git branch -D <nameOfYourBranch>
```
and the file is gone from your locale. Run 
```shell=
git push origin --delete <nameOfYourBranch>
```
to delete it from your remote.

# The workflow
[Anna]() told me, that the general workflow is as follows:
1. Navigate to a project and make sure you are on the `master branch` and up to date
```shell= 
git status
git pull
```
if you are not, do this to get on the master branch
```shell=
git checkout master
```
2. Create a new branch `(-b)` from the `master branch` with
```shell= 
git checkout -b <NameOfYourNewBranch>
``` 
3. This new branch only exist on your `locale` right now, so in order to notify your `remote` about its existence and track future changes, run this command
```shell=
git push --set-upstream origin <NameOfYourNewBranch>
```

4. Stay on your new branch, make your changes, add files
5. When you are done, push your changes to your branch and make a `pull request` on the github website of the repository you were working on. A `pull request` will let the admin know, that you want changes on your branch to be included on the `master branch`.
6. Once the admin pulls your changes, you can delete your branch. Please delete your branch to make sure you delete your branch so it is easier to track. 


An overview of the most important git commands can be found [here](https://www.hostinger.com/tutorials/basic-git-commands)


### Authors  
[Anh Kim Nguyen](https://slam.phil.hhu.de/authors/anh/)
[Anna Stein](https://slam.phil.hhu.de/authors/anna/)
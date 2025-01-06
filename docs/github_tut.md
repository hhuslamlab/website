Things to sort out and be aware of before doing this:
- [ ] Where do you plan on using git? On Windows? On your WSL? You have to install git where you plan on saving all of your repositories. You cannot switch between terminals as you wish to once you install git on one system ~~(You can, if you know how to and enjoy chaos, but don't go open an issue if you do)~~
- [ ] This tutorial is written for Linux users and Windows users who use a Linux subsystem. Consider looking into the [WSL](https://docs.slam.phil.hhu.de/#/wsl) if you would like to use WSL. More documentation on `git bash` for only Windows may follow in the future.


- [Getting started with git](#getting-started-with-git)
	- [Step 1: Setting up git](#step-1-setting-up-git-on-your-computer)
	- [Step 2: Locale and Remote](#step-2-linking-your-local-with-your-remote)
- [Making a repository](#making-your-own-repository-commit-things-and-push-them)
	- [Committing files](#step-2-committing-your-files)
	- [Pushing files](#step-3-pushing-your-files)
	- [Token authentification](#step-4-authenticate-yourself-in-the-eyes-of-github-after-august-2021)
	- [Keep your Repository updated](#step-5-rinse-and-repeat)
- [Cloning a repository](#cloning-a-repository)
- [Workflow suggestion](#the-workflow)
- [Erase your mistakes](#erase-your-mistakes)
    - [Restoring files](#restoring-files-you-have-changed-by-mistake)
    - [Delete Branches](#delete-branches)
    - [Go back to a previous commit](#restoring-the-head-of-the-current-branch)    
- [More commands](#more-commands)


# Getting started with git
There are some things to do first before working with git. That is, you need to register to the website, so do [that first on github](https://github.com/).  

### Step 1: Setting up git on your computer

#### Windows
Once you are set, you need to download git. There is an executable `git bash` terminal for windows out there and _the commands in this tutorial should work the same way for that one_. In your windows terminal, simply type:  
```shell=
winget install Git.Git
```
Then, with `Cortana` look for an application called `Git Bash` and use it for the rest of this tutorial. Follow the `git config --global user` instructions further down this section.

#### Linux and WSL

If you wish to use WSL, do not install `git bash` for windows, instead, open `ubuntu` and run this line  
```shell=
git --version
```
If you get something that reads 
```shell=
git version <someNumberHere>
```
You already have git installed! This can happen, because Linux may come with git.  
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
2. The key will be saved on your default directory in a hidden folder called `.ssd`. If you don't really know what you are doing, press enter when you see these three messages
```shell=
Enter a file in which to save the key (/<yourDefaultDirectory>/.ssh/id_ed25519):
Enter passphrase (empty for no passphrase): 
Confirm passphrase:
```
3. The key's `fingerprint` is displayed on your screen along with a cute randomart image. Locate the key files in your file explorer. You should be able to find two files named `id_ed25519` and `id_ed25519.pub` in the `.ssd` folder. Right-click the file that has the `.pub` extension, `open in editor` and copy its content
4. Back on browser, hop over to `profile > settings > SSH and GPG` click new `SSH key` and select `authentification key`. You can name it whatever you like, if you use multiple devices, call it after the machine you are using, so you know where the edits are coming from. Paste the info you copied into the box below and `add SSH key`.
6. *Voila!* You should now see the `fingerprint` of your key under the name you gave it. Lastly, to make sure you don't have to input the key everytime you do anything, you can pass on your key to an `ssh-agent` who will manage your key automatically. Execute the following lines
```shell= 
eval "$(ssh-agent -s)"
ssh-add ~/.ssh/id_ed25519
```
You are done with the setup, when you see:
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
git status
```
Check the files that you have modified and add them:
```shell=
git add <nameOfYourFile>
```
```shell=
git commit -m "messageThatSummarisesWhatChangesYouMade"
```
```shell=
git push
```

# Cloning a repository
In case you are joining in on an existing project, you will have to  `clone` the repository:

1. Visit the repo's github page and copy its SSH key 
2. In your terminal, navigate to the folder you want to keep the repo in and run
```shell=
git clone <Repo's SSH key>
```
3. Follow the workflow of the project you are joining

# The workflow
[Anna](https://slam.phil.hhu.de/authors/anna/) told me, that we generally avoid committing and pushing changing to the `master branch`. The `master branch` is the branch that is actually going to show on the internet, so all changes made to it should undergo careful review first. Depending on the project we are working on, it may have a different name, like `main` or. Instead, we create our own branches, make changes to them, push alterations to them and create a pull request on the website, which have to undergo reviews first. This ensures that no one makes unwanted changes to our website.
The workflow of our website therefore is as follows:

1. Navigate to a project and make sure you are on the `master branch` and up to date
```shell= 
git status
git pull
```
if `git status` tells you you aren't on the masterbranch yet, use the `checkout` command to get there
```shell=
git checkout master
```
2. Create a new branch `(-b)` from the `master branch` with
```shell= 
git checkout -b <NameOfYourNewBranch>
``` 
3. When `pulling`, the source of your `pulls` is by default the `remote branch` that bears the same name as your `local branch`. If you are working alone in a repository, will prevent you from accidentally overwriting your data. However, if you work in a team, you are likely to want to track the changes everyone is making on the `master branch`. You can change the source from where your branch is `pulling` from by setting an `upstream` (`-u`). The following command translates to "git push (Set the `upstream` of `NameOfYourBranch` to the `origin` it was created from)":
```shell=
git push -u origin <NameOfYourNewBranch>
```
4. Stay on your new branch, make your changes, add files
5. When you are done, `git commit` and `git push` your changes to your branch and make a `pull request` on the repository's page in browser. A `pull request` will let the admin know, that you want changes on your branch to be included in the `master branch`.
6. Once the admin pulls your changes, you can delete your branch. Please delete your branch to make sure changes are easy to track. 

# Erase your mistakes
We make mistakes. Github is a safe space for making mistakes, that's what version control is for, after all. Below are some  things you can do, regarding deleting or reverting mistakes.

### Restoring files you have changed by mistake
You have changed some files and it broke something. You do not remember how the original file looked like.
In cases like these, use this:
```shell=
git status
```
Check what the name of the files are, that you want to revert back. Then type this:
```shell=
git restore <name of file>
```
And it will restore the files back to when you last committed a change.

### Delete branches
After successful merging, you can choose to delete your local branch. Or you have made so many branches already, you want to declutter the stale ones. To delete branches, do the following:

1. Be on the masterbranch
2. Execute this
```shell=
git branch -D <nameOfYourBranch>
```
and the file is gone from your locale. Run 
```shell=
git push origin --delete <nameOfYourBranch>
```
to delete it from your remote. Alternatively, you can also delete it from the `branches` menu on browser.

### Resetting the head of the current branch
If you pushed something to a branch or want to restore the current state (head) of the branch to a previous one (because this is what version control is for) do the following:
1. Be on the branch you want to change. You can check this with `git status`. 
2. Get a history of previous commit IDs, messages and authors with `git log`. Copy the commit ID that corresponds to what you would like to be the last change of the branch. Everything before that will be undone. The commit ID can look like the following: 
```sh
commit 5d6cf483ed24fdeb9e4a6bcf61c04bf13b4ba501
```

3. In order to restore the branch to the state of that commit use the command below and substitue (only) the number of the commit ID for `<commit ID>`. Use `:`+ `q` to quit the logs.
```sh
git reset --hard <commit ID> 
```

4. Use `git log` again to test if it worked. 
5. Now push the changes to the remote with `git push origin HEAD --force`

You have successfully erased your mistakes :moyai:


# More commands
More documentation is to come. For now, an overview of the most important git commands can be found [here](https://www.hostinger.com/tutorials/basic-git-commands)

### Authors  
[Anh Kim Nguyen](https://slam.phil.hhu.de/authors/anh/) :bowtie:
  
[Anna Stein](https://slam.phil.hhu.de/authors/anna/) 

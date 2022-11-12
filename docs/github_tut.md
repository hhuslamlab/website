# Making your own repository and commit, and push things there (WSL)
You have created something and are ready to push it to github. Your first step is to create a repository.

### Step 1: Make a repository and get its SSH address
In your browser, go to your Github profile and click the little [+] next to your icon to create a new repository. Follow the instructions on the screen. For now you don't need to add a `READ.ME` or a`.gitignore` or a license. Make sure your repository name uses underbars _ instead of `spaces`. Create a repository.

A new page will show up, click on the `SSH Key` tab and check the address that is shown there. It should look like this

```sh
git@github.com:<YourName>/<YourRepository'sName>.git
```
Keep the tab open, we will need this later.

### Step 2: Committing your files

At this point, make sure the files you want to push are in a non-compressed/non-zipped folder somewhere on your computer. You may want to move your files to a folder that you can easily access with your terminal.

In your terminal, navigate to that folder, go inside it and type the following line.

```sh
git init -b main 
```
This will show the following message 
```sh
Initialized empty Git repository in <YourFolder'sPath>
```
You are initialising something on the `main` branch (`-b`)
Check your status.

```sh
git status
```
Check the info:
```sh
On branch main

No commits yet

Untracked files:
  (use "git add <file>..." to include in what will be committed)
                <TheNamesOfYourFilesButInRed>
nothing added to commit but untracked files present (use "git add" to track)
```
The files are listed in red, meaning they are on your locale. Next, type

```sh
git add .
```

This (.) will add all prior shown files for pushing. The files should show in green now, when you check `git status` again.
```sh
On branch main

No commits yet

Changes to be committed:
  (use "git rm --cached <file>..." to unstage)
              <YourFilesButNowInGreen>
```
If all is fine, you are ready to commit. Type a message(`-m`) so you know what this commit is about. The quotation marks are necessary.
```sh
git commit -m "First commit!" 
```
### Step 3: Pushing your files

Now go back to the open tab from Step 1 and copy the `SSH address` of your repository. Execute these lines:

```sh
git remote add origin <YOUR SSH ADDRESS>
```

```sh
git remote -v 
```
And finally, push everything with this line:

```sh
git push origin main 
```


# Authenticate yourself in the eyes of Github after August 2021 (WSL)

Github has removed password authentification when using `git push origin main`. Upon pushing, the console will ask for the `Username` and the `Password`, but will not accept the password that you have set when you signed up for github.

```sh
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
```sh
git push origin main
```
It will ask for your `Username`, so provide that and enter.
When it asks for your `Password`, paste your `access token` and confirm. 
This should push your files to your repository.

### Author  
[Anh Kim Nguyen](https://slam.phil.hhu.de/authors/anh/)
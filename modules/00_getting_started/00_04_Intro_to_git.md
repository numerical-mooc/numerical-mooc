Based heavily on [this intro](https://github.com/barbagroup/teaching-materials/blob/master/git/00-GettingStarted.md) by @anushkrish.

# Intro to git

Version control is a method to keep track of changes that we introduce to a set of files or documents that we use. This is especially useful when writing code because most code is written and improved through incremental changes. Version control allows us to compare newer versions of code with older versions, and investigate when certain changes were made that may have caused the code to malfunction. Git is a one such version control software, which was created by Linus Torvalds to help with writing the Linux kernel.

Version control systems store files in a directory known as a repository. Apart from the files, a repository also contains information about the history of each file, and all the edits that were made. In this tutorial, we will learn how to create a Git repository, add files to it, make changes to those files, and record the history of those changes.

## Before anything else
When we write commit messages (this is all coming up) we need to use a text editor.  The default text editor, `vim`, is... unfriendly.  It's incredibly powerful but not the way you want to start off.  In light of that, let's change the default editor to the more friendly `nano` by doing the following in a terminal (we only do this once, the changes will persist):

```
echo "export EDITOR=nano" >> .bashrc
source .bashrc
```

## `git config`
Before we use Git, we have to configure two small things to help track the changes we make to files.
Please run the following two commands, filling in your personal info.  Make sure to use the same email address that you used to sign up for Github.

```
git config --global user.email "your.github.email"
git config --global user.name "First Last"
```

If you copy+paste these, make sure to do it one line at a time.  If you paste two lines into a terminal, it will run the first command automatically and Git will think your email address is "your.github.email".

## Creating a `git` repository
First we are going to make a new directory that will become our first git repository.  
Do you remember the command to make a new directory?  It's `mkdir`!  We like to keep all of our `git` directories in a folder called "git".  Let's make that folder first.

```
mkdir git
```

Now let's `cd` into the `git` folder and make a new folder called "first_repo" that will be, unsurprisingly, our first repository.

```
cd git
mkdir first_repo
```

**Careful:** If you are used to using spaces in folder names, watch out!  On linux (and OSX) if you run the command

```
mkdir first repo
```

You'll actually end up with *two* folders, one called `first` and one called `repo`.

### Add a Python script to the new directory

Let's `cd` into `first_repo` and then create a quick Python script.

```
cd first_repo
nano HelloWorld.py
```

### What's `nano`?
`nano` is a simple terminal-based text editor.  There are several incredibly powerful terminal based editors (vim, emacs) but they come with pretty steep learning curves.  `nano` is much friendlier.

The file `HelloWorld.py` doesn't exist, but we run `nano HelloWorld.py` and it creates that file and opens it for editing.

### Back to the script
Type

```Python
print("Hello, World!")
```

on the first line.  Then hit Ctrl+o to save the file, then Ctrl+x to exit `nano`.  

## Initializing a repository

Now we have a folder called `first_repo` with the script `HelloWorld.py` in it.  We want to convert this folder into a Git repository, which is easy!  

First, check that you are in the folder you created with `pwd`.

```
pwd
```

If you are in the right place, then run

```
git init
```

Now `first_repo` is a Git repository.

## Repo status

We can check the status of the repository using

```
git status
```

which will return the following:

```
# On branch master
#
# Initial commit
#
# Untracked files:
#   (use "git add <file>..." to include in what will be committed)
#
#   HelloWorld.py
nothing added to commit but untracked files present (use "git add" to track)
```

#### What's going on here?

* The history of the repository is stored along a timeline known as a *branch*.  We're on the "main" (and only) branch.
* At any point of time, the user can choose to save a snapshot of all the files in the repository. Each snapshot is referred to as a *commit*. The act of saving a snapshot is referred to as *committing changes*.


## Adding files to the repository

The status command also told us that we have an "Untracked file" (`HelloWorld.py`).  That means that `HelloWorld.py` isn't part of any snapshots and its history isn't being recorded by Git.

The output also tells us what we must do to commit our changes: `(use "git add <file>..." to include in what will be committed)`. So let's do that, and check the status again:

```
git add HelloWorld.py
git status
```

which gives us

```
# On branch master
#
# Initial commit
#
# Changes to be committed:
#   (use "git rm --cached <file>..." to unstage)
#
#   new file:   HelloWorld.py
#
```

Note that this still does not commit the changes. The `git add` command adds the file to what is known as the staging area. This is where all the changes to the files that are ready to be committed are stored. All files in the staging area are listed under "Changes to be committed:". We can see that `HelloWorld.py` has been added to this list.

## Committing changes

We want to save a snapshot of the repository as it is right now; it's time to commit!

```
git commit
```

This will open `nano` and you will see a bunch of information about the commit you are making.  Don't worry about that too much for now, let's instead focus on writing our first commit message.  Write out a commit message on the first line, something like

```
First commit.  Add HelloWorld.py
```

Then hit Ctrl+o to save and then Ctrl+x to quit.

Congratulations!  You just made your first commit!  Writing good commit messages is a habit you want to develop. It will help both you and anyone else who uses your code down the line.  Try to follow the guidelines on [this page](http://tbaggery.com/2008/04/19/a-note-about-git-commit-messages.html) when writing commit messages.


Check the status of the repository again:

```
git status
```

and you should see

```
# On branch master
nothing to commit (working directory clean)
```

## Editing a tracked file

Now, suppose you decide to make some changes to the file. Instead of printing "Hello world!", you want to display "Greetings Earth! We come in peace." Open `nano` again to edit the file

```
nano HelloWorld.py
```

and make the appropriate changes to the file:

```
print("Greetings Earth! We come in peace.")
```

Ctrl+o and Ctrl+x to save and quit, then check the status of the repository again

```
git status
```

You should see

```
# On branch master
# Changes not staged for commit:
#   (use "git add <file>..." to update what will be committed)
#   (use "git checkout -- <file>..." to discard changes in working directory)
#
#   modified:   HelloWorld.py
#
no changes added to commit (use "git add" and/or "git commit -a")
```
You have a list of files that have been changed since the last commit, along with some tips on what you can do with them.

## Viewing changes

We only changed one line in one file -- you probably remember that pretty clearly at this point.  But sometimes you might edit several lines, or go grab some coffee and come back, and find you can't remember everything you've done.  This is where `git diff` comes in.  It will show all the changes made to the current repository (even if they aren't committed yet!).  Try it out!

```
git diff
```

The output will look something like this:

```
diff --git a/HelloWorld.py b/HelloWorld.py
index ed708ec..ce3f2ef 100644
--- a/HelloWorld.py
+++ b/HelloWorld.py
@@ -1 +1 @@
-print "Hello world!"
+print "Greetings Earth! We come in peace."
```

All the lines starting with `-` are those that have been removed, and the lines beginning with `+` are the ones that have been added. In our case, we can see that `print("Hello world!")` has been removed and `print("Greetings Earth! We come in peace.")` has been added to the file.

## Committing changes

We want to add the changes we made to the history of the "HelloWorld.py" file.  To do this, we follow the same steps as when we first added the file.

First, we "stage" the changes by running

```
git add HelloWorld.py
```

Now check the repo status again (you'll be typing this out LOTS):

```
> git status
# On branch master
# Changes to be committed:
#   (use "git reset HEAD <file>..." to unstage)
#
#   modified:   HelloWorld.py
#
```

Now we're ready to commit that change!  But it's a pretty simple change, isn't it?  If we know that we don't need to write out a more complicated commit message, we can use a shortcut:

```
git commit -m "Edit the message to sound more friendly"
```

The `-m` flag is short for `message`.  This command will commit the changes with the message we pass to it.  No need to open `nano` this time!

## Viewing a repo's history
We have saved two snapshots of this repository.  We can look at the list of all commits using the `git log` command

```
git log
```

which will output something like

```
commit e9d7cbab2205d00d5ef574fcae8ff75701529565
Author: Gil Forsyth <gforsyth@...>
Date:   Tue Aug 19 16:36:08 2015 -0400

    Edit the message to sound more friendly.

commit 16bb3d3b5af5e485e4713a3fdefcff7ae88ce7df
Author: Gil Forsyth <gforsyth@...>
Date:   Tue Aug 19 15:45:12 2015 -0400

    First commit. Add HelloWorld.py.
```

## Uploading your repository to Github

One of the nifty features of Git is that it allows you to copy the folder containing the repository to any other location, and all the information regarding the history of the repository is also transferred automatically. It also allows you to create a backup of your repository on a remote server. Services like Github run servers where you can host your repositories for free. 

Create an account on Github and follow the [instructions](https://help.github.com/articles/creating-a-new-repository) to create your own Github repository. 

To avoid confusion, it's a good idea to give the Github repository the same name as the folder on your computer.

After the repository is created, Github will display instructions to push an existing repository to Github using the command line. The commands are:

```
git remote add origin https://github.com/gforsyth/first_repo.git
git push -u origin master
```

Of course, you should make the appropriate changes so it reflects your Github username and the name of your repository.

`git remote add` is the command used to specify information about the remote repository to which you want to upload. To do this, we need to provide a name for the remote, and the address of the server where it is hosted. In the above, we name the remote repository `origin` (by convention), and specify the URL created by Github. 

`git push` is used to push all changes from the local repository to the remote repository. The `-u` flag is only used the first time you push a new branch.

### `403 Forbidden while accessing...`
Older version of `git` will sometimes throw errors while attempting to push to GitHub or any other site that uses HTTPS authentication.  If you get the above error when trying to `git push` you can fix it with one extra line:

```
git remote add origin https://github.com/gforsyth/first_repo.git
git remote set-url origin https://gforsyth@github.com/gforsyth/first_repo.git
git push -u origin master
```

Make sure to change the username and repository name to match what you have created.  If you are using an older version of `git`, the easiest solution is to upgrade, but if you can't for whatever reason, then running that extra command when you set up a new repository should fix the issue.

## Look at your repo on Github
Your changes should be reflected immediately on Github.  The URL for your repo should be `https://github.com/<your username>/first_repo`.  Take a look around.  You can look at the file(s) you pushed and also look at the commit history of your repository.  

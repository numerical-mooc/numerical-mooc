#Intro to git

Version control is a method to keep track of changes that we introduce to a set of files or documents that we use. This is especially useful when writing code because most code is written and improved through incremental changes. Version control allows us to compare newer versions of code with older versions, and investigate when certain changes were made that may have caused the code to malfunction. Git is a one such version control software, which was created by Linus Torvalds to help with writing the Linux kernel.

Version control systems store files in a directory known as a repository. Apart from the files, a repository also contains information about the history of each file, and all the edits that were made. In this tutorial, we will learn how to create a Git repository, add files to it, make changes to those files, and record the history of those changes.

##Before anything else
When we write commit messages (this is all coming up) we need to use a text editor.  The default text editor, `vim`, is... unfriendly.  It's incredibly powerful but not the way you want to start off.  In light of that, let's change the default editor to the more friendly `nano` by doing the following in a terminal (we only do this once, the changes will persist):

```
echo "export EDITOR=nano" >> .bashrc
source .bashrc
```
##`git config`
Before we use Git, we have to configure two small things to help track the changes we make to files.
Please run the following two commands, filling in your personal info.  Make sure to use the same email address that you used to sign up for Github.

```
git config --global user.email "your.github.email"
git config --global user.name "First Last"
```

If you copy+paste these, make sure to do it one line at a time.  If you paste two lines into a terminal, it will run the first command automatically and Git will think your email address is "your.github.email".

##Creating a `git` repository
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

###Add a Python script to the new directory

Let's `cd` into `first_repo` and then create a quick Python script.

```
cd first_repo
nano HelloWorld.py
```

###What's `nano`?
`nano` is a simple terminal-based text editor.  There are several incredibly powerful terminal based editors (vim, emacs) but they come with pretty steep learning curves.  `nano` is much friendlier.

The file `HelloWorld.py` doesn't exist, but we run `nano HelloWorld.py` and it creates that file and opens it for editing.

###Back to the script
Type

```Python
print("Hello, World!")
```

on the first line.  Then hit Ctrl+o to save the file, then Ctrl+x to exit `nano`.  

Now we have a folder called `first_repo` wiht the script `HelloWorld.py` in it.  We want to convert this folder into a Git repository, which is easy!  Just type

```
git init
```

Now `first_repo` is a Git repository.  We can check the status of the repository using

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

What's going on here?

* The history of the repository is stored along a timeline known as a *branch*.  We're on the "main" (and only) branch.
* At any point of time, the user can choose to save a snapshot of all the files in the repository. Each snapshot is referred to as a *commit*. The act of saving a snapshot is referred to as *committing changes*.

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

We want to save a snapshot of the repository as it is right now

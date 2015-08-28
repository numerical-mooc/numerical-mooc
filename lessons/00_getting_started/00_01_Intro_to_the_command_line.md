#Intro to the command line

Welcome!  The command can be one of the most powerful ways to interact with a variety of computer systems, but it can also be a little confusing at first glance.  This mini-crash-course should help familiarize you with the basics of command line usage and navigation.  

##Quick config step

This one bit we are asking you to do before we explain anything else.  Please open up a terminal

Applications -> System Tools -> Terminal

Now copy the two lines below by selecting them and hitting Ctrl+c and then paste them into the terminal using Ctrl+Shift+v and hit \<Enter\>.  **Note** that Ctrl+v doesn't work, you need to add Shift.  

```Bash
echo "export PATH=/opt/anaconda/bin:\$PATH" >> .bashrc
echo "export PS1=\"\u \w \"" >> .bashrc
```

Now, to activate the options we just selected, type the following line in the terminal and hit \<Enter\>

```Bash
source .bashrc
```

It should look a little something like this:

![image](https://gist.githubusercontent.com/gforsyth/e21639591d61e436433f/raw/7c4f02f87dbaf77d1b1ddeb662a033bc7aa5fea3/1.bashrc.gif)

##`whoami`

Time to get started!  You might have noticed that the prompt used to read `-bash-4.1$`.  Now it should display your username instead.  That's one of the tweaks we made above.  Not all prompts are so friendly and if you ever lose track of what user you're logged in as, you can always run

```Bash
whoami
```

to find out who you are.

![whoami](https://gist.githubusercontent.com/gforsyth/e21639591d61e436433f/raw/7a7d92d3b5dc0e1ab3f08fc72af62d59fb6463ce/2.whoami.gif)

##`pwd`

We know who we are, time to find out *where* we are.  You can always find out what folder you're in by using the "print working directory" command, or `pwd`.  Try it out!

```Bash
pwd
```

![pwd](https://gist.githubusercontent.com/gforsyth/e21639591d61e436433f/raw/6c1efde71f8eb9cc978ebbb9332100c0ac22f486/3.pwd.gif)

We're in our home directory.  This is the base directory for a regular user in Linux.  In the SEAS labs, the home directory is always `/home/seas/<username>`

##`ls`

We know who we are and where we are, now it's time to figure out what's in here.  We use the "list" command, `ls`, to view any files or directories that are in the current folder.

```Bash
ls
```

![ls](https://gist.githubusercontent.com/gforsyth/e21639591d61e436433f/raw/c3c7b6c0a087de5c3e663192382e4707b40fc50e/4.ls.gif)

The items you see above in the gif are all folders.  They're the usual folders created by default in Red Hat Linux.  Your home folder is actually the same folder as your Titan network drive on Windows, so you may have other files and folders in your home directory.  

##`cd`

To navigate to a new folder, we use the change directory command, `cd`, followed by the name of the folder.  While you *can* type out the full folder name, it's usually nicer to use what's called Tab-completion.  

Let's change to the `Pictures` directory.  Type `cd Pi` and then hit the TAB key to complete the directory name.  Then hit \<Enter\>

Now you're in the `Pictures` directory.  It's probably empty, but you can check with `ls`.  Notice also that the command-prompt has changed to show your current location.  

To go back to your home directory, type `cd ..`

The `..` is a command-line shortcut to move "up" one folder in a directory tree.  Try `cd`-ing into a few other folders and then returning back to your home directory to get the hang of moving around.  

![cd](https://gist.github.com/gforsyth/e21639591d61e436433f/raw/3ace959d96bf313523c1eef5f5083d9a46d14c77/5.cd.gif)

###Tab-completion

If there are multiple possible completions for a partial directory name, you can ask the terminal to display them by hitting TAB twice.  Try entering

```Bash
cd Do
```

and then hit TAB twice to see the list of matching directories.  Then you can add a `c` and Tab-complete `Documents`.

![cdtabtab](https://gist.github.com/gforsyth/e21639591d61e436433f/raw/69ffcfc51baa77ab104d10bcf547b147c0917768/6.cdtabtab.gif)

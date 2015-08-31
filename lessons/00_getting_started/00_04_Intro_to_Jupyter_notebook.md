# Intro to Jupyter notebooks

## What is the Jupyter Notebook?
We'll work extensively with [Jupyter Notebooks](https://jupyter-notebook.readthedocs.org/en/latest/notebook.html) (formerly IPython Notebooks) in this course. They are media-rich documents that combine text with markown formatting, typeset mathematics with MathJax, and executable Python statements.

The best way to understand the notebooks is to try them out, so let's get started!

## Launching the notebook server

To launch the notebook server, first open up a terminal and then enter

```Bash
jupyter notebook
```

This will start the notebook server.  It *should* automatically open the main page of the notebook server in your default browser, but if it doesn't, simply open the browser of your choice and enter

```
http://localhost:8888/tree
```

in the address bar.  

This will bring up a simple file-browser that will show the contents of the directory where you've launched the terminal from.  Click on the `New Notebook` button and then select **Python 3** at the bottom to create your first notebook.

![newnotebook](./images/newnotebook.gif)

##Executing a code cell

Below the toolbars, you'll see a single code cell, prepended with `In [ ]:`.  This cell can contain an arbitrarily long code segment, but we'll start with a simple one liner.  In that lone code cell, type

```Python
x = 5
```

and then hit *Shift+Enter*.  If you just hit Enter you'll find that it will simply add another line to the current cell.  So remember, **to execute a cell**, it's **Shift+Enter**.  

So what happened?  We've assigned the label x to the number 5.  And also you should see that the label of that cell will now read `In[1]:` because that's the first statement we've executed in this Python kernel.  You'll also notice that the notebook has created a new cell, since we already used the only existing cell.  

In this new cell, let's try to print out the value we assigned to x, so enter


```Python
print(x)
```

and then hit **Shift+Enter**.  And there's the output we expect!  The cell gets labeled `In[2]:` and the output of that command is printed immediately below the cell.

The whole procedure should look something like this:

![runandprint](./images/runandprint.gif)

##The Kernel
Don't worry too much about what the "kernel" is, but the main point to remember here is that we can assign a variable in one cell but still access it in a separate cell.  The cells are ways for *us* to divide up our thoughts and our code, but everything is connected underneath.  

##Overwriting variables

Since each cell is interacting with the same Python instance, if we give `x` a new value and then enter `print(x)` we'll get that new value.  That's pretty straight forward —but what if we then delete the cell where we gave `x` a new value?

Let's take a look!

![overwrite](./images/overwrite.gif)

## Download using git

You can `git clone` the library from Jake Vanderplas' GitHub repository: [https://github.com/jakevdp/JSAnimation](https://github.com/jakevdp/JSAnimation)

```Bash
git clone https://github.com/jakevdp/JSAnimation.git
```

## Download without git

If you don't want to clone the repo, you can instead download a zipfile snapshot

[https://github.com/jakevdp/JSAnimation/archive/master.zip](https://github.com/jakevdp/JSAnimation/archive/master.zip)

Download and unzip the file.  You can extract it anywhere since you'll be deleting the folder after installation is complete.

## Install JSAnimation Library

Now open a terminal in the newly created JSAnimation folder and install the library into your current Python environment 

```Bash
python setup.py install --user
```

## Clean up

JSAnimation is now installed.  If you `git clone`d the repository, you can keep it and use it to update JSAnimation whenever updates are released, or you can delete it and just re-clone it at a later date.  

If you downloaded the zip file, you can go ahead and delete both the zip file and the extracted folder.  

## Note for users with Python 3 *and* Python 2
If you're using multiple environments (with Anaconda or virtualenv) you have to install the JSAnimation library into each environment.   
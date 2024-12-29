# Setup your python environment
You are free to setup your python environment however you like. The following is my recommended approach and what I will assume you have done for the purposes of this course.

1. [Install Conda](#1-install-conda)
2. [Configure Conda](#2-configure-conda)
3. [Create a sandboxed python environment for this course](#3-create-a-sandboxed-python-environment-for-this-course)
4. [Install Visual Studio Code (VSCode)](#4-install-visual-studio-code-vscode)
5. [`OPTIONAL:` Install JupyterLab](#5-optional-install-jupyterlab)
- [Python in the cloud](#python-in-the-cloud)

# 1. Install conda
I highly recommend installing [miniforge](https://github.com/conda-forge/miniforge) which includes `conda`.

- **macOS**: You can first install [Homebrew](https://brew.sh/), then run `brew install miniforge`. Finally, if it is not already there, copy the *conda initialize* portion added to your `.bash_profile` to your `.zshrc`.

# 2. Configure Conda
Conda groups collections of packages into [channels](https://docs.conda.io/projects/conda/en/latest/user-guide/concepts/channels.html). Most of the packages that you will install for this course will come from either the defaults or [conda-forge](https://conda-forge.org/docs/user/introduction.html) channels. Conda only searches channels that you tell it to. To setup conda so that it automatically searches the [conda-forge](https://conda-forge.org/docs/user/introduction.html) channel before searching the defaults channel, open a command shell or terminal and run:
```
conda config --add channels conda-forge
```
To see a list of all of the channels that conda will search (top = highest priority, bottom = lowest priority):
```
conda config --show channels
```
Note that you can always specify the channel to search when installing packages on a per package basis.

# 3. Create a sandboxed python environment for this course
First, create a new conda environment named "neu365p". In a command shell or terminal run:
```
conda create --name neu365p
```
Next, set neu365p as the active environment for all conda commands. Run:
```
conda activate neu365p
```
Now install the latest version of the `python` package into the active (neu365p) environment.
```
conda install python
```

⚠️ Note that each time you open a new command shell or terminal, you will need to activate the conda environment that you want to use:
```
conda activate neu365p
```
The currently active environment should be displayed in your command prompt, e.g. `(neu365p)`.

You can see a list of all your conda environments with:
```
conda env list
```
You can see a list of all installed packages in your active environment with:
```
conda list
```
If you ever want to delete this environment and start over:
```
conda remove --name neu365p --all
```
For just about everything else you can do with conda there is a plethora of available online information.

# 4. Install Visual Studio Code (VSCode)
There are a variety of user interfaces for Python coding from the most basic text editor and cmd shell to more complex integrated development environments (IDEs) with more features such as [VSCode](https://code.visualstudio.com/), [JupyterLab](https://jupyter.org), [PyCharm](https://www.jetbrains.com/pycharm/), etc. I recommend VSCode, but if you have any issues I suggest just trying one of the others which should offer an equivalent experience (see below for instructions on installing JupyterLab). *It does NOT matter which user interface you use* so long as it supports Jupyter notebooks which we will use in this course. Both VSCode and JupyterLab will give you a pretty similar experience, as will several other IDEs.

1. Download [Visual Studio Code (VSCode)](https://code.visualstudio.com/)
2. Open VSCode and install the `Python` and `Jupyter` extensions.
3. In VSCode, Select `View->Command Palette...` and search for and select `Python: Select Interpreter`, then select the Python version associated with your neu365p environment (e.g., something like `Python 3.12.0 ('neu365p')`).
4. In VSCode you can set the python interpreter for each individual file. When you open a python file the interpreter will be displayed in one of the corners. Make sure it is set to the python version associated with your neu365p environment, otherwise repeat step #3 above.

# 5. `OPTIONAL:` Install JupyterLab
[JupyterLab](https://jupyter.org) is a complete python integrated development environment (IDE) that supports Jupyter notebooks (which we will use in this course). It runs in a tab in your browser.

First make sure your neu365p environment is active:
```
conda activate neu365p
```
Then use `pip` to install JupyterLab into your active (neu365p) environment. *Note: When you installed python you also got pip.*
```
pip install jupyterlab
```
To open JupyterLab as a tab in your browser, make sure your neu365p environment is active and then simply run the command:
```
jupyter lab
```
When you are done using JupyterLab, from within the JupyterLab browser interface select `File->Shutdown`.

# Python in the cloud
[Google Colab](https://colab.research.google.com) is a purely cloud-based option that is worth taking a look at. However, for this course I want you to setup a local python environment on your computer by following steps 1-4(5) above. This way you will be able to familiarize yourself with managing your own packages and virtual environments, both of which are important skills for working in a general python ecosystem.

# ---
# jupyter:
#   jupytext:
#     cell_metadata_filter: all
#     notebook_metadata_filter: all,-language_info,-toc,-latex_envs
#     text_representation:
#       extension: .py
#       format_name: percent
#       format_version: '1.3'
#       jupytext_version: 1.3.2
#   kernelspec:
#     display_name: 'Python 3.7.6 64-bit (''numeric'': conda)'
#     language: python
#     name: python37664bitnumericcondabd5c031d404d4597ae8310d0bb6bf5f0
# ---

# %% [markdown]
# # VScode notes
#
# ## First, make sure conda-forge is your preferred channel
#
# ```
# % conda config --show channels
# channels:
#   - conda-forge
#   - defaults
# ```
#
# If defaults is above conda-forge, revers this with:
#
# ```
# % conda config --prepend channels conda-forge
# Warning: 'conda-forge' already in 'channels' list, moving to the top
# ```
#
# ## Next install vscode from https://code.visualstudio.com/download
#
# Install the command line version as well. On windows, this should be done as part of 
# the install.  On MacOS, you need to open the vscode command pallette (&#8984;shift-P) and type
# ```
# Shell Command: Install 'code' 
# ```
#
# once that is done, you should be able to start vscode from the command line in a particular
# folder by typing:
#
# ```
# code .
# ```
#
# ## Some definitions
#
# In vscode a "workspace" is any folder containing a folder named .vscode or a file ending in `code-workspace`.
# The .vscode folder denotes a "single root" workspace, in which everything in the tree below
# the folder containing the .vscode file has the same default specifications.  If instead the folder contains
# a "code-workspace" file, then the workspace is "multiroot" and can have independent toplevel .vscode settings.
# Here is an example of a [workspace file for numeric](  https://github.com/phaustin/numeric/blob/master/utils/numeric.code-workspace) and here is an example
# of a [vscode folder](https://github.com/phaustin/numeric/tree/master/utils/.vscode)
#
# ## Possible workflows
#
# First, install the [python extension](https://marketplace.visualstudio.com/items?itemName=ms-python.python).
#
# Next, as demonstrated in class, if you open a file ending in ".py", and set the python interpeter to the
# conda numeric environment, you can then save workspace called "numeric", add flake8 as your linter,
# and black as your formatter.  At that point you are getting both intellisense command competions and
# linting and formatting.  Another possible route is to install ipython:
#
# ```
# conda install ipython
# ```
#
# and start ipython in a bash terminal with:
#
# ```
# ipython --matplotlib
# ```
#
# so that you can pop up figures that are much larger than the vscode window.
#
# ##  Next steps
#
# 1. Using git with vscode
# 2. Writing markdown with vscode
#

# %%

# %%

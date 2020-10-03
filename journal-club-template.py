"""
This will be an interactive guide through
a) The basics of pandas, so that you can understand our utils script in the rds repo
b) A variety of additional optional content

Preliminaries
1) Make sure you have python, pandas, and ipython installed locally
2) Install the offical Microsoft python extension for vscode
3) (Recommended) make sure you have a version of python registered with vscode
4) make sure you can run test.py from the vscode terminal
5) make sure you can run test.py by hitting the run cell option in the code editor
"""

# %%
# import pandas as pd because we're not heathens
import pandas as pd

#%%
# read in the csv

# %%
# read in the csv with the id data type set


# %%
# manipulating an existing column
# transform last_time_eaten to remove hyphens with map, lambda, join, split

# %%
# but often simple manipulations have better ways
# tranform favorite_food to title case with no hyphens with str.replace and str.title

# %%
# Renaming columns
# set favoriteFood to favorite_food by restating the whole columns list

# %%
# adding a new column with a single default

# %%
# adding a new column with rowwise defaults

# %%
# Dropping and rearranging columns
# set df to only the name, times_eaten, and favorite_food columns in that order

# %%
# A warning on copies
# try to manipulate the name column to all upper case

# %%
# make a copy, df_short with only the desire columns first then do the manipulation

# %%
# writing results to a csv

# %%
# I hate the default index
# write the df_short dataframe to a csv without the index

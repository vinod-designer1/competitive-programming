# copy file from tmp directory to tmp2 directory
#cp tmp/tmp_sub_1.txt tmp2

# copy file of type file_<anything>.c to tmp2 directory
#cp file_* *.c tmp2

# using man command
# to know what ls command do
man ls

# if you don't knoe the command search for keyword using
man -k l # this will list all commands with l

# to know what perticular option in man do
# man <option>
man -k #output:What manual page do you want?

# command apropos which is alias to man -k
#if not available we can add it to .cdhrc file
# alias apropos `man -k \!'
man mkdir
# output:
# MKDIR(1)                  BSD General Commands Manual                 MKDIR(1)
#NAME
#     mkdir -- make directories
# 1st line say's which category it belongs to
# here it is 1
# which unix distrbutin here it is BSD

# To find disk commands
man -k disk

# trim down command to category
man -k disk | grep '(1' # shows 1 an 1m

# whatis command searches for complete words
# example whatis cd
whatis cd

# Making better apropos command
# alias apropos _man -k \!* | uniq_
# to get uniq and user commands
# alias apropos _man -k \!* | uniq | grep 1_

# to get intro for a category 
man 1 intro # to get inroduction for category 1 commands
#remove execute permission
#chmod -x file

# To update command table after new command added
# type rehash in command lin

# Permissions
#--- No access is allowed
#r-- Read-only access
#r-x Read and execute access, for programs and shell scripts
#rw- Read and write access, for files
#rwx All access allowed, for programs

#chmod for group
chmod g+w temp_file.c
#take away permission for everyone not in your group
chmod o-rx temp_file.c
#grant permission to everyone
chod a+r temp_file.c

# permission codes
#--- 000   0
#--x 001   1
#-w- 010   2
#-wx 011   3
#r-- 100   4
#r-x 101   5
#rw- 110   6
#rwx 111   7

# common permission 
#--------- 000 All types
#r-------- 400 Files
#r--r--r-- 444 Files
#rw------- 600 Files
#rw-r--r-- 644 Files
#rw-rw-r-- 664 Files
#rw-rw-rw- 666 Files
#rwx------ 700 Programs and directories
#rwxr-x--- 750 Programs and directories
#rwxr-xr-x 755 Programs and directories

# umask reveals default permission
umask
# umask 007 changes umask value

# chnage own chown command
# change group chgrp command
# rm -i confirm before remove
# rm -r to remove directory
# change shell chsh
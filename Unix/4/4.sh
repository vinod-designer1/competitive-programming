# shows file along with file size
# s = size in blocks
# 1 block = 1024kb 1kb = 1024bytes
ls -s
# can also specify file names we need with space
# ls -s tmp file_tmp.c ...

# list all files comma seperated
ls -m # ls -m -1 shows files in a seperate line

# ls options
#-a List all files, including any dot files.
#-F Indicate file types; / = directory, * = executable.
#-m Show files as a comma-separated list.
#-s Show size of files, in blocks (typically, 1 block = 1,024 bytes).
#-C Force multiple-column output on listings.
#-1 Force single-column output on listings.
#-x sort files
#-t most recently accessed to leat recently accessed
# -r reverses sorting order
#-R recursively show all files even in child directories
#-l to find permisions and sizes of file
#-d List directories rather than their contents.
#-F Indicate file types; / = directory, * = executable.
#-l Generate a long listing of files and directories.
#-m Show files as a comma-separated list.
#-r Reverse the order of any file sorting.
#-R Recursively show directories and their contents.
#-s Show size of files, in blocks (typically 1 block = 1,024 bytes).
#-t Sort output in most-recently-modified order.
#-x Sort output in row-first order.
#-1 Force single-column output on listings.
#-a List all files, including any dot files.
#-C Force multiple-column output on listings.
#-d Directory
#-b Block-type special file
#-c Character-type special file
#-l Symbolic link
#-p Pipe
#-s Socket
#- Regular file

# creating files
touch some_touch_file.c

# cheking disk space
# list file in kilobytes
du

# total size
du -s

# to add additional info
du -a # du and du -s

# cheking disk availability
df

# compress file
#compress filename1 filename2..

#uncompress filename  to uncompress files
# compress -v filename to verbose output
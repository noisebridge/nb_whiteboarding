Given a string that represents a file structure where directory and file 
names are on separate lines and where these names are indented with a tab 
to show which directories they are stored under, return the length of the 
absolute path to a file that has the most characters. 

For example, given `"dir1\n\tsubdir\n\t\tfile1.txt\n\tfile2.txt"`, the 
file structure is:

        dir1
          subdir
            file1.txt
          file2.txt

And the absolute path to a file with the most characters is 
`"dir1/subdir/file1.txt"`.

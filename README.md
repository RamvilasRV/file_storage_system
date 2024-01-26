# A cloud file storage system with cmd tool

A simple site made using Flask, where you can upload your files and then download them when needed.<br>
This also has a command line tool where you can view, upload, download, or remove files through the command line without going on the website.<br>
To get the cmd tool working, just add the fts.bat file [from cmd access] to the environment variables of your device.

### Commands for cmd access
#### USAGE : 
    fts <action> <filepath>
#### ACTIONS:
    disp -- displays the list of the files present in the server<br>
    down -- downloads the file mentioned, takes 1 parameter i.e. filename<br>
    up -- uploads the given file from the file path<br>
    rem -- removes the file from the server<br>

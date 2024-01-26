import fts_actions
import sys

if len(sys.argv)==2:
    action = sys.argv[1]
    filename = ""
elif len(sys.argv)==3:
    action = sys.argv[1]
    filename = sys.argv[2]
else:
    print('''
USAGE : fts <action> <filname>
ACTIONS:
    disp -- displays the list of the files present in the server
    down -- downloads the file mentioned, takes 1 parameter i.e. filename
    up -- uploads the given file from the file path
    rem -- removes teh file from the server
''')
    exit()

if action=="disp":
    fts_actions.disp()
elif action=="down":
    fts_actions.down(filename)
elif action=="up":
    fts_actions.up(filename)
elif action=="rem":
    fts_actions.rem(filename)
else:
    print("INVALID ARGUMENTS")
    print("ARGUMENT LIST : [DISP, DOWN, UP, REM]")

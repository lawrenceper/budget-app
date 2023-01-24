from os import system

"""This Python script makes committing to Git easier providing that you are running it under Unix or unix-like operating systems. It may work under Windows, but I have not tested it yet. Use on Windows at your own risk!

It asks the user to type a git message. If empty, nothing happens and the program exits.

If input is given, the Python script runs 'git add .', then runs git commit with the typed input as the commit message.

Finally, the program runs git push and git pull."""

commit_message = input("Please type a commit message.")
if commit_message == True:
    print("No commit message was given. Abort")
    exit()

system("git add .")
system(f'git commit -m "{commit_message}"')
system("git push")
system("git pull")

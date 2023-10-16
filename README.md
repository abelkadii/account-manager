Account Manager

This is a CLI application to manage your accounts.

to use clone this reposotory on your local envirment and run "python main.py"

-to create a new account run: create -u "username" -p "password" -d "domain" -r "recovery email"

example: "create -u email@google.com -p 12345678 -d google"

if you want to create an account with a random password don't include the -p arg

the -u and -d are the only required arguments

-to show accounts run ls folowed by any filter you wish to apply

example: "ls -d google" will list all your google account

-to update an account run: update -id "account id" folowed by what you with to update

exapmle: update -id U18 -p abcdefghi

-to delete an account run: delete -id



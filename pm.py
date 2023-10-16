from app import App, Command, Arg
from commands import Commands

class Log:
    log=print

pm = App('PasswordManager', provider=input, root="abelkadii@pm$~ ")
pm.setLogger(Log())

pm.register(Command('create', ['create', 'add'], [
    Arg("domain", ["domain", "d"], required=True), 
    Arg("username", ["username", "u"], required=True), 
    Arg("password", ["password", "p"]), 
    Arg("email", ["email", "e"]), 
    Arg("first_name", ["first_name", "f", "fn"]), 
    Arg("last_name", ["last_name", "l", "ln"]), 
    Arg("phone", ["phone", "ph"]), 
    Arg("recovery", ["recovery", "r"])
], Commands.create))

pm.register(Command('ls', ['ls', 'list'], [
    Arg("domain", ["domain", "d"]), 
    Arg("username", ["username", "u"]), 
    Arg("password", ["password", "p"]), 
    Arg("email", ["email", "e"]), 
    Arg("first_name", ["first_name", "f", "fn"]), 
    Arg("last_name", ["last_name", "l", "ln"]), 
    Arg("phone", ["phone", "ph"]), 
    Arg("recovery", ["recovery", "r"])
], Commands.ls))

pm.register(Command('get', ['get'], [Arg("id", ['id', 0], required=True)], Commands.get))
pm.register(Command('delete', ['delete'], [Arg("id", ['id', 0], required=True)], Commands.delete))


pm.register(Command('update', ['update', 'change'], [
    Arg("id", ['id', 0], required=True),
    Arg("domain", ["domain", "d"]), 
    Arg("username", ["username", "u"]), 
    Arg("password", ["password", "p"]), 
    Arg("email", ["email", "e"]), 
    Arg("first_name", ["first_name", "f", "fn"]), 
    Arg("last_name", ["last_name", "l", "ln"]), 
    Arg("phone", ["phone", "ph"]), 
    Arg("recovery", ["recovery", "r"])
], Commands.update))


pm.register(Command('exit', ['exit'], [], Commands.exit))
pm.register(Command('clear', ['clear', 'cls'], [], Commands.clear))
from console import Exit, Error
import logging
from input import InputDecoder

class App:
    def __init__(self, name, logger=None, commands=[], root=None, provider=None):
        self.name = name
        self.commands = commands
        self.logger=logger
        self.root=root
        self.provider=provider
    
    def setLogger(self, logger):
        self.logger = logger
    
    def setProvider(self, logger):
        self.provider = provider

    def register(self, command):
        self.commands.append(command)

    def execute(self, command, args, kwargs):
        if command=='':
            return
        for cmd in self.commands:
            if command in cmd.keywords:
                console=cmd.execute(*args, **kwargs)
                if console:
                    return console.log(self.logger)
                return
        self.logger.log('%s command does not exsiste'%command)
    
    def exit(self):
        exit()

    def main_loop(self):
        while True:
            self.logger.log('')
            try:
                cin = self.provider(self.root)
                command, args, kwargs = InputDecoder.decode(cin)
                self.execute(command, args, kwargs)
            except (KeyboardInterrupt, Exit):
                self.exit()
            except Exception as e:
                raise e

class Command:
    def __init__(self, name, keywords, args,  function):
        self.name = name
        self.keywords = keywords
        self.args = args
        self.function = function
    

    def execute(self, *args, **kwargs):
        for index, arg in enumerate(args):
            kwargs[index]=arg
        args = {}
        for kw in kwargs:
            found=False
            for arg in self.args:
                if kw in arg.keys:
                    key, value = arg.parse(kwargs[kw])
                    args[key]=value
                    found=True
                    break
            if not found:
                logging.warn('command "%s" does not take argument "%s"'%(self.name, kw if isinstance(kw, str) else 'of position %s'%kw))
        for arg in self.args:
            if arg.name not in args and arg.required:
                if arg.default is None:
                    raise Error('%s arg is required'%arg.name)
            if arg.name not in args and arg.default is not None:
                kwargs[arg.name]=arg.default
        return self.function(**args)
    
    
class Arg:
    def __init__(self, name, keys, required=False, decode=None, default=None, minlength=0, maxlength=float('inf')):
        self.name=name
        self.keys=keys
        self.required=required
        self.decode=decode
        self.default = default
        self.minlength = minlength
        self.maxlength = maxlength
    
    def parse(self, arg):
        if not (self.minlength<=len(arg)<=self.maxlength):
            raise Error('%s arg has to be in the range [%s, %s]'%(self.name, self.minlength, self.maxlength))
        if self.decode:
            return self.name, self.decode(arg)
        return self.name, arg
    

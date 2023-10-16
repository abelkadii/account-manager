from accounts import Account
from console import *
import os

class Commands:
    def __init__(self):
        pass

    @classmethod
    def ls(self, **params):
        return Table([e.to_dict() for e in Account.filter(**params)], log_length=True)

    @classmethod
    def create(self, **kwargs):
        account = Account.new(**kwargs)
        return Obj(account.to_dict(), msg='successfully created new account id %s'%account.id)


    @classmethod
    def get(self, id):
        account = Account.get(id)
        if account:
            return Obj(account.to_dict())
        return Warn('no account with id %s'%id)


    @classmethod
    def delete(self, id):
        account = Account.get(id)
        account.delete()
        return Success('successfully deleted account id %s'%id)

    @classmethod
    def update(self, id, **kwargs):
        account = Account.get(id)
        for key, value in kwargs.items():
            if hasattr(account, key):
                setattr(account, key, value)
        account.save()
        return Obj(account.to_dict(), msg='successfully updated account id %s'%id)


    # command line commands
    @classmethod
    def exit(self):
        raise Exit()

    @classmethod
    def clear(self):
        return os.system('cls')
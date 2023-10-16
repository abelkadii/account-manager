from utils import settings,  random_id, random_password
import datetime, json

class Account:
    # def __init__(self, id, domain, username, password, security_questions, email, first_name, last_name, phone, recovery, associated, encryption, created):
    def __init__(self, id, domain, username, password, email, first_name, last_name, phone, recovery, created):
        self.id=id
        self.domain=domain
        self.username=username
        self.password=password
        self.email=email
        self.first_name=first_name
        self.last_name=last_name
        self.phone=phone
        self.recovery=recovery
        self.created=created
        # self.security_questions=security_questions
        # self.associated=associated
        # self.encryption=encryption


    @classmethod
    def new(self, domain=None, username=None, password=None, email=None, first_name=None, last_name=None, phone=None, recovery=None):
        id = self.generate_id()
        password = password or self.generate_random_password()
        created = datetime.datetime.now().ctime()
        associated = {}
        new_item = Account(id, domain, username, password, email, first_name, last_name, phone, recovery, created)
        new_item.save()
        return new_item

    
    def to_dict(self):
        return {
            'id': self.id,
            'domain': self.domain,
            'username': self.username,
            'password': self.password,
            'email': self.email,
            'first_name': self.first_name,
            'last_name': self.last_name,
            'phone': self.phone,
            'recovery': self.recovery,
            'created': self.created
        }
    @classmethod
    def from_dict(self, obj):
        return Account(**obj)


    @classmethod
    def write(self, items):
        return Data.json_write([item.to_dict() for item in items], settings.get('paths').get('data'))

    def save(self):
        all_items = self.all()
        for i, item in enumerate(all_items):
            if item.id == self.id:
                all_items[i]=self
                return self.write(all_items)
        all_items.append(self)
        return self.write(all_items)

    @classmethod
    def generate_id(self):
        all_ids = [e.id for e in self.all()]
        while (rnd:=random_id()) in all_ids:
            continue
        return rnd
    
    @classmethod
    def generate_random_password(self):
        password=random_password(settings.get('gen-password'))
        return password
    
    @classmethod
    def all(self):
        return [self.from_dict(item) for item in Data.json_read(settings.get('paths').get('data'))]
    
    @classmethod
    def get(self, id):
        all_items = self.all()
        for item in all_items:
            if item.id==id:
                return item
        return None
    
    
    def delete(self):
        all_items = self.all()
        for i, item in enumerate(all_items):
            if item.id == self.id:
                all_items.pop(i)
                return self.write(all_items)
        raise Exception('404, no account with id="%s"'%id)

    
    @classmethod
    def filter(self, **kwargs):
        all_items = self.all()
        if not kwargs:
            return all_items
        filtered=[]
        for item in all_items:
            if any([item.__getattribute__(key)!=kwargs[key] for key in kwargs]):
                continue
            filtered.append(item)
        return filtered
    

        
class Data:
    def __init__(self):
        pass
    
    @classmethod
    def json_read(self, path):
        return json.load(open(path, 'r'))

    @classmethod
    def json_write(self, data, path):
        return json.dump(data, open(path, 'w'), indent=4)

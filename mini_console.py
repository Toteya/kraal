#!/usr/bin/python3
"""
test objects
"""
import json
from models import storage
from models.base_model import BaseModel
from models.category import Category
from models.location import Location
from models.offer import Offer
from models.order import Order
from models.product import Product
from models.request import Request
from models.user import User
from sys import argv

classes = {
    'BaseModel': BaseModel,
    'Category': Category,
    'Location': Location,
    'Offer': Offer,
    'Order': Order,
    'Product': Product,
    'Request': Request,
    'User': User
}

commands = ['all', 'get', 'delete', 'create']

def all(cls=None):
    """
    Return all object of the specified class.
    If no class is specified, return all objects
    """
    objs = []
    if cls and cls not in classes:
        print('*** Class does not exist ***')
        return
    if cls:
        objs = storage.all(classes[cls]).values()
    else:
        objs = storage.all().values()
    objs_list = []
    for obj in objs:
        objs_list.append(obj.to_dict())
    print(json.dumps(objs_list, indent=4))
    


def get(cls=None, id=None):
    """
    Return an object based on the given class and id
    """
    if not cls:
        print('*** class missing ***')
        return
    if cls not in classes:
        print('*** class does not exist ***')
        return
    if not id:
        print('*** id missing ***')
        return
    obj = storage.get(classes[cls], id)
    if not obj:
        print('*** object not found ***')
        return
    print(json.dumps(obj.to_dict(), indent=4))

def delete(cls=None, id=None):
    """
    Delete an object based on the given class and id
    """
    if not cls:
        print('*** class missing ***')
        return
    if cls not in classes:
        print('*** class does not exist ***')
        return
    if not id:
        print('*** id missing ***')
        return
    obj = storage.get(classes[cls], id)
    if not obj:
        print('*** object not found ***')
        return
    obj.delete()
    storage.save()
    print('object deleted')

def create(cls, *args, **kwargs):
    """
    Create an object of the given class
    """
    if not cls:
        print('*** class missing ***')
        return
    if cls not in classes:
        print('*** class does not exist ***')
        return
    obj = classes[cls](**kwargs)
    storage.new(obj)
    storage.save()
    print('object created\n{}'.format(obj.id))

if __name__ == '__main__':
    if len(argv) < 2:
        print("Usage: mini_console command [CLASS] [ID]")
    cmd = argv[1]
    if cmd not in commands:
        print('*** unknown command ***')
    try:
        cls = argv[2]
    except:
        cls = None
    try:
        id = argv[3]
    except:
        id = None
    
    if cmd == 'all':
        all(cls)
    elif cmd == 'get':
        get(cls, id)
    elif cmd == 'delete':
        delete(cls, id)
    elif cmd == 'create':
        # print(type(argv[2:len(argv)]))
        obj_dict = {}
        for arg in argv[2:len(argv)]:
            try:
                key = arg.split('=')[0]
                value = arg.split('=')[1]
                obj_dict[key] = value
            except:
                pass
        create(cls, **obj_dict)
    






import unittest
import requests
from users import *
from api import *

class TestStringMethods(unittest.TestCase):
    
    API_URL = "http://127.0.0.1:1234"
    USERS_URL = "{}/users".format(API_URL)
    USER_OBJID = [{
        'name': 'test', 
        'id': 3,
        'age': 20, 
        'sexe': 'M'
    }]
    NEW_USER = {
            'name': 'test', 
            'age': 20, 
            'sexe': 'M'
        }
    

    def test_getAll_user(self):
        r = requests.get(TestStringMethods.USERS_URL)
        self.getUserAll = User.get_all_users()
        self.assertEqual(r.status_code, 200)
        self.assertNotEqual(self.getUserAll, [])


    def test_getId_user(self):
        id = 1
        userId = [{
            "age": 23,
            "id": 1,
            "name": "Melly",
            "sexe": "F"
        }]
        r = requests.get("{}/{}".format(TestStringMethods.USERS_URL, id))
        self.assertEqual(r.status_code, 200)
        self.assertEqual(r.json(), userId)


    def test_add_user(self):
        id = 3
        userId = [{
            'id': 3,
            'name': 'test', 
            'age': 20, 
            'sexe': 'M'
        }]

        #add user
        r = requests.post(TestStringMethods.USERS_URL, json=(TestStringMethods.NEW_USER))
        self.assertEqual(r.status_code, 201)

        #getId user
        r = requests.get("{}/{}".format(TestStringMethods.USERS_URL, id))
        self.assertEqual(r.status_code, 200)
        self.assertEqual(r.json(), userId)

        #delete user
        r = requests.delete("{}/{}".format(TestStringMethods.USERS_URL, id))


    def test_put_user(self):
        id = 3
        userPut = {
            'name': 'test',
            'age': 25, 
            'sexe': 'M'
        }
        userPutId = [{
            'name': 'test', 
            'id': 3,
            'age': 25, 
            'sexe': 'M'
        }]

        #add user
        r = requests.post(TestStringMethods.USERS_URL, json=(TestStringMethods.NEW_USER))

        #put user
        r = requests.put("{}/{}".format(TestStringMethods.USERS_URL, id), json=userPut)
        self.assertEqual(r.status_code, 200)

        #getId user
        id = 3
        r = requests.get("{}/{}".format(TestStringMethods.USERS_URL, id))
        self.assertEqual(r.status_code, 200)
        self.assertEqual(r.json(), userPutId)

        #delete user
        r = requests.delete("{}/{}".format(TestStringMethods.USERS_URL, id))


    def test_delete_user(self):
        id = 3
        
        #add user
        r = requests.post(TestStringMethods.USERS_URL, json=(TestStringMethods.NEW_USER))

        #delete user
        r = requests.delete("{}/{}".format(TestStringMethods.USERS_URL, id))
        self.assertEqual(r.status_code, 200)

        #get user
        r = requests.get("{}/{}".format(TestStringMethods.USERS_URL, id))
        self.assertEqual(r.status_code, 500)


if __name__ == "__main__":
    unittest.main()

   
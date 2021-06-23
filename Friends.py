from os import path
import argparse
import json
import logging

MAX_NAME_LENGTH = 30
MAX_PHONE_LENGTH = 15
ILLEGAL_NAME = 1
ILLEGAL_PHONE = 2
ALREADY_EXIST = 3

def logger(func):
    logging.basicConfig(filename='friends.log', level=logging.INFO)
    def wrapper(*args, **kwargs):
        logging.info('{} with args: {} and kwargs: {}'.format(func.__name__, args, kwargs))
        return func(*args, **kwargs)

    return wrapper

class Friend:
    """
    A class representing friends
    A friend has a name, lastname and optionally phone
    All the friends are persisted in a file, in json format:
    {"1": ["John", "Doe", "555-123"], "2": ["Jane", "Doe", "555-234"], "3": ["Mary", "Jane", "23456"]}
    The dictionary key is generated automatically incrementing the last key (From Python 3.7 dictionaries are ordered)
    Same friend can be saved multiple times if phone is different
    """
    @logger
    def __init__(self, datafile=None):
        """
        A dict with friends is initialized from a specified file
        If the file is not specified, a default file is loaded
        :param datafile:
        """
        self.friends = {}
        if datafile is None:
            self.datafile = 'MyFriends.db'
        else:
            self.datafile = datafile
        if path.exists(self.datafile):
            with open(self.datafile, 'r') as f:
                data = json.load(f)
                for key, value in data.items():
                    self.friends[key] = value

    @staticmethod
    def validate_name(name):
        """
        validate a name with respect to length and characters
        :param name:
        :return: Boolean
        """
        new_name = name.replace("'", '', 1).replace('-', '', 2) # accept names like O'Tool or Maria-Magdalena
        return True if new_name.isalpha() and 1 <= len(new_name) <= MAX_NAME_LENGTH else False

    @staticmethod
    def validate_phone(phone):
        """
        validate a phone with respect to length and characters
        :param phone:
        :return: Boolean
        """
        new_phone = phone.replace('-', '', 5).replace('.', '', 5) # accept formatted strings like 555-123 or 555.123
        return True if new_phone is None or (new_phone.isnumeric() and len(new_phone) <= MAX_PHONE_LENGTH) else False

    @logger
    def next_id(self):
        """
        generate next key in friends dictionary
        :return: integer
        """
        return int(list(self.friends.keys())[-1]) + 1 if len(self.friends) != 0 else 1

    @logger
    def add_friend(self, name, lastname, phone):
        """
        try to add a friend to dictionary
        :param name:
        :param lastname:
        :param phone:
        :return:
        """
        success = 0
        if not self.validate_name(name):
            print(name, " is too long or contains unaccepted characters")
            success = ILLEGAL_NAME
        if not self.validate_name(lastname):
            print(lastname, " is too long or contains unaccepted characters")
            success = ILLEGAL_NAME
        if not self.validate_phone(phone):
            print(lastname, " is too long or contains unaccepted characters")
            success = ILLEGAL_PHONE
        if not self.check_existing(name, lastname, phone):
            self.friends[self.next_id()] = [name, lastname, phone]
        else:
            print("record already exist")
            success = ALREADY_EXIST
        if success == 0:
            self.save_data()


    @logger
    def list_friends(self):
        """
        list all friends
        :return:
        """
        for key, value in self.friends.items():
            print(key, value)

    @logger
    def delete_friend(self, id):
        """
        delete friend with key=id
        :param id:
        :return:
        """
        self.friends.pop(id, None)

    @logger
    def check_existing(self, name, lastname, phone):
        """
        check for duplicate record
        :param name:
        :param lastname:
        :param phone:
        :return: Boolean
        """
        record_exist = False
        for key, value in self.friends.items():
            if value[0] == name and value[1] == lastname and value[2] == phone:
                record_exist = True
                break

        return record_exist

    @logger
    def save_data(self):
        """
        save dictionary to file
        :return:
        """
        with open(self.datafile, 'w') as f:
            json.dump(self.friends, f)


def main():
    parser = argparse.ArgumentParser(description='User option1')
    parser.add_argument('Option',
                        metavar=['1', '2', '3'],
                        type=str,
                        help='list friends')
    parser.add_argument('-File',
                        type=str,
                        help='friends file')
    parser.add_argument('-Name',
                        type=str,
                        help='friend name')
    parser.add_argument('-Last',
                        type=str,
                        help='friend last name')
    parser.add_argument('-Phone',
                        type=str,
                        help='friend phone')
    parser.add_argument('-Id',
                        type=str,
                        help='friend id')

    args = parser.parse_args()
    print(args)
    if args.Option == "1":
        f = Friend(args.File)
        f.list_friends()

    if args.Option == "2":
        f = Friend(args.File)
        f.add_friend(args.Name, args.Last, args.Phone)
        f.list_friends()

    if args.Option == "3":
        f = Friend(args.File)
        f.delete_friend(args.Id)
        f.list_friends()

if __name__ == '__main__':
    main()






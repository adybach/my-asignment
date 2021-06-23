import pytest
import os
from os import path
from Friends import Friend


def test_empty_friends_file():
    f = Friend()
    assert f.datafile == 'MyFriends.db'


def test_friends_file():
    f = Friend(datafile='Friends.db')
    assert f.datafile == 'Friends.db'


def test_add_friend(name='John', lastname='Doe', phone='555.123'):
    f = Friend()
    new_id = f.next_id()
    f.add_friend(name, lastname, phone)
    assert f.friends[new_id][0] == 'John'


def test_add_illegal_name(name='Jo1hn', lastname='Doe', phone='555-123'):
    f = Friend()
    new_id = f.next_id()
    f.add_friend(name, lastname, phone)
    assert str(new_id) not in f.friends.keys()


def test_save_file():
    if path.exists("MyFriends.db"):
        os.remove("MyFriends.db")
    assert path.exists("MyFriends.db") is False
    f = Friend()
    f.save_data()
    assert path.exists("MyFriends.db") is True





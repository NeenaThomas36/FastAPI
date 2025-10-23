import pytest # type: ignore



def test_equal_or_not_equal():
    assert 1==1
    assert 3!=1

def test_is_instance():
    assert isinstance('string',str)
    assert not isinstance('10',int)


def test_boolean():
    validated = True
    assert validated is True
    assert ('hello'=='world') is False


def test_type():
    assert type('Hello' is str)
    assert type('world' is not int)


def test_greater_or_less():
    assert 3>2
    assert 4<5


def test_list():
    num_list =[1,2,3,4,5]
    any_list =[False,False]
    assert 4 in num_list
    assert 8 not in num_list
    assert not any(any_list)


class Student:
    def __init__(self,first_name:str,last_name:str,major:str,years:int):
        self.first_name = first_name
        self.last_name = last_name
        self.major = major
        self.years = years



@pytest.fixture
def default_employee():
    return Student('John','Doe','Math',3)

def test_person_initialization(default_employee):
    p = default_employee
    assert p.first_name=='John'
    assert p.last_name=='Doe'
    assert p.major=='Math'
    assert p.years==3
import sys
sys.path.insert(0, '..')

from src.user import User

def test_sanity():
    test_user = User("test", "1234", "Nithin", "Joseph")
    assert test_user.get_fname() == "Nithin"
    assert test_user.get_lname() == "Joseph"
    assert test_user.get_uname() == "test"
    assert test_user.get_password() == "1234"
import unittest
from unittest import mock, TestCase
from app import app


# mock the call to the function
@mock.patch('app.app.was_i_called', return_value=True)
class TestApp(TestCase):
    def test_mocking(self, mock_was_i_called):
        self.assertTrue(app.was_i_called(15), 'function was not called in time')


if __name__ == '__main__':
    unittest.main()

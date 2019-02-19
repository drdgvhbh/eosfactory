import unittest

from eosfactory.core.errors import validate, EOSIOAssertionError


class ErrorsTest(unittest.TestCase):
    def test_validate_assertion_error(self):
        with self.assertRaises(EOSIOAssertionError):
            class TestError:
                def __init__(self):
                    self.err_msg = """ERROR:
Error 3050003: eosio_assert_message assertion failure
Error Details:
assertion failure with message: the question Where is the question? cannot be found
pending console output:"""
            validate(TestError())


if __name__ == "__main__":
    unittest.main()

"""
Module to define default class behaviors that are not default in Python
but necessary to handle object patterns defined in the package

:author: Julian M. Kleber
"""

from abc import ABC

from typing import Any


class BaseInterface(ABC):
    """
    Base Interface used by all class objects throughout the package#

    :doc-author: Julian M. Kleber
    """

    def test(self) -> bool:
        """
        The return_true function returns True.

        :param self: Used to Refer to the current instance of a class.
        :return: True.

        :doc-author: Trelent
        """

        raise NotImplementedError()  # pragma: no cover

    def get_method(self, method_name: str) -> Any:
        """
        The get_method function is a helper function that returns the method object
            for the given method name. This is useful when you want to call a method
            dynamically, but don't know what it's called. For example:

                def do_something(self):
                    # ...
                    self.get_method('do_something')()  # calls itself!

                def do_otherthing(self):
                    # ...
                    self.get_method('do_something')()  # calls 'do something'!

            Note that this function will raise an AttributeError if there is no such
            attribute on this class (i.e., if there is no such method). If you want to
            be able to check whether or not a particular attribute exists, use hasattr instead.

        :param method_name:str: Used to get the method name and return it as a string.
        :return: The method object from the class.

        :doc-author: Julian M. Kleber
        """

        return getattr(self, method_name)


class TestInterface(BaseInterface):
    """
    Interface for testing the base-interface in
    the tests/

    :doc-author: Julian M. Kleber
    """

    def test(self) -> bool:
        """
        The test function is used to test the functionality of the class.
            It is not required for grading, but it is highly recommended.

        :param self: Used to Represent the instance of the class.
        :return: True.

        :doc-author: Trelent
        """

        return True

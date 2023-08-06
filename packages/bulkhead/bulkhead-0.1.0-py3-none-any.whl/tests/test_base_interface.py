from bulkhead.base_interface import TestInterface


def test_base_interface():

    method_name = "test"
    interf = TestInterface()
    method = interf.get_method(method_name=method_name)
    assert method()

import pygroupexc


def a():
    b()


def b():
    raise ValueError()


def test_format():
    try:
        a()
    except Exception:
        assert pygroupexc.format_exception() == [
            ('/home/frantisek/playground/pygroupexc/pygroupexc_test.py', 'test_format'),
            ('/home/frantisek/playground/pygroupexc/pygroupexc_test.py', 'a'),
            ('/home/frantisek/playground/pygroupexc/pygroupexc_test.py', 'b'),
            'ValueError'
        ]
        assert pygroupexc.exception_id() == 'ac00f63bd63c8b05be6d967ac79378f9'


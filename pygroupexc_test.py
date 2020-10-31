import os
import pygroupexc


def a():
    b()


def b():
    raise ValueError()


def recursive(n):
    if n <= 0:
        raise ValueError()
    recursive(n-1)


def test_format():
    try:
        a()
    except Exception:
        assert pygroupexc.format_exception() == [
            (__file__, 'test_format'),
            (__file__, 'a'),
            (__file__, 'b'),
            'ValueError'
        ]
        assert pygroupexc.exception_id() == 'ac00f63bd63c8b05be6d967ac79378f9'


def test_format_with_root():
    dirname, base = os.path.split(__file__)
    try:
        a()
    except Exception:
        assert pygroupexc.format_exception(root=dirname) == [
            (base, 'test_format_with_root'),
            (base, 'a'),
            (base, 'b'),
            'ValueError'
        ]


def test_format_recursive():
    try:
        recursive(5)
    except Exception:
        assert pygroupexc.format_exception() == [
            (__file__, 'test_format_recursive'),
            (__file__, 'recursive'),
            'ValueError'
        ]


def test_format_attribute_error():
    try:
        5 .missing_attribute
    except Exception:
        assert pygroupexc.format_exception() == [
            (__file__, 'test_format_attribute_error'),
            'AttributeError', 'int', 'missing_attribute'
        ]

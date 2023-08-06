import sys
from textwrap import dedent

from datadiff import tools
from datadiff.tests.test_datadiff import assert_equal

from nose.tools import assert_raises


def test_assert_equal_true():
    # nothing raised
    assert_equal(None, tools.assert_equals(7, 7))


def test_assert_equal_false():
    with assert_raises(AssertionError) as raised:
        tools.assert_equals([3, 4], [5, 6])
    assert_equal(str(raised.exception), dedent('''\
        
        --- a
        +++ b
        [
        @@ -0,1 +0,1 @@
        -3,
        -4,
        +5,
        +6,
        ]'''))


def test_assert_equal_msg():
    with assert_raises(AssertionError) as raised:
        tools.assert_equals(3, 4, "whoops")
    assert_equal(str(raised.exception), "whoops")


def test_assert_equals():
    assert_equal(tools.assert_equal, tools.assert_equals)


def test_assert_equal_simple():
    with assert_raises(AssertionError) as raised:
        tools.assert_equals(True, False)
    assert_equal(str(raised.exception), 'True != False')


def test_assert_equal_simple_types():
    with assert_raises(AssertionError) as raised:
        tools.assert_equals('a', 7)
    assert_equal(str(raised.exception), dedent("'a' != 7"))


def test_assert_almost_equal():
    tools.assertAlmostEqual([1.0], [1.0])
    tools.assertAlmostEqual([1.0], [1.000000001])
    tools.assertAlmostEqual([1.0], [1.00001], places=4)
    tools.assertAlmostEqual({"k": 1.0}, {"k": 1.00001}, places=4)
    tools.assertAlmostEqual({1.0}, {1.00001}, places=4)


def test_assert_not_almost_equal():
    assert_raises(AssertionError, tools.assertAlmostEqual, [1.0], [1.00001])
    assert_raises(AssertionError, tools.assertAlmostEqual, [1.0], [1.0001], places=4)
    assert_raises(AssertionError, tools.assertAlmostEqual, {"k": 1.0}, {"k": 1.1}, places=4)
    assert_raises(AssertionError, tools.assertAlmostEqual, {1.0}, {1.1}, places=4)

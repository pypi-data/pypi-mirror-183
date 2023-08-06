from hamcrest import assert_that, is_

from nolog.tests.conftest import Truthy, Falsy


def test_truthy_predicate():
    a = Truthy()
    assert_that(a.eval(), is_(True))


def test_falsy_predicate():
    a = Falsy()
    assert_that(a.eval(), is_(False))

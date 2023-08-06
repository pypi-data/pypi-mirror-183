from hamcrest import assert_that, is_

from nolog.logic_engine.negation import Not
from nolog.tests.conftest import Truthy, Falsy


def test_negation_of_truthy_is_falsy():
    prop = Not(Truthy())
    assert_that(prop.eval(), is_(False))


def test_negation_of_falsy_is_truthy():
    prop = Not(Falsy())
    assert_that(prop.eval(), is_(True))

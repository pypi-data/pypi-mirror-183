from hamcrest import assert_that, is_

from nolog.logic_engine.conjunction import And
from nolog.logic_engine.disjunction import Or
from nolog.logic_engine.negation import Not
from nolog.tests.conftest import Truthy, Falsy


def test_simple_conjunction():
    prop = And(Truthy(), Truthy())

    assert_that(prop.eval(), is_(True))


def test_failing_conjunction():
    prop = And(Truthy(), Falsy())

    assert_that(prop.eval(), is_(False))


def test_conjunction_with_negation():
    prop = And(Truthy(), Not(Falsy()))
    assert_that(prop.eval(), is_(True))


def test_conjunction_with_negation_unordered():
    prop = And(Not(Falsy()), Truthy())
    assert_that(prop.eval(), is_(True))


def test_conjunction_of_disjunctions():
    prop = And(Truthy(), Or(Truthy(), Falsy()))
    assert_that(prop.eval(), is_(True))


def test_conjunction_of_disjunctions_with_negation():
    prop = And(Truthy(), Or(Not(Truthy()), Falsy()))
    assert_that(prop.eval(), is_(False))


def test_conjunction_of_disjunctions_with_more_predicates():
    prop = And(Not(Falsy()), Truthy(), Or(Truthy(), Falsy()))
    assert_that(prop.eval(), is_(True))


def test_conjunction_of_disjunctions_with_more_predicates_and_negation():
    prop = And(Not(Falsy()), Truthy(), Or(Not(Truthy()), Falsy()))
    assert_that(prop.eval(), is_(False))

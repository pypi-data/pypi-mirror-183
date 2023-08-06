from hamcrest import assert_that, is_

from nolog.logic_engine.conjunction import And
from nolog.logic_engine.disjunction import Or
from nolog.logic_engine.negation import Not
from nolog.tests.conftest import Truthy, Falsy


def test_simple_disjunction():
    prop = Or(Truthy(), Truthy())

    assert_that(prop.eval(), is_(True))


def test_partial_disjunction():
    prop = Or(Truthy(), Falsy())

    assert_that(prop.eval(), is_(True))


def test_disjunction_with_negative():
    prop = Or(Falsy(), Falsy())

    assert_that(prop.eval(), is_(False))


def test_disjunction_with_negation():
    prop = Or(Falsy(), Not(Falsy()))
    assert_that(prop.eval(), is_(True))


def test_disjunction_with_negation_unordered():
    prop = Or(Not(Falsy()), Truthy())
    assert_that(prop.eval(), is_(True))


def test_disjunction_of_disjunctions():
    prop = Or(Truthy(), Or(Truthy(), Falsy()))
    assert_that(prop.eval(), is_(True))


def test_disjunction_of_disjunctions_with_negation():
    prop = Or(Truthy(), Or(Not(Truthy()), Falsy()))
    assert_that(prop.eval(), is_(True))


def test_disjunction_of_disjunctions_with_more_predicates():
    prop = Or(Not(Falsy()), Truthy(), Or(Truthy(), Falsy()))
    assert_that(prop.eval(), is_(True))


def test_disjunction_of_disjunctions_with_more_predicates_and_negation():
    prop = Or(Not(Falsy()), Truthy(), Or(Not(Truthy()), Falsy()))
    assert_that(prop.eval(), is_(True))


def test_disjunction_of_conjunctions():
    prop = Or(And(Truthy(), Not(Falsy())), Falsy())
    assert_that(prop.eval(), is_(True))


def test_disjunction_of_failing_conjunctions():
    prop = Or(And(Truthy(), Falsy()), Falsy())
    assert_that(prop.eval(), is_(False))


def test_disjunction_of_conjunctions_with_truthy_value():
    prop = Or(And(Truthy(), Falsy()), Truthy())
    assert_that(prop.eval(), is_(True))

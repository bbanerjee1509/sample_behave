# file:features/steps/steps_country.py
# ----------------------------------------------------------------------------
# STEPS:
# ----------------------------------------------------------------------------
from behave import *
from hamcrest import assert_that, equal_to, contains_string
from lib.movie import Movie


@given('I want to search movie name "{movie_name}"')
def step_set_movie_name(context, movie_name):
    context.movie = Movie()
    context.movie.set_movie(movie_name)

@when('I send the search request')
def step_when_request_sent(context):
    context.movie.send_api()

@then('response should return integer "{parameter_integer}" : "{parameter_movie}"')
def step_should_return_integer(context, parameter_integer, parameter_movie):
    assert_that(context.movie.response_json_map[parameter_integer], equal_to(int(parameter_movie)))

@then('response should contain "{parameter_string}" in "{parameter_field}"')
def step_should_contain(context, parameter_string, parameter_field):
    assert_that(context.movie.response_json_map[parameter_field], contains_string(parameter_string))

from behave import then, when
from behave.runner import Context
from hamcrest import assert_that, equal_to


@when("the string '{}' is encoded")
def the_string_is_encoded(context: Context, plain_text: str):
    """
    Args:
        context: The feature context.
        plain_text: The text to encode.
    """
    context.plain_text = plain_text
    context.cypher_text = context.mark.encode(plain_text)


@then("the string '{}' is returned.")
def the_string_is_returned(context, cypher_text):
    """
    Args:
        context: The feature context.
        cypher_text: The encoded text.
    """
    assert_that(context.cypher_text, equal_to(cypher_text))

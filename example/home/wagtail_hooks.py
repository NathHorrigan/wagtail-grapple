from wagtail.core import hooks
from .mutations import Mutations
from .subscriptions import Subscription


@hooks.register("register_schema_mutation")
def register_author_mutation(mutation_mixins):
    mutation_mixins.append(Mutations)


@hooks.register("register_schema_subscription")
def register_example_subscription(subscription_mixins):
    subscription_mixins.append(Subscription)

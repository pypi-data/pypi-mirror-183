from __future__ import annotations

import factory.fuzzy
from django.contrib.auth import get_user_model

from ob_dj_survey.core.survey.models import (
    Answer,
    Choice,
    Question,
    Response,
    Section,
    Survey,
    SurveyQuestionMembership,
)


class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = get_user_model()


class SectionFactory(factory.django.DjangoModelFactory):
    name = factory.Faker("name")
    description = factory.Faker("text")
    meta = factory.Faker("json")

    class Meta:
        model = Section

    def __new__(cls, *args, **kwargs) -> SectionFactory.Meta.model:
        return super().__new__(*args, **kwargs)


class SurveyFactory(factory.django.DjangoModelFactory):
    name = factory.Faker("name")
    callback = factory.Faker("url")
    meta = factory.Faker("json")
    is_active = True

    class Meta:
        model = Survey

    def __new__(cls, *args, **kwargs) -> SurveyFactory.Meta.model:
        return super().__new__(*args, **kwargs)


class QuestionFactory(factory.django.DjangoModelFactory):
    title = factory.Faker("name")
    section = factory.SubFactory(SectionFactory)
    type = factory.fuzzy.FuzzyChoice(choices=Question.QuestionTypes.values)
    meta = factory.Faker("json")

    class Meta:
        model = Question

    def __new__(cls, *args, **kwargs) -> QuestionFactory.Meta.model:
        return super().__new__(*args, **kwargs)


class SurveyQuestionMembershipFactory(factory.django.DjangoModelFactory):
    question = factory.SubFactory(QuestionFactory)
    survey = factory.SubFactory(SurveyFactory)

    class Meta:
        model = SurveyQuestionMembership

    def __new__(cls, *args, **kwargs) -> SurveyQuestionMembershipFactory.Meta.model:
        return super().__new__(*args, **kwargs)


class ChoiceFactory(factory.django.DjangoModelFactory):
    title = factory.Faker("name")
    description = factory.Faker("text")
    meta = factory.Faker("json")

    class Meta:
        model = Choice

    def __new__(cls, *args, **kwargs) -> ChoiceFactory.Meta.model:
        return super().__new__(*args, **kwargs)


class AnswerFactory(factory.django.DjangoModelFactory):
    survey = factory.SubFactory(
        SurveyFactory,
        questions=factory.RelatedFactoryList(QuestionFactory, size=3),
    )
    created_by = factory.SubFactory(UserFactory)
    status = factory.fuzzy.FuzzyChoice(choices=Answer.Status.values)
    meta = factory.Faker("json")

    class Meta:
        model = Answer

    def __new__(cls, *args, **kwargs) -> AnswerFactory.Meta.model:
        return super().__new__(*args, **kwargs)


class ResponseFactory(factory.django.DjangoModelFactory):
    question = factory.SubFactory(QuestionFactory)
    choice = factory.SubFactory(ChoiceFactory)
    answer = factory.SubFactory(AnswerFactory)
    meta = factory.Faker("json")

    class Meta:
        model = Response

    def __new__(cls, *args, **kwargs) -> ResponseFactory.Meta.model:
        return super().__new__(*args, **kwargs)

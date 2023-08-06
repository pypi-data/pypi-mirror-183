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

    class Meta:
        model = Section

    def __new__(cls, *args, **kwargs) -> SectionFactory.Meta.model:
        return super().__new__(*args, **kwargs)


class SurveyFactory(factory.django.DjangoModelFactory):
    name = factory.Faker("name")
    callback = factory.Faker("url")
    is_active = True

    class Meta:
        model = Survey

    def __new__(cls, *args, **kwargs) -> SurveyFactory.Meta.model:
        return super().__new__(*args, **kwargs)


class QuestionFactory(factory.django.DjangoModelFactory):
    title = factory.Faker("name")
    section = factory.SubFactory(SectionFactory)
    type = Question.QuestionTypes.RADIO

    class Meta:
        model = Question

    def __new__(cls, *args, **kwargs) -> QuestionFactory.Meta.model:
        return super().__new__(*args, **kwargs)

    @classmethod
    def _create(cls, model_class, *args, **kwargs):
        instance = model_class(*args, **kwargs)
        instance.save()
        if instance.type in [
            Question.QuestionTypes.RADIO,
            Question.QuestionTypes.SELECT,
            Question.QuestionTypes.SELECT_MULTIPLE,
        ]:
            instance.choices.add(*ChoiceFactory.create_batch(4))
        return instance


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
    status = Answer.Status.COMPLETED

    class Meta:
        model = Answer

    def __new__(cls, *args, **kwargs) -> AnswerFactory.Meta.model:
        return super().__new__(*args, **kwargs)

    @classmethod
    def _create(cls, model_class, *args, **kwargs):
        instance = model_class(*args, **kwargs)
        instance.save()

        if kwargs.get("status") == Answer.Status.COMPLETED:
            for question in instance.survey.questions.all():
                response_kwargs = {"choice": None}

                if question.type in [
                    question.QuestionTypes.RADIO,
                    question.QuestionTypes.SELECT,
                    question.QuestionTypes.SELECT_MULTIPLE,
                ]:
                    # get random choice
                    choice = question.choices.all().order_by("?").first()
                    response_kwargs.update(choice=choice)

                elif question.type == question.QuestionTypes.DATE:
                    response_kwargs.update(value="2022-10-01")

                elif question.type == question.QuestionTypes.COUNTRY:
                    response_kwargs.update(value="CA")

                else:
                    response_kwargs.update(value="text")

                ResponseFactory(question=question, **response_kwargs, answer=instance)

            instance.status = instance.Status.COMPLETED
            instance.save()
        return instance


class ResponseFactory(factory.django.DjangoModelFactory):
    question = factory.SubFactory(QuestionFactory)
    choice = factory.SubFactory(ChoiceFactory)
    answer = factory.SubFactory(AnswerFactory)

    class Meta:
        model = Response

    def __new__(cls, *args, **kwargs) -> ResponseFactory.Meta.model:
        return super().__new__(*args, **kwargs)

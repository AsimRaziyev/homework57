from django.core.exceptions import ValidationError
from django.shortcuts import redirect


def validate_summary(value):
    if len(value) > 7:
        raise ValidationError("Название должно быть короче 7 символов")
    return value


def validate_author(value):
    if len(value) > 50:
        raise ValidationError("Имя должен содержать до 50 символов")
    return value


def validate_description(value):
    if len(value) > 3000:
        raise ValidationError("Текст должен содержать до 3000 символов")
    return value

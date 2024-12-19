from django.core.validators import MaxValueValidator

class RatingValidator(MaxValueValidator):
    def __init__(self, limit_value, message = ...):
        self.limit_value = limit_value

    
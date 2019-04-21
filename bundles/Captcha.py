from random import randrange


class Captcha():
    QUESTION = 0
    RESULT = 1

    checks = [
        ('1 + 2', 3),
        ('2 + 2', 4),
        ('3 + 2', 5),
        ('4 + 2', 6),
        ('4 + 3', 7),
        ('4 + 4', 8),
        ('3 + 6', 9),
        ('5 + 5', 10),
        ('3 + 8', 11),
        ('2 + 10', 12),
        ('5 + 8', 13),
        ('7 + 7', 14),
    ]

    def get_captcha(self):
        return Captcha.checks[randrange(len(Captcha.checks))]

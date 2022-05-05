from django.db import models


class Poduct(models.Model):
    class Set(models.TextChoices):
        BUY = 'b', 'Куплю',
        SELL = 's', 'Продам',
        __empty__ = 'Выберите че-то'

    class Num(models.IntegerChoices):
        NBUY = 1, 'Не Куплю',
        NSELL = 2, 'Не Продам',
        __empty__ = 'Выберите че-то'

    ACTIVE = (

        ('Нету', (
            ('z', 'Зашел'),
            ('v', 'Вышел'),
        )),
        ('Есть', (

            ('u', 'Ушел'),
        ))
    )

    name = models.CharField(max_length=100, verbose_name='Название', help_text='Введи название', unique=True)
    discription = models.TextField(max_length=100, default='Какая-то фигня')
    mail = models.EmailField(help_text='Введи mail', null=True)
    url = models.URLField(help_text='Введи URL', null=True)
    online = models.BooleanField(default=True)
    age = models.IntegerField(null=True)
    visit = models.DateField(auto_now=True)
    activity = models.CharField(max_length=1, choices=ACTIVE, default='u')
    reason = models.CharField(max_length=1, choices=Set.choices, default=Set.SELL)
    not_reason = models.SmallIntegerField(choices=Num.choices, default=Num.NSELL)



class Profession(models.Model):
    class Prof(models.IntegerChoices):
        E = 1, 'Электрик',
        S = 2, 'Сварщик',
        K = 3, 'Конструктор',
        P = 4, 'Пилот',
        PR = 5, 'Проект менеджер',
        ST = 6, 'Строитель',

    human = models.ForeignKey(Poduct, on_delete=models.PROTECT, max_length=100, unique=True)
    profession = models.IntegerField(choices=Prof.choices, default=Prof.E, help_text='Выберите профессию')













# Create your models here.

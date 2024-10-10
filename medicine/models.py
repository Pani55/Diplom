from django.core.validators import MinValueValidator
from django.db import models


class Procedures(models.Model):
    title = models.CharField(
        max_length=100,
        verbose_name="Название процедуры",
        help_text="Введите название процедуры",
        unique=True,
    )
    description = models.TextField(
        verbose_name="Описание процедуры",
        help_text="Введите описание процедуры",
        blank=True,
        null=True,
    )
    price = models.IntegerField(
        verbose_name="Цена процедуры",
        default=100,
        validators=[MinValueValidator(100)],  # Значение не может быть меньше 100
        help_text="Введите цену процедуры",
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Процедура"
        verbose_name_plural = "Процедуры"


class Doctors(models.Model):
    first_name = models.CharField(
        max_length=50,
        verbose_name="Имя",
        help_text="Введите имя доктора",
    )
    last_name = models.CharField(
        max_length=50,
        verbose_name="Фамилия",
        help_text="Введите фамилию доктора",
    )
    photo = models.ImageField(
        verbose_name="Фотография",
        help_text="Загрузите фотографию доктора",
        upload_to="doctor_photos",
        blank=True,
        null=True,
    )
    specialization = models.CharField(
        max_length=100,
        verbose_name="Специализация",
        help_text="Введите специализацию доктора",
    )
    degree = models.CharField(
        max_length=100,
        verbose_name="Ученая степень",
        help_text="Введите ученую степень доктора",
    )
    procedures = models.ManyToManyField(
        Procedures,
        verbose_name="Процедуры",
        help_text="Выберите процедуры, которые доктор может провести",
        blank=True,
    )

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    class Meta:
        verbose_name = "Доктор"
        verbose_name_plural = "Доктора"


class Appointment(models.Model):
    doctor = models.ForeignKey(
        Doctors,
        on_delete=models.CASCADE,
        verbose_name="Доктор",
        help_text="Выберите доктора для записи",
    )
    patient = models.ForeignKey(
        "users.User",
        on_delete=models.CASCADE,
        verbose_name="Пациент",
        help_text="Выберите пациента для записи",
    )
    procedure = models.ForeignKey(
        Procedures,
        on_delete=models.CASCADE,
        verbose_name="Процедура",
        help_text="Выберите процедуру для записи",
    )
    appointment_datetime = models.DateTimeField(
        verbose_name="Дата и время записи",
        help_text="Выберите дату и время записи",
    )

    def __str__(self):
        return f"{self.doctor} - {self.patient} - {self.procedure}"

    class Meta:
        verbose_name = "Запись на приём"
        verbose_name_plural = "Записи на приём"


class Feedback(models.Model):
    user = models.ForeignKey(
        "users.User",
        on_delete=models.CASCADE,
        verbose_name="Пользователь",
    )
    text = models.TextField(
        verbose_name="Отзыв",
    )

    class Meta:
        verbose_name = "Отзыв"
        verbose_name_plural = "Отзывы"

    def __str__(self):
        return f"{self.user} - {self.text[:50]}..."

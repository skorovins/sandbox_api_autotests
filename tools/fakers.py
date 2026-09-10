from faker import Faker


class Fake:
    """
    Класс для генерации случайных тестовых данных с использованием библиотеки Faker.
    """

    def __init__(self, faker: Faker):
        """
        :param self: Экземпляр класс Faker, который будет использоваться для генерации данных.
        """
        self.fake = faker

    def title(self):
        """
        Генерирует случайный заголовок.

        :return: Случайный заголовок.
        """
        return self.fake.word()

    def views(self):
        """
        Генерирует случайное количество просмотров.

        :return: Случайное количество просмотров.
        """
        return self.fake.random.randint(1, 300)

fake = Fake(faker=Faker())
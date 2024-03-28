#================================================
#================================================
# Паттерн-Наблюдатель
# Блок 3. Урок 4
#================================================
#================================================


from abc import ABC
from abc import abstractmethod


class ObservableEngine(Engine):
    """ Класс, уведомляющий наблюдателей о полученных достижениях"""
    def __init__(self):
        """ Создадим пустое множество наблюдателей"""
        self.subscribers = set()

    def subscribe(self, subscriber):
        """ Добавляет наблюдателя в множество"""
        self.subscribers.add(subscriber)

    def unsubscribe(self, subscriber):
        """ Удоляет наблюдателя из множества"""
        self.subscribers.remove(subscriber)

    def notify(self, massege):
        """ Отправляет изменения наблюдателям"""
        for subscriber in self.subscribers:
            subscriber.update(massege)
        

class AbstractObserver(ABC):
    """ Класс Абстрактный наблюдатель. От него наследуются все наблюдатели."""

    @abstractmethod
    def update(self, massege):
        pass


class ShortNotificationPrinter(AbstractObserver):
    """ Класс-наблюдатель, который хранит сокращенные данные о полученных достижениях"""
    def __init__(self):
        self.achievements = set()  # множество достижений

    def update(self, massege):
        """ Метод наблюдения за обновлениями в классе ObservableEngine"""
        self.achievements.add(massege["title"])


class FullNotificationPrinter(AbstractObserver):
    """ Класс-наблюдатель, который хранит полные данные о полученных достижениях"""
    def __init__(self):
        self.achievements = list()  # список достижений

    def update(self, massege):
        """ Метод наблюдения за обновлениями в классе ObservableEngine"""
        if massege not in self.achievements:
            self.achievements.append(massege)
        

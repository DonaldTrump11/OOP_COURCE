#================================================
#================================================
# Паттерн-Декоратор
# Блок 3. Урок 2
#================================================
#================================================

from abc import ABC
from abc import abstractmethod
from inspect import isabstract

class Hero:
    def __init__(self):
        self.positive_effects = []
        self.negative_effects = []
        self.stats = {
            "HP": 128,  # health points
            "MP": 42,  # magic points, 
            "SP": 100,  # skill points
            "Strength": 15,  # сила
            "Perception": 4,  # восприятие
            "Endurance": 8,  # выносливость
            "Charisma": 2,  # харизма
            "Intelligence": 3,  # интеллект
            "Agility": 8,  # ловкость 
            "Luck": 1  # удача
        }

    def get_positive_effects(self):
        return self.positive_effects.copy()

    def get_negative_effects(self):
        return self.negative_effects.copy()

    def get_stats(self):
        return self.stats.copy()

class AbstractEffect(ABC, Hero):

    @abstractmethod
    def get_positive_effects(self):
        pass

    @abstractmethod
    def get_negative_effects(self):
        pass
    
    @abstractmethod
    def get_stats(self):
        pass
    
class AbstractPositive(AbstractEffect):

    def __init__(self, base):
        self.base = base

    @abstractmethod
    def get_positive_effects(self):
        self.base.get_positive_effects()

    @abstractmethod
    def get_negative_effects(self):
        self.base.get_negative_effects()

    @abstractmethod
    def get_stats(self):
        self.base.get_stats()

    
class AbstractNegative(AbstractEffect):

    def __init__(self, base):
        self.base = base
            
    @abstractmethod
    def get_positive_effects(self):
        self.base.get_positive_effects()

    @abstractmethod
    def get_negative_effects(self):
        self.base.get_negative_effects()

    @abstractmethod
    def get_stats(self):
        self.base.get_stats()

    
class Berserk(AbstractPositive):
    """ Увеличивает характеристики: Сила, Выносливость, Ловкость, Удача на 7;
уменьшает характеристики: Восприятие, Харизма, Интеллект на 3;
количество единиц здоровья увеличивается на 50."""
           
    def get_stats(self):
        """ Возвращаем статистику, динамически измененную от наложенного эффекта Berserk"""
        tmp_dict =self.base.get_stats()
        tmp_dict['HP'] = tmp_dict['HP'] + 50
        tmp_dict['Strength'] = tmp_dict['Strength'] + 7
        tmp_dict['Perception'] = tmp_dict['Perception'] - 3
        tmp_dict['Endurance'] = tmp_dict['Endurance'] + 7
        tmp_dict['Charisma'] = tmp_dict['Charisma'] - 3
        tmp_dict['Intelligence'] = tmp_dict['Intelligence'] - 3
        tmp_dict['Agility'] = tmp_dict['Agility'] + 7
        tmp_dict['Luck'] = tmp_dict['Luck'] + 7
       
        return tmp_dict

    def get_positive_effects(self):
        """ Возвращаем список наложенных позитивных эффектов, с добавленным Berserk"""
        spis = self.base.get_positive_effects()
        spis.append("Berserk")
        return spis

    def get_negative_effects(self):
        """ Возвращаем список наложенных негативных эффектов"""
        spis = self.base.get_negative_effects()
        return spis


class Blessing(AbstractPositive):
    """ Благословение (Blessing) -
        увеличивает все основные характеристики на 2."""

    def get_stats(self):
        """ Возвращаем статистику, динамически измененную от наложенного эффекта Blessing"""

        tmp_dict =self.base.get_stats()
        tmp_dict['Strength'] = tmp_dict['Strength'] + 2
        tmp_dict['Perception'] = tmp_dict['Perception'] + 2
        tmp_dict['Endurance'] = tmp_dict['Endurance'] + 2
        tmp_dict['Charisma'] = tmp_dict['Charisma'] + 2
        tmp_dict['Intelligence'] = tmp_dict['Intelligence'] + 2
        tmp_dict['Agility'] = tmp_dict['Agility'] + 2
        tmp_dict['Luck'] = tmp_dict['Luck'] + 2
       
        return tmp_dict

    def get_positive_effects(self):
        """ Возвращаем список наложенных позитивных эффектов, с добавленным Blessing"""
        spis = self.base.get_positive_effects()
        spis.append("Blessing")
        return spis
    def get_negative_effects(self):
        """ Возвращаем список наложенных негативных эффектов"""
        spis = self.base.get_negative_effects()
        return spis
    

class Weakness(AbstractNegative):
    """ Слабость (Weakness) -
        уменьшает характеристики: Сила, Выносливость, Ловкость на 4."""
    
    def get_stats(self):
        """ Возвращаем статистику, динамически измененную от наложенного эффекта Weakness"""

        tmp_dict =self.base.get_stats()
        tmp_dict['Strength'] = tmp_dict['Strength'] - 4
        tmp_dict['Endurance'] = tmp_dict['Endurance'] - 4
        tmp_dict['Agility'] = tmp_dict['Agility'] - 4
       
        return tmp_dict

    def get_positive_effects(self):
        """ Возвращаем список наложенных позитивных эффектов"""
        spis = self.base.get_positive_effects()
        return spis
    def get_negative_effects(self):
        """ Возвращаем список наложенных негативных эффектов, с добавленным Weakness"""
        spis = self.base.get_negative_effects()
        spis.append("Weakness")
        return spis


class Curse(AbstractNegative):
    """ Проклятье (Curse) -
        уменьшает все основные характеристики на 2."""

    def get_stats(self):
        """ Возвращаем статистику, динамически измененную от наложенного эффекта Curse"""

        tmp_dict =self.base.get_stats()
        tmp_dict['Strength'] = tmp_dict['Strength'] - 2
        tmp_dict['Perception'] = tmp_dict['Perception'] - 2
        tmp_dict['Endurance'] = tmp_dict['Endurance'] - 2
        tmp_dict['Charisma'] = tmp_dict['Charisma'] - 2
        tmp_dict['Intelligence'] = tmp_dict['Intelligence'] - 2
        tmp_dict['Agility'] = tmp_dict['Agility'] - 2
        tmp_dict['Luck'] = tmp_dict['Luck'] - 2
       
        return tmp_dict

    def get_positive_effects(self):
        """ Возвращаем список наложенных позитивных эффектов"""
        spis = self.base.get_positive_effects()
        return spis

    def get_negative_effects(self):
        """ Возвращаем список наложенных негативных эффектов, с добавленным Curse"""
        spis = self.base.get_negative_effects()
        spis.append("Curse")
        return spis
        

class EvilEye(AbstractNegative):
    """ Сглаз (EvilEye) -
        уменьшает  характеристику Удача на 10."""

    def get_stats(self):
        """ Возвращаем статистику, динамически измененную от наложенного эффекта EvilEye"""

        tmp_dict =self.base.get_stats()
        tmp_dict['Luck'] = tmp_dict['Luck'] - 10
       
        return tmp_dict

    def get_positive_effects(self):
        """ Возвращаем список наложенных позитивных эффектов"""
        spis = self.base.get_positive_effects()
        return spis

    def get_negative_effects(self):
        """ Возвращаем список наложенных негативных эффектов, с добавленным EvilEye"""
        spis = self.base.get_negative_effects()
        spis.append("EvilEye")
        return spis


#==========================================
#==========================================
#               ТЕСТИРОВАНИЕ
#==========================================
#==========================================

exit()
it __name__=='__main__':
    #------------------------------------------------
    print('-'*30, end = '\n')
    print("AbstractEffect абстрактный класс: ", isabstract(AbstractEffect))
    print("AbstractPositive абстрактный класс: ", isabstract(AbstractPositive))
    print("AbstractNegative абстрактный класс: ", isabstract(AbstractNegative))
    print("Berserk абстрактный класс: ", isabstract(Berserk))
    print("Weakness абстрактный класс: ", isabstract(Weakness))
    print('-'*30, end = '\n\n')
    #------------------------------------------------

    a = Hero()
    print('*'*20)
    print("stats: ", a.get_stats())
    print("positive: ", a.get_positive_effects())
    print("negative: ", a.get_negative_effects())
    print('*'*20, end = '\n\n')

    b = Berserk(a)
    print('Berserk', '*'*20)
    print("stats: ", b.get_stats())
    print("positive: ", b.get_positive_effects())
    print("negative: ", b.get_negative_effects())
    print('*'*20, end = '\n\n')

    c = Blessing(b)
    print('Blessing', '*'*20)
    print("stats: ", c.get_stats())
    print("positive: ", c.get_positive_effects())
    print("negative: ", c.get_negative_effects())
    print('*'*20, end = '\n\n')

    d = Weakness(c)
    print('Weakness', '*'*20)
    print("stats: ", d.get_stats())
    print("positive: ", d.get_positive_effects())
    print("negative: ", d.get_negative_effects())
    print('*'*20, end = '\n\n')

    e = Curse(d)
    print('Curse', '*'*20)
    print("stats: ", e.get_stats())
    print("positive: ", e.get_positive_effects())
    print("negative: ", e.get_negative_effects())
    print('*'*20, end = '\n\n')

    f = EvilEye(e)
    print('EvilEye', '*'*20)
    print("stats: ", f.get_stats())
    print("positive: ", f.get_positive_effects())
    print("negative: ", f.get_negative_effects())
    print('*'*20, end = '\n\n')

    f.base = f.base.base.base
    print('-Weakness -Curse', '*'*20)
    print("stats: ", f.get_stats())
    print("positive: ", f.get_positive_effects())
    print("negative: ", f.get_negative_effects())
    print('*'*20, end = '\n\n')


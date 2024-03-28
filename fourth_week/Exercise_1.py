#================================================
#================================================
# Паттерн 'Цепочка обязанностей'
# Блок 4. Урок 1
#================================================
#================================================

class EventGet:
    def __init__(self, type_name):
        self.type_name = type_name


class EventSet:
    def __init__(self, value_name):
        self.value_name = value_name


class NullHandler:
    """ Базовый класс для других классов-событий"""
    def __init__(self, base=None):
        self.base = base

    def handle(self, obj, event):
        if self.base is not None:
            result = self.base.handle(obj, event)
            if result is not None:
                return result


class IntHandler(NullHandler):
    """ Класс, отвечающий за действия с int"""
    def handle(self, obj, event):        
        if isinstance(event, EventGet):
            if not event.type_name == int:
                # Для обработки этого типа нужен другой класс
                return super().handle(obj, event)
            else:
                # Возвращаем значение переменной
                return obj.integer_field
    
        elif isinstance(event, EventSet):
            if not isinstance(event.value_name, int):
                # Для обработки этого типа нужен другой класс
                return super().handle(obj, event)
            else:
                # Задаем значение переменной integer_field
                obj.integer_field = event.value_name
        else:
            print("ERROR((... IntHandler")


class FloatHandler(NullHandler):
    """ Класс, отвечающий за действия с float"""
    def handle(self, obj, event):
        if isinstance(event, EventGet):
            if not event.type_name == float:
                # Для обработки этого типа нужен другой класс
                return super().handle(obj, event)                
            else:
                # Возвращаем значение переменной
                return obj.float_field
                
    
        elif isinstance(event, EventSet):
            if not isinstance(event.value_name, float):
                # Для обработки этого типа нужен другой класс
                return super().handle(obj, event)
            else:
                # Задаем значение переменной float_field
                obj.float_field = event.value_name


class StrHandler(NullHandler):
    """ Класс, отвечающий за действия с string"""
    def handle(self, obj, event):
        if isinstance(event, EventGet):
            if not event.type_name == str:
                # Для обработки этого типа нужен другой класс
                return super().handle(obj, event)
            elif event.type_name == str:
                # Возвращаем значение переменной
                return obj.string_field
    
        elif isinstance(event, EventSet):
            if not isinstance(event.value_name, str):
                # Для обработки этого типа нужен другой класс
                return super().handle(obj, event)
            else:
                # Задаем значение переменной string_field
                obj.string_field = event.value_name





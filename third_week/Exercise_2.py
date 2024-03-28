#================================================
#================================================
# Паттерн-Адаптер
# Блок 3. Урок 3
#================================================
#================================================


class MappingAdapter:
    """ Класс-Адаптер. Реализовывает метод ligten, используемый в System. 
    Реализовывает метод lighten с помощью методов класса Light"""
    def __init__(self, adaptee):
        self.adaptee = adaptee      # объект класса Light

    def lighten(self, grid):
        """ Метод подсчета освещенности и установки препятствий исходя из карты - grid(двойной массив)"""
                
        # Зададим новый размер матрицы класса Light 
        # исходя из размеров переданной карты (map)       
        self.adaptee.set_dim((len(grid[0]), len(grid)))

        # Добавляем координаты источников света 
        # кортежеми во временный список
        mass_light = []
        for x in range(len(grid)):
            for y in range(len(grid[x])):
                if grid[x][y] == 1:
                    mass_light.append((y, x))

        # Посчитем освещенность карты(1 на карте):
        self.adaptee.set_lights(mass_light)

        # Добавляем координаты объектов 
        # кортежеми во временный список
        mass_obj = []
        for x in range(len(grid)):
            for y in range(len(grid[x])):
                if grid[x][y] == -1:
               	    mass_obj.append((y, x))
        
        # Посчитаем установку препятствий(-1 на карте)
        self.adaptee.set_obstacles(mass_obj)
	
	    # Выведем карту
        return self.adaptee.generate_lights()




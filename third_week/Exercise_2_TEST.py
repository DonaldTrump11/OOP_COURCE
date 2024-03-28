#================================================
#================================================
# Паттерн-Адаптер
# Блок 3. Урок 3
#================================================
#================================================

# TODO: передаются (массив, массив[элемент]). Что передаем в return. SELF.adaptee!!!!! Координаты мартиц. 
# Неправильно записываются координаты в циклах
# Можно перевести цикл for по номерам мтрок и номерам элементов!?!?!?!

class MappingAdapter:
    """ Класс-Адаптер. Реализовывает метод ligten, используемый в System. 
    Реализовывает метод lighten с помощью методов класса Light"""
    def __init__(self, adaptee):
        self.adaptee = adaptee      # объект класса Light

    def lighten(self, grid):
        """ Метод подсчета освещенности и установки препятствий исходя из карты - grid(двойной массив)"""

        
        #___________________TEST___________________
        #print("До изменения размера матрицы: ", self.adaptee.dim)
        #print('\n\n')
        #__________________________________________


                
        # Зададим новый размер матрицы класса Light        
        self.adaptee.set_dim((len(grid), len(grid[0])))

        #___________________TEST___________________
        print("grid после изменения размера матрицы:\n ", self.adaptee.grid)
        print('\n\n')
        #__________________________________________

        # Пройдемся по всем координатам карты.
        # Те координаты, где находится 1, занесем 
        # во временный список кортежем
        mass_light = []
        for x in range(len(grid)):
            for y in range(len(grid[x])):
                if grid[x][y] == 1:
                    mass_light.append((y, x))

        # Посчитем освещенность карты(1 на карте):
        self.adaptee.set_lights(mass_light)

        # Пройдемся по всем координатам карты.
        # Те координаты, где находится -1, занесем 
        # во временный список кортежем
        mass_obj = []
        for x in range(len(grid)):
            for y in range(len(grid[x])):
                if grid[x][y] == -1:
               	    mass_obj.append((y, x))
        
        # Посчитаем установку препятствий(-1 на карте)
        self.adaptee.set_obstacles(mass_obj)
	
	    # Поворачиваем матрицу
        a = self.adaptee.generate_lights()
        a = list(tuple(zip(*a[::-1])))
        for i in range(len(a)):
            a[i] = list(a[i])
        return a
        #return adaptee.grid

#exit()




#================================================
#================================================
#                   ТЕСТИРОВАНИЕ
#================================================
#================================================

if __name__ == '__main__':
    
    #================================================
    #================================================
    # Код других классов для тестирования:
    class Light:
        def __init__(self, dim):
            self.dim = dim
            self.grid = [[0 for i in range(dim[0])] for _ in range(dim[1])]
            self.lights = []
            self.obstacles = []
            
        def set_dim(self, dim):
            self.dim = dim
            self.grid = [[0 for i in range(dim[0])] for _ in range(dim[1])]
        
        def set_lights(self, lights):
            self.lights = lights
        
        def set_obstacles(self, obstacles):
            self.obstacles = obstacles
            
        def generate_lights(self):
            return self.grid.copy()
    

    class System:
        def __init__(self):
            self.map = self.grid = [[0 for i in range(8)] for _ in range(9)]
            self.map[4][4] = 1 # Источники света
            self.map[1][3] = 1 # Источники света
            self.map[4][2] = 1 # Источники света
            self.map[2][2] = -1 # Стены
            self.map[1][2] = -1 # Стены
            self.map[2][4] = -1 # Стены
    
        def get_lightening(self, light_mapper):
            self.lightmap = light_mapper.lighten(self.map)

    #================================================
    #================================================
    # Код тестировки:

    a = Light((5,6))
    b = System()
    print("Начальный grid карты: ")
    print(b.grid)
    print('*'*25)
    c = MappingAdapter(a)
    b.get_lightening(c)

    #assert (len(c.adaptee.grid[1]), len(c.adaptee.grid)) == (6, 5), 'Неправильный размер мтрицы adaptee.grid'

    assert (4, 4) in c.adaptee.lights, 'Нужные координаты не передаются в метод set_lights'
    assert (1, 3) in c.adaptee.lights, 'Нужные координаты не передаются в метод set_lights'
    assert (4, 2) in c.adaptee.lights, 'Нужные координаты не передаются в метод set_lights'

    assert (2, 2) in c.adaptee.obstacles, 'Нужные координаты не передаются в метод set_obstacles'
    assert (1, 2) in c.adaptee.obstacles, 'Нужные координаты не передаются в метод set_obstacles'
    assert (2, 4) in c.adaptee.obstacles, 'Нужные координаты не передаются в метод set_obstacles'


    




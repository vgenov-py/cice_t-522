# class mun:
#     annual_growth = 1.03
#     def __init__(self, ine, density, area):
#         self.ine = ine
#         self.density = density
#         self.area = area

#     @property
#     def population(self):
#         return self.area * self.density

#     def population_times_value(self, value):
#         return self.population * value
    


# mun_1 = mun("280009", 3, 15)
# print(mun_1.population_times_value(3))

class Statistics:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        # self.n = len(x)

    @property
    def n(self):
        return len(self.x)
   
    def x_mean(self):
        return sum(self.x)/self.n

subject_1 = Statistics([20,18,18, 16], [1,2,3,4]) # semana 4
print(subject_1.x_mean())
subject_1.x.append(19) # semana 5
print(subject_1.x_mean())




    

    

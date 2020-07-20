#Tatoo-салон. Клиент имеет возможность осуществлять поиск и заказ Изображений в Каталоге, а также высталвять им оценку,
# в том числе и за качество работы. Клиент может предлагать свои изображения салону, за это может получать скидки и 
# повышение рейтинга. Администратор управляет Клиентами и контентом системы.

#Customer 
#       name
#       email
#       password
#   поиск изображений 
#   заказ изображений
#   выставление оценки изображению
#   выставление оценки за качество изображения
#   пердлагать свои изображения
#   получать скидки
#   получать повышение рейтинга

Class User:
    def __init__(self, fn, sn, e, l, p):
        self.fname = fn
        self.sname = sn
        self.email = e
        self.login = l
        self.password = p

Class Customer (User):
    def __init__(self, d, r)
    self.discount = d
    self.raiting = r



#Administrator
#       name
#       email
#       password
#   Управление Клиентами
#   Управление контентом (Изображениями)

Class Admin:


#Picture
#       description
#       prise
#       raiting
#       quality assessment

Class Picture:
    description =
    prise =
    raiting =
    quality_assessment


#ImageCatalog





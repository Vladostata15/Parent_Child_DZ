class Animals:
    amount_of_eyses = 2
    there_is_nous = 'Yes'

class Predators(Animals):
    teeth = 'Sharp teeth'
    amount_of_claws = 10
    middle_age = 20



class Tiger(Predators):
    middle_age = 18
    who_is_hunting = 'Wild boars, wild pigs, bears, buffaloes'




    def __init__(self):
        print(f'Who is hunting: {self.who_is_hunting}')
        print(f'Middle age: {self.middle_age}')
        print(f'Teeth: {self.teeth}')
        print(f'Amount of eyses: {self.amount_of_eyses}')
        print(f'Is there nous: {self.there_is_nous}')
        print(f'Amount of claws: {self.amount_of_claws}')


zoo = Tiger()


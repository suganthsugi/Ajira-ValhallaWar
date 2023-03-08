class Communicate:
    def __init__(self, message="success", status=0):
        self.message = message
        if(status==0):
    
    def success_message(self):


# class for a base 
class Base:
    # lets get the base name and shape and lengths of the sides of the base dynamically 
    # so that it may be changed later like triangle / hexagon
    def __init__(self, base_name, shape_of_the_base = "Square", lengths_of_the_sides = [0, 0, 0, 0]):
        # lets declare it as a private variable 
        # so that no other bases will not know about the wall hights and other info
        self.__base_name = base_name
        self.__shape_of_the_base = shape_of_the_base
        self.__lengths_of_the_sides = lengths_of_the_sides
        
        # to store the damaged walls and values
        self.damaged_side= -1
        self.damage_got = 0
    

    # setting and getting the base_name
    def get_base_name(self):
        return self.__base_name
    
    def set_base_name(self, base_name):
        self.__base_name = base_name
    

    # setting and getting the lengths_of_the_sides
    def get_lengths_of_the_sides(self):
        return self.__lengths_of_the_sides
    
    def set_lengths_of_the_sides(self, lengths_of_the_sides):
        self.__lengths_of_the_sides = lengths_of_the_sides
    

    # setting and getting the shape_of_the_base
    def get_shape_of_the_base(self):
        return self.__shape_of_the_base

    def set_shape_of_the_base(self, shape):
        self.__shape_of_the_base = shape
    


    # Attacking and recovering logics
    def gotAttack(self, attack):
        attacked_direction = attack.direction
        attacked_strength = attack.strength
        if(self.get_lengths_of_the_sides()[attacked_direction]<attacked_strength):
            self.recover(attacked_direction, attacked_strength)
    
    def recover(self, attacked_direction, attacked_strength):
        recovering_wall = self.get_lengths_of_the_sides()
        recovering_wall[attacked_direction] = attacked_strength
        self.set_lengths_of_the_sides(recovering_wall)




# class for attacks
class Attack:
    # getting the base to attack
    # and other attacking values
    def __init__(self, base, wepon_name = 'X', strength = 0, direction = 0):
        self.base_attacked = base
        self.wepon_name = wepon_name
        self.strength = strength
        self.direction = direction

    def attack(self, base, attack):
        base.gotAttack(attack)


# creating a base for Bersekers
bersekers_base = Base('Bersekers Base', "Square", [0, 0, 0, 0])
print(bersekers_base.get_lengths_of_the_sides())

attack1 = Attack(bersekers_base, 'X', 1, 0)
attack1.attack(bersekers_base, attack1)
print(bersekers_base.get_lengths_of_the_sides())
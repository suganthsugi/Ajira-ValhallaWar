from abc import ABC, abstractmethod

class Communicate:
    # for logging message
    def __init__(self, message="success", status=-1):
        self.message = message
        if(status==1):
            self.success_message()
        elif(status==0):
            self.failure_message()
        else:
            self.normal_message()
        
    
    def success_message(self):
        print(f"Hurray!!! {self.message}\n\n")
    
    def failure_message(self):
        print(f"Opps... {self.message}\n\n")
    
    def normal_message(self):
        print(f"{self.message}")


class Shapes(ABC):
    def __init__(self, shape_name = "Square", sides=4):
        self.shape_name = shape_name
        self.sides = sides
        self.walls = []
    
    @abstractmethod
    def set_sides(self, walls):
        pass


# class for a base 
class Base(Shapes):
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
    

    def set_sides(self, walls):
        self.__lengths_of_the_sides = walls
    

    # Attacking and recovering logics
    def gotAttack(self, attack):
        attacked_direction = attack.direction
        attacked_strength = attack.strength
        if(self.get_lengths_of_the_sides()[attacked_direction]<attacked_strength):
            Communicate("Attack successfull", 1)
        else:
            Communicate("Wall is high", 0)
    
    def recover(self, attacked_direction, attacked_strength):
        recovering_wall = self.get_lengths_of_the_sides()
        recovering_wall[attacked_direction] = attacked_strength
        self.set_lengths_of_the_sides(recovering_wall)



# class for attacks
class Attack():
    # getting the base to attack
    # and other attacking values
    def __init__(self, base, attacker_name, wepon_name = 'X', strength = 0, direction = 0):
        self.base_attacked = base
        self.attacker_name = attacker_name
        self.wepon_name = wepon_name
        self.strength = strength
        self.direction = direction

    def attack(self, base, attack):
        base.gotAttack(attack)





if __name__ == '__main__':
    print("-----\t  Valhalla \t-----\n")
    
    # creating a base dynamically
    base_name = input("Enter the base name (eg:Bersekers Base): ")
    
    # initializing the base
    base = Base(base_name, "Square", [0, 0, 0, 0])
    
    flag=True
    while(flag):
        # getting the shape of the base
        base_shape = input("Enter your base shape (eg: Square / Rectange / Triangle): ")
        if(base_shape.lower()=="square" or base_shape.lower()=="rectangle"):
            base = Base(base_name, base_shape, [0, 0, 0, 0])
            flag=False
        elif(base_shape.lower()=="triangle"):
            base = Base(base_name, base_shape, [0, 0, 0])
            flag=False
        else:
            Communicate("Invalid imput", 0)
    Communicate(f"Base Created with name {base.get_base_name()}\n\n", 1)
            
    print('---\t Attacks \t---\n\n')
    
    # attacking day by day
    attack_number = 1
    attacks_log = []
    choice = 1
    while(choice):
        print(f"Day {attack_number}")
        attack_number+=1
        
        # getting console inputs
        attacklogs=[]
        N = int(input("Number of attack"))
        for i in range(N):
            attacker_name = input("Enter the attacker name : ")
            wepon_name = input("Wepon name : ")
            strength = int(input("Magnitude of the attack : "))
            print("Direction to attack...\n")
            atk_dir=0
            attack=[]
            
            if(base.get_shape_of_the_base().lower()=="square"):
                directions={
                    'n':0,
                    's':1,
                    'e':2,
                    'w':3,
                }
                direction = input("Enter which side to attack [n - North, s - South, e - East, w - West] : ")
                atk_dir = directions[direction]
            elif(base.get_shape_of_the_base().lower()=='trianle'):
                directions={
                    'l':0,
                    'r':1,
                    'b':2
                }
                direction = input("Enter which side to attack [l - Left, r - Right, b - Base] : ")
                atk_dir = directions[direction]
            
            attacklogs.append([atk_dir, strength])
            
            # attacking
            attack = Attack(base, attacker_name, wepon_name, strength ,atk_dir)
            attack.attack(base, attack)
        print(attacklogs)
        
        for x in attacklogs:
            base.recover(x[0], x[1])
        
        print(base.get_lengths_of_the_sides())
        
        choice = int(input("Enter 1 to attack and 0 to give up : "))
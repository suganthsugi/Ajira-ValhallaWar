from abc import ABC, abstractmethod


# creating a class walls with protected sides
class Wall:
    def __init__(self, sides=4):
        self.__sides = [0 for i in range(sides)]
    
    def get_walls(self):
        return self.__sides

    def set_walls(self, ind, strength):
        if(self.__sides[ind]<strength):
            self.__sides[ind]=strength



# class for shapes so that we can make differt kinds of shapes
class Shapes(ABC, Wall):
    def __init__(self, shape_name = "Square", sides=4):
        self.shape_name = shape_name
        self.sides = sides
        super().__init__(sides)
    
    @abstractmethod
    def set_sides(self, walls):
        pass


# class for a base 
class Base(Shapes):
    # lets get the base name and shape and lengths of the sides of the base dynamically 
    # so that it may be changed later like triangle / hexagon
    def __init__(self, base_name, shape_of_the_base = "square"):
        # lets declare it as a private variable 
        # so that no other bases will not know about the wall hights and other info
        self.__base_name = base_name
        self.__shape_of_the_base = shape_of_the_base
        super().__init__(shape_of_the_base, 4)
        # to store the damaged walls and values
        self.damaged_side= -1
        self.damage_got = 0
        self.res=0
    

    # setting and getting the base_name
    def get_base_name(self):
        return self.__base_name
    
    def set_base_name(self, base_name):
        self.__base_name = base_name
    

    # setting and getting the lengths_of_the_sides
    def get_lengths_of_the_sides(self):
        return self.get_walls()
    
    def set_lengths_of_the_sides(self, ind, strength):
        self.set_walls(ind, strength)
    

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
            self.res+=1
            Communicate("Attack successfull", 1)
        else:
            Communicate("Wall is high", 0)
    
    def recover(self, attacked_direction, attacked_strength):
        recovering_wall = self.get_lengths_of_the_sides()
        recovering_wall[attacked_direction] = attacked_strength
        self.set_lengths_of_the_sides(attacked_direction, attacked_strength)



# for fancy printing the console message
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
    base = Base(base_name, "square")
    
    flag=True
    while(flag):
        # getting the shape of the base
        base_shape = input("Enter your base shape (eg: Square / Rectange / Triangle): ")
        if(base_shape.lower()=="square" or base_shape.lower()=="rectangle"):
            base = Base(base_name, base_shape)
            flag=False
        elif(base_shape.lower()=="triangle"):
            base = Base(base_name, base_shape)
            flag=False
        else:
            Communicate("Invalid imput", 0)
    Communicate(f"Base Created with name {base.get_base_name()}\n\n", 1)
            
    print('---\t Attacks \t---\n\n')
    
    # attacking day by day
    attack_number = 1
    logs=[]
    inp = [x.strip().split(':') for x in input().strip().split(';')]
    resinp=[]
    for x in inp:
        tx=[]
        for y in x:
            tx.append(y.strip().split(' - '))
        resinp.append(tx)
    for i in range(len(resinp)):
        resinp[i][0][0]=(resinp[i][0][0][(resinp[i][0][0].find('$')+1):]).strip()
    for i in range(len(resinp)):
        currday = resinp[i]
        attacklog=[]
        for x in currday:
            attacker_name = x[0]
            direction = x[1]
            wepon_name = x[2]
            strength = int(x[3])
            directions={
                'N':0,
                'S':1,
                'E':2,
                'W':3,
            }
            atk_dir = directions[direction]
            print(attacker_name, direction, wepon_name, strength)
            attack = Attack(base, attacker_name, wepon_name, strength ,atk_dir)
            attack.attack(base, attack)
            attacklog.append([atk_dir, strength])
        for x in attacklog:
            base.recover(x[0], x[1])
    print(base.res)
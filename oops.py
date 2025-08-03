# Creating class - blueprint of anything 
class Fruit:
    # constructor -> inside constructor u will add atributes
    def __init__(self,color,taste,shape,preference): 
        self.color=color
        self.taste=taste
        self.shape=shape
        self.preference=preference

# methods - fuction created inside class
    def get_color(self):
        return self.color

    def set_shape(self,new_shape):
        self.shape = new_shape
        return self.shape

    def increase_preference(self):
        self.preference = self.preference +1

    def showFruit(self):
        print ("Hello, I am fruit with {}, {}, {}, {}".format(self.color, self.taste, self.shape, self.preference))

apple =Fruit ("red","sweet","circle",2)
print(apple.get_color())
print(apple.set_shape("round"))
apple.showFruit()

lemon = Fruit ("yellow", "sour", "egg shape",1)
print(lemon.get_color())
print(lemon.set_shape("eggshape"))
lemon.showFruit()

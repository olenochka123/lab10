class Lawn_mower:
    count_of_sells = 0

    def __init__(self, width_of_grass_cut=None, power=None, model=None,
                 capacity=None,
                 wheels_height=None, count_of_stages=None, weight=None):
        self.width_of_grass_cut = width_of_grass_cut
        self.power = power
        self.model = model
        self.capacity = capacity
        self.wheels_height = wheels_height
        self.count_of_stages = count_of_stages
        self.weight = weight
        Lawn_mower.count_of_sells = Lawn_mower.count_of_sells + 1

    @staticmethod
    def staticmethod():
        return Lawn_mower.count_of_sells

    def __str__(self):
        f_width_of_grass_cut = "width_of_grass_cut: {0}\n".format(self.width_of_grass_cut)
        f_power = "power: {0}\n".format(self.power)
        f_model = "model: {0}\n".format(self.model)
        f_capacity = "capacity : {0}\n".format(self.capacity)
        f_wheels_height = "wheels height: {0}\n".format(self.wheels_height)
        f_count_of_stages = "count of stages: {0}\n".format(self.count_of_stages)
        f_weight = "weights: {0}\n".format(self.weight)
        return f_width_of_grass_cut + f_power + f_model + f_capacity + f_wheels_height + \
               f_count_of_stages + f_weight

    def __del__(self):
        print("Delete " + self.__class__.__name__ + " | Object ID: " + str(id(self)))
        return


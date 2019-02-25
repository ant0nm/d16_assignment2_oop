class Field:

    # class variables
    fields = []
    food_harvested = 0

    # insatnce methods
    def __init__(self, type, hectares, num_cows, num_chickens):
        self.type = type
        self.hectares = hectares
        self.animals = {"cows": num_cows, "chickens": num_chickens}
        if type == 'corn':
            self.yield_per_hectare = 20
        elif type == 'wheat':
            self.yield_per_hectare = 30
        elif type == "potato":
            self.yield_per_hectare = 40

    # class methods
    @classmethod
    def create(cls, type, hectares, num_cows, num_chickens):
        new_field = Field(type, hectares, num_cows, num_chickens)
        cls.fields.append(new_field)
        return new_field

    @classmethod
    def total_food_harvested(cls):
        return "The farm has {} harvested food so far.".format(cls.food_harvested)

    @classmethod
    def harvest(cls):
        for field in cls.fields:
            field_yield = field.hectares * field.yield_per_hectare
            cls.food_harvested += field_yield
            for animal in field.animals:
                field.animals[animal] += 5

    @classmethod
    def get_status(cls):
        for field in cls.fields:
            field_type = field.type.capitalize()
            print("{} field is {} hectares.".format(field_type, field.hectares))
            for animal in field.animals:
                print("\t> It has {} {}.".format(field.animals[animal], animal))
        print(cls.total_food_harvested())

    @classmethod
    def relax(cls):
        for field in cls.fields:
            if field.type == 'corn':
                print("{} hectares of tall green stalks rustling in the breeze fill your horizon.".format(field.hectares))
            elif field.type == 'wheat':
                print("The sun hangs low, casting an orange glow on a sea of {} hectares of wheat.".format(field.hectares))
            elif field.type == "potato":
                print("The wind is blowing, the sun in shining, your potatoes are growing by the hour.")

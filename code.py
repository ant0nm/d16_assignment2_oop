from field import Field

class FieldManager:

    def main_menu(self):
        while True:
            self.print_main_menu()
            user_selected = input()
            self.call_option(user_selected)

    def print_main_menu(self):
        print()
        print("--------------------")
        print("Options:")
        print("field -> adds a new field")
        print("harvest -> harvests crops and adds to total harvested")
        print("status -> displays some information about the farm")
        print("relax -> provides lovely descriptions of your fields")
        print("exit -> exits the program")
        print("--------------------")
        print()
        print("Enter an option: ", end="")

    def call_option(self, user_selected):
        if user_selected == "field":
            self.add_new_field()
        elif user_selected == "harvest":
            self.harvest_fields()
        elif user_selected == "status":
            self.farm_status()
        elif user_selected == "relax":
            self.farm_relax()
        elif user_selected == "exit":
            print("Exiting...")
            exit()
        else:
            print("Please enter a valid option!")

    def add_new_field(self):
        print("What kind of field is it: corn or wheat?")
        field_type = input()

        print("How large is the field in hectares?")
        field_size = int(input())

        Field.create(field_type, field_size)

        print("Added a {} field of {} hectares!".format(field_type, field_size))

    def harvest_fields(self):
        Field.harvest()
        for field in Field.fields:
            print("Harvesting {} food from {} hectare {} field.".format((field.hectares * field.yield_per_hectare), field.hectares, field.type))
        print(Field.total_food_harvested())

    def farm_status(self):
        Field.get_status()

    def farm_relax(self):
        Field.relax()

manager = FieldManager()
manager.main_menu()

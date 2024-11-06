class Students:
    def __init__(self, name, house, spell):
        if not name:
            raise ValueError("Missing Name")
        if house not in ['Gdynia', 'Sopot', 'Gdansk']:
            raise ValueError('Wrong house')
        self.name = name
        self.house = house
        self.spell = spell

    def __str__(self):
        return f"{self.name} from {self.house} and {self.spell}"

    def charm(self):
        match self.spell:
            case 'Lumos':
                return 'Light'
            case 'Patronus':
                return 'Animal'
            case _:
                return 'No spell'

def main():
    student = get_student()
    print(f"Spell {student.charm()}")

def get_student():
    name = input('What is the name: ')
    house = input('What is the house: ')
    spell = input('Favourit spell: ')
    return Students(name, house, spell)

if __name__ == '__main__':
    main()
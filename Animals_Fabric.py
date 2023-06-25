from Animals import Dog, Bird, Fish


class AnimalFabric:
    def make_animal(self, animal_type: str, *args, **kwargs):
        new_animal = self._get_maker(animal_type)
        return new_animal(*args, **kwargs)

    @staticmethod
    def _get_maker(animal_type: str):
        types = {"dog": Dog, "bird": Bird, "fish": Fish}
        return types[animal_type.lower()]


fabric = AnimalFabric()
animal_from_fabric = fabric.make_animal("dog", "Рэкс", 40, 5, "Бульдог")
animal_from_fabric1 = fabric.make_animal("bird", "Саша", 1, 3, "Попугай", "Катя")

print(animal_from_fabric)
print(animal_from_fabric1)
print(fabric.make_animal('Fish', "Немо", 10, 5, "Морской"))
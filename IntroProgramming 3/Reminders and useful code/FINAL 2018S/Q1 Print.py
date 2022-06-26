
class Pet(object):

    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age

    def __repr__(self):
        return "Pet({}, {})".format(self.name, self.age)

class PetWatcher(object):
    def notify(self, pet: Pet):
        raise NotImplementedError("Concrete PetWatcher must have notify method")

class PetList(object):
    def __init__(self):
        self._pets = [ ]
        self._listeners = [ ]

    def add_listener(self, listener: PetWatcher):
        self._listeners.append(listener)

    def notify_all(self, pet: Pet):
        for listener in self._listeners:
            listener.notify(pet)

    def add(self, pet: Pet):
        self._pets.append(pet)
        self.notify_all(pet)

class OldPetWatcher(PetWatcher):
    def __init__(self):
        self.max_age = -1
        self.oldest = None

    def notify(self, pet: Pet):
        if pet.age > self.max_age:
            self.max_age = pet.age
            self.oldest = pet

pets = PetList()
watcher = OldPetWatcher()
pets.add_listener(watcher)
pets.add(Pet("Nora", 6))
pets.add(Pet("Merlin", 9))
pets.add(Pet("Meza", 7))

print(watcher.oldest)
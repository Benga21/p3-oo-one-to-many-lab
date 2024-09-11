# owner_pet.py

class Pet:
    # Variable storing allowed pet types
    PET_TYPES = ['dog', 'cat', 'rodent', 'bird', 'reptile', 'exotic']
    
    # Class variable to store all Pet instances
    all = []
    
    def __init__(self, name, pet_type, owner=None):
        self.name = name
        
        # Validate if pet_type is valid
        if pet_type not in Pet.PET_TYPES:
            raise Exception(f"Invalid pet type: {pet_type}")
        self.pet_type = pet_type

        # Assign owner if provided
        self.owner = owner
        if owner:
            owner.add_pet(self)

        # Add the pet to the class variable `all`
        Pet.all.append(self)

class Owner:
    def __init__(self, name):
        self.name = name
        # List to store pets related to the owner
        self._pets = []

    def pets(self):
        """Returns all pets belonging to the owner."""
        return self._pets

    def add_pet(self, pet):
        """Adds a pet to the owner, ensuring it is an instance of the Pet class."""
        if not isinstance(pet, Pet):
            raise Exception("Only instances of Pet can be added as pets.")
        pet.owner = self
        self._pets.append(pet)

    def get_sorted_pets(self):
        """Returns all pets sorted by their name."""
        return sorted(self.pets(), key=lambda pet: pet.name)

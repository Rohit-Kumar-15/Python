# 03 - Combining Objects (Composition)
# One object can contain and use another object.
# basically doing inhertiance , 
# engine and music system are the parent class and engine and music system are the parent class , 
# multiple inheritiance 
class Engine:
    def start(self):
        print("Engine started.")

class MusicSystem:
    def play(self, song):
        print(f"Playing: {song}")

class Car:
    def __init__(self, brand):
        self.brand = brand
        self.engine = Engine()
        self.music_system = MusicSystem()

    def start_car(self):
        print(f"Starting {self.brand}...")
        self.engine.start()

    def play_music(self, song):
        self.music_system.play(song)

my_car = Car("Toyota")
my_car.start_car()
my_car.play_music("My favourite song")

# Car is composed of smaller objects: Engine and MusicSystem.

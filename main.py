import sys, os, re, random, time
import threading

def clear_console():
    if sys.platform == "win32":
        os.system("cls")
    elif sys.platform == "linux1" or sys.platform == "linux2"\
        or sys.platform == "darwin":
        os.system("clear")

class Game:
    
    def __init__(self):
        self.goal : int = 0
        self.inventory : list(int) = []
        self.endgame = False

    def run(self):
        print("Welcome to Countdown")
        print("You are presented a set of 6 numbers, and one target number")
        print("Try to get as close as you can to the target number, but there are some rules")
        print("You can use only numbers from the set, each number should be used only once or less")
        print("type quit or q to end the game")
        
        while not self.endgame:
            self._play_round()
    
    def _play_round(self):
        """ plays the round """
        self._setup_round()
        while True:
            print("*****************************")
            print(f"The goal is {self.goal}")
            print(f"Your set of numbers is {self.inventory}")
            solution = input(">> ")
            if solution == "quit" or solution == "q":
                self.endgame = True
                return
            
            
            clear_console()
            if self._verify_input(solution):
                break
            print("Error: Wait, that's illegal")

        result = int(eval(solution.replace("/", "//")))
        error = abs(result - self.goal)

        print("*****************************")
        if error == 0:
            print("Congratz, You scored a perfect one")
        print(f"The goal:{self.goal}, Your result:{result}")
        print(f"Your result was off by {error}")
            
    
    def _setup_round(self):
        self.goal = random.randint(1, 999)
        small = [random.randint(1, 9) for _ in range(2)]
        medium = [random.randint(10, 99) for _ in range(2)]
        big = [random.randint(100, 999) for _ in range(2)]
        self.inventory = small + medium + big
        self.inventory.sort()
    
    def _verify_input(self, solution : str):
        # verify that the input doesn't contain any other chars we dont want
        if not re.match(r"^[\d\+\-\/\*\(\) ]+$", solution):
            return False

        # split the input to the individual numbers
        split = list(filter(None, re.split(r" |\+|\-|\/|\*|\(|\)", solution)))
        answers = self.inventory[:]

        for num in split:
            try:
                answers.remove(int(num))
            except:
                return False

        return True

if __name__ == "__main__":
    game = Game()
    game.run()
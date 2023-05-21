class SpaceShip():
  
    def __init__(self, row=0, col=0):
        self.row = row
        self.col = col
    def move(self,direction):
        if direction == "north":
            self.row = self.row -2
        elif direction == "south":
            self.row = self.row +2
        if direction == "northwest":
            self.row = self.row -1
            self.col = self.col -1
        elif direction == "southwest":
            self.row = self.row +1
        elif direction == "northeast":
            self.row = self.row -1
            self.col = self.col +1
        elif direction == "southeast":
            self.row = self.row +1
            self.col = self.col +1
        
    def __repr__(self) -> str:
        return f"row:{self.row}, col:{self.col}"

class Destination():
    def __init__(self, row, col=0):
        self.row = row
        self.col = col

def main():
    ss = SpaceShip()
    m = input("input a direction")
    while m != "":
        ss.move(m)
        print (ss)
        m = input("input a direction")
        
if __name__=="__main__":
    main()




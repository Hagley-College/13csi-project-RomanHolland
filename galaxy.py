class Galaxy:
    g = [[0,0,0,0],
         [0,1,1,0],
         [0,1,1,0],
         [0,0,0,0]]
    
    def __repr__(self) -> str:
        s=""
        for row in self.g:
            for col in row:
                if col == 1:
                    s = s+(" ")
                else:
                    s = s+("#")
            s = s+("\n")
        return s

def main():
    g = Galaxy()
    print(g)
 
if __name__== "__main__":
    main()

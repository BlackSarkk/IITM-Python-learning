class Vector():
    def __init__(self, x:int, y:int):
        self.x = x
        self.y = y
        
        
    def print_info(self):
        print(f"({self.x},{self.y})")
        
    def scale(self, s):
        self.x *= s
        self.y *= s
        
    def reflect_about_X(self):
        self.y = -1 * self.y
        
    def reflect_about_Y(self):
        self.x = -1 * self.x
        
    
    def add(self, other: "Vector") -> "Vector":
        # other is expected to be a Vector; return a new Vector (do not modify self)
        return Vector(self.x + other.x, self.y + other.y)
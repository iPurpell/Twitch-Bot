class User:
    
    lurktotal=None
    lurktime=None
    points=0

    def __init__(self, lurktotal, lurktime, points):
        self.lurktotal = lurktotal
        self.lurktime = lurktime
        self.points = points
             
    def add_lurk(self,time):
        self.lurktotal=+time
    
    def get_lurktime(self):
        return self.lurktime
    
    def set_lurktime(self, time):
        self.lurktime = time

    def get_lurktotal(self):
        return self.lurktotal

    def add_points(self, points):
        self.points=+points
    
    def spend_points(self, points):
        self.points=-points
    
    def get_points(self):
        return self.points
    
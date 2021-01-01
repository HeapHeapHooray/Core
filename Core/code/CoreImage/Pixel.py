class Pixel:
    def __init__(self,r: int,g: int,b: int,a: int):
        self.r,self.g,self.b,self.a = r,g,b,a
    def get_rgba(self):
        return self.r, self.g, self.b, self.a
    def set_rgba(self,r: int,g: int,b: int,a: int):
        self.r,self.g,self.b,self.a = r,g,b,a
    def set_pixel(self,pixel):
        if not isinstance(pixel,Pixel):
            pixel = Pixel(0,0,0,0)
        self.set_rgba(*pixel.get_rgba())
    def equals(self,pixel) -> bool :
        return self.get_rgba() == pixel.get_rgba()

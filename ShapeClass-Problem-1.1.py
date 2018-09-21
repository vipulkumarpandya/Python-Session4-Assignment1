class shape:

    def setSides(self):
       msg = "Enter sides of " + self.__class__.__name__  + " seperated by Comma : "
       a = input(msg).split(",")
       self.sides = a


    def getSides(self):
       return self.sides


class triangle(shape):

    def areaTriangle(self):

        allsides = super().getSides()

        side1 = int(allsides[0])
        side2 = int(allsides[1])
        side3 = int(allsides[2])

        s = (side1+side2+side3)/2
        print((side1+side2+side3)/2)
        print(s)

        area = (s*(s-side1)*(s-side2)*(s-side3))**0.5
        return area

class square(shape):

    def areaSquare(self):
        allsides=super().getSides()
        side1 = int(allsides[0])
        area = side1 * side1
        return area



tri=triangle()
tri.setSides()
print("Area of triangle = ",tri.areaTriangle())

sq=square()
sq.setSides()
print("Area of Square = ",sq.areaSquare())

class triangle:
    def __init__(self,s1,s2,s3):
        self.s1 = s1
        self.s2 = s2
        self.s3 = s3
        
    def perimeter(self):
        self.perimeter = self.s1+self.s2+self.s3
        print('Perimeter: ',self.perimeter)

    def area(self):
        s = self.perimeter/2
        self.area = (s*(s-self.s1)*(s-self.s2)*(s-self.s3))**0.5
        print('Area of the triangle is: ',self.area)
        
    def __str__(self):
        return("\nTriangle has \nSide 1: "+ str(self.s1)+ '\nSide 2: '+ str(self.s2)+'\nSide 3: ' + str(self.s3))

tri1 = triangle(2,2,3)




tri1.perimeter()

tri1.area()

print(tri1)



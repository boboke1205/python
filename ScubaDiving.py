class ScubaDiving:


    def __init__(self, name, sex, age, height):
        self.name = name
        self.sex = sex
        self.age = age
        self.height = height

    def showMyProfile(self):
        print "Name = %s" % self.name
        print "Sex = %s" % self.sex
        print "Age = %s" % self.age
        print "Height = %s" % self.height
        print "-------------------------"

    def swimming(self):
        print self.name + " swimming"

    def diving(self):
        print self.name + " diving"

    def kick(self):
        print self.name + " kick"

    def breathing(self):
        print self.name + " breathing"


class RescueScubaDiving(ScubaDiving) :
    def rescue(self):
        print self.name + " rescue"

    def diving(self):
        print self.name + " rescue diving"



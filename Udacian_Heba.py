class Udacian:
    def __init__(self,name,city,enrollment,nanodegree,status):
    	self.name=name
    	self.city=city
    	self.enrollment=enrollment
    	self.nanodegree=nanodegree
    	self.status=status
    def print_Udacity(self):
    	return "name: "+self.name+" city: "+self.city+" enrollment: "+self.enrollment+" nanodegree: "+self.nanodegree+" status: "+self.status

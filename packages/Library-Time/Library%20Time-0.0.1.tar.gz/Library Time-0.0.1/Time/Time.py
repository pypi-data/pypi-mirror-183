class Time:
    '''
    Enter time like : 12:25:5
    
    '''
    Csec=0
    Cmin=0
    def __init__(self,time):
        get_time=time.split(':')
        self.h=int(get_time[0])
        self.m=int(get_time[1])
        self.s=int(get_time[2])

    def __str__(self):
        return f"self.h:self.m:self.s"

    def __add__(self,other):
        Gs=self.sum_sec(self.s,other.s)
        Gm=self.sum_min(self.m,other.m)
        Gh=self.sum_hour(self.h,other.h)
        return Tim(f"{Gh}:{Gm}:{Gs}")

    def sum_sec(self,s1,s2):
        Fsec=s1+s2
        while Fsec>60:
            Fsec-=60
            self.Csec=+1
        return self.Fsec

    def sum_min(self,m1,m2):
        Fmin=m1+m2+self.Csec
        while Fmin>60:
            Fmin-=60
            self.Cmin+=1
        return self.Fmin

    def sum_hour(self,h1,h2):
        Fhour=h1+h2+self.Fmin
        while Fhour>24:
            Fhour-=24
        return self.Fhour
        

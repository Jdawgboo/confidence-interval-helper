from math import sqrt
def proportion_interval(successes:int,total:int,z:float=1.96)->tuple[float,float]:
 p=successes/total; margin=z*sqrt(p*(1-p)/total)
 return round(max(0,p-margin),6),round(min(1,p+margin),6)

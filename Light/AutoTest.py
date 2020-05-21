import numpy as np
import random

import FunktionLight as Fun

#'The optical path is reversible'
def AutoCheckTest(IncidentLight,Plane,ReflectedLight,TrasmittedLight,n1,n2):
    #'use the Reflectedlight to calculate the Incidentlight'
    r2 = np.array([0,0,0])
    r2 = Fun.CaRDir(ReflectedLight,Plane)

    #'use the Trasmitted light to calculate the Incidentlight'
    t2 = np.array([0,0,0])
    t2 = Fun.CaTdir(TrasmittedLight,Plane,n2,n1)
    

    if abs(np.linalg.norm(np.cross(IncidentLight.dn,r2))) <= 0.01:
        print('ok')
    else:
        print('-------->  R false for this point:--------<')
        IncidentLight.displayLight()
        return False
    
    if abs(np.linalg.norm(np.cross(IncidentLight.dn,t2))) <= 0.01:
        print('ok')
    else:
        print('-------->  T false for this point:--------<')
        IncidentLight.displayLight()
        return False

    return True

def RandomLightInput():
    
    a = Fun.Light()# a is Incidentlight
    b = Fun.Plane()# b is the Plane

    a.inc(np.random.randint(5,size=3),np.random.randint(5,size=3))
    b.inc(np.random.randint(5,size=3),np.random.randint(5,size=3))   
    n1 = random.randint(1,3)
    n2 = random.randint(1,3)
    return (a,b,n1,n2)
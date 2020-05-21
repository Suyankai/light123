import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import axes3d
from matplotlib import cm
import random

import FunktionLight as Fun
import DisplayWholeProcess as DisWP
import DisplayWholeProcess2 as DisWP2
import test as TS
import AutoTest as TIS

if __name__ == '__main__':
    
    a = Fun.Light()# a is Incidentlight
    b = Fun.Plane()# b is the Plane
    r = Fun.Light()# r is reflectedlight
    t = Fun.Light()# t is refractedlight(transmitted light)
    n1 = 1
    n2 = 1


    Autotest = False
    #'here we input the situation'   
    if Autotest == True:
        (a,b,n1,n2) = TIS.RandomLightInput()
    else:
        #'use the Test Case we set by hand'
        (a,b,n1,n2) = TS.InputLightPlane7()

    #''
    if Fun.JudgeCrossPoint(a,b):

        r.inc(Fun.CaPoint(a,b),Fun.CaRDir(a,b))
        print('The point and direction of the reflected light is:')
        r.displayLight()

        #'first judge if the total reflection will happen, Ture is not happen, and False is happen'
        if Fun.JudgeTotalReflection(a,b,n1,n2):
            t.inc(Fun.CaPoint(a,b),Fun.CaTdir(a,b,n1,n2))
            print('The point and direction of the transmitted(refractedlight) light is:')
            t.displayLight()

            if Autotest == True:
                TIS.AutoCheckTest(a,b,r,t,n1,n2)
            else:
                # Display the picture of the lights and plane
                DisWP.DisplayWholeProcess(a,r,t,b)
        else:
            print('Total reflection and no more transmitted(refractedlight) light')
            
            # there is no more refractedlight, and then we display a,r,b, 
            # because the default(class of Light)set of the direction is [0,0,0]
            # actually we cant see the refractedlight of t 
            if Autotest == True:
                TIS.AutoCheckTest(a,b,r,t,n1,n2)
            else:
                # Display the picture of the lights and plane
                DisWP.DisplayWholeProcess(a,r,t,b)
    else:
        print('There is no cross point, so the reflected light and the transmitted light miss')
        DisWP2.DisplayWholeProcess2(a,b)
    

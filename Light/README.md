## Introduction
**Class**
- **Light** 
 -**One point in Light**
 -**The direction vector**
 -**The normalized direction vector**
- **Plane**
 -**One point in Plane**
 -**The normal vector**
 -**The normalized normal vector**

**Function**
- **Normalized**: put in the vector [x,y,z] and normalize it
- **JudgeCrossPoint**: Determine if there will be a cross point between the Incidentlight and the plane or not
- **JudgeTotalReflection**: Determine if total reflection will occur
- **CaRDir**: calculate the direction of the reflected light.
- **CaPoint**: calculate the point -Intersection of light and plane
- **CaTdir**: calculate the direction of the transmitted light
- **DisplayWholeProcess**: Plot the normalized light and plane
- **InputLightPlane*N**: the test case for the default input, here we have 7 different cases(N = 7)
- **AutoCheckTest**: "The optical path is reversible", then we use that to test the correctness of the program.


## The Equation (Latex)

### Fun(CaRDir)
If the incident light is **vertical or nearly vertical** to the plane, we take $\vec{r} = -\vec{i}$
And for other cases we use the following formula to calculate: 
$$ \vec{r} = \vec{i} - 2 * \left ( \vec{i} * \vec{n} \right ) *\vec{n} $$

*There will be some deviation in the vertical case, but it will be a short time for calculation.*

### Fun(CaPoint)
In the class of line, we have set a point $pl = [pl_0 ,pl_1 ,pl_2]$ which the light goes through, and also a direction $\vec{d} = [v_0 ,v_1 ,v_2]$, and then we can write the function of line: 
$$ 
f(x)=\left\{
\begin{aligned}
x & = & \ pl_0 + v_0 *t \\
y & = & \ pl_1 + v_1 *t  \\
z & = & \ pl_2 + v_2 *t 
\end{aligned}
\right.
$$

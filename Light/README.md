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
In the class of the plane, we already have a point $po = [pp_0 ,pp_1 ,pp_2]$ in the plane, and the normal vector  $\vec{n} = [n_0 ,n_1 ,n_2]$, we know all the vector in plane is vertical to the normal vector: $\vec{n} \cdot \vec{x1}= 0 $, and $\vec{x1} = [x - pp_0 ,y - pp_1 ,z - pp_2]$. so we get the function:
$$ n_0 * (x - pp_0) + n_1 * (y - pp_1) + n_2 * (z - pp_2) = 0 $$ 
and with the function of light and plane we can get:
$$t = \frac{n_0*(pp_0-pl_0)+n_1*(pp_1-pl1)+n_3*(pp_2-pl_2)}{n_0*v_0+n_1*v_1+n_2*v_2} $$
then we can get the cross point $P$.
### Fun(CaTdir)
we have the function for calculate the refracted light:
$$\vec{t} = \vec{n} \times \vec{a}\times \vec{n}\cdot n_1/ n_2 + \sqrt{ \left | \vec{a}\right |^{2} - \left | \vec{n}  \times \vec{a}\times \vec{n}\right |^{2} } \cdot \vec{n} $$
and the vector n should be meet the following conditions:$  \vec{a} \cdot  \vec{n} >0 $

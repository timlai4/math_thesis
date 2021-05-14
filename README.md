# Math

This repository hosts the scripts used in my dissertation, titled "Classification of Sato-Tate Subgroups of U(3)" defended and approved on April 26, 2021, in satisfaction of the requirements for my Ph.D. degree at Indiana University, Bloomington, awarded on May 7, 2021. 

## Overview of scripts

In the paper, there are several places where a computer search for rational elements was used. There were instances in both the case when the Hodge circle was of the first type and of the second type (scalar embedding). 
For the former, a computer search was conducted in the cyclic case. 
First, I searched for rational elements under the tensor square character, using https://github.com/timlai4/math/blob/master/diagonal_elements.py
Next, using the general rationality condition for any irreducible character, I checked these putative elements to see if they satisfied general rationality using https://github.com/timlai4/math/blob/master/rational_elements.py
In these early versions of the scripts, I manually changed the hardcoded parameters, such as order and generators of the multiplicative cyclic groups. 

All the scripts are doing the same thing: namely given some set corresponding to the exponents, checking whether it is stable under Galois automorphisms. 
However, the computer search was more extensive in the scalar embedding case and therefore, necessitated significant updates to the scripts. 
https://github.com/timlai4/math/blob/master/scalar_diagonal_elements.py generates the list of possible groups for case C (Table 3) as well as the diagonal elements for case D. 
To classify the nondiagonal elements, https://github.com/timlai4/math/blob/master/D_final.py picks up where the previous script left off. 
Finally, to remove redundancies, we used GAP and https://github.com/timlai4/math/blob/master/GAP_inputs.py gives the necessary commands to input into GAP verbatim. 

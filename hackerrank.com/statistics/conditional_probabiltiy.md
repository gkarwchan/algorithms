# Problem

Suppose a family has 2 children, one of which is a boy. What is the probability that both children are boys?

# Solution

### Simple approach

the whole sample space: 
{BB, BG, GB, GG}

As one of them already a boy, so the samples that has a boy are one of these: { BB, GB, GB }

ρ(BB) = 1 / 3


### Mathematical approach

let's try Bayes thorem

ρ(BB | B) = (ρ(B | BB) * ρ(BB)) / ρ(B) 

where:

ρ(B|BB) is the probability of one child being a boy if both are boys 
ρ(B) is the probability of at least one child being a boy

ρ(B | BB) = 1
ρ(B) = ρ(BB) + ρ(BG) + ρ(GB) = 1/4 + 1/4 + 1/4  = 3/4

ρ(BB) = 1/4


description:
ρ(BB|B) = 1/4 / 3/4 = 1/3

probability the second is boy if the first one is boy: ρ(BB | B)

1. the probability if one child is boy if two are boys is : ρ(B | BB) = 1
2. the probability of two are boys is: ρ(BB)  = 1/4

ρ(BB | B) = ρ(B| BB) * ρ(BB)




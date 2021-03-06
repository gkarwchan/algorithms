# Basic Probability

ρ(A) = Number of favorable outcomes / Total number of outcomes
ρ(Aᶜ) = probability of that event not occur

```
ρ(A) + ρ(Aᶜ) = 1 = Sample space (S)
```
# Compound events
A compound event is a combination of 2 or more simple events.  

* **A∪B** : denotes the occurrence of either A or B.  
* **A∩B** : denotes the occurrence of A and B together.  

## Mutually exclusive

A and B are mutually exclusive (or disjoint) if they have no events in common.  
```
A∩B = 0
```
example:
the probability of getting 2 And 6 when we role a dice is impossible.
```
ρ(2 ∩ 6) = 0
```

the probability of the union of disjoint events is the sum of the events' individual probabilities.

```
ρ(A∪B) = ρ(A) + ρ(B)
```
the probability of the occurrence of any of 2 disjoint events is the sum of the probability of those individual events:
```
ρ(A or B) = ρ(A) + ρ(B)
```

## Collectively exhaustive
Two events are collectively exhaustive if their union covers all events in the sample space.

```javascript 
ρ(A) + ρ(B) = 1
A ∪ B = S   // (sample space)
```
example probability when we role a dice to get 2 or 6:
```
ρ(2 or 6) = ρ(2) + ρ(6)
ρ(2 ∪ 6) = 1/6 + 1/6 = 1/3
```


# Conditional Probability

Conditional probability is the probability of an event occurring, assuming that one or more other events have already occurred.  
There are two different scenarios:  

1. the events are dependent.
2. the events are independent.

A and B are considered to be independent if A has no effect on the probability of event B.  

#### Symbol denotes
We express that as `ρ(B | A)`, as the probability of event B, assuming the A already occurred.

### The events are independent
```
ρ(B | A) = ρ(B).
```

### The events are dependents
The probability of both events is the product of the probabilities for each event.  
We can express that as: `ρ(A and B)` or `ρ(A ∩ B)`

```javascript 
ρ(A ∩ B) = ρ(A) * ρ(B)
```

If Event A and B are not independent, then we must consider the probability of that both events occur, we call that the **intersection** of events:  
```
ρ(A∩B) = ρ(B | A) * ρ(A).
```
We can use the above definition to find the conditional probability by dividing the probability of the intersection of the two by the probability of the event that is assumed to have already occurred:
```
ρ(B|A) = ρ(A∩B) / ρ(A)
```

### Bayes' Thorem:
```
ρ(A | B) = (ρ(B | A) * ρ(A)) / ρ(B) 
         = (ρ(B | A) * ρ(A)) / ((ρ(B | A) * ρ(A)) + ρ(B | Aᶜ) * ρ(Aᶜ))
```
## Question 1:

If the probability of student A passing the exam is 2/7, and the probability of student B failing the exam is 3/7, then find the probability of at least one student pass the exam.  

```
ρ(A) = 2/7, ρ(Bᶜ) = 3/7

ρ(B) = 4/7
```
there are four possibilities: 

1. Both A and B pass the exam: A∩B
2. Both A and B fail the exam: Aᶜ∩Bᶜ
3. A passes and B fail: A∩Bᶜ
4. B passes and A fail: Aᶜ∩B

#### Approach 1:

Because the events are independent then:  
```
ρ(A∩B) = ρ(A) . ρ(B) = (2/7) * (4/7) = 8/49
```
probability of one student pass the exam: ρ(A∪B)
```
ρ(A∪B) = ρ(A) + ρ(B) - ρ(A∩B) = ρ(A) + ρ(B) - ρ(A) . ρ(B)

ρ(A∪B) = (2/7) + (4/7) - 8/49 = 34 / 49
```
#### Approach 2:

Find the probability of event 2 where both fail the exam and subtract from 1:
```
ρ(A∪B) = 1 - ρ(Aᶜ) . ρ(Bᶜ) = 1 - (5/7) * (3/7) = 34/49
```

## Question 2:

Historical data shows that it has only rained 5 days per year in the desert. A meteorologist predicts that it will rain.

* when it actually rains, the meteorologist correctly predicts rain 90%
* when it doesn't rain the meteorologist incorrectly predicts rain 10% of the time.

Find the probability that it will rain.

Solution:  
Event R: it rains today ρ(R) = 5/365 = 1/73
Event Rᶜ: it won't rain ρ(Rᶜ) = 360/365 = 72/73
Event M: the meteorologist predicted the rain:
ρ(M | R) = 9/10
ρ(M | Rᶜ) = 1/10

We want to calculate ρ(R | M)

```
ρ(R | M) = (ρ(M | R) * ρ(R)) / ((ρ(M | R) * ρ(R)) + ρ(M | Rᶜ) * ρ(Rᶜ))

ρ(R | M) = (9/10 * 1/73) / ((9/10 * 1/73) + (1/10 * 72/73) = (9/730) / (9/730 + 72/730) = 9 / 81 = 1 / 9
```
# Permutation

Permutation is the number of scenarios or possibilities for different input.

example:

> How many ways you can seat 5 people in 5 chairs?  
> the answer is : 5 * 4 * 3 * 2 * 1  
> How many ways you can seat 5 people in 3 chairs:
> the answer is: 5 * 4 * 3

### Permutation formula:
```python
permutation(n,r) = n! / (n-r)!
ρ(n, r) = nρr = n! / (n -r)! # if order is important

ρ(n, r) = nρr = n! / (n -r)! / r! # if order is important
```

#### example 1:  
To put 6 people in 3 chairs.
```python
ρ(6, 3) = 6! / 3! = 120 # if order is important
ρ(6, 3) = 6! / 3! / 3! = 20 # if order is important
```

#### example 2:
4 poeple shaking hands. How many possibilities.  
It is about 4 people in group of 2.  

```
ρ(4, 2) = 4! / 2! / 2! = 6
```

# Permutations, counting and combinations

#### example 1:
Find the possibility of flipping exactly 2 heads out of 3 flipps.  

Total number = 2**3 = 8
Number of exactly 2 heads = 3 = (2 + 1) = ~∑ⁿ⁻¹ n
Propability = 3/8

#### example 3:
Club of 9 peopel want to choose a board of three officers: President, Vice President, and Secretary.  

Total number of possibilities = 9! / (9-3)! = 504

#### example 4:
Card deck of 36 unique cards (from 1-9). What is the probability of getting 4 Aces.

ρ(all 4 aces in 9 cards) = # of uniques ways that can happend / total # of hands

ρ(total arrangement of 9 cards) = 36! / ((36-9)! * 9!)

ρ(# of ways to get 4 aces) = 4 aces and ρ(5 other cards) = (36 - 4)! / ((36 - 9)! * 5!)

ρ(4 aces) = ((36 - 4)! / ((36 - 9)! * 5!)) / (36! / ((36-9)! * 9!))
ρ(4 aces) = ((36 - 4)! / ((36 - 9)! * 5!)) * ((36-9)! * 9!) / 36!) = 2 / 935


# Formulas

∑ⁿ⁻¹ k = (n * (n - 1)) / 2
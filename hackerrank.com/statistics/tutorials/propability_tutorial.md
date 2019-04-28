# Basic Probability

ρ(A) = Number of favorable outcomes / Total number of outcomes
ρ(Aᶜ) = probability of that event not occur

```
ρ(A) + ρ(Aᶜ) = 1 = Sample space (S)
```
# Compound events
A compound event is a combination of 2 or more simple events.  

* **A∪B** : denotes the occurrence of either A or B.  
* **A∪B** : denotes the occurrence of A and B together.  

## Mutually exclusive

A and B are mutually exclusive if they have no events in common.  
```
A∩B = 0
```

the propability of any of 2 events occurring is the union of events `(∪)`
if they are mutually exclusive then 

```javascript 
ρ(A) + ρ(B) = 1
A + B = S   // (sample space)
```

# Conditional Probability

Conditional probability is the probability of an event occuring, assuming that one or more other events have already occured.  
There are two different scenarios:  

1. the events are dependent.
2. the events are independent.

A and B are considered to be independent if A has no effect on the probability of event B.  

#### Symbol denotes
We express that as `ρ(B | A)`, as the probability of event B, assuming the A already occured.

### The events are independent
```
ρ(B | A) = ρ(B).
```

### The events are dependents
If Event A and B are not independent, then we must consider the probability of that both events occur, we call that the **Intersection** of events:  
```
ρ(A∩B) = ρ(B | A) * ρ(A).
```
We can use the above definition to find the conditional probability by dividing the probability of the intersection of the two by the probability of the event that is assumed to have already occured:
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



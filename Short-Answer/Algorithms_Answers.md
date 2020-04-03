#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

a)  
~~~
python   
a)  a = 0                       
    while (a < n * n * n):       
      a = a + n * n             
~~~

**O(n)** <br>
**Reason:** <br>
`a = 0` is O(1).<br>  `while (a < n*n*n):` is O(n).<br>  `a = a + n * n` is O(1).<br>
I tried removing like terms, but that's high school / college math, and I'm not too confident on that.
But if I try to get the Big O for each line, the most complext one is O(n) -- and there aren't any nested for loops to increase complexity.  So O(n) is my answer.

b)  
~~~
b)  sum = 0                   
    for i in range(n):         
      j = 1
      while j < n:
        j *= 2
        sum += 1
~~~

**O(n)** <br>
**Reason:** The loop will loop through the range (which is n); so it's O(n).  It's a linear function.

c)  
~~~
c)  def bunnyEars(bunnies):     
      if bunnies == 0:
        return 0

      return 2 + bunnyEars(bunnies-1)
~~~

**O(n)** <br>
**Reason:** The bunnies are incremented by two in each recursion. So that hints that this is a linear function. That tips us off that this is O(n) 

## Exercise II

Suppose that you have an n-story building and plenty of eggs. Suppose also that an egg gets broken if it is thrown off floor f or higher, and doesn't get broken if dropped off a floor less than floor f. Devise a strategy to determine the value of f such that the number of dropped + broken eggs is minimized.

Write out your proposed algorithm in plain English or pseudocode AND give the runtime complexity of your solution.

**ANSWER**:
(Cheating a bit, using Sprint 3 knowledge on this Sprint 2 content)
- The floors are sorted, and it always goes up by +1 (floor).
- Given the bullet point above, a binary search makes sense.
- We get an idea on the total number of floors.  Binary search works by dividing n // 2. 
    - create a current_floor tracker
    - n//2 gives us midpoint.  
    - We check outcome: does egg break, or does it survive unbroken?
    - If broken, we do another another n//2 on our current_floor (so if we have 100 floors, our prev. current_tracker was 50, and current_tracker now at 25)
    - If unbroken, we mark it as such, ... and go above? (*some confusion on my end here, finish thought process later*)
- So we'd continue this until the egg doesn't break upon initial drop -- 
    - and then we go up one (*my initial confusion was whether we'd do halving of floors _upwards_ or not*)

*Originally I thought that dropping an egg from each floor, starting at Floor 0 would make the most sense.
But then realized that we have a limited supply of eggs; and if we have a skyscraper, that wouldn't work.

**Runtime Complexity**: O(log n)


SCRATCH NOTES: Delete later

```python   
a)  a = 0                       O(1)
    while (a < n * n * n):      # O(n)  
      a = a + n * n             
```


```
b)  sum = 0                     O(1)
    for i in range(n):          # O(n)
      j = 1
      while j < n:
        j *= 2
        sum += 1
```

```
c)  def bunnyEars(bunnies):     # O(n)
      if bunnies == 0:
        return 0

      return 2 + bunnyEars(bunnies-1)
```
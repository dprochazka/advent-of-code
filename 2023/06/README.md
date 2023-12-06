# Mathematical approach

Here is how I arrived at the solution mathematically.

Let $T$ be the time limit of the race and $R$ the record distance. The distance traveled in the boat race is
$$
d(t) = (T-t) \times t = - t^2 + T t,
$$
where $t$ is the time spent holding the button in the beggining of the race.

To beat the record, $d(t) \geq R$. This leads us to the following inequality:
$$
t^2 - Tt + R \leq 0.
$$

The left hand side of this inequality is a quadratic function, which means we can find the discriminant $D = T^2 - 4R$ and apply it to the formula for when the graph intersects zero:
$$
x_{1,2} = \tfrac{1}{2} \left( T \pm \sqrt{D} \right) = \tfrac{1}{2} \left( T \pm \sqrt{T^2 - 4R} \right)
$$

The set of whole number times when we beat the record $R$ has a lower limit of $\lceil x_1 \rceil$ and upper limit of $\lfloor x_2 \rfloor$. The number of ways to win is $\lfloor x_2 \rfloor - \lceil x_1 \rceil + 1$.
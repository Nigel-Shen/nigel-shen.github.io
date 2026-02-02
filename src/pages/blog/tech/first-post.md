---
layout: ../../../layouts/BlogPost.astro
title: "Solving the Heat Equation in Julia"
date: "2026-02-01"
description: "A look at high-performance finite difference methods using Julia's broadcasting capabilities."
tag: "Numerical Methods"
---

The heat equation is the "Hello World" of numerical PDEs. In this post, we will solve the 1D heat equation using a simple explicit finite difference scheme.

## The Mathematical Model

The equation is given by:

$$
\frac{\partial u}{\partial t} = \alpha \frac{\partial^2 u}{\partial x^2}
$$

Discretizing this using a central difference in space and forward difference in time gives us the update rule:

$$
u_i^{n+1} = u_i^n + \frac{\alpha \Delta t}{\Delta x^2} (u_{i+1}^n - 2u_i^n + u_{i-1}^n)
$$

## Implementation in Julia

One of the reasons I love **Julia** is that the code looks almost exactly like the math.

```julia
using Plots

# Parameters
α = 0.1   # Thermal diffusivity
dx = 0.01
dt = 0.0001
T = 1.0

# Grid
x = 0:dx:1
u = exp.(-100 * (x .- 0.5).^2) # Initial Gaussian pulse

# Time Stepping
const coeff = α * dt / dx^2

function solve_heat!(u, steps)
    u_new = copy(u)
    for t in 1:steps
        # Vectorized update (Fast!)
        u_new[2:end-1] = u[2:end-1] + coeff * (u[3:end] - 2u[2:end-1] + u[1:end-2])
        u .= u_new
    end
    return u
end

solve_heat!(u, 1000)
plot(x, u, label="t = $T")
```
import odesolverpy
import numpy as np


#------------------------------------ test functions (1/2 dimensions)---------------------------------------
def fun(t, y):
    a = 2
    dy = -a * y[0] * t
    return np.array([dy])

def analytic(t):
    y = np.exp(-t * t)
    return np.array([y])

def fun2(t, y):
   a = 4
   b = 3
   c = 0
   d = 2
   e = 3
   result = np.zeros(2)
   result[0] = -a*y[0] - b*y[1] + c*t
   result[1] = d*y[0] + e*y[1]
   return result

def analytic2(t):
   y = np.zeros(2)
   y[0] = -((np.exp(-3*t)*(np.exp(5*t)-6))/5)
   y[1] = 2*(np.exp(-3*t)*(np.exp(5*t)-1))/5
   return y
#--------------------------------------------------------------------------------------------------------

# Parameters definition
n1=70
n2=100

t_start = 0
t_start2=0

t_end = 10
t_end2=50

y0 = np.array([1.0])
y02= np.array([1.0, 0.0])

# Building of the instances to solve the Cauchy problem
solver = odesolverpy.ODESolverpy(fun, t_start, t_end, y0)
solver2 = odesolverpy.ODESolverpy(fun2, t_start2, t_end2, y02)

# Solving and plotting

solutionRK4=solver.solve(method='RK4', n=n1, filenametxt='./solutions_ode/RK4_solution.txt')
solutionRK4_dim2=solver2.solve(method='RK4', n=n2, filenametxt='./solutions_ode/RK4_solution_2dim.txt')
solver.plot_solution(solutionRK4, filenamepng='./plots_ode/RK4_solution.png')
solver2.plot_solution(solutionRK4_dim2, filenamepng='./plots_ode/RK4_solution_2dim.png')

solutioneuler=solver.solve(method='euler', n=n1, filenametxt='./solutions_ode/euler_solution.txt' )
solutioneuler_dim2=solver2.solve(method='euler', n=n2, filenametxt='./solutions_ode/euler_solution_2dim.txt')
solver.plot_solution(solutioneuler, filenamepng='./plots_ode/euler_solution.png')   
solver2.plot_solution(solutioneuler_dim2, filenamepng='./plots_ode/euler_solution_2dim.png')

solutionmidpoint=solver.solve(method='midpoint', n=n1, filenametxt='./solutions_ode/midpoint_solution.txt')
solutionmidpoint_dim2=solver2.solve(method='midpoint', n=n2, filenametxt='./solutions_ode/midpoint_solution_2dim.txt')
solver.plot_solution(solutionmidpoint, filenamepng='./plots_ode/midpoint_solution.png')
solver2.plot_solution(solutionmidpoint_dim2, filenamepng='./plots_ode/midpoint_solution_2dim.png')


print("\n-------------------------ACCURACY---------------------------------------------\n")

solver.accuracy_test(method='RK4', analytic_solution=analytic, n=n1)
solver2.accuracy_test(method='RK4', analytic_solution=analytic2, n=n2)

solver.accuracy_test(method='euler', analytic_solution=analytic, n=n1)
solver2.accuracy_test(method='euler', analytic_solution=analytic2, n=n2)

solver.accuracy_test(method='midpoint', analytic_solution=analytic, n=n1)
solver2.accuracy_test(method='midpoint', analytic_solution=analytic2, n=n2)

print("\n-------------------------EFFICIENCY---------------------------------------------\n")

solver.efficiency_test(method='RK4', n=n1)
solRK4pyt, solRK4pyY=solver.RK4scipy_solve( filenametxt='./solutions_ode/RK4_solution_scipy.txt')
solver.plot_py('RK4',solRK4pyt, solRK4pyY, filenamepng='./plots_ode/RK4_solution_scipy.png')

solver2.efficiency_test(method='RK4', n=n2)
solRK4pyt_2dim, solRK4pyY_2dim=solver2.RK4scipy_solve( filenametxt='./solutions_ode/RK4_solution_scipy_2dim.txt')
solver2.plot_py('RK4',solRK4pyt_2dim, solRK4pyY_2dim, filenamepng='./plots_ode/RK4_solution_scipy_2dim.png')

solver.efficiency_test(method='euler', n=n1)
soleulpyt, soleulpyY=solver.euler(n=n1)
solver.plot_py('euler',soleulpyt, soleulpyY, filenamepng='./plots_ode/euler_solution_py.png')

solver2.efficiency_test(method='euler', n=n2)
soleulpyt_2dim, soleulpyY_2dim=solver2.euler(n=n2)
solver2.plot_py('euler',soleulpyt_2dim, soleulpyY_2dim, filenamepng='./plots_ode/euler_solution_py_2dim.png')

solver.efficiency_test(method='midpoint', n=n1)
solmidpyt,solmidpyY=solver.midpoint(n=n1)
solver.plot_py('midpoint',solmidpyt,solmidpyY, filenamepng='./plots_ode/midpoint_solution_py.png')

solver2.efficiency_test(method='midpoint', n=n2)
solmidpyt_2dim,solmidpyY_2dim=solver2.midpoint(n=n2)
solver2.plot_py('midpoint',solmidpyt_2dim,solmidpyY_2dim, filenamepng='./plots_ode/midpoint_solution_py_2dim.png')    

print("\n-------------------------STABILITY---------------------------------------------\n")

solver.stability_test(method='RK4', perturbation=0.01, n=n1)
solver2.stability_test(method='RK4', perturbation=0.01, n=n2)

solver.stability_test(method='euler', perturbation=0.01, n=n1)
solver2.stability_test(method='euler', perturbation=0.01, n=n2)

solver.stability_test(method='midpoint', perturbation=0.01, n=n1)
solver2.stability_test(method='midpoint', perturbation=0.01, n=n2)

print("\n-------------------------CONVERGENCE---------------------------------------------\n")

solver.convergence_test(method='RK4', analytic_solution=analytic, n=n1)
solver2.convergence_test(method='RK4', analytic_solution=analytic2, n=n2)

solver.convergence_test(method='euler', analytic_solution=analytic, n=n1)
solver2.convergence_test(method='euler', analytic_solution=analytic2, n=n2)

solver.convergence_test(method='midpoint', analytic_solution=analytic, n=n1)
solver2.convergence_test(method='midpoint', analytic_solution=analytic2, n=n2)

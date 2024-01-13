import sys
sys.path.append('../build')
import odesolver
import numpy as np
import matplotlib.pyplot as plt
import time
import os 
from scipy.integrate import solve_ivp

if not os.path.exists("./plots"):
    os.mkdir("./plots")
if not os.path.exists("./solutions"):
    os.mkdir("./solutions")

class ODESolverpy:
    def __init__(self, fun, t_start, t_end, y0):
        self.c = odesolver.ODESolver(fun, t_start, t_end, y0)
        self.fun = fun
        self.t_start = t_start
        self.t_end = t_end
        self.y0 = y0

    def solve(self, method, n, filenametxt):
        if method == 'RK4':
            solution = self.c.RK4(n)
            with open(filenametxt, 'w') as f:
                f.write("t , y\n")
                for t, y in zip(solution.t, solution.Y):
                    f.write(str(t) + ' , ' + str(y) + '\n')
        elif method == 'midpoint':
            solution = self.c.midpoint(n)
            with open(filenametxt, 'w') as f:
                f.write("t , y\n")
                for t, y in zip(solution.t, solution.Y):
                    f.write(str(t) + ' , ' + str(y) + '\n')
        elif method == 'euler':
            solution = self.c.euler(n)
            with open(filenametxt, 'w') as f:
                f.write("t , y\n")
                for t, y in zip(solution.t, solution.Y):
                    f.write(str(t) + ' , ' + str(y) + '\n')
        else:
            raise ValueError("Invalid method. Choose between 'RK4', 'midpoint', or 'euler'.")
        return solution


    def RK4scipy_solve(self, filenametxt):
        t1=time.time()
        solution = solve_ivp(fun=self.fun, t_span=(self.t_start, self.t_end), y0=self.y0, method='RK45', dense_output=True)
        t2=time.time()
        print(f'RK4 implemented in python takes {t2-t1} seconds to run')
        
        t = np.linspace(self.t_start, self.t_end, 1000)
        y = solution.sol(t)
        
        with open(filenametxt, 'w') as f:
            f.write("t , y\n")
            for ti, yi in zip(t, y.T):
                f.write(f"{ti} , {', '.join(map(str, yi))}\n")

        return t, y
    
    def plot_RK4_py(self, t, y, filenamepng):
        plt.figure(figsize=(10, 6))
        for i in range(len(self.y0)):
            plt.plot(t, y[i], label=f"y{i}")

        plt.title(" RK4 - ODE Solution (SciPy)")
        plt.xlabel("Time")
        plt.ylabel("Solution")
        plt.legend(loc='best')
        if filenamepng:
            plt.savefig(filenamepng)
            print(f"Plot saved as {filenamepng}")
        else:
            plt.show()


    def euler(self, n):
        t1 = time.time()
        h = (self.t_end - self.t_start) / n
        t = np.linspace(self.t_start, self.t_end, n+1)
        Y = np.zeros((n+1, len(self.y0)))
        Y[0] = self.y0
        for j in range(n):
            k1 = self.fun(t[j], Y[j])
            Y[j+1] = Y[j] + h * k1
        t2 = time.time()
        print(f"Euler implemented in python run in: {t2-t1} seconds")
        return t, Y

    def plot_euler_py(self, t,Y , filenamepng):
        for i in range(len(Y[0])):
            plt.plot(t, Y[:, i], label=f'y{i+1}')
        plt.title("Euler solution")
        plt.xlabel('Time')
        plt.ylabel('Solution')
        plt.legend()
        if filenamepng:
            plt.savefig(filenamepng)
           # print(f"Plot saved as {filenamepng}")
        else:
            plt.show()
        
    def midpoint(self, n):
      t1 = time.time()
      h = (self.t_end - self.t_start) / n
      t = np.linspace(self.t_start, self.t_end, n+1)
      Y = np.zeros((n+1, len(self.y0)))
      Y[0] = self.y0
      for j in range(n):
          k1 = self.fun(t[j], Y[j])
          k2 = self.fun(t[j] + h / 2.0, Y[j] + 0.5 * h * k1)
          Y[j+1] = Y[j] + h * k2
          t2 = time.time()
      print(f"Midpoint implemented in python run in: {t2-t1} seconds")
      return t, Y
    

    def plot_midpoint_py(self, t, Y, filenamepng):
        for i in range(len(Y[0])):
            plt.plot(t, Y[:, i], label=f'y{i+1}')
        plt.title("Midpoint solution")
        plt.xlabel('Time')
        plt.ylabel('Solution')
        plt.legend()
        if filenamepng:
            plt.savefig(filenamepng)
        else:
            plt.show()

    
    def plot_solution(self, solution, filenamepng):
        plt.figure(figsize=(10, 6))
        for i in range(len(solution.Y[0])):
            plt.plot(solution.t, [y[i] for y in solution.Y], label="y")
            #repeat the loop for every dimension of the solution

        plt.title(f"Method - ODE Solution")
        plt.xlabel("Time")
        plt.ylabel("Solution")
        plt.legend(loc='best')
        if filenamepng:
            plt.savefig(filenamepng)
            print(f"Plot saved as {filenamepng}")
        else:
            plt.show()

    def accuracy_test(self,method, analytic_solution, n):
        if method == 'RK4':
            solution = self.c.RK4(n)  # Using RK4 method for accuracy test
        elif method == 'midpoint':
            solution = self.c.midpoint(n)
        elif method == 'euler':
            solution = self.c.euler(n)
        max_error = self.c.accuracy(solution, analytic_solution)
        print(f"Max Error of method {method}: {max_error}")


    def efficiency_test(self, method, n):
        time_taken = self.c.efficiency(method, n)
        print(f"Efficiency of {method}: {time_taken} seconds")

    def stability_test(self, method, perturbation,n):
        if method == 'RK4':
            solution = self.c.RK4(n)  # Using RK4 method for stability test
        elif method == 'midpoint':
            solution = self.c.midpoint(n)
        elif method == 'euler':
            solution = self.c.euler(n)
        stability = self.c.stability(method, solution, perturbation)
        print(f"Stability of {method} with perturbation {perturbation}: {stability}")

    def convergence_test(self, method, analytic_solution,n):
        if method == 'RK4':
            solution = self.c.RK4(n)
        elif method == 'midpoint':
            solution = self.c.midpoint(n)
        elif method == 'euler':
            solution = self.c.euler(n)
        convergence = self.c.convergence(solution, analytic_solution)
        print(f"Convergence of method {method}: {convergence}")




#------------------------------------ Test della classe ODESolverpy---------------------------------------
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

# Parametri del problema
n1=70
n2=100

t_start = 0
t_start2=0

t_end = 10
t_end2=50

y0 = np.array([1.0])
y02= np.array([1.0, 0.0])

# Creazione dell'istanza di ODESolverpy
solver = ODESolverpy(fun, t_start, t_end, y0)
solver2 = ODESolverpy(fun2, t_start2, t_end2, y02)

# Esempi di test

solutionRK4=solver.solve(method='RK4', n=n1, filenametxt='./solutions/RK4_solution.txt')
solutionRK4_dim2=solver2.solve(method='RK4', n=n2, filenametxt='./solutions/RK4_solution_2dim.txt')
solver.plot_solution(solutionRK4, filenamepng='./plots/RK4_solution.png')
solver2.plot_solution(solutionRK4_dim2, filenamepng='./plots/RK4_solution_2dim.png')


solutioneuler=solver.solve(method='euler', n=n1, filenametxt='./solutions/euler_solution.txt' )
solutioneuler_dim2=solver2.solve(method='euler', n=n2, filenametxt='./solutions/euler_solution_2dim.txt')
solver.plot_solution(solutioneuler, filenamepng='./plots/euler_solution.png')   
solver2.plot_solution(solutioneuler_dim2, filenamepng='./plots/euler_solution_2dim.png')

solutionmidpoint=solver.solve(method='midpoint', n=n1, filenametxt='./solutions/midpoint_solution.txt')
solutionmidpoint_dim2=solver2.solve(method='midpoint', n=n2, filenametxt='./solutions/midpoint_solution_2dim.txt')
solver.plot_solution(solutionmidpoint, filenamepng='./plots/midpoint_solution.png')
solver2.plot_solution(solutionmidpoint_dim2, filenamepng='./plots/midpoint_solution_2dim.png')


print("\n-------------------------ACCURACY---------------------------------------------\n")

solver.accuracy_test(method='RK4', analytic_solution=analytic, n=n1)
solver2.accuracy_test(method='RK4', analytic_solution=analytic2, n=n2)

solver.accuracy_test(method='euler', analytic_solution=analytic, n=n1)
solver2.accuracy_test(method='euler', analytic_solution=analytic2, n=n2)

solver.accuracy_test(method='midpoint', analytic_solution=analytic, n=n1)
solver2.accuracy_test(method='midpoint', analytic_solution=analytic2, n=n2)

print("\n-------------------------EFFICIENCY---------------------------------------------\n")

solver.efficiency_test(method='RK4', n=n1)
solRK4pyt, solRK4pyY=solver.RK4scipy_solve( filenametxt='./solutions/RK4_solution_scipy.txt')
solver.plot_RK4_py(solRK4pyt, solRK4pyY, filenamepng='./plots/RK4_solution_scipy_scipy.png')
solver2.efficiency_test(method='RK4', n=n2)
solRK4pyt_2dim, solRK4pyY_2dim=solver2.RK4scipy_solve( filenametxt='./solutions/RK4_solution_scipy_2dim.txt')
#solver2.plot_RK4_py(solRK4pyt, solRK4pyY, filenamepng='./plots/RK4_solution_scipy_2dim.png')

solver.efficiency_test(method='euler', n=n1)
soleulpyt, soleulpyY=solver.euler(n=n1)
solver.plot_euler_py(soleulpyt, soleulpyY, filenamepng='./plots/euler_solution_py.png')
solver2.efficiency_test(method='euler', n=n2)
soleulpyt_2dim, soleulpyY_2dim=solver2.euler(n=n2)
solver2.plot_euler_py(soleulpyt_2dim, soleulpyY_2dim, filenamepng='./plots/euler_solution_py_2dim.png')

solver.efficiency_test(method='midpoint', n=n1)
solmidpyt,solmidpyY=solver.midpoint(n=n1)
solver.plot_midpoint_py(solmidpyt,solmidpyY, filenamepng='./plots/midpoint_solution_py.png')
solver2.efficiency_test(method='midpoint', n=n2)
solmidpyt_2dim,solmidpyY_2dim=solver2.midpoint(n=n2)
solver2.plot_midpoint_py(solmidpyt_2dim,solmidpyY_2dim, filenamepng='./plots/midpoint_solution_py_2dim.png')    

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

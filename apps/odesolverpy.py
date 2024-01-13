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

    def plot_solution(self, solution, filenamepng):
        '''non toccare è quello di c++'''
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

    def plot_py(self, method , t,Y , filenamepng):
        if method == 'RK4':
            for i in range(len(self.y0)):
                plt.plot(t, Y[i], label=f"y{i}")

        elif method == 'midpoint' or method == 'euler':
            for i in range(len(Y[0])):
                plt.plot(t, Y[:, i], label=f'y{i+1}')
        else:
            raise ValueError("Invalid method. Choose between 'RK4', 'midpoint', or 'euler'.")       
        
        plt.title(f"Method {method} - ODE solution")
        plt.xlabel('Time')
        plt.ylabel('Solution')
        plt.legend()
        if filenamepng:
            plt.savefig(filenamepng)
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


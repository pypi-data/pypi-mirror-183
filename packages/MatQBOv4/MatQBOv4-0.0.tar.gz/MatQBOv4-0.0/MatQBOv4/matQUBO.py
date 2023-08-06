import numpy as np
import pyqubo
import dimod
import neal
from dwave.cloud import Client
import time

class MatQUBO:
    def __init__(self, input_name, number_of_variables, coef_objective_linear = None , coef_objective_quadratic = None, coef_equal_constraint_linear = None , coef_equal_constraint_quadratic = None,  coef_unequal_constraint_linear = None, coef_unequal_constraint_quadratic = None ,bias_equality_linear = 0 , bias_equality_quadratic = 0 , bias_unequality_linear = 0, bias_unequality_quadratic = 0, variable_type = 'BINARY', token = None, hard_penalty = True, solver_name = 'neal'):
        """
        this class use to solve BINARY and SPIN optimization problems
        problem:
            Minimize: c_o_l * x + x * c_o_q * x.T 
            Subject to: c_e_c_linear_linear_linear * x = bias_equality_linear (linear equal constraints)
                        c_u_c_linear * x <= bias_unequality_linear (linear unequality constraints)
                        where x is a vector of variables
        
        input_name: name of vector of variables like x
        number_of_variables: number of variables
        coef_objective: coefficient of objective function
        coef_equal_constraint: coefficient of equal constraints
        bias_equality_linear: bias of equal constraints
        coef_unequal_constraint_linear: coefficient of unequal constraints
        bias_unequality_linear: bias of unequal constraints
        variable_type: BINARY or SPIN
        token: token of your account in DWave (if you want to use DWaveCloudClient)
        hard_penalty: for solving problem in Quantum anneling, we must add unequality constraints to the objective function . if hard_penalty = True , we fine the solution with the minimum penalty. if not, we fine the solution with the minimum objective function value
        """
        self.token = token
        self.token = 'DEV-154f5f5ce1cf05b732906131cd2dc83452a8f92b' # temp . should be deleted
        self.name = input_name
        self.n = number_of_variables
        self.solver = solver_name
        self.vartype = variable_type
        self.variables = pyqubo.Array.create(f'{self.name}', shape=self.n, vartype=self.vartype)
        self.slack_variable_id = 0 # for creating slack variables for unequal constraints
        self.penalty = 1000 if hard_penalty else 2 # penalty for adding constraints to the objective function
        
        
        self.has_equal_constraint_linear = True if coef_equal_constraint_linear != None else False # check if there is equal constraints
        self.has_equal_constraint_quadratic = True if coef_equal_constraint_quadratic != None else False # check if there is equal constraints
        self.has_unequal_constraint_linear = True if coef_unequal_constraint_linear != None else False # check if there is unequal constraints
        self.has_unequal_constraint_quadratic = True if coef_unequal_constraint_quadratic != None else False # check if there is unequal constraints
        self.has_linear_objective = True if coef_objective_linear != None else False # check if there is linear objective function
        self.has_quadratic_objective = True if coef_objective_quadratic != None else False # check if there is quadratic objective function

        if self.has_equal_constraint_linear:
            self.c_e_c_linear = np.array(coef_equal_constraint_linear)
            self.bias_equality_linear = np.array(bias_equality_linear) if bias_equality_linear != 0 else np.zeros(self.c_e_c_linear.shape[0])
            ### check input ### 
            if self.c_e_c_linear.shape[0] != self.bias_equality_linear.shape[0]:
                raise ValueError('The number of equal constraints should be equal to the number of bias')
            if self.c_e_c_linear.shape[1] != self.n:
                raise ValueError('The number of variables should be equal to the number of coefficients in the equal constraints')
        if self.has_equal_constraint_quadratic:
            self.c_e_c_quadratic = np.array(coef_equal_constraint_quadratic)
            self.bias_equality_quadratic = np.array(bias_equality_quadratic) if bias_equality_quadratic != 0 else 0 #first version only one quadratic constraint
            ### check input ### 
            if self.c_e_c_quadratic.shape != (self.n,self.n):
                raise ValueError('The shape of the quadratic equal constraints coefficient should be equal to (number of variables , number of variables)')
        if self.has_unequal_constraint_linear:
            self.c_u_c_linear = np.array(coef_unequal_constraint_linear)
            self.bias_unequality_linear = np.array(bias_unequality_linear) if bias_unequality_linear != 0 else np.zeros(self.c_u_c_linear.shape[0])
            ### check input ### 
            if self.c_u_c_linear.shape[0] != self.bias_unequality_linear.shape[0]:
                raise ValueError('The number of unequal constraints should be equal to the number of bias')
            if self.c_u_c_linear.shape[1] != self.n:
                raise ValueError('The number of variables should be equal to the number of coefficients in the unequal constraints')
        if self.has_unequal_constraint_quadratic:
            self.c_u_c_quadratic = np.array(coef_unequal_constraint_quadratic)
            self.bias_unequality_quadratic = np.array(bias_unequality_quadratic) if bias_unequality_quadratic != 0 else 0
            ### check input ###
            if self.c_u_c_quadratic.shape != (self.n,self.n):
                raise ValueError('The shape of the quadratic unequal constraints coefficient should be equal to (number of variables , number of variables)')

        if self.has_linear_objective:
            self.c_o_l = np.array(coef_objective_linear)
            ## check input ##
            if len(self.c_o_l) != self.n:
                raise ValueError('The length of the linear objective function coefficient should be equal to the number of variables')
        if self.has_quadratic_objective:
            self.c_o_q = np.array(coef_objective_quadratic)
            ## check input ##
            if self.c_o_q.shape != (self.n,self.n):
                raise ValueError('The shape of the quadratic objective function coefficient should be equal to (number of variables , number of variables)')
        ### check input ### 
        if self.vartype != 'BINARY' and self.vartype != 'SPIN':
            raise ValueError('The variable type should be BINARY or SPIN')
        
        

    def objective_linear(self):
        if self.has_linear_objective:
            return sum(self.c_o_l[i] * self.variables[i] for i in range(self.n))
        else:
            return 0

    def objective_quadratic(self):
        if self.has_quadratic_objective:
            return sum(self.c_o_q[i,j] * self.variables[i] * self.variables[j] for i in range(self.n) for j in range(self.n))
        else:
            return 0
    def objective(self):
        return self.objective_linear() + self.objective_quadratic()

    def add_equal_constraint_linear(self, coeffient, bias,label = None):
        return pyqubo.Constraint((sum(coeffient[i] * self.variables[i] for i in range(self.n)) - bias) ** 2 , label=f'equal_linear_constraint_{label}')

    def add_equal_constraint_quadratic(self, coeffient, bias, label = None):
        return pyqubo.Constraint((sum(coeffient[i,j] * self.variables[i] * self.variables[j] for i in range(self.n) for j in range(self.n)) - bias) ** 2 , label=f'equal_quadratic_constraint_{label}')
    def add_unequal_constraint_linear(self, coeffient, bias, coef_slack , label = None):
        slack_varible = pyqubo.Array.create(f'{self.name}_slack_{self.slack_variable_id}', shape=1, vartype='BINARY') #slack variable i think should be positive 
        slack_varible = slack_varible[0]
        self.slack_variable_id += 1
        return pyqubo.Constraint((sum(coeffient[i] * self.variables[i] for i in range(self.n)) - bias + coef_slack * slack_varible) ** 2 , label='unequal_constraint')
    def add_unequal_constraint_quadratic(self, coeffient, bias, coef_slack , label = None):
        slack_varible = pyqubo.Array.create(f'{self.name}_slack_{self.slack_variable_id}', shape=1, vartype='BINARY') #slack variable i think should be positive
        slack_varible = slack_varible[0]
        self.slack_variable_id += 1
        return pyqubo.Constraint((sum(coeffient[i,j] * self.variables[i] * self.variables[j] for i in range(self.n) for j in range(self.n)) - bias + coef_slack * slack_varible) ** 2 , label='unequal_constraint')

    def add_constraints(self, penalty):
        if self.has_equal_constraint_linear:
            for row,i in zip(self.c_e_c_linear,range(len(self.c_e_c_linear))):
                self.H += penalty * self.add_equal_constraint_linear(row, self.bias_equality_linear[i], label = 'i')
        if self.has_equal_constraint_quadratic:
            self.H += penalty * self.add_equal_constraint_quadratic(self.c_e_c_quadratic, self.bias_equality_quadratic, label = 'i')
        if self.has_unequal_constraint_linear:
            for row,i in zip(self.c_u_c_linear,range(len(self.c_u_c_linear))):
                self.H += penalty * self.add_unequal_constraint_linear(row, self.bias_unequality_linear[i], coef_slack = 1, label = 'i')
        if self.has_unequal_constraint_quadratic:
            self.H += penalty * self.add_unequal_constraint_quadratic(self.c_u_c_quadratic, self.bias_unequality_quadratic, coef_slack = 1, label = 'i')
        return self.H

    def create_model(self, penalty = 1000):
        self.H = None
        self.H = self.objective()
        self.H = self.add_constraints(penalty)
        self.model = self.H.compile()
        if self.vartype == 'BINARY':
            self.compiled_model = self.model.to_qubo()
        else:
            self.compiled_model = self.model.to_ising()
        return self.model
    
    def solve(self, solver = 'neal', num_reads = 1000, num_sweeps = 1000, penalty = None):
        penalty = self.penalty if penalty is None else penalty
        self.create_model(penalty)
        if self.vartype == 'BINARY': #binary variables
            if solver == 'neal':
                sampler = neal.SimulatedAnnealingSampler()
                self.response = sampler.sample_qubo(self.compiled_model[0], num_reads=num_reads)
            elif solver == 'tabu':
                sampler = dimod.TabuSampler()
                self.response = sampler.sample_qubo(self.compiled_model[0], num_reads=num_reads)
            elif solver == 'exact':
                sampler = dimod.ExactSolver()
                self.response = sampler.sample_qubo(self.compiled_model[0])
            elif solver == 'simulated_annealing':
                sampler = dimod.SimulatedAnnealingSampler()
                self.response = sampler.sample_qubo(self.compiled_model[0], num_reads=num_reads)
            elif solver == 'sqa':
                sampler = dimod.SQASampler()
                self.response = sampler.sample_qubo(self.compiled_model[0], num_reads=num_reads)
            elif solver == 'hybrid':
                sampler = dimod.HybridSampler()
                self.response = sampler.sample_qubo(self.compiled_model[0], num_reads=num_reads)
            elif solver == 'dwave-cloud-client':
                clinet = Client.from_config(token = self.token)
                solver = clinet.get_solver('hybrid_binary_quadratic_model_version2')
                bqm = dimod.BinaryQuadraticModel(self.model.to_bqm(), "BINARY")
                computation = solver.sample_bqm(bqm,time_limit = 1000)
                while not computation.done():
                    print('Waiting for results...')
                    time.sleep(10)
                sampleset = computation.result()
                decoded_samples = self.model.decode_sampleset(sampleset) ### MY API EXPIRED . I CANT TEST IT
                best_sample = min(decoded_samples, key=lambda x: x.energy).sample ### MY API EXPIRED . I CANT TEST IT
                soloution = self.get_solution(best_sample)
                return soloution, self.check_solution(soloution[0], penalty)
            else:
                raise ValueError('Please choose a valid solver')
        else:
            if solver == 'neal':
                sampler = neal.SimulatedAnnealingSampler()
                self.response = sampler.sample_ising(self.compiled_model[0], self.compiled_model[1], num_reads=num_reads)
            elif solver == 'tabu':
                sampler = dimod.TabuSampler()
                self.response = sampler.sample_ising(self.compiled_model[0], self.compiled_model[1], num_reads=num_reads)
            elif solver == 'exact':
                sampler = dimod.ExactSolver()
                self.response = sampler.sample_ising(self.compiled_model[0], self.compiled_model[1])
            elif solver == 'simulated_annealing':
                sampler = dimod.SimulatedAnnealingSampler()
                self.response = sampler.sample_ising(self.compiled_model[0], self.compiled_model[1], num_reads=num_reads)
            elif solver == 'sqa':
                sampler = dimod.SQASampler()
                self.response = sampler.sample_ising(self.compiled_model[0], self.compiled_model[1], num_reads=num_reads)
            elif solver == 'hybrid':
                sampler = dimod.HybridSampler()
                self.response = sampler.sample_ising(self.compiled_model[0], self.compiled_model[1], num_reads=num_reads)
            elif solver == 'dwave-cloud-client': #cloud D-Wave solver
                clinet = Client.from_config(token = self.token)

                solver = clinet.get_solver('hybrid_binary_quadratic_model_version2') # temp . need to change to find itself

                bqm = dimod.BinaryQuadraticModel(self.model.to_bqm(), "SPIN")
                computation = solver.sample_bqm(bqm,time_limit = 1000)
                while not computation.done():
                    print('Waiting for results...')
                    time.sleep(10)
                sampleset = computation.result()
                decoded_samples = self.model.decode_sampleset(sampleset)
                best_sample = min(decoded_samples, key=lambda x: x.energy).sample ### MY API EXPIRED . I CANT TEST IT
                soloution = self.get_solution(best_sample)
                return soloution , self.check_solution(soloution[0], penalty) ### MY API EXPIRED . I CANT TEST IT
            else:
                raise ValueError('Please choose a valid solver')
        sampleset = self.response
        decoded_samples = self.model.decode_sampleset(sampleset)
        best_sample = min(decoded_samples, key=lambda x: x.energy).sample
        soloution = self.get_solution(best_sample)
        return soloution , self.check_solution(soloution[0],penalty)
    
    def get_solution(self,sample_set):
        energy = 0
        keys = list(sample_set.keys())
        keys = [key for key in keys if 'slack' not in key and "*" not in key]
        values = [sample_set[key] for key in keys]
        if self.has_linear_objective:
            energy = sum(self.c_o_l[i] * values[i] for i in range(self.n))
        if self.has_quadratic_objective:
            energy += sum(self.c_o_q[i,j] * values[i] * values[j] for i in range(self.n) for j in range(self.n))
        solution = dict(zip(keys, values))
        print(f'Variables: {values}')
        print(f'Objective Value: {energy}')
        return solution, energy
    
    def check_solution(self, solution,penalty): #check constraints satisfication
        if penalty == 0 : #this case we have no constraints
            print("Soloution is Valid")
            return True
        print(" ~~~~~~~~ Checking solution ~~~~~~~~")
        solution = list(solution.values())
        satisfied_equal_linear = True
        satisfied_equal_quadratic = True
        satisfied_unequal_linear = True
        satisfied_unequal_quadratic = True
        if self.has_equal_constraint_linear:
            for row,i in zip(self.c_e_c_linear,range(len(self.c_e_c_linear))):
                equality = sum(row[i] * solution[i] for i in range(self.n)) - self.bias_equality_linear[i]
                if abs(equality) > 1e-6:
                    print(f'Linear Equality constraint {i} is not satisfied')
                    satisfied_equal_linear = False
        if self.has_equal_constraint_quadratic:
            equality = sum(self.c_e_c_quadratic[i,j] * solution[i] * solution[j] for i in range(self.n) for j in range(self.n)) - self.bias_equality_quadratic
            if abs(equality) > 1e-6:
                print(f'Quadratic Equality constraint {i} is not satisfied')
                satisfied_equal_quadratic = False
        if self.has_unequal_constraint_linear:
            for row,i in zip(self.c_u_c_linear,range(len(self.c_u_c_linear))):
                inequality = sum(row[i] * solution[i] for i in range(self.n)) - self.bias_unequality_linear[i]
                if inequality > 0:
                    print(f'Inequality constraint {i} is not satisfied')
                    satisfied_unequal_linear = False
        if self.has_unequal_constraint_quadratic:
            inequality = sum(self.c_u_c_quadratic[i,j] * solution[i] * solution[j] for i in range(self.n) for j in range(self.n)) - self.bias_unequality_quadratic
            if inequality > 0:
                print(f'Inequality constraint {i} is not satisfied')
                satisfied_unequal_quadratic = False
        if satisfied_equal_linear and satisfied_unequal_linear and satisfied_equal_quadratic and satisfied_unequal_quadratic:
            print("Soloution is Valid")
            return True
        else:
            print("Soloution is not Valid")
            return False
            
    def solve_with_different_penalty(self, penalties = [1e10,1e5,1e3,1e1]):
        if self.has_equal_constraint_linear or self.has_equal_constraint_quadratic or self.has_unequal_constraint_linear or self.has_unequal_constraint_quadratic:
            print("Solving with different penalties")
            for penalty in penalties:
                print(f'~~~~~ Solve Problem with Penalty = {penalty} ~~~~~')
                soloution, valid = self.solve(penalty = penalty)
                if valid:
                    return soloution, valid
            print("No valid solution found maybe empty feasible region | result with default penalty")
            return self.solve(penalty = self.penalty)




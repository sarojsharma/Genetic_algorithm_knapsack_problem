
import numpy as np
import random



class Genetic_Algorithm(object):

    def __init__(self):
        
        self.no_of_population = 4
        self.no_of_gene = 4
        self.value = np.array([6,7,8,11])
        self.weight = np.array([3,4,3,5])
        self.max_weight = 10
        self.num_of_parentmating = 2
        self.fit = []
        self.mate = []
        
    
        
        self.population = np.random.randint(2,size = (self.no_of_population,self.no_of_gene))        #chromosome encoding
        print("\n Initial population",self.population)
   
        
        
        
    def fitness(self):
        
        for i in range(self.no_of_population):
            
            mul1 = np.multiply(self.population[i],self.weight)        # Ci*Wi
            summation = np.sum(mul1)
            
            if(summation <= self.max_weight):                                 
                mul2 = np.multiply(self.population[i],self.value)     # Ci.Vi
                fit = np.sum(mul2)
            else:
                fit = 0
                
            self.fit.append(fit)
            
        print("\nfitness value",self.fit)
        tf = np.sum(self.fit)
        print("total fitness",tf)
                
                
            
    def selection(self):
        
       
       for x in range(4):
            a = np.argmax(self.fit)
            b = self.population[a]
            self.mate.append(b)
            self.fit[a] = 0
       print("\nparents seleceted based on fitness value")
       print("parent1",self.mate[0])
       print("parent2",self.mate[1])
       
       
            
          
    def crossover(self):
        
       print("\noffspring produced after twopoint crossover") 
       self.offspring1 = np.array([self.mate[0][0],self.mate[1][1],self.mate[1][2],self.mate[0][3]])     #two point crossover
       print("offspring1",self.offspring1)
       self.offspring2 = np.array([self.mate[1][0],self.mate[0][1],self.mate[0][2],self.mate[1][3]])
       print("offspring2",self.offspring2)


    def mutation(self):
        
        random_value1 = np.random.randint(0,2,1)
        random_value2 = np.random.randint(0,2,1)
        position1 = np.random.randint(0,4,1)
        position2 = np.random.randint(0,4,1)
        self.offspring1[position1] = random_value1
        self.offspring2[position2] = random_value2
        print("\noffspring after mutation")
        print("offspring1",self.offspring1)
        print("offspring2",self.offspring2)
        self.population = np.array([self.mate[0],self.mate[1],self.offspring1,self.offspring2])
        print("\nnew generation")
        print(self.population)
        self.fit = []
        
        
 


if __name__=="__main__":

    print("SAROJ SHARMA 73071 ((WELCOME))")
   
    ga = Genetic_Algorithm()
    for x in range(100):
       ga.fitness()
       ga.selection()
       ga.crossover()
       ga.mutation()
       
    print("My Github link is http://www.github.com/sarojsharma")
    print("No of population taken is 4")
   

        
    

import numpy as np
import matplotlib.pyplot as plt
from IPython.display import clear_output
import time

class GoldenSectionAlg:
    def __init__(self,x):
        self.x = x

    def func_fx(self,x):
        x_val = x
        fx=np.sin(x_val)
        # print(fx)
        return fx

    def check_pos(self,x1,x2):
        if x2<x1:
            label='right'
        else:
            label=''
        return label

    def update_interior(self,xl,xu):
        d=((np.sqrt(5)-1)/2)*(xu-xl)
        x1=xl+d
        x2=xu-d
        return x1,x2

    def find_max(self,xl,xu,x1,x2,label):
        fx1=self.func_fx(x1)
        fx2=self.func_fx(x2)
        if fx2>fx1 and label=='right':
            xl=xl
            xu=x1
            new_x=self.update_interior(xl,xu)
            x1=new_x[0]
            x2=new_x[1]
            xopt=x2
        else:
            xl=x2
            xu=xu
            new_x=self.update_interior(xl,xu)
            x1=new_x[0]
            x2=new_x[1]
            xopt=x1
        return xl,xu,xopt

    def find_min(self,xl,xu,x1,x2,label):
        fx1=self.func_fx(x1)
        fx2=self.func_fx(x2)
        if fx2>fx1 and label=='right':
            xl=x2
            xu=xu
            new_x=self.update_interior(xl,xu)
            x1=new_x[0]
            x2=new_x[1]
            xopt=x1
        else:
            xl=xl
            xu=x1
            new_x=self.update_interior(xl,xu)
            x1=new_x[0]
            x2=new_x[1]
            xopt=x2
        return xl,xu,xopt

    def plot_graph(self,xl,xu,x1,x2):
        clear_output(wait=True)

        y=self.func_fx(self.x)
        # print(y)

        #plot sinus graph
        plt.plot(self.x,y)
        plt.plot([0,6],[0,0],'k')
        
        # print(x1)
        # print(self.func_fx(x1))
        #plot x1 point
        plt.plot(x1,self.func_fx(x1),'ro',label='x1')
        plt.plot([x1,x1],[0,self.func_fx(x1)],'k')
        
        #plot x2 point
        plt.plot(x2,self.func_fx(x2),'bo',label='x2')
        plt.plot([x2,x2],[0,self.func_fx(x2)],'k')
        
        #plot xl line
        plt.plot([xl,xl],[0,self.func_fx(xl)])
        plt.annotate('xl',xy=(xl-0.01,-0.2))
            
        #plot xu line
        plt.plot([xu,xu],[0,self.func_fx(xu)])
        plt.annotate('xu',xy=(xu-0.01,-0.2))
            
        #plot x1 line
        plt.plot([x1,x1],[0,self.func_fx(x1)],'k')
        plt.annotate('x1',xy=(x1-0.01,-0.2))
            
        #plot x2 line
        plt.plot([x2,x2],[0,self.func_fx(x2)],'k')
        plt.annotate('x2',xy=(x2-0.01,-0.2))
        
        #y-axis limit
        plt.ylim([-1.2,1.2])
        plt.show()

    def golden_search(self,xl,xu,mode,et):
        it=0
        e=1
        while e>=et:
            new_x=self.update_interior(xl,xu)
            x1=new_x[0]
            x2=new_x[1]
            fx1=self.func_fx(x1)
            fx2=self.func_fx(x2)
            label=self.check_pos(x1,x2)
            clear_output(wait=True)
            self.plot_graph(xl,xu,x1,x2) 
            plt.show()
            
            #SELECTING AND UPDATING BOUNDARY-INTERIOR POINTS
            if mode=='max':
                new_boundary=self.find_max(xl,xu,x1,x2,label)
            elif mode=='min':
                new_boundary=self.find_min(xl,xu,x1,x2,label)
            else:
                print('Please define min/max mode')
                break #exit if mode not min or max
            xl=new_boundary[0]
            xu=new_boundary[1]
            xopt=new_boundary[2]
            
            it+=1
            print ('Iteration: ',it)
            r=(np.sqrt(5)-1)/2 #GOLDEN RATIO
            e=((1-r)*(abs((xu-xl)/xopt)))*100 #Error
            print('Error:',e)
            time.sleep(1)
    

# x=np.linspace(0,6,100)

# gss = GoldenSectionAlg(x)

# gss.golden_search(0,6,'max',0.05)


#LCM function
def find_lcm(num1, num2): 
    if(num1>num2): 
        num = num1 
        den = num2 
    else: 
        num = num2 
        den = num1 
    rem = num % den 
    while(rem != 0): 
        num = den 
        den = rem 
        rem = num % den 
    gcd = den 
    lcm = int(int(num1 * num2)/int(gcd)) 
    return lcm 
    
#   Function for algorithm for rate scheduling   
def tasktable(task,num,lcm):
    timetable=[]
    for i in range(0,lcm):
        timetable.append(0)
    numsl=[]
    for x in range(0,len(task)):
        numsl.append(task[x][0]*(lcm/task[x][1]))
    print(numsl)
    print(timetable)
    if(sum(numsl)>lcm):
        print('Not possible to schedule')
        return 0
    else:
        timeperiods=[]
        for i in range(0,num):
            n=[]
            for a in range(0,lcm):
                if(a%task[i][1]==0):
                    n.append(a)
            timeperiods.append(n)
    for m in range(0,len(numsl)):
        while(numsl[m]>0):
            for k in range(0,len(timeperiods[m])):
                if(numsl[m]>0):
                    if(timetable[timeperiods[m][k]]==0):
                        timetable[timeperiods[m][k]]=m+1
                        numsl[m]=numsl[m]-1
                       
                    else:
                        try:
                           
                                for b in range(timeperiods[m][k],timeperiods[m][k+1]):
                                     if(numsl[m]>0):
                                         if(timetable[b]==0):
                                             timetable[b]=m+1
                                             numsl[m]=numsl[m]-1
                                             break
                        except:
                            if(numsl[m]>0):
                                timetable[b]=m+1
                                numsl[m]=numsl[m]-1
    print(timetable)     
    print(numsl)     
    return timetable
 
    
n=int(input("Enter number of tasks: "))
task=[]
print("Enter Execution time and Period of tasks")
for i in range(0,n):
 pair=[]
 inp1=input()
 c,t=map(int,inp1.split(','))
 pair.append(int(c))
 pair.append(int(t))
 task.append(pair)
task.sort(key=lambda x:x[1])
print(task)
u=0
num1 = task[0][1] 
num2 = task[1][1]
lcm = find_lcm(num1, num2) 
  
for i in range(2, len(task)): 
    lcm = find_lcm(lcm, task[i][1]) 
      
for i in range(0,n):
    u=u+(task[i][0]/task[i][1])

print('The utilization for give process is:'+str(u) )
if(u<1):
     if(u<=(n*((2**(1/n))-1))):
        print('Scheduling guaranteed to be possible as '+str(u)+'<='+str((n*((2**(1/n))-1))))
        tasktable(task,n,lcm)
     else:
        print('Scheduling may or may not be possible as '+str(u)+'>'+str((n*((2**(1/n))-1))) )
        tasktable(task,n,lcm)
else:
    print('Scheduling not possible as '+str(u)+' >1')
    

      

X=[]
fit=[]
ps=input("enter the population size")
ps=int(ps)
n=input("number of decision variables")
n=int(n)
for i in range(ps):
    x=[]
    for j in range(n):
        x.append(LB+(UB-LB)*rand())
    X.append(x)

for i in range(ps):
    fit.append(F(X[i]))
    
delta_index=fit.index(min(fit))
swarm=X[delta_index]
X_star=swarm

for i in range(ps):
    alpha=1
    x=[]
    for j in range(n):
        x[j]=X[i][j]+alpha*(X[i][j]-swarm[j])
        if(x[j]>UB):
            x[j]=UB
        if(x[j]<LB):
            x[j]=LB
        X[i][j]=x[j]

fit=[]
for i in range(ps):
    fit.append(F(X[i]))
    
delta_index1=fit.index(min(fit))
X_best=X[delta_index1]
if(F(X_best)<F(swarm)):
    swarm=X_best
if(F(swarm)<F(X_star)):
    X_star=swarm

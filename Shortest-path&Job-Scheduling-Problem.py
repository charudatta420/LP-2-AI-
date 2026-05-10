print("1. Single Source Shortest Path")
print("2. Job Scheduling Problem")

choice=int(input("Enter your choice: "))

if choice==1:
    n=int(input("Enter number of vertices: "))
    graph=[]
    print("Enter adjacency matrix:")
    
    for i in range(n):
        row=list(map(int,input().split()))
        graph.append(row)
    source=int(input("Enter source vertex: "))
    visited=[0]*n
    distance=[999]*n
    distance[source]=0
    
    for i in range(n):
        minimum=999
        u=-1
        for j in range(n):
            if not visited[j] and distance[j]<minimum:
                minimum=distance[j]
                u=j
        visited[u]=1
        
        for v in range(n):
            if graph[u][v]!=0 and not visited[v]:
                if distance[u]+graph[u][v]<distance[v]:
                    distance[v]=distance[u]+graph[u][v]
                    
    print("Shortest Distances:")
    
    for i in range(n):
        print(source,"to",i,"=",distance[i])
        
elif choice==2:
    n=int(input("Enter number of jobs: "))
    jobs=[]
    
    for i in range(n):
        name=input("Enter job name: ")
        deadline=int(input("Enter deadline: "))
        profit=int(input("Enter profit: "))
        jobs.append([name,deadline,profit])
    jobs.sort(key=lambda x:x[2],reverse=True)
    max_deadline=0
    
    for job in jobs:
        if job[1]>max_deadline:
            max_deadline=job[1]
    slots=["-"]*max_deadline
    total_profit=0
    
    for job in jobs:
        for j in range(job[1]-1,-1,-1):
            if slots[j]=="-":
                slots[j]=job[0]
                total_profit+=job[2]
                break
    print("Job Sequence:")
    
    for i in slots:
        print(i,end=" ")
    print("\nTotal Profit:",total_profit)
else:
    print("Invalid Choice")
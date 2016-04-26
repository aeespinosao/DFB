def camino_corto(cost,inter):
	for i in range(0,len(cost)):
		for j in range(0,len(cost)):
			for k in range(0,len(cost)):
				if(cost[j][i]+cost[i][k]<cost[j][k]):
					cost[j][k]=cost[j][i]+cost[i][k]
					inter[j][k]=inter[i][k]
	return(cost,inter)

mat=[[0,3,10,(2)**32,(2)**32],[3,0,(2)**32,5,(2)**32],[10,(2)**32,0,6,15],[(2)**32,5,6,0,4],[(2)**32,(2)**32,15,4,0]]

inter=[]
for i in range(len(mat)):
	fila=[]
	for j in range(len(mat)):
		if(i==j):
			fila.append(0)
		else:
			fila.append(i+1)
	inter.append(fila)


mat,inter=camino_corto(mat,inter)



nodoin=int(input("nodo inicio: "))
nodof=int(input("nodo final: "))

if(nodoin>nodof):
        nodoi=nodof-1
        nodoj=nodoin-1
        alreves=True
        nodofin=nodoin
else:
        nodoi=nodoin-1
        nodoj=nodof-1
        alreves=False
        nodofin=nodof

x=""+str(inter[nodoi][nodoj])
if(inter[nodoi][nodoj]==0):
        t=False
nodoj=inter[nodoi][nodoj]-1

while(inter[nodoi][nodoj]!=nodoi):
    if(inter[nodoi][nodoj]==0):
            t=False
            break    
    x+=str(inter[nodoi][nodoj])
    
    nodoj=inter[nodoi][nodoj]-1
    
camino=""
if(alreves):
        for i in x:
                camino+=(str(i)+"->")

else:        
        for i in range(len(x)-1,-1,-1):
                camino+=(x[i]+"->")
if(alreves):
        print(str(nodofin)+"->"+camino[:-2]+"  Costo del camino= "+str(mat[nodoin-1][nodof-1]))
else:
        print(camino+str(nodofin)+"  Costo del camino= "+str(mat[nodoin-1][nodof-1]))

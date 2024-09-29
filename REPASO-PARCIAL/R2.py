n=int(input("escribe el valor de n: "))
i=int()
sumatoria=float()

sumatoria=0

for i in range(1, n+1):
    sumatoria=sumatoria + (1/i) 
    
print(f"la sumatoria total es de {sumatoria}")
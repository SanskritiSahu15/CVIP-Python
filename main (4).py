def add(x,y):
    return x+y

def multiply(x,y):
    return x*y
    
def divide(x,y):
    if(y==0):
        return("Error cannot divide by 0")
    else:
        return x/y
        
def subtract(x,y):
    return x-y
        

def main():
    while True:
        
        print("1.Sum , 2.Multiply , 3.Divide , 4.Subtract , 5.Exit")
        choice=int(input("Enter choice: "))
        
        if(choice==5):
            print("Exiting program")
            break
        
        if choice not in [1,2,3,4,5]:
            print("Invalid choice , enter again")
            continue
        
        
        x=int(input("enter 1st number "))
        y=int(input("enter 2nd number "))
        
        
        if(choice==1):
            print("result= ",add(x,y))
            
        if(choice==2):
            print("result= ",multiply(x,y))
            
        elif(choice==3):
            print("result= ",divide(x,y))
            
        elif(choice==4):
            print("result= ",subtract(x,y))
            
        
if __name__ == "__main__":
    main()


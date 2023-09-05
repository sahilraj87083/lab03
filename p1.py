import pandas as pd
class Employee:
    
    def show(self ,data):
        df = pd.DataFrame(data)
        print(df)
    def Search(self ,data):
        df = pd.DataFrame(data)
        print("Choose for Searching")
        print("1. Age")
        print("2. Name")
        print("3. Salary")
        ch=int(input())
        if (ch==1):
            age=int (input())
            filtered_df = df[df['Age'] >= age]
            print(filtered_df)
        elif(ch==2):
            name=input()
            filtered_df = df[df['Name'] == name]
            print(filtered_df)
        elif (ch==3):
            sal=int(input())
            print("Choose Operator \n 1. > \n 2. < \n 3. <= \n 4. >=")
            ch1=int(input())
            if(ch1==1):
                filtered_df = df[df['Salary'] > sal]
                print(filtered_df)
            elif(ch1==2):
                filtered_df = df[df['Salary'] < sal]
                print(filtered_df)
            elif(ch1==3):
                filtered_df = df[df['Salary'] <= sal]
                print(filtered_df)
            elif(ch1==4):
                filtered_df = df[df['Salary'] >= sal]
                print(filtered_df)
def main():
    data= {
        'Employee ID ': ['161E90', '161F91 ', '161F99', '171E20','171G30'],
        'Name':['Raman','Himadri','jaya','Tejas','Ajay'],
        'Age': [41, 38, 51, 30,40],
        'Salary': [56000,67500,82100,55000,44000]
        
    }
    emp=Employee()
    emp.show(data)
    emp.Search(data)
if __name__ == "__main__":
    main()

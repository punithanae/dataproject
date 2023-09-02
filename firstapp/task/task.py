import pandas as pd
from collections import defaultdict
data=pd.read_csv('Number.csv') 

li=pd.DataFrame(data)
ls=li.values.tolist()




def cal_total_sum(s,num):
 my_dict = {} 
 for j in range(0,len(s)) :
  t=s[j][0]
  total=0
  key=t
  for i in str(t):
   total=total+int(i)
  value=total
  if(value==num):
   my_dict[key]=value
 return my_dict

def calculate_pyramid_number(input_number,num):
#    s=(int(input_number[1][0]))
   my_dict = {} 
   for i in range(0,len(input_number)):
    result = str(input_number[i][0])
    key=result
    while len(result) != 2:
        temp_result = ""
        
        for i in range(len(result) - 1):
            num1 = int(result[i])
            num2 = int(result[i + 1])
            num_sum = num1 + num2
            
            while num_sum >= 10:
                num_sum = num_sum % 10 + num_sum // 10
            
            temp_result += str(num_sum)
        result = temp_result
    if (temp_result==str(num)):
     my_dict[key]=temp_result
   
        
        
    
   return my_dict
  
# s1=calculate_pyramid_number(ls)
# print(s1)


 
# s1=cal_total_sum(ls)
# print(s1)

def find(s,f):
  result=[]
  for i in range(0,len(s)):
    s1=ls[i]
    fin=str(ls[i][0])
    print()
    if(f==int(fin[-2:])):
      result.append(ls[i])
    else:
      continue
  return result




def commonfind(s,f):
   result=[]
   
   for i in range(0,len(s)):
    count=0
    for j in f:
       s1=s[i]
       if(str(j) in str(s1)):
          count=count+1
       else:
          continue
       if(count==len(f)):
         result.append(ls[i][0])
       else:
         continue
    
   return result
print("1.Pyramid number 2.Total sum 3.Common_finding number 4.last number find 5.exit")
print("Enter the option: ")
num=int(input())

while(num != 5):

 if(num==1):
   print("Enter the number to find: ")
   number=int(input())
   s1=calculate_pyramid_number(ls,number)
   print(s1)
 elif(num==2):
  print("Enter the number to find: ")
  nu=int(input())
  s1=cal_total_sum(ls,nu)
  print(s1)
 elif(num==3):
  print("Enter the number to find: ")
  nu=int(input())
  re=commonfind(ls,str(nu))
  print(re)
 elif(num==4):
  print("Enter the number to find: ")
  nu=int(input())
  sl=find(ls,nu)
  print(sl)
 print("1.Pyramid number 2.Total sum 3.Common_finding number 4.last number find 5.exit")
 print("Enter the option: ")
 num=int(input())

  






# def search():
#    n=int(input())
# #########################----------common find
#    if(n==1):{
#    re=commonfind(ls,'2345')
#    print(re)
     
#    }

#  ########################--------------last find
#    elif(n==2):
#      {
#           # sl=find(ls,12)
#           # print(sl)
       
#      }
#    elif(n==3):
#     {
#      s1=calculate_pyramid_number(ls)
#      print(s1)
#     }
#    elif(n==4):
#    {
#    s1=cal_total_sum(ls)
#    print(s1)
#    }


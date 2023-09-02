from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def Home(request):
    return render(request,"firstapp/index.html")

def handle_uploaded_file(uploaded_file):
    # Define the desired location to save the file
    file_path = '/path/to/save/file.ext'

    # Write the uploaded file to the desired location
    with open(file_path, 'wb+') as destination:
        for chunk in uploaded_file.chunks():
            destination.write(chunk)

    return file_path
def read_file_data(file_path):
    file_data = []
    with open(file_path, 'r') as file:
        for line in file:
            file_data.append(line.strip())

    return file_data
def cal_total_sum(s,num):
 my_dict = {} 
 for j in range(1,len(s)) :
  t=s[j]
  total=0
  key=t
  for i in str(t):
   total=total+int(i)
  value=total
  if(value==int(num)):
   my_dict[key]=value
 return my_dict

def calculate_pyramid_number(input_number, num):
    my_dict = {}
    for i in range(1, len(input_number)):
        result = str(input_number[i])
        key = result
        
        while len(result) != 2:
            temp_result = ""
            for j in range(len(result) - 1):
                num1 = int(result[j])
                num2 = int(result[j + 1])
                num_sum = num1 + num2
                
                while num_sum >= 10:
                    num_sum = num_sum % 10 + num_sum // 10
                
                temp_result += str(num_sum)
            
            result = temp_result
        
        if temp_result == str(num):
            my_dict[key] = temp_result
    
    return my_dict

def commonfind(s,f):
   result=[]
   
   for i in range(1,len(s)):
    count=0
    for j in f:
       s1=s[i]
       if(str(j) in str(s1)):
          count=count+1
       else:
          continue
       if(count==len(f)):
         result.append(s[i])
       else:
         continue
    
   return result

def find(s,f):
  result=[]
  for i in range(1,len(s)):
    fin=str(s[i])
    if(int(f)==int(fin[-2:])):
      result.append(s[i])
    else:
      continue
  return result
def download_data(request):
    data = [
        'Item 1',
        'Item 2',
        'Item 3',
        # ... Include your data items here
    ]

    response = HttpResponse(content_type='text/plain')
    response['Content-Disposition'] = 'attachment; filename="data.txt"'

    for item in data:
        response.write(item + '\n')

    return response
def totalfind(s,p,t,e,c):
   re=[]
   result=cal_total_sum(s,t)
   result1=commonfind(s,c)
   result2=find(s,e)
   result3=calculate_pyramid_number(s,p)
   for i in result:
    for j in result1:
       for y in result2:
            for x in result3:
                 if(i==j and i==y and i==x):
                     re.append(i)
   return re
   
def upload(request):
    if request.method == 'POST' and request.FILES['file']:
        uploaded_file = request.FILES['file']
        #path=handle_uploaded_file(uploaded_file)
        # Handle the uploaded file as per your requirements
        # For example, you can save the file or process its contents

        # Fetch the data to display in the data view
        file_content = uploaded_file.read().decode('utf-8')  # Read and decode the file content

        # Split the file content into separate lines
        lines = file_content.split('\r\n')
        text_field_value = request.POST.get('input_box', '')
        p = request.POST.get('pyramid', '')
        e = request.POST.get('ended', '')
        c = request.POST.get('common', '')
        result=cal_total_sum(lines,text_field_value)
        result1=commonfind(lines,c)
        result2=find(lines,e)
        result3=calculate_pyramid_number(lines,p)
        total=totalfind(lines,p,text_field_value,e,c)

        # Pass the concatenated string to the template for rendering
        # context = {
        #     'lines': lines,
        # }
        
        
        data = [result]
        data2=[result1]
        data1=[result2]
        data3=[result3]
        data4=[total]

        return render(request, 'firstapp/index.html', {'data': data,'data2':data2,'data1':data1,'data3':data3,'data4':data4})
    else:
        return render(request, 'firstapp/index.html')
    
    


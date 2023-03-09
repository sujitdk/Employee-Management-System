from django.shortcuts import render,HttpResponse
from . models import Employee, Role, Department
# Create your views here.
def index(request):
    return render(request,'index.html')


def all_emp(request):
    emps = Employee.objects.all()
    context = {
        'emps':emps
    }
    print(context)
    return render(request,'all_emp.html',context)


def add_emp(request):
    if request.method == 'POST':
        first_name=request.POST['first_name']
        last_name = request.POST['last_name']
        salary = request.POST['salary']
        bonus = request.POST['bonus']
        phone = request.POST['phone']
        dept = request.POST['dept']
        role = request.POST['role']
        new_emp = Employee( First_name =first_name, Last_name=last_name, salary=salary,bonus=bonus, phone=phone, dept_id=dept,  role_id=role)
        new_emp.save()
        return HttpResponse('Employee added succeesfully')

    elif request.method =='GET':
         return render(request,'add_emp.html')

    else:
        return HttpResponse('An error occured')

def remove_emp(request,emp_id = 0):
    if emp_id:
        try:
           emp_to_be_removed=Employee.objects.get(id= emp_id)
           emp_to_be_removed.delete()
           return HttpResponse("Employee Removed Successfully")
        except:
            return HttpResponse("enter valid emp_id")

    emps = Employee.objects.all()
    context = {
        'emps':emps
    }
    return render(request,'remove_emp.html',context)

def filter_emp(request):
    return render(request,'filter_emp.html')


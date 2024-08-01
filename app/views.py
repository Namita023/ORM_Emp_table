from django.shortcuts import render

# Create your views here.
from app.models import *

def retrieve_emp(request):
    d={"employee":Emp.objects.all()}
    #WAQ to display all the details of the employee except dept no. 30
    d={"employee":Emp.objects.exclude(deptno=30)}
    #WAQ to display all the details of the employee whose salary is greater than 1500
    d={"employee":Emp.objects.filter(sal__gt="1500")}
    #WAQ to display all the details of employee whose salary>1000 and working in dept 10 and 30.
    d={"employee":Emp.objects.filter(sal__gt="1000",deptno__in=(10,30))}
    #WAQ to display all the details of the salesman, manager, clerk who are working in dept no 10 and 30
    d={"employee":Emp.objects.filter(job__in=("Salesman","Manager","Clerk"),deptno__in=(10,30))}
    #WAQ to display all the details of the employee who are working in deptno 10,20 and getting a salary more than 1500 and less than 3000.
    d={"employee":Emp.objects.filter(deptno__in=(10,20),sal__gt=1500,sal__lt=3000)}
    #WAQTD all the details of the employee who joined the company on 04-jan-82 to 01-jan-83, who are working in deptno 10 and 20.
    d={"employee":Emp.objects.filter(hiredate__gte='1982-1-4',hiredate__lte='1983-1-1',deptno__in=(10,30))}
    #WAQTD all the employees except salesman and clerk who are getting salary between 1000 to 3000.
    d={"employee":Emp.objects.exclude(job__in=('Salesman','Clerk')).filter(sal__range=(1000,3000))}
    #WAQTD all the details of employees except deptno 30 and whoever working as a salesman and manager.
    d={"employee":Emp.objects.exclude(deptno=30).filter(job__in=("Salesman","Manager"))}
    #WAQTD all the details who are working in deptno 10,30 and getting a salary >1000 and <3500, except manager
    d={"employee":Emp.objects.filter(deptno__in=(10,30),sal__gt=1000,sal__lt=3500).exclude(job="Manager")}
    #WAQTD all the details of smith, allen who are working in deptno 10 and 30 and getting a salary between 1000 and 3000
    d={"employee":Emp.objects.filter(ename__in=('Smith','Allen'),deptno__in=(10,30),sal__range=(1000,3000))} 
    #WAQTD all the details of employees who are working in deptno 10,20 and joined the company from 01-feb-1980 and 01-jan-1984.
    d={"employee":Emp.objects.filter(deptno__in=(10,20),hiredate__range=("1980-2-1","1984-1-1"))} 
    #WAQTD all the details of manager, president, analyst who are getting commission more than 800 and joined the company in the year of 81.
    d={"employee":Emp.objects.filter(job__in=("Manager","President","Analyst"), comm__gt=800, hiredate__year=1981)}
    #WAQTD the details of the employees whose name are in the range of A to C
    d={"employee":Emp.objects.filter(ename__range=("A","C"))}
    #WAQTO all the details of employees who are working in dept 10 to 30 and getting a salary of 500 to 3500 except salesman.
    d={'employee':Emp.objects.filter(deptno__in=(10,30),sal__range=(500,3500)).exclude(job='Salesman')}
    #WAQTD names whose name starting with letter M and 5th letter is I.
    d={"employee":Emp.objects.filter(ename__regex=r"^M[a-z][a-z][a-z]i.")}
    #WAQTD job consists of man
    d={"employee":Emp.objects.filter(job__regex=r"[a-zA-Z]?[Mm]an[a-zA-Z]?")}
    #WAQTD job where 6th letter is D and ending with letter t.
    d={"employee":Emp.objects.filter(job__regex=r"^[a-zA-Z]{5}d[a-zA-Z]*t$")}
    #WAQTD all the details of employees who joined the company in the month of dec.
    d={"employee":Emp.objects.filter(hiredate__month=12)}
    d={"employee":Emp.objects.filter(hiredate__regex=r".+12.+")}
    #WAQTD employee whose 2nd letter is L and 4th letter is k and the string consists of only 5 letters.
    d={"employee":Emp.objects.filter(ename__regex=r"[a-zA-Z]l[a-zA-Z]k[a-zA-Z]")}
    #WAQTD all the details of the employee who are not getting any commission.
    d={"employee":Emp.objects.filter(comm__isnull=True)}



    
    return render(request,"retrieve_emp.html",d)

def specific_col(request):
    #WAQ to display ename,salary,designation of all the managers
    Q={"employee":Emp.objects.filter(job="Manager")}#casesensitive
    #WAQ to display emp whose salary is greater than equal to 2200
    Q={"employee":Emp.objects.filter(sal__gte=2200)}

    return render(request,"specific_col.html",Q)

def equi_join(request):
    #WAQTD all the details of the employees and the department currently they are working
    d={"emp":Emp.objects.select_related('deptno').all()}
    #WAQTD the details of the employees who are working in accounting dept and manager job role
    d={"emp":Emp.objects.select_related('deptno').filter(deptno__dname="Accounting",job="Manager")}
    #WAQTD all employee details who's working loc consists atleast one character a.
    d={'emp':Emp.objects.select_related('deptno').filter(deptno__loc__regex=r"[a-zA-Z]*[aA][a-zA-Z]*")}
    #WAQTD all employee details who are getting the salary within 1500 and 2900.
    d={'emp':Emp.objects.select_related('deptno').filter(sal__range=(1500,2900))}

    return render(request,"equi_join.html",d)

#JOINS
def empdeptmgr(request):
    d={"Emp":Emp.objects.select_related('deptno','mgr').all()}
    d={"Emp":Emp.objects.select_related('deptno','mgr').filter(ename="Scott")}
    d={"Emp":Emp.objects.select_related('deptno','mgr').filter(deptno__in=(10,30),job="Manager")}
    d={"Emp":Emp.objects.select_related('deptno','mgr').filter(sal__gt=3000,comm__isnull=True)}
    d={"Emp":Emp.objects.select_related('deptno','mgr').filter(mgr=7698)}
    d={"Emp":Emp.objects.select_related('deptno','mgr').filter(job="Analyst").order_by("-ename")}
    d={"Emp":Emp.objects.select_related('deptno','mgr').filter(job__in=('Analyst',"Salesman"),deptno__in=(10,20))}
    d={"Emp":Emp.objects.select_related('deptno','mgr').filter(deptno__dname="Accounting")}
    d={"Emp":Emp.objects.select_related('deptno','mgr').filter(deptno__loc="Dallas")}
    d={"Emp":Emp.objects.select_related('deptno','mgr').filter(deptno__deptno__range=(10,30),deptno__loc__range=("A","E"))}
    d={"Emp":Emp.objects.select_related('deptno','mgr').filter(deptno__loc__in=("Chicago","New York"))}
    d={"Emp":Emp.objects.select_related('deptno','mgr').exclude(deptno__dname='Sales')}
    d={"Emp":Emp.objects.select_related('deptno','mgr').filter(mgr__isnull=True)}
    d={"Emp":Emp.objects.select_related('deptno','mgr').filter(mgr__ename='Clark')}
    d={"Emp":Emp.objects.select_related('deptno','mgr').filter(mgr__ename="Turner")}
    
    return render(request,"empdeptmgr.html",d)
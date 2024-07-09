from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from mysql import connector
from datetime import datetime
con =connector.connect(host="localhost",user="root",password="2003@Lalit",database="project")
cursor=con.cursor()
def getdata(atname,id):
    q=f"""select {atname} from students where student_id={id}"""
    cursor.execute(q)
    s=cursor.fetchone()
    for k in s:
        s=k
    return s
def getdatafac(atname,id):
    q=f"""select {atname} from faculty where faculty_id={id}"""
    cursor.execute(q)
    s=cursor.fetchone()
    for k in s:
        s=k
    return s
def home (request):
   return render(request,'index.html')
def login(request):
    if request.method=="POST":
        id=request.POST.get('userId')
        pasw=request.POST.get('password')
        utyp=request.POST.get('userType')
        if utyp=='admin':
            if id=='1042':
                if pasw=='456789':
                   return admin(request)
            return HttpResponse('invailid id and pasword')
        c=f"""select*from users where user_id={id} and user_password='{pasw}'and user_type='{utyp}'"""
        cursor.execute(c)
        k=tuple(cursor.fetchall())
        if k==():
            return HttpResponse('invailid password and user id')
        if utyp=='student':
            q=f"""select department_id from studentbelongto where student_id={id}"""
            cursor.execute(q)
            s=cursor.fetchone()
            for k in s:
                s=k
            dname=s
            q=f"""select department_name from department where department_id={dname}"""
            cursor.execute(q)
            s=cursor.fetchone()
            for k in s:
                s=k
            dname=s        
            studname=getdata("student_name",id)
            studemail=getdata("email",id)
            dob=getdata("date_of_birth",id)
            q=f"""select reply from querise where student_id={id}"""
            cursor.execute(q)
            rp=cursor.fetchone()
            q=f"""select*from querise where student_id={id}"""
            cursor.execute(q)
            x=tuple(cursor.fetchall())
            print(x)
            if x==():
                data={
               'id':id,
               'name':studname,
               'email':studemail,
               'dob':dob,
               'age':"20",
               'dname':dname,
                'reply':' -'
                 } 
                return  render(request,'prof.html',data)
            for k in rp:
                rp=k
            data={
            'id':id,
            'name':studname,
            'email':studemail,
            'dob':dob,
            'age':"20",
            'dname':dname,
            'reply':rp
            }
            
            return  render(request,'prof.html',data)
        if utyp=='faculty':
            q=f"""select department_id from facultybelongto where faculty_id={id}"""
            cursor.execute(q)
            s=cursor.fetchone()
            for k in s:
                s=k
            dname=s
            studname=getdatafac("faculty_name",id)
            studemail=getdatafac("email",id)
            dob=getdatafac("date_of_birth",id)
            q=f"""select querey,student_id from querise where faculty_id={id} """
            cursor.execute(q)
            p=cursor.fetchall()
            data={
               'id':id,
               'name':studname,
               'email':studemail,
               'dob':dob,
               'dname':dname,
               'p':p
             }
            return render(request,'profviewf.html',data)
    return render(request,'loginpage.html')
def dataindepartment(did):
    q=f"""select faculty_id,faculty_name,email from faculty where faculty_id in(select faculty_id from facultybelongto where department_id={did}) """
    print(q)
    cursor.execute(q)
    s=cursor.fetchall()
    return s
def signup(request):
    if request.method=='POST':
        role=request.POST.get('role')
        name=request.POST.get('name')
        id=int(request.POST.get('id'))
        phone=request.POST.get('phoneNumber')
        email=request.POST.get('email')
        dob=request.POST.get('date')
        ad=request.POST.get('address')
        dept=int(request.POST.get('department_name'))
        pasw=request.POST.get('password')
        doj=request.POST.get('doj')
        cid=request.POST.get('course')
        if role=='Student':
            c=f"""insert into students(student_id,student_name,date_of_birth,email,adress,phone_number) values("{id}","{name}","{dob}","{email}","{ad}","{phone}")"""
            d=f"""insert into studentbelongto(student_id,department_id,since) values("{id}","{dept}","{doj}")"""
            print(c)
            cursor.execute(c)
            cursor.execute(d)
        if role=='Faculty':
            c=f"""select*from coursebelongto where course_id={cid} and department_id={dept} """
            cursor.execute(c)
            k=tuple(cursor.fetchall())
            if k==():
                return HttpResponse('invailid  course id')
            else:
               c=f"""insert into faculty(faculty_id,faculty_name,date_of_birth,email,adress,phone_number) values("{id}","{name}","{dob}","{email}","{ad}","{phone}")"""
               d=f"""insert into facultybelongto(faculty_id,department_id,since) values("{id}","{dept}","{doj}")"""
               print(c)
               cursor.execute(c)
               cursor.execute(d)
               c=f"""insert into teachus(faculty_id,courseId) values("{id}","{cid}")"""
               cursor.execute(c)
            
        use=f"""insert into users(user_id,user_name,user_password,user_type) values("{id}","{name}","{pasw}","{role}")"""
        cursor.execute(use)
        con.commit()
        return HttpResponse('your data has been saved')
    return render(request,'from1.html')
def profview(request):
    return render(request,'profveiw.html')
def gradesheet(request,val):
    q=f"""select * from enrollment where student_id={val}"""
    cursor.execute(q)
    p=tuple(cursor.fetchall())
    if p==():
        return HttpResponse('you did not enroll any course')
    q=f"""select course_name,credit,grade_id from enrollment join grade on enrollment.enrollment_id=grade.enrollment_id join course on course.courseId=enrollment.courseId where student_id={val}"""
    cursor.execute(q)
    s=cursor.fetchall()
    q=f"""select sum(grade_id) from grade join enrollment on grade.enrollment_id=enrollment.enrollment_id where student_id={val}"""
    cursor.execute(q)
    p=cursor.fetchone()
    for i in p:
        p=i
    p=float(p)
    q=f"""select sum(credit) from enrollment join grade on enrollment.enrollment_id=grade.enrollment_id join course on course.courseId=enrollment.courseId where student_id={val}"""
    cursor.execute(q)
    tc=cursor.fetchone()
    for t in tc:
        tc=t
    tc=float(tc)
    tc=p/tc
    name=getdata('student_name',13)
    data={
        'id':val,
        's':s,
        'name':name,
        'sum':p,
        'tc':tc
    }
    return render(request,'viewgradesheet.html',data)
def csedept(request):
    data={
        'w':dataindepartment(1)
    }
    return render(request,'department.html',data)
def biodept(request):
     data={
        'w':dataindepartment(4)
     }
     return render(request,'biologydept.html',data)
def envidept(request):
     data={
        'w':dataindepartment(2)
     }
     return render(request,'enviormentdepartment.html',data)
def archedept(request):
     data={
        'w':dataindepartment(6)
     }
     return render(request,'archetcdepartment.html',data)
def materdept(request):
    data={
        'w':dataindepartment(5)
    }
    return render(request,'materideparment.html',data)
def mathdept(request):
     data={
        'w':dataindepartment(3)
    }
     return render(request,'mathdeparment.html',data)
def scholdept(request):
    return render(request,'scholarship.html')
def course(request,id):
    q=f"""select department_name from department where department_id={id}"""
    cursor.execute(q)
    s=cursor.fetchone()
    for k in s:
        s=k
    q=f"""select * from course where (courseId in(select course_id from coursebelongto where department_id={id}))"""
    cursor.execute(q)
    w=cursor.fetchall()
    data={
         'k':s,
         'w':w
     }
    
    return render(request,'course.html',data)
def adcos(request):
    if request.method=="POST":
        name=request.POST.get('name')
        id=request.POST.get('id')
        code=request.POST.get('code')
        credit=request.POST.get('credit')
        sem=request.POST.get('sem')
        did=request.POST.get('did')
        q=f"""insert into course(courseId,course_code,course_name,credit,semester) values('{id}','{code}','{name}','{credit}','{sem}')"""
        cursor.execute(q)
        q=f"""insert into coursebelongto(course_id,department_id) values('{id}','{did}')"""
        cursor.execute(q)
        con.commit()
        return HttpResponse('course has been added')
    return render(request,'adcos.html')
def addquery(request):
    if request.method=="POST":
        id=request.POST.get('id')
        query=request.POST.get('query')
        fid=request.POST.get('facultyId')
        q=f"""delete from querise where student_id={id}"""
        cursor.execute(q)
        q=f"""insert into querise(student_id,faculty_id,querey) values({id},{fid},'{query}')"""
        cursor.execute(q)
        con.commit()
        return HttpResponse('Query has been added')
    return render(request,'adqury.html')
def enroll(request,Pd):
    if request.method=="POST":
        id=request.POST.get('ID')
        cid=request.POST.get('cid')
        enid=id+cid
        id=int(id)
        cin=int(cid)
        con =connector.connect(host="localhost",user="root",password="2003@Lalit",database="project")
        cursor=con.cursor()
        q=f"""select department_id from studentbelongto where student_id={id}"""
        cursor.execute(q)
        s=cursor.fetchone()
        for i in s:
            s=i
        c=f"""select*from coursebelongto where course_id={cid} and department_id={s} """
        cursor.execute(c)
        k=tuple(cursor.fetchall())
        if k==():
            return HttpResponse('invailid  course id')
        q=f"""insert into enrollment(enrollment_id,student_id,courseId) values({enid},{id},{cid})"""
        cursor.execute(q)
        q=f"""insert into grade(enrollment_id,totle_mark) values({enid},{100})"""
        cursor.execute(q)
        con.commit()
        return HttpResponse('you enroll in the course')
    con =connector.connect(host="localhost",user="root",password="2003@Lalit",database="project")
    cursor=con.cursor()
    q=f"""select department_id from studentbelongto where student_id={Pd}"""
    cursor.execute(q)
    s=cursor.fetchone()
    for i in s:
        s=i
    q=f"""select courseId,course_name,course_code,credit,semester from coursebelongto join course on coursebelongto.course_id=course.courseId where department_id={s}"""
    cursor.execute(q)
    x=cursor.fetchall()
    data={
        's':x
    }
    return render(request,'enroll.html',data)
def students(request):
    q=f"""select student_id,student_name,email from students where student_id in (select user_id from users)"""
    cursor.execute(q)
    s=cursor.fetchall()
    data={
        'p':'MK Gandhi',
        'w':s
    }
    return render (request,'students.html',data)
def faculty(request):
    q=f"""select faculty_id,faculty_name,email from faculty """
    cursor.execute(q)
    s=cursor.fetchall()
    data={
        'w':s
    }
    return render (request,'faculty.html',data)
def studentdid(request,did):
    q=f"""select student_id,student_name,email from students where student_id in(select student_id from studentbelongto where department_id={did}) """
    cursor.execute(q)
    s=cursor.fetchall()
    q=f"""select department_name from department where department_id={did}"""
    cursor.execute(q)
    p=cursor.fetchone()
    for k in p:
        p=k
    data={
        'p':p+' '+'Department',
        'w':s
    }
    return render (request,'students.html',data)
def tryi(request):
    return render(request,'esehi.html')
def admin(request):
     q=f"""select* from students where student_id in (select user_id from users)"""
     cursor.execute(q)
     s=cursor.fetchall()
     q=f"""select* from faculty where faculty_id in (select user_id from users)"""
     cursor.execute(q)
     f=cursor.fetchall()
     q=f"""select *from course"""
     cursor.execute(q)
     c=cursor.fetchall()
     data={
         's':s,
         'f':f,
         'c':c
     }
     return render(request,'admin.html',data)
def upmark(request,fid):
    if request.method=='POST':
        id=request.POST.get('ID')
        gi=request.POST.get('gi')
        mb=request.POST.get('mb')
        q=f"""select faculty_id from teachus join enrollment on teachus.courseId=enrollment.courseId where enrollment_id={id}"""
        cursor.execute(q)
        s=cursor.fetchall()
        lalit=0
        for i in s:
            for k in i:
               if k==fid:
                lalit=1
        if lalit==0:
            return HttpResponse('you cant update the mark of this enroll id')
        q=f"""update grade set grade_id={gi},mark_obtain={mb} where enrollment_id={id} """
        cursor.execute(q)
        con.commit()
        return HttpResponse('mark and grade is updated')
    else:
        con =connector.connect(host="localhost",user="root",password="2003@Lalit",database="project")
        cursor=con.cursor()
        q=f"""select * from teachus join enrollment on teachus.courseId=enrollment.courseId where faculty_id={fid}"""
        cursor.execute(q)
        s=cursor.fetchall()
        data={
            's':s
        }
        return render (request,'upmark.html',data)
def contact(request):
    return render (request,'contact.html')
def blog(request):
    return render (request,'blog.html')
def adreply(request):
    if request.method=="POST":
        fid=request.POST.get('fid')
        reply=request.POST.get('reply')
        sid=request.POST.get('sId')
        q=f"""delete from querise where student_id={sid} and faculty_id={fid}"""
        print(q)
        cursor.execute(q)
        q=f"""insert into querise (student_id,reply) values({sid},'{reply}')"""
        print(q)
        cursor.execute(q)
        con.commit()
        return HttpResponse('reply has been added')
    return render(request,'addreply.html')
def removeu(request):
    if request.method=="POST":
        id=request.POST.get('ID')
        id=int(id)
        q=f"""delete from users where user_id={id}"""
        cursor.execute(q)
        con.commit()
        return HttpResponse('user has been removed')
    return render (request,'removeuser.html')
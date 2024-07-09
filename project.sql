create database project;
use project;
create table students (
student_id int primary key,
student_name varchar(160),
date_of_birth varchar(15),
email varchar(150),
adress varchar(300),
phone_number varchar(15)
);
create table users(
user_id int,
user_name varchar(150),
user_password varchar(150),
user_type varchar(150)
);
create table faculty(
faculty_id int primary key,
faculty_name varchar(150),
date_of_birth varchar(15),
email varchar(150),
adress varchar(300),
phone_number varchar(15)
); 
create table department(
department_id int primary key,
department_name varchar(150),
HOD int, 
foreign key(HOD) references faculty(faculty_id) 
);
create table course(
courseId int primary key,
course_code varchar(20),
course_name varchar(150),
credit float,
semester int
);
create table enrollment(
enrollment_id int primary key,
student_id int,
courseId int,
enrollment_date date,
foreign key(student_id) references students(student_id),
foreign key(courseId) references course(courseId)
);
create table scholarship(
scholarshipId int primary key,
scholarship_name varchar(150),
eligebility_critarie text,
award_amount decimal,
deadline date
);
create table feepayment(
applicationId int,
student_id int,
application_date date,
totle_fee decimal,
amount_recived decimal,
feestatus varchar(150),
foreign key(student_id) references students(student_id)
);
create table studentbelongto(
student_id int primary key ,
department_id int ,
since varchar(15),
foreign key(student_id) references student(student_id),
foreign key(department_id) references department(department_id));
create table facultybelongto(
faculty_id int primary key,
department_id int,
since varchar(15),
foreign key(faculty_id) references faculty(faculty_id),
foreign key(department_id) references department(department_id));
create table coursebelongto(
course_id int,
department_id int,
foreign key(course_id) references course(courseId),
foreign key(department_id) references department(department_id)
);
create table teachus(
faculty_id int primary key,
courseId int,
foreign key(faculty_id) references faculty(faculty_id),
foreign key(courseId) references course(courseId)
);
create table grade(
grade_id int,
enrollment_id int,
mark_obtain float,
totle_mark float,
foreign key(enrollment_id) references enrollment(enrollment_id)
);
create table aligebitlty(
 student_id int primary key,
 scholarshipId int,
 foreign key(scholarshipID) references scholarship(scholarshipId),
 foreign key(student_id) references students(student_id));
create table querise(
 student_id int ,
 faculty_id int,
 querey text,
 reply text,
 foreign key(faculty_id) references faculty(faculty_id),
 foreign key(student_id) references students(student_id));




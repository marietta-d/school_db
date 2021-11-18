create database if not exists school;

use school;

drop table if exists registrations;
drop table if exists timetable_entry;
drop table if exists teacher_subject;
drop table if exists student;
drop table if exists subject;
drop table if exists teacher;


create table student (
	id int auto_increment primary key,
    first_name varchar(255) not null,
    last_name varchar(255) not null,
    date_of_birth date,
    level varchar(255));

create table subject (
	id varchar(255) primary key,
    name varchar(255) not null,
    level varchar(255));

create table teacher (
	id int auto_increment primary key,
    first_name varchar(255) not null,
    last_name varchar(255) not null);
    
create table timetable_entry (
	day varchar(20), 
	start time,
    end time,
    room varchar(255),
    subject_id varchar(255),
    teacher_id int,
    foreign key (subject_id) references subject(id),
    foreign key (teacher_id) references teacher(id),
    primary key (day, start, room, subject_id, teacher_id));
    
create table registrations (
	student_id int,
    subject_id varchar(255),
    primary key (student_id, subject_id),
    foreign key (student_id) references student(id),
    foreign key (subject_id) references subject(id));
    
create table teacher_subject (
	teacher_id int,
    subject_id varchar(255),
    primary key (teacher_id, subject_id),
    foreign key (teacher_id) references teacher(id),
    foreign key (subject_id) references subject(id));
    
    
show tables;
    

    
    
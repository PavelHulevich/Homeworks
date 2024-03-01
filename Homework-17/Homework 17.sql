
CREATE TABLE Subjects (
id SERIAL PRIMARY KEY, 
name varchar(30) UNIQUE NOT null
);

CREATE TABLE Teachers (
id SERIAL PRIMARY KEY, 
name varchar(50) NOT NULL,
subject_id int not null,
foreign key (subject_id) REFERENCES Subjects (id)
);

CREATE TABLE Students (
id SERIAL PRIMARY KEY, 
name varchar(30) NOT NULL,
age int NOT NULL CHECK(age BETWEEN 6 AND 18)
);

CREATE TABLE Grades (
id SERIAL PRIMARY KEY, 
student_id int not null,
foreign key (student_id) references Students(id),
grade int not null check(grade between 1 and 10),
letter varchar(1) not null check(letter between 'A' and 'Z')
);

CREATE TABLE Marks (
id SERIAL PRIMARY KEY, 
student_id int not null,
foreign key (student_id) references Students(id),
subject_id int not null,
foreign key (subject_id) REFERENCES Subjects (id),
mark int not null
);

insert into Subjects values (1, 'Хатский язык');
insert into Subjects values (2, 'Нелинейная Алгебра');
insert into Subjects values (3, 'Физика пустоты');
insert into Subjects values (4, 'Джамп-навигация');
insert into Subjects values (5, 'Прорицание');
insert into Subjects values (6, 'Зельеварение');
insert into Subjects values (7, 'Трансфигурация');
insert into Subjects values (8, 'Нумерология');
insert into Subjects values (9, 'Астрология');
insert into Subjects values (10, 'Английский язык');

insert into Teachers (name, subject_id) values ('Дроид C-3PO', 8), ('Дроид R2-D2', 7), 
('Энакин Скайуокер', 3), ('Падме Амидала', 2), ('Лея Органа', 1), ('Оби-Ван Кеноби', 5),
('Чубака Чуи', 4), ('Дарт Сидиус', 6), ('Мастер Йода', 9), ('Дарт Вейдер', 10),
 ('Мастер Йода', 10), ('Дарт Вейдер', 3);

insert into Students (name, age) values ('Кира', 15), ('Иван', 16),
('Леонид', 17), ('Елена', 14), ('Анна', 13), ('Галина', 15), 
('Виктор', 16), ('Борис', 16), ('Мария', 12), ('Лера', 11);

insert into Grades (student_id, grade, letter) values (1, 8, 'A'), (2, 9, 'B'), (3, 10, 'A'),
(4, 7, 'C'), (5, 5, 'C'), (6, 8, 'B'), (7, 10, 'A'), (8, 9, 'A'), (9, 5, 'C'), (10, 5, 'C');

insert into Marks (student_id, subject_id, mark) values (1, 1, 7), (2, 3, 8),
(3, 3, 7), (4, 3, 8), (5, 8, 6), (6, 8, 9), (7, 7, 7), (8, 7, 8), (9, 9, 6), (10, 9, 9),
(1, 4, 5), (1, 7, 6), (3, 3, 10), (4, 9, 6), (5, 10, 3), (6, 10, 2), (7, 9, 4), (8, 7, 4), (9, 1, 6), (10, 3, 5);

--Создать индексы для ускорения поиска по таблицам. Использовать инструкцию CREATE
--INDEX. Создать индексы для следующих полей:

CREATE INDEX idx_students_name ON Students(name);
CREATE INDEX idx_teachers_name ON Teachers(name);
CREATE INDEX idx_subjects_name ON Subjects(name);
CREATE INDEX idx_grades_student_id ON Grades(student_id);
CREATE INDEX idx_marks_student_id ON Marks(student_id);

--Найти имена и возраст всех студентов, которые учатся в классе "10А".
select name, age
from Students
where Students.id in (
select student_id
from Grades
where grade=10 and letter='A');

--• Найти имена и предметы всех учителей, которые преподают Трансфигурацию или Английский язык
select t."name" , s."name" 
from teachers as t
inner join subjects as s on
t.subject_id = s.id 
where s.name='Трансфигурация' or s.name='Английский язык'

--• Найти средний балл по всем предметам для каждого студента
select name, avg(mark)
from Students 
inner join Marks on 
Marks.student_id=Students.id 
group by Students.id 

--Найти имена и оценки всех студентов, которые получили лучшую оценку по
--английскому языку.
with english_stud as (
select s.name, mark
from students as s 
left join marks m on
m.student_id = s.id 
left join subjects as su on
m.subject_id  = su.id 
where su.name = 'Английский язык'
)
select * from english_stud
where mark in (
select max(mark)
from english_stud)

--• Найти имена и количество предметов всех учителей, которые преподают более одного
--предмета.
with teachers_sum as(
select name, count(subject_id)
from teachers t group by name
)
select *
from teachers_sum
where count > 1

--• Найти имена и классы всех студентов, которые учатся в том же классе, что и Анна.
with grade_letter as(
select g.grade, g.letter 
from students s 
inner join grades g on
s.id = g.student_id 
where s.name = 'Анна'
)
select s.name, g.grade, g.letter
from students s 
inner join grades g on
s.id = g.student_id 
where grade=(select grade from grade_letter) and
	  letter=(select letter from grade_letter)

--• Найти имена и количество студентов в каждом классе.
with grade_letter as (	  
select g.grade, g.letter, count(*)
from grades g 
group by g.grade, g.letter order by g.grade, g.letter
)
select s."name" , g.grade , g.letter , count
from students s
inner join grades g on
s.id = g.student_id 
inner join grade_letter on
grade_letter.grade = g.grade
and grade_letter.letter = g.letter 
order by grade, letter

--• Найти имена всех предметов, по которым не было выставлено ни одной оценки.

select name
from subjects s 
left join marks m  on
s.id  = m.subject_id
where subject_id is null








CREATE TABLE "departments" (
    "dept_no" char(15)   NOT NULL,
    "dept_name" varchar(30)   NOT NULL,
    CONSTRAINT "pk_departments" PRIMARY KEY (
        "dept_no"
     )
);

CREATE TABLE "dept_emp" (
    "emp_no" char(15)   NOT NULL,
    "dept_no" char(15)   NOT NULL
);

CREATE TABLE "dept_manager" (
    "dept_no" char(15)   NOT NULL,
    "emp_no" char(15)   NOT NULL,
    CONSTRAINT "pk_dept_manager" PRIMARY KEY (
        "dept_no"
     )
);

CREATE TABLE "employees" (
    "emp_no" char(15)   NOT NULL,
    "emp_title_id" varchar(30)   NOT NULL,
    "birth_date" varchar(30)   NOT NULL,
    "first_name" varchar(30)   NOT NULL,
    "last_name" varchar(30)   NOT NULL,
    "sex" varchar(30)   NOT NULL,
    "hire_date" varchar(30)   NOT NULL,
    CONSTRAINT "pk_employees" PRIMARY KEY (
        "emp_no"
     )
);

CREATE TABLE "salaries" (
    "emp_no" char(15)   NOT NULL,
    "salary" int   NOT NULL,
    CONSTRAINT "pk_salaries" PRIMARY KEY (
        "emp_no"
     )
);

CREATE TABLE "title" (
    "title_id" char(15)   NOT NULL,
    "title" varchar(30)   NOT NULL,
    CONSTRAINT "pk_title" PRIMARY KEY (
        "title_id"
     )
);

ALTER TABLE "dept_emp" ADD CONSTRAINT "fk_dept_emp_emp_no" FOREIGN KEY("emp_no")
REFERENCES "employees" ("emp_no");

ALTER TABLE "dept_emp" ADD CONSTRAINT "fk_dept_emp_dept_no" FOREIGN KEY("dept_no")
REFERENCES "departments" ("dept_no");

ALTER TABLE "dept_manager" ADD CONSTRAINT "fk_dept_manager_emp_no" FOREIGN KEY("emp_no")
REFERENCES "employees" ("emp_no");

ALTER TABLE "employees" ADD CONSTRAINT "fk_employees_emp_title_id" FOREIGN KEY("emp_title_id")
REFERENCES "title" ("title_id");

ALTER TABLE "salaries" ADD CONSTRAINT "fk_salaries_emp_no" FOREIGN KEY("emp_no")
REFERENCES "employees" ("emp_no");


select * from departments
select * from employees
select * from dept_emp
select * from salaries
select * from title
select * from dept_manager

SELECT 
    e.emp_no,
    e.last_name,
    e.first_name,
    e.sex,
    s.salary
FROM 
    employees AS e
JOIN 
    salaries AS s
ON 
    e.emp_no = s.emp_no;

SELECT 
    first_name,
    last_name,
    hire_date
FROM 
    employees
WHERE 
    YEAR (hire_date) = 1986;


SELECT 
    e.emp_no,
    e.last_name,
    e.first_name,
    d.dept_no,
    d.dept_name
FROM 
    employees AS e
JOIN 
    dept_emp AS de
ON 
    e.emp_no = de.emp_no
JOIN 
    departments AS d
ON 
    de.dept_no = d.dept_no;

SELECT 
    first_name,
    last_name,
    sex
FROM 
    employees
WHERE 
    first_name = 'Hercules'
    AND last_name LIKE 'B%';

SELECT 
    last_name,
    COUNT(*) AS frequency
FROM 
    employees
GROUP BY 
    last_name
ORDER BY 
    frequency DESC;
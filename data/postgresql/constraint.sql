ALTER TABLE rawdata.student_subject
ADD CONSTRAINT fk_student_id
FOREIGN KEY (student_id)
REFERENCES rawdata.students(student_id)


ALTER TABLE rawdata.courses
ADD CONSTRAINT fk_class_id
FOREIGN KEY (class_id)
REFERENCES rawdata.class_section(class_id)

ALTER TABLE rawdata.courses
ADD CONSTRAINT fk_subject_id
FOREIGN KEY (subject_id)
REFERENCES rawdata.subjects(subject_id)

ALTER TABLE rawdata.course_student
ADD CONSTRAINT fk_student_id
FOREIGN KEY (student_id)
REFERENCES rawdata.students(student_id)

ALTER TABLE rawdata.course_student
ADD CONSTRAINT fk_course_id
FOREIGN KEY (course_id)
REFERENCES rawdata.courses(course_id)

ALTER TABLE rawdata.outcome
ADD CONSTRAINT fk_course_id
FOREIGN KEY (course_id)
REFERENCES rawdata.courses(course_id)

ALTER TABLE rawdata.outcome_student
ADD CONSTRAINT fk_outcome_id
FOREIGN KEY (outcome_id)
REFERENCES rawdata.outcome(outcome_id)

ALTER TABLE rawdata.outcome_student
ADD CONSTRAINT fk_student_id
FOREIGN KEY (student_id)
REFERENCES rawdata.students(student_id)

ALTER TABLE rawdata.attendance_statistics
ADD CONSTRAINT fk_student_id
FOREIGN KEY (student_id)
REFERENCES rawdata.students(student_id)

ALTER TABLE rawdata.attendance_statistics
ADD CONSTRAINT fk_course_id
FOREIGN KEY (course_id)
REFERENCES rawdata.courses(course_id)

CREATE TYPE rawdata.ternary AS ENUM ('0', '1', '2');

ALTER TABLE rawdata.detail_attendance
ADD CONSTRAINT fk_course_id
FOREIGN KEY (course_id)
REFERENCES rawdata.courses(course_id)






























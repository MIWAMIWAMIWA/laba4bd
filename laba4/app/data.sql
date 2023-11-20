INSERT INTO `iot_db`.`courses` (`courses_name`, `courses_description`,`courses_diffc`)
VALUES
  ('Course 1', 'Description for Course 1',1),
  ('Course 2', 'Description for Course 2',2),
  ('Course 3', 'Description for Course 3',3),
  ('Course 4', 'Description for Course 4',4),
  ('Course 5', 'Description for Course 5',5),
  ('Course 6', 'Description for Course 6',1),
  ('Course 7', 'Description for Course 7',2),
  ('Course 8', 'Description for Course 8',3),
  ('Course 9', 'Description for Course 9',4),
  ('Course 10', 'Description for Course 10',5);

  INSERT INTO `iot_db`.`authors` (`authors_name`, `authors_title`, `authors_email`)
VALUES
  ('Author 1', 'Title 1', 'author1@example.com'),
  ('Author 2', 'Title 2', 'author2@example.com'),
  ('Author 3', 'Title 3', 'author3@example.com'),
  ('Author 4', 'Title 4', 'author4@example.com'),
  ('Author 5', 'Title 5', 'author5@example.com'),
  ('Author 6', 'Title 6', 'autho6@example.com'),
  ('Author 7', 'Title 7', 'author7@example.com'),
  ('Author 8', 'Title 8', 'author8@example.com'),
  ('Author 9', 'Title 9', 'author9@example.com'),
  ('Author 10', 'Title 10', 'author10@example.com');

INSERT INTO `iot_db`.`affiliation` (`courses_id1`, `authors_id1`)
VALUES
  (1, 1),
  (2, 2),
  (3, 3),
  (4, 4),
  (5, 5),
  (1, 2),
  (2, 3),
  (3, 4),
  (4, 5),
  (5, 1);

INSERT INTO `iot_db`.`modules` (`modules_name`, `modules_position`, `time_to_deadline`, `courses_id`)
VALUES
  ('Module 1', 1, 7, 1),
  ('Module 2', 2, 10, 2),
  ('Module 3', 3, 5, 3),
  ('Module 4', 4, 8, 4),
  ('Module 5', 5, 3, 5),
  ('Module 6', 1, 9, 1),
  ('Module 7', 2, 6, 2),
  ('Module 8', 3, 12, 3),
  ('Module 9', 4, 4, 4),
  ('Module 10', 5, 11, 5);

INSERT INTO `iot_db`.`students` (`students_name`, `students_surname`)
VALUES
  ('John', 'Doe'),
  ('Jane', 'Smith'),
  ('Michael', 'Johnson'),
  ('Emily', 'Brown'),
  ('Daniel', 'Wilson'),
  ('Sarah', 'Anderson'),
  ('David', 'Lee'),
  ('Olivia', 'Martinez'),
  ('William', 'Taylor'),
  ('Sophia', 'Hernandez');

INSERT INTO `iot_db`.`progress` (`date_of_start`, `current_deadline`, `students_id`, `modules_modules_id`)
VALUES
  ('2023-01-01', '2023-02-01', 1, 1),
  ('2023-01-02', '2023-02-02', 2, 1),
  ('2023-01-03', '2023-02-03', 3, 2),
  ('2023-01-04', '2023-02-04', 4, 2),
  ('2023-01-05', '2023-02-05', 5, 3),
  ('2023-01-06', '2023-02-06', 6, 3),
  ('2023-01-07', '2023-02-07', 7, 4),
  ('2023-01-08', '2023-02-08', 8, 4),
  ('2023-01-09', '2023-02-09', 9, 5),
  ('2023-01-10', '2023-02-10', 10, 5);

INSERT INTO `iot_db`.`test` (`modules_modules_id`)
VALUES
  (1),
  (1),
  (2),
  (2),
  (3),
  (3),
  (4),
  (4),
  (5),
  (5);

INSERT INTO `iot_db`.`test_question` (`question_text`, `answers`, `correct_answer`, `test_idtest`)
VALUES
  ('What is 2 + 2?', 'A) 3, B) 4, C) 5', 'B) 4', 1),
  ('Who is the first president of the USA?', 'A) John Adams, B) Benjamin Franklin, C) George Washington', 'C) George Washington', 2),
  ('What is the capital of France?', 'A) London, B) Berlin, C) Paris', 'C) Paris', 3),
  ('What is the largest planet in our solar system?', 'A) Earth, B) Mars, C) Jupiter', 'C) Jupiter', 4),
  ('Which gas do plants absorb from the atmosphere?', 'A) Oxygen, B) Carbon Dioxide, C) Nitrogen', 'B) Carbon Dioxide', 5),
  ('Who wrote "Romeo and Juliet"?', 'A) Charles Dickens, B) William Shakespeare, C) Mark Twain', 'B) William Shakespeare', 6),
  ('What is the chemical symbol for gold?', 'A) Ag, B) Au, C) Hg', 'B) Au', 7),
  ('What is the largest mammal on Earth?', 'A) Elephant, B) Blue Whale, C) Giraffe', 'B) Blue Whale', 8),
  ('What is the process of converting food into energy called?', 'A) Respiration, B) Digestion, C) Photosynthesis', 'B) Digestion', 9),
  ('What is the powerhouse of the cell?', 'A) Mitochondria, B) Nucleus, C) Ribosome', 'A) Mitochondria', 10);

  INSERT INTO `iot_db`.`Attempt` (`date_of_attempt`, `score`, `test_idtest`, `students_id`)
VALUES
  ('2023-01-01', 90, 1, 1),
  ('2023-01-02', 85, 1, 2),
  ('2023-01-03', 92, 1, 3),
  ('2023-01-04', 88, 2, 4),
  ('2023-01-05', 78, 2, 5),
  ('2023-01-06', 95, 3, 6),
  ('2023-01-07', 91, 3, 7),
  ('2023-01-08', 87, 4, 8),
  ('2023-01-09', 86, 4, 9),
  ('2023-01-10', 94, 5, 10);

  INSERT INTO `iot_db`.`Attempt_answer` (`user_answer`, `is_correct`, `Attempt_idAttempt`, `test_question_id_question`)
VALUES
  ('B) 4', 1, 1, 1),
  ('C) George Washington', 1, 2, 2),
  ('C) Paris', 1, 3, 3),
  ('C) Jupiter', 1, 4, 4),
  ('B) Carbon Dioxide', 1, 5, 5),
  ('B) William Shakespeare', 1, 6, 6),
  ('B) Au', 1, 7, 7),
  ('B) Blue Whale', 1, 8, 8),
  ('B) Digestion', 1, 9, 9),
  ('A) Mitochondria', 1, 10, 10);
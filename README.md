[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-24ddc0f5d75046c5622901739e7c5dd533143b0c8e959d652212380cedb1ea36.svg)](https://classroom.github.com/a/MvgsrTWB)
# Project

## Table of Contents

- [Summary](#summary)
- [Project Descriptions](#project-descriptions)
- [Project Requirements](#project-requirements)
- [Required Deliverables and Deadlines](#required-deliverables-and-deadlines)
- [Running and Testing](#running-and-testing)
- [Project Assessment](#project-assessment)
- [Receiving Assistance](#receiving-assistance)

## Summary

Throughout the semester, you have learned the underlying workings of the programming language design and experimented with various programming languages. The course project invites you to explore, in greater detail, specific programming language(s) design or applications of languages.

Your project should result in a detailed project repository that includes all of your source code, in addition to written materials and technical diagrams that highlight the key contributions of your work. Part of written materials must include a technical report with a description of why the chosen topic is important and discuss the implementation and/or experimentation that you undertook. The written material should be precise, formal, appropriately formatted, grammatically correct, informative, and interesting. The source code that you write must be carefully documented and tested. If you install and use existing computer software, the steps for installation and use should be clearly documented in your report. Also, the report must explain the steps to run your programs. Finally, if you work in a team, your report must detail the work completed by each member of your team; individual contributions should also be reflected in commits to the team's repository. In addition to writing the aforementioned final report in Markdown, you will also use Markdown to write and submit a project proposal.

## Project Descriptions

Students are invited to pick one of the following projects. Please note that a student or a team selecting the student-designed project must first discuss the idea with the course instructor, and receive feedback and then final approval. Please note that you are fully responsible for ensuring the feasibility of the final project that is proposed.

1. **New Language**: Design and implement your own programming language. It can be very small but it must contain and specify all of the components pertaining to a programming language, and have some purpose/application behind it.

2. **Combination**: Select a realistic problem and implement a solution to it using a combination (at least two) of programming languages (Java and Python is not an appropriate combination). The languages must interact with each other in some way. You are allowed to make use of tools that help bridge the gap between languages. You need to be able to justify how mixing languages is beneficial for the problem you have chosen.

3. **Lox Interpreter**: Implement virtual machine for the lox interpreter by following [Section III](https://craftinginterpreters.com/a-bytecode-virtual-machine.html) of the Crafting Interpreters book. Add an enhancement to make it your own. If you pursue this project, please include your implementation in the interpreter repository that one of your team members worked on, not in the `src/` directory of this repository.

4. **Translation**: Select two languages and write a translation program that takes a program written in one language and translates it into another language. It does not need to be very complicated or sophisticated, you may choose which aspects of programming languages you want to incorporate and which you want to avoid. Select existing programs or write your own as test cases; your translator should be able to translate at least 200 lines of code - combined from your test cases.

5. **Student-Designed Project**: Students will develop an idea for their own project that focuses on one or more real-world topics in the field of programming languages. After receiving the course instructor's approval for your idea, you will complete the project and report on your results.

## Project Requirements

Please note that the course instructor expects students to implement and evaluate all of the source code needed to complete their proposed project. As such, there are no provided source code files for this assignment. You must store your programs in an `src` directory. You will also need to edit the three Markdown files in the `writing/directory` by the stated deadline. 

There are no GatorGrader code checks since each final project is different. In GatorGrader's absence, you should establish correctness checks for your source code. Importantly, you must implement test cases to assess your programs' correctness. Also, make sure to regularly commit to your GitHub repository.

## Required Deliverables and Deadlines

### Summary of Deliverables

This assignment invites you to submit, using GitHub, the following deliverables.

1. Completed, correct, fully commented, and properly formatted versions of all source code files, saved in the `src/` directory.

2. A three-paragraph written proposal, saved in the file `writing/proposal.md`, with an informative title, a description of the main idea, an initial listing of the tasks that you must complete, and a plan that you will follow to complete the work.

3. Participation in a Code Walkthrough. Code Walkthrough is a peer review of the code in which an author of the code leads the review process and the reviewers ask questions and spot possible errors. The technical leaders and the instructor will act as the reviewers. Each project's team members (or a single member) is considered to be an author of the code. For each written program, the author(s) will describe the written program by going through the code line by line and explaining the purpose of each line or a sequence of lines. The reviewers will provide feedback at the end of the review of each program or a complete review of programs, as appropriate. At the end of the walkthrough, the reviewers will report a list of findings and also identify high level action items, which will include the required next steps for the author(s) to take.

4. A detailed final project report, saved in the file `writing/report.md`, that documents, in a project-specific fashion, how you designed, implemented, and evaluated your system. This Markdown-based document should also explain and include the input, output, and the challenges that you confronted when implemented the project. For every challenge that you encountered, please explain your solution for it. If worked in a team, this document should also explain how your team collaborated to finish the assignment, with each team member writing their own paragraph inside of this Markdown file. Finally, your report should include information on how to compile/run your system and if there are dependencies beyond what is included in the `progator`, specify commands necessary to install these dependencies.

5. A commit log in your GitHub repository that clearly shows incremental progress made on the assignment.

### Deadlines

You must complete all of the aforementioned deliverables by the following due dates:

1. **Project Proposal: Friday, April 14th, 2023**: After brainstorming ideas during the class session, pick a topic for your final project. Remember, if you select the student-designed project, you must first have your project approved by the course instructor. Next, make sure that you accept the assignment and create a GitHub repository for the project. Finally, write and submit a proposal for your project. Your proposal should have an informative title, a description of the main idea, an initial listing of the tasks that you must complete, and a plan for completing the work.

2. **Code Walkthrough: Tuesday, April 25th, 2023**: You should give a demonstration, during the laboratory session, highlighting the most important code that you have finished. Code walkthrough is an informal process where code is reviewed for technical accuracy with the objective of finding errors and improving the quality of the code. The author(s) of the code lead the code walkthrough. The main purpose of walkthrough is to help authors gain an understanding of the content of the project and identify its potential flaws. Note that the goal of a walkthrough is an error detection, not error correction. When the walkthrough is finished, the author of the output is responsible for taking the necessary actions to correct the errors.

3. **Final Project Due Date: Monday, May 1st, 2023 by midnight**: You should submit the final version of your project through your project's GitHub repository. This submission should include all of the relevant source code and output, the written reports, and any additional materials that will demonstrate the success of your project. While you are encouraged to turn in the final project earlier, students must submit the completed assignment no later than 11:59 pm on the due date.

## Running and Testing

### Docker Instructions

You can use course's Docker environment if needed for running and testing your project. 

You should already have the [progator Docker Image](https://hub.docker.com/repository/docker/janyljumadinova/progator). If not, you can download automated build from public Docker Hub Registry:

`docker pull janyljumadinova/progator`

Once you have the Docker image, you can mount a directory as a volume with the argument *-v /your-path/:/root/ like this :

`docker run -d -p 80:80 -v /your-path/:/root/environment janyljumadinova/progator`

#### Accessing the IDE

<http://localhost>

## Project Assessment

The grade that a student receives on this assignment will have the following components:

- **Proposal [up to 10% of the project grade]**: Completed proposal document satisfying requirements of the proposal document specified above.

- **Code Walkthrough [up to 20% of the project grade]**: Participation in the walthrough with explanations presented during the walkthrough revealing a thorough understanding of the code. Every member of the team is expected to explain some part of the code written by the team. The reviewer reserves to question any member of the team to assess their understanding.

- **Implementation and Report [up to 70% of the project grade]**: As a part of this grade, the instructor will assess aspects of the project including, but not limited to, the correct and useful source code and Markdown report, its evaluation, the use of effective source code comments and Git commit messages. Your grade will be reduced if insufficient details are provided on how to run your source code or if it does not describe the necessary input to your system or does not include its sample output. Your grade will also be reduced if the commit log does not show consistent, individual contributions, or if an individual contribution is significantly lower than that of the other team members. 

## Receiving Assistance

If you are having trouble completing any part of this project, then please talk with either the course instructor or a student technical leader during the lab session. Alternatively, you may ask questions in the Slack workspace for this course. Finally, you can schedule a meeting during the course instructor's office hours.

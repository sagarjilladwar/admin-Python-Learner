# admin-Pthon-Learner

Python-Learner repository, to learn explore things in Python, DataStructures and Algorithms

## Setup

### Installing pre-req software for the course

#### Instructions for Installation and setting up of your development environments:

##### Installing Python :

Install Python 3.6.5(32 Bit) on your machines. If you have any older versions please uninstall and install this particular version of python.

https://www.python.org/ftp/python/3.6.5/python-3.6.5.exe

> Installation video: https://youtu.be/CO5YLsZ8Bwk

##### Installing and Configuring PyCharm Community Edition (IDE) :

Download the Pycharm Community Edition from the following link :

> https://download.jetbrains.com/python/pycharm-community-2017.2.4.exe

Note: Please download the file from the link we provided above (PyCharm 2017 Version),

Make sure you select shortcut (32-bit or 64-bit) based on your processor/OS type (i.e, Select 32-bit Launcher Shortcut if you have a 32-bit Processor/OS or else select 64-bit Launcher)

We recommend that you watch this video once in full and then try to start your installation on your second viewing:

Part 1: https://youtu.be/qRtVucXKXc4

Part 2: https://youtu.be/UPsDwdCnlkM

**The above installation video shows you how to**:
* How to install pycharm community edition
* How to create and configure your "pythoncourse" project
* How to install dependency packages - pytest
* How to configure a shortcut for your python console.
* How to configure the comments color. Download this file for this step: [ppcourse.icls](./ppcourse.icls)

Changing the default coloring scheme of pycharm

The default coloring scheme in pycharm (for comments, docstrings and strings) makes it easy to skip over the lesson notes and helpful comments/hints and we see questions that will not come up if you read the notes carefully. So be sure to do step 5 above.

##### Installation Issues

For any issues during installation, please post a clear description of your problem with screenshots (taken using Jing! and annotated appropriately) on the forum and try to help each other resolve these issues.

-------------------------

### Configure and run your first lesson

This task assumes that you have installed all the pre-req software in post  @17. So finish your installations before you do this.

 

This post contains instructions to configure pycharm and verify that your machines are ready for course use!

 

Each of the lessons in this course are given in the form of 'coding lessons'. In particular, each concept in python is given as a module, for e.g. unit1_lesson2_understanding_strings.py. The module file contains many test cases which explore the concept (of strings) from many angles (for e.g. mutability, slicing, indexing, operations on string...).

 

The tests are run using a python testing framework called pytest, which you have already installed. You must configure your project to use it so that you can run the tests. The instructions to set it up and run your first lesson are given below.

**Configuring your project (one time process)**:
* Open the pythoncourse project that we created in the installation videos.
* Configure py.test as your default test runner: [configure_pytest_runner.png](./images/configure_pytest_runner.png)
* Mark pythoncourse as sources root: [mark_pythoncourse_as_sourcesroot.png](./images/mark_pythoncourse_as_sourcesroot.png)
 

> Once you do this, copy the lesson folder in this repo into your c:\pythoncourse folder:  [first_lesson](./first_lesson/). DO NOT CREATE SUB FOLDERS. Just copy the lesson folder itself into the c:\pythoncourse folder.

 

#### Doing your first lesson:

 
Your project now has a sample lesson on assert and a placeholders file which you must not modify (it just defines a few constants). I want you to finish this lesson to ensure that the end to end flow is working for you. 

 

1. See this image to run a single test [running_a_test.png](./images/running_a_test.png)  . Initially every test will fail. You have to replace the blanks (__ and ___) in the file so that the tests pass. For example assert __ == 2 + 5 will  pass if __ is replaced by 7 :).

1. Get familiar with all the pytest window commands. Once you have worked through each test, run all tests once and ensure that they pass before you submit any lesson (instructions will for submission via google drive follow in a week): [run_all_tests.png](./images/run_all_tests.png)

Once these tests pass, you can be sure that you have configured everything properly to start the course.

Next steps:

1. Unit1 lessons will be posted. So make sure all your installs are done and your pycharm is configured properly to start doing the lessons!


--------

## Lessons

1. ### [first_lesson](./first_lesson/)

1. ### [unit1_lessons](./unit1_lessons/)

  Unit 1 lessons (lessons 02 to 06)

  You can find unit1 lessons at the end of this post. Before you get started:
  

  **Ensure that you have done these**:


  Your computers are setup correctly (py.test, sources root etc.) and the end to end flow is working properly as described in @28
  Read on how to do these lessons effectively - it is not just getting the lessons to pass, it is about building your personal skill: @27 and @28
  

  **Unit 1 Goals**:

  >At the end of this unit, you should have met the following goals.

  

  * Learn builtin data types like numbers and strings
  * Learn how to use builtin data structures in python - lists, dicts(hashtables), tuples and sets. When do you use which data structure? 
  * Learn to use some of the builtin functions in python using online and console help
  * Learn to use the Pycharm console (Alt + P)
  * Learn to use the Python visualizer
  * Learn to ask and answer questions in the forums.  Will post some guidance on this shortly.
  * Python comes with a very powerful set of features and libraries which makes it easy to get a lot of work done very fast. This is at the heart of rapid application development - using available features, frameworks and libraries to get your work done without reinventing things like lists, sets and hashtables.

  Your job is to learn how to use all of them to solve problems efficiently (both in terms of runtime performance and in terms of how much time it takes to write the code :) ).

  Once you finish the lessons, review this post and ensure that you have met the direct and incidental goals (tools, asking questions) mentioned above.

  Unit1 lessons: 

  This folder contains all the unit1 lessons. Download it and copy into your c:\pythoncourse folder (DON'T CREATE SUB FOLDERS) and work through the lessons as described.

1. ### [unit1_assignments](./unit1_assignments/)

  **Instructions to get started**:

  * Download and copy the files into your pythoncourse folder (DONT CREATE SUBFOLDERS)
  * Read the notes and documentation carefully
  * Follow the constraints for each problem. This is important even if you know python already. The assignments are given to develop a certain style of thinking, so write code according to constraints.
  * Once you finish your assignments, review the goals for unit1 and see if you have met them! If not, do additional tasks on your own to meet them.

1. ### [unit2_lessons](./unit2_lessons/)

  This unit will explore cool stuff like control flow, truth, functions and exceptions. Do these after finishing unit1 assignments.

  **Before you start**:

  * Review unit1 goals in @32 and see if you have met them, if not, do spend time on filling up the gaps.
  * Don't panic and rush through unit1 if you started late.
  * If you started late, go through all the posts starting with the welcome post in order and do them in order. DON'T DO THINGS OUT OF ORDER OR YOU WILL FACE UNNECESSARY PROBLEMS.

  **Goals for unit2**:


  * Learn how to use control flow statements in python (if, for, while, ..)
  * Learn to define and use python functions.
  * Understand various forms of parameters and arguments.
  * Learn notions of equality and identity in python
  * Learn notions of truth equivalence in python
  * Learn exceptions in python
  * Understand scopes of variables in python
  * Increase proficiency in use of the shell, python tutor and the forums
  * Get better at researching information on the web.

  **Unit 2 lessons**

  copy these into your pythoncourse folder unit2_lessons. Do not create sub folders.
  Spend sufficient time and dig deep into these lessons. Assignments will follow.

  If you find any issues in the lessons, do feel free to bring them up in the #forum channel.

  Happy coding and learning :).

1. ### [unit3](./unit3/)

  #### unit 3 - debugging

  Initially we used to give this unit on debugging pretty late in the course. However, I pushed it up as it can really help you progress better if you pick up this skill.

  In Units 1 - 2 we have have covered some of the basic aspects of python programming. A good understanding of those units is essential to write good code. However, there are few orthogonal skills without which you will not go far. 

  These skills deal with mindsets and knowledge of tools to make you a productive programmer. One of these topics is debugging and this unit deals with that. Debugging is probably the MOST IMPORTANT TOPIC in this whole course.

  I recommend you to start this unit even if you are stuck on previous assignments as what you learn here can help you debug your previous units problems faster. 

  While it is never discussed as a first class concept in most classes, for a new developer proficiency in debugging can make all the difference in how fast you grow in your job.  This is because:

  * As a new programmer you will make a lot of mistakes
  * If you cannot debug fast, you will get blocked and block your team because your work is not ready
  * If you repeatedly ask for help for many issues, you will lose reputation as a developer
  * The more time you spend debugging, the less time you have to learn other things on the job like design, tools, product space, customer behavior etc. which are important for your growth.
  * So a vicious cycle develops and it is frustrating to come out of it.
  

  In contrast, good troubleshooters/debuggers who can debug all kinds of problems like installation errors, ide errors, customer problems, their own code, other programmers code etc. are highly respected and shine through in the early stages of their career.

  In many companies, it is not uncommon to start new developers on "outstanding bugs/customer issues" as a way to bring them up to speed on the teams application/product. If you are weak in this area, you are off to a bad start!

  So take this unit seriously and do it well.  

  Once you learn how to use the debugger and start developing a debugging mindset, you are just a breakpoint away from solving most of your infinite loops and other problems :-)

  There are many useful ways of debugging and each lesson introduces one method/tool. You are expected to read the comments and try to fix the buggy code using the method described. Try to use these tools on all issues that you hit everyday and overtime you will become good debuggers.

  There are no separate assignments, the lessons themselves are the assignments.

  Enjoy and master this unit!
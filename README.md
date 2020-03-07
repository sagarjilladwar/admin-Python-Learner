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

1. [first_lesson](./first_lesson/)
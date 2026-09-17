Day 6 — Kernel & System Calls: Challenges and Explanations

Overview

This document contains the Day 6 challenges, my answers, and the explanations for revision.

Challenge 1 — Complete the Flow

Question

Complete the flow:

Application
↓

---

    ↓

Kernel
↓
Hardware / Resources

My Answer

Application → Runtime → OS → Kernel → Hardware / Resources

Correct Explanation

The complete simplified flow is:

Application
↓
Runtime / Libraries
↓
OS Interface / System Call
↓
Kernel
↓
Hardware / Resources

The runtime and libraries help the application communicate with the operating system. A system call is a controlled request to the kernel.

Key Takeaway

A system call is a bridge between an application and the kernel.

Challenge 2 — Explain the Restaurant Analogy

Question

Explain system calls using a restaurant analogy.

My Answer

Customer → Waiter → Kitchen → Chef → Waiter → Customer

Correct Explanation

Restaurant

Computer

Customer

Application

Waiter

Request or interface

Kitchen

Kernel

Chef

System performing the operation

Food/result

Returned result

The customer does not directly control the kitchen. They make a request through the waiter.

Similarly, an application requests a service through a controlled interface, and the kernel handles the operation.

Key Takeaway

Applications request services instead of directly controlling all hardware.

Challenge 3 — Identify the OS-Related Operation

Question 1

What does this do?

os.getcwd()

My Answer

I was confused.

Correct Explanation

os.getcwd() means get current working directory.

It returns the folder in which the program is currently working.

Example:

import os

print(os.getcwd())

Possible output:

C:\Users\Alex\software-engineering-journey

Question 2

What does this do?

os.listdir()

My Answer

It checks and lists the directory.

Correct Explanation

Correct.

os.listdir() lists the files and folders in a directory.

Example:

import os

print(os.listdir())

Question 3

What does this do?

os.mkdir("test")

My Answer

It makes a directory, meaning a file or folder.

Correct Explanation

Almost correct.

os.mkdir("test") creates a directory, which means a folder. It does not create a file.

os.mkdir("test")
↓
Creates folder: test

Question 4

What does this do?

open("file.txt", "r")

My Answer

It reads a file.

Correct Explanation

Correct.

The "r" mode means read mode.

Example:

with open("file.txt", "r") as file:
content = file.read()

print(content)

Question 5

What does this do?

subprocess.run(...)

My Answer

It starts another Python program through the OS and kernel, creating another process.

Correct Explanation

Correct main idea.

subprocess.run() can request that the operating system start another program as a separate process.

Simplified flow:

Python Process A
↓
subprocess.run()
↓
Operating System
↓
Python Process B

The exact low-level implementation depends on the operating system.

Key Takeaway

Python provides convenient functions for using operating-system functionality, but one Python function does not necessarily equal one raw system call.

Challenge 4 — User Mode vs Kernel Mode

Question

Which mode is generally associated with normal application code?

User mode

Kernel mode

Explain why.

My Answer

User mode is where the application enters and uses the system.

Kernel mode is where the application uses a system call, runtime, OS interface, and hardware/resources.

Correct Explanation

Normal applications generally run in user mode, where they have restricted privileges.

The application requests privileged services through an OS interface or system call. The kernel handles the protected operation in kernel mode.

Simplified flow:

Application (User Mode)
↓
Runtime / Libraries
↓
OS Interface / System Call
↓
Kernel (Kernel Mode)
↓
Hardware / Resources

Key Takeaway

User mode: normal application execution with restricted privileges.

Kernel mode: privileged kernel execution for managing protected operations and resources.

Challenge 5 — Backend Writes a Log File

Question

Explain this simplified flow:

Backend
↓
?
↓
?
↓
Log file

My Answer

Backend → Runtime → OS / Kernel → Log file

Correct Explanation

A more complete flow is:

Backend Process
↓
Runtime / File Library
↓
OS Interface
↓
Kernel
↓
Filesystem / Storage
↓
Log File

The backend creates a log message and uses a library or OS interface to request a file operation. The operating system and filesystem handle the underlying work.

The write must succeed, and persistence depends on how the data is buffered and flushed.

Key Takeaway

Applications use OS services to work with files instead of directly controlling storage hardware.

Day 6 Mental Model

Application
↓
Process
↓
Runtime / Libraries
↓
OS Interface / System Call
↓
Kernel
↓
CPU / RAM / Storage / Network

Important Definitions

Kernel

The core part of the Operating System that manages important resources and handles privileged operations.

System Call

A controlled request from an application to the Operating System kernel.

User Mode

A restricted execution mode used by normal applications.

Kernel Mode

A privileged execution mode used by the OS kernel.

Process

A program that is currently running.

Final Review

I should now be able to explain:

What the kernel is

What a system call is

Why applications use controlled interfaces

The difference between user mode and kernel mode

How Python interacts with OS functionality

How a backend can use OS services

Why the kernel is important for security and stability

One-Sentence Summary

Applications run in user mode and request operating-system services through controlled interfaces; the kernel handles privileged operations and manages system resources.

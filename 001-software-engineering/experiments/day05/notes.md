# Day 5 — Processes & Operating Systems

## Goal

Understand what an Operating System is and what a process is.

---

## What is an Operating System?

An Operating System (OS) is software that manages the computer and provides resources and services for applications.

Examples:

- Windows
- macOS
- Linux
- Android
- iOS

The OS manages things such as:

- CPU
- RAM
- Storage
- Files
- Networking
- Devices
- Running processes

---

## What is a Process?

A process is a program that is currently running.

Simple model:

```text
Program
   ↓
Run it
   ↓
Process
```

A Python file stored on the computer is a program.

When I run it, the operating system creates/manages a running process for it.

---

## Program vs Process

### Program

A set of instructions stored somewhere.

Example:

```text
hello.py
```

### Process

A running instance of a program.

Example:

```text
python hello.py
        ↓
Python process
```

---

## Mental Model

Think about a recipe.

```text
Recipe sitting on shelf
        ↓
Program

Actually cooking the recipe
        ↓
Process
```

---

## Process ID

A running process has a Process ID (PID).

Python example:

```python
import os

print(os.getpid())
```

The operating system uses the PID to identify the process.

---

## Process Resources

A process needs resources while running.

Examples:

- CPU time
- RAM
- Program instructions
- Data
- Other system resources

The operating system manages these resources.

---

## Process Lifecycle

A simplified lifecycle:

```text
Start
  ↓
Created
  ↓
Ready
  ↓
Running
  ↓
Finished
```

A process can also spend time waiting.

For example:

```text
Running
   ↓
Waiting for network
   ↓
Running again
```

---

## CPU and Processes

Multiple programs may need CPU time.

The operating system manages which runnable work gets CPU time.

Simplified:

```text
Python
  ↓
CPU
  ↓
Chrome
  ↓
CPU
  ↓
VS Code
```

Modern computers have multiple CPU cores, so multiple pieces of work can execute concurrently, but the OS still schedules work across the available CPU resources.

---

## AI Todo Connection

Our future application will have a backend.

```text
User
 ↓
Frontend
 ↓
API
 ↓
Backend
 ↓
PostgreSQL
```

The backend application runs as a process on a computer or server.

Therefore:

```text
Node.js Backend
      ↓
Running Program
      ↓
Process
      ↓
Operating System
      ↓
CPU + RAM + Network + Storage
```

---

## Important Connection to Previous Days

Day 2:

```text
Code
 ↓
Runtime
 ↓
CPU
```

Day 3:

```text
Information
 ↓
Bits
 ↓
0 and 1
```

Day 4:

```text
Storage
 ↓
RAM
 ↓
CPU
```

Day 5:

```text
Application
 ↓
Process
 ↓
Operating System
 ↓
CPU + RAM + Storage + Network
```

We are building the full picture layer by layer.

---

## Interview Questions

### What is a process?

A process is a program that is currently running.

### Program vs process?

A program is stored instructions. A process is a running instance of those instructions.

### What does an OS do?

The OS manages computer resources and provides services that applications use.

---

## Five Things to Remember

1. **OS = manager of the computer**
2. **Program = instructions**
3. **Process = running program**
4. **PID = identifier for a process**
5. **OS manages resources used by processes**

---

## Biggest Takeaway

> A program is something we have. A process is something that is currently running.

And the Operating System manages the processes and the resources they need.

```text
Application
    ↓
Process
    ↓
Operating System
    ↓
CPU / RAM / Storage / Network
```

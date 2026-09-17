# Day 6 — Kernel & System Calls

## Goal

Understand the Operating System kernel and how applications request services from the OS.

## What Is the Kernel?

The kernel is the core part of an Operating System.

It manages important resources such as:

- CPU
- Memory
- Processes
- Hardware access
- Filesystems
- Networking

## What Is a System Call?

A system call is a controlled request from an application to the Operating System kernel.

Simple model:

```text
Application
    ↓
System Call
    ↓
Kernel
    ↓
OS Resource / Hardware
    ↓
Result
```

## Why Are System Calls Needed?

Applications should not have unrestricted access to hardware or other processes.

Controlled interfaces help protect:

- Security
- Stability
- Resource management
- Isolation

## User Mode vs Kernel Mode

### User Mode

Normal applications generally execute in user mode.

Examples:

- Python
- Chrome
- VS Code
- Node.js

Applications have restricted privileges.

### Kernel Mode

The OS kernel runs with higher privileges.

It can manage resources and perform protected operations.

Simplified:

```text
User Mode
    ↓
System Call
    ↓
Kernel Mode
    ↓
Hardware / Resources
```

## Mental Model

```text
Application
    ↓
Request
    ↓
Reception Desk
    ↓
Kernel
    ↓
Building Resources
```

The application requests a service instead of directly controlling everything.

## Python Experiments

### Process Information

```python
import os

print(os.getpid())
print(os.getcwd())
print(os.listdir())
```

### Create a Directory

```python
import os

directory_name = "day6_test_folder"

if not os.path.exists(directory_name):
    os.mkdir(directory_name)
```

### Read a File

```python
with open("message.txt", "r") as file:
    content = file.read()

print(content)
```

### Run Another Program

```python
import subprocess
import sys

result = subprocess.run(
    [sys.executable, "--version"],
    capture_output=True,
    text=True
)

print(result.stdout)
print(result.returncode)
```

## Important Clarification

Python functions do not always map directly to one raw system call.

Python may use libraries and operating-system APIs that perform one or more lower-level operations.

The important concept is that applications interact with OS functionality through controlled interfaces.

## AI Todo Connection

Our backend depends on operating-system services.

```text
AI Todo Backend
      ↓
Backend Process
      ↓
Runtime / Libraries
      ↓
Operating System APIs
      ↓
Kernel
      ↓
CPU / RAM / Storage / Network
```

The OS helps our application:

- Run processes
- Access files
- Use memory
- Communicate over the network
- Write logs
- Access resources

## Interview Definitions

### Kernel

The core part of the OS that manages resources and provides important system services.

### System Call

A controlled request from an application to the OS kernel.

### User Mode

Restricted execution mode for normal applications.

### Kernel Mode

Privileged execution mode used by the OS kernel.

## Five Things to Remember

1. The kernel is the core of the Operating System.
2. Applications request OS services through controlled interfaces.
3. System calls provide a bridge to kernel services.
4. User mode has restricted privileges.
5. Kernel mode has higher privileges for managing resources.

## Biggest Takeaway

> Applications do not need to control hardware directly. They request services from the Operating System, and the kernel manages protected operations.

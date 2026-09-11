# Day 2 — What Actually Happens When Code Runs?

## 🎯 Goal

Understand what happens between the code I write and the CPU executing it.

---

# 1. Source Code

Source code is the code written by developers using a programming language.

Example:

```python
a = 10
b = 20

print(a + b)
```

Humans can understand this code, but the CPU cannot directly understand Python.

---

# 2. CPU

The CPU (Central Processing Unit) executes machine instructions.

A simplified model of CPU execution is:

```text
Fetch
  ↓
Decode
  ↓
Execute
  ↓
Repeat
```

The CPU performs operations such as:

- Loading data
- Storing data
- Adding values
- Comparing values
- Jumping to another instruction

---

# 3. Machine Instructions

A machine instruction tells the CPU to perform a specific operation.

Conceptually:

```text
LOAD
STORE
ADD
COMPARE
JUMP
```

The actual instructions depend on the CPU architecture.

Examples of CPU architectures:

```text
x86-64
ARM64
```

Different architectures can have different instruction sets.

---

# 4. Compiler

A compiler translates code from one representation into another.

A simplified model is:

```text
Source Code
     ↓
Compiler
     ↓
Machine Code
     ↓
Executable
     ↓
CPU
```

Languages such as C and C++ commonly use compilation as an important part of their execution process.

---

# 5. Interpreter

An interpreter executes a program through a runtime rather than simply producing a traditional native executable ahead of time.

A simplified model is:

```text
Source Code
     ↓
Interpreter / Runtime
     ↓
Execution
```

Modern programming language implementations can use a combination of compilation, interpretation, optimization, and runtime techniques.

Therefore:

> "Compiled language = fast and interpreted language = slow"

is an oversimplification.

---

# 6. Python Execution

Python does not simply go:

```text
Python Code
    ↓
CPU
```

A simplified model is:

```text
Python Source
      ↓
Python Interpreter
      ↓
Python Bytecode
      ↓
Python Runtime / Virtual Machine
      ↓
CPU
```

Python can produce bytecode that the Python runtime executes.

---

# 7. Python Bytecode Experiment

Example:

```python
a = 10
b = 20
result = a + b

print(result)
```

To inspect Python bytecode:

```bash
python -m dis math.py
```

The output may contain instructions such as:

```text
LOAD_CONST
STORE_NAME
LOAD_NAME
...
```

The exact output depends on the Python version.

The important lesson is not memorizing these instructions.

The important lesson is:

> High-level Python code is processed into a lower-level representation that the Python runtime can execute.

---

# 8. JavaScript Execution

JavaScript also requires a runtime/engine.

In Node.js, JavaScript is executed using the V8 JavaScript engine.

A simplified model is:

```text
JavaScript
     ↓
V8 / Runtime
     ↓
Lower-level execution
     ↓
CPU
```

This is why JavaScript code is not directly understood by the CPU.

---

# 9. Abstraction

Programming languages provide abstraction.

Instead of manually writing CPU instructions, I can write:

```python
result = price + tax
```

The programming language and runtime handle many lower-level details for me.

A simplified abstraction stack is:

```text
Application
    ↓
Programming Language
    ↓
Runtime
    ↓
Operating System
    ↓
CPU / Memory
    ↓
Hardware
```

Abstraction makes software easier to build.

However, understanding the layers underneath helps me reason about how software actually works.

---

# 10. Source Code vs Bytecode vs Machine Code

## Source Code

Code written by humans.

Example:

```python
a = 10
b = 20
print(a + b)
```

## Bytecode

A lower-level representation used by some language runtimes.

Example:

```text
LOAD_CONST
STORE_NAME
LOAD_NAME
...
```

## Machine Code

Instructions encoded for a particular CPU architecture.

Conceptually:

```text
Binary instructions
        ↓
CPU
```

These are different levels of representation.

---

# 11. Important Mental Model

Keep this model in mind:

```text
┌─────────────────────┐
│     Source Code     │
│ Python / JS / C     │
└──────────┬──────────┘
           ↓
┌─────────────────────┐
│ Compiler / Runtime  │
│ Interpreter / Engine│
└──────────┬──────────┘
           ↓
┌─────────────────────┐
│ Intermediate or     │
│ Machine Instructions│
└──────────┬──────────┘
           ↓
┌─────────────────────┐
│        CPU          │
└──────────┬──────────┘
           ↓
┌─────────────────────┐
│       Result        │
└─────────────────────┘
```

This is a simplified model.

I will make this model more detailed as I learn about CPUs, memory, operating systems, processes, compilers, and runtimes.

---

# 12. What I Learned Today

### Main ideas

- The CPU executes machine instructions.
- CPUs don't directly understand Python or JavaScript.
- Source code is written for humans.
- Compilers translate code between representations.
- Interpreters and runtimes execute programs.
- Python can use bytecode as an intermediate representation.
- JavaScript runs through a JavaScript engine/runtime.
- CPU architecture determines the machine instruction set.
- Abstraction allows developers to work without directly managing hardware instructions.

---

# 13. Experiment

## Experiment 1

Create:

```text
hello.py
```

Code:

```python
message = "Hello, Software Engineering!"

print(message)
```

Run:

```bash
python hello.py
```

Expected output:

```text
Hello, Software Engineering!
```

---

## Experiment 2

Inspect the bytecode:

```bash
python -m dis hello.py
```

Observe the instructions.

Don't try to memorize them.

Ask:

> How did my high-level Python code become these lower-level instructions?

---

## Experiment 3

Create:

```text
math.py
```

Code:

```python
a = 10
b = 20

result = a + b

print(result)
```

Run:

```bash
python math.py
```

Then:

```bash
python -m dis math.py
```

Compare the Python code with the bytecode.

---

# 14. Questions I Should Be Able to Answer

### 1. Why can't a CPU directly execute Python?

Because the CPU executes machine instructions defined by its architecture, not Python source code.

### 2. What does a compiler do?

It translates code from one representation into another, often producing machine code or another lower-level representation.

### 3. What does an interpreter/runtime do?

It provides the environment that processes and executes a program's representation.

### 4. What is a machine instruction?

An instruction that tells the CPU to perform a specific operation.

### 5. What is bytecode?

A lower-level representation of a program designed to be executed by a language runtime or virtual machine.

### 6. What happens conceptually when I run:

```bash
python hello.py
```

A simplified explanation is:

```text
hello.py
   ↓
Python
   ↓
Python bytecode / execution representation
   ↓
Python runtime
   ↓
CPU
   ↓
Program result
```

---

# 15. Biggest Takeaway

> **The CPU does not directly understand the high-level code I write. There are multiple layers of software between my source code and the hardware executing it.**

Understanding those layers is one of the goals of this journey.

---

# 🔜 Tomorrow

## Day 3 — Binary & Hexadecimal

Next, I will learn how computers represent information using:

```text
Bits
Bytes
Binary
Hexadecimal
```

Before moving on, I should commit today's work to Git:

```bash
git add .
git commit -m "learn how code gets executed"
git push
```

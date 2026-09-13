# Day 4 — RAM, Storage & Memory

## 🎯 Goal

Understand where a computer keeps data while a program is running.

The main idea:

> **Storage keeps data. RAM holds data the program is currently working with. The CPU processes it.**

---

# 🧠 1. What is RAM?

RAM stands for **Random Access Memory**.

Think of RAM like your **desk**.

When you're working, you put the things you need on your desk.

```text
📚 Bookshelf
   ↓
Storage

📝 Your desk
   ↓
RAM

🧠 You working
   ↓
CPU
```

RAM holds the information that programs are actively using.

---

# 💾 2. What is Storage?

Storage is where information is kept for the long term.

Examples:

- SSD
- HDD

Your computer's storage can contain:

- Programs
- Photos
- Videos
- Documents
- Projects
- Operating system files

Think of storage as a **bookshelf or cabinet**.

```text
💾 STORAGE

├── Programs
├── Photos
├── Documents
├── Projects
└── Operating System
```

---

# ⚡ 3. RAM vs Storage

| RAM                                | Storage                     |
| ---------------------------------- | --------------------------- |
| Temporary                          | Persistent                  |
| Used while programs run            | Keeps files long-term       |
| Fast working area                  | Long-term storage           |
| Usually smaller                    | Usually larger              |
| Data is lost when power is removed | Data remains after shutdown |

Simple rule:

> **RAM = work here**

> **Storage = keep it here**

---

# 🔄 4. What happens when I run a program?

Suppose I have:

```python
name = "Alex"
age = 25
```

The file is stored on my SSD.

When I run it, the computer needs to load the program and its required data into memory.

Simplified:

```text
Python file
     ↓
💾 SSD
     ↓
🧠 RAM
     ↓
⚙️ CPU
     ↓
Result
```

The CPU processes instructions and data while the program is running.

---

# 🧠 5. RAM is temporary

RAM is generally **volatile memory**.

That means its contents don't persist when the computer loses power.

```text
Computer ON
     ↓
RAM contains working data
```

Turn the computer off:

```text
Computer OFF
     ↓
RAM contents are lost
```

Storage is different:

```text
Computer OFF
     ↓
SSD still contains your files
```

---

# 📦 6. What does memory store?

Remember Day 3.

Computers ultimately represent information using **bits**.

```text
Memory
  ↓
Bytes
  ↓
Bits
  ↓
0s and 1s
```

For example:

```text
01001000
```

is 8 bits, which is one byte.

---

# 🏷️ 7. Variables and memory

When we write:

```python
age = 25
```

we see a simple variable.

But while the program runs, Python needs to represent that data using objects in memory.

Simplified:

```text
age
 ↓
25
 ↓
Object in memory
```

The exact way Python manages memory is more complicated, but this mental model is useful for now.

---

# 🔍 8. Python's `id()`

Python provides:

```python
id()
```

which gives an identifier associated with an object during its lifetime.

Example:

```python
age = 25

print(id(age))
```

You might see a number such as:

```text
140706427833528
```

Don't memorize the number.

The important idea is:

> Python objects exist somewhere in memory while the program is running.

In CPython, `id()` commonly corresponds to the object's memory address, but Python does not require that interpretation.

---

# 📏 9. Different data can use different amounts of memory

We used:

```python
import sys

number = 25
text = "Hello"
numbers = [1, 2, 3, 4, 5]

print(sys.getsizeof(number))
print(sys.getsizeof(text))
print(sys.getsizeof(numbers))
```

Our experiment produced:

```text
Number: 28 bytes
Text: 54 bytes
List: 104 bytes
```

The exact values can vary depending on the Python version and implementation.

The important lesson is:

> **Different objects can have different memory footprints.**

---

# 📈 10. More data can require more memory

We compared a small list with a larger list.

Our experiment produced:

```text
Small List: 88 bytes
Large List: 856 bytes
```

Again, don't memorize the numbers.

The important relationship is:

```text
More data
   ↓
More memory required
```

This becomes important when applications become large.

---

# 🧹 11. What happens when a program ends?

Consider:

```python
tasks = [
    {"title": "Learn Python", "completed": False}
]
```

While the program is running:

```text
Program
   ↓
RAM
   ↓
tasks
```

When the program ends, that in-memory application state is no longer available to the program.

If we want the task to still exist tomorrow, we need **persistent storage**.

For example:

```text
RAM
 ↓
Temporary working data

Database
 ↓
Persistent application data
```

---

# 🚀 12. Connection to our AI Todo product

Our Todo application will eventually have data such as:

```text
Users
Tasks
Projects
Labels
Comments
Notifications
AI history
```

We don't want this data to exist only in RAM.

We need persistent storage.

Our future architecture will look something like:

```text
👤 User
   ↓
⚛️ React Frontend
   ↓
🌐 API
   ↓
🟢 Node.js Backend
   ↓
🗄️ PostgreSQL
```

While the backend is running, it will also use RAM:

```text
Node.js Backend
      │
      ├── 🧠 RAM
      │     └── Temporary working data
      │
      └── 🗄️ PostgreSQL
            └── Persistent data
```

Later we'll learn databases and why we shouldn't simply keep everything in memory.

---

# 🧩 13. Why memory matters to software engineers

Memory affects:

- Performance
- Application size
- Scalability
- Memory leaks
- Caching
- Databases
- Servers
- Browsers
- AI applications

Imagine our Todo application has:

```text
10 tasks
```

That's easy.

But eventually imagine:

```text
1,000,000 users
        ↓
Millions of tasks
        ↓
Huge amounts of data
```

Now memory becomes an engineering concern.

We need to think about how much data we're loading and keeping in memory.

---

# 🧩 14. Interview connection

A basic interview question:

### What's the difference between RAM and storage?

Good beginner answer:

> RAM is temporary working memory used while programs are running. Storage, such as an SSD, keeps data persistently even after the computer is turned off.

Later we'll go deeper into:

- Stack
- Heap
- Memory allocation
- References
- Garbage collection
- Memory leaks
- Caching

Don't memorize these yet.

We'll learn them when we need them.

---

# 🧩 15. LeetCode connection

There is no LeetCode problem for today.

That's intentional.

We're building the foundation first.

Eventually we'll connect:

```text
Data Structure
      ↓
Memory usage
      ↓
Space complexity
      ↓
Algorithm
      ↓
LeetCode
      ↓
Interview explanation
```

Remember:

> **Problem solved ≠ concept understood.**

The goal is to understand why the solution works.

---

# 🔬 16. Experiments completed

## Experiment 1

```python
name = "Alex"
age = 25

print(name)
print(age)

print(id(name))
print(id(age))
```

Learned:

> Python objects have identifiers while they exist.

---

## Experiment 2

```python
age = 25

print(id(age))

age = 30

print(id(age))
```

Learned:

> A program can change its state and work with different values.

---

## Experiment 3

```python
numbers = []

for i in range(10):
    numbers.append(i)

print(numbers)
```

Learned:

> Data structures hold data in memory.

---

## Experiment 4

```python
import sys

number = 25
text = "Hello"
numbers = [1, 2, 3, 4, 5]

print(sys.getsizeof(number))
print(sys.getsizeof(text))
print(sys.getsizeof(numbers))
```

Learned:

> Different objects can require different amounts of memory.

---

# 🧠 17. Day 4 mental picture

Remember this:

```text
                 YOUR PROGRAM
                      │
                      ↓
                 💾 STORAGE
                  "Keep it"
                      │
                    load
                      ↓
                   🧠 RAM
                "Work here"
                      │
                      ↓
                   ⚙️ CPU
                 "Process it"
                      │
                      ↓
                    RESULT
```

And underneath:

```text
RAM
 ↓
Bytes
 ↓
Bits
 ↓
0s and 1s
```

---

# ⭐ 18. Five things to remember

1. **RAM is working memory.**
2. **Storage keeps data persistently.**
3. **RAM is temporary.**
4. **Programs need memory to work with data.**
5. **More data can require more memory.**

---

# 🎯 Day 4 biggest takeaway

Don't try to memorize complicated definitions.

Remember the story:

> **Storage keeps my data. RAM holds the data my program is currently using. The CPU processes it. Underneath, the information is represented using bits.**

---

# 🔮 What's next?

Day 5 will continue building our computer fundamentals.

We'll move closer to understanding:

**Memory → CPU → Programs → Operating System → Processes**

The goal is to slowly build a complete mental model of what happens inside a computer.

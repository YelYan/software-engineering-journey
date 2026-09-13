# Day 3 — Binary & Hexadecimal

## 🎯 Today's Goal

Today I want to understand one simple question:

> **How does a computer represent information?**

The simple answer:

> **Computers ultimately work with 0s and 1s.**

---

# 1. What is a Bit?

A **bit** is the smallest piece of information a computer can work with.

A bit can be:

```text
0
```

or

```text
1
```

Think about a light switch:

```text
OFF = 0
ON  = 1
```

So:

> **A bit is like a tiny switch that can be OFF or ON.**

---

# 2. What is a Byte?

A computer puts bits together.

**8 bits = 1 byte**

For example:

```text
01001000
```

There are 8 numbers here, so this is:

```text
8 bits = 1 byte
```

Easy way to remember:

```text
Bit   → one tiny switch 💡

Byte  → 8 switches together 📦
```

---

# 3. What is Binary?

Humans normally use the decimal number system.

Decimal uses:

```text
0 1 2 3 4 5 6 7 8 9
```

That's 10 different digits.

Computers use **binary**.

Binary only uses:

```text
0 1
```

So:

> **Binary is a number system that uses only 0 and 1.**

---

# 4. Counting in Binary

Normal decimal:

```text
0
1
2
3
4
5
6
7
8
```

Binary:

```text
Decimal    Binary

0          0
1          1
2          10
3          11
4          100
5          101
6          110
7          111
8          1000
```

It might look strange at first, but binary is simply another way of counting.

---

# 5. How Does `101` Become 5?

Binary uses powers of 2.

For:

```text
101
```

the positions represent:

```text
4   2   1
```

Now look at the bits:

```text
1   0   1
```

So:

```text
1 × 4 = 4
0 × 2 = 0
1 × 1 = 1
```

Add them:

```text
4 + 0 + 1 = 5
```

Therefore:

```text
101 in binary = 5 in decimal
```

I don't need to memorize this.

I just need to understand that binary uses powers of 2.

---

# 6. Why Do We Need Hexadecimal?

Binary can become very long.

For example:

```text
10101111
```

That's difficult for humans to read.

So programmers often use **hexadecimal**, or **hex**, as a shorter way to represent binary.

---

# 7. What is Hexadecimal?

Hexadecimal is a number system that uses **16 symbols**.

It uses:

```text
0 1 2 3 4 5 6 7 8 9 A B C D E F
```

The letters represent numbers:

```text
A = 10
B = 11
C = 12
D = 13
E = 14
F = 15
```

That's all hexadecimal means.

---

# 8. Why is Hex Useful?

Here's the useful part:

```text
4 bits = 1 hex digit
```

For example:

```text
1010 = A
1111 = F
```

So:

```text
1010 1111
```

can be written as:

```text
AF
```

Instead of:

```text
10101111
```

So hexadecimal is basically:

> **A shorter, easier way for humans to read groups of binary bits.**

---

# 9. The Important Relationship

Remember these:

```text
4 bits = 1 hexadecimal digit

8 bits = 1 byte

8 bits = 2 hexadecimal digits
```

For example:

```text
Binary:
10101111

Hex:
AF

Byte:
1 byte
```

---

# 10. What Does `0x` Mean?

Sometimes I will see something like:

```text
0xFF
```

The `0x` simply tells me:

> **"This number is written in hexadecimal."**

For example:

```text
0xFF
```

is hexadecimal.

It represents:

```text
255
```

in decimal.

I don't need to be scared when I see `0x`.

It's just a label telling me:

```text
"This is hex."
```

---

# 11. Python and Binary

Python can help me experiment with binary.

```python
number = 10

print(bin(number))
```

Python gives:

```text
0b1010
```

The `0b` means:

> "This is binary."

I can also convert binary back to decimal:

```python
binary_number = "1010"

print(int(binary_number, 2))
```

Result:

```text
10
```

Useful Python functions:

```text
bin()        → decimal to binary

int(value, 2) → binary to decimal
```

---

# 12. Python and Hexadecimal

Python can also work with hexadecimal.

```python
number = 255

print(hex(number))
```

Result:

```text
0xff
```

The `0x` tells me it is hexadecimal.

I can convert it back:

```python
hex_number = "FF"

print(int(hex_number, 16))
```

Result:

```text
255
```

Useful Python functions:

```text
hex()          → decimal to hexadecimal

int(value, 16) → hexadecimal to decimal
```

---

# 13. A Real Example From Web Development 🎨

I've probably seen colors like:

```text
#FF0000
```

This is a hexadecimal color.

It represents:

```text
Red   = FF
Green = 00
Blue  = 00
```

So:

```text
#FF0000
```

represents red.

This is one example of hexadecimal that I have probably already used as a web developer.

---

# 14. What About Text?

What happens when I type:

```text
A
```

A computer can't simply store a magical letter "A".

It needs a way to represent that letter as data.

For example, ASCII represents:

```text
A = 65
```

And 65 can be represented in binary:

```text
01000001
```

So, very simply:

```text
A
↓
65
↓
01000001
↓
Bits
```

We'll learn more about this later when we study **ASCII, Unicode, and character encoding**.

---

# 15. What Does This Have to Do With My Code?

When I write:

```python
age = 25
```

I see:

```text
25
```

But underneath my programming language, the computer needs to represent that information using lower-level data.

The simplified idea is:

```text
My Code
   ↓
Programming Language
   ↓
Data
   ↓
Bits
   ↓
0 and 1
   ↓
Computer Hardware
```

This is why I'm learning binary and hexadecimal.

I'm trying to understand what happens **underneath the code I write**.

---

# 16. Where Will I See Binary and Hex?

I may see these concepts when learning about:

- CPU
- Memory
- Machine code
- Networking
- Files
- Images
- Colors
- Character encoding
- Permissions
- Security
- Performance
- Low-level programming

I don't need to master all of these today.

I'm just building the foundation.

---

# 17. Simple Mental Picture

Imagine a computer has billions of tiny switches:

```text
💡 💡 💡 💡 💡 💡 💡 💡
 0  1  0  1  1  0  0  1
```

These switches represent **bits**.

8 switches:

```text
💡 💡 💡 💡 💡 💡 💡 💡
        ↓
      1 byte
```

We can write them as binary:

```text
01011001
```

And hexadecimal gives us a shorter way to represent them.

The important idea is:

> **Hexadecimal does not replace the bits. It is just a shorter way for humans to write them.**

---

# 18. The 5 Things I Must Remember

If I forget everything else, remember these five things:

### 1. Bit

```text
0 or 1
```

### 2. Byte

```text
8 bits
```

### 3. Binary

```text
Uses 0 and 1
```

### 4. Hexadecimal

```text
Uses 0-9 and A-F
```

### 5. Relationship

```text
4 bits = 1 hex digit
8 bits = 1 byte
```

---

# 🧠 My Day 3 Mental Model

```text
Computer
   ↓
Works with bits
   ↓
0 and 1
   ↓
Bits are grouped into bytes
   ↓
Binary represents the bits as numbers
   ↓
Hexadecimal gives humans a shorter way
to read groups of bits
```

---

# 🎯 What I Should Be Able to Explain

After Day 3, I should be able to explain:

**What is a bit?**

> A tiny piece of information that can be 0 or 1.

**What is a byte?**

> 8 bits together.

**What is binary?**

> A number system that uses 0 and 1.

**What is hexadecimal?**

> A number system using 0-9 and A-F that gives humans a shorter way to represent binary data.

**Why do programmers use hex?**

> Because long binary numbers are difficult for humans to read.

**What does `0x` mean?**

> It tells me that a number is written in hexadecimal.

---

# 🔬 My Day 3 Experiments

I created:

```text
experiments/
└── day-03/
    ├── binary.py
    ├── hex.py
    └── notes.md
```

I practiced:

- Decimal → Binary
- Binary → Decimal
- Decimal → Hexadecimal
- Hexadecimal → Decimal
- Basic bitwise operations

---

# 📝 Day 3 Challenge

Try these **without Python first**.

### Challenge 1

What is:

```text
101
```

in decimal?

Answer:

```text
5
```

---

### Challenge 2

What is:

```text
1111
```

in decimal?

Answer:

```text
15
```

---

### Challenge 3

What is:

```text
255
```

in hexadecimal?

Answer:

```text
FF
```

---

### Challenge 4

What is:

```text
0x10
```

in decimal?

Answer:

```text
16
```

---

### Challenge 5

Convert:

```text
1010 1111
```

to hexadecimal.

Answer:

```text
AF
```

---

# 💡 Biggest Takeaway

> **Computers ultimately work with 0s and 1s.**

Bits are the tiny building blocks.

Bytes are groups of 8 bits.

Binary is a way to represent numbers using 0 and 1.

Hexadecimal is a shorter, more human-friendly way to represent groups of binary bits.

I'm learning these concepts because I don't just want to know **how to write code**.

I want to understand **what is happening underneath my code.**

---

# 🚀 What's Next?

Next, I'll learn:

> **How does a computer represent things like text, numbers, images, and other types of data?**

This will lead into:

```text
Bits
 ↓
Bytes
 ↓
Characters
 ↓
ASCII
 ↓
Unicode
 ↓
Memory
```

And this will make the lower-level side of programming much clearer.

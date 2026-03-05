📘 Diamond Star Pattern Program (Python)

📌 Overview

This Python program prints a Diamond Star (*) Pattern using loops and string multiplication.

The diamond is divided into two parts:

🔺 Upper (Pyramid)

🔻 Lower (Inverted Pyramid)

This project demonstrates loop control, string repetition, and pattern design logic.

⚙️ Source Code
rows = 5

# Upper Part
for i in range(1, rows + 1):
    print(" " * (rows - i) + "*" * (2*i - 1))

# Lower Part
for i in range(rows - 1, 0, -1):
    print(" " * (rows - i) + "*" * (2*i - 1))
🧠 How It Works
1️⃣ Define Height of Diamond
rows = 5

This controls:

Total height = 2 * rows - 1

Width of the diamond

🔺 Upper Part (Pyramid)
for i in range(1, rows + 1):

This loop builds the top half.

Spaces Logic
" " * (rows - i)

Adds decreasing spaces

Keeps stars centered

Stars Logic
"*" * (2*i - 1)

Generates odd numbers: 1, 3, 5, 7, 9

Forms the pyramid shape

🔻 Lower Part (Inverted Pyramid)
for i in range(rows - 1, 0, -1):

Runs backward

Mirrors the upper part

Same logic:

Spaces increase

Stars decrease

▶️ Output (rows = 5)
    *
   ***
  *****
 *******
*********
 *******
  *****
   ***
    *
🔑 Key Concepts Demonstrated

Nested loop logic

Forward and reverse looping

String multiplication

Pattern symmetry

Mathematical pattern formula (2*i - 1)

⏱️ Time Complexity

O(n²)
Because each row prints multiple characters.

🚀 Customization

Change the size by modifying:

rows = 7

You will get a larger diamond.

📚 Learning Outcomes

After understanding this project, you should be able to:

Build symmetrical patterns

Use arithmetic expressions in pattern design

Combine multiple loops effectively

Think in terms of row-by-row visual logic

<img width="650" height="871" alt="image" src="https://github.com/user-attachments/assets/6931f191-533b-4284-9138-b3c51dd823c8" />

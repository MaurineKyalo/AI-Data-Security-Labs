# 🛡️ Password Strength Checker

## Project Overview
This is a Python-based security tool that evaluates the strength of a password. It checks for common security vulnerabilities (like short length or lack of complexity) and provides a strength rating.

## 🧠 The Logic and Algorithm
This project demonstrates foundational cybersecurity principles and string manipulation. Here is how the logic flows:

1. **Length Check:** The program assigns points based on the length of the password. It gives 1 point if the password is at least 8 characters long, and another point if it is 12 or more characters long.
2. **Character Complexity Check (Regex):** The program uses Python's `re` (Regular Expressions) module to search for specific character types:
   - It checks for the presence of **lowercase** letters (`[a-z]`).
   - It checks for the presence of **uppercase** letters (`[A-Z]`).
   - It checks for **numbers** (`\d`).
   - It checks for **special characters** (e.g., `!@#$%^&*`).
   Each successful check adds 1 point to the score.
3. **Final Evaluation:** Based on the total score, the program returns a final verdict:
   - **Score 5+:** Strong 
   - **Score 3-4:** Moderate 
   - **Score 0-2:** Weak (Needs improvement)

## 🛠️ How to Run
To run this script locally, you need Python 3 installed.
1. Open your terminal.
2. Navigate to this folder.
3. Run: `python password_checker.py`

## 📚 Skills Demonstrated
*   Python 3
*   Regular Expressions (Regex)
*   Conditional Logic (If/Elif/Else)
*   Cybersecurity Fundamentals (Password Policies)
# Quiz Game with Tkinter

This is a simple **Quiz Game** built with Python's `Tkinter` library. The game allows users to answer multiple-choice questions, with a timer for each question. It also tracks the score and stores the highest score in a text file.

## Features

- Timer for each question (15 seconds per question).
- Randomized questions and answer options.
- Tracks the score as you go.
- Saves and displays the high score.
- Simple, interactive GUI with `Tkinter`.

## Code Explanation

### 1. Importing Libraries

```python
import tkinter as tk
from tkinter import messagebox
from quiz_data import quiz_questions
import random
import os
```
* *   **`TIME_LIMIT`**: Defines the time allowed for each question (15 seconds).
*     
* *   **`HIGHSCORE_FILE`**: Specifies the file used to store the highest score.
*     

### 3\. **QuizApp Class**

The `QuizApp` class contains the main logic of the quiz game, from UI setup to question handling and score management.

#### Constructor: `__init__(self, root)`

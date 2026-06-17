# Intro to Scripting Languages

Portfolio repository for an Intro to Scripting Languages college course completed in Summer 2024.

The original submissions are preserved as Word documents in `docs/original-submissions/`. The Python files in `labs/` were reconstructed from the submitted documents and their embedded screenshots so the work is easier to review in GitHub.

## Course Context

- Student: Devin Thomas
- Course: Intro to Scripting Languages
- Term completed: Summer 2024
- Institution: Alamo Colleges
- Campus note: the document metadata lists `SAC, NVC`, so the repo uses Alamo Colleges rather than choosing one campus.

## What This Shows

This coursework demonstrates introductory scripting concepts in Python:

- recognizing patterns and translating simple logic into code
- using IDEs such as IDLE, Visual Studio Code, and PyCharm
- creating variables and constants
- using numeric expressions, floats, and formatted output
- indexing strings and using string length
- writing conditional logic with relational and logical operators
- iterating with `for` and `while` loops
- organizing scripts with `main()` functions

## Repository Structure

```text
.
|-- docs/
|   `-- original-submissions/   # Original .docx lab submissions
|-- labs/                       # Python versions of the lab work
|-- .gitignore
`-- README.md
```

## Lab Index

| Lab | Topic | Python file | Original submission |
| --- | --- | --- | --- |
| 1.3 | Pattern identification | `labs/lab_1_3_pattern_identification.py` | `Lab 1.3 Pattern Identification.docx` |
| 1.4 | Abstraction basics | `labs/lab_1_4_abstraction_basics.py` | `Lab 1.4 Abstraction Basics (1).docx` |
| 2.5 | IDLE basics | `labs/lab_2_5_idle_hello_world.py` | `Lab 2.5 Integrated Development Environments (IDLE).docx` |
| 2.6 | Visual Studio Code basics | `labs/lab_2_6_visual_studio_code.py` | `Lab 2.6 Visual Studio Code.docx` |
| 3.2 | Variables and constants | `labs/lab_3_2_variables_and_constants.py` | `Lab 3.2 Variables and Constants.docx` |
| 3.3 | Initializing variables | `labs/lab_3_3_initializing_variables.py` | `Lab 3.3 Initializing Variables.docx` |
| 4.1 | Mathematical expressions | `labs/lab_4_1_mathematical_expressions.py` | `Lab 4.1 Mathematical Expressions.docx` |
| 4.4 | Rounding quirks | `labs/lab_4_4_rounding_quirks.py` | `Lab 4.4 Rounding Quirks.docx` |
| 5.2 | String indexes | `labs/lab_5_2_string_indexes.py` | `Lab 5.2 String Indexes.docx` |
| 5.3 | String length | `labs/lab_5_3_string_length.py` | `Lab 5.3 String Length.docx` |
| 6.2 | Relational operators | `labs/lab_6_2_relational_operators.py` | `Lab 6.2 Using Relational Operators.docx` |
| 6.4 | Conditional logical operators | `labs/lab_6_4_conditional_logical_operators.py` | `Lab 6.4 Conditional Logical Operators.docx` |
| 7.1 | For loops | `labs/lab_7_1_for_loops.py` | `Lab 7.1 For Loops.docx` |
| 7.4 | While loops | `labs/lab_7_4_while_loops.py` | `Lab 7.4 While Loops.docx` |

## Notes

- The original `.docx` files are included for provenance and to preserve the submitted lab format.
- Both Lab 1.4 Word files are preserved; the Python transcription maps to `Lab 1.4 Abstraction Basics (1).docx`, which contains the code screenshot.
- Most code appeared in screenshots rather than selectable document text, so the `.py` files are careful transcriptions for GitHub readability.
- The scripts are intentionally left close to the original beginner coursework rather than refactored into a polished application.
- This repository is shared as a portfolio artifact, not as a template for current coursework submissions.

## Running The Scripts

Use Python 3 to run any individual lab file:

```powershell
python labs/lab_4_1_mathematical_expressions.py
```

Several scripts prompt for keyboard input. No third-party packages are required.

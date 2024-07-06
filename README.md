# Arithmetic Arranger

## Description

`arithmetic_arranger` is a Python function that arranges arithmetic problems vertically and side-by-side, making them easier to solve. It can optionally display the answers to the problems. This project is particularly useful for primary school students who often need to organize arithmetic problems in this manner.

## Features

- Supports addition and subtraction problems.
- Aligns numbers and operators correctly for easy readability.
- Optionally displays the answers to the arithmetic problems.
- Handles up to five problems at a time.
- Validates input to ensure problems are correctly formatted.

## Usage

### Function Definition

```python
def arithmetic_arranger(problems, show_answers=False):
    """
    Arranges arithmetic problems vertically and side-by-side.

    Parameters:
        problems (list): List of strings containing arithmetic problems.
        show_answers (bool): If True, displays the answers.

    Returns:
        str: The arranged problems or an error message.
    """
    # Vérification des erreurs
    if len(problems) > 5:
        return "Error: Too many problems."
    
    first_line = ""
    second_line = ""
    dashes_line = ""
    answers_line = ""

    for problem in problems:
        parts = problem.split()
        operand1 = parts[0]
        operator = parts[1]
        operand2 = parts[2]

        # Vérification des opérateurs valides
        if operator not in ["+", "-"]:
            return "Error: Operator must be '+' or '-'."
        
        # Vérification que les opérandes sont numériques
        if not operand1.isdigit() or not operand2.isdigit():
            return "Error: Numbers must only contain digits."

        # Vérification de la taille des opérandes
        if len(operand1) > 4 or len(operand2) > 4:
            return "Error: Numbers cannot be more than four digits."

        # Calcul des largeurs nécessaires
        width = max(len(operand1), len(operand2)) + 2
        top = operand1.rjust(width)
        bottom = operator + operand2.rjust(width - 1)
        line = "-" * width
        answer = str(eval(problem)).rjust(width)

        # Ajouter les morceaux formatés aux lignes respectives
        if first_line:
            first_line += "    "
            second_line += "    "
            dashes_line += "    "
            if show_answers:
                answers_line += "    "

        first_line += top
        second_line += bottom
        dashes_line += line
        if show_answers:
            answers_line += answer

    problems = first_line + "\n" + second_line + "\n" + dashes_line
    if show_answers:
        problems += "\n" + answers_line

    return problems
```

## Args
problems: A list of strings, where each string is an arithmetic problem. For example: ["32 + 698", "3801 - 2", "45 + 43", "123 + 49"].
show_answers: A boolean value. If set to True, the answers to the arithmetic problems will be displayed.

## Example Calls
```python
    # Arrange problems without answers
    print(arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"]))
    
    # Arrange problems with answers
    print(arithmetic_arranger(["32 + 8", "1 - 3801", "9999 + 9999", "523 - 49"], True))
```
## Output
```plaintext
  32         1      9999      523
+  8    - 3801    + 9999    -  49
----    ------    ------    -----

  32         1      9999      523
+  8    - 3801    + 9999    -  49
----    ------    ------    -----
  40     -3800     19998      474
```

## Error Handling
The function will return meaningful error messages in the following cases:

- If more than five problems are provided: "Error: Too many problems."
- If an operator other than + or - is used: "Error: Operator must be '+' or '-'."
- If an operand contains non-digit characters: "Error: Numbers must only contain digits."
- If an operand has more than four digits: "Error: Numbers cannot be more than four digits."

## Contributing
Contributions are welcome! If you have any suggestions or improvements, please create an issue or submit a pull request.


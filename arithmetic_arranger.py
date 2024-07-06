def arithmetic_arranger(problems, show_answers=False):
    """
    Arranges arithmetic problems vertically and side-by-side.

    Args:
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

print(f'\n{arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"],True)}')

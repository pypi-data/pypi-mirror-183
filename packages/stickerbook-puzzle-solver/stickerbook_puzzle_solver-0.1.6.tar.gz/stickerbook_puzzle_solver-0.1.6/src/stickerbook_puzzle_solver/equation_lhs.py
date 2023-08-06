class RowOrColumn:
    """
    Calculate the left hand side of a puzzle equation
    given the three numbers and two operations
    """

    def __init__(self):
        self._lhs = None

    def build_equation(
            self,
            number_1: int,
            operation_1: str,
            number_2: int,
            operation_2: str,
            number_3: float,
            output: float
    ) -> bool:
        self.build_lhs(
            number_1,
            operation_1,
            number_2,
            operation_2,
            number_3
        )

        return self.check_equals(output)

    def check_equals(self, output: float):
        return self._lhs == output

    def build_lhs(
            self,
            number_1: int,
            operation_1: str,
            number_2: int,
            operation_2: str,
            number_3: float
    ) -> None:
        """
        E.g. build_lhs(number_1, '+', number_2, '*', number_3) does
        (number_1 + number_2) * number_3
        params:
        number_1: int. First number in equation
        operation_1: str. Must be '+', '-', '*', '/'
        number_2: int. Second number in equation
        operation_2: str. Must be '+', '-', '*', '/'
        number_3: float. Third number in equation
        return: int
        """
        step_1 = self.apply_string_operation(number_1=number_1, operation_string=operation_1, number_2=number_2)
        step_2 = self.apply_string_operation(number_1=step_1, operation_string=operation_2, number_2=number_3)

        self._lhs = step_2


    def apply_string_operation(
            self,
            number_1: float,
            operation_string: str,
            number_2: float
    ) -> float:
        """
        Perform one of the four key operation according to which key word was entered
        a: First number in expression
        operation_word: str. Must be '+', '-', '*', '/'
        b: Second number in expression
        """
        if operation_string == '+':
            return number_1 + number_2
        elif operation_string == '-':
            return number_1 - number_2
        elif operation_string == '*':
            return number_1 * number_2
        elif operation_string == '/':
            return number_1 / number_2

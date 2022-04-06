from datetime import datetime

from com.frogmi.task.exceptions.InvalidDateRangeError import InvalidDateRangeError


class Incident:
    def __init__(self, description, action_to_solve, open_date):
        self.description = description
        self.action_to_solve = action_to_solve
        self.open_date = datetime.strptime(open_date, "%d/%m/%Y")
        self.state = "open"
        self.solved_date = None

    # method to solve incident with a determined solved date
    def solve_incident(self, solved_date):
        self.state = "solved"
        format_solved_date = datetime.strptime(solved_date, "%d/%m/%Y")
        if format_solved_date < self.open_date:
            raise InvalidDateRangeError(self.open_date, format_solved_date)
        self.solved_date = format_solved_date

from datetime import datetime

from com.frogmi.task.exceptions.InvalidDateRangeError import InvalidDateRangeError


class Store:
    def __init__(self, incidents):
        self.incidents = incidents

    def incident_status(self, init_date_str, end_date_str):

        init_date = datetime.strptime(init_date_str, "%d/%m/%Y")
        end_date = datetime.strptime(end_date_str, "%d/%m/%Y")

        if end_date < init_date:
            raise InvalidDateRangeError(init_date, end_date)

        open_cases = 0
        solved_cases = 0

        # aux variable to store the total days of solving all the incidents in the period of time
        total_days_solved = 0
        max_solved_time = 0
        for incident in self.incidents:
            # it will only take account the open incidents between those dates
            open_date_cond = init_date <= incident.open_date <= end_date
            # it will only take account the solved incidents between those dates
            solved_date_cond = incident.solved_date is not None and init_date <= incident.solved_date <= end_date

            if open_date_cond and incident.state == "open":
                open_cases += 1
                current_time = (datetime.now() - incident.open_date).days
                if current_time > max_solved_time:
                    max_solved_time = current_time
            elif solved_date_cond and incident.state == "solved":
                solved_cases += 1
                solved_days = (incident.solved_date - incident.open_date).days
                total_days_solved += solved_days
                if solved_days > max_solved_time:
                    max_solved_time = solved_days

        if solved_cases != 0:
            avg_time = round((total_days_solved / solved_cases))
        else:
            avg_time = 0

        return {'open_cases': open_cases,
                'closed_cases': solved_cases,
                'average_solution': avg_time,
                'maximum_solution': max_solved_time}

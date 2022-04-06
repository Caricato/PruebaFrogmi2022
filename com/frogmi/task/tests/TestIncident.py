import unittest

from com.frogmi.task.exceptions.InvalidDateRangeException import InvalidDateRangeException
from com.frogmi.task.models.Incident import Incident


class TestIncident(unittest.TestCase):
    def setUp(self):
        pass

    def test_error_format_open_date(self):
        self.assertRaises(ValueError, Incident, "The floor needs mopping", "Mop the floor", "02/31/2022")

    def test_error_date_solve_incident(self):
        incident_1 = Incident("The floor needs mopping", "Mop the floor", "02/04/2022")

        self.assertRaises(InvalidDateRangeException, incident_1.solve_incident, "01/04/2022")

    def test_solve_incident(self):
        incident_1 = Incident("The floor needs mopping", "Mop the floor", "02/04/2022")
        incident_1.solve_incident("04/04/2022")

        self.assertEqual(incident_1.state, "solved")


if __name__ == '__main__':
    unittest.main()

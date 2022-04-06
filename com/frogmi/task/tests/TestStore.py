import unittest

from com.frogmi.task.exceptions.InvalidDateRangeError import InvalidDateRangeError
from com.frogmi.task.models.Incident import Incident
from com.frogmi.task.models.Store import Store


class TestStore(unittest.TestCase):
    def setUp(self):
        pass

    def test_error_date_range(self):
        new_store = Store(incidents=[])
        self.assertRaises(InvalidDateRangeError, new_store.incident_status, "31/12/2022", "01/01/2022")

    def test_empty_incidents(self):
        new_store = Store(incidents=[])
        result = new_store.incident_status("01/01/2022", "31/12/2022")

        print(result)

        self.assertEqual(result.get("open_cases"), 0)
        self.assertEqual(result.get("closed_cases"), 0)
        self.assertEqual(result.get("average_solution"), 0)
        self.assertEqual(result.get("maximum_solution"), 0)

    def test_only_open_cases(self):
        incident_1 = Incident("The floor needs mopping", "Mop the floor", "02/04/2022")
        incident_2 = Incident("Fix the vending machine", "Call an electrician", "04/04/2022")

        # Incident not included in the date range
        incident_3 = Incident("The door is broken", "Buy a new door", "04/04/2021")

        new_store = Store(incidents=[incident_1, incident_2, incident_3])
        result = new_store.incident_status("01/01/2022", "31/12/2022")

        print(result)

        self.assertEqual(result.get("open_cases"), 2)
        self.assertEqual(result.get("closed_cases"), 0)
        self.assertEqual(result.get("average_solution"), 0)
        self.assertEqual(result.get("maximum_solution"), 4)

    def test_only_closed_cases(self):
        incident_1 = Incident("The floor needs mopping", "Mop the floor", "02/04/2022")
        incident_2 = Incident("Fix the vending machine", "Call an electrician", "04/04/2022")

        # Incident not included in the date range
        incident_3 = Incident("The door is broken", "Buy a new door", "04/04/2021")

        # solve the incidents two days later
        incident_1.solve_incident("04/04/2022")
        incident_2.solve_incident("06/04/2022")

        new_store = Store(incidents=[incident_1, incident_2, incident_3])
        result = new_store.incident_status("01/01/2022", "31/12/2022")

        print(result)

        self.assertEqual(result.get("open_cases"), 0)
        self.assertEqual(result.get("closed_cases"), 2)
        self.assertEqual(result.get("average_solution"), 2)
        self.assertEqual(result.get("maximum_solution"), 2)

    def test_open_and_closed_cases(self):
        incident_1 = Incident("The floor needs mopping", "Mop the floor", "02/04/2022")
        incident_2 = Incident("Fix the vending machine", "Call an electrician", "04/04/2022")
        incident_3 = Incident("We are out of soap", "Buy more soap", "15/03/2022")
        incident_4 = Incident("The door needs cleaning", "Clean the door", "01/01/2022")

        # Incident not included in the date range
        incident_5 = Incident("We are out of bubble gum", "Order more bubble gum", "03/12/2021")

        # solve the incidents two days later
        incident_1.solve_incident("04/04/2022")
        incident_2.solve_incident("06/04/2022")

        new_store = Store(incidents=[incident_1, incident_2, incident_3, incident_4, incident_5])
        result = new_store.incident_status("01/01/2022", "31/12/2022")

        print(result)

        self.assertEqual(result.get("open_cases"), 2)
        self.assertEqual(result.get("closed_cases"), 2)
        self.assertEqual(result.get("average_solution"), 2)
        self.assertEqual(result.get("maximum_solution"), 95)


if __name__ == '__main__':
    unittest.main()

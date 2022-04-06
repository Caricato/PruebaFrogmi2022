from com.frogmi.task.models.Incident import Incident
from com.frogmi.task.models.Store import Store

if __name__ == '__main__':
    incident_n1 = Incident("Something happened", "Do Something!", "04/03/2022")
    incident_n1.open_date
    incident_n2 = Incident("Resolve this", "Ok", "01/05/2022")

    incident_n2.solve_incident("13/05/2022")

    new_store = Store([incident_n1, incident_n2])
    response = new_store.incident_status("01/01/2022", "31/12/2022")
    print(response)


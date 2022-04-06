class InvalidDateRangeError(Exception):
    def __init__(self, init_date, end_date):
        self.init_date = init_date
        self.end_date = end_date
        self.message = "The start date is more recent than the end date"
        super().__init__(self.message)

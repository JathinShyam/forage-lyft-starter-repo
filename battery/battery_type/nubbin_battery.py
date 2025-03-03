from battery.battery import Battery

class NubbinBattery(Battery):
    def __init__(self, current_date, last_service_date):
        self.current_date = current_date
        self.last_service_date = last_service_date
        self.nubbin_year_service = 3

    def needs_service(self):
        date_service_threshold = self.last_service_date.replace(year = self.last_service_date.year + self.nubbin_year_service)
        if date_service_threshold < self.current_date:
            return True
        else:
            return False

from battery.battery import Battery

class NubbinBattery(Battery):
    def __init__(self, current_date, last_service_date):
        self.current_date = current_date
        self.last_service_date = last_service_date
        self.nubbin_year_service = 4

    def needs_service(self, current_date, last_service_date):
        date_service_threshold = last_service_date.replace(year = self.current_date.year + self.nubbin_year_service_after)
        if date_service_threshold < current_date:
            return True
        else:
            return False

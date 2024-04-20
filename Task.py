class Task:
    def __init__(self, name, duration,
                 duration_buff_late_days=0,
                 duration_buff_early_days=0):
        self.name = name
        self.duration_days = duration_days
        self.duration_buff_early_days = duration_buff_late_days
        self.duration_buff_late_days = duration_buff_early_days

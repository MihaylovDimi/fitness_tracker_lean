"""FitnessTracker MVP: log runs, estimate calories and set a weekly goal."""

RUNNING_MET = 9.8
WALKING_MET = 3.5
CYCLING_MET = 7.5


class FitnessTracker:
    def __init__(self):
        self.runs = []
        self.weekly_goals = {}

    def log_run(self, distance_in_km, elapsed_time_minutes):
        run_record = {
            "distance_in_km": distance_in_km,
            "elapsed_time_minutes": elapsed_time_minutes,
        }
        self.runs.append(run_record)

    def calories_running(self, weight_in_kg, elapsed_time_minutes):
        return self._calculate_calories(RUNNING_MET, weight_in_kg, elapsed_time_minutes)

    def calories_walking(self, weight_in_kg, elapsed_time_minutes):
        return self._calculate_calories(WALKING_MET, weight_in_kg, elapsed_time_minutes)

    def calories_cycling(self, weight_in_kg, elapsed_time_minutes):
        return self._calculate_calories(CYCLING_MET, weight_in_kg, elapsed_time_minutes)

    def _calculate_calories(self, met, weight_in_kg, elapsed_time_minutes):
        hours = elapsed_time_minutes / 60
        return round(met * weight_in_kg * hours, 1)

    def set_weekly_goal(self, week_start, distance_in_km):
        self.weekly_goals[week_start] = distance_in_km

    def get_weekly_goal(self, week_start):
        return self.weekly_goals.get(week_start)

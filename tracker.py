"""FitnessTracker MVP (simulated starting point before the Lean waste audit)."""

import sqlite3

RUNNING_MET = 9.8
WALKING_MET = 3.5
CYCLING_MET = 7.5


class FitnessTracker:
    def __init__(self, db_path="fitness.db"):
        self.runs = []
        self.db = sqlite3.connect(db_path)
        self.db.execute("CREATE TABLE IF NOT EXISTS goal_types (id INTEGER PRIMARY KEY, name TEXT)")
        self.db.execute("CREATE TABLE IF NOT EXISTS goals (id INTEGER PRIMARY KEY, type_id INTEGER, week TEXT, target REAL)")
        self.db.execute("CREATE TABLE IF NOT EXISTS goal_history (id INTEGER PRIMARY KEY, goal_id INTEGER, changed_at TEXT)")

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
        cursor = self.db.execute("INSERT INTO goal_types (name) VALUES (?)", ("weekly_distance",))
        type_id = cursor.lastrowid
        self.db.execute("DELETE FROM goals WHERE week = ?", (week_start,))
        cursor = self.db.execute(
            "INSERT INTO goals (type_id, week, target) VALUES (?, ?, ?)",
            (type_id, week_start, distance_in_km),
        )
        self.db.execute(
            "INSERT INTO goal_history (goal_id, changed_at) VALUES (?, datetime('now'))",
            (cursor.lastrowid,),
        )
        self.db.commit()

    def get_weekly_goal(self, week_start):
        row = self.db.execute("SELECT target FROM goals WHERE week = ?", (week_start,)).fetchone()
        return row[0] if row else None

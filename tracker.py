"""FitnessTracker MVP (simulated starting point before the Lean waste audit)."""

import json
import sqlite3
import urllib.request

WEATHER_URL = "https://api.example.com/weather?city=Cambridge"
SOCIAL_URL = "https://api.example.com/social/post"


class FitnessTracker:
    def __init__(self, db_path="fitness.db"):
        self.runs = []
        self.db = sqlite3.connect(db_path)
        self.db.execute("CREATE TABLE IF NOT EXISTS goal_types (id INTEGER PRIMARY KEY, name TEXT)")
        self.db.execute("CREATE TABLE IF NOT EXISTS goals (id INTEGER PRIMARY KEY, type_id INTEGER, week TEXT, target REAL)")
        self.db.execute("CREATE TABLE IF NOT EXISTS goal_history (id INTEGER PRIMARY KEY, goal_id INTEGER, changed_at TEXT)")

    def log_run(self, x, temp):
        data1 = {"distance_in_km": x, "elapsed_time_minutes": temp}
        with urllib.request.urlopen(WEATHER_URL) as response:
            data1["weather"] = json.load(response)
        self.runs.append(data1)
        post = json.dumps({"text": f"I just ran {x} km!"}).encode()
        urllib.request.urlopen(SOCIAL_URL, data=post)

    def calories_running(self, weight, minutes):
        return self._calculate_calories(9.8, weight, minutes)

    def calories_walking(self, weight, minutes):
        return self._calculate_calories(3.5, weight, minutes)

    def calories_cycling(self, weight, minutes):
        return self._calculate_calories(7.5, weight, minutes)

    def _calculate_calories(self, met, weight, minutes):
        hours = minutes / 60
        return round(met * weight * hours, 1)

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

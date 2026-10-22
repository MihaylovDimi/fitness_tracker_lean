"""Baseline unit tests for the FitnessTracker MVP."""

import unittest

from tracker import FitnessTracker


class FitnessTrackerTest(unittest.TestCase):
    def setUp(self):
        self.tracker = FitnessTracker()

    def test_log_run_records_distance_and_time(self):
        self.tracker.log_run(distance_in_km=5, elapsed_time_minutes=30)

        self.assertEqual(
            self.tracker.runs, [{"distance_in_km": 5, "elapsed_time_minutes": 30}]
        )

    def test_calories_use_the_met_value_of_each_activity(self):
        self.assertEqual(self.tracker.calories_running(70, 30), 343.0)
        self.assertEqual(self.tracker.calories_walking(70, 30), 122.5)
        self.assertEqual(self.tracker.calories_cycling(70, 30), 262.5)

    def test_new_goal_for_the_same_week_replaces_the_old_one(self):
        self.tracker.set_weekly_goal("2026-10-19", 15)
        self.tracker.set_weekly_goal("2026-10-19", 20)

        self.assertEqual(self.tracker.get_weekly_goal("2026-10-19"), 20)

    def test_week_without_a_goal_returns_none(self):
        self.assertIsNone(self.tracker.get_weekly_goal("2026-10-26"))


if __name__ == "__main__":
    unittest.main()

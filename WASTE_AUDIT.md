# Waste Audit: FitnessTracker MVP

This audit reviews `tracker.py` against the Week 4 user stories (Log a Run, Set a Weekly Goal, View Weekly Progress). Anything the stories do not ask for, or anything that makes the code harder to change, is treated as waste (muda).

## Findings

| # | Where | Waste | Why it is waste |
|---|---|---|---|
| 1 | `log_run()` fetches weather data and posts to a social media API | Needless Complexity (gold-plating) | No user story asks for weather or social sharing. It was added "just in case". |
| 2 | `calories_running()`, `calories_walking()`, `calories_cycling()` | Needless Repetition | The three methods repeat the same calculation and differ only by one number. |
| 3 | `x`, `temp`, `data1` and the numbers 9.8, 3.5, 7.5 | Opacity | The names and bare numbers do not say what they mean, so the code has to be decoded before it can be changed. |
| 4 | Three database tables (`goal_types`, `goals`, `goal_history`) for the weekly goal | Needless Complexity (YAGNI) | The story only needs one number per week. A dictionary is enough for the MVP. |

## Why the weather and social features are gold-plating

The "Log a Run" story only asks to save the distance and the duration of a run. Fetching the weather and posting to social media were never requested by the customer, so they add cost without adding value. They also make the core feature depend on two outside services.

## Impact on Sustainable Pace

1. **Extra maintenance for ever.** Two third-party APIs can change, ask for keys or stop working. Every time that happens the team has unplanned work on something nobody asked for, which takes time away from real stories.
2. **Slower and more fragile feedback.** `log_run()` cannot be unit tested without mocking two external services, which is why the baseline tests do not cover it. If the weather service is down, logging a run fails, so the main feature of the app breaks because of an unrequested extra.

## Plan

1. Refactor the calorie methods to use one private helper (Once and Only Once).
2. Rename the opaque variables and give the MET values names (Boy Scout Rule).
3. Remove the weather and social media code from `log_run()`.
4. Replace the goal tables with a simple dictionary.

The baseline tests must stay green after every step.

# Reflection: Lean Waste Audit of the FitnessTracker MVP

## 1. How does "maximizing the amount of work not done" help you deliver valuable software to the customer faster?

By removing the unrequested features and the three database tables, we reduced the amount of code that has to be maintained and tested. This saved time and lowered the risk of errors, while keeping everything the user stories actually need.

## 2. Which Lean waste did you find most difficult to identify in the FitnessTracker MVP?

The hardest one to spot was the three unnecessary database tables, because they looked like a good engineering decision. Only when we compared them with the requirements in the user stories did it become clear that a simple dictionary was enough.

## 3. How does the practice of the Boy Scout Rule prevent "Software Rot" from accumulating as the project grows?

The Boy Scout Rule means leaving the code a little better than we found it. Because we made small changes, ran the tests after each one and saved every step in a separate commit, we could find problems quickly and improve the code gradually, instead of letting technical debt pile up.

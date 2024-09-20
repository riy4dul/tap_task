<h3># Worker Pay Calculator</h3>

This project provides a Python solution to calculate the total salary of a part-time worker based on varying hourly rates throughout the day. The pay rates differ depending on the time worked: regular hours (9:00 AM to 5:00 PM), nighttime hours (5:00 PM to 10:00 PM), and midnight hours (all other times).

## Problem Statement

The hourly rates are as follows:
- **X Yen/hour** for regular hours (9:00 AM to 5:00 PM).
- **Y Yen/hour** for nighttime hours (5:00 PM to 10:00 PM).
- **Z Yen/hour** for midnight hours (10:00 PM to 9:00 AM).

The worker's start and end times for `N` days are provided in one-hour increments. The program calculates the total amount of money the worker will earn over these `N` days.



```bash
python Tap_Task.py
1000 1300 1500 4 0 9 9 17 17 22 22 23 # Input string
29500                                 # Output total earnings

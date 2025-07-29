# URECA Project – Crazyflie Drone Control

This repository contains the code used in my URECA (Undergraduate Research Experience on CAmpus) project at Nanyang Technological University on **Advancing Omnidirectional Wireless Power Transfer for Drone Charging**. The drone was controlled using Bitcraze’s [Crazyflie 2.1](https://www.bitcraze.io/products/crazyflie-2-1/) equipped with the Flowdeck for indoor positioning.

This repo focuses on the control code and system setup.

---

## Background

The aim of the project was to test the performance of wireless charging under magnetically coupled conditions. As part of the testing framework, we automated drone hovering and landing using Python and the Crazyflie Python library (`cflib`). This helped us conduct consistent and repeatable experiments during wireless charging trials.

---

## What This Code Does

- Initializes communication with the Crazyflie via Crazyradio PA
- Takes off to a height of 15 cm using `MotionCommander`
- Hovers for 10 seconds (fixed)
- Lands automatically and stops all motion

---

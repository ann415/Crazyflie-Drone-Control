# System Setup and Experimental Configuration

This document outlines the system setup used in the URECA project for automating drone hover tests using the Crazyflie 2.1 platform.

---

## Hardware Components

| Component                  | Description                                                  |
|---------------------------|--------------------------------------------------------------|
| Crazyflie 2.1             | Nano quadcopter used for indoor flight and hovering          |
| Flowdeck v2               | Optical flow and range sensor for position stabilization     |
| Crazyradio PA             | USB radio dongle to communicate with the drone               |
| Wireless Power Coils      | Custom transmitter and receiver coil setup (under testing)   |
| Power Supply + Oscilloscope | For measuring voltage/current during OWPT testing           |
| Laptop (Ubuntu/Windows)   | Runs Python control script and logs data                     |

---

## Environment Setup

- **Indoor** testbed with minimal airflow or external disturbances
- Non-metallic landing surface placed over wireless charging coil

---

## Experiment Configuration

- **Takeoff Height**: 15 cm (set in `MotionCommander`)
- **Hover Duration**: 10 seconds (fixed delay for stable measurement)
- **Landing**: Automatic after hover
- **Data Collection**: Oscilloscope probes placed at receiver circuit

---

## Connection and Initialization

1. Connect **Crazyradio PA** to your laptop via USB.
2. Power on the **Crazyflie 2.1** with Flowdeck attached.
3. Make sure `radio://0/80/2M/E7E7E7E7E7` URI matches your device (or modify in code).
4. Run `main.py` to execute automated takeoff–hover–land sequence.

---

## Software Setup

- Install Python 3.8+ with `pip`
- Install `cflib` using:

```bash
pip install cflib

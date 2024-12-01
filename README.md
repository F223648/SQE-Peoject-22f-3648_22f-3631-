# Chaos Engineering Project

This project demonstrates the principles and practices of **Chaos Engineering** to test the reliability and resilience of a system by intentionally introducing failures and disruptions.

### **Project Overview**

Chaos Engineering focuses on simulating real-world failures to ensure that systems are resilient under stress. This project implements chaos experiments in a simple Flask application, which includes:
- **Failure Simulation**: Random server failure to simulate infrastructure crashes.
- **Delay Experiment**: Simulate random response delays.
- **Gremlin Experiment**: Introduce CPU stress to simulate resource exhaustion.
- **Chaos Monkey**: Randomly crashes the server to test recovery mechanisms.

### **Requirements**

To run this project locally, you need:
- **Python 3.x** 
- **Flask**: For running the web application.
- **Random**: Used for simulating failures.
- **Time**: To simulate delays.
- **Logging**: For capturing logs during chaos experiments.
- **Sys**: For terminating the server.

You can install the necessary dependencies using `pip`:
```bash
pip install -r requirements.txt

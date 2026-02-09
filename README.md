# Delivery Routing Simulator

A command-line delivery routing simulator built in Python that models a parcel delivery system with multiple trucks, delivery constraints, and time-based package tracking.

The routing logic is based on a **greedy nearest-neighbor heuristic**, a common approximation approach for problems related to the **Traveling Salesman Problem (TSP)** and the **Vehicle Routing Problem (VRP)**.  
The system uses a custom-built hash table to enable constant-time package lookups and real-time delivery status checks.

---

## Tech Stack

- Python 3
- Custom hash table implementation
- Greedy nearest-neighbor routing algorithm
- Command-line interface (CLI)

---

## Problem Context

This project simulates a delivery scenario similar to real-world logistics systems.  
The routing challenge is a variation of the **Traveling Salesman Problem**, which is an **NP-hard optimization problem**.

In this scenario:

- Multiple trucks must deliver packages to different addresses.
- Each package has constraints such as deadlines or special conditions.
- The total distance traveled must remain under a fixed limit.
- Only a limited number of drivers are available.

This turns the problem into a simplified **Vehicle Routing Problem (VRP)**, which is a practical extension of the Traveling Salesman Problem used in logistics and transportation systems.

Because optimal solutions to TSP/VRP are computationally expensive, this system uses a **greedy nearest-neighbor heuristic** to produce efficient delivery routes in polynomial time.

---

## Features

- Custom hash table for constant-time package lookup
- Greedy nearest-neighbor routing algorithm
- Simulation of three delivery trucks with constraints
- Real-time package status tracking:
  - At hub
  - En route
  - Delivered with timestamp
- Total mileage calculation across all trucks
- Interactive terminal menu for status queries

---

## Algorithm Overview

The routing system uses a **greedy nearest-neighbor approach**:

1. Each truck starts at the hub with assigned packages.
2. The algorithm selects the nearest valid delivery address.
3. The package is delivered and marked with a timestamp.
4. The truck repeats the process until all packages are delivered.

This method:

- Runs in polynomial time
- Produces efficient routes with low computational cost
- Satisfies all delivery constraints in the simulation

---

## Data Structure

Packages are stored in a **custom hash table**:

- Each package is indexed by its unique package ID.
- Full package data is stored in each hash entry.
- Lookup operations run in constant time (O(1)).
- Enables real-time status checks at any point in the simulation.

---

Project Context


The objective was to design a delivery system that:

    Delivers all packages on time
    Handles special delivery constraints
    Keeps total mileage under a fixed limit
    Allows status checks at any time during the simulation

The focus of the project was on:

    Algorithm design
    Data structure implementation
    Efficiency and correctness under constraints

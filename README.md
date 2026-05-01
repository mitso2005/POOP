# SafeCheck

*A Python OOP Assignment — Fire Safety Equipment Maintenance System*

**Three-Part Progressive Assignment**
Covers: Classes • Inheritance • Abstraction • Polymorphism • Composition • Magic Methods • Properties • Exceptions • Module Structure

---

You will build this across multiple files inside a `safecheck/` project folder.

## Overview

You are building **SafeCheck** — a command-line Python system for managing fire safety equipment across buildings.

By the end of all three parts, the system will be able to:

* Track assets
* Run inspections
* Raise alerts
* Print summary reports

Real professional Python codebases are not a single file. Each class lives in its own module. A dedicated entry point ties everything together.

> **Note:** Read each part in full before writing any code. Understanding the destination makes the structure much clearer.

---

# Concepts by Part

| Part   | Day      | Concepts                                                                                                                        |
| ------ | -------- | ------------------------------------------------------------------------------------------------------------------------------- |
| Part 1 | Saturday | Classes, `__init__`, instance & class variables, inheritance, `super()`, `isinstance()`, modules & imports                      |
| Part 2 | Sunday   | Abstract classes, polymorphism, composition, static methods, class methods, `@property`, custom exceptions, list comprehensions |
| Part 3 | Monday   | Magic methods (`__str__`, `__repr__`, `__eq__`, `__len__`), aggregation, duck typing, full system integration                   |

---

# Final Project Structure

```text
safecheck/
├── assets/
│   ├── __init__.py        # marks assets/ as a package
│   ├── base.py            # SafetyAsset base class
│   └── devices.py         # FireExtinguisher, SmokeDetector, FireDoor
├── exceptions.py          # custom exception classes
├── building.py            # Building class
├── technician.py          # Technician class
├── utils.py               # helper functions
└── main.py                # entry point
```

> **Interview Tip:** Splitting code into modules demonstrates the **Single Responsibility Principle**.

---

# Part 1 — The Asset Registry

**Concepts:** Classes, `__init__`, instance & class variables, inheritance, `super()`, `isinstance()`, modules & imports

## Background

Uptick's platform tracks fire safety assets installed in buildings.

Your first task is to build the data model.

---

## Task 1.0 — Set Up the Project Folder

### Concept: Modules & Packages

Create:

```bash
mkdir -p safecheck/assets
cd safecheck
touch assets/__init__.py
```

Project structure:

```text
safecheck/
└── assets/
    └── __init__.py
```

`__init__.py` tells Python that `assets/` is a package.

---

## Task 1.1 — SafetyAsset in Its Own Module

Create:

```text
assets/base.py
```

Structure:

```text
safecheck/
├── assets/
│   ├── __init__.py
│   └── base.py
```

### Requirements

Every asset has:

* `serial_number`
* `location`
* `last_inspected` (default: `"Never"`)

Add a method:

```python
describe()
```

Output:

```text
[EX-00142] SafetyAsset at Level 3, stairwell B (last inspected: 2024-11-01)
```

> **Interview Tip:** Write `describe()` early to simplify debugging.

---

## Task 1.2 — Tracking Assets with Class Variables

In `assets/base.py`:

Add:

```python
total_assets = 0
all_serials = []
```

Inside `__init__`:

```python
SafetyAsset.total_assets += 1
SafetyAsset.all_serials.append(serial_number)
```

> Use `SafetyAsset.total_assets`, not `self.total_assets`.

---

## Task 1.3 — Subclasses in a Separate Module

Create:

```text
assets/devices.py
```

Import:

```python
from assets.base import SafetyAsset
```

Create subclasses:

### FireExtinguisher

Adds:

* `extinguisher_type`

Override `describe()`.

---

### SmokeDetector

Adds:

* `detector_model`

Override `describe()`.

---

### FireDoor

Adds:

* `door_rating`

Override `describe()`.

---

## Task 1.4 — Use `super()`

Every subclass should call:

```python
super().__init__()
```

Only define subclass-specific attributes inside the child class.

---

## Task 1.5 — Utility Module and `isinstance()`

Create:

```text
utils.py
```

Structure:

```text
safecheck/
├── assets/
├── utils.py
```

Add:

```python
print_asset_summary(assets)
```

Function should:

1. Print total assets
2. Count each asset type
3. Call `describe()` on every asset

Use:

```python
isinstance()
```

Imports:

```python
from assets.devices import FireExtinguisher, SmokeDetector, FireDoor
```

---

## Task 1.6 — Main Entry Point

Create:

```text
main.py
```

Add:

```python
if __name__ == "__main__":
```

Demo should:

1. Create sample assets
2. Check `SafetyAsset.total_assets`
3. Print `all_serials`
4. Run `print_asset_summary()`

Run:

```bash
python main.py
```

---

## Part 1 Checklist

* `assets/base.py` contains `SafetyAsset`
* `assets/devices.py` contains subclasses
* `super().__init__()` used correctly
* `utils.py` contains `print_asset_summary()`
* `main.py` is entry point
* `total_assets` increments correctly

---

# Part 2 — Inspections, Buildings & Rules

**Concepts:** Abstract classes, polymorphism, composition, static methods, class methods, properties, exceptions

---

## Task 2.1 — Custom Exceptions

Create:

```text
exceptions.py
```

Add:

```python
class InspectionError(Exception):
    pass
```

---

## Task 2.2 — Abstract Inspection Interface

In `assets/base.py`:

```python
from abc import ABC, abstractmethod
```

Update:

```python
class SafetyAsset(ABC):
```

Add:

```python
@abstractmethod
def run_inspection(self):
    pass
```

Implement `run_inspection()` in all subclasses.

### FireExtinguisher

* Validate extinguisher type
* Raise `InspectionError` if invalid
* Update inspection date

### SmokeDetector

* Test alarm
* Update inspection date

### FireDoor

* Confirm latch/close
* Update inspection date

Import:

```python
from exceptions import InspectionError
```

---

## Task 2.3 — Polymorphism

Add to `utils.py`:

```python
run_all_inspections(assets)
```

Requirements:

* Loop through assets
* Call `.run_inspection()`
* No type checks

Import:

```python
from exceptions import InspectionError
```

---

## Task 2.4 — Building Class (Composition)

Create:

```text
building.py
```

### Building Properties

* `name`
* `address`
* `_assets` (private list)

Imports:

```python
from assets.base import SafetyAsset
from exceptions import InspectionError
```

Methods:

### `add_asset(asset)`

* Verify with `isinstance()`
* Prevent duplicate serial numbers
* Append to `_assets`

### `get_assets()`

Return a copy:

```python
return list(self._assets)
```

---

## Task 2.5 — Properties

Add:

```python
@property
def asset_count(self):
    return len(self._assets)
```

Protect `name` using getter/setter.

Raise:

```python
ValueError
```

for empty names.

---

## Task 2.6 — Static and Class Methods

### In `SafetyAsset`

Add:

```python
is_valid_serial(serial)
```

Rules:

* Two uppercase letters
* Hyphen
* At least 3 digits

Examples:

```text
EX-001
SD-0042
```

---

### In `Building`

Add classmethod:

```python
@classmethod
def from_dict(cls, data):
```

Example:

```python
Building.from_dict({
    "name": "Riverside Tower",
    "address": "42 Fire Lane"
})
```

---

## Task 2.7 — List Comprehensions

Add:

### `get_overdue_assets()`

```python
[x for x in self._assets if x.last_inspected == "Never"]
```

### `get_assets_by_type(asset_type)`

```python
[x for x in self._assets if isinstance(x, asset_type)]
```

---

## Task 2.8 — Update `main.py`

Demonstrate:

1. `Building.from_dict()`
2. Serial validation
3. Add assets
4. Run inspections
5. Overdue assets
6. Filter by type

---

## Part 2 Checklist

* `exceptions.py` exists
* `SafetyAsset` is abstract
* `run_all_inspections()` uses polymorphism
* `Building` works correctly
* Imports are clean
* `python main.py` runs

---

# Part 3 — Technicians, Reports & Polish

**Concepts:** Magic methods, aggregation, duck typing

---

## Task 3.1 — Magic Methods on `SafetyAsset`

Add:

### `__str__`

Human-readable:

```text
FireExtinguisher EX-001 at Lobby
```

### `__repr__`

Developer-readable:

```text
FireExtinguisher(serial='EX-001')
```

### `__eq__`

Two assets are equal if serial numbers match.

Return:

```python
NotImplemented
```

if wrong type.

---

## Task 3.2 — Magic Methods on `Building`

Add:

### `__len__`

```python
len(building)
```

### `__str__`

```text
Riverside Tower (42 Fire Lane) — 5 assets
```

---

## Task 3.3 — Technician (Aggregation)

Create:

```text
technician.py
```

Properties:

* `name`
* `licence_number`
* `_assigned_buildings`

Methods:

### `assign_to(building)`

Append building reference.

### `get_workload()`

Returns:

```text
Riverside Tower (5 assets)
```

Do not import `Building`.

---

## Task 3.4 — Duck Typing

In `utils.py`:

Add:

```python
print_report(obj)
```

Requirements:

* Call `summary()`
* Call `list_items()`
* No type checks

---

### Add to `Building`

```python
summary()
list_items()
```

---

### Create `InspectionLog`

Inside `utils.py`.

Must implement:

```python
summary()
list_items()
```

---

## Task 3.5 — Final Integration

Final imports:

```python
from assets.base import SafetyAsset
from assets.devices import FireExtinguisher, SmokeDetector, FireDoor
from building import Building
from technician import Technician
from exceptions import InspectionError
from utils import (
    print_asset_summary,
    run_all_inspections,
    print_report,
    InspectionLog,
)
```

Demo:

1. Create building
2. Validate serials
3. Add assets
4. Assign technician
5. Run inspections
6. Print `len(building)`
7. Print building
8. Call `print_report()`
9. Print workload

---

## Part 3 Checklist

* Magic methods implemented
* `technician.py` exists
* Duck typing works
* `main.py` imports cleanly
* System runs end-to-end

---

# Quick Reference

## Final File Structure

```text
safecheck/
├── assets/
│   ├── __init__.py
│   ├── base.py
│   └── devices.py
├── exceptions.py
├── building.py
├── technician.py
├── utils.py
└── main.py
```

---

## Import Hierarchy

1. `exceptions.py` imports nothing
2. `assets/base.py` imports from `abc` and exceptions
3. `assets/devices.py` imports from assets.base and exceptions
4. `building.py` imports from assets.base and exceptions
5. `technician.py` imports nothing
6. `utils.py` imports from assets.base, devices, exceptions
7. `main.py` imports everything

---

# OOP Cheat Sheet

| Pattern              | Reminder                      |
| -------------------- | ----------------------------- |
| `super().__init__()` | Extend parent setup           |
| `@abstractmethod`    | Forces implementation         |
| `@property`          | Controlled attribute access   |
| `@staticmethod`      | Utility function on class     |
| `@classmethod`       | Alternative constructor       |
| `isinstance()`       | Proper runtime type check     |
| `__str__`            | Human-readable                |
| `__repr__`           | Developer-readable            |
| `__eq__`             | Equality operator             |
| `__len__`            | Supports `len()`              |
| Composition          | Ownership relationship        |
| Aggregation          | Shared reference relationship |
| Duck Typing          | Method-based compatibility    |
| List Comprehension   | Pythonic filtering            |
| Module Structure     | One responsibility per file   |

---

# Interview Reminders

1. Explain your class structure before coding
2. Explain why you use `super().__init__()`
3. Explain why you prefer `isinstance()`
4. Explain abstract classes as contracts
5. Explain module separation by responsibility
6. Think out loud
7. Focus on understanding over syntax memorization

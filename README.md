# api-lab

# QuickPizza API Testing Lab

This repository contains an automated API test suite for the QuickPizza application, built using Python, `pytest`, and the `requests` library.

## Setup and Installation

**Prerequisites:** 
* Python 3.8+ installed on your system.
* Git installed.

**1. Clone the repository**
```bash
git clone <your-repository-url>
cd api-lab

# On Windows (PowerShell)
python -m venv venv
.\venv\Scripts\Activate.ps1

# On macOS and Linux (Bash)
python3 -m venv venv
source venv/bin/activate

pip install -r requirements.txt

#run the test
pytest -v

### Input Domain Model: POST /api/ratings
| Characteristic | Blocks | Values in the tests | Test Name Covering Block |
|---|---|---|---|
| **C1 Value of stars** | below 1 <br> 1 to 5 (base) <br> above 5 | 0 <br> 3 <br> 6 | `test_stars_out_of_range` <br> `test_base_choice_is_saved` <br> `test_stars_out_of_range` |
| **C2 Type of stars** | whole number (base) <br> decimal <br> text <br> missing | 3 <br> 3.5 <br> "3" <br> no field | `test_base_choice_is_saved` <br> `test_stars_decimal` <br> `test_stars_text` <br> `test_stars_missing` |
| **C3 Pizza** | exists (base) <br> does not exist | a new pizza <br> 999999999 | `test_base_choice_is_saved` <br> `test_pizza_does_not_exist` |
| **C4 Token** | the user's own (base) <br> none <br> wrong length | from auth <br> no header <br> token short | `test_base_choice_is_saved` <br> `test_token_missing` <br> `test_token_wrong_length` |
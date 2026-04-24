# 🔬 Four Probe Data Analyzer

## 📊 Description

This project is a scientific data analysis tool built using Python.
It processes experimental data from the Four Probe Method to calculate resistivity and energy band gap, and generates graphical visualization.

---

## 🚀 Features

* Reads input data from Excel file
* Calculates:

  * Temperature in Kelvin
  * Resistance
  * Resistivity
* Generates graph of log(resistivity) vs inverse temperature
* Computes slope using linear regression
* Calculates energy band gap
* Saves processed data and graph automatically

---

## 🛠️ Technologies Used

* Python
* pandas
* NumPy
* Matplotlib

---

## 📂 Input Data Format

The input file (`four_probe_data.xlsx` or `.csv`) must contain:

| Column Name | Description            |
| ----------- | ---------------------- |
| tempC       | Temperature in Celsius |
| vcool       | Cooling voltage        |
| vheat       | Heating voltage        |

---

## ▶️ How to Run

1. Install required libraries:

```
pip install pandas numpy matplotlib openpyxl
```

2. Run the program:

```
python main.py
```

3. Enter:

* File name 
* Current value
* Probe distance
* Error value

---

## 📊 Output

The program generates:

* 📄 `output.xlsx` → Processed data
* 📈 `graph.png` → Visualization of results
* 📉 Console output → Slope and energy band gap

---

## 📸 Sample Output Graph
<img width="1568" height="959" alt="Screenshot (25)" src="https://github.com/user-attachments/assets/eed97200-10c2-48ff-8fcb-dfef3f34f13f" />


## 📈 Formula Used

* Resistivity calculation based on four probe method
* Energy band gap:

Eg = 2.3026 × 0.02 × 8.6 × slope

---

## 💡 Applications

* Semiconductor analysis
* Material science experiments
* Physics lab data processing

---

## 📌 Future Improvements

* Add GUI using Streamlit
* Allow file upload via interface
* Improve visualization with multiple graphs

---

## 👨‍💻 Author

Uttam Singh
BTech CSE Student

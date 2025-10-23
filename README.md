### 🧠 Password Strength Visualizer

A simple **cybersecurity  tool** that analyzes password strength and visualizes it with a bar chart.
It estimates entropy, calculates brute-force resistance time, and hashes the password using SHA-256.


#### ⚙️ Features

* Calculates **entropy** (bits of security)
* Estimates **brute-force crack time**
* Displays **SHA-256 hash** for learning
* **Visual bar chart** comparing entropy and crack time (log-scaled)


#### 🚀 How to Run

```bash
# Clone the repository
git clone https://github.com/me/password_strength_visualizer.git
cd password_strength_visualizer

# Install dependencies
pip install -r requirements.txt

# Run the visualizer
python password_checker_visual.py
```


#### 📊 Example Output

```
Enter password to analyze: bhsfukeb

Entropy: 66.96 bits
Estimated brute-force time: 455.16 years → Moderate
SHA-256 Hash: e4b8da66a23f0b522bb10f8c946cf8a35a02efc2f3d42d4415bff52b0a02302a
```

Then, a chart will appear showing **entropy** vs **crack time**.


#### 🧩 Requirements

```
matplotlib
```


#### 💡 Educational Purpose

This tool is for **cybersecurity awareness and learning only**  to help you understand how password complexity affects security.

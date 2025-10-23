import re, math, hashlib
import matplotlib.pyplot as plt

def calculate_entropy(password):
    """Estimate entropy based on password composition."""
    charset = 0
    if re.search(r'[a-z]', password): charset += 26
    if re.search(r'[A-Z]', password): charset += 26
    if re.search(r'[0-9]', password): charset += 10
    if re.search(r'[^a-zA-Z0-9]', password): charset += 32

    if charset == 0:
        return 0
    entropy = math.log2(charset ** len(password))
    return entropy

def crack_time(entropy):
    """Estimate brute-force crack time assuming 10 billion guesses/sec."""
    guesses_per_second = 10_000_000_000
    seconds = 2 ** entropy / guesses_per_second
    years = seconds / (60 * 60 * 24 * 365)
    return years

def plot_results(entropy, years):
    """Visualize entropy and crack time."""
    plt.figure(figsize=(8, 4))
    plt.bar(['Entropy (bits)', 'Crack Time (years)'], [entropy, years if years < 1e6 else 1e6], color=['#007acc', '#ff9900'])
    plt.title("Password Strength Visualization")
    plt.ylabel("Value (log scale for time)")
    plt.yscale('log')
    plt.text(0, entropy/2, f"{entropy:.2f} bits", ha='center', color='white', weight='bold')
    plt.text(1, min(years, 1e6)/2, f"{years:.2f} years", ha='center', color='white', weight='bold')
    plt.tight_layout()
    plt.show()

def analyze_password(password):
    print(f"\nAnalyzing password: {password}")
    entropy = calculate_entropy(password)
    years = crack_time(entropy)
    hash_value = hashlib.sha256(password.encode()).hexdigest()
    verdict = (
        "Weak" if years < 1 else
        "Moderate" if years < 10_000 else
        "Strong"
    )

    print(f"Entropy: {entropy:.2f} bits")
    print(f"Estimated brute-force time: {years:.2f} years → {verdict}")
    print(f"SHA-256 Hash: {hash_value}")
    
    plot_results(entropy, years)

if __name__ == "__main__":
    password = input("Enter password to analyze: ")
    analyze_password(password)

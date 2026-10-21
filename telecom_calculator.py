# Basic Free Space Path Loss (FSPL) calculator script
# Useful for radio links in telecommunications.

import math

def calculate_fspl(frequency_mhz, distance_km):
    """
    Calculates Free Space Path Loss (FSPL) in dB.
    Formula: FSPL = 20 * log10(d) + 20 * log10(f) + 32.44
    """
    fspl = 20 * math.log10(distance_km) + 20 * math.log10(frequency_mhz) + 32.44
    return fspl

if __name__ == "__main__":
    print("--- Basic Telecommunications Calculator ---")
    
    # Example values (e.g., frequency in MHz and distance in km)
    freq = float(input("Enter frequency in MHz (e.g., 2400 for Wi-Fi): "))
    dist = float(input("Enter distance in km: "))
    
    result = calculate_fspl(freq, dist)
    print(f"\nResult: Free Space Path Loss is {result:.2f} dB.")
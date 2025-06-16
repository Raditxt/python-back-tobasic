import math
import numpy as np
import matplotlib.pyplot as plt

# ==============================
# 1. Modul Parabolc Motion Simulation
# ==============================
class ProjectileMotion:
    def __init__(self, velocity: float, angle: float, gravity: float = 9.81):
        self.velocity = velocity  # Initial speed (m/s)
        self.angle = math.radians(angle)  # Angle in radians
        self.gravity = gravity  # Gravitation (m/s²)
    
    def calculate_time_of_flight(self) -> float:
        return (2 * self.velocity * math.sin(self.angle)) / self.gravity
    
    def calculate_max_height(self) -> float:
        return (self.velocity**2 * (math.sin(self.angle)**2)) / (2 * self.gravity)
    
    def calculate_horizontal_range(self) -> float:
        return (self.velocity**2 * math.sin(2 * self.angle)) / self.gravity
    
    def generate_trajectory(self, points: int = 100):
        time_of_flight = self.calculate_time_of_flight()
        time_intervals = np.linspace(0, time_of_flight, points)
        
        x_positions = [self.velocity * math.cos(self.angle) * t for t in time_intervals]
        y_positions = [self.velocity * math.sin(self.angle) * t - 0.5 * self.gravity * t**2 for t in time_intervals]
        
        return x_positions, y_positions
    
    def visualize(self):
        x, y = self.generate_trajectory()
        plt.figure(figsize=(10, 5))
        plt.plot(x, y, label=f"v={self.velocity} m/s, θ={math.degrees(self.angle):.1f}°")
        plt.title("Trajectory of Projectile Motion")
        plt.xlabel("Horizontal Distance (m)")
        plt.ylabel("Vertical Height (m)")
        plt.grid(True)
        plt.legend()
        plt.show()

# ==============================
# 2. Modul ac circuit analysis
# ==============================
class ACAnalysis:
    def __init__(self, voltage: complex, impedance: complex):
        self.voltage = voltage  # Tegangan kompleks
        self.impedance = impedance  # Impedansi kompleks
    
    def calculate_current(self) -> complex:
        return self.voltage / self.impedance
    
    def calculate_power(self) -> complex:
        current = self.calculate_current()
        return self.voltage * current.conjugate()
    
    def get_power_factor(self) -> float:
        power = self.calculate_power()
        return power.real / abs(power)

# ==============================
# 3. Numeric Input Function
# ==============================
def get_numeric_input(prompt: str, data_type: type) -> any:
    while True:
        try:
            value = input(prompt)
            if data_type == complex:
                return complex(value.replace(' ', ''))
            return data_type(value)
        except ValueError:
            print(f"Input tidak valid. Masukkan nilai {data_type.__name__}.")

# ==============================
# 4. Main Function
# ==============================
def main():
    print("=== Advanced Physics & Math Simulator ===")
    print("1. Simulasi Gerak Parabola")
    print("2. Analisis Rangkaian AC dengan Bilangan Kompleks")
    
    choice = input("Pilih mode simulasi (1/2): ")
    
    if choice == "1":
        print("\n=== Simulasi Gerak Parabola ===")
        velocity = get_numeric_input("Masukkan kecepatan awal (m/s): ", float)
        angle = get_numeric_input("Masukkan sudut peluncuran (derajat): ", float)
        
        projectile = ProjectileMotion(velocity, angle)
        
        print(f"\nWaktu Penerbangan: {projectile.calculate_time_of_flight():.2f} s")
        print(f"Tinggi Maksimum: {projectile.calculate_max_height():.2f} m")
        print(f"Jarak Horizontal: {projectile.calculate_horizontal_range():.2f} m")
        
        plot_choice = input("Ingin menampilkan grafik trajektori? (y/n): ").lower()
        if plot_choice == 'y':
            projectile.visualize()
    
    elif choice == "2":
        print("\n=== Analisis Rangkaian AC ===")
        print("Masukkan tegangan dan impedansi dalam format kompleks (misal: 120+5j)")
        
        voltage = get_numeric_input("Tegangan (V): ", complex)
        impedance = get_numeric_input("Impedansi (Ω): ", complex)
        
        ac = ACAnalysis(voltage, impedance)
        current = ac.calculate_current()
        power = ac.calculate_power()
        
        print(f"\nArus: {current:.2f} A")
        print(f"Daya: {power:.2f} VA")
        print(f"Power Factor: {ac.get_power_factor():.2f}")
    
    else:
        print("Pilihan tidak valid!")

if __name__ == "__main__":
    main()
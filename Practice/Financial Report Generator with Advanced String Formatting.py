from datetime import datetime

# ==============================
# 1. Financial Data Class
# Handles data collection and validation
# ==============================
class FinancialData:
    def __init__(self):
        self.data = {
            "date": datetime.now().strftime("%Y-%m-%d %H:%M"),
            "revenue": 0.0,
            "expenses": 0.0,
            "tax_rate": 0.0,
            "currency": "USD"
        }

    def collect_input(self):
        print("=== Financial Report Generator ===")
        print("Masukkan data keuangan Anda (gunakan angka saja, tanpa simbol):")
        
        try:
            self.data["revenue"] = float(input("Total Pendapatan (Revenue): "))
            self.data["expenses"] = float(input("Total Pengeluaran (Expenses): "))
            self.data["tax_rate"] = float(input("Tarif Pajak (%): "))
            self.data["currency"] = input("Mata uang (misal: IDR, USD, EUR): ").upper()
        except ValueError:
            print("Input harus berupa angka!")
            self.collect_input()

    def calculate_metrics(self):
        """Hitung metrik keuangan"""
        self.data["gross_profit"] = self.data["revenue"] - self.data["expenses"]
        self.data["tax_amount"] = self.data["gross_profit"] * (self.data["tax_rate"] / 100)
        self.data["net_profit"] = self.data["gross_profit"] - self.data["tax_amount"]
        self.data["profit_margin"] = self.data["net_profit"] / self.data["revenue"] if self.data["revenue"] != 0 else 0

# ==============================
# 2. Report Formatter
# Handles advanced string formatting
# ==============================
class ReportFormatter:
    def __init__(self, data):
        self.data = data
        self.report_lines = []

    def format_currency(self, amount):
        """Format angka dengan ribuan pemisah"""
        return f"{amount:,.2f}"

    def format_percentage(self, value):
        """Format persentase dengan 1 desimal"""
        return f"{value:.1%}"

    def format_status(self):
        """Format status berdasarkan profit"""
        profit = self.data["net_profit"]
        if profit > 0:
            return "\033[92mProfit\033[0m"  # Hijau
        elif profit < 0:
            return "\033[91mLoss\033[0m"    # Merah
        else:
            return "\033[93mBreak-even\033[0m"  # Kuning

    def generate_report(self):
        """Buat laporan dengan berbagai format string"""
        currency = self.data["currency"]
        status = self.format_status()
        
        # Header laporan
        self.report_lines.append("=== LAPORAN KEUANGAN ===")
        self.report_lines.append(f"Dicetak pada: {self.data['date']}")
        self.report_lines.append("-" * 50)

        # Tabel data
        self.report_lines.append("|| {:^15} || {:>15} {} ||".format("Item", "Jumlah", " " * 5))
        self.report_lines.append("-" * 50)
        self.report_lines.append(f"|| {'Pendapatan':^15} || {self.format_currency(self.data['revenue']):>15} {currency} ||")
        self.report_lines.append(f"|| {'Pengeluaran':^15} || {self.format_currency(self.data['expenses']):>15} {currency} ||")
        self.report_lines.append(f"|| {'Profit Kotor':^15} || {self.format_currency(self.data['gross_profit']):>15} {currency} ||")
        self.report_lines.append(f"|| {'Pajak ({self.data["tax_rate"]}%)':^15} || {self.format_currency(self.data['tax_amount']):>15} {currency} ||")
        self.report_lines.append(f"|| {'Net Profit':^15} || {self.format_currency(self.data['net_profit']):>15} {currency} ||")
        self.report_lines.append("-" * 50)
        self.report_lines.append(f"|| {'Profit Margin':^15} || {self.format_percentage(self.data['profit_margin']):>15} ||")
        self.report_lines.append(f"|| {'Status':^15} || {status:>15} ||")
        self.report_lines.append("-" * 50)

        # Analisis cepat dengan ekspresi matematika
        self.report_lines.append("\n=== ANALISIS CEPAT ===")
        self.report_lines.append("-" * 50)
        self.report_lines.append(f"{'Profit > 1000':<20}: {'Ya' if self.data['net_profit'] > 1000 else 'Tidak'}")
        self.report_lines.append(f"{'Profit Margin > 10%':<20}: {'Ya' if self.data['profit_margin'] > 0.1 else 'Tidak'}")
        self.report_lines.append("-" * 50)

    def get_report(self):
        """Kembalikan laporan sebagai string"""
        return "\n".join(self.report_lines)

# ==============================
# 3. Report Saver
# Handles saving report to file
# ==============================
class ReportSaver:
    @staticmethod
    def save_to_file(report, filename="financial_report.txt"):
        with open(filename, "w") as f:
            f.write(report)
        print(f"\nLaporan tersimpan ke '{filename}'")

# ==============================
# 4. Main Program
# ==============================
def main():
    financial_data = FinancialData()
    financial_data.collect_input()
    financial_data.calculate_metrics()
    
    formatter = ReportFormatter(financial_data.data)
    formatter.generate_report()
    
    report = formatter.get_report()
    print(report)
    
    save_choice = input("\nSimpan laporan? (y/n): ").lower()
    if save_choice == "y":
        filename = input("Masukkan nama file: ")
        ReportSaver.save_to_file(report, filename)

# ==============================
# 5. Jalankan program
# ==============================
if __name__ == "__main__":
    main()
import os
from collections import Counter

# ==============================
# 1. Text Cleaning Module
# Handles text normalization and cleaning
# ==============================
class TextCleaner:
    def __init__(self, raw_text):
        self.raw = raw_text
        self.cleaned = self.raw

    def normalize_case(self, case="lower"):
        """Normalize text case to upper or lower"""
        if case == "lower":
            self.cleaned = self.cleaned.lower()
        elif case == "upper":
            self.cleaned = self.cleaned.upper()
        return self.cleaned

    def remove_whitespace(self):
        """Remove leading/trailing whitespace"""
        self.cleaned = self.cleaned.strip()
        return self.cleaned

    def replace_text(self, old, new):
        """Replace all occurrences of old substring with new"""
        self.cleaned = self.cleaned.replace(old, new)
        return self.cleaned

    def clean_all(self):
        """Apply all cleaning steps in sequence"""
        self.remove_whitespace()
        self.normalize_case("lower")
        self.cleaned = ' '.join(self.cleaned.split())  # Remove extra spaces
        return self.cleaned

# ==============================
# 2. Text Analysis Module
# Handles word frequency, sentence count, etc.
# ==============================
class TextAnalyzer:
    def __init__(self, text):
        self.text = text
        self.words = self.text.split()
        self.sentences = self.text.split('.') if '.' in self.text else [self.text]

    def word_count(self):
        """Return total word count"""
        return len(self.words)

    def sentence_count(self):
        """Return total sentence count"""
        return len(self.sentences)

    def most_common_words(self, n=5):
        """Return top n most common words"""
        return Counter(self.words).most_common(n)

    def character_count(self):
        """Return total number of characters"""
        return len(self.text)

# ==============================
# 3. Report Generator
# Formats and outputs analysis results
# ==============================
class ReportGenerator:
    @staticmethod
    def generate_summary(cleaned_text, analyzer):
        """Generate formatted analysis summary"""
        report = []
        report.append("=== TEXT ANALYSIS SUMMARY ===")
        report.append(f"Original Length: {len(cleaned_text)} characters")
        report.append(f"Cleaned Length: {analyzer.character_count()} characters")
        report.append(f"Word Count: {analyzer.word_count()}")
        report.append(f"Sentence Count: {analyzer.sentence_count()}")
        report.append(f"Top 5 Words: {analyzer.most_common_words(5)}")
        return "\n".join(report)

# ==============================
# 4. File Handler
# Load from/write to files
# ==============================
class FileHandler:
    @staticmethod
    def load_file(filepath):
        """Load text from file"""
        try:
            with open(filepath, 'r', encoding='utf-8') as f:
                return f.read()
        except FileNotFoundError:
            print(f"File not found: {filepath}")
            return ""

    @staticmethod
    def save_file(filepath, content):
        """Save processed text to file"""
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Output saved to {filepath}")

# ==============================
# 5. Main Program
# Interactive CLI interface
# ==============================
def main():
    print("=== Text Cleaner & Analyzer ===")
    
    # Input source selection
    print("\nInput Source:")
    print("1. Manual Input")
    print("2. Load from File")
    choice = input("Select input method (1/2): ")
    
    if choice == "1":
        print("\nEnter your text (press Enter twice to finish):")
        lines = []
        while True:
            line = input()
            if not line:
                break
            lines.append(line)
        raw_text = '\n'.join(lines)
    elif choice == "2":
        filename = input("Enter filename: ")
        raw_text = FileHandler.load_file(filename)
        if not raw_text:
            print("Using empty text.")
            raw_text = ""
    else:
        print("Invalid choice. Using empty text.")
        raw_text = ""

    # Initialize cleaner
    cleaner = TextCleaner(raw_text)
    print("\nCleaning Options:")
    print("1. Clean All (default)")
    print("2. Custom Cleaning")
    clean_choice = input("Select cleaning method (1/2): ")

    if clean_choice == "2":
        # Custom cleaning steps
        case_choice = input("Normalize case? (lower/upper/no): ").lower()
        if case_choice in ["lower", "upper"]:
            cleaner.normalize_case(case_choice)

        space_choice = input("Remove whitespace? (yes/no): ").lower()
        if space_choice == "yes":
            cleaner.remove_whitespace()

        replace_choice = input("Replace text? (yes/no): ").lower()
        if replace_choice == "yes":
            old = input("Text to replace: ")
            new = input("Replacement text: ")
            cleaner.replace_text(old, new)
    else:
        # Default full cleaning
        cleaner.clean_all()

    # Initialize analyzer
    analyzer = TextAnalyzer(cleaner.cleaned)

    # Show analysis
    print("\n=== CLEANED TEXT ===")
    print(cleaner.cleaned[:200] + ("..." if len(cleaner.cleaned) > 200 else ""))
    
    print("\n=== ANALYSIS RESULTS ===")
    report = ReportGenerator.generate_summary(cleaner.cleaned, analyzer)
    print(report)

    # Save option
    save_choice = input("\nSave output? (yes/no): ").lower()
    if save_choice == "yes":
        output_file = input("Enter output filename: ")
        FileHandler.save_file(output_file, report)

# ==============================
# 6. Run the Program
# ==============================
if __name__ == "__main__":
    main()
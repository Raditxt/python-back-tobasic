# ==============================
# 1. Game Core Module
# Handles game flow and string concatenation
# ==============================
class AdventureGame:
    def __init__(self):
        self.player = Player()
        self.story = Story()
        self.log = []

    def start(self):
        print(self.story.welcome_message())
        
        # Concatenate dynamic intro
        intro = "Selamat datang, " + self.player.name + "! Anda adalah seorang " + self.player.character_type + "."
        intro += "\nPetualangan Anda dimulai di kota kecil bernama " + self.story.town_name + "."
        intro += "\nTujuan Anda: " + self.story.quest + "."
        print("\n" + "-"*50 + "\n" + intro + "\n" + "-"*50 + "\n")

        # Game loop
        while self.player.health > 0 and not self.player.completed:
            self.show_options()
            choice = input("Apa yang ingin Anda lakukan? ").strip()
            
            if choice == "1":
                event = self.story.random_event()
                self.process_event(event)
            elif choice == "2":
                self.show_status()
            elif choice == "3":
                print("Permainan selesai. Terima kasih!")
                break
            else:
                print("Pilihan tidak valid!")

        self.end_game()

    def show_options(self):
        options = "\n=== Opsi ===\n"
        options += "1. Lanjutkan petualangan\n"
        options += "2. Lihat status\n"
        options += "3. Keluar\n"
        print(options)

    def process_event(self, event):
        # Concatenate event message
        message = "Kejadian: " + event['description'] + "\n"
        
        if event['type'] == 'positive':
            self.player.health += event['effect']
            message += "Anda mendapatkan " + str(event['effect']) + " poin kesehatan."
        elif event['type'] == 'negative':
            self.player.health -= event['effect']
            message += "Anda kehilangan " + str(event['effect']) + " poin kesehatan."
        elif event['type'] == 'quest':
            self.player.completed = True
            message += "Anda berhasil menyelesaikan misi! Petualangan selesai."
        
        self.log.append(message)
        print("\n" + message + "\n")

    def show_status(self):
        status = "=== Status Karakter ===\n"
        status += "Nama: " + self.player.name + "\n"
        status += "Jenis Karakter: " + self.player.character_type + "\n"
        status += "Kesehatan: " + str(self.player.health) + "\n"
        status += "Misi: " + ("Selesai" if self.player.completed else "Belum selesai")
        print("\n" + status + "\n")

    def end_game(self):
        result = "\n=== Permainan Selesai ===\n"
        result += "Log Permainan:\n"
        
        # Concatenate all log entries
        full_log = ""
        for entry in self.log:
            full_log += entry + "\n"
        
        result += full_log
        result += "-"*50 + "\n"
        result += "Terima kasih telah bermain!"
        
        print(result)
        
        # Save log to file
        with open("adventure_log.txt", "w") as f:
            f.write(result)
        print("Log tersimpan ke 'adventure_log.txt'")

# ==============================
# 2. Player Class
# Handles player data and status
# ==============================
class Player:
    def __init__(self):
        self.name = input("Masukkan nama karakter: ").strip()
        self.character_type = input("Jenis karakter (penjelajah, penyihir, dll.): ").strip()
        self.health = 100
        self.completed = False

# ==============================
# 3. Story Engine
# Generates dynamic narrative elements
# ==============================
class Story:
    def __init__(self):
        self.town_name = "Elmwood"
        self.quest = "menemukan harta karun legendaris"
        self.events = [
            {"description": "Anda menemukan ramuan penyembuh", "type": "positive", "effect": 20},
            {"description": "Anda terkena perangkap", "type": "negative", "effect": 15},
            {"description": "Anda menemukan peta harta karun", "type": "neutral", "effect": 0},
            {"description": "Anda berhasil mengalahkan monster", "type": "positive", "effect": 10},
            {"description": "Anda tersesat di hutan", "type": "negative", "effect": 25},
            {"description": "Anda menemukan harta karun!", "type": "quest", "effect": 0}
        ]

    def welcome_message(self):
        message = "Selamat datang di Dunia Fantasi!\n"
        message += "Di sini Anda akan menghadapi berbagai rintangan dan tantangan.\n"
        message += "Petualangan Anda akan berakhir ketika misi selesai atau kesehatan habis."
        return message

    def random_event(self):
        import random
        return random.choice(self.events)

# ==============================
# 4. Run the Game
# ==============================
if __name__ == "__main__":
    game = AdventureGame()
    game.start()
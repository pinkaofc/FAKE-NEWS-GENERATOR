import random

# Ridiculous category database
categories = {
    "bollywood": {
        "subjects": [
            "Shah Rukh Khan's pet hamster",
            "Deepika's secret clone",
            "Ranveer Singh's left shoe",
            "Alia Bhatt's imaginary friend",
            "Amitabh Bachchan's vintage fax machine",
            "Salman Khan's bicycle",
            "A rogue AI pretending to be Kareena Kapoor"
        ],
        "actions": [
            "elopes with",
            "declares itself supreme leader of",
            "gets arrested for secretly being",
            "wins Oscar for playing",
            "spontaneously combusts near",
            "launches OnlyFans account featuring",
            "adopts 50 copies of"
        ],
        "locations": [
            "inside SRK's mansion toilet",
            "at a secret Bollywood Illuminati meeting",
            "on the sets of 'Golmaal 27'",
            "during a dramatic rain song sequence",
            "while disguised as a coconut tree",
            "in the middle of a fake airport terminal"
        ]
    },
    "cricket": {
        "subjects": [
            "Virat Kohli's suspiciously shiny forehead",
            "Dhoni's secret army of clones",
            "Rohit Sharma's magic bat",
            "Bumrah's sentient yorker ball",
            "The ghost of Sachin Tendulkar",
            "The pitch that gained consciousness",
            "The stump mic that started gossiping"
        ],
        "actions": [
            "files police complaint against",
            "gets kidnapped by",
            "wins Nobel Prize for",
            "forms political party with",
            "starts viral dance challenge with",
            "gets turned into NFT by",
            "time travels to defeat"
        ],
        "locations": [
            "inside a giant vat of butter chicken",
            "at secret IPL match-fixing sauna",
            "during rain delay pillow fight",
            "on top of a moving stadium roof",
            "while umpire was napping",
            "in the middle of a Bollywood item number"
        ]
    },
    "politics": {
        "subjects": [
            "Modi's floating samosa",
            "Rahul Gandhi's mysterious WiFi network",
            "Kejriwal's talking muffler",
            "Amit Shah's pet election symbol",
            "The demonetized ghost of 500 rupee note",
            "EVMs that developed feelings",
            "Parliament's secret underground dance floor"
        ],
        "actions": [
            "organizes flash mob against",
            "gets possessed by spirit of",
            "launches TikTok channel exposing",
            "accidentally becomes president of",
            "gets stuck in escalator at",
            "starts cult worshiping",
            "gets reincarnated as"
        ],
        "locations": [
            "inside Sonia Gandhi's handbag",
            "at Area 51 (Indian edition)",
            "during yoga session on Mars",
            "in the middle of demonetization 2.0",
            "while disguised as chaiwala",
            "at secret Antilla after-party"
        ]
    },
    "wtf": {
        "subjects": [
            "A sentient vada pav",
            "Delhi's talking pollution",
            "Mumbai's self-aware pothole",
            "Bengaluru's rogue traffic signal",
            "The ghost of Rajinikanth's mustache",
            "A WhatsApp University professor",
            "PM's lost slipper"
        ],
        "actions": [
            "marries",
            "declares nuclear war on",
            "gets cancelled by Twitter for",
            "reveals shocking truth about",
            "becomes TikTok famous for",
            "takes over as CEO of",
            "gets abducted by aliens after criticizing"
        ],
        "locations": [
            "inside a Maggi noodle packet",
            "at Cow University convocation",
            "during Antilla's garage sale",
            " Mannat's rooftop during full moon",
            "while time traveling to 1947",
            "in parallel universe where Modi is a poet"
        ]
    }
}

def generate_headline(category):
    subject = random.choice(categories[category]["subjects"])
    action = random.choice(categories[category]["actions"])
    location = random.choice(categories[category]["locations"])
    emoji = random.choice(["🤯", "💥", "👑", "🦄", "🌶️", "🔥", "🎭"])
    return f"{emoji} BREAKING: {subject} {action} {location} {emoji}"

def main():
    print("\n" + "="*50)
    print("🤪 ULTIMATE FAKE NEWS GENERATOR 9000 🤪".center(50))
    print("="*50)
    
    print("\nSelect Absurd Category:")
    print("1. Bollywood Gone Wild 🤪")
    print("2. Cricket Conspiracies 🏏")
    print("3. Political Dramas 🎩")
    print("4. WTF India Edition 🤡")
    print("5. Random Chaos 🎲")
    
    while True:
        try:
            choice = input("\nYour choice (1-5, q to quit): ")
            
            if choice.lower() == 'q':
                print("\n" + "="*50)
                print("Thanks for the laughs! Go spread some chaos!".center(50))
                print("="*50 + "\n")
                break
            
            choice = int(choice)
            if choice == 1:
                cat = "bollywood"
            elif choice == 2:
                cat = "cricket"
            elif choice == 3:
                cat = "politics"
            elif choice == 4:
                cat = "wtf"
            elif choice == 5:
                cat = random.choice(list(categories.keys()))
            else:
                print("Enter valid option (1-5)!")
                continue
                
            print("\n" + "="*50)
            print(generate_headline(cat).center(50))
            print("="*50)
            
            save = input("\nSave this masterpiece? (y/n): ")
            if save.lower() == 'y':
                with open("fake_news.txt", "a") as f:
                    f.write(generate_headline(cat) + "\n")
                print("Saved to 'fake_news.txt'! 📁")
                
        except ValueError:
            print("Numbers only please! (1-5)")

if __name__ == "__main__":
    main()

import random

class VirtualPetGame:
    def __init__(self):
        self.animals = {
            "cat": "(=^‥^=)",
            "dog": "U・ᴥ・U",
            "bear": "ʕ·ᴥ·ʔ",
            "rabbit": "૮₍ ˶• ༝ •˶ ₎ა",
            "mouse": "<:3 )~",
            "pig": "( ´(00)ˋ )",
            "cow": "｡ﾟ(ﾟ´(00)`ﾟ)ﾟ｡",
            "horse": " (◕(‘人‘) ◕)",
            "sheep": " Ꮚ¯ꈊ¯Ꮚ",
            "monkey": " @(´･ｪ･`)@",
            "chicken": "( ˋ Θ ´ )",
            "duck": " ⊹⋛⋋(◐⊝◑)⋌⋚⊹",
            "frog": " Ꮚ[◐ o ◑ ]Ꮚ",
            "tiger": " ฅ^•ﻌ•^ฅ",
            "lion": " (,,^・⋏・^,,)",
            "elephant": " @ •́||•̀ @ ",
            "panda": " ʕ·͡ᴥ·ʔ ",
            "koala": " ʢٛ•ꇵٛ•ʡ ",
            "snake": " ～>`)～～～ ",
            "turtle": " ,=,e ",
            "fish": "><(((('>",
            "octopus": "~/\( •̀ ω •́ )/\~",
            "whale": " . ><(((.______.)",
            "bird": " ⊹⋛⋋( ՞ਊ ՞)⋌⋚⊹",
            "owl": " [ᓀ˵◇˵ᓂ] ",
            "penguin": " (•͈⌔•͈⑅) ",
            "bat": " /|\ ^._.^ /|\ ",
            "spider": "/╲/\╭[ ᴼᴼ ౪ ᴼᴼ]╮/\╱\ ",
            "butterfly": " ƸӜƷ ",
            "bee": "¸.·´¯`·¸¸. ི♥ྀ",
            "snail": " _@/ ",
            "ant": " ૂི•̮͡• ૂ ྀ ",
            "ladybug": " * ूི-̭͡- ૂ ྀ⁎ꂚᴉᴉᴉ ",
            "dragonfly": ">ï<",
            "caterpillar": "𓆙",
            "firefly": "✨ ᙙᙖ ",
            "unicorn": " (◕(‘人‘) ◕) ∋,｡･:*:･ﾟ’☆",
            "dragon": " ᏊˊꍓˋᏊ ",
            "phoenix": " 炎炎(o｀Θ´)o*:･ﾟ’☆ ",
            "fairy": " (⊃｡•́‿•̀｡)⊃━✿✿✿✿✿✿",
            "yeti": "༼☯﹏☯༽",
            "kraken": "ԅ( ˘ω˘ ԅ)",
            "ghost": "༼ つ ◕_◕ ༽つ",
            "alien": "(◣ _ ◢)",
            "angel": "ଘ(੭ˊᵕˋ)੭* ੈ✩‧₊˚ ",
            "zombies": "乁( x ω x乁)",
            "hare": "／(˃ᆺ˂)＼",
            "kitty": "ฅ(=^･ｪ･^=)ฅ",
        }

        self.super_rare_animals = {
            "phoenix": " 炎炎(o｀Θ´)o*:･ﾟ’☆ ",
            "fairy": " (⊃｡•́‿•̀｡)⊃━✿✿✿✿✿✿",
            "yeti": "༼☯﹏☯༽",
            "kraken": "ԅ( ˘ω˘ ԅ)",
            "ghost": "༼ つ ◕_◕ ༽つ",
            "alien": "(◣ _ ◢)",
            "angel": "ଘ(੭ˊᵕˋ)੭* ੈ✩‧₊˚ ",
            "zombies": "乁( x ω x乁)",
        }

        self.food = {
            "pineapple": " ミ(ZZZ) ",
            "cherries": " ๑/\๑ ",
            "carrot": "<===彡",
            "cake": " ┌iii┐ ",
            "corndog": " ―⊂ZZZ⊃",
            "barbecue": "―{}@{}@{}-",
        }

    def choose_pet(self):
        pets = random.sample(list(self.animals.keys()), 3)
        print("Welcome to the Virtual Pet Game!")
        print("Choose your pet:")
        for i, pet in enumerate(pets, 1):
            print(f"{i}. {pet.capitalize()}: {self.animals[pet]}")
        print("0. Roll again")
        choice = int(input("Enter your choice: "))
        if choice == 0:
            return self.choose_pet()
        elif choice in range(1, 4):
            chosen_pet = pets[choice - 1]
            confirm = input(f"This is your pet! Are you sure you want to choose {chosen_pet.capitalize()}? (yes/no): ").lower()
            if confirm == "yes":
                return chosen_pet
            else:
                return self.choose_pet()
        else:
            print("Invalid choice! Please select a valid option.")
            return self.choose_pet()

    def chat_with_pet(self, pet):
        responses = {
            "hello": "(=^･ω･^=) Hello!",
            "how are you": "(=^-ω-^=) I'm doing great!",
            "i'm fine": "(=^-ω-^=) That's wonderful!",
            "what's your favorite food": "(=^-ω-^=) I love all kinds of food!",
            "bye": "ﾉﾉbye~ Take care!",
        }

        while True:
            print("\nOptions:")
            print("1. Chat with your pet")
            print("2. Give a hug")
            print("3. Give a kiss")
            print("4. Sing for it")
            print("5. Feed it")
            print("6. Exit")
            user_input = input("Choose an option: ").lower()

            if user_input == "6" or user_input == "exit":
                print("Goodbye!")
                break
            elif user_input == "1" or user_input == "chat":
                chat_input = input("You: ").lower()
                if chat_input in responses:
                    print(f"Pet: {responses[chat_input]} {self.animals[pet]}")
                else:
                    print(f"Pet: {self.animals[pet]}")
            elif user_input == "2" or user_input == "hug":
                print(f"You gave your pet a hug! {self.animals[pet]} (⊃｡•́‿•̀｡)⊃")
            elif user_input == "3" or user_input == "kiss":
                print(f"You gave your pet a kiss! {self.animals[pet]} (づ￣ ³￣)づ")
            elif user_input == "4" or user_input == "sing":
                print(f"You sang for your pet! {self.animals[pet]} ♪♪♪ ヽ(ˇ∀ˇ )ゞ")
            elif user_input == "5" or user_input == "feed":
                print("Choose a food item to feed your pet:")
                for i, food_item in enumerate(self.food.keys(), 1):
                    print(f"{i}. {food_item.capitalize()}")
                food_choice = int(input("Enter your choice: "))
                if food_choice in range(1, len(self.food) + 1):
                    food_item = list(self.food.keys())[food_choice - 1]
                    print(f"You fed your pet {food_item.capitalize()}! {self.animals[pet]} {self.food[food_item]}")
                else:
                    print("Invalid choice! Please select a valid option.")
            else:
                print("Invalid input! Please choose a valid option.")

    def start(self):
        pet = self.choose_pet()
        if pet:
            print(f"You have chosen {pet.capitalize()} as your pet!")
            pet_name = input("Give your pet a name: ")
            print(f"You have named your pet '{pet_name}'!")
            self.chat_with_pet(pet)

game = VirtualPetGame()
game.start()

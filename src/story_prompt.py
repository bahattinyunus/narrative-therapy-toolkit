import json
import random
import os

def load_data():
    current_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(current_dir, 'prompts.json')
    with open(file_path, 'r', encoding='utf-8') as f:
        return json.load(f)

def generate_prompt():
    data = load_data()
    
    genre = random.choice(data['genres'])
    archetype = random.choice(data['archetypes'])
    conflict = random.choice(data['conflicts'])
    setting = random.choice(data['settings'])
    
    print("\n✨ --- HİKAYE FİKRİ JENERATÖRÜ --- ✨")
    print(f"📚 Tür:      {genre}")
    print(f"👤 Karakter: {archetype}")
    print(f"🌍 Mekan:    {setting}")
    print(f"🔥 Çatışma:  {conflict}")
    print("---------------------------------------")
    print("🚀 Şimdi yazmaya başla!\n")

if __name__ == "__main__":
    generate_prompt()

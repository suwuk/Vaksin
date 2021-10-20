from Friday import Friday

AI = "Babumu"
Tuan = "Diaz"
Friday().talk(f"Hallo {Tuan},i'm {AI} what can i do for you")
while True:
    Listen_to_me = Friday().take_command()
    print(Listen_to_me)
    if "hello" in Listen_to_me:
        print(f"Hello tot,What's up")
        Friday().talk(f"Hello tot,What's up")
    elif "how is the weather now" in Listen_to_me:
        print("Cerah banget kaya masa depan kamu")
        Friday().talk("Cerah banget kaya masa depan kamu")
    elif "any assignment" in Listen_to_me:
        print(f"No,You can have fun right now but you wont later")
        Friday().talk(f"No,You can have fun right now but you wont later")
    elif "really" in Listen_to_me:
        print("Bocah batu bat anjing")
        Friday().talk("get outta here now")
    elif "stop" in Listen_to_me:
        Friday().talk("Yes sir")
        break
    elif "no you don't" in Listen_to_me:
        print("yeah i do")
        Friday().talk("yeah i do")
    elif "no" in Listen_to_me:
        print("are you tryna make a fight with me?")
        Friday().talk("are you tryna make a fight with me?")
    else:
        print("Ngomong yang tegas asu")
        Friday().talk("Ngomong yang tegas asu")
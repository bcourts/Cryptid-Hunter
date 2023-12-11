"""
Program: Cryptid Hunter
Author: Brookes Courts
Last Date Modified: 11 December 2023
Cryptid Hunter is a text based Choose Your Own Adventure game that uses TKinter.
"""

from tkinter import *
from PIL import ImageTk, Image

def clear_screen():
    for widget in root.winfo_children():
        widget.destroy()

def select_mission():
    clear_screen()

    # Add a photo of Yukon Jack
    select_photo = ImageTk.PhotoImage(Image.open("Yukonjack2.png"))
    select_photo_label = Label(root, image=select_photo)
    select_photo_label.image = select_photo  # Keep a reference to avoid garbage collection
    select_photo_label.pack()

    # Display Mission Information
    mission_info_label = Label(root, text="Choose a Cryptid to Hunt:")
    mission_info_label.pack()

    chupacabra_button = Button(root, text="Chupacabra", command=lambda: start_mission("Chupacabra"))
    chupacabra_button.pack()

def start_mission(cryptid):
    clear_screen()

    # Display Mission Information
    mission_info_label = Label(root, text=f"Mission: {cryptid}")
    mission_info_label.pack()

    # Display Cryptid-specific information for Chupacabra
    if cryptid == "Chupacabra":
        mission_text = (
            "As Yukon Jack gears up for adventure, the Chupacabra mission beckons from the sun-scorched deserts of Mexico. "
            "The Chupacabra, a mythical creature, is said to be a blood-sucking entity known for preying on livestock, leaving a trail of mystery in its wake. "
            "In this arid landscape, Yukon Jack faces the harsh challenges of the desert, where temperatures soar, and water is a precious commodity. "
            "Legends speak of the Chupacabra's ability to vanish into the vastness of the desert, making it a formidable cryptid to track. "
            "Will Yukon Jack overcome the heat, find the elusive creature, and capture it on film, or will the desert hold secrets too perilous to uncover?"
        )
        mission_image_path = "Desert2.png"

    mission_info_text = Label(root, text=mission_text, wraplength=400)
    mission_info_text.pack()

    # Add a photo to the Mission Information section
    mission_photo = ImageTk.PhotoImage(Image.open(mission_image_path))
    mission_photo_label = Label(root, image=mission_photo)
    mission_photo_label.image = mission_photo
    mission_photo_label.pack()

    start_adventure_button = Button(root, text="Start Adventure", command=start_adventure)
    start_adventure_button.pack()

def start_adventure():
    clear_screen()

    # Adventure logic goes here
    adventure_label = Label(
        root,
        text=("Amid the scorching desert, Yukon Jack finds himself at a crossroads, a pivotal moment in his Chupacabra mission. "
              "The trail forks, and the shimmering heat distorts the horizon. Sweat beads on Yukon Jack's forehead as he contemplates his next move.\n"
              "Left Path: Yukon Jack decides to take the left path, guided by intuition or perhaps a gut feeling. The landscape unfolds with sandy dunes "
              "and rocky formations. As he ventures deeper, the heat becomes more intense, and mirages dance on the horizon. The left path appears to lead "
              "towards a vast open space where the Chupacabra might find refuge.\n"
              "Right Path: Opting for the right path, Yukon Jack heads into a more rugged terrain with sparse vegetation. The air carries a distinct "
              "stillness, and the silence is broken only by the occasional howl of the wind. The right path appears to wind its way through a series of rocky "
              "outcrops and shaded areas. Yukon Jack wonders if this route might lead to a prime Chupacabra hunting ground."),
        wraplength=800
    )
    adventure_label.pack()

    left_path_button = Button(root, text="Left Path", command=left_path_result)
    left_path_button.pack()

    right_path_button = Button(root, text="Right Path", command=right_path_result)
    right_path_button.pack()

def left_path_result():
    clear_screen()

    # Display result of choosing the left path
    left_result_label = Label(
        root,
        text=("The relentless desert sun beats down on Yukon Jack as he attempts to navigate the unforgiving terrain. "
              "Despite his best efforts, the heat takes a toll on his body, and dehydration sets in. Disoriented and weakened, "
              "Jack's mind begins to play tricks on him. Mirage-like images dance on the horizon, and the scorching heat distorts his perception of reality."),
        wraplength=800
    )
    left_result_label.pack()

    # Display the Dead.png image
    dead_image = ImageTk.PhotoImage(Image.open("Dead.png"))
    dead_label = Label(root, image=dead_image)
    dead_label.image = dead_image  # Keep a reference to avoid garbage collection
    dead_label.pack()

def right_path_result():
    clear_screen()

    # Display result of choosing the right path
    right_result_label = Label(
        root,
        text=("The right path guides Yukon Jack through rocky outcrops, and he discovers a hidden water source where the Chupacabra frequently visits. "
              "Will this position provide him with the opportunity to observe and capture the creature on film?"),
        wraplength=800
    )
    right_result_label.pack()

    # Add buttons for the next choices
    explore_cave_button = Button(root, text="Explore the Cave", command=explore_cave_result)
    explore_cave_button.pack()

    continue_ridge_button = Button(root, text="Continue Along the Ridge", command=continue_ridge_result)
    continue_ridge_button.pack()

def explore_cave_result():
    clear_screen()

    # Display result of choosing to explore the cave
    explore_cave_label = Label(
        root,
        text=("As Yukon Jack delves deeper into the cave, the oppressive darkness seems to close in around him. "
              "Unbeknownst to him, the cave harbors not only the chilling secrets of the Chupacabra but also a den of mysterious desert-dwelling creatures. "
              "The air becomes thick with an eerie tension as he disturbs the creatures from their shadowy corners.\n"
              "In the suffocating blackness, the creatures emerge with unsettling whispers and frenzied movements. Jack, unprepared and vulnerable, "
              "finds himself ensnared in a chaotic encounter with these unknown assailants. Their features remain shrouded in darkness, adding to the uncertainty "
              "and fear that permeates the cavern.\n"
              "Struggling against the unseen attackers, Jack's attempts to defend himself prove futile. In the tumultuous turmoil, any hope of photographing "
              "the elusive Chupacabra slips away like a fleeting mirage. The cave, initially a refuge for the cryptid's secrets, transforms into a nightmarish trap. "
              "The creatures' haunting calls reverberate through the cavern as Yukon Jack succumbs to the darkness, his chance at documenting the Chupacabra's existence vanquished in a sinister encounter."),
        wraplength=800
    )
    explore_cave_label.pack()

    # Display the Dead.png image
    dead_image = ImageTk.PhotoImage(Image.open("Dead.png"))
    dead_label = Label(root, image=dead_image)
    dead_label.image = dead_image  # Keep a reference to avoid garbage collection
    dead_label.pack()

def continue_ridge_result():
    clear_screen()

    # Display result of choosing to continue along the ridge
    continue_ridge_label = Label(
        root,
        text=("Success: Yukon Jack's decision to remain on the ridge proves fortuitous. "
              "From this elevated position, he spots the Chupacabra gracefully moving through the desert landscape below. "
              "The clear line of sight allows him to capture stunning photographs, showcasing the creature's beauty and elusiveness. "
              "If only the Chupacabra appeared!"),
        wraplength=800
    )
    continue_ridge_label.pack()

    # Add buttons for the next choices
    telephoto_lens_button = Button(root, text="Use a Telephoto Lens", command=telephoto_lens_result)
    telephoto_lens_button.pack()

    approach_stealthily_button = Button(root, text="Approach Stealthily", command=approach_stealthily_result)
    approach_stealthily_button.pack()

def telephoto_lens_result():
    clear_screen()

    # Display result of choosing to use a telephoto lens
    telephoto_lens_label = Label(
        root,
        text=("Yukon Jack's decision to use the telephoto lens proves effective. "
              "The Chupacabra remains undisturbed as he captures stunning, detailed photographs from a safe distance. "
              "This method not only ensures a successful encounter but also provides a valuable addition to Yukon Jack's Cryptid Hunter portfolio."),
        wraplength=800
    )
    telephoto_lens_label.pack()

    # Display the Chupacabra2.png image
    chupacabra2_image = ImageTk.PhotoImage(Image.open("Chupacabra2.png"))
    chupacabra2_label = Label(root, image=chupacabra2_image)
    chupacabra2_label.image = chupacabra2_image  # Keep a reference to avoid garbage collection
    chupacabra2_label.pack()

    # Display success message
    success_label = Label(root, text="You photographed the Chupacabra!")
    success_label.pack()

def approach_stealthily_result():
    clear_screen()

    # Display result of choosing to approach stealthily
    stealth_result_label = Label(
        root,
        text=("The desolate desert landscape becomes an unforgiving theater for Yukon Jack's attempt at stealth. "
              "Every step, every breath is met with an oppressive silence, broken only by the rhythmic beating of his heart. "
              "However, the harsh reality of the desert proves treacherous for the unwary.\n"
              "A sudden noise or Jack's inadvertent misstep echoes through the arid expanse, not only startling the elusive Chupacabra but also drawing the attention of a more ominous presence lurking in the shadows. "
              "From the sun-scorched depths of the desert emerges a territorial predator, a creature more dangerous and formidable than Jack could have anticipated.\n"
              "The air becomes charged with an instinctual fear as the territorial predator stalks towards the commotion. "
              "Jack, now caught between the Chupacabra and this newfound threat, faces an uncertain fate in the merciless desert. "
              "The missed opportunity to document the cryptid serves as a harsh reminder, not only of the risks inherent in the pursuit of cryptids but also of the malevolent forces that dwell in the unforgiving wilderness. "
              "Survival itself hangs in the balance, with the desolation of the desert concealing threats that go beyond the scope of Jack's cryptid hunt."),
        wraplength=800
    )
    stealth_result_label.pack()

    # Display the Dead.png image
    dead_image = ImageTk.PhotoImage(Image.open("Dead.png"))
    dead_label = Label(root, image=dead_image)
    dead_label.image = dead_image  # Keep a reference to avoid garbage collection
    dead_label.pack()

# GUI setup
root = Tk()
root.title("Cryptid Hunter")

my_image = ImageTk.PhotoImage(Image.open("Start.png"))
image_label = Label(image=my_image)
image_label.pack()

start_button = Button(root, text="Click here to start your adventure!", command=select_mission)
start_button.pack()

root.mainloop()

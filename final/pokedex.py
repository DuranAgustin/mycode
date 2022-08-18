#!/usr/bin/env python3
"""Module is used for img handling and tkinter is used to create a gui"""
import urllib.request
from io import BytesIO
from tkinter import END, RIGHT, Button, Entry, Label, Text, Tk

import requests
from PIL import Image, ImageTk


def main():
    """ Creating a pokedex using the PokiAPI,
    able to search any pokemon with either a name or a number!"""
    display = Tk()
    # title and dimensions capped at 800x800 so relx/y doesn't move.
    display.title("PokeDex")
    display.geometry("800x800")
    display.maxsize(800, 800)
    display.minsize(800, 800)
    # Pokedex background
    url = "https://cdn.domestika.org/content-items/002/087/036/Captura_de_pantalla_2016-09-21_a_las_19.30.10-original.png"
    with urllib.request.urlopen(url) as url_inf:
        raw_data = url_inf.read()
    b_img = Image.open(BytesIO(raw_data))
    images = ImageTk.PhotoImage(b_img)
    bg_img = Label(image=images)
    bg_img.place(x=0, y=0, relwidth=1, relheight=1)
    bg_img.lower()

    # lower needed to stop entry and button from disappearing..
    # box to display output
    pokemon_attr = Text()
    pokemon_attr.place(relx=0.338, rely=0.542, height=190, width=314)

    # entry/input box
    inputbox = Entry(display)
    inputbox.place(relx=0.462, rely=0.801)

    def api_call():
        # deletes the entire Text box
        pokemon_attr.delete('1.0', END)
        name = inputbox.get()
        # we are going to try
        if isinstance(name, str):
            name = name.lower()
        try:

            name_img = requests.get(
                "https://pokeapi.co/api/v2/pokemon/" + name).json()
            #pokemon_name = name_img['name']
            #pokemon_id = str(name_img['id'])
            #pokemon_img = name_img["sprites"]["front_default"]

            with urllib.request.urlopen(name_img["sprites"]["front_default"]) as url_inf:
                raw_data = url_inf.read()
            img = Image.open(BytesIO(raw_data))
            images = ImageTk.PhotoImage(img)
            poke_img = Label(pokemon_attr)

            poke_img.pack(side=RIGHT)
            # poke_img.config(image=images)
            poke_img.image = images
            pokemon_attr.image_create('1.0', image=images)

            pokemon_attr.insert('3.0', "\n\nPokemon name: " + name_img['name'])
            pokemon_attr.insert(
                '5.0', "\nPokedex Numeber: " + str(name_img['id']))
        except Exception:
            pokemon_attr.insert(
                '1.0', "Check spelling or number.\n404 Pokemon Not found")

        # print(name_img["sprites"]["other"]["official-artwork"]['front_default'])
        evo_des = requests.get(
            "https://pokeapi.co/api/v2/pokemon-species/" + name).json()
        # print(evo_des)
        #evo_des = evo_des.json()
        try:
            #evolution = evo_des["evolves_from_species"]["name"]
            pokemon_attr.insert('7.0', "\nEvolution: " +
                                evo_des["evolves_from_species"]["name"])
        except Exception:
            pokemon_attr.insert('7.0', "\nEvolution: None")

        try:
            alpha = 'abcdefghijklmnopqrstuvwxyz'
            context = evo_des["flavor_text_entries"][0]["flavor_text"]
            if context in alpha:
                pokemon_attr.insert('9.0', "\n\nBIO:" + context)
            else:
                #context = evo_des["flavor_text_entries"][1]["flavor_text"]
                pokemon_attr.insert(
                    '9.0', "\n\nBIO:" + evo_des["flavor_text_entries"][1]["flavor_text"])
        except Exception:
            pokemon_attr.insert('9.0', "\n\nunregisted bio")

    # button to call functions.
    Button(display, text="Search",
           command=api_call).place(relx=0.40, rely=0.8)
    display.mainloop()


if __name__ == "__main__":
    main()


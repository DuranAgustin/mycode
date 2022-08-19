#!/usr/bin/env python3
"""Agustin Duran (NiceWork) | Python3
The objective of this project is to create a Python application that may be executed
from the command line and performs some kind of service using the skills you have learned thus far.
I Created a Pokedex using the PokeAPI if input a number or name it should return the pokemon.
"""
import urllib.request
from io import BytesIO
from tkinter import END, RIGHT, Button, Entry, Label, Text, Tk

import requests
from PIL import Image, ImageTk


def main():
    """ Main is called using if name main"""
    display = Tk()
    # title and dimensions capped at 800x800 so relx/y doesn't move.
    display.title("PokeDex")
    display.geometry("800x800")
    # Pokedex background
    url = "https://cdn.domestika.org/content-items/002/087/036/Captura_de_pantalla_2016-09-21_a_las_19.30.10-original.png"
    with urllib.request.urlopen(url) as url_inf:
        raw_data = url_inf.read()
    b_img = Image.open(BytesIO(raw_data))
    images = ImageTk.PhotoImage(b_img)
    bg_img = Label(image=images)
    bg_img.place(x=0, y=0, relwidth=1, relheight=1)
    # lower needed to stop entry and button from disappearing..
    bg_img.lower()

    # box to display output
    pokemon_attr = Text()
    pokemon_attr.place(relx=0.338, rely=0.542, height=190, width=314)

    # entry/input box
    inputbox = Entry(display)
    inputbox.place(relx=0.462, rely=0.801)

    def api_call():
        # deletes the entire Text box content
        pokemon_attr.delete('1.0', END)
        name = inputbox.get()
        # we are going to try to make it case insensitive
        if isinstance(name, str):
            name = name.lower()
        # it trys the api if it comes back with a response.
        try:
            # takes in the request, opens the url where the png is then
            # takes it in as bytes(BIKES) then we get an image.
            name_img = requests.get(
                "https://pokeapi.co/api/v2/pokemon/" + name).json()
            with urllib.request.urlopen(name_img["sprites"]["front_default"]) as url_inf:
                raw_data = url_inf.read()
            img = Image.open(BytesIO(raw_data))
            images = ImageTk.PhotoImage(img)
            poke_img = Label(pokemon_attr)
            poke_img.pack(side=RIGHT)
            poke_img.image = images
            # creates the image and id then adds it to the text box
            pokemon_attr.image_create('1.0', image=images)
            pokemon_attr.insert('3.0', "\n\nPokemon name: " + name_img['name'])
            pokemon_attr.insert(
                '5.0', "\nPokedex Numeber: " + str(name_img['id']))
        # if there isn't a pokemon at that name or number then it spits this out.
        except ValueError:
            pokemon_attr.insert(
                '1.0', "404 Pokemon Not found.\nCheck spelling or number.")

        # trys to get the evolution line if there is none(type).
        try:
            evo_des = requests.get(
                "https://pokeapi.co/api/v2/pokemon-species/" + name).json()
            pokemon_attr.insert('7.0', "\nEvolution: " +
                                evo_des["evolves_from_species"]["name"])
        # Using TypeError instead of Value because it is String not a NoneType.
        except TypeError:
            pokemon_attr.insert('7.0', "\nEvolution: None")

        # trys and see if it has a bio.
        try:
            # if the bio isn't in english it goes to the very next one which is in english.
            alpha = 'abcdefghijklmnopqrstuvwxyz'
            context = evo_des["flavor_text_entries"][0]["flavor_text"]
            if context in alpha:
                pokemon_attr.insert('9.0', "\n\nBIO:" +
                                    context.decode('uft-8'))
            else:
                pokemon_attr.insert(
                    '9.0', "\n\nBIO:" + evo_des["flavor_text_entries"][1]["flavor_text"])
        except ValueError:
            pokemon_attr.insert('9.0', "\n\nunregisted bio")

    # button to call functions.
    Button(display, text="Search",
           command=api_call).place(relx=0.40, rely=0.8)
    display.mainloop()


if __name__ == "__main__":
    main()


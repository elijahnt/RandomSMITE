import random
import sys
dir(random)
from random import randint
from tkinter import *



def God():
    options = ["Start","start","Physical","physical","Magical","magical","p"]
    choice = ""
    while choice not in options:
        print('''Welcome to the SMITE Random God and Build Generator v1 by elijahn't
Type Start if you are ready to begin with a Random God and Random Build, or type
Physical or Magical if you would like, well, Physical or Magical.''')
        choice = str(input(">>>"))
    if choice == options[0]:
        randomgod = randint(1,2)
        if randomgod == 1:
            print("Randomizing.. hold on to your memes")
            print("You got a Physical God!")
            physical()
        if randomgod == 2:
            print("Randomizing.. hold on to your memes")
            print("You got a Magical God!")
            magical()
    if choice == options[1]:
        randomgod = randint(1,2)
        if randomgod == 1:
            print("You got a Physical God!")
            physical()
        if randomgod == 2:
            print("You got a Magical God!")
            magical()
    if choice == options[2]:
        print("You have chosen a Physical God!")
        physical()
    if choice == options[3]:
        print("You have chosen a Physical God!")
        physical()
    if choice == options[6]:
        print("You have chosen a Physical God!")
        physical()
    if choice == options[4]:
        print("You have chosen a Magical God!")
        magical()
    if choice == options[5]:
        print("You have chosen a Magical God!")
        magical()
            
def physical():
    god = randint(1,51)
    if god == 1:
        print("You got Achilles")
    if god == 2:
        print("You got Ah Muzen Cab")
    if god == 3:
        print("You got Amaterasu")
    if god == 4:
        print("You got Anhur")
    if god == 5:
        print("You got Apollo")
    if god == 6:
        print("You got Arachne")
    if god == 7:
        print("You got Artemis")
    if god == 8:
        print("You got Awilix")
    if god == 9:
        print("You got Bakasura")
    if god == 10:
        print("You got Bastet")
    if god == 11:
        print("You got Bellona")
    if god == 12:
        print("You got Camazotz")
    if god == 13:
        print("You got Cernunnos")
    if god == 14:
        print("You got Chaac")
    if god == 15:
        print("You got Chernobog")
    if god == 16:
        print("You got Chiron")
    if god == 17:
        print("You got Cu Chulainn")
    if god == 18:
        print("You got Cupid")
    if god == 19:
        print("You got Da Ji")
    if god == 20:
        print("You got Erlang Shen")
    if god == 21:
        print("You got Fenrir")
    if god == 22:
        print("You got Guan Yu")
    if god == 23:
        print("You got Hachiman")
    if god == 24:
        print("You got Hercules")
    if god == 25:
        print("You got Hou Yi")
    if god == 26:
        print("You got Hun Batz")
    if god == 27:
        print("You got Izanami")
    if god == 28:
        print("You got Jing Wei")
    if god == 29:
        print("You got Kali")
    if god == 30:
        print("You got Loki")
    if god == 31:
        print("You got Medusa")
    if god == 32:
        print("You got Mercury")
    if god == 33:
        print("You got Ne Zha")
    if god == 34:
        print("You got Neith")
    if god == 35:
        print("You got Nemesis")
    if god == 36:
        print("You got Nike")
    if god == 37:
        print("You got Odin")
    if god == 38:
        print("You got Osiris")
    if god == 39:
        print("You got Rama")
    if god == 40:
        print("You got Ratatoskr")
    if god == 41:
        print("You got Ravana")
    if god == 42:
        print("You got Serqet")
    if god == 43:
        print("You got Skadi")
    if god == 44:
        print("You got Sun Wukong")
    if god == 45:
        print("You got Susano")
    if god == 46:
        print("You got Thanatos")
    if god == 47:
        print("You got Thor")
    if god == 48:
        print("You got Tyr")
    if god == 49:
        print("You got Ullr")
    if god == 50:
        print("You got Vamana")
    if god == 51:
        print("You got Xbalanque")
    lst_samples = range(0,58)
    ran_sample = random.sample(lst_samples,5)
    print("~//~" '\n')
    def boots():
        if god == 40:
            print("Acron of Yggdrasil")
        if god != 40:
            boots = randint(1,4)
            if boots == 1:
                print("Warrior Tabi")
            if boots == 2:
                print("Ninja Tabi")
            if boots == 3:
                print("Reinforced Greaves")
            if boots == 4:
                print("Talaria Boots")
    boots()
    def Build():
        if ran_sample[0] == 1:
            print("Sovereignty")
        if ran_sample[0] == 2:
            print("Mystical Mail")
        if ran_sample[0] == 3:
            print("Midgardian Mail")
        if ran_sample[0] == 4:
            print("Emperor's Armor")
        if ran_sample[0] == 5:
            print("The Executioner")
        if ran_sample[0] == 6:
            print("Qin's Sais")
        if ran_sample[0] == 7:
            print("Titan's Bane")
        if ran_sample[0] == 8:
            print("Brawler's Beat Stick")
        if ran_sample[0] == 9:
            print("Jotunn's Wrath")
        if ran_sample[0] == 10:
            print("The Crusher")
        if ran_sample[0] == 11:
            print("Transendence")
        if ran_sample[0] == 12:
            print("Hydra's Lament")
        if ran_sample[0] == 13:
            print("Deathbringer")
        if ran_sample[0] == 14:
            print("Rage")
        if ran_sample[0] == 15:
            print("Malice")
        if ran_sample[0] == 16:
            print("Soul Eater")
        if ran_sample[0] == 17:
            print("Devourer's Gauntlet")
        if ran_sample[0] == 18:
            print("Bloodforge")
        if ran_sample[0] == 19:
            print("Witchblade")
        if ran_sample[0] == 20:
            print("Winged Blade")
        if ran_sample[0] == 21:
            print("Relic Dagger")
        if ran_sample[0] == 22:
            print("Toxic Blade")
        if ran_sample[0] == 23:
            print("Frostbound Hammer")
        if ran_sample[0] == 24:
            print("Runeforged Hammer")
        if ran_sample[0] == 25:
            print("Blackthorn Hammer")
        if ran_sample[0] == 26:
            print("Shifter's Shield")
        if ran_sample[0] == 27:
            print("Void Shield")
        if ran_sample[0] == 28:
            print("Hide of the Nemean Lion")
        if ran_sample[0] == 29:
            print("Brestplate of Valor")
        if ran_sample[0] == 30:
            print("Spectral Armor")
        if ran_sample[0] == 31:
            print("Magi's Cloak")
        if ran_sample[0] == 32:
            print("Hide of the Urchin")
        if ran_sample[0] == 33:
            print("Spirit Robe")
        if ran_sample[0] == 34:
            print("Mantle of Discord")
        if ran_sample[0] == 35:
            print("Bulwark of Hope")
        if ran_sample[0] == 36:
            print("Pestilence")
        if ran_sample[0] == 37:
            print("Heartward Amulet")
        if ran_sample[0] == 38:
            print("Talisman of Energy")
        if ran_sample[0] == 39:
            print("Runic Shield")
        if ran_sample[0] == 40:
            print("Ancile")
        if ran_sample[0] == 41:
            print("Odysseus' Bow")
        if ran_sample[0] == 42:
            print("Stone of Gaia")
        if ran_sample[0] == 43:
            print("Shield of Regrowth")
        if ran_sample[0] == 44:
            print("Mail of Renewal")
        if ran_sample[0] == 45:
            print("Gauntlet of Thebes")
        if ran_sample[0] == 46:
            print("Wind Demon")
        if ran_sample[0] == 47:
            print("Poisoned Star")
        if ran_sample[0] == 48:
            print("Stone Cutting Sword")
        if ran_sample[0] == 49:
            print("Masamune")
        if ran_sample[0] == 50:
            print("Heartseeker")
        if ran_sample[0] == 51:
            print("Hastened Katana")
        if ran_sample[0] == 52:
            print("Genji's Guard")
        if ran_sample[0] == 53:
            print("Oni Hunter's Garb")
        if ran_sample[0] == 54:
            print("Shogun's Kusari")
        if ran_sample[0] == 55:
            print("Atlanta's Bow")
        if ran_sample[0] == 56:
            print("Asi")
        if ran_sample[0] == 57:
            print("Silverbranch Bow")
        if ran_sample[0] == 57:
            print("Ichaival")
        if ran_sample[0] == 58:
            print("Gladiator's Shield")
        if ran_sample[1] == 1:
            print("Sovereignty")
        if ran_sample[1] == 2:
            print("Mystical Mail")
        if ran_sample[1] == 3:
            print("Midgardian Mail")
        if ran_sample[1] == 4:
            print("Emperor's Armor")
        if ran_sample[1] == 5:
            print("The Executioner")
        if ran_sample[1] == 6:
            print("Qin's Sais")
        if ran_sample[1] == 7:
            print("Titan's Bane")
        if ran_sample[1] == 8:
            print("Brawler's Beat Stick")
        if ran_sample[1] == 9:
            print("Jotunn's Wrath")
        if ran_sample[1] == 10:
            print("The Crusher")
        if ran_sample[1] == 11:
            print("Transendence")
        if ran_sample[1] == 12:
            print("Hydra's Lament")
        if ran_sample[1] == 13:
            print("Deathbringer")
        if ran_sample[1] == 14:
            print("Rage")
        if ran_sample[1] == 15:
            print("Malice")
        if ran_sample[1] == 16:
            print("Soul Eater")
        if ran_sample[1] == 17:
            print("Devourer's Gauntlet")
        if ran_sample[1] == 18:
            print("Bloodforge")
        if ran_sample[1] == 19:
            print("Witchblade")
        if ran_sample[1] == 20:
            print("Winged Blade")
        if ran_sample[1] == 21:
            print("Relic Dagger")
        if ran_sample[1] == 22:
            print("Toxic Blade")
        if ran_sample[1] == 23:
            print("Frostbound Hammer")
        if ran_sample[1] == 24:
            print("Runeforged Hammer")
        if ran_sample[1] == 25:
            print("Blackthorn Hammer")
        if ran_sample[1] == 26:
            print("Shifter's Shield")
        if ran_sample[1] == 27:
            print("Void Shield")
        if ran_sample[1] == 28:
            print("Hide of the Nemean Lion")
        if ran_sample[1] == 29:
            print("Brestplate of Valor")
        if ran_sample[1] == 30:
            print("Spectral Armor")
        if ran_sample[1] == 31:
            print("Magi's Cloak")
        if ran_sample[1] == 32:
            print("Hide of the Urchin")
        if ran_sample[1] == 33:
            print("Spirit Robe")
        if ran_sample[1] == 34:
            print("Mantle of Discord")
        if ran_sample[1] == 35:
            print("Bulwark of Hope")
        if ran_sample[1] == 36:
            print("Pestilence")
        if ran_sample[1] == 37:
            print("Heartward Amulet")
        if ran_sample[1] == 38:
            print("Talisman of Energy")
        if ran_sample[1] == 39:
            print("Runic Shield")
        if ran_sample[1] == 40:
            print("Ancile")
        if ran_sample[1] == 41:
            print("Odysseus' Bow")
        if ran_sample[1] == 42:
            print("Stone of Gaia")
        if ran_sample[1] == 43:
            print("Shield of Regrowth")
        if ran_sample[1] == 44:
            print("Mail of Renewal")
        if ran_sample[1] == 45:
            print("Gauntlet of Thebes")
        if ran_sample[1] == 46:
            print("Wind Demon")
        if ran_sample[1] == 47:
            print("Poisoned Star")
        if ran_sample[1] == 48:
            print("Stone Cutting Sword")
        if ran_sample[1] == 49:
            print("Masamune")
        if ran_sample[1] == 50:
            print("Heartseeker")
        if ran_sample[1] == 51:
            print("Hastened Katana")
        if ran_sample[1] == 52:
            print("Genji's Guard")
        if ran_sample[1] == 53:
            print("Oni Hunter's Garb")
        if ran_sample[1] == 54:
            print("Shogun's Kusari")
        if ran_sample[1] == 55:
            print("Atlanta's Bow")
        if ran_sample[1] == 56:
            print("Asi")
        if ran_sample[1] == 57:
            print("Silverbranch Bow")
        if ran_sample[1] == 57:
            print("Ichaival")
        if ran_sample[1] == 58:
            print("Gladiator's Shield")
        if ran_sample[2] == 1:
            print("Sovereignty")
        if ran_sample[2] == 2:
            print("Mystical Mail")
        if ran_sample[2] == 3:
            print("Midgardian Mail")
        if ran_sample[2] == 4:
            print("Emperor's Armor")
        if ran_sample[2] == 5:
            print("The Executioner")
        if ran_sample[2] == 6:
            print("Qin's Sais")
        if ran_sample[2] == 7:
            print("Titan's Bane")
        if ran_sample[2] == 8:
            print("Brawler's Beat Stick")
        if ran_sample[2] == 9:
            print("Jotunn's Wrath")
        if ran_sample[2] == 10:
            print("The Crusher")
        if ran_sample[2] == 11:
            print("Transendence")
        if ran_sample[2] == 12:
            print("Hydra's Lament")
        if ran_sample[2] == 13:
            print("Deathbringer")
        if ran_sample[2] == 14:
            print("Rage")
        if ran_sample[2] == 15:
            print("Malice")
        if ran_sample[2] == 16:
            print("Soul Eater")
        if ran_sample[2] == 17:
            print("Devourer's Gauntlet")
        if ran_sample[2] == 18:
            print("Bloodforge")
        if ran_sample[2] == 19:
            print("Witchblade")
        if ran_sample[2] == 20:
            print("Winged Blade")
        if ran_sample[2] == 21:
            print("Relic Dagger")
        if ran_sample[2] == 22:
            print("Toxic Blade")
        if ran_sample[2] == 23:
            print("Frostbound Hammer")
        if ran_sample[2] == 24:
            print("Runeforged Hammer")
        if ran_sample[2] == 25:
            print("Blackthorn Hammer")
        if ran_sample[2] == 26:
            print("Shifter's Shield")
        if ran_sample[2] == 27:
            print("Void Shield")
        if ran_sample[2] == 28:
            print("Hide of the Nemean Lion")
        if ran_sample[2] == 29:
            print("Brestplate of Valor")
        if ran_sample[2] == 30:
            print("Spectral Armor")
        if ran_sample[2] == 31:
            print("Magi's Cloak")
        if ran_sample[2] == 32:
            print("Hide of the Urchin")
        if ran_sample[2] == 33:
            print("Spirit Robe")
        if ran_sample[2] == 34:
            print("Mantle of Discord")
        if ran_sample[2] == 35:
            print("Bulwark of Hope")
        if ran_sample[2] == 36:
            print("Pestilence")
        if ran_sample[2] == 37:
            print("Heartward Amulet")
        if ran_sample[2] == 38:
            print("Talisman of Energy")
        if ran_sample[2] == 39:
            print("Runic Shield")
        if ran_sample[2] == 40:
            print("Ancile")
        if ran_sample[2] == 41:
            print("Odysseus' Bow")
        if ran_sample[2] == 42:
            print("Stone of Gaia")
        if ran_sample[2] == 43:
            print("Shield of Regrowth")
        if ran_sample[2] == 44:
            print("Mail of Renewal")
        if ran_sample[2] == 45:
            print("Gauntlet of Thebes")
        if ran_sample[2] == 46:
            print("Wind Demon")
        if ran_sample[2] == 47:
            print("Poisoned Star")
        if ran_sample[2] == 48:
            print("Stone Cutting Sword")
        if ran_sample[2] == 49:
            print("Masamune")
        if ran_sample[2] == 50:
            print("Heartseeker")
        if ran_sample[2] == 51:
            print("Hastened Katana")
        if ran_sample[2] == 52:
            print("Genji's Guard")
        if ran_sample[2] == 53:
            print("Oni Hunter's Garb")
        if ran_sample[2] == 54:
            print("Shogun's Kusari")
        if ran_sample[2] == 55:
            print("Atlanta's Bow")
        if ran_sample[2] == 56:
            print("Asi")
        if ran_sample[2] == 57:
            print("Silverbranch Bow")
        if ran_sample[2] == 57:
            print("Ichaival")
        if ran_sample[2] == 58:
            print("Gladiator's Shield")
        if ran_sample[3] == 1:
            print("Sovereignty")
        if ran_sample[3] == 2:
            print("Mystical Mail")
        if ran_sample[3] == 3:
            print("Midgardian Mail")
        if ran_sample[3] == 4:
            print("Emperor's Armor")
        if ran_sample[3] == 5:
            print("The Executioner")
        if ran_sample[3] == 6:
            print("Qin's Sais")
        if ran_sample[3] == 7:
            print("Titan's Bane")
        if ran_sample[3] == 8:
            print("Brawler's Beat Stick")
        if ran_sample[3] == 9:
            print("Jotunn's Wrath")
        if ran_sample[3] == 10:
            print("The Crusher")
        if ran_sample[3] == 11:
            print("Transendence")
        if ran_sample[3] == 12:
            print("Hydra's Lament")
        if ran_sample[3] == 13:
            print("Deathbringer")
        if ran_sample[3] == 14:
            print("Rage")
        if ran_sample[3] == 15:
            print("Malice")
        if ran_sample[3] == 16:
            print("Soul Eater")
        if ran_sample[3] == 17:
            print("Devourer's Gauntlet")
        if ran_sample[3] == 18:
            print("Bloodforge")
        if ran_sample[3] == 19:
            print("Witchblade")
        if ran_sample[3] == 20:
            print("Winged Blade")
        if ran_sample[3] == 21:
            print("Relic Dagger")
        if ran_sample[3] == 22:
            print("Toxic Blade")
        if ran_sample[3] == 23:
            print("Frostbound Hammer")
        if ran_sample[3] == 24:
            print("Runeforged Hammer")
        if ran_sample[3] == 25:
            print("Blackthorn Hammer")
        if ran_sample[3] == 26:
            print("Shifter's Shield")
        if ran_sample[3] == 27:
            print("Void Shield")
        if ran_sample[3] == 28:
            print("Hide of the Nemean Lion")
        if ran_sample[3] == 29:
            print("Brestplate of Valor")
        if ran_sample[3] == 30:
            print("Spectral Armor")
        if ran_sample[3] == 31:
            print("Magi's Cloak")
        if ran_sample[3] == 32:
            print("Hide of the Urchin")
        if ran_sample[3] == 33:
            print("Spirit Robe")
        if ran_sample[3] == 34:
            print("Mantle of Discord")
        if ran_sample[3] == 35:
            print("Bulwark of Hope")
        if ran_sample[3] == 36:
            print("Pestilence")
        if ran_sample[3] == 37:
            print("Heartward Amulet")
        if ran_sample[3] == 38:
            print("Talisman of Energy")
        if ran_sample[3] == 39:
            print("Runic Shield")
        if ran_sample[3] == 40:
            print("Ancile")
        if ran_sample[3] == 41:
            print("Odysseus' Bow")
        if ran_sample[3] == 42:
            print("Stone of Gaia")
        if ran_sample[3] == 43:
            print("Shield of Regrowth")
        if ran_sample[3] == 44:
            print("Mail of Renewal")
        if ran_sample[3] == 45:
            print("Gauntlet of Thebes")
        if ran_sample[3] == 46:
            print("Wind Demon")
        if ran_sample[3] == 47:
            print("Poisoned Star")
        if ran_sample[3] == 48:
            print("Stone Cutting Sword")
        if ran_sample[3] == 49:
            print("Masamune")
        if ran_sample[3] == 50:
            print("Heartseeker")
        if ran_sample[3] == 51:
            print("Hastened Katana")
        if ran_sample[3] == 52:
            print("Genji's Guard")
        if ran_sample[3] == 53:
            print("Oni Hunter's Garb")
        if ran_sample[3] == 54:
            print("Shogun's Kusari")
        if ran_sample[3] == 55:
            print("Atlanta's Bow")
        if ran_sample[3] == 56:
            print("Asi")
        if ran_sample[3] == 57:
            print("Silverbranch Bow")
        if ran_sample[3] == 57:
            print("Ichaival")
        if ran_sample[3] == 58:
            print("Gladiator's Shield")
        if ran_sample[4] == 1:
            print("Sovereignty")
        if ran_sample[4] == 2:
            print("Mystical Mail")
        if ran_sample[4] == 3:
            print("Midgardian Mail")
        if ran_sample[4] == 4:
            print("Emperor's Armor")
        if ran_sample[4] == 5:
            print("The Executioner")
        if ran_sample[4] == 6:
            print("Qin's Sais")
        if ran_sample[4] == 7:
            print("Titan's Bane")
        if ran_sample[4] == 8:
            print("Brawler's Beat Stick")
        if ran_sample[4] == 9:
            print("Jotunn's Wrath")
        if ran_sample[4] == 10:
            print("The Crusher")
        if ran_sample[4] == 11:
            print("Transendence")
        if ran_sample[4] == 12:
            print("Hydra's Lament")
        if ran_sample[4] == 13:
            print("Deathbringer")
        if ran_sample[4] == 14:
            print("Rage")
        if ran_sample[4] == 15:
            print("Malice")
        if ran_sample[4] == 16:
            print("Soul Eater")
        if ran_sample[4] == 17:
            print("Devourer's Gauntlet")
        if ran_sample[4] == 18:
            print("Bloodforge")
        if ran_sample[4] == 19:
            print("Witchblade")
        if ran_sample[4] == 20:
            print("Winged Blade")
        if ran_sample[4] == 21:
            print("Relic Dagger")
        if ran_sample[4] == 22:
            print("Toxic Blade")
        if ran_sample[4] == 23:
            print("Frostbound Hammer")
        if ran_sample[4] == 24:
            print("Runeforged Hammer")
        if ran_sample[4] == 25:
            print("Blackthorn Hammer")
        if ran_sample[4] == 26:
            print("Shifter's Shield")
        if ran_sample[4] == 27:
            print("Void Shield")
        if ran_sample[4] == 28:
            print("Hide of the Nemean Lion")
        if ran_sample[4] == 29:
            print("Brestplate of Valor")
        if ran_sample[4] == 30:
            print("Spectral Armor")
        if ran_sample[4] == 31:
            print("Magi's Cloak")
        if ran_sample[4] == 32:
            print("Hide of the Urchin")
        if ran_sample[4] == 33:
            print("Spirit Robe")
        if ran_sample[4] == 34:
            print("Mantle of Discord")
        if ran_sample[4] == 35:
            print("Bulwark of Hope")
        if ran_sample[4] == 36:
            print("Pestilence")
        if ran_sample[4] == 37:
            print("Heartward Amulet")
        if ran_sample[4] == 38:
            print("Talisman of Energy")
        if ran_sample[4] == 39:
            print("Runic Shield")
        if ran_sample[4] == 40:
            print("Ancile")
        if ran_sample[4] == 41:
            print("Odysseus' Bow")
        if ran_sample[4] == 42:
            print("Stone of Gaia")
        if ran_sample[4] == 43:
            print("Shield of Regrowth")
        if ran_sample[4] == 44:
            print("Mail of Renewal")
        if ran_sample[4] == 45:
            print("Gauntlet of Thebes")
        if ran_sample[4] == 46:
            print("Wind Demon")
        if ran_sample[4] == 47:
            print("Poisoned Star")
        if ran_sample[4] == 48:
            print("Stone Cutting Sword")
        if ran_sample[4] == 49:
            print("Masamune")
        if ran_sample[4] == 50:
            print("Heartseeker")
        if ran_sample[4] == 51:
            print("Hastened Katana")
        if ran_sample[4] == 52:
            print("Genji's Guard")
        if ran_sample[4] == 53:
            print("Oni Hunter's Garb")
        if ran_sample[4] == 54:
            print("Shogun's Kusari")
        if ran_sample[4] == 55:
            print("Atlanta's Bow")
        if ran_sample[4] == 56:
            print("Asi")
        if ran_sample[4] == 57:
            print("Silverbranch Bow")
        if ran_sample[4] == 57:
            print("Ichaival")
        if ran_sample[4] == 58:
            print("Gladiator's Shield")       
    Build()
    print('\n' "~//~")
    retry()
        
    

def magical():
    god = randint(1,45)
    if god == 1:
        print("You got Agni")
    if god == 2:
        print("You got Ah Puch")
    if god == 3:
        print("You got Anubis")
    if god == 4:
        print("You got Ao Kuang")
    if god == 5:
        print("You got Aphrodite")
    if god == 6:
        print("You got Ares")
    if god == 7:
        print("You got Artio")
    if god == 8:
        print("You got Athena")
    if god == 9:
        print("You got Bacchus")
    if god == 10:
        print("You got Baron Samedi")
    if god == 11:
        print("You got Cabrakan")
    if god == 12:
        print("You got Cerberus")
    if god == 13:
        print("You got Chang'e")
    if god == 14:
        print("You got Chronos")
    if god == 15:
        print("You got Discordia")
    if god == 16:
        print("You got Fafnir")
    if god == 17:
        print("You got Freya")
    if god == 18:
        print("You got Ganesha")
    if god == 19:
        print("You got Geb")
    if god == 20:
        print("You got Hades")
    if god == 21:
        print("You got He Bo")
    if god == 22:
        print("You got Hel")
    if god == 23:
        print("You got Isis")
    if god == 24:
        print("You got Janus")
    if god == 25:
        print("You got Khepri")
    if god == 26:
        print("You got Kukulkan")
    if god == 27:
        print("You got Kumbhakarna")
    if god == 28:
        print("You got Kuzenbo")
    if god == 29:
        print("You got Nox")
    if god == 30:
        print("You got Nu Wa")
    if god == 31:
        print("You got Poseidon")
    if god == 32:
        print("You got Ra")
    if god == 33:
        print("You got Raijin")
    if god == 34:
        print("You got Scylla")
    if god == 35:
        print("You got Sobek")
    if god == 36:
        print("You got Sol")
    if god == 37:
        print("You got Sylvanus")
    if god == 38:
        print("You got Terra")
    if god == 39:
        print("You got The Morrigan")
    if god == 40:
        print("You got Thoth")
    if god == 41:
        print("You got Vulcan")
    if god == 42:
        print("You got Xing Tian")
    if god == 43:
        print("You got Zeus")
    if god == 44:
        print("You got Zhong Kui")
    if god == 45:
        print("You got Ymir")
    lst_samples = range(0,50)
    ran_sample = random.sample(lst_samples,5)
    print("~//~" '\n')
    def boots():
        boots = randint(1,4)
        if boots == 1:
            print("Shoes of the Magi")
        if boots == 2:
            print("Shoes of Focus")
        if boots == 3:
            print("Reinforced Shoes")
        if boots == 4:
            print("Traveler's Shoes")
    boots()
    def Build():
        if ran_sample[0] == 1:
            print("Sovereignty")
            second=1
        if ran_sample[0] == 2:
            print("Mystical Mail")
            second=2
        if ran_sample[0] == 3:
            print("Midgardian Mail")
            second=3
        if ran_sample[0] == 4:
            print("Emeror's Armor")
            second=4
        if ran_sample[0] == 5:
            print("Pythagorem's Piece")
            second=5
        if ran_sample[0] == 6:
            print("Bancroft's Talon")
            second=6
        if ran_sample[0] == 7:
            print("Typhon's Fang")
            second=7
        if ran_sample[0] == 8:
            print("Soul Gem")
            second=8
        if ran_sample[0] == 9:
            print("Hide of the Nemean Lion")
            second=9
        if ran_sample[0] == 10:
            print("Brestplate of Valor")
            second=10
        if ran_sample[0] == 11:
            print("Spectral Armor")
            second=11
        if ran_sample[0] == 12:
            print("Magi's Cloak")
            second=12
        if ran_sample[0] == 13:
            print("Hide of the Urchin")
            second=13
        if ran_sample[0] == 14:
            print("Spirit Robe")
            second=14
        if ran_sample[0] == 15:
            print("Mantle of Discord")
            second=15
        if ran_sample[0] == 16:
            print("Bulwark of Hope")
            second=16
        if ran_sample[0] == 17:
            print("Pestilence")
            second=17
        if ran_sample[0] == 18:
            print("Heartward Amulent")
            second=18
        if ran_sample[0] == 19:
            print("Talisman of Energy")
            second=19
        if ran_sample[0] == 20:
            print("Demonic Grip")
            second=20
        if ran_sample[0] == 21:
            print("Telkhines Ring")
            second=21
        if ran_sample[0] == 22:
            print("Shaman's Ring")
            second=22
        if ran_sample[0] == 23:
            print("Hastened Ring")
            second=23
        if ran_sample[0] == 24:
            print("Obsidian Shard")
            second=24
        if ran_sample[0] == 25:
            print("Divine Ruin")
            second=25
        if ran_sample[0] == 26:
            print("Spear of the Magus")
            second=26
        if ran_sample[0] == 27:
            print("Spear of Desolation")
            second=27
        if ran_sample[0] == 28:
            print("Gem of Isolation")
            second=28
        if ran_sample[0] == 29:
            print("Warlock's Staff")
            second=29
        if ran_sample[0] == 30:
            print("Etheral Staff")
            second=30
        if ran_sample[0] == 31:
            print("Rod of Asclepius")
            second=31
        if ran_sample[0] == 32:
            print("Book of Thoth")
            second=32
        if ran_sample[0] == 33:
            print("Polynomicon")
            second=33
        if ran_sample[0] == 34:
            print("Soul Reaver")
            second=34
        if ran_sample[0] == 35:
            print("Book of the Dead")
            second=35
        if ran_sample[0] == 36:
            print("Rod of Tahuti")
            second=36
        if ran_sample[0] == 37:
            print("Chronos' Pendant")
            second=37
        if ran_sample[0] == 38:
            print("Celestial Legion Helm")
            second=38
        if ran_sample[0] == 39:
            print("Lotus Crown")
            second=39
        if ran_sample[0] == 40:
            print("Jade Emperor's Crown")
            second=40
        if ran_sample[0] == 41:
            print("Stone of Gaia")
            second=41
        if ran_sample[0] == 42:
            print("Shield of Regrowth")
            second=42
        if ran_sample[0] == 43:
            print("Gauntlet of Thebes")
            second=43
        if ran_sample[0] == 44:
            print("Genji's Guard")
            second=44
        if ran_sample[0] == 45:
            print("Oni Hunter's Garb")
            second=45
        if ran_sample[0] == 46:
            print("Shogun's Kusari")
            second=46
        if ran_sample[0] == 47:
            print("Void Stone")
            second=47
        if ran_sample[0] == 48:
            print("Stone of Fal")
            second=48
        if ran_sample[0] == 49:
            print("Mail of Renewal")
            second=49
        if ran_sample[0] == 50:
            print("Doom Orb")
        if ran_sample[1] == 1:
            print("Sovereignty")
            third=1
        if ran_sample[1] == 2:
            print("Mystical Mail")
            third=2
        if ran_sample[1] == 3:
            print("Midgardian Mail")
            third=3
        if ran_sample[1] == 4:
            print("Emeror's Armor")
            third=4
        if ran_sample[1] == 5:
            print("Pythagorem's Piece")
            third=5
        if ran_sample[1] == 6:
            print("Bancroft's Talon")
            third=6
        if ran_sample[1] == 7:
            print("Typhon's Fang")
            third=7
        if ran_sample[1] == 8:
            print("Soul Gem")
            third=8
        if ran_sample[1] == 9:
            print("Hide of the Nemean Lion")
            third=9
        if ran_sample[1] == 10:
            print("Brestplate of Valor")
            third=10
        if ran_sample[1] == 11:
            print("Spectral Armor")
            third=11
        if ran_sample[1] == 12:
            print("Magi's Cloak")
            third=12
        if ran_sample[1] == 13:
            print("Hide of the Urchin")
            third=13
        if ran_sample[1] == 14:
            print("Spirit Robe")
            third=14
        if ran_sample[1] == 15:
            print("Mantle of Discord")
            third=15
        if ran_sample[1] == 16:
            print("Bulwark of Hope")
            third=16
        if ran_sample[1] == 17:
            print("Pestilence")
            third=17
        if ran_sample[1] == 18:
            print("Heartward Amulent")
            third=18
        if ran_sample[1] == 19:
            print("Talisman of Energy")
            third=19
        if ran_sample[1] == 20:
            print("Demonic Grip")
            third=20
        if ran_sample[1] == 21:
            print("Telkhines Ring")
            third=21
        if ran_sample[1] == 22:
            print("Shaman's Ring")
            third=22
        if ran_sample[1] == 23:
            print("Hastened Ring")
            third=23
        if ran_sample[1] == 24:
            print("Obsidian Shard")
            third=24
        if ran_sample[1] == 25:
            print("Divine Ruin")
            third=25
        if ran_sample[1] == 26:
            print("Spear of the Magus")
            third=26
        if ran_sample[1] == 27:
            print("Spear of Desolation")
            third=27
        if ran_sample[1] == 28:
            print("Gem of Isolation")
            third=28
        if ran_sample[1] == 29:
            print("Warlock's Staff")
            third=29
        if ran_sample[1] == 30:
            print("Etheral Staff")
            third=30
        if ran_sample[1] == 31:
            print("Rod of Asclepius")
            third=31
        if ran_sample[1] == 32:
            print("Book of Thoth")
            third=32
        if ran_sample[1] == 33:
            print("Polynomicon")
            third=33
        if ran_sample[1] == 34:
            print("Soul Reaver")
            third=34
        if ran_sample[1] == 35:
            print("Book of the Dead")
            third=35
        if ran_sample[1] == 36:
            print("Rod of Tahuti")
            third=36
        if ran_sample[1] == 37:
            print("Chronos' Pendant")
            third=37
        if ran_sample[1] == 38:
            print("Celestial Legion Helm")
            third=38
        if ran_sample[1] == 39:
            print("Lotus Crown")
            third=39
        if ran_sample[1] == 40:
            print("Jade Emperor's Crown")
            third=40
        if ran_sample[1] == 41:
            print("Stone of Gaia")
            third=41
        if ran_sample[1] == 42:
            print("Shield of Regrowth")
            third=42
        if ran_sample[1] == 43:
            print("Gauntlet of Thebes")
            third=43
        if ran_sample[1] == 44:
            print("Genji's Guard")
            third=44
        if ran_sample[1] == 45:
            print("Oni Hunter's Garb")
            third=45
        if ran_sample[1] == 46:
            print("Shogun's Kusari")
            third=46
        if ran_sample[1] == 47:
            print("Void Stone")
            third=47
        if ran_sample[1] == 48:
            print("Stone of Fal")
            third=48
        if ran_sample[1] == 49:
            print("Mail of Renewal")
            third=49
        if ran_sample[1] == 50:
            print("Doom Orb")
        if ran_sample[2] == 1:
            print("Sovereignty")
            fourth=1
        if ran_sample[2] == 2:
            print("Mystical Mail")
            fourth=2
        if ran_sample[2] == 3:
            print("Midgardian Mail")
            fourth=3
        if ran_sample[2] == 4:
            print("Emeror's Armor")
            fourth=4
        if ran_sample[2] == 5:
            print("Pythagorem's Piece")
            fourth=5
        if ran_sample[2] == 6:
            print("Bancroft's Talon")
            fourth=6
        if ran_sample[2] == 7:
            print("Typhon's Fang")
            fourth=7
        if ran_sample[2] == 8:
            print("Soul Gem")
            fourth=8
        if ran_sample[2] == 9:
            print("Hide of the Nemean Lion")
            fourth=9
        if ran_sample[2] == 10:
            print("Brestplate of Valor")
            fourth=10
        if ran_sample[2] == 11:
            print("Spectral Armor")
            fourth=11
        if ran_sample[2] == 12:
            print("Magi's Cloak")
            fourth=12
        if ran_sample[2] == 13:
            print("Hide of the Urchin")
            fourth=13
        if ran_sample[2] == 14:
            print("Spirit Robe")
            fourth=14
        if ran_sample[2] == 15:
            print("Mantle of Discord")
            fourth=15
        if ran_sample[2] == 16:
            print("Bulwark of Hope")
            fourth=16
        if ran_sample[2] == 17:
            print("Pestilence")
            fourth=17
        if ran_sample[2] == 18:
            print("Heartward Amulent")
            fourth=18
        if ran_sample[2] == 19:
            print("Talisman of Energy")
            fourth=19
        if ran_sample[2] == 20:
            print("Demonic Grip")
            fourth=20
        if ran_sample[2] == 21:
            print("Telkhines Ring")
            fourth=21
        if ran_sample[2] == 22:
            print("Shaman's Ring")
            fourth=22
        if ran_sample[2] == 23:
            print("Hastened Ring")
            fourth=23
        if ran_sample[2] == 24:
            print("Obsidian Shard")
            fourth=24
        if ran_sample[2] == 25:
            print("Divine Ruin")
            fourth=25
        if ran_sample[2] == 26:
            print("Spear of the Magus")
            fourth=26
        if ran_sample[2] == 27:
            print("Spear of Desolation")
            fourth=27
        if ran_sample[2] == 28:
            print("Gem of Isolation")
            fourth=28
        if ran_sample[2] == 29:
            print("Warlock's Staff")
            fourth=29
        if ran_sample[2] == 30:
            print("Etheral Staff")
            fourth=30
        if ran_sample[2] == 31:
            print("Rod of Asclepius")
            fourth=31
        if ran_sample[2] == 32:
            print("Book of Thoth")
            fourth=32
        if ran_sample[2] == 33:
            print("Polynomicon")
            fourth=33
        if ran_sample[2] == 34:
            print("Soul Reaver")
            fourth=34
        if ran_sample[2] == 35:
            print("Book of the Dead")
            fourth=35
        if ran_sample[2] == 36:
            print("Rod of Tahuti")
            fourth=36
        if ran_sample[2] == 37:
            print("Chronos' Pendant")
            fourth=37
        if ran_sample[2] == 38:
            print("Celestial Legion Helm")
            fourth=38
        if ran_sample[2] == 39:
            print("Lotus Crown")
            fourth=39
        if ran_sample[2] == 40:
            print("Jade Emperor's Crown")
            fourth=40
        if ran_sample[2] == 41:
            print("Stone of Gaia")
            fourth=41
        if ran_sample[2] == 42:
            print("Shield of Regrowth")
            fourth=42
        if ran_sample[2] == 43:
            print("Gauntlet of Thebes")
            fourth=43
        if ran_sample[2] == 44:
            print("Genji's Guard")
            fourth=44
        if ran_sample[2] == 45:
            print("Oni Hunter's Garb")
            fourth=45
        if ran_sample[2] == 46:
            print("Shogun's Kusari")
            fourth=46
        if ran_sample[2] == 47:
            print("Void Stone")
            fourth=47
        if ran_sample[2] == 48:
            print("Stone of Fal")
            fourth=48
        if ran_sample[2] == 49:
            print("Mail of Renewal")
            fourth=49
        if ran_sample[2] == 50:
            print("Doom Orb")
        if ran_sample[3] == 1:
            print("Sovereignty")
            fifth=1
        if ran_sample[3] == 2:
            print("Mystical Mail")
            fifth=2
        if ran_sample[3] == 3:
            print("Midgardian Mail")
            fifth=3
        if ran_sample[3] == 4:
            print("Emeror's Armor")
            fifth=4
        if ran_sample[3] == 5:
            print("Pythagorem's Piece")
            fifth=5
        if ran_sample[3] == 6:
            print("Bancroft's Talon")
            fifth=6
        if ran_sample[3] == 7:
            print("Typhon's Fang")
            fifth=7
        if ran_sample[3] == 8:
            print("Soul Gem")
            fifth=8
        if ran_sample[3] == 9:
            print("Hide of the Nemean Lion")
            fifth=9
        if ran_sample[3] == 10:
            print("Brestplate of Valor")
            fifth=10
        if ran_sample[3] == 11:
            print("Spectral Armor")
            fifth=11
        if ran_sample[3] == 12:
            print("Magi's Cloak")
            fifth=12
        if ran_sample[3] == 13:
            print("Hide of the Urchin")
            fifth=13
        if ran_sample[3] == 14:
            print("Spirit Robe")
            fifth=14
        if ran_sample[3] == 15:
            print("Mantle of Discord")
            fifth=15
        if ran_sample[3] == 16:
            print("Bulwark of Hope")
            fifth=16
        if ran_sample[3] == 17:
            print("Pestilence")
            fifth=17
        if ran_sample[3] == 18:
            print("Heartward Amulent")
            fifth=18
        if ran_sample[3] == 19:
            print("Talisman of Energy")
            fifth=19
        if ran_sample[3] == 20:
            print("Demonic Grip")
            fifth=20
        if ran_sample[3] == 21:
            print("Telkhines Ring")
            fifth=21
        if ran_sample[3] == 22:
            print("Shaman's Ring")
            fifth=22
        if ran_sample[3] == 23:
            print("Hastened Ring")
            fifth=23
        if ran_sample[3] == 24:
            print("Obsidian Shard")
            fifth=24
        if ran_sample[3] == 25:
            print("Divine Ruin")
            fifth=25
        if ran_sample[3] == 26:
            print("Spear of the Magus")
            fifth=26
        if ran_sample[3] == 27:
            print("Spear of Desolation")
            fifth=27
        if ran_sample[3] == 28:
            print("Gem of Isolation")
            fifth=28
        if ran_sample[3] == 29:
            print("Warlock's Staff")
            fifth=29
        if ran_sample[3] == 30:
            print("Etheral Staff")
            fifth=30
        if ran_sample[3] == 31:
            print("Rod of Asclepius")
            fifth=31
        if ran_sample[3] == 32:
            print("Book of Thoth")
            fifth=32
        if ran_sample[3] == 33:
            print("Polynomicon")
            fifth=33
        if ran_sample[3] == 34:
            print("Soul Reaver")
            fifth=34
        if ran_sample[3] == 35:
            print("Book of the Dead")
            fifth=35
        if ran_sample[3] == 36:
            print("Rod of Tahuti")
            fifth=36
        if ran_sample[3] == 37:
            print("Chronos' Pendant")
            fifth=37
        if ran_sample[3] == 38:
            print("Celestial Legion Helm")
            fifth=38
        if ran_sample[3] == 39:
            print("Lotus Crown")
            fifth=39
        if ran_sample[3] == 40:
            print("Jade Emperor's Crown")
            fifth=40
        if ran_sample[3] == 41:
            print("Stone of Gaia")
            fifth=41
        if ran_sample[3] == 42:
            print("Shield of Regrowth")
            fifth=42
        if ran_sample[3] == 43:
            print("Gauntlet of Thebes")
            fifth=43
        if ran_sample[3] == 44:
            print("Genji's Guard")
            fifth=44
        if ran_sample[3] == 45:
            print("Oni Hunter's Garb")
            fifth=45
        if ran_sample[3] == 46:
            print("Shogun's Kusari")
            fifth=46
        if ran_sample[3] == 47:
            print("Void Stone")
            fifth=47
        if ran_sample[3] == 48:
            print("Stone of Fal")
            fifth=48
        if ran_sample[3] == 49:
            print("Mail of Renewal")
            fifth=49
        if ran_sample[3] == 50:
            print("Doom Orb")
        if ran_sample[4] == 1:
            print("Sovereignty")
            sixth=1
        if ran_sample[4] == 2:
            print("Mystical Mail")
            sixth=2
        if ran_sample[4] == 3:
            print("Midgardian Mail")
            sixth=3
        if ran_sample[4] == 4:
            print("Emeror's Armor")
            sixth=4
        if ran_sample[4] == 5:
            print("Pythagorem's Piece")
            sixth=5
        if ran_sample[4] == 6:
            print("Bancroft's Talon")
            sixth=6
        if ran_sample[4] == 7:
            print("Typhon's Fang")
            sixth=7
        if ran_sample[4] == 8:
            print("Soul Gem")
            sixth=8
        if ran_sample[4] == 9:
            print("Hide of the Nemean Lion")
            sixth=9
        if ran_sample[4] == 10:
            print("Brestplate of Valor")
            sixth=10
        if ran_sample[4] == 11:
            print("Spectral Armor")
            sixth=11
        if ran_sample[4] == 12:
            print("Magi's Cloak")
            sixth=12
        if ran_sample[4] == 13:
            print("Hide of the Urchin")
            sixth=13
        if ran_sample[4] == 14:
            print("Spirit Robe")
            sixth=14
        if ran_sample[4] == 15:
            print("Mantle of Discord")
            sixth=15
        if ran_sample[4] == 16:
            print("Bulwark of Hope")
            sixth=16
        if ran_sample[4] == 17:
            print("Pestilence")
            sixth=17
        if ran_sample[4] == 18:
            print("Heartward Amulent")
            sixth=18
        if ran_sample[4] == 19:
            print("Talisman of Energy")
            sixth=19
        if ran_sample[4] == 20:
            print("Demonic Grip")
            sixth=20
        if ran_sample[4] == 21:
            print("Telkhines Ring")
            sixth=21
        if ran_sample[4] == 22:
            print("Shaman's Ring")
            sixth=22
        if ran_sample[4] == 23:
            print("Hastened Ring")
            sixth=23
        if ran_sample[4] == 24:
            print("Obsidian Shard")
            sixth=24
        if ran_sample[4] == 25:
            print("Divine Ruin")
            sixth=25
        if ran_sample[4] == 26:
            print("Spear of the Magus")
            sixth=26
        if ran_sample[4] == 27:
            print("Spear of Desolation")
            sixth=27
        if ran_sample[4] == 28:
            print("Gem of Isolation")
            sixth=28
        if ran_sample[4] == 29:
            print("Warlock's Staff")
            sixth=29
        if ran_sample[4] == 30:
            print("Etheral Staff")
            sixth=30
        if ran_sample[4] == 31:
            print("Rod of Asclepius")
            sixth=31
        if ran_sample[4] == 32:
            print("Book of Thoth")
            sixth=32
        if ran_sample[4] == 33:
            print("Polynomicon")
            sixth=33
        if ran_sample[4] == 34:
            print("Soul Reaver")
            sixth=34
        if ran_sample[4] == 35:
            print("Book of the Dead")
            sixth=35
        if ran_sample[4] == 36:
            print("Rod of Tahuti")
            sixth=36
        if ran_sample[4] == 37:
            print("Chronos' Pendant")
            sixth=37
        if ran_sample[4] == 38:
            print("Celestial Legion Helm")
            sixth=38
        if ran_sample[4] == 39:
            print("Lotus Crown")
            sixth=39
        if ran_sample[4] == 40:
            print("Jade Emperor's Crown")
            sixth=40
        if ran_sample[4] == 41:
            print("Stone of Gaia")
            sixth=41
        if ran_sample[4] == 42:
            print("Shield of Regrowth")
            sixth=42
        if ran_sample[4] == 43:
            print("Gauntlet of Thebes")
            sixth=43
        if ran_sample[4] == 44:
            print("Genji's Guard")
            sixth=44
        if ran_sample[4] == 45:
            print("Oni Hunter's Garb")
            sixth=45
        if ran_sample[4] == 46:
            print("Shogun's Kusari")
            sixth=46
        if ran_sample[4] == 47:
            print("Void Stone")
            sixth=47
        if ran_sample[4] == 48:
            print("Stone of Fal")
            sixth=48
        if ran_sample[4] == 49:
            print("Mail of Renewal")
            sixth=49
        if ran_sample[4] == 50:
            print("Doom Orb")
    Build()
    print('\n' "~//~")
    
    retry()

def retry():
    tryag=["Y","y","yes","YES","Yes","YeS","n","N","NO","No","no"]
    retry=""
    print("Would you like to get another build? Y/N")
    retry = str(input(">>>"))

    if retry == tryag[1]:
        God()
    if retry == tryag[2]:
        God()
    if retry == tryag[0]:
        God()
    if retry == tryag[3]:
        God()
    if retry == tryag[4]:
        God()
    if retry == tryag[5]:
        God()
    if retry == tryag[6]:
        exit()
    if retry == tryag[7]:
        exit()
    if retry == tryag[8]:
        exit()
    if retry == tryag[9]:
        exit()
    if retry == tryag[10]:
        exit()

God()


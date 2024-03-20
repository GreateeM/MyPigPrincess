label FreeEnding:
    stop music fadeout 1.0
    scene black with dissolve
    pause 0.3
    play sound "audio/soundFX/FX2/dat-s-right.wav"
    window show
    $ _skipping = False
    $ preferences.afm_enable = False
    "{color=#FFE159} {i}This ends the first Chapter of \" My Pig Princess\"! {/color}{/i}"
    "{color=#FFE159} {i}You can play {u}Chapter 2{/u}{space=5} {b}AND{/b}{space=5} {u}Chapter 3{/u} over on my Patreon right now for 3$! {space=285}  www.Patreon.com/CyanCapsule {/color}{/i}"
    "{color=#FFE159} {i}Supporting also grants you access to my art before it goes into the game, and for 6$ you get access to my behind-the-scenes sketches & PSDs! {/color}{/i}"
    "{color=#FFE159} {i}Thank you for reading and playing!{/color}{/i}"
    "{color=#FFE159} {b}~End~{/color}{/b}"
    "{color=#FFE159} {i}Returning you to the Main Menu next.{/color}{/i}"
    "{color=#FFE159} {i}Button linking to my Patreon can be found in the bottom right corner!{/color}{/i}"
    $ _skipping = True
    window hide
    $ renpy.music.set_volume(0.90, delay=0, channel='music')
    pause 0.1
    $ renpy.music.set_volume(0.80, delay=0, channel='music')
    pause 0.1
    $ renpy.music.set_volume(0.70, delay=0, channel='music')
    pause 0.1
    $ renpy.music.set_volume(0.60, delay=0, channel='music')
    pause 0.1
    $ renpy.music.set_volume(0.50, delay=0, channel='music')
    pause 0.1
    $ renpy.music.set_volume(0.40, delay=0, channel='music')
    pause 0.1
    $ renpy.music.set_volume(0.30, delay=0, channel='music')
    pause 0.1
    $ renpy.music.set_volume(0.20, delay=0, channel='music')
    pause 0.1
    $ renpy.music.set_volume(0.10, delay=0, channel='music')
    pause 0.1
    $ renpy.music.set_volume(0.00, delay=0, channel='music')
    $ renpy.pause(2.0, hard=True)
    return

# This ends the game

label Ending:
    stop music fadeout 1.0
    scene black with dissolve
    pause 0.3
    play sound "audio/soundFX/FX2/dat-s-right.wav"
    window show
    $ _skipping = False
    $ preferences.afm_enable = False
    "{color=#FFE159} {i}This ends the {u}Seventh{/u} Chapter of \" My Pig Princess\"! {/color}{/i}"
    "{color=#FFE159} {i}Thank you for playing!{/color}{/i}"
    "{color=#FFE159} {i}Consider supporting the project and my art over at: \n www.Patreon.com/CyanCapsule {/color}{/i}"
    "{color=#FFE159} {b}~To be continued~{/color}{/b}"
    "{color=#FFE159} {i}Returning you to the Main Menu.{/color}{/i}"
    $ _skipping = True
    window hide
    $ renpy.music.set_volume(0.90, delay=0, channel='music')
    pause 0.1
    $ renpy.music.set_volume(0.80, delay=0, channel='music')
    pause 0.1
    $ renpy.music.set_volume(0.70, delay=0, channel='music')
    pause 0.1
    $ renpy.music.set_volume(0.60, delay=0, channel='music')
    pause 0.1
    $ renpy.music.set_volume(0.50, delay=0, channel='music')
    pause 0.1
    $ renpy.music.set_volume(0.40, delay=0, channel='music')
    pause 0.1
    $ renpy.music.set_volume(0.30, delay=0, channel='music')
    pause 0.1
    $ renpy.music.set_volume(0.20, delay=0, channel='music')
    pause 0.1
    $ renpy.music.set_volume(0.10, delay=0, channel='music')
    pause 0.1
    $ renpy.music.set_volume(0.00, delay=0, channel='music')
    $ renpy.pause(2.0, hard=True)
    return


# This ends the game

image splash = "splash.png"

#Enable below to turn on loading screen.

#label splashscreen:
#     scene black
#     with Pause(1)


#     show splash with dissolve
#     with Pause(2)

#     scene black with dissolve
#     with Pause(1)

#     return

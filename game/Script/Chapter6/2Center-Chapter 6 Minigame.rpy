#Timer etc.

#eyepoke?!"
#Bleeding, fuck!

#If bleeding isnt controlled, Rolf loses via TKO Doctor Stoppage. He then gets pissed off and goes to drink. Ilves also shows his sad art and is sad he can't continue later. " beer is on me, soldier... Sorry I couldn't get it done."
#Ilves later comes back with a big belt of the pig pits showing he won it all. If you lose u later spot the bull with the belt?

label minigamecut:
    call enable_minigame_mode from _call_enable_minigame_mode

    scene rolfcutbase
    show blackshake at truecenter zorder -100
    show rolfcuteye shut
    show rolfcuteyeblood shut
    show blackshake at truecenter behind rolfcutbase


    window hide
    pause 0.3

    play sound "audio/soundFX/FX6/615949__julesv4__ding-effectedit.wav" volume 0.6
    show screen minigametimer(duration=60, failure_label='aftercutloss') with Dissolve(0.3)
    with vpunch
    play music "audio/MPP_-_Patch_Him_Up_Loop.mp3" fadein 0.0 volume 0.14
    window show
    "SHIT! What do I do again?!"
    $ step1correct = False
    $ step2correct = False
    $ step3correct = False
    $ bandaidscold = False
    $ eyeironfail = False

    window hide
label cutquest:

    menu(screen='positionable_choice', ypos=500):
        with dissolve

        "{alpha=*0.87}Wipe {size=-2}the{/size} blood away {size=-2} with a{/size} {space=4}{/alpha}{size=+6}Towel{/size}{alpha=*0.87}{space=8}{/alpha}" if step1correct == False:
            call disable_saving from _call_disable_saving
            pause 0.3
            play sound "audio/soundFX/softget.wav" volume 1.6
            show rolfcuttowel clean with dissolve
            pause 0.5
            show rolfcuttowel bloody with dissolve
            pause 0.9
            play sound "audio/soundFX/move2.wav"
            hide rolfcuttowel
            hide rolfcuteyeblood
            show rolfcut openn
            with dissolve
            pause 0.1
            play sound "audio/soundFX/FX6/bloodspurt.wav" volume 0.5
            show rolfcutspurt
            with dissolve
            with vpunch
            pause 0.1
            play sound "audio/soundFX/FX6/blooddrips.wav" volume 0.5
            show rolfcuteye us
            hide rolfcutspurt
            show rolfcutblood
            show rolfcutfrown base behind rolfcut
            with dissolve

            pause 0.4

            window show
            me"GHAH! "
            "The blood's gone, but now the wound's wide open!"
            window hide
            hide rolfcutblood with dissolve

            pause 0.2
            show rolfcuteye usb
            show rolfcutfrown usb
            with dissolve
            pause 0.2
            $ step1correct = True
            jump cutquest




        "{alpha=*0.87}Apply {space=3}{/alpha}{size=+6}Vaseline{/size}{alpha=*0.87}{space=3}{size=-2} to the {/size} wound{/alpha}"if step3correct == False:#Fails. " The blood just mixes with the vaseline!"
            call disable_saving from _call_disable_saving_1
            if step1correct == False:
                pause 0.2
                play sound "audio/soundFX/FX6/167075__drminky__slime-land.wav" volume 1.0
                show rolfcuthand two
                with dissolve
                with hpunch
                pause 0.2
                hide rolfcutfrown
                with dissolve
                pause 0.9
                with vpunch
                play sound "audio/soundFX/FX6/bloodspurt.wav" volume 0.5

                show rolfcutspurt
                hide rolfcuthand
                with dissolve
                play sound "audio/soundFX/FX6/blooddrips.wav" volume 0.5
                hide rolfcuteyeblood
                hide rolfcutspurt
                show rolfcutblood
                show rolfcuteyeblood shut behind rolfcutblood
                with dissolve

                pause 0.4

                window show
                me"SHIEHT! "
                "Blood spurted out right as I touched him!"
                "I can't use the vaseline yet!"
                window hide
                pause 0.2

                hide rolfcutblood
                with dissolve
                pause 0.2
                show rolfcutfrown shut behind rolfcuteyeblood
                with dissolve
                jump cutquest




            if step2correct == True:
                pause 0.2
                $ step3correct = True
                play sound "audio/soundFX/FX6/167075__drminky__slime-land.wav" volume 1.0
                show rolfcuthand two
                with dissolve
                with vpunch
                pause 0.3
                show rolfcuteye us
                show rolfcutfrown base
                with dissolve
                pause 0.3

                play sound "audio/soundFX/FX6/167073__drminky__squelchy-squirt.wav" volume 1.0
                show rolfcuthand one
                show rolfcut goo
                with dissolve

                # You win! You can't run out of time if you've clicked this this far. Timer fades.

                pause 0.8
                hide rolfcuthand with dissolve
                show rolfcut goob with dissolve


                if step1correct == True:
                    if step2correct == True:

                        stop music fadeout 0.7

                        jump aftercutminigamewin

            if step1correct == True:
                pause 0.2
                play sound "audio/soundFX/FX6/167075__drminky__slime-land.wav" volume 1.0
                show rolfcuthand two
                with dissolve
                with hpunch
                pause 0.2
                hide rolfcutfrown
                show rolfcuteye squintus
                with dissolve
                pause 0.9
                with vpunch
                play sound "audio/soundFX/FX6/bloodspurt.wav" volume 0.5

                show rolfcutspurt
                hide rolfcuthand
                with dissolve
                play sound "audio/soundFX/FX6/blooddrips.wav" volume 0.5
                hide rolfcuteyeblood
                hide rolfcutspurt
                show rolfcutblood
                with dissolve

                pause 0.4

                window show
                me"SHIEHT! "
                "Blood spurted straight at me before I could get the vaseline in place!"
                "I can't use it yet!"
                window hide
                pause 0.2

                hide rolfcutblood
                with dissolve
                show rolfcutfrown usb
                show rolfcuteye usb
                with dissolve
                jump cutquest


            jump cutquest


        " {alpha=*0.87}Press{size=-2} the{/size} {space=3}{/alpha}{size=+6}Eye-Iron{/size}{alpha=*0.87} {space=3}{size=-2} on it{/size}{/alpha}"if eyeironfail == False: # It doesnt seem to do much!"
            call disable_saving from _call_disable_saving_2
            if step1correct == False:
                play sound "audio/soundFX/sit pillow.wav" volume 1.0
                show rolfcuthand press
                show rolfcutfrown shut behind rolfcut, rolfcuthand
                show rolfcuteye shut
                with dissolve
                with vpunch
                pause 4.0
                play sound "audio/soundFX/move.wav" volume 1.0
                hide rolfcutfrown
                hide rolfcuthand press
                with dissolve
                pause 0.2
                window show
                "It didn't do anything!!"
                window hide
                # $ eyeironfail = True
                jump cutquest
            if step1correct == True:
                play sound "audio/soundFX/sit pillow.wav" volume 1.0
                show rolfcuthand press
                show rolfcutfrown shut behind rolfcut, rolfcuthand
                show rolfcuteye shut
                with dissolve
                with vpunch
                pause 4.0
                play sound "audio/soundFX/move.wav" volume 1.0
                hide rolfcutfrown
                hide rolfcuthand press
                with dissolve
                pause 0.2
                window show
                "It didn't do anything!!"
                window hide
                show rolfcutfrown usb
                show rolfcuteye usb
                with dissolve
                #$ eyeironfail = True
                jump cutquest


        " {alpha=*0.87}Constrict {size=-2}the{/size} wound{size=-2} with an{/size} {space=4}{/alpha}{size=+6}Ointment Swab{space=8}{/size}{alpha=*0.87}{/alpha}"if step2correct == False:# " Gah, It keeps sliding off, the area is too messy!"
            call disable_saving from _call_disable_saving_3
            if step1correct == False:
                pause 0.2
                play sound "audio/soundFX/move.wav" volume 1.0
                show swabs one with dissolve
                pause 0.2
                show swabs two with dissolve
                pause 1.1
                with vpunch
                play sound "audio/soundFX/FX6/bloodspurt.wav" volume 0.5
                hide swabs
                show rolfcutspurt
                with dissolve

                pause 0.1
                with hpunch
                play sound "audio/soundFX/FX6/blooddrips.wav" volume 0.5
                hide rolfcutspurt
                show rolfcutblood
                show rolfcutfrown shut behind rolfcuteyeblood
                with dissolve

                pause 0.4

                window show
                me "PHAH! "
                "That didn't work at all! It just made blood spurt all over me!"
                window hide
                hide rolfcutblood with dissolve
                pause 0.2
                hide rolfcutfrown with dissolve
                pause 0.2
                jump cutquest
            if step1correct == True:
                pause 0.2
                play sound "audio/soundFX/softget.wav"
                show rolfcut swab
                show rolfcutfrown behind rolfcut
                with dissolve
                with vpunch
                show rolfcuteye squintus
                show rolfcutfrown squint
                show rolfcut swab2
                with dissolve
                pause 1.5
                play sound "audio/soundFX/move.wav" volume 1.0
                show rolfcut clean
                with dissolve
                pause 0.1
                show rolfcutfrown usb
                show rolfcuteye usb
                with dissolve
                pause 0.3
                window show
                "It's looking a bit better now!!"
                window hide
                if step1correct == True:
                    $ step2correct = True

                    jump cutquest

                jump cutquest


        " {alpha=*0.87}Smack {size=-2}a {/size}{/alpha}{size=+6}{space=3}Bandaid{space=3}{/size}{alpha=*0.87}{size=-2} on {/size}him{/alpha}"if bandaidscold == False: #It slips off!" ref- Hey, no bandages 'til AFTER the contest!
            call disable_saving from _call_disable_saving_4
            if step2correct == True:
                pause 0.2
                play sound "audio/soundFX/move.wav" volume 1.0
                show bandaidhands
                with dissolve
                with vpunch
                pause 0.2
                show rolfcutfrown shut behind bandaidhands, rolfcuteyeblood
                with dissolve
                pause 1.0
                window show
                "That's pretty good placement, I think!"
                with hpunch
                ref "HEY!"
                ref "No bandaids or bandages are allowed during the fight! Take it off or Rolf's disqualified!"
                me "Okay, okay! I forgot!"
                window hide
                pause 0.2
                play sound "audio/soundFX/move.wav" volume 1.0
                hide bandaidhands
                with dissolve
                show rolfcutfrown shut
                with dissolve
                window show
                "Shit, That didn't do anything!!"
                window hide
                $ bandaidscold = True
                jump cutquest
            if step1correct == True:
                pause 0.2
                play sound "audio/soundFX/move.wav" volume 1.0
                show bandaidhands
                with dissolve
                with vpunch
                show rolfcutfrown usb behind bandaidhands
                show bandaidhandsblood2
                with dissolve
                pause 1.0
                window show
                "That's pretty good placement, I think!"
                window hide
                hide bandaidhands
                hide bandaidhandsblood
                hide bandaidhandsblood2
                play sound "audio/soundFX/FX6/bloodspurt.wav" volume 0.5
                show rolfcutspurt
                show rolfcuteye us
                show rolfcutfrown base behind rolfcut
                with dissolve
                with vpunch
                pause 0.1
                play sound "audio/soundFX/FX6/blooddrips.wav" volume 0.5
                hide rolfcutspurt
                show rolfcutblood

                with dissolve

                pause 0.4

                window show
                me "PHHFPT-! "
                window hide
                with hpunch
                hide rolfcutblood with dissolve
                pause 0.2
                window show
                ref "HEY!"
                ref "No bandaids or bandages are allowed during the fight! Take it off or Rolf's disqualified!"
                me "Okay, okay! I forgot!"
                window hide
                pause 0.2
                show rolfcuteye usb
                show rolfcutfrown usb
                with dissolve
                $ bandaidscold = True
                jump cutquest
            if step1correct == False:
                pause 0.2
                play sound "audio/soundFX/move.wav" volume 1.0
                show bandaidhands
                with dissolve
                with vpunch
                pause 0.2
                show rolfcutfrown shut behind bandaidhands, rolfcuteyeblood
                show rolfcuteyeblood shut behind bandaidhands
                with dissolve
                show bandaidhandsblood
                with dissolve
                pause 1.0
                window show
                "That's pretty good placement, I think!"
                with hpunch
                ref "HEY!"
                ref "No bandaids or bandages are allowed during the fight! Take it off or Rolf's disqualified!"
                me "Okay, okay! I forgot!"
                window hide
                pause 0.2
                play sound "audio/soundFX/move.wav" volume 1.0
                hide bandaidhands
                hide bandaidhandsblood
                with dissolve
                show rolfcutfrown shut
                with dissolve
                window show
                "Shit, That didn't do anything!!"
                window hide
                $ bandaidscold = True
                jump cutquest
            pause 0.2
            play sound "audio/soundFX/move.wav" volume 1.0
            show bandaidhands
            with dissolve
            with vpunch
            pause 0.2
            show rolfcuteye us
            show rolfcutfrown base
            with dissolve
            pause 1.0
            window show
            "That's pretty good placement, I think!"
            with hpunch
            ref "HEY!"
            ref "No bandaids or bandages are allowed during the fight! Take it off or Rolf's disqualified!"
            me "Okay, okay! I forgot!"
            window hide
            pause 0.2
            play sound "audio/soundFX/move.wav" volume 1.0
            hide bandaidhands
            with dissolve
            show rolfcuteye squintus
            show rolfcutfrown squint
            with dissolve
            window show
            $ bandaidscold = True
            jump cutquest

        #" Try losing \n( Remove before release of game. ) \njump aftercutloss":
            #jump aftercutloss

    "Something went wrong."
    "Ending game."
    return

label minigamecutcensor:

    scene rolfcutbase
    show blackshake at truecenter zorder -100
    show rolfcuteye shut
    show rolfcuteyeblood shut
    show blackshake at truecenter behind rolfcutbase
    #TIMER
    show censoreye zorder 100
    with vpunch
    pause 0.3
    play music "audio/MPP_-_Patch_Him_Up_Loop.mp3" fadein 0.0 volume 0.14
    window show
    "SHIT! "
    "I'll just... fiddle with my supplies and hope for the best!"
    window hide
    #-------------------------------------------------------------------------------------- FIRST
    play sound "audio/soundFX/softget.wav" volume 1.6
    show rolfcuttowel clean with dissolve
    pause 1.2
    show rolfcuttowel bloody with dissolve
    pause 0.9
    play sound "audio/soundFX/move2.wav"
    hide rolfcuttowel
    hide rolfcuteyeblood
    show rolfcut openn
    with dissolve
    pause 0.1
    play sound "audio/soundFX/FX6/bloodspurt.wav" volume 0.5
    show rolfcutspurt
    with dissolve
    with vpunch
    pause 0.1
    play sound "audio/soundFX/FX6/blooddrips.wav" volume 0.5
    show rolfcuteye us
    hide rolfcutspurt
    show rolfcutblood
    with dissolve
    pause 0.5
    window show
    "Something warm splashed onto me!!"
    window hide
    pause 0.5
    show rolfcutfrown base behind rolfcut
    with dissolve

    pause 0.4

    play sound "audio/soundFX/move.wav" volume 1.0
    show bandaidhandz with dissolve
    window show

    "I feel something squishy!"
    window hide
    hide rolfcutblood with dissolve

    pause 0.2
    show rolfcuteye usb
    show rolfcutfrown usb
    with dissolve
    pause 0.2

    #-------------------------------------------------------------------------------------- SECOND
    pause 0.2
    play sound "audio/soundFX/softget.wav"
    show rolfcut swab
    show rolfcutfrown behind rolfcut
    hide bandaidhandz
    with dissolve
    with vpunch
    show rolfcuteye squintus
    show rolfcutfrown squint
    show rolfcut swab2
    with dissolve
    pause 0.5
    play sound "audio/soundFX/move.wav" volume 1.0
    show rolfcut clean
    with dissolve
    pause 0.1
    show rolfcutfrown usb
    show rolfcuteye usb
    with dissolve
    pause 0.3
    window show
    "I think it's working!"
    window hide
    #-------------------------------------------------------------------------------------- THIRD
    pause 0.2
    play sound "audio/soundFX/FX6/167075__drminky__slime-land.wav" volume 1.0
    show rolfcuthand two
    with dissolve
    with vpunch
    pause 0.3
    show rolfcuteye us
    show rolfcutfrown base
    with dissolve
    pause 0.3
    window show
    "Gleh! My fingers are covered in gunk!"
    window hide

    play sound "audio/soundFX/FX6/167073__drminky__squelchy-squirt.wav" volume 1.0
    show rolfcuthand one
    show rolfcut goo
    with dissolve

    # You win! You can't run out of time if you've clicked this this far. Timer fades.

    pause 0.8
    hide rolfcuthand with dissolve
    show rolfcut goob with dissolve

    pause 0.2

    hide rolfcutblood
    with dissolve
    pause 0.2
    stop music fadeout 3.0
    #--------------------------------------------------------------------------------------IfCensorWinState
label aftercutminigamewinbutcensored:
    #Ilves rubs eyes open
    #play music "audio/MPP_-_Brewing_Tension_Pre-Fight_VERSE.mp3" fadein 1.0 volume 0.4
    queue music "audio/Seagul.wav" loop fadein 5.0 volume 0.25
    window show
    me "That... might be it!"
    "I slowly open my eyes-"
    window hide
    hide censoreye with dissolve
    pause 0.4
    window show
    me " Whew, that's looking pretty good!"
    show rolfcuteye usb
    hide rolfcutfrown
    with dissolve
    rolf "... Can't believe you got that done without looking!"
    me "Me neither... Must've gotten lucky!"
    hide rolfcuteye
    with dissolve
    rolf "I'm ready to fight!"
    ref "Good! "
    ref "Now get out of the Pit before the round starts, [Protagonist]!"

    jump endfightafterminigame

#    jump aftercutloss

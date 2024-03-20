label aftercutloss:
    call disable_minigame_mode from _call_disable_minigame_mode
    call enable_saving from _call_enable_saving
    window hide
    stop music fadeout 0.2
    play sound "audio/soundFX/FX6/singlebell.wav" volume 0.6
    scene dong2
    show blackshake at truecenter zorder -100
    with hpunch

    window show
    ref "Round two!"
    show dong1 with dissolve
    "Shit! I'm not done yet!"
    ref "FIIIIIGH-"
    #With record scratch
    window hide
    play music "audio/Seagul.wav" loop fadein 5.0 volume 0.35
    scene bg pits
    show blackshake at truecenter zorder -100
    show bgpits people
    show rounds two
    show goatbg base
    with fade
    pause 0.1
    show goatbg base2
    with dissolve
    hide goatbg
    with dissolve
    show goat handout at center:
        xalign 0.47 yalign 4.5 zoom 0.83
    with dissolve
    with vpunch
    window show
    ref "W-Wait, STOP!"


    pause 0.2
    show goat handup
    show goatf think at center:
        xalign 0.47 yalign 4.5 zoom 0.83
    show goateye right at center:
        xalign 0.47 yalign 4.5 zoom 0.83
    with dissolve
    ref "Rolf... Come to the center."
    window hide

    show goat handright with dissolve
    play sound "audio/soundFX/run2r.wav" volume 1.0
    show rolfn base at right behind goat:
        zoom 0.85 yalign 1.0 xalign 1.3
    show rol blood2 at right behind goat:
        zoom 0.85 yalign 1.0 xalign 1.3

    with easeinright


    window show
    rolf "What? Start the round already!"
    show goat think
    hide goateye
    with dissolve
    ref "First-"
    ref "I need you to answer my following question..."
    show goat handup2
    show goateye right at center:
        xalign 0.47 yalign 4.5 zoom 0.83
    with dissolve
    ref "How many fingers am I holding up?"
    show rol blood with dissolve
    rolf "..."
    show rolfn knuckles
    with dissolve
    with hpunch
    rolf "Thrfeour!"
    window hide
    show goat handdown
    show goatf nod
    hide goateye
    with dissolve
    pause 0.3
    window show

    ref "...The answer's two... "
    show goatf sad1
    show goateye right at center:
        xalign 0.47 yalign 4.5 zoom 0.83
    with dissolve
    ref "Sorry, Rolf. "
    show rolfn base
    show rol blood2
    with dissolve
    rolf "Shit..."
    window hide
    pause 0.1
    play sound "audio/soundFX/move.wav"
    show goat timeout
    hide goatf
    hide goateye
    with dissolve
    with hpunch

    pause 0.3
    window show
    ref "The fight's over!"
    ref "Alfred wins via TKO due to Rolf's eyesight being compromised."
    "The crowd groans with disappointment and anger."
    window hide
    show crowdbronbase
    show crowdbronn rage
    show crowdbron fistdown
    if modest == True:
        show crowdemesuit
    else:
        show crowdemelon
    show crowdbouth grr
    show crowdem pout
    hide crowdbronn rage
    show crowdbron fistup
    show crowdb rage
    show crowdem pout

    with fade
    pause 0.2
    window show
    bron "But the cut was from an eye poke!"
    window hide
    hide crowdbronn rage
    hide crowdbron fistup
    hide crowdb rage
    hide crowdemlookbron
    hide crowdem pout
    hide crowdbronbase
    hide crowdbronn rage
    hide crowdbron fistdown
    hide crowdemesuit
    hide crowdemelon
    hide crowdbouth grr
    hide crowdem pout
    hide crowdbronn rage
    with fade
    pause 0.3
    show goat handdown
    show goatf crowd2  at center:
        xalign 0.47 yalign 4.5 zoom 0.83
    with dissolve
    window show
    ref "Attempted eye poke, maybe. But nothing actually touched his eye. "
    show goatf nodz with dissolve
    ref "My call is final."
    ref "I can't let my own feelings affect the ruling."
    "Frank steps back with disappointment across his face."
    window hide
    hide goatf
    hide goat
    with dissolve
    show goatbg base2z with dissolve
    pause 0.3
    show goatbg base2zx with dissolve
    play sound "audio/soundFX/FX6/triplebell.wav"  volume 0.3 fadeout 0.6
    pause 1.1
    show goatbg base2z with dissolve
    pause 0.3
    window show
    "Frank rings the bell thrice, signaling the end of the fight."
    pause 0.3
    me "I'm sorry for messing up, Rolf..."
    "Rolf grumbles to himself."
    rolf "{alpha=*0.90}{size=-3}Fuckin' hell... I shouldn't have let that hit me..."
    #show bron
    #bron " Let's go find some water to rinse that eye, dad..."
    #Ilves shows up
    window hide
    pause 0.1
    show ilvescrowdbase
    show ilvescrowdrub
    with fade
    pause 0.3
    window show
    "Ilves rubs his eyes-"
    window hide
    play sound "audio/soundFX/move2.wav"
    hide ilvescrowdrub
    with dissolve
    pause 0.3

    show ilvescrowd normalb
    with dissolve
    window show
    cat "Uh-"
    window hide
    with hpunch
    show ilvcrowdohno with dissolve
    pause 0.3
    window show
    cat "Oh no!"
    cat "Rolf lost..."
    window hide
    hide ilvescrowdbase
    hide ilvescrowd normalb
    hide ilvcrowdohno
    with fade
    pause 0.3
    play sound "audio/soundFX/runn.wav"
    show ilv draw3b at right:
        yalign -18.0 xalign 0.35 zoom 0.83
    show ilvf sadrolf at right:
        yalign -18.0 xalign 0.35 zoom 0.83
    with easeinright
    pause 0.3
    window show
    cat "Thanks for stepping up for me, soldier..."
    show ilvf sadus
    hide ilv
    with dissolve
    cat "... But seems I'll be going back home with a bad memory from this journey." #Sad art
    show ilv sad at right:
        yalign -18.0 xalign 0.35 zoom 0.83
    hide ilvf
    with dissolve
    play sound "audio/soundFX/Get.mp3"
    with vpunch
    "Ilves hands me the paper in his hand."
    window hide
    show blackopacity with dissolve
    play sound "audio/soundFX/FX3/postit.wav" volume 0.5
    show hoghaven3tex
    with dissolve
    pause 1.5
    window show
    "Oh no..."
    "My heart breaks when I see Ilves' art."
    me "... That's so sad."
    "He finished it off with a traumatic depiction of himself being poked in the eyes."
    window hide
    pause 0.2
    hide hoghaven3tex with dissolve
    hide blackopacity with dissolve

    play sound "audio/soundFX/run2r.wav" volume 0.7
    pause 0.3
    show bullb base at left behind ilv:
        yalign 0.6 xalign -0.25 zoom 0.80
    show bullf darklaugh at left behind ilv:
        yalign 0.6 xalign -0.25 zoom 0.80
    with easeinleft
    with vpunch
    pause 0.3
    window show
    bull "KHAHAHA!"
    show bullf dark2
    show bullb hips
    show bulleye right4 at left behind ilv:
        yalign 0.6 xalign -0.25 zoom 0.80
    with dissolve
    bull "Who's the best?! "
    hide bulleye with dissolve
    show bullf dark3
    show bullb iwin
    with dissolve
    with hpunch
    bull "{size=+5}ME!"
    window hide
    play sound "audio/soundFX/runn.wav" volume 0.7
    show vulture spookup at left:
        yalign 0.6 xalign -0.23 zoom 0.80
    with easeinleft
    pause 0.2
    show bullb crack
    show bullf rageglenn
    with dissolve
    with vpunch
    window show
    bull "Drinks are on YOU tonight, Glenn!"
    show vulture scryy with dissolve
    glenn "!!?"
    pause 0.2
    "{cps=*0.1}...{/cps}"
    pause 0.2
    "I really messed things up for everyone."
    window hide
    pause 0.5
    #Retry minigame
    stop music fadeout 2.0
    scene black with fade
    show blackshake at truecenter zorder -100

    pause 0.2
    show endscreen with dissolve
    window show
    "I don't think I'll ever emotionally recover from this."
    stop music fadeout 1.0
    pause 0.3

label beeforemin:

    menu:
        with dissolve

        "{u}{color=#E20018}{b}{cps=*0.1}END.{/color}{/b}{/u}{/cps}"


        "Try patching Rolf up again!":
            pause 0.5
            $ renpy.block_rollback()
            window hide
            scene rolfcutbase
            show blackshake at truecenter zorder -100
            show rolfcuteye shut
            show rolfcuteyeblood shut
            show blackshake at truecenter behind rolfcutbase
            with fade
            play sound "audio/soundFX/FX2/pig-grunt-5-deep-96khz.wav" volume 0.3
            with vpunch
            pause 0.9
            window show
            ref "Hey, [Protagonist]!"
            me "Y-Yeah!?"
            ref"What are you waiting for?! That cut is in a TERRIBLE spot!"
            ref "If Rolf can't see when the bell clangs, the fight's up! "
            #scene ilvescrowdbase
            #show ilvescrowdrub
            #with fade
            #cat " Oh no, Rolf's hurt?"
            #"Ilves starts rubbing his eyes again-"
            #scene goatclosebase with fade
            ref "You've got ONE MINUTE!"

            jump minigamecut





label aftercutminigamewin:
    call disable_minigame_mode from _call_disable_minigame_mode_1
    $ win_cutgame()

    #Ilves rubs eyes open
    $ banish_timer()
    call enable_saving from _call_enable_saving_1
    stop music fadeout 2.5
    pause 0.5
    window show
    me "I... Think I got it under control!"
    play music "audio/Seagul.wav" loop fadein 5.0 volume 0.25
    show rolfcuteye usb
    hide rolfcutfrown
    with dissolve



    if cutspveryslow == True:
        rolf "'You trying to give me a heart attack while you're at it?!"
        rolf "That was WAY too close!"
        me "You can't rush a masterpiece!"

    if cutspslow == True:
        rolf "Phew... That got pretty close!"
        me "I had it under control!"


    if cutspmedium == True:
        rolf "...Not bad."



    if cutspfast == True:
        with vpunch
        rolf "Already?! You're pretty quick!"
        if perfscore == True:
            me "I am! And I'm a damn good assistant, too!"
            rolf "...Don't get cocky."
        else:
            me "'Guess I'm a natural!"
            rolf "...Don't get cocky."

    if cutspveryfast == True:
        with vpunch
        rolf "What the he-"
        rolf "What are you? The fastest damn cutman in the world?!"
        if perfscore == True:
            me "Yeah! AND the best assistant!!!"
            rolf "...You're getting cocky."
        else:
            me "'Guess I'm a natural!"
            rolf "...Don't get cocky."


    hide rolfcuteye
    with dissolve
    rolf "I'm ready!"
    ref "Good! "
    ref "Now get out of the pit before the round starts, [Protagonist]!"

label endfightafterminigame: #It jumps you here even if you censor blood.
    window hide
    pause 0.3
    scene ilvescrowdbase
    show blackshake at truecenter zorder -100
    show ilvescrowdrub
    with fade
    pause 0.3
    window show
    "Ilves rubs his eyes-"
    window hide
    play sound "audio/soundFX/move2.wav"
    hide ilvescrowdrub
    with dissolve
    pause 0.3
    show ilvescrowd normalb
    with dissolve
    window show
    cat "Uh-"
    with hpunch
    show ilvescrowd glad with dissolve
    cat "My vision's back!"
    cat "[Protagonist] must've done a good job, I barely see any blood!"
    cat "Fight well, comrade!"
    window hide
    scene eyeconfront1
    show blackshake at truecenter zorder -100
    show eyeconfront2b
    show eyeconfrontcut one
    with fade
    pause 0.3
    show eyeconfront2 behind eyeconfront2b with dissolve
    window show
    bull "Hnf-"

    rolf "You got any other tricks up your sleeve? "
    window hide
    show eyeconfront1b behind eyeconfrontcut
    show eyeconfrontcut two
    with dissolve
    pause 0.4
    window show
    rolf "'Cus I won't fall for that one again! "
    window hide
    scene dong1 with fade
    stop music fadeout 0.3
    play sound "audio/soundFX/FX6/singlebell.wav" volume 0.6
    show dong2 with hpunch



    show blackshake at truecenter zorder -100
    pause 0.3
    window show
    ref "Round two!"
    window hide
    scene dong1 with dissolve
    pause 0.3
    scene black with fade
    show blackshake at truecenter zorder -100
    show fightgallery1 behind black
    show fightgallery2 behind black
    show fightgallery3 behind black
    window show

    ref "FIIIGHT!"
    #Stepruns
    window hide
    play sound "audio/soundFX/FX6/bullstomp.mp3" volume 0.8
    stop music fadeout 0.3
    scene hornsfight with fade
    show blackshake at truecenter zorder -100
    with vpunch
    pause 0.9
    window show
    bull "How about THIS?!"
    "Alfred leans forward and charges straight at Rolf with his horns!!"
    window hide
    with vpunch
    scene hornsfight at truecenter:
        linear 0.1 zoom 1.07 yalign 1.00
    show blackshake at truecenter zorder -100
    pause 0.15

    scene goatclosebase:
        zoom 1.05 yalign 1.0 xalign 0.1
    show blackshake at truecenter zorder -100
    show goatfing point:
        zoom 1.05 yalign 1.0 xalign 0.1
    show goatexpress yell:
        zoom 1.05 yalign 1.0 xalign 0.1
    with fade
    play sound "audio/soundFX/FX6/goatscream.wav" volume 0.6
    with hpunch
    pause 0.3
    window show
    ref "S-STOP!"
    ref "HORNS ARE AGAINST THE RULES!"
    window hide

    scene tooeasy with fade
    show blackshake at truecenter zorder -100
    #play sound "audio/soundFX/FX2/pig-grunt-5-deep-96khz.wav" volume 0.3
    pause 0.3
    window show
    rolf "Predictable!"
    window hide
    scene tripbull
    show blackshake at truecenter zorder -100
    show tripbullspeed
    with fade
    play sound "audio/soundFX/FX6/trip.wav" volume 0.6


    with hpunch
    pause 0.3
    hide tripbullspeed with dissolve
    pause 0.4
    window show
    "!!"
    "Rolf slides to the side and trips him!"
    bull "U-UGhaa!-"
    "The bull falls head first-"
    window hide
    scene stuckground with fade
    show blackshake at truecenter zorder -100
    play sound "audio/soundFX/FX6/stuckk.wav" volume 0.6
    with vpunch
    pause 0.3
    window show
    "Right onto his horns!"
    bull "U-Uhh-"
    window hide
    scene ilvescrowdbase
    show blackshake at truecenter zorder -100
    show ilvescrowd scream
    with fade
#    play sound "audio/soundFX/FX6/415209__inspectorj__cat-screaming-a.wav" volume 0.6
    pause 0.3
    window show
    cat "GET HIM!"
    window hide
    scene stuckground with fade
    show blackshake at truecenter zorder -100
    play sound "audio/soundFX/run2r.wav" volume 0.3 fadeout 2.0
    pause 0.3
    show stuckgroundrolf with easeinleft
    pause 0.3
    window show
    rolf "Oh, I will."
    show stuckground2 behind stuckgroundrolf with dissolve
    with hpunch
    bull "W-Wait-"
    bull "Don't! "
    bull "Punching someone who's stuck isn't fair!"
    rolf "HAH! Well, isn't that perfect? "
    rolf "You hate fighting fair!"
    window hide
    play sound "audio/soundFX/move.wav" volume 0.3
    show stuckgroundfist with easeinbottom
    pause 0.3
    window show
    rolf "Now watch and learn, kid."
    rolf "Here's how you throw a punch with proper form!"
    window hide
    pause 0.2
    scene black with fade
    show blackshake at truecenter zorder -100
    #with vpunch
    play sound "audio/soundFX/FX6/bigpunch.wav" volume 0.75
    pause 0.1
    show blackshake at truecenter zorder -100
    scene headhitbase
    show blackshake at truecenter zorder -100
    show blackshake at truecenter zorder -100
    with vpunch
    show blackshake at truecenter zorder -100
    pause 0.5
    window show
    "SMACK!"
    "Rolf hits him square in the face!"
    bull "DHAA-!"
    window hide
    play sound "audio/soundFX/FX6/bouldercrunch3.mp3" volume 0.9
    scene headhitz1 with dissolve
    show blackshake at truecenter zorder -100
    with hpunch
    pause 0.3
    window show
    bull "AAAAGH-!"
    "The punch sends him flying, ripping through the ground and bouncing him off the edge of the arena!"
    window hide
    pause 0.2
    scene headhitz2 with dissolve
    show blackshake at truecenter zorder -100
    window show
    bull  " {alpha=*0.80}{size=-4}Aaa{size=-5}aa{size=-6}aaa{size=-7}aaaa{size=-8}aaaaa-"
    window hide
    pause 0.2
    play sound "audio/soundFX/FX6/pling.wav"
    show headhitzstar with dissolve
    pause 0.5
    window show

    ref "Woaaah!"
    window hide
    show headhitz3 behind headhitzstar with dissolve
    hide headhitzstar with dissolve
    pause 0.2
    window show
    ref "..."
    window hide
    stop music fadeout 0.5
    play sound "audio/soundFX/FX2/dat-s-right.wav"
    show headhitz3b with dissolve

    pause 0.5
    window show

    ref "Rolf wins! "
    window hide
    scene black with fade
    show blackshake at truecenter zorder -100
    play sound "audio/soundFX/FX6/triplebell.wav"  volume 0.5 fadeout 0.4


    pause 1.8
label rolfwins:
    play music "audio/beachfundrums.mp3"  fadein 4.0 volume 0.15
    play sound "audio/soundFX/Crowd/donnacheer2.wav"  volume 0.25 fadein 1.8

    # DING DING DING
    #pause 0.6

    scene crowdbronbase
    show blackshake at truecenter zorder -100
    if modest == True:
        show crowdemesuit
    else:
        show crowdemelon
    show crowdem smile
    show crowdbron fistup
    show crowdb win
    with fade
    with vpunch
    pause 0.3
    window show
    bron "FUCK YEAH, DAD!"
    bron "'Shut him up good! "
    emelie "P-Pheeew!"#tense"
    show crowdemlookbron with dissolve
    emelie "I hate confrontations and violence..."#worry"
    show crowdem happy
    hide crowdemlookbron
    with dissolve
    emelie "But I'm also kinda relieved that bully got whacked!"#happy
    show crowdbron fistdown
    show crowdb proud
    with dissolve
    bron "Mhm!"
    "Bronwen looks proud."#and looks to emelie
    #Ilves has his eyes open and starry.
    window hide
    scene ilvescrowdbase
    show blackshake at truecenter zorder -100
    show ilvescrowd smile
    with fade
    pause 0.3
    window show
    cat "Great work, fellow soldier." # :D
    window hide
    scene bg pitsb
    show blackshake at truecenter zorder -100
    show goatbg base2
    show bgpits people
    show rounds two
    show rolfn pantz at right:
        zoom 0.85 yalign 1.2 xalign 1.2

    show rol zen at right:
        zoom 0.85 yalign 1.2 xalign 1.2
    with fade
    pause 0.2
    hide goatbg base2 with dissolve
    pause 0.2
    show goat handdown at center:
        xalign 0.15 yalign 4.5 zoom 0.83
    show goateye right at center:
        xalign 0.15 yalign 4.5 zoom 0.83
    with dissolve



    #Rolf feels bad about Ilves having such a horrible eye-poke situation, so he invites him into the city. he can stay!
    #They drink later and Rolf talks about how back in the war the pigs managed to push the wolves back, and the wolves fled to the north thinking they'd be safe, but that's when they met resistance from the northern allies!
    #Wolves are of course much larger than lynxes, but lynxes are very crafty and know their lands very well. And even if theyre small, their claws and paws are big!
    #This means he can show up to the bachelor party later and maybe do some sneaky favor.
    show rol hapifrank at right:
        zoom 0.85 yalign 1.2 xalign 1.2
    show roleye downhap at right:
        zoom 0.85 yalign 1.2 xalign 1.2
    with dissolve
    show goatf hapiilves behind goateye at center:
        xalign 0.15 yalign 4.5 zoom 0.83
    show goateye right at center:
        xalign 0.15 yalign 4.5 zoom 0.83
    with dissolve
    window show
    ref "Good job, Rolf. "
    show goat think with dissolve
    ref "'Knew you had this in the bag."
    #show rolfn base
    show rol surprise2 behind roleye
    with dissolve
    rolf "Thanks for the opportunity, Frank."
    show goat handdown
    show goatf nod at center:
        xalign 0.15 yalign 4.5 zoom 0.83
    hide goateye
    with dissolve
    "Frank nods respectfully and steps back again."
    stop music fadeout 2.5
    queue music "audio/Seagul.wav" loop fadein 5.0 volume 0.25
    window hide
    hide goat
    hide goatf
    hide goateye
    with dissolve
    hide rol
    hide roleye
    show rolfn pantz
    with dissolve
    show goatbg base2 behind rolfn
    with dissolve

    show rolfn pantz at right:
        zoom 0.85 yalign 1.2 xalign 1.2
        linear 0.6 xalign 0.6
    pause 0.6
    show rolfn pantz at right:
        yalign 1.2 xalign 0.6
    window show

    rolf "..."
    "Rolf turns to face me."
    show rol closed at right:
        zoom 0.85 yalign 1.2 xalign 0.6
    show rolfn base
    with dissolve

    rolf "So, [Protagonist]..."
    if liename == True:

        "He used my real name?!"

    me "Yeah?"
    show rol sidewary3
    show rolfn base
    with dissolve
    rolf "... Let's play a quick game of Rock, Paper, Scissors..."
    #Sure! or "now,really?"
    me "Now? Really?"
    show rolfn knuckles
    show rol concern
    with dissolve
    rolf "Y-Yes. Come on, now."
    "I won't deny him a simple game of Rock, Paper, Scissors after what he just pulled off..."
    me "Sure, sure."
    show rolfn fist
    hide rol
    with dissolve
    "He holds his fist out and approaches me."
    window hide
    show rolfn fist at right:

        linear 1.1 zoom 1.2 yalign 0.2 xalign 0.6
    play sound "audio/soundFX/Step1.wav" volume 0.0
    pause 1.1

    scene shakebg with fade
    show blackshake at truecenter zorder -100
    show rpsrolf rock:
        xpos 70
    with easeinright
    show rpsprotag rock:
        xpos -0
    with easeinleft
    pause 0.5
    window show

    #RPS
    "We move our fists to the middle. "
    rolf "Remember how... a warrior opens?"
    if RPS == "paper":
        me "'Sure do! I opened with it, remember?"
        rolf "Yeah, yeah. Show me. "
    if RPS == "rock":
        me "'You playing mind games to win with paper again?"
        rolf "No. But I hear you do remember!"
        me "Yeah."
        rolf "... Show me."
    if RPS == "scissors ":
        me "'Sure do! Paper."
        me "I beat you when you last opened with it, remember?"
        rolf "Yeah, yeah... Don't get cocky."
        rolf "Show me."


    show rpsprotag paper
    with dissolve

    "I open my hand and show him \" Paper\". "

    me "There it is!"
    stop music fadeout 2.0
    rolf "..."
    show rpsrolf paper with dissolve
    "Rolf matches my move and-"
    #Handshake!
    #Music!"
    window hide
    play sound "audio/soundFX/Get.mp3"


    hide rpsrolf
    hide rpsprotag
    show shakehands:
        ypos 1 xpos -333
    with dissolve
    play music "audio/trailsshort2.mp3" volume 0.4 noloop
    with vpunch
    pause 0.3
    show shakehands:
        ypos 1 xpos -333
        linear 2.5 ypos 0 xpos 0
    pause 2.6
    window show
    "Grips my hand!"
    window hide
    show shakehands:
        yoffset 0
        linear 0.3 yoffset -40
        yoffset -40
        linear 0.2 yoffset 00
        yoffset 0
        pause 0.3
        yoffset 0
        linear 0.2 yoffset -10
        yoffset -10
        linear 0.3 yoffset 00
        yoffset 0
        pause 0.3
    pause 2.0
    window show
    "His big hand shakes mine firmly."

    #Shakeshake"
    #face shot of rolf looking away and then to the center
    window hide
    scene interroshakebase
    show blackshake at truecenter zorder -100
    show shakebgss behind interroshakebase
    show interroshake sidesad
    with fade
    pause 0.3
    window show
    rolf "..."
    window hide
    hide shakebgss
    hide interroshake
    with dissolve
    pause 0.5
    window show
    play sound "audio/soundFX/FX6/thankyougrunt.wav" volume 0.6
    rolf "Thank you."# silent text
    window hide
    #choice ' Anytime! ' ' Happy to help. That bully deserved a beating.'
    pause 0.5
    play sound "audio/soundFX/move2.wav" volume 0.6
    pause 0.2
    window show
    "He lets go of my hand and steps back."
    window hide
    hide interroshakebase
    scene bg pitsb
    show blackshake at truecenter zorder -100
    show bgpits people
    show goatbg base2
    show ilv draw1c at right:
        yalign -18.0 xalign 0.35 zoom 0.83
    show ilveye thank at right:
        yalign -18.0 xalign 0.35 zoom 0.83


    show rolfn base at right:
        zoom 1.2 yalign 0.2 xalign 1.70


    hide bgpits
    hide goatbg
    show rounds two behind ilv
    with fade
    pause 0.2
    show rolfn base at right:
        linear 1.5 zoom 0.9 yalign 1.0 xalign 1.55
    pause 1.5
    #play sound "audio/soundFX/Step1.wav"
    show rolfn base at right:
        zoom 0.9 yalign 1.0 xalign 1.55
    show rol belly at right:
        zoom 0.9 yalign 1.0 xalign 1.55
    with dissolve
    pause 0.3
    window show
    #back to convo shot-ilves is now holding his paper and is drawing
    #Everyone shows up
    play music "audio/beachlong2.mp3" noloop fadein 2.5 volume 0.2
    queue music "audio/Tavern+Brawl+-+320bit.mp3" loop fadein 1.5 volume 0.25
    cat "Wooow! "
    cat "What a great memory!"
    window hide
    show ilv draw3
    show ilvf thank behind ilveye at right:
        yalign -18.0 xalign 0.35 zoom 0.83
    show ilveye downsquint at right:
        yalign -18.0 xalign 0.35 zoom 0.83
    with dissolve
    play sound "audio/soundFX/runn.wav" volume 0.6
    show bronsw base behind ilv at left:
        yalign 3.7 xalign -5.6
        zoom 0.87
    with easeinright
    show bron smile2 behind ilv at left:
        yalign 3.7 xalign -5.6
        zoom 0.87
    show broneye lookright behind ilv at left:
        yalign 3.7 xalign -5.6
        zoom 0.87
    with dissolve
    pause 0.3

    window show
    bron "Got him good, dad! "
    show rolfn knuckles
    show roleye looksidehapi2 at right:
        zoom 0.9 yalign 1.0 xalign 1.55
    with dissolve
    rolf "He deserved it."
    show rol think
    hide roleye
    with dissolve
    rolf "Felt a bit rusty, though... Ugh."
    hide broneye
    show bron laugh
    show bronsw hips
    with dissolve
    bron "That's the price you pay for living in peaceful times!"
    show rolfn base
    show rol close
    show roleye looksidehapi2 at right:
        zoom 0.9 yalign 1.0 xalign 1.55

    with dissolve
    rolf "True... It is a good thing."
    show bronsw knuckles
    show bron laugh2
    with dissolve
    bron "But y'know what makes victory taste even sweeter?"
    show rolfn pant
    show rol pout
    show roleye lookside at right:
        zoom 0.9 yalign 1.0 xalign 1.55
    with dissolve
    rolf "A beer."
    show bron biggersmileright
    hide broneye
    show bronsw hips
    with dissolve
    bron "Yes! Let's grab a pint! It's damn sweaty."
    show rol surprisen
    with dissolve
    rolf "Aye!"
    "Rolf looks happy."
    show bron biggersmilerightilves
    show bronsw base
    with dissolve

    bron "'You following along, lil guy? "
    show ilveye upz at right:
        yalign -18.0 xalign 0.35 zoom 0.83
    with dissolve
    cat "?"
    bron "'Got some time before your next match."
    show rol hapifrank
    hide roleye
    show rolfn base
    show ilveye upz2
    with dissolve
    rolf "Drinks at the beach bar are on me!"
    show ilv draw4b
    hide ilveye
    show ilvf lookrolf at right:
        yalign -18.0 xalign 0.35 zoom 0.83
    with dissolve
    cat "Whaaa, yes!"
    hide ilvf lookrolf
    with dissolve
    cat "I'll be right with you in a second!"
    show bronsw think
    show bron think
    hide broneye
    with dissolve
    "Bronwen smiles my way."
    show bronsw think
    show bron pull
    hide broneye
    with dissolve
    bron "You're welcome to tag along, too, [Protagonist]. "
    bron "Though I'm sure Emelie will need your attention first!"
    me "Yes! I'll catch up with ya later!"
    #show rol closed
    #rolf " Keep her safe!"
    show bronsw base
    show bron smile
    with dissolve
    "Bronwen nods and walks out of the arena with Rolf."
    window hide

    show ilv draw4c  at right:
        yalign -18.0 xalign 0.35 zoom 0.83
    show ilv draw3
    show ilvf thank at right:
        yalign -18.0 xalign 0.35 zoom 0.83
    with dissolve
    hide rol
    with dissolve
    play sound "audio/soundFX/run2r.wav" volume 0.7
    hide rolfn
    hide rol
    hide roleye
    with easeoutright
    play audio  "audio/soundFX/runn.wav" volume 0.7
    hide bronsw
    hide bron
    with easeoutright
    pause 0.5

    show ilvf thank2 at right:
        yalign -18.0 xalign 0.35 zoom 0.83
    with dissolve
    window show
    cat "[Protagonist]... "
    me "Hm?"
    show ilvf thank at right:
        yalign -18.0 xalign 0.35 zoom 0.83
    with dissolve
    cat "I want to thank you for stepping up back there."
    show ilv base with dissolve
    play sound "audio/soundFX/Get.mp3"
    with vpunch
    "He hands me the paper. "
    hide ilvf
    show ilv bigsmile
    show ilveye thank2 at right:
        yalign -18.0 xalign 0.35 zoom 0.83
    with dissolve
    cat "And for giving me a great memory to show the kittens back home!"
    window hide
    show blackopacity with dissolve
    play sound "audio/soundFX/FX3/postit.wav" volume 0.5
    show hoghaven2tex
    with dissolve


    pause 1.6
    window show
    #"Handshake artYou finished the piece off with me and Rolf shaking hands!"
    "Woah!"
    me "You finished the piece off with me and Rolf shaking hands!"
    me "It really came together great! "
    cat "I'm glad you like it!"
    cat "I painted Rolf first, then just couldn't seem to fit that handsome face of yours into frame... "
    cat "Sorry!"
    me "It's okay!"
    "I think I'll have to get used to that... "
    "People around these parts probably don't have much experience with drawing humans."
    cat "Seeing the two of you step up to help me with a common foe was just beautiful. "
    cat "And it resulted in an unlikely friendship! "
    window hide

    hide hoghaven2tex
    hide blackopacity
    with dissolve
    pause 0.3
    show ilv draw4
    hide ilveye
    show ilvf thank at right:
        yalign -18.0 xalign 0.35 zoom 0.83
    with dissolve
    pause 0.5
    window show
    me "I'm not sure if I'd go so far as to call it a \" friendship \" just yet- "
    me "But I'm happy we could boost your spirit and get you that deserved win!"
    hide ilvf
    show ilv basehips
    with dissolve
    #I give him the drawing back "
    cat "I've still got some matches left in the tournament... But I don't really care about winning or losing anymore. "
    show ilv bigsmile
    show ilvouth smile2 at right:
        yalign -18.0 xalign 0.35 zoom 0.83
    with dissolve
    cat "Because I feel like I've gotten new friends!"
    show ilv second
    hide ilvouth
    with dissolve
    cat "Speaking of which- "
    cat "I've gotta catch up with the big hogs!"#!
    show ilv basehips with dissolve
    cat "'Hope we'll meet each other again in the future, [Protagonist] ! "
    me "I hope so, too!"
    show ilv grin with dissolve
    cat "This lynx owes you a favor!"
    window hide
    play sound "audio/soundFX/run2.wav" volume 0.7
    hide ilv with easeoutright
    pause 0.3
    window show
    "Ilves runs off."
    window hide
    play sound "audio/soundFX/runn.wav" volume 0.7
    show emeswim normal at right:
        #zoom 0.9 yalign -0.20 xalign 0.85
        zoom 1.0 yalign 0.06 xalign  0.9
    with easeinright
    pause 0.4
    show emeswim normal at right:
        zoom 1.0 yalign 0.06 xalign  0.9
        linear 0.7 zoom 1.15 yalign 0.06 xalign 0.8
    pause 0.7
    show emeswim at right:
        zoom 1.15 yalign 0.06 xalign 0.8
    show emeswim out
    show emf surprise2 at right:
        zoom 1.15 yalign 0.06 xalign 0.8
    show emear high at right:
        zoom 1.15 yalign 0.06 xalign 0.8
    with dissolve
    pause 0.4
    window show
    emelie "Pheew, that was tense!!"
    show emf wide with dissolve

    emelie "My legs got so shaky I couldn't stand up until just now! "
    show emf insecure at right:
        zoom 1.15 yalign 0.06 xalign 0.8
    show emeye side2 at right:
        zoom 1.15 yalign 0.06 xalign 0.8
    hide emear
    with dissolve
    emelie "I hate violence and confrontations like that!"
    #emelie " I could use a hug."
#    "We hug "
    show emf decided
    hide emeye
    with dissolve
    emelie "Rolf and Bronwen have the right idea...  "
    show emf decided2
    show emeswim hips
    hide emear
    show emear high at right:
        zoom 1.15 yalign 0.06 xalign 0.8
    with dissolve
    emelie "We could use a drink too after all that, don't you think? "
    me "Absolutely... I need something to wash that stress away! "
    show emf smile
    hide emear
    show emeswim normal
    with dissolve
    emelie "Then let's get going!"
    window hide
    scene black with fade
    show blackshake at truecenter zorder -100
    pause 0.3
    window show
    "Me and Emelie leave the Pig Pit and head for the beach bar. "


    jump drinks

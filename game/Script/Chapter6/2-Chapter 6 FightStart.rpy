label fightstart:

    window show
    ref "FIIIIIGHT!"
    window hide

    play sound "audio/soundFX/FX6/bullstomp.mp3" volume 0.8
    pause 0.3
    #play music "audio/MPP_-_Fight_Loopround.mp3" fadein 0.0 volume 0.4
    stop music fadeout 0.3
    pause 0.4
    scene tripfightbase1 with dissolve
    show blackshake at truecenter zorder -100


    pause 0.6
    window show

    "The large bull charges Rolf with his fist ready to strike!"
    bull "Take THIS!"
    #swooshswoosh
    window hide
    pause 0.2
    play sound "audio/soundFX/FX6/hitmiss.mp3" volume 1.0
    show tripfightbase2 with dissolve
    pause 0.9
    window show
    "But it wooshes right past Rolf's face!"
    rolf "Hah! Terrible uppercut form, and too slow!"
    window hide

    pause 0.2
    play sound "audio/soundFX/FX6/twirl.wav" volume 0.5

    show tripfightbase3 with dissolve
    with hpunch
    pause 0.8
    window show
    bull "'That so?!"
    "Alfred twists his wrist, with a finger extending from his closed fist!"
    rolf "Hmn?!"
    window hide
    scene rolfdodge with fade
    show blackshake at truecenter zorder -100
    play sound "audio/soundFX/FX6/EarCut5.mp3" volume 1.0
    with hpunch
    pause 1.0
    window show
    show blackshake at truecenter zorder -100
    rolf "-Kha!"
    "Rolf quickly bends his legs and lowers his upper body!"
    "The bull's sharp fingernail just barely misses Rolf's eye!"

    window hide


    scene groundpoke
    show blackshake at truecenter zorder -100
    show groundpokee
    show groundpokewind
    with fade
    play sound "audio/soundFX/FX6/sandpoke.mp3" volume 1.0
    with vpunch
    pause 0.3
    hide groundpokee
    hide groundpokewind
    with dissolve
    pause 0.5
    window show
    bull "!!"
    "His finger digs into the ground!"
    window hide
    show groundpokeb with dissolve
    pause 0.3
    window show
    rolf "You cheating bastard!"
    "Rolf flattens his hand and-"
    window hide
    play sound "audio/soundFX/FX6/slap4.mp3" volume 0.7

    scene bullslap
    show blackshake at truecenter zorder -100
    show bullslaphand
    show bullslapsmack
    with dissolve
    with hpunch
    hide bullslapsmack with dissolve
    pause 0.5
    hide bullslaphand with dissolve
    window show
    bull "PHUUN!"
    "Smacks him HARD across the face!"
    window hide
    scene dong1 with fade
    show blackshake at truecenter zorder -100
    play sound "audio/soundFX/FX6/singlebell.wav" volume 0.8
    show dong2 with hpunch
    play music "audio/MPP_-_Brewing_Tension_Pre-Fight_VERSE.mp3" fadein 5.0 volume 0.11
    pause 0.3
    window show
    "The bell rings again!"
    window hide
    scene dong1 with dissolve
    show blackshake at truecenter zorder -100
    play sound "audio/soundFX/Crowd/donnacheer.wav"fadein 0.7 volume 0.1
    window hide
    pause 0.1
    scene crowdbronbase
    show blackshake at truecenter zorder -100
    if modest == True:
        show crowdemesuit
    else:
        show crowdemelon
    show crowdbron fistup
    show crowdem pout
    with fade
    pause 0.5
    window show
    bron "Hah! Got him good!"
    show crowdemlookbron

    with dissolve
    emelie "That slap was loud! This is so scary! "
    show crowdb eyeside
    with dissolve
    bron "And that's his damaged arm!"
    show crowdbron fistdown with dissolve
    bron "He can't even make a proper fist with that one!"
    hide crowdem pout
    hide crowdemlookbron
    with dissolve
    emelie "Whaaa-"
    window hide
    hide crowdb with dissolve
    pause 0.3

    scene cornerrolf
    show blackshake at truecenter zorder -100
    show cornerrolfblur
    if modest == True:
        show cornerrolfblurblue
    with fade
    pause 0.3
    window show
    rolf "Ugh..."
    window hide
    show blurrolf with dissolve
    show blurrolfx with dissolve

    hide cornerrolfblur
    if modest == True:
        hide cornerrolfblurblue
        show cornerrolfblue
    with dissolve
    with hpunch
    pause 0.3
    window show
    bron "HEY, DAD! Stop playing around!"
    "Bronwen cheers him on from behind!"
    bron "One round left, so get him with a good one!"
    window hide
    show cornerrolfblur
    if modest == True:
        show cornerrolfblurblue
    hide blurrolf
    with dissolve
    hide blurrolfx with dissolve
    pause 0.3
    window show
    rolf "..."
    rolf "Can't believe that shithead tried to poke me, too..."#smaller text
    rolf "And he almost got away with it! "#smaller text
    window hide
    play sound "audio/soundFX/FX6/270482__littlerobotsoundfactory__blood_drip_02.wav" volume 0.6

    show cornerrol blood1 with dissolve
    pause 0.3
    window show
    "Blood drips down onto Rolf's hand! "
    window hide
    show cornerrol blood2

    with dissolve
    pause 0.3
    window show
    rolf "Hmn?! "
    rolf "Shit. Seems he did get me after all."
    show cornerrol blood2b with dissolve

    rolf "I've gotten slow."
label rolfwound:

    if bloodcensor == True:
        "I hate the sight of blood, so I follow Frank's advice and squint as I step forward to inspect Rolf's wound!"
        window hide
        show censoreye zorder 100
        with dissolve

    else:
        "I step forward to take a look at Rolf's wound."
        window hide
    scene rolfcutbase
    show blackshake at truecenter zorder -100
    if bloodcensor == True:
        show censoreye zorder 100
    with fade
    pause 0.3
    stop music fadeout 3.0
    window show
    me "'You good? "
    show rolfcuteye usb with dissolve
    rolf "Yes, yes... Just a scratch."
    window hide
    show rolfcutopen1 with dissolve
    play sound "audio/soundFX/FX6/270482__littlerobotsoundfactory__blood_drip_02slow.wav" volume 1.0
    pause 0.1
    hide rolfcutopen1
    show rolfcuteyeblood usb
    with dissolve
    show rolfcuteyeblood us
    with dissolve
    pause 0.2
    window show
    "The cut opens slightly and blood starts flowing out."
    show rolfcuteye shut
    show rolfcuteyeblood shut
    with dissolve

    rolf "Hmf-"

    rolf "I'll just-"
    window hide
    show rolfcuteye squintb
    show rolfcuteyeblood usc
    with dissolve
    pause 0.3
    show rolfcuteye shut
    show rolfcuteyeblood shut
    with dissolve
    show rolfcuteye squint
    show rolfcuteyeblood usc
    with dissolve
    pause 0.3
    window show
    rolf "Blink this out real quick-"
    window hide
    show rolfcuteye shut
    show rolfcuteyeblood shut
    with dissolve
    pause 0.2
    window show
    rolf "..."
    ref "Hey, [Protagonist]!"
    me "Y-Yeah!?"
    ref"What are you waiting for?! That cut is in a TERRIBLE spot!"
    ref "If Rolf can't see when the bell clangs, the fight's up! "
    ref "You've got ONE MINUTE!"
    if bloodcensor == True:
        window hide
        jump minigamecutcensor
    else:
        jump minigamecut

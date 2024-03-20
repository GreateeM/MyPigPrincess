label Chapter2:
    stop music fadeout 1.2
    scene black with fade
    $ unlock("S1")
    $ renpy.end_replay()
    pause 0.5
    scene bg emelieroom with fade
    play sound "audio/soundFX/Blanket Move.wav"
    show em oilhole at right:
        yalign 0.15
        zoom 1.0

    show emf normalblush at right:
        yalign 0.15
        zoom 1.0
    show emear high at right:
        yalign 0.15
        zoom 1.0
    if cumface == True:
        show Emoil barefacial at right:
            yalign 0.15
            zoom 1.0
    if cumface == False:
        show Emoil cum at right:
            yalign 0.15
            zoom 1.0
    with dissolve

label gotinface:
    window show
    play music "audio/starting-out-waltz-vivace-by-kevin-macleod-from-filmmusic-io.mp3" fadein 0.1 volume 0.3

    emelie "T-that sure was a lot!"
    if cumface== True:
        emelie "It got all over my face, too! Jeez!"
        me "Sorry about that-"
        show emf bigsmile with dissolve
        emelie "No, no!"
        emelie "I told you not to hold back, so don't apologize!"

    else:
        hide emear high
        show emf fluster
        with dissolve
        emelie "Jeez, my cleavage is dripping like crazy!"
        emelie "At least you showed some restraint by keeping it contained to my breasts!"
        emelie "Such a gentleman!~"
    emelie "Anyways, I'm one big gooey mess right now with all this oil too, huh?"
    show blackshake at truecenter behind bg
    show emf laugh
    show emear high
    with dissolve
    emelie "Is it a good look on me or what? Hahaha~"
    "She looks both amused and embarrassed by the big mess we made and I can't help but join in with her laughter."
    me "I could definitely get used to it! "
    show emf grin
    hide emear high
    with dissolve
    emelie "Ha-ha."
    show emf normal with dissolve
    emelie "Well, you're pretty spotless by comparison!"
    show emf normalblush with dissolve
    emelie "A little sweaty maybe but all that oil's been absorbed into your skin!"
    emelie "And you made sure to get your ENTIRE load on me!"
    show emf surprise with dissolve
    emelie "I have to go clean up!"
    emelie "..."
    show emf insecure with dissolve
    emelie "You can join me if you'd like-"
    window hide
    stop music fadeout 0.1
    with vpunch
    play music "audio/Unsafe+Roads+-+320bit.mp3" fadein 3.0 volume 0.3
    play sound "audio/soundFX/FX2/pig-scream.wav"
    #subtle tense music playing


    show em crownpop
    hide emf
    with dissolve


    window show
    rolf "EMELIEEEEEEEEEEEEE!"
    "A scream echoes down the halls!"
    "That's definitely Rolf, Billy's uncle from earlier!"
    emelie "Oh crap!"
    with hpunch
    rolf "PRINCEEEEEEEEEEEEEEEESSSSS!"
    show emear high at right:
        yalign 0.15
        zoom 1.0
    if cumface== True:
        hide Emoil
        show em tidoilsurprise behind emf at right:
            yalign 0.15
            zoom 1.0
        show emf panic at right:
            yalign 0.15
            zoom 1.0
        show emfacecum at right:
            yalign 0.15
            zoom 1.0
        with dissolve
    else:
        hide Emoil
        show em tidoilsurprisetidcum behind emf at right:
            yalign 0.15
            zoom 1.0
        show emf panic at right:
            yalign 0.15
            zoom 1.0
        with dissolve

    emelie "This is bad! Put your clothes on!"
    emelie "Hurry!"
    me"O-okay!"
    window hide

    show blackopacity
    show feetbare
    with dissolve
    window show
    "I quickly put my clothes back on, followed by my shoes."
    play sound "audio/soundFX/Get.mp3"
    show feet
    with dissolve
    "Phew! My back's definitely a lot better now!"
    hide feet
    hide feetbare
    hide blackopacity
    with dissolve


    me "Done!"
    me "Now, what about you?"
    window hide
    play sound "audio/soundFX/Step1.wav"
    with vpunch

    show emeye side2 behind emfacecum at right:
        yalign 0.15
        zoom 1.0
    if cumface== True:
        show emfacecum at right:
            yalign 0.15
            zoom 1.0

    with dissolve
    window show

    emelie "I ... UUUHH..."
    "Billy's voice can be faintly heard just outside the door."
    window hide
    show blackopacity
    show EmelieDoorInside
    with dissolve
    window show
    billy "Oh hey, uncle!"
    billy "'You want some carrot cake?-"
    rolf "NEPHEW!! "
    "Rolf's right outside!"
    rolf "You brought a damn peasant through the gates?!"
    rolf "DIRECTLY INTO THE ROYAL CHAMBERS?!"
    play sound "audio/soundFX/FX2/outsidebonk.wav"
    with vpunch
    "A metallic bonk is heard from the other side of the door!"
    window hide
    hide blackopacity
    hide EmelieDoorInside
    with dissolve

    hide emeye side2
    hide emf
    hide emear
    hide Emoil
    hide em
    hide emfacecum
    if cumface== True:
        show emcomp facialconcern at right:
            yalign 0.15
            zoom 1.0

    else:
        show emcomp betweentids at right:
            yalign 0.15
            zoom 1.0
    with dissolve

    window show
    emelie "I've gotta hide fast!"
    if cumface== True:
        hide emcomp facialconcern with easeoutleft

    else:

        hide emcomp betweentids with easeoutleft
    "Emelie quickly jumps inside a medium-sized wardrobe at the other side of the room, slamming it shut."
    window hide

    show blackopacity
    show Wardrobe
    with dissolve
    play sound "audio/soundFX/Door Slam.wav"
    with hpunch
    window show
    emelie "Try to act like nothing's out of the ordinary!"

    window hide

    hide blackopacity
    hide Wardrobe
    with dissolve
    window show
    me "What?!"
label rolfbargesin:
    window hide
    show blackopacity
    show EmelieDoorInside
    with dissolve
    window show
    rolf "DON'T WORRY, PRINCESS! I'M HERE!"


    window hide
    pause 0.3
    play sound "audio/soundFX/FX2/kicking-forcing-breaking-wooden-door.flac"
    play music "audio/7.+Stöðvar+-+320bit.mp3" fadein 0.1 volume 0.7 noloop
    queue music "audio/1.+Grundar+-+320bit.mp3" fadein 0.1 volume 0.7

    with hpunch

    show blackshake at truecenter behind bg
    show RolfDoorSmash with dissolve
    pause 0.3
    window show
    "Rolf barges right through the heavy wooden door!"
    "I quickly hop to the side as it breaks off the hinges and crashes into the bed!"
    window hide
    hide blackopacity
    hide RolfDoorSmash
    hide EmelieDoorInside
    with dissolve
    show EmelieRoomDoor behind blackopacity
    with dissolve
    pause 0.4
    play sound "audio/soundFX/run2r.wav" volume 0.5
    pause 0.3
    show rolf fistsmoke at right:
        yalign 0.35 xalign 1.20
        zoom 0.9
    with easeinright
    window show
    rolf "Where are you, Emelie?!"
    "Rolf quickly scans the room before locking eyes with me."
    show rolf fist
    with dissolve
    if liename == True:
        rolf "Well if it isn't \" [lie_name] \"?!"
    else:
        rolf "Well if it isn't [Protagonist]!"
    show rolf knuckles
    with dissolve
    rolf "I knew something smelled rotten with you!"
    show roleye squint at right:
        yalign 0.35 xalign 1.20
        zoom 0.9
    with dissolve

    rolf "\"New recruit\" my hairy fuckin' ass!"
    hide roleye
    hide rolf
    show rolcomp knucklerage at right:
        yalign 0.35 xalign 1.20
        zoom 0.9
    with dissolve

    rolf "Where have you taken the princess?!"

    show rolcomp knucklerage at right:
        linear 0.4 zoom 1.0 yalign 0.35 xalign 1.50
    pause 0.3
    play sound "audio/soundFX/Step1.wav"
    with vpunch
    "He takes a heavy step towards me!"
    me "I didn't take her anywhere!"
    hide rolcomp
    show rolf base at right:
        zoom 1.0 yalign 0.35 xalign 1.50
    show roleye squint at right:
        zoom 1.0 yalign 0.35 xalign 1.50
    with dissolve

    rolf "Not gonna talk?"
    show rolf back2 at right:
        zoom 1.0 yalign 0.35 xalign 1.50
    with dissolve
    "He reaches behind his back."
    window hide
    hide rolf
    hide roleye
    show rolcomp axescream at right:
        zoom 1.0 yalign 0.35 xalign 1.50
    play sound "audio/soundFX/FX2/unsheath-wav.wav"
    with dissolve
    pause 0.2
    window show
    rolf "I'll make you bloody talk!"
    window hide
    show rolcomp axescream at right:
        linear 0.4 zoom 1.1 yalign 0.30 xalign 2.20
    pause 0.3
    play sound "audio/soundFX/Step1.wav"
    with vpunch

    show rolcomp axescream at right:
        linear 0.1 zoom 1.2 yalign 0.23 xalign -0.60

    pause 0.2
    play sound "audio/soundFX/Step1.wav"
    with vpunch
    window show
    "He quickly lunges towards me with his massive axe!"

    window hide
    show blackopacity
    show Wardrobe
    with dissolve
    window show
    emelie "Rolf, stop!"
    emelie "I'm in here!"
    window hide
    hide blackopacity
    hide Wardrobe
    with dissolve
    pause 0.3
    show rol concern at right:
        zoom 1.2 yalign 0.23 xalign -0.60
    show roleye lookside at right:
        zoom 1.2 yalign 0.23 xalign -0.60
    with dissolve
    window show
    rolf "Emelie, is that you?!"
    show rol scream
    show roleye intenseside
    with dissolve
    rolf "Are you alone in there or are you being held captive?!"
    hide rolcomp
    show rolf axe behind roleye at right:
        zoom 1.2 yalign 0.23 xalign -0.60
    hide rol
    with dissolve
    rolf "How many others are in there?! 'They armed or not!?"
    window hide
    show rolcomp axescream2 at right:
        zoom 1.2 yalign 0.23 xalign -0.60
    show blackopacity
    show Wardrobe
    with dissolve
    window show
    emelie "I'm all alone!"
    emelie "You have to calm down!"
    window hide
    hide roleye
    show rol rage at right:
        zoom 1.2 yalign 0.23 xalign -0.60
    show roleye intenseside at right:
        zoom 1.2 yalign 0.23 xalign -0.60



    hide blackopacity
    hide Wardrobe
    with dissolve
    hide rol
    hide rolmouth
    hide roleye
    hide rolf
    show rolcomp axescream3 at right:
        zoom 1.2 yalign 0.23 xalign -0.60

    with dissolve
    show rolcomp axescream3 at right:

        linear 0.6 zoom 1.0 yalign 0.25 xalign 1.50

    pause 0.4
    play sound "audio/soundFX/Step1.wav"
    pause 0.2
    hide rolcomp
    show rolf back at right:
        zoom 1.0 yalign 0.25 xalign 1.50
    show roleye intenseside at right:
        zoom 1.0 yalign 0.25 xalign 1.50
    show rolmouth pout at right:
        zoom 1.0 yalign 0.25 xalign 1.50
    with dissolve
    pause 0.3
    show rolf base at right:
        zoom 1.0 yalign 0.25 xalign 1.50
    show rolmouth pout at right:
        zoom 1.0 yalign 0.25 xalign 1.50
    with dissolve
    window show
    rolf "Hmph!"
    rolf "But how do I know they're not holding a knife to your neck and forcing you to say that?!"
    window hide
    play sound "audio/soundFX/run2.wav"
    show billy ko at left:
        yalign -2.0 xalign -2.0

        linear 0.5 yalign -1.0 xalign -0.6
    pause 0.4
    window show
    billy "U-uncle, please! "
    billy "[Protagonist]'s a nice guy, you don't have to be so suspicious!-"
    if liename == True:
        show rolf knuckles at right:
            zoom 1.0 yalign 0.25 xalign 1.50
        show roleye intense at right:
            zoom 1.0 yalign 0.25 xalign 1.50
        hide rolmouth
        with dissolve
        rolf "So THAT'S the real name of this infiltrator!"
        rolf "If he was such a  \"nice guy \" he wouldn't fake his name and disguise himself with a guard's helmet!"
        show billy ko at left:
            yalign -1.0 xalign -0.6

            linear 0.5 yalign -1.0 xalign -0.5
        billy "That was my idea because I knew you'd have such a strong reaction to a human in the royal quarters!"
    else:
        show rolf knuckles at right:
            zoom 1.0 yalign 0.25 xalign 1.50
        show roleye intense at right:
            zoom 1.0 yalign 0.25 xalign 1.50
        hide rolmouth
        with dissolve
        rolf "Why would such a \"nice guy \" disguise himself with a guard's helmet?!"
        show billy ko at left:
            yalign -1.0 xalign -0.6

            linear 0.5 yalign -1.0 xalign -0.5
        billy "That was my idea because I knew you'd have such a strong reaction to a human in the royal quarters!"
    show billy ko at left:
        yalign -1.0 xalign -0.5

        linear 0.5 yalign -1.0 xalign -0.4
    billy "Just take a few breaths and calm down."
    window hide
    show roleye lookside at right:
        zoom 1.0 yalign 0.25 xalign 1.50
    with dissolve

    window show
    rolf "You take one step closer and I'll flatten the other half of your goddamn head too."
    show billy:
        linear 0.5 yalign -1.2 xalign -0.5
    pause 0.2
    billy "O-Okay..."
    "Billy looks in pretty bad shape!"
    window hide
    menu:
        with dissolve
        "Billy are you okay?!":
            window show
            me  "Billy are you okay?!"
            show billy kohappy with dissolve
            billy "Aw...Thanks for your concern, buddy!"
            billy "Legs feel a little wobbly is all... "
            billy "This is why you should always wear a helmet!"
            billy "But don't worry about me, [Protagonist]!"
        "Don't you dare hit him again, Rolf!":
            window show
            me "Don't you dare hit him again!"
            hide roleye lookside with dissolve
            rolf "HAH! Or what?!"
            rolf "I'm the highest rankin' guard in the kingdom! "
            show roleye squint at right:
                zoom 1.0 yalign 0.25 xalign 1.50
            with dissolve
            rolf "Boy's lucky we're family or I'd have to punch some REAL sense into that stupid helmet! "

            billy "Please, [Protagonist]! "
            billy "Stay back and don't worry about me!"


    billy "Just be honest about what happened here today and you'll be out of trouble in no time!"
    show billy:
        linear 0.8 yalign -2.0 xalign -2.0
    "I give Billy a nod as he crawls out the door."
    hide billy
    "His advice would probably be solid if sneaking in and lying were the only issues at hand."
    "But if Rolf finds Emelie in a torn-down dress covered in oil and cum I'm definitely done for!"
    show rolf base
    show roleye intenseside at right:
        zoom 1.0 yalign 0.25 xalign 1.50
    with dissolve

    rolf "Emelie why are you in the goddamn wardrobe?! "
    window hide
    show blackopacity
    show Wardrobe
    with dissolve
    window show
    emelie "I'm... just changing clothes!"
    rolf "INSIDE the wardrobe!?"
    emelie "Of course!"
    emelie "You wouldn't want me changing in front of [Protagonist], would you!?"
    window hide
    hide blackopacity
    hide Wardrobe
    with dissolve
    show rolf apologetic
    hide roleye
    with dissolve
    window show

    rolf "Well no of course not-"
    show rolf knuckles with dissolve
    rolf "Wait why is he in here to begin with?!"
    window hide
    show blackopacity
    show Wardrobe
    with dissolve
    window show
    emelie "Because I requested it!"
    emelie "He's...uuhh..."
    emelie "He's my new personal assistant!"
    "What?!"
    emelie "And he just brought me this new dress I'm trying on."
    emelie "If it doesn't fit he'll return it quick before closing time!"
    window hide
    hide blackopacity
    hide Wardrobe
    with dissolve
    show roleye squint at right:
        zoom 1.0 yalign 0.25 xalign 1.50
    with dissolve
    window show
    rolf "Assistant, eh?!"
    show roleye intenseside at right:
        zoom 1.0 yalign 0.25 xalign 1.50
    with dissolve
    rolf "Your mother's tried to get you one for years now but you never want the help!"
    window hide
    show blackopacity
    show Wardrobe
    with dissolve
    window show
    emelie "It's... becaaause...they've never been good enough!"
    emelie "But [Protagonist] here is the best one in the whole kingdom!"
    window hide
    hide blackopacity
    hide Wardrobe
    with dissolve
    window show
    rolf "That doesn't add up at all!"
    rolf "I bumped into Per on my patrol who told me he'd just let Billy in with a human {u}PEASANT{/u}."
    emelie"..."
    show roleye intense with dissolve
    rolf "I realized this \"new recruit\" was on his way to your chambers!"
    rolf "That's why I came running!"
    show roleye intenseside with dissolve
    rolf "Emelie, show yourself right now so I know you're unharmed!"
    window hide
    show blackopacity
    show Wardrobem Empty
    with dissolve
    window show

    emelie "I'm basically naked in here!"
    emelie "I'm trying to fit into this new dress but it's too tight!"
    if cumface== True:
        rolf "FINE! But at least show me your face!"
        "Crap that's not going to work!"
        "Her face is covered with cum!"
        emelie "I uuhh... I'm not wearing any makeup!"
        emelie "I can't show my face like this!"
        rolf "Emelie! No more games!"
        rolf "Show me SOMETHING!"
        window hide

        play sound "audio/soundFX/FX2/tada2.wav" volume 0.7

        show blackopacity
        show Wardrobem Thumb
        with dissolve
        pause 0.7
        window show
        emelie "There!"
        emelie "Now stop interrupting me so I can focus on getting this dress on!"
        rolf "Hmph okay FINE."
        rolf "BUT I'M NOT HAPPY WITH THIS!"
        window hide
    else:
        rolf "FINE! But at least show me your face!"
        emelie "... Just my face!"
        window hide
        show blackopacity
        show Wardrobem Clean
        with dissolve
        pause 0.3
        window show
        "Her face is pretty spotless as far as any suspicious fluids are concerned!"
        emelie "See? I'm all good in here! Not a mark on me!"
        rolf "Hmph... fine!"
        window hide

    hide blackopacity
    hide Wardrobem
    hide Wardrobem Clean
    hide Wardrobe
    with dissolve
    if cumface== False:
        window show
        rolf "Now focus on getting dressed so you can come out of there!"
    hide roleye with dissolve
    window show
    "Rolf turns his attention back towards me."
    rolf "Now, if Emelie's right and you're some sort of amazing assistant..."
    window hide
    show rolf knuckles at right:
        linear 0.4 zoom 1.1 yalign 0.30 xalign 2.20
    pause 0.3
    play sound "audio/soundFX/Step1.wav"
    with vpunch

    show rolf knuckles at right:
        linear 0.1 zoom 1.2 yalign 0.23 xalign -0.60

    pause 0.2
    play sound "audio/soundFX/Step1.wav"
    with vpunch

    show roleye squint at right:
        zoom 1.2 yalign 0.23 xalign -0.60
    show rolf base at right:
        zoom 1.2 yalign 0.23 xalign -0.60
    with dissolve
    window show
    rolf "Then I don't think you'd be against answering a few basic questions you should know!"
    "He grabs me and pulls me closer!"
    # stop music fadeout 0.5
    window hide
label interrogation:




    #Start with 3 points, at 0 you fail? if you have 2 but also came on Emelie's face then Roll will still tell you it's a perfect score.
    scene Interrogate Base
    play sound "audio/soundFX/Get.mp3"
    show InterroSquint
    with fade
    window show
    # play music "audio/1.+Grundar+-+320bit.mp3" fadein 0.1 volume 0.6
    if liename == True:
        rolf "Now listen closely,\" [lie_name] \"!"
    else:
        rolf "Now listen closely, [Protagonist]!"
    rolf "My vision isn't all it used to be..."
    hide InterroSquint with dissolve
    rolf "But up close I only need one eye to see right through the lies of a twerp like you!"
    show InterroSquint with dissolve
    rolf "If you answer my {u}TEN{/u} questions successfully I'll be on my way. "
    show Interrogate Hateh
    hide InterroSquint
    with dissolve
    rolf "But get more than {u}THREE{/u} questions wrong and I'll cave that skull of yours in!"

    #menu:
        #with dissolve
        #"didn't cum on face":
        #    $ cumface = False
        #    $ HardQuestions = False
        #    $ Failed = 0
        #    "No \"Failed\" question variable added."

        #"Came on face":
        #    $ cumface = True

    if cumface == True:
        $ HardQuestions = True
        $ Failed = 1
        # "Added 1 \"Failed\" question variable."

        show Interrogate Hate with dissolve
        show blackshake at truecenter behind Interrogate
        with hpunch
        rolf "Or those WOULD HAVE been the rules if Emelie had shown her face earlier like I asked!"
    # if questioning = hard then skip failed 1 dialogue
        rolf "Her refusal to do so has made me uneasy!"
        show Interrogate Hateh with dissolve
        rolf "SO YOU'RE ONLY ALLOWED {u}TWO{/u} INCORRECT QUESTIONS!"
        "Crap! That's what I get for not showing any restraint!"
        show InterroSquint
        show Interrogate Smile behind InterroSquint
        with dissolve
        rolf "Now, are you ready to begin the questioning?!"
    # rolf "Thinking too long is a sign of conjuring lies, so you better answer fast!"
    if cumface== False:
        $ HardQuestions = False
        $ Failed = 0
        rolf "Understood?"
        me "Yes!"
        rolf "Then are you ready to begin the questioning?"
    window hide
    menu:
        with dissolve
        "Let's start!":
            window show
            me "Let's start!"
    hide InterroSquint
    show Interrogate Laugh
    show InterroTongue
    with dissolve
    rolf "Good... I haven't interrogated anyone in weeks!"
    hide InterroTongue
    show InterroSquint
    with dissolve
    rolf "These are things any assistant in the kingdom should know!"
label questions:

    $ seenq1 = False
    $ seenq2 = False
    $ seenq3 = False
    "I hope I've been paying enough attention to get through this!"
    show Interrogate Base
    hide InterroSquint
    with dissolve
    rolf "Let's start off easy..."

label firstQ:
    show InterroSquint with dissolve

    rolf "What's the name of this city?!"
    "I'm pretty sure of this one!"

    menu:
        "What's the name of this city?"
        with dissolve
        "Hog Haven":
            me  "Hog Haven."
            hide InterroSquint with dissolve
            $ renpy.block_rollback()
            play sound "audio/soundFX/FX2/pig-grunt-double.wav"
            rolf "Of course!"
            rolf "The best city in the best kingdom!"
        "Piggy Paradise":
            $ Failed +=1
            me "Pig Paradise."
            hide InterroSquint
            $ renpy.block_rollback()
            show Interrogate Hate
            play sound "audio/soundFX/FX2/pig-squeak.wav"
            with dissolve
            rolf "Wrong!"
            rolf "But it has a nice ring to it..."
            show Interrogate Hateh
            show InterroSquint
            with dissolve
            me "Crap! I'm not good in these high stress situations!"


        "Swine Settlement":
            $ Failed +=1
            me "Swine Settlement"
            $ renpy.block_rollback()
            hide InterroSquint
            show Interrogate Hate
            play sound "audio/soundFX/FX2/pig-squeak.wav"
            with dissolve
            rolf "Wrong! "
            show Interrogate Hateh with dissolve
            rolf "And don't call us swines, you ape!"

            me "Crap! I'm not good in these high stress situations!"

    if seenq1==False:
        if Failed == 1 :
            #if HardQuestions == True

            if HardQuestions == False:
                hide InterroSquint
                show Interrogate Smile
                with dissolve
                rolf "That's your first wrong answer!"
                $ seenq1 = True

    if seenq2== False:
        if Failed == 2 :
            if HardQuestions == True:

                scene Interrogate Smile
                with dissolve
                rolf "That's your first wrong answer!"
                show InterroSquint with dissolve
                rolf "Maybe you're not such a good \"assistant\" after all!"
            if HardQuestions == False:

                scene Interrogate Smile
                with dissolve
                rolf "That's another incorrect answer!"
                show InterroSquint with dissolve
                rolf "Maybe you're not such a good \"assistant\" after all!"
            $ seenq2 = True

    if seenq3== False:
        if Failed == 3 :
            if HardQuestions == True:

                scene Interrogate Laugh
                with dissolve
                rolf "Now that's another incorrect answer!"
                show InterroSquint
                show Interrogate Smile
                with dissolve
                rolf "Hehe... Get {u}ONE{/u} more question wrong and you're done for!"
            if HardQuestions == False:

                scene Interrogate Laugh
                with dissolve
                rolf "Now that's yet another incorrect answer!"
                show InterroSquint
                show Interrogate Smile
                with dissolve
                rolf "Hehe... Get {u}ONE{/u} more question wrong and you're done for!"
            $ seenq3 = True

    if Failed == 4 :
        jump badend


screen Chapter2Choice1:
    add "gui/choices/RolfInterrogationUI.png"

    imagebutton:
        style "mainmenunew"
        idle "gui/choices/RolfChoiceLeft_idle.png"
        hover "gui/choices/RolfChoiceLeft.png"
        action Show(screen="ConfirmChoices", YesAction=Jump("secondQNr1"), Choice="Left", NoAction=Show(screen="Chapter2Choice1"), transition=dissolve)

    imagebutton:
        style "mainmenunew"
        idle "gui/choices/RolfChoiceMid_idle.png"
        hover "gui/choices/RolfChoiceMid.png"
        action Show(screen="ConfirmChoices", YesAction=Jump("secondQNr2"), Choice="Mid", NoAction=Show(screen="Chapter2Choice1"), transition=dissolve)

    imagebutton:
        style "mainmenunew"
        idle "gui/choices/RolfChoiceRight_idle.png"
        hover "gui/choices/RolfChoiceRight.png"
        action Show(screen="ConfirmChoices", YesAction=Jump("secondQNr3"), Choice="Right", NoAction=Show(screen="Chapter2Choice1"), transition=dissolve)

screen Chapter2Choice2:
    add "gui/choices/RolfInterrogationUI2.png"

    imagebutton:
        style "mainmenunew"
        idle "gui/choices/RolfChoiceLeft_idle2.png"
        hover "gui/choices/RolfChoiceLeft2.png"
        action Show(screen="ConfirmChoices", YesAction=Jump("thirdQNr1"), Choice="Left", NoAction=Show(screen="Chapter2Choice2"), transition=dissolve)

    imagebutton:
        style "mainmenunew"
        idle "gui/choices/RolfChoiceMid_idle2.png"
        hover "gui/choices/RolfChoiceMid2.png"
        action Show(screen="ConfirmChoices", YesAction=Jump("thirdQNr2"), Choice="Mid", NoAction=Show(screen="Chapter2Choice2"), transition=dissolve)

    imagebutton:
        style "mainmenunew"
        idle "gui/choices/RolfChoiceRight_idle2.png"
        hover "gui/choices/RolfChoiceRight2.png"
        action Show(screen="ConfirmChoices", YesAction=Jump("thirdQNr3"), Choice="Right", NoAction=Show(screen="Chapter2Choice2"), transition=dissolve)

screen Chapter2Choice3:
    add "gui/choices/RolfInterrogationUI3.png"

    imagebutton:
        style "mainmenunew"
        idle "gui/choices/RolfChoiceLeft_idle3.png"
        hover "gui/choices/RolfChoiceLeft3.png"
        action Show(screen="ConfirmChoices", YesAction=Jump("fourthQNr1"), Choice="Left", NoAction=Show(screen="Chapter2Choice3"), transition=dissolve)

    imagebutton:
        style "mainmenunew"
        idle "gui/choices/RolfChoiceMid_idle3.png"
        hover "gui/choices/RolfChoiceMid3.png"
        action Show(screen="ConfirmChoices", YesAction=Jump("fourthQNr2"), Choice="Mid", NoAction=Show(screen="Chapter2Choice3"), transition=dissolve)

    imagebutton:
        style "mainmenunew"
        idle "gui/choices/RolfChoiceRight_idle3.png"
        hover "gui/choices/RolfChoiceRight3.png"
        action Show(screen="ConfirmChoices", YesAction=Jump("fourthQNr3"), Choice="Right", NoAction=Show(screen="Chapter2Choice3"), transition=dissolve)

screen Chapter2Choice4:
    add "gui/choices/RolfInterrogationUI4.png"

    imagebutton:
        style "mainmenunew"
        idle "gui/choices/RolfChoiceLeft_idle4.png"
        hover "gui/choices/RolfChoiceLeft4.png"
        action Show(screen="ConfirmChoices", YesAction=Jump("fifthQNr1"), Choice="Left", NoAction=Show(screen="Chapter2Choice4"), transition=dissolve)

    imagebutton:
        style "mainmenunew"
        idle "gui/choices/RolfChoiceMid_idle4.png"
        hover "gui/choices/RolfChoiceMid4.png"
        action Show(screen="ConfirmChoices", YesAction=Jump("fifthQNr2"), Choice="Mid", NoAction=Show(screen="Chapter2Choice4"), transition=dissolve)

    imagebutton:
        style "mainmenunew"
        idle "gui/choices/RolfChoiceRight_idle4.png"
        hover "gui/choices/RolfChoiceRight4.png"
        action Show(screen="ConfirmChoices", YesAction=Jump("fifthQNr3"), Choice="Right", NoAction=Show(screen="Chapter2Choice4"), transition=dissolve)

screen Chapter2Choice5:
    add "gui/choices/RolfInterrogationUI5.png"

    imagebutton:
        style "mainmenunew"
        idle "gui/choices/RolfChoiceLeft_idle5.png"
        hover "gui/choices/RolfChoiceLeft5.png"
        action Show(screen="ConfirmChoices", YesAction=Jump("sixthQNr1"), Choice="Left", NoAction=Show(screen="Chapter2Choice5"), transition=dissolve)

    imagebutton:
        style "mainmenunew"
        idle "gui/choices/RolfChoiceMid_idle5.png"
        hover "gui/choices/RolfChoiceMid5.png"
        action Show(screen="ConfirmChoices", YesAction=Jump("sixthQNr2"), Choice="Mid", NoAction=Show(screen="Chapter2Choice5"), transition=dissolve)

    imagebutton:
        style "mainmenunew"
        idle "gui/choices/RolfChoiceRight_idle5.png"
        hover "gui/choices/RolfChoiceRight5.png"
        action Show(screen="ConfirmChoices", YesAction=Jump("sixthQNr3"), Choice="Right", NoAction=Show(screen="Chapter2Choice5"), transition=dissolve)

screen ConfirmChoices(YesAction, NoAction, Choice=None):
    modal True

    if Choice:
        use expression "Choice" + Choice + "Dark"

    imagebutton:
        idle "gui/choices/No Idle.png"
        hover "gui/choices/No Hover.png"
        style "mainmenunew"
        action Hide(screen="ConfirmChoices"), NoAction

    imagebutton:
        idle "gui/choices/Yes Idle.png"
        hover "gui/choices/Yes Hover.png"
        style "mainmenunew"
        action Hide(screen="ConfirmChoices"), YesAction

screen ChoiceLeftDark:
    add "gui/choices/LeftSelect.png"

screen ChoiceMidDark:
    add "gui/choices/MiddleSelect.png"

screen ChoiceRightDark:
    add "gui/choices/RightSelect.png"

label secondQ:
    scene Interrogate Base
    show InterroSquint
    with dissolve
    rolf "This next one requires a visual..."

    show InterroLookdown with dissolve

    "Rolf pulls out a stack of thick paper sheets and a pencil and starts sketching."
    show Interrogate Grump with dissolve
    rolf "If you get this one wrong you can't blame my drawing skills!"
    rolf "I've done sketches based on witness descriptions for years now. "
    rolf "A witness is all you have to go on most of the time, so a good sketch is the fastest way to put scum behind bars!"
    "He scribbles for another moment then raises the sketch mere inches in front of my face."
    show Interrogate Base
    hide InterroLookdown
    with dissolve
    pause 0.3
    show sketches faces with dissolve
    rolf "Point to the image of the princess!"

    window hide
    hide sketches faces
    show screen Chapter2Choice1
    $ preferences.afm_enable = False
    $ disableAFMbutton = True
    $ _skipping = False
    $ renpy.pause(hard=True)

label secondQNr1:
    hide screen Chapter2Choice1
    show sketches faces
    $ Failed +=1
    window show
    me  "The left pig."
    $ _skipping = True
    $ disableAFMbutton = False
    $ renpy.block_rollback()
    hide InterroSquint
    hide sketches faces
    show Interrogate Hate
    play sound "audio/soundFX/FX2/pig-scream-loud-oink.wav"
    with dissolve
    rolf "INCORRECT! The princess has much softer features!"
    if Failed == 4 :
        jump badend
    jump secondQFinished

label secondQNr2:
    hide screen Chapter2Choice1
    show sketches faces
    $ Failed +=1
    window show
    me "The middle pig."
    $ _skipping = True
    $ disableAFMbutton = False
    $ renpy.block_rollback()
    hide InterroSquint
    hide sketches faces
    show Interrogate Hate
    play sound "audio/soundFX/FX2/pig-scream-loud-oink.wav"
    with dissolve
    rolf "That's the damn queen! WRONG!"
    if Failed == 4 :
        jump badend
    rolf "They may look alike but mistaking them is near impossible even with just one eye!"
    jump secondQFinished

label secondQNr3:
    hide screen Chapter2Choice1
    show sketches faces
    window show
    me "The pig to the right."
    $ disableAFMbutton = False
    $ _skipping = True
    $ renpy.block_rollback()
    play sound "audio/soundFX/FX2/pig-grunt.wav"
    rolf "Yes, that is correct!"
    hide sketches faces
    with dissolve
    rolf "I guess you're familiar enough to at least distinguish her from other piggies!"
    jump secondQFinished

label secondQFinished:
    hide screen Chapter2Choice1

    if seenq1==False:
        if Failed == 1 :
            #if HardQuestions == True

            if HardQuestions == False:
                hide InterroSquint
                show Interrogate Smile
                with dissolve
                rolf "That's your first wrong answer!"
                $ seenq1 = True

    if seenq2== False:
        if Failed == 2 :
            if HardQuestions == True:

                scene Interrogate Smile
                with dissolve
                rolf "That's your first wrong answer!"
                show InterroSquint with dissolve
                rolf "Maybe you're not such a good \"assistant\" after all!"
            if HardQuestions == False:

                scene Interrogate Smile
                with dissolve
                rolf "That's another incorrect answer!"
                show InterroSquint with dissolve
                rolf "Maybe you're not such a good \"assistant\" after all!"
            $ seenq2 = True

    if seenq3== False:
        if Failed == 3 :
            if HardQuestions == True:

                scene Interrogate Laugh
                with dissolve
                rolf "Now that's another incorrect answer!"
                show InterroSquint
                show Interrogate Smile
                with dissolve
                rolf "Hehe... Get {u}ONE{/u} more question wrong and you're done for!"
            if HardQuestions == False:

                scene Interrogate Laugh
                with dissolve
                rolf "Now that's yet another incorrect answer!"
                show InterroSquint
                show Interrogate Smile
                with dissolve
                rolf "Hehe... Get {u}ONE{/u} more question wrong and you're done for!"
            $ seenq3 = True

    if Failed == 4 :
        jump badend




    window hide
    scene Interrogate Base
    show InterroSquint
    with dissolve

    menu:
        with dissolve
        "Those were some nice drawings!":
            window show
            me  "Those were some nice drawings!"
            hide InterroSquint
            show Interrogate Cute
            play sound "audio/soundFX/FX2/pig-grunt.wav"
            with dissolve
            rolf "Thank you, I'm pretty happy with them myself!"
            rolf "Maybe I'll bring 'em back home and buy a nice frame-"
            show Interrogate Grump with dissolve
            rolf "..."
            play sound "audio/soundFX/FX2/pig-squeak.wav"
            show Interrogate Hateh with dissolve
            rolf "YOU TRYING TO FLATTER YOUR WAY OUT OF THIS?"
            me "No, I was just surprised!"
            show Interrogate Grump
            show InterroSquint
            with dissolve
            "..."
            rolf "Well here comes the next question!"

        "*Don't say anything.* ":
            window show
            "I hold the urge to compliment his drawings."

            rolf "Now here comes the next question!"


label thirdQ:
    show InterroLookdown with dissolve
    rolf "A good assistant will do everything possible to save their client some extra time!"
    rolf "One of these small daily tasks is to put on or remove the client's shoes."
    hide InterroLookdown
    show InterroSquint
    with dissolve

    rolf "So what do the princess' feet look like?!"
    $ preferences.afm_enable = False
    show sketches feet with dissolve
    window hide
    hide sketches feet
    show screen Chapter2Choice2
    $ disableAFMbutton = True
    $ preferences.afm_enable = False
    $ _skipping = False
    $ renpy.pause(hard=True)


label thirdQNr1:
    hide screen Chapter2Choice2
    show sketches feet
    window show
    me  "Like the left foot."
    $ _skipping = True
    $ disableAFMbutton = False
    $ renpy.block_rollback()
    hide sketches feet
    show Interrogate Base
    show InterroSquint
    play sound "audio/soundFX/FX2/pig-grunt-double.wav"
    with dissolve
    rolf "Yes! And stuffing 'em inside a pair of uncomfy shoes all day won't do them any good!"
    rolf "As an assistant it's your job to make sure your client's comfortable at all times!"
    jump thirdQFinished

label thirdQNr2:
    hide screen Chapter2Choice2
    show sketches feet
    window show
    me "Like the middle foot."
    $ disableAFMbutton = False
    $ _skipping = True
    $ renpy.block_rollback()
    $ Failed +=1
    hide InterroSquint
    hide sketches faces
    show Interrogate Hate
    play sound "audio/soundFX/FX2/pig-squeak.wav"
    with dissolve
    rolf "THOSE ARE MY FEET! Wrong!"

    me "...oh."
    if Failed == 4 :
        jump badend
    jump thirdQFinished

label thirdQNr3:
    hide screen Chapter2Choice2
    show sketches feet
    window show
    me "Like the foot to the right."
    $ disableAFMbutton = False
    $ _skipping = True
    $ renpy.block_rollback()
    $ Failed +=1
    hide InterroSquint
    hide sketches faces
    show Interrogate Hate
    play sound "audio/soundFX/FX2/pig-squeak.wav"
    with dissolve
    rolf "That's a damn horse foot! "
    if Failed == 4 :
        jump badend
    rolf "Maybe scraping horseshoes clean would suit you more than this assistant business..."
    jump thirdQFinished
label thirdQFinished:
    hide screen Chapter2Choice2
    hide sketches feet
    with dissolve


    if seenq1==False:
        if Failed == 1 :
            #if HardQuestions == True

            if HardQuestions == False:
                hide InterroSquint
                show Interrogate Smile
                with dissolve
                rolf "That's your first wrong answer!"
                $ seenq1 = True

    if seenq2== False:
        if Failed == 2 :
            if HardQuestions == True:

                scene Interrogate Smile
                with dissolve
                rolf "That's your first wrong answer!"
                show InterroSquint with dissolve
                rolf "Maybe you're not such a good \"assistant\" after all!"
            if HardQuestions == False:

                scene Interrogate Smile
                with dissolve
                rolf "That's another incorrect answer!"
                show InterroSquint with dissolve
                rolf "Maybe you're not such a good \"assistant\" after all!"
            $ seenq2 = True

    if seenq3== False:
        if Failed == 3 :
            if HardQuestions == True:

                scene Interrogate Laugh
                with dissolve
                rolf "Now that's another incorrect answer!"
                show InterroSquint
                show Interrogate Smile
                with dissolve
                rolf "Hehe... Get {u}ONE{/u} more question wrong and you're done for!"
            if HardQuestions == False:

                scene Interrogate Laugh
                with dissolve
                rolf "Now that's yet another incorrect answer!"
                show InterroSquint
                show Interrogate Smile
                with dissolve
                rolf "Hehe... Get {u}ONE{/u} more question wrong and you're done for!"
            $ seenq3 = True

    if Failed == 4 :
        jump badend

label fourthQ:
    scene Interrogate Base
    show InterroSquint
    with dissolve
    rolf "..."

    rolf "A good assistant also needs to be aware of what interests their clients have..."
    show InterroSide with dissolve
    rolf "And I see the princess has been reading a book recently ..."
    hide InterroSide
    hide InterroSquint
    show Interrogate Smile
    with dissolve

    rolf "What's the name of the book on the bed?!"
    "Rolf's body is blocking me from seeing it! I remember it started with an \"H\" and ended with \"Hunk\"..."

    menu:
        "What's the name of the book Emelie was reading??"
        with dissolve
        "Horny Hunk":
            $ Failed +=1
            me "Horny Hunk."
            $ renpy.block_rollback()
            hide InterroSquint
            hide sketches faces
            show Interrogate Hate
            play sound "audio/soundFX/FX2/pig-scream-loud-oink.wav"
            with dissolve
            rolf "Wrong!"

            if Failed == 4 :
                jump badend
            rolf "And what do you mean horny?! "
            rolf "Hope you're talkin'bout the kinda horns one may find on a bull's head!"
        "Humane Hunk":
            me "Humane Hunk."
            $ renpy.block_rollback()
            show Interrogate Grump
            hide InterroSquint
            play sound "audio/soundFX/FX2/pig-grunt.wav"
            with dissolve
            rolf "Correct..."
            rolf "Not my kinda book from the sounds of it."

        "Humongous Hunk":
            $ Failed +=1
            me "Humongous Hunk."
            $ renpy.block_rollback()
            hide InterroSquint
            hide sketches faces
            show Interrogate Hate
            play sound "audio/soundFX/FX2/pig-scream-loud-oink.wav"
            with dissolve
            rolf "Wrong!"
            if Failed == 4 :
                jump badend
            rolf "I've never seen a human worthy of being called \"humongous\" before..."
            rolf "You're all small compared to me!"

    if seenq1==False:
        if Failed == 1 :
            #if HardQuestions == True

            if HardQuestions == False:
                hide InterroSquint
                show Interrogate Smile
                with dissolve
                rolf "That's your first wrong answer!"
                $ seenq1 = True

    if seenq2== False:
        if Failed == 2 :
            if HardQuestions == True:

                scene Interrogate Smile
                with dissolve
                rolf "That's your first wrong answer!"
                show InterroSquint with dissolve
                rolf "Maybe you're not such a good \"assistant\" after all!"
            if HardQuestions == False:

                scene Interrogate Smile
                with dissolve
                rolf "That's another incorrect answer!"
                show InterroSquint with dissolve
                rolf "Maybe you're not such a good \"assistant\" after all!"
            $ seenq2 = True

    if seenq3== False:
        if Failed == 3 :
            if HardQuestions == True:

                scene Interrogate Laugh
                with dissolve
                rolf "Now that's another incorrect answer!"
                show InterroSquint
                show Interrogate Smile
                with dissolve
                rolf "Hehe... Get {u}ONE{/u} more question wrong and you're done for!"
            if HardQuestions == False:

                scene Interrogate Laugh
                with dissolve
                rolf "Now that's yet another incorrect answer!"
                show InterroSquint
                show Interrogate Smile
                with dissolve
                rolf "Hehe... Get {u}ONE{/u} more question wrong and you're done for!"
            $ seenq3 = True

    if Failed == 4 :
        jump badend




label fifthQ:

    scene Interrogate Base
    with dissolve

    rolf "Now here's another visual one!"
    show InterroLookdown with dissolve
    "He looks down at his stack of papers once more and pulls out a wet red crayon. "
    rolf "Sometimes you need a good red to capture a bloody crime scene. This one will be quick to draw!"
    show InterroSquint
    hide InterroLookdown
    with dissolve
    rolf "Which of the following is the city guard symbol!?"
    $ preferences.afm_enable = False
    window hide
    show sketches symbols with dissolve
    hide sketches symbols
    show screen Chapter2Choice3
    $ disableAFMbutton = True
    $ preferences.afm_enable = False
    $ _skipping = False
    $ renpy.pause(hard=True)



label fourthQNr1:
    hide screen Chapter2Choice3
    show sketches symbols
    window show
    me  "The left symbol."
    $ disableAFMbutton = False
    $ _skipping = True
    $ renpy.block_rollback()
    play sound "audio/soundFX/FX2/pig-grunt-double.wav"
    hide sketches symbols with dissolve
    rolf "Indeed! Every damn guard wears one on their chest!"
    hide InterroSquint with dissolve
    rolf "Well... except for me... "
    show Interrogate Smile with dissolve
    rolf "With a thick hide like mine, any added layer of clothing just gets too damn hot in this weather!"
    jump fourthQFinished

label fourthQNr2:
    hide screen Chapter2Choice3
    show sketches symbols
    window show
    me "The middle symbol."
    $ disableAFMbutton = False
    $ _skipping = True
    $ renpy.block_rollback()
    $ Failed +=1
    hide InterroSquint
    hide sketches faces
    show Interrogate Hate
    play sound "audio/soundFX/FX2/pig-squeak.wav"
    with dissolve
    rolf "WRONG!"
    if Failed == 4 :
        jump badend
    rolf "We use that symbol on some of the city banners, but it isn't tied to the army!"
    jump fourthQFinished
label fourthQNr3:
    hide screen Chapter2Choice3
    show sketches symbols
    window show
    me "The symbol to the right."
    $ disableAFMbutton = False
    $ _skipping = True
    $ renpy.block_rollback()
    $ Failed +=1
    hide InterroSquint
    hide sketches faces
    show Interrogate Hate
    play sound "audio/soundFX/FX2/pig-squeak.wav"
    with dissolve
    rolf "WRONG!"
    if Failed == 4 :
        jump badend
    rolf "That's the symbol of the great truffle-sniffing company!"
    jump fourthQFinished

label fourthQFinished:


    if seenq1==False:
        if Failed == 1 :
            #if HardQuestions == True

            if HardQuestions == False:
                hide InterroSquint
                show Interrogate Smile
                with dissolve
                rolf "That's your first wrong answer!"
                $ seenq1 = True

    if seenq2== False:
        if Failed == 2 :
            if HardQuestions == True:

                scene Interrogate Smile
                with dissolve
                rolf "That's your first wrong answer!"
                show InterroSquint with dissolve
                rolf "Maybe you're not such a good \"assistant\" after all!"
            if HardQuestions == False:

                scene Interrogate Smile
                with dissolve
                rolf "That's another incorrect answer!"
                show InterroSquint with dissolve
                rolf "Maybe you're not such a good \"assistant\" after all!"
            $ seenq2 = True

    if seenq3== False:
        if Failed == 3 :
            if HardQuestions == True:

                scene Interrogate Laugh
                with dissolve
                rolf "Now that's another incorrect answer!"
                show InterroSquint
                show Interrogate Smile
                with dissolve
                rolf "Hehe... Get {u}ONE{/u} more question wrong and you're done for!"
            if HardQuestions == False:

                scene Interrogate Laugh
                with dissolve
                rolf "Now that's yet another incorrect answer!"
                show InterroSquint
                show Interrogate Smile
                with dissolve
                rolf "Hehe... Get {u}ONE{/u} more question wrong and you're done for!"
            $ seenq3 = True

    if Failed == 4 :
        jump badend

label sixthQ:


    scene Interrogate Grump
    with dissolve

    rolf "Okay, you're halfway through... {u}FIVE{/u} questions to go!"

    hide InterroSquint
    show Interrogate Smile
    with dissolve
    rolf "What's one of the princess' royal duties?"
    "I think Emelie said something about that!"
    menu:
        with dissolve
        "Hmmm... What's one of the princess' royal duties ?"
        "Attending \"Princess Classes\"":
            me "Attending \"Princess Classes\"."
            $ renpy.block_rollback()
            play sound "audio/soundFX/FX2/pig-grunt.wav"
            show Interrogate Grump with dissolve
            rolf "Hmph, correct again..."
        "Kissing piglets":
            me "Kissing piglets."
            $ renpy.block_rollback()
            $ Failed +=1
            hide InterroSquint
            hide sketches faces
            show Interrogate Hate
            play sound "audio/soundFX/FX2/pig-scream-loud-oink.wav"
            with dissolve
            rolf "Wrong!"
            if Failed == 4 :
                jump badend
            rolf "But a lot of couples do want their piglets kissed for some reason!"
            show Interrogate Grump with dissolve
            rolf "Sometimes a grown hog will ask for a kiss from the queen or princess too..."
            show Interrogate Laugh with dissolve
            rolf" If they can't take no for an answer they'll end up kissing my fist instead! Mwehehe."
            "Rolf seems to enjoy punching things about as much as Billy enjoys eating stuff."
            show Interrogate Base with dissolve
            rolf "One royal duty is to help strengthen the kingdom's unity and stability!"
            show InterroSquint with dissolve
            rolf "Exactly what that means is a bit unclear..."
            rolf "She also needs to attend all her royal classes!"
            rolf "There's a lot to learn if you're going to lead and represent a kingdom as big as ours!"

        "Waving at the public through a window":
            $ Failed +=1
            me "Waving at the public through a window"
            $ renpy.block_rollback()
            hide InterroSquint
            hide sketches faces
            show Interrogate Hate
            play sound "audio/soundFX/FX2/pig-scream-loud-oink.wav"
            with dissolve
            rolf "Wrong! That's just something they do in the stage plays!"
            if Failed == 4 :
                jump badend
            show Interrogate Base with dissolve
            rolf "But I have seen her do it... at least twice."
            show InterroSquint with dissolve
            rolf "One royal duty is to help strengthen the kingdom's unity and stability!"
            rolf "Exactly what that means is a bit unclear..."
            show Interrogate Grump
            hide InterroSquint
            with dissolve
            rolf "She also needs to attend all her royal classes!"
            rolf "There's a lot to learn if you're going to lead and represent a kingdom as big as ours!"

    if seenq1==False:
        if Failed == 1 :
            #if HardQuestions == True

            if HardQuestions == False:
                hide InterroSquint
                show Interrogate Smile
                with dissolve
                rolf "That's your first wrong answer!"
                $ seenq1 = True

    if seenq2== False:
        if Failed == 2 :
            if HardQuestions == True:

                scene Interrogate Smile
                with dissolve
                rolf "That's your first wrong answer!"
                show InterroSquint with dissolve
                rolf "Maybe you're not such a good \"assistant\" after all!"
            if HardQuestions == False:

                scene Interrogate Smile
                with dissolve
                rolf "That's another incorrect answer!"
                show InterroSquint with dissolve
                rolf "Maybe you're not such a good \"assistant\" after all!"
            $ seenq2 = True

    if seenq3== False:
        if Failed == 3 :
            if HardQuestions == True:

                scene Interrogate Laugh
                with dissolve
                rolf "Now that's another incorrect answer!"
                show InterroSquint
                show Interrogate Smile
                with dissolve
                rolf "Hehe... Get {u}ONE{/u} more question wrong and you're done for!"
            if HardQuestions == False:

                scene Interrogate Laugh
                with dissolve
                rolf "Now that's yet another incorrect answer!"
                show InterroSquint
                show Interrogate Smile
                with dissolve
                rolf "Hehe... Get {u}ONE{/u} more question wrong and you're done for!"
            $ seenq3 = True

    if Failed == 4 :
        jump badend


    show blackopacity
    if cumface== True:
        show Wardrobem Empty
    else:
        show Wardrobem Angry


    with dissolve
    emelie "I hate those damn royal classes!"

    rolf "Don't interrupt or I'll have to disqualify him!"
    emelie "Sorry!"
    hide blackopacity
    hide Wardrobem
    with dissolve
    scene Interrogate Grump
    show InterroSide
    with dissolve
    rolf "But I don't blame you for disliking 'em, princess!"
    show InterroSquintSide
    show Interrogate Grump
    with dissolve
    rolf "That old hag of a hog Helga gets crankier and crankier every year, and she was cranky enough forty years ago when I was in school! "






label seventhQ:
    scene Interrogate Base
    show InterroLookdown
    with dissolve
    rolf "So..."
    "He quickly sketches onto a new piece of paper."
    hide InterroLookdown with dissolve
    show sketches fountains with dissolve
    rolf "What does the fountain outside this building we're in look like?!"
    "Hmm... Me and Billy spent a fair bit of time out there talking about the helmet plan!"
    $ preferences.afm_enable = False

    window hide
    hide sketches fountains
    show screen Chapter2Choice4
    $ _skipping = False
    $ disableAFMbutton = True
    $ preferences.afm_enable = False
    $ renpy.pause(hard=True)



label fifthQNr1:
    hide screen Chapter2Choice4
    show sketches fountains
    window show
    me  "The left fountain."
    $ disableAFMbutton = False
    $ _skipping = True
    $ renpy.block_rollback()
    $ Failed +=1
    hide sketches
    hide InterroSquint
    show Interrogate Hate
    play sound "audio/soundFX/FX2/pig-squeak.wav"
    with dissolve
    rolf "INCORRECT! That fountain is by the chapel!"
    if Failed == 4 :
        jump badend
    "Shit! They look pretty similar!"
    rolf "But out of the three fountains, it's definitely my favorite!"
    jump fifthQFinished

label fifthQNr2:
    hide screen Chapter2Choice4
    show sketches fountains
    window show
    me "The middle fountain."
    $ disableAFMbutton = False
    $ _skipping = True
    $ renpy.block_rollback()
    hide sketches
    show Interrogate Base
    show InterroSquint
    play sound "audio/soundFX/FX2/pig-grunt-double.wav"
    with dissolve
    rolf "Correct."
    hide InterroSquint with dissolve
    rolf" Our great savior Särimner who made the ultimate sacrifice for all of pigkind!"
    show Interrogate Grump with dissolve
    rolf "Or that's the story at least. It's hundreds of years old by now and makes some outrageous claims. "
    show InterroSquint with dissolve
    rolf "I only believe what I can confirm to be true! "
    hide InterroSquint
    show Interrogate Smile
    with dissolve
    rolf" And you've got some more work to do to convince me you're some damn assistant!"
    jump fifthQFinished

label fifthQNr3:
    hide screen Chapter2Choice4
    show sketches fountains
    window show
    me "The fountain to the right."
    $ disableAFMbutton = False
    $ _skipping = True
    $ renpy.block_rollback()
    $ Failed +=1
    hide InterroSquint
    hide sketches
    show Interrogate Hate
    play sound "audio/soundFX/FX2/pig-squeak.wav"
    with dissolve
    rolf "No! Wrong! That's just the most vile thing I could think of to draw!"
    if Failed == 4 :
        jump badend
    rolf "A pig with rows of nipples? I'm going to be sick! Maybe that's what you humans are hiding under your damn shirts!"
    me "...I only picked it because I didn't think you'd be weird enough to imagine such a thing!"
    show Interrogate Grump
    show InterroLookSide
    with dissolve
    rolf "..."
    "He quickly scrunches the paper up and puts it into his pocket "
    hide InterroLookSide
    show InterroSquint
    with dissolve
    rolf "You better forget what you saw and I'll do the same."
    jump fifthQFinished

label fifthQFinished:
    hide screen Chapter2Choice4

    if seenq1==False:
        if Failed == 1 :
            #if HardQuestions == True

            if HardQuestions == False:
                hide InterroSquint
                show Interrogate Smile
                with dissolve
                rolf "That's your first wrong answer!"
                $ seenq1 = True

    if seenq2== False:
        if Failed == 2 :
            if HardQuestions == True:

                scene Interrogate Smile
                with dissolve
                rolf "That's your first wrong answer!"
                show InterroSquint with dissolve
                rolf "Maybe you're not such a good \"assistant\" after all!"
            if HardQuestions == False:

                scene Interrogate Smile
                with dissolve
                rolf "That's another incorrect answer!"
                show InterroSquint with dissolve
                rolf "Maybe you're not such a good \"assistant\" after all!"
            $ seenq2 = True

    if seenq3== False:
        if Failed == 3 :
            if HardQuestions == True:

                scene Interrogate Laugh
                with dissolve
                rolf "Now that's another incorrect answer!"
                show InterroSquint
                show Interrogate Smile
                with dissolve
                rolf "Hehe... Get {u}ONE{/u} more question wrong and you're done for!"
            if HardQuestions == False:

                scene Interrogate Laugh
                with dissolve
                rolf "Now that's yet another incorrect answer!"
                show InterroSquint
                show Interrogate Smile
                with dissolve
                rolf "Hehe... Get {u}ONE{/u} more question wrong and you're done for!"
            $ seenq3 = True

    if Failed == 4 :
        jump badend





label eightQ:
    scene Interrogate Base
    show InterroSquint
    with dissolve
    rolf "Now get ready for the next question!"
    hide InterroSquint with dissolve
    rolf "My nephew is one of Emelie's favorite royal guards... so you should know some things about him!"
    rolf "What's his favorite vegetable?"
    "I can remember a few coming up in conversation!"
    menu:
        with dissolve
        "What's Billy's favorite vegetable?"
        "Cucumbers":
            me "Cucumbers."
            $ renpy.block_rollback()
            $ Failed +=1
            hide InterroSquint
            hide sketches faces
            show Interrogate Hate
            play sound "audio/soundFX/FX2/pig-scream-loud-oink.wav"
            with dissolve
            rolf "Wrong!"
            if Failed == 4 :
                jump badend
            rolf "Billy loves cucumbers, and especially the sound of biting into crispy ones, but they're not his favorites!"
        "Carrots":
            me "Carrots."
            $ renpy.block_rollback()
            play sound "audio/soundFX/FX2/pig-grunt.wav"
            show InterroSquint with dissolve
            rolf "Correct!"
            hide InterroSquint
            show Interrogate Laugh
            show InterroTongue
            with dissolve
            rolf "Carrot cake is his favorite thing, so carrots end up being his favorite vegetable!"
            show Interrogate Grump
            hide InterroSquint
            hide InterroTongue
            with dissolve
            rolf "... He never shuts up about food."


        "Apples":
            me "Apples."
            $ renpy.block_rollback()
            $ Failed +=1
            hide InterroSquint
            hide sketches faces
            show Interrogate Hate
            play sound "audio/soundFX/FX2/pig-scream-loud-oink.wav"
            with dissolve
            rolf "That's a fruit, stupid! Wrong!"
            if Failed == 4 :
                jump badend
            rolf "But you're right in that Billy loves apples... Specifically apple juice on a warm summer day."

    if seenq1==False:
        if Failed == 1 :
            #if HardQuestions == True

            if HardQuestions == False:
                hide InterroSquint
                show Interrogate Smile
                with dissolve
                rolf "That's your first wrong answer!"
                $ seenq1 = True

    if seenq2== False:
        if Failed == 2 :
            if HardQuestions == True:

                scene Interrogate Smile
                with dissolve
                rolf "That's your first wrong answer!"
                show InterroSquint with dissolve
                rolf "Maybe you're not such a good \"assistant\" after all!"
            if HardQuestions == False:

                scene Interrogate Smile
                with dissolve
                rolf "That's another incorrect answer!"
                show InterroSquint with dissolve
                rolf "Maybe you're not such a good \"assistant\" after all!"
            $ seenq2 = True

    if seenq3== False:
        if Failed == 3 :
            if HardQuestions == True:

                scene Interrogate Laugh
                with dissolve
                rolf "Now that's another incorrect answer!"
                show InterroSquint
                show Interrogate Smile
                with dissolve
                rolf "Hehe... Get {u}ONE{/u} more question wrong and you're done for!"
            if HardQuestions == False:

                scene Interrogate Laugh
                with dissolve
                rolf "Now that's yet another incorrect answer!"
                show InterroSquint
                show Interrogate Smile
                with dissolve
                rolf "Hehe... Get {u}ONE{/u} more question wrong and you're done for!"
            $ seenq3 = True

    if Failed == 4 :
        jump badend




label ninthQ:
    scene Interrogate Base
    show InterroLookdown
    with dissolve
    rolf "Now... The last visual question!"
    rolf "As an assistant, you must've gotten used to running in and out through the door to this room... "
    show Interrogate Base
    hide InterroLookdown
    show InterroSquint
    with dissolve
    show sketches door with dissolve
    rolf "So which symbol is on the princess' door?!"
    $ preferences.afm_enable = False
    window hide
    hide sketches door
    show screen Chapter2Choice5
    $ disableAFMbutton = True

    $ _skipping = False
    $ renpy.pause(hard=True)



label sixthQNr1:
    hide screen Chapter2Choice5
    show sketches door
    window show
    me  "The left door symbol."
    $ disableAFMbutton = False
    $ _skipping = True
    $ renpy.block_rollback()
    hide sketches
    show InterroSquint
    play sound "audio/soundFX/FX2/pig-grunt-double.wav"
    with dissolve
    rolf "Yes! The golden crown!"
    rolf "Gave it a real good punch to get the damn door open!"
    jump sixthQFinished


label sixthQNr2:
    hide screen Chapter2Choice5
    show sketches door
    window show
    me "The middle door symbol."
    $ disableAFMbutton = False
    $ _skipping = True
    $ renpy.block_rollback()
    $ Failed +=1
    hide InterroSquint
    hide InterroLookdown
    hide sketches faces
    show Interrogate Hate
    play sound "audio/soundFX/FX2/pig-squeak.wav"
    with dissolve
    rolf "WRONG! I just made that one up!"
    if Failed == 4 :
        jump badend
    jump sixthQFinished

label sixthQNr3:
    hide screen Chapter2Choice5
    show sketches door
    window show
    me "The door symbol to the right."
    $ disableAFMbutton = False
    $ _skipping = True
    $ renpy.block_rollback()
    $ Failed +=1
    hide InterroSquint
    hide InterroLookdown
    hide sketches faces
    show Interrogate Hate
    play sound "audio/soundFX/FX2/pig-squeak.wav"
    with dissolve
    rolf "INCORRECT! "
    if Failed == 4 :
        jump badend
    rolf "That's just the army symbol with some balls at the ends!"
    jump sixthQFinished

label sixthQFinished:
    hide screen Chapter2Choice5
    hide sketches door
    with dissolve


    if seenq1==False:
        if Failed == 1 :
            #if HardQuestions == True

            if HardQuestions == False:
                hide InterroSquint
                show Interrogate Smile
                with dissolve
                rolf "That's your first wrong answer!"
                $ seenq1 = True

    if seenq2== False:
        if Failed == 2 :
            if HardQuestions == True:

                scene Interrogate Smile
                with dissolve
                rolf "That's your first wrong answer!"
                show InterroSquint with dissolve
                rolf "Maybe you're not such a good \"assistant\" after all!"
            if HardQuestions == False:

                scene Interrogate Smile
                with dissolve
                rolf "That's another incorrect answer!"
                show InterroSquint with dissolve
                rolf "Maybe you're not such a good \"assistant\" after all!"
            $ seenq2 = True

    if seenq3== False:
        if Failed == 3 :
            if HardQuestions == True:

                scene Interrogate Laugh
                with dissolve
                rolf "Now that's another incorrect answer!"
                show InterroSquint
                show Interrogate Smile
                with dissolve
                rolf "Hehe... Get the final question wrong and you're done for!"
            if HardQuestions == False:

                scene Interrogate Laugh
                with dissolve
                rolf "Now that's yet another incorrect answer!"
                show InterroSquint
                show Interrogate Smile
                with dissolve
                rolf "Hehe... Get the final question wrong and you're done for!"
            $ seenq3 = True

    if Failed == 4 :
        jump badend

    scene Interrogate Base
    show InterroSquint
    with dissolve

    rolf "Now..."

label tenthQ:
    hide InterroLookdown
    hide InterroSquint
    show Interrogate Hateh
    with dissolve
    if HardQuestions == True :
        if Failed == 1 :
            rolf "You might think you've got a shot at a perfect score! "
            rolf "But you have one last question ahead of you!"

    if HardQuestions == False :
        if Failed == 0 :
            rolf "You might think you've got a shot at a perfect score! "
            rolf "But you have one last question ahead of you!"

    if Failed == 2 :
            rolf "As expected you haven't answered all my questions correctly!"
            rolf "AND THIS FINAL QUESTION WILL SURELY PUT YOUR KNOWLEDGE TO THE TEST!"

    if Failed == 3 :
            rolf "You're in some deep shit!"
            rolf "AT THE MERCY OF THIS FINAL QUESTION!"
    show Interrogate Hate with dissolve
    rolf "THE HARDEST ONE OF THEM ALL!"
    "Oh crap!"
    show Interrogate Mega with dissolve
    rolf "HOW DO YOU SPELL THE PRINCESS' NAME?!"

    menu:
        with dissolve
        "How's the princess' name spelled?!"
        "E.M.I.L.Y":
            me "E.M.I.L.Y"
            $ renpy.block_rollback()
            $ Failed +=1
            rolf "..."
            play sound "audio/soundFX/FX2/pig-scream-loud-oink.wav"
            rolf "WROOONG!!"
            if Failed == 4 :
                jump badend
            else:
                rolf"..."
                stop music fadeout 0.6
                show Interrogate Base with dissolve
                rolf "But that's to be expected on that question..."
                jump passquestions


        "E.M.I.L.I.E":
            me "E.M.I.L.I.E"
            $ renpy.block_rollback()
            $ Failed +=1
            rolf "..."
            play sound "audio/soundFX/FX2/pig-scream-loud-oink.wav"
            rolf "WROOONG!!"
            if Failed == 4 :
                jump badend
            else:
                rolf"..."
                stop music fadeout 0.6
                show Interrogate Base with dissolve
                rolf "But that's to be expected on that question..."
                jump passquestions




        "E.M.E.L.I.E":
            me "E.M.E.L.I.E"
            $ renpy.block_rollback()
            rolf "!!!"
            play sound "audio/soundFX/FX2/pig-grunt.wav"
            show Interrogate Grump with dissolve
            stop music fadeout 0.6
            rolf "Yes."
            jump passquestions
            #tense music stops here



label badend:
    scene Interrogate Mega with dissolve
    show blackshake at truecenter behind Interrogate
    play sound "audio/soundFX/FX2/monster-shriek1.wav"
    with hpunch
    rolf "I knew you were no damn assistant!"
    "Crap! I failed!"
    me "I can explain--"
    rolf "That time is over!"
    window hide
    show blackopacity
    show Wardrobe
    with dissolve
    window show
    emelie "Rolf, don't!"
    window hide
    hide blackopacity
    hide Wardrobe
    with dissolve
    show Interrogate Grump
    show InterroSquintSide
    with dissolve
    window show
    rolf "Fine, princess...I'll go easy on him for ya..."
    window hide

    hide InterroSquintSide
    with dissolve
    $ renpy.pause(0.2, hard=True)
    show Interrogate Mega with dissolve
    play sound "audio/soundFX/FX2/monster-shriek2.wav"
    $ renpy.pause(0.2, hard=True)
    show Interrogate Mega:
        zoom 1.0
        linear 0.3 zoom 1.8 yalign 0.5
    $ renpy.pause(0.1, hard=True)
    with vpunch
    with hpunch
    stop music fadeout 0.1
    show red with dissolve
    play sound "audio/soundFX/FX2/3-punch.wav"
    pause 0.5
    scene black with dissolve

    pause 0.5
    window show
    pause 0.5
    "....."
    "..."
    "Ugh..."
    "..."
    "My head's spinning..."
    "I'm lying on... grass?"
    window hide
    play music "audio/Birds.wav" fadein 4.0 volume 0.5

    show bg castle with dissolve
    pause 0.5
    window show
    "Shit."
    "I'm back at the farm... The castle is once again so far away..."
    "On shaky legs, I walk down toward my land."
    window hide
    scene bg hill with fade
    pause 1.0
    window show
    "Well..."
    "At least my back's better now."
    window hide
    show blackopacity
    show carriage
    with dissolve
    window show
    "And hey, my cart's still full!"
    "Guess I'll have to get back to work..."
    scene black with fade
    "But I'll miss her."
    stop music fadeout 1.0
    pause 0.3
    scene endscreen with dissolve


    menu:
        with dissolve

        "{u}{color=#E20018} {b}END.{/color}{/b}{/u}"


        " Retry interrogation!":
            pause 0.5
            $ renpy.block_rollback()
            window hide
            play music "audio/1.+Grundar+-+320bit.mp3" fadein 0.1 volume 0.7
            jump interrogation





label passquestions:
    $ perfscore = False
    window hide
    scene black with fade
    if HardQuestions == True :
        if Failed == 1 :
            play sound "audio/soundFX/FX2/dat-s-right.wav"
            window show
            "I got them all right!"
            $ perfscore = True

    if HardQuestions == False :
        if Failed == 0 :
            play sound "audio/soundFX/FX2/dat-s-right.wav"
            window show
            "I got them all right!"
            $ perfscore = True

    window hide

    scene bg emelieroom
    play music "audio/Tavern+Brawl+-+320bit.mp3" fadein 5.0 volume 0.2
    show EmelieRoomDoor
    show rolf pout at right:
        zoom 1.2 yalign 0.35 xalign 1.50
    with fade
    pause 0.3
    show rolf pout at right:
        zoom 1.2 yalign 0.35 xalign 1.50
        linear 0.5 zoom 1.0 yalign 0.35 xalign 1.50
    pause 0.5


    if HardQuestions == True :
        if Failed == 1 :
            window show
            rolf "Ghrrr!"
            "Rolf lets out a guttural grunt. He sounds pissed!"
            show rolf knuckles at right with dissolve:
                zoom 1.0 yalign 0.35 xalign 1.50
            rolf "I can't believe you got a perfect score!"
            rolf"..."
            show rolf concern at right with dissolve:
                zoom 1.0 yalign 0.35 xalign 1.50
            rolf "Maybe you really are the best assistant in the world..."
        else :
            window show
            rolf "..."
            rolf "Hmmm... You got most of my questions right."
            show rolf concern at right with dissolve:
                zoom 1.0 yalign 0.35 xalign 1.50
            rolf "Maybe you really are an assistant after all..."

    if HardQuestions == False :
        if Failed == 0 :
            window show
            rolf "Ghrrr!"
            "Rolf lets out a guttural grunt. He sounds pissed!"
            show rolf knuckles at right with dissolve:
                zoom 1.0 yalign 0.35 xalign 1.50
            rolf "I can't believe you got a perfect score!"
            rolf"..."
            show rolf concern at right with dissolve:
                zoom 1.0 yalign 0.35 xalign 1.50
            rolf "Maybe you really are the best assistant in the world..."
        else :
            window show
            rolf "..."
            rolf "Hmmm... You got most of my questions right."
            show rolf concern at right with dissolve:
                zoom 1.0 yalign 0.35 xalign 1.50
            rolf "Maybe you really are an assistant after all..."

    me "I sure am!"


    "He scuffs and looks to the wardrobe, suddenly speaking in a much gentler tone."
    show rolf apologetic
    show roleye apologeticside at right:
        zoom 1.0 yalign 0.35 xalign 1.50
    with dissolve
    rolf "Emelie, I'm very sorry I yelled at you! "
    rolf "I just wanted to make sure you're safe! "
    emelie "I get it... But now you have to clean your mess up!"
    rolf "Yes, princess!"
    hide roleye
    show rolf belly
    with dissolve
    rolf "..."
    rolf" Guess I have to go get this damn door fixed ..."
    show rolf knuckles
    show roleye lookside at right:
        zoom 1.0 yalign 0.35 xalign 1.50
    with dissolve
    rolf "Hey nephew! "
    play sound "audio/soundFX/run2.wav"
    show billy ko at left:
        yalign -3. xalign -2.0
        linear 0.3 yalign -1.7 xalign -0.7
    billy "Y-yes??"
    show rolf pout
    show roleye lookside
    with dissolve
    rolf "Follow along to the smithy!"
    rolf "Might as well straighten that helmet out while we grab some new hinges for the door."

    billy "Good idea, uncle!"
    window hide
    hide roleye
    hide rolf base
    with easeoutright
    pause 0.3
    hide EmelieRoomDoor with dissolve
    pause 0.2
    window show
    "Rolf carries the broken door out without acknowledging me."
    show billy ko at left:
        yalign -1.7 xalign -0.7
        linear 0.3 yalign -0.0 xalign -0.0
    billy "I'll come see you again later, buddy!"
    show billy kohappy with dissolve
    billy "You did good!"
    me "Thanks for having my back, Billy!"
    me "And good luck with the helmet!"
    "I give Billy a wave as he hurries out to catch up with Rolf."
    window hide
    play sound "audio/soundFX/Run.mp3"
    hide billy with easeoutleft
    pause 1.5
    window show
    me "..."
    pause 0.3
    "I listen carefully as their footsteps fade out into the hallway."
    me "I think we're clear!"
    window hide
    show blackopacity
    if cumface== True:
        show Wardrobem Cum
    else:
        show Wardrobem Clean

    with dissolve
    pause 0.4
    window show
    emelie "Are they gone? Are you okay?"
    emelie "That was close!"
    emelie "I'm sorry I couldn't be of more help!"
    emelie "I tried finding some decent clean clothes but I've been lazy with my laundry now that my parents are away!"
    window hide
    hide blackopacity
    hide Wardrobem Cum
    hide Wardrobem Clean
    with dissolve


    show em oilhole at right:
        yalign 0.15
        zoom 1.0

    show emf concern at right:
        yalign 0.15
        zoom 1.0
    show emear high at right:
        yalign 0.15
        zoom 1.0
    if cumface == True:
        show Emoil barefacial at right:
            yalign 0.15
            zoom 1.0
    if cumface == False:
        show Emoil cum at right:
            yalign 0.15
            zoom 1.0
    with easeinleft
    window show
    emelie "And y'know it was really dark back there!"
    emelie "I've got a fear of the dark so I was freaking out a bit!"

    me "YOU were freaking out?!"
    me "I'm pretty sure I almost got my head chopped off!"
    show emf laugh with dissolve
    emelie "Haha, I sound pretty silly when you put it like that!"
    show emf insecure with dissolve
    emelie "But I really was freaking out... I got really worried for you."
    show emf fluster
    show emeye scared at right:
        yalign 0.15
        zoom 1.0
    with dissolve
    emelie "Now, we can't stay here much longer without a door!"
    emelie "Anyone who walks by could see us and I'm still a dripping mess!"
    hide emeye
    show emf concern
    with dissolve
    emelie "The bath is just down the hall and to the left, let's go quickly before anyone comes by!"
    window hide

    stop music fadeout 2.0
    scene black with fade
    show Wardrobem Thumb behind black
    show Wardrobem Cum behind black
    show Wardrobem Clean behind black
    show Wardrobem Angry behind black
    jump Bath

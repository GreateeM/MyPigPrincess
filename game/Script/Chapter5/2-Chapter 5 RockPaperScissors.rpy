label RPSS:

    window hide
    show black with fade
    stop music fadeout 1.0
    window show
    " I wave Bronwen goodbye and follow Rolf outside."
    play music "audio/birds.wav" fadein 0.1 volume 0.5
    window hide
    scene tailorsmith
    show blackshake at truecenter behind tailorsmith
    show rolf base at right:
        zoom 0.95 yalign 0.25 xalign 1.50
    show rol pout at right:
        zoom 0.95 yalign 0.25 xalign 1.50
    with fade
    window show
    rolf "Hmpf... "
    if liename == True:

        rolf "Hey, \" [lie_name] \"..."
    else:
        rolf "Hey, twerp..."

    show rolf think2
    hide rol
    with dissolve
    rolf "... Maybe you're not THAT bad of an assistant after all..."
    rolf " If you're being this generous with my daughter."
    me " I, uuh..."
    me " Thanks?"

    show rolf base with dissolve
    rolf " I can't remember the last time she took a day off. Probably on my last birthday."
    " Hearing that makes me think I got ripped off big time..."
    me " Well... Good work deserves a generous tip!"
    show rol pout2 at right:
        zoom 0.95 yalign 0.25 xalign 1.50
    with dissolve
    rolf " That might be the first thing the two of us agree on."
    show rol pout
    show rolf belly
    with dissolve
    rolf " ... Hmm..."
    " Rolf squints at me as if he's pondering something."
    show rolf calm
    show rol closed

    with dissolve
    rolf " Let me check something real quick..."
    show rol pout
    show roleye lookside2 at right:
        zoom 0.95 yalign 0.25 xalign 1.50
    with dissolve
    rolf " Ya heard of rock, paper, scissors?"




    me " Of course."
    show roleye squint at right:
        zoom 0.95 yalign 0.25 xalign 1.50

    show rol base at right:
        zoom 0.95 yalign 0.25 xalign 1.50

    with dissolve
    rolf " Let's do a round. "
    me " ...Really?"

    show rolf angryy
    hide roleye
    hide rol
    with dissolve
    rolf " One round only! I need to confirm something."
    window hide
    show rolf fist with dissolve
    pause 0.2
    stop music fadeout 1.0
    play sound "audio/soundFX/Step1.wav"
    #play music "audio/7.+Stöðvar+-+320bit.mp3" fadein 0.1 volume 0.7
    play music "audio/1.+Grundar+-+320bit.mp3" fadein 0.1 volume 0.7
    show rolf fist at right:
        linear 0.4 zoom 1.2 yalign 0.30 xalign 2.20
    with vpunch
    pause 0.8
    scene rpsbg with fade
    show blackshake at truecenter behind rpsbg
    window show
    " Rolf steps up and moves his fist forward."
    window hide
    show rpsrolf rock with easeinright
    pause 0.4
    window show
    "...I should probably just roll with this."
    me" Okay."
    window hide
    show rpsprotag rock with easeinleft
    pause 0.4
    window show
    "...Fuckin' hell."
    " Seeing his fist next to mine makes me self-conscious..."
    window hide
    show Interrogate Grump with fade
    pause 1.0
    window show
    rolf " Now before we start... We'll reveal our move on the fourth shake of the fist. "
    rolf "Rock-Paper-Scissors-Reveal. "
    show Interrogate Base with dissolve
    rolf "Got it?"
    show InterroSquint with dissolve
    rolf " Don't open your fist when you say \"scissors\"! "
    show InterroSquintSide
    show Interrogate Grump
    with dissolve
    rolf "Wait for the movement after! "
    me " Okay okay, sure."
    " He's very particular about the rules..."

    "Oh well, a silly game could be a bit of fun."
    window hide
    show InterroLookdown
    show Interrogate Base
    with dissolve
    pause 0.2

    hide Interrogate Base
    hide InterroLookdown
    hide InterroSquint
    hide InterroSquintSide
    with fade
    window show
    "He said we're only doing one round... So it's all about the opener!"
    "Hmm, what should I pick?"
    #"Rolf opens paper"
    #"Rolf then does scissors or paper"
    #"Rolf then does a random move if you tie."

    window hide
    show darkenbehindall with dissolve
    jump showingRPSChoice1

label showingRPSChoice1:
    show screen RPSChoice1 with dissolve
    $ renpy.pause(hard=True)
    jump showingRPSChoice1

screen RPSChoice1:

    add "gui/RPS/whobeatswho.png"

    imagebutton:
        idle "gui/RPS/paperidle.png"
        hover "gui/RPS/paperhover.png"
        focus_mask True
        activate_sound "audio/UIsounds/cluck.wav"
        hover_sound "audio/UIsounds/hover.wav"
        mouse "hover"
        action Show(screen="RPSConfirm1", transition=dissolve, RPSChosen="Paper")

    imagebutton:
        idle "gui/RPS/rockidle.png"
        hover "gui/RPS/rockhover.png"
        focus_mask True
        activate_sound "audio/UIsounds/cluck.wav"
        hover_sound "audio/UIsounds/hover.wav"
        mouse "hover"
        action Show(screen="RPSConfirm1", transition=dissolve, RPSChosen="Rock")

    imagebutton:
        idle "gui/RPS/scissorsidle.png"
        hover "gui/RPS/scissorshover.png"
        focus_mask True
        activate_sound "audio/UIsounds/cluck.wav"
        hover_sound "audio/UIsounds/hover.wav"
        mouse "hover"
        action Show(screen="RPSConfirm1", transition=dissolve, RPSChosen="Scissors")

screen RPSConfirm1(RPSChosen):
    modal True

    add "gui/RPS/" + RPSChosen + "chosen.png"

    imagebutton:
        idle "gui/RPS/rpsyesidle.png"
        hover "gui/RPS/rpsyeshover.png"
        focus_mask True
        activate_sound "audio/UIsounds/cluck.wav"
        hover_sound "audio/UIsounds/hover.wav"
        mouse "hover"
        action Hide("RPSConfirm1", transition=Dissolve(0.5)), Hide("RPSChoice1", transition=Dissolve(0.5)), Jump("RPSS1" + RPSChosen)

    imagebutton:
        idle "gui/RPS/rpsnoidle.png"
        hover "gui/RPS/rpsnohover.png"
        focus_mask True
        activate_sound "audio/UIsounds/cluck.wav"
        hover_sound "audio/UIsounds/hover.wav"
        mouse "hover"
        action Hide("RPSConfirm1")

label RPSS1Rock:

    with dissolve


    $ renpy.block_rollback()
    $ RPS = "Rock"

    hide darkenbehindall with dissolve
    hide rpsrolf
    hide rpsprotag
    show fists
    window show
    show fists:
        yoffset 0
        linear 0.3 yoffset -20
        yoffset -20
        linear 0.1 yoffset 20

    me "{size=50} ROCK!{/size}{w=0.7}{nw}"

    show fists:
        yoffset 20
        linear 0.3 yoffset -20
        yoffset -20
        linear 0.1 yoffset 20

    rolf " {size=60}PAPER!{/size}{w=0.7}{nw}"

    show fists:
        yoffset 20
        linear 0.3 yoffset -20
        yoffset -20
        linear 0.1 yoffset 20

    me "{size=70}SCISSORS!{/size}{w=0.7}{nw}"
    window hide
    show fists:
        yoffset 20
        linear 0.3 yoffset -30
        yoffset -30
        linear 0.1 yoffset 25

    pause 0.6
    play sound "audio/soundFX/Get.mp3"
    hide fists
    show rpsrolf paper:
        yoffset 25
    show rpsprotag rock:
        yoffset 25
    with dissolve

    with hpunch
    pause 0.8
    window show
    "!!"
    "Shit!"
    " I lost!"
    window hide
    show Interrogate Smile
    show InterroLookdown
    with fade
    stop music fadeout 1.5
    play sound "audio/soundFX/FX2/pig-grunt-double.wav"
    play music "audio/birds.wav" fadein 1.0 volume 0.2
    with vpunch
    hide InterroLookdown with dissolve
    window show
    rolf " Heh... That's what I thought..."
    me " Fine, ya got me. "
    me "Good win."
    $ playbestof3 = False
    show Interrogate Laugh with dissolve
    rolf " This has nothing to do with winning or losing!"
    rolf "I knew you were weak!"
    rolf " And this just reaffirmed it!"
    me " ...What? "
    show Interrogate Smile
    show InterroSquint
    with dissolve
    rolf " Rock, paper, scissors can tell you a lot about a man!"
    " Rolf looks smug and full of himself."
    jump RPSSAfter

label RPSS1Paper:

    with dissolve

    $ renpy.block_rollback()
    $ RPS = "Paper"
    hide darkenbehindall with dissolve
    hide rpsrolf
    hide rpsprotag
    show fists
    window show
    show fists:
        yoffset 0
        linear 0.3 yoffset -20
        yoffset -20
        linear 0.1 yoffset 20

    me "{size=50} ROCK!{/size}{w=0.7}{nw}"

    show fists:
        yoffset 20
        linear 0.3 yoffset -20
        yoffset -20
        linear 0.1 yoffset 20

    rolf " {size=60}PAPER!{/size}{w=0.7}{nw}"

    show fists:
        yoffset 20
        linear 0.3 yoffset -20
        yoffset -20
        linear 0.1 yoffset 20

    me "{size=70}SCISSORS!{/size}{w=0.7}{nw}"
    window hide
    show fists:
        yoffset 20
        linear 0.3 yoffset -30
        yoffset -30
        linear 0.1 yoffset 25

    pause 0.6
    play sound "audio/soundFX/Get.mp3"
    hide fists
    show rpsrolf paper:
        yoffset 25
    show rpsprotag paper:
        yoffset 25
    with dissolve

    with hpunch
    pause 0.8
    window show
    "!!"
    " A tie!"
    hide Interrogate
    window hide

    show Interrogate What
    with fade

    stop music fadeout 1.5
    play sound "audio/soundFX/FX2/pig-grunt-4-96khz.wav"
    play music "audio/birds.wav" fadein 1.0 volume 0.2
    with vpunch
    window show

    rolf "Hmm!?"
    me " I guess we'll go again to settle the tie."
    show Interrogate Grr with dissolve
    rolf "{alpha=*0.80}{size=-4}Hmppf, I can't believe it...{/alpha}{/size}"
    rolf " {alpha=*0.80}{size=-4}This doesn't make any sense...{/alpha}{/size}"
    me " ...What? "
    me " Were you that confident about winning with your opener?"
    show Interrogate Hateh with dissolve
    rolf " This has nothing to do with winning or losing!"
    rolf " Rock, paper, scissors can tell you a lot about a man!"
    " Rolf looks pissed."
    jump RPSSAfter

label RPSS1Scissors:

    with dissolve

    $ renpy.block_rollback()
    $ RPS = "Scissors"
    hide darkenbehindall with dissolve
    hide rpsrolf
    hide rpsprotag
    show fists
    window show
    show fists:
        yoffset 0
        linear 0.3 yoffset -20
        yoffset -20
        linear 0.1 yoffset 20

    me "{size=50} ROCK!{/size}{w=0.7}{nw}"

    show fists:
        yoffset 20
        linear 0.3 yoffset -20
        yoffset -20
        linear 0.1 yoffset 20

    rolf " {size=60}PAPER!{/size}{w=0.7}{nw}"

    show fists:
        yoffset 20
        linear 0.3 yoffset -20
        yoffset -20
        linear 0.1 yoffset 20

    me "{size=70}SCISSORS!{/size}{w=0.7}{nw}"
    window hide
    show fists:
        yoffset 20
        linear 0.3 yoffset -30
        yoffset -30
        linear 0.1 yoffset 25

    pause 0.6
    play sound "audio/soundFX/Get.mp3"
    hide fists
    show rpsrolf paper:
        yoffset 25
    show rpsprotag scissors:
        yoffset 25
    with dissolve

    with hpunch
    pause 0.8
    window show
    "!!"
    " I won!!!"
    window hide
    show Interrogate Base
    show InterroSquint
    show InterroLookdown
    with fade
    stop music fadeout 1.5
    play sound "audio/soundFX/FX2/pig-grunt-5-deep-96khz.wav"
    play music "audio/birds.wav" fadein 1.0 volume 0.2
    with vpunch
    hide InterroLookdown with dissolve

    window show
    rolf "Interesting... I took you for a rock-thrower..."
    me " ...?"
    "Rolf seemed to care a lot about this competition before we started..."
    "But for some reason, he took the loss like it was nothing."
    me "So do I... get anything from winning?"
    hide InterroSquint
    show Interrogate Grump
    with dissolve
    rolf " Hmpf."
    rolf " Rock, paper, scissors has nothing to do with winning or losing!"
    show Interrogate Hateh with dissolve
    rolf " It's a game that tells you a lot about a man's character!"
    jump RPSSAfter

label RPSSAfter:
    window hide
    show black with fade
    window show
    "He takes a step back."
    stop music fadeout 2.0
    window hide
    scene tailorsmith
    show blackshake at truecenter behind tailorsmith
    if RPS == "Paper":
        show rolf angryy at right:
            zoom 1.2 yalign 0.30 xalign 2.20

        with fade
        pause 0.2
        play sound "audio/soundFX/Step1.wav"
        show rolf angryy at right:
            linear 0.5 zoom 0.95 yalign 0.25 xalign 1.50
        pause 0.5
        show rolf angryy at right:
            zoom 0.95 yalign 0.25 xalign 1.50
    if RPS == "Scissors":
        show rolf pout at right:
            zoom 1.2 yalign 0.30 xalign 2.20

        with fade
        pause 0.2
        play sound "audio/soundFX/Step1.wav"
        show rolf pout at right:
            linear 0.5 zoom 0.95 yalign 0.25 xalign 1.50
        pause 0.5
        show rolf pout at right:
            zoom 0.95 yalign 0.25 xalign 1.50
    if RPS == "Rock":
        show rolf heh at right:
            zoom 1.2 yalign 0.30 xalign 2.20

        with fade
        pause 0.2
        play sound "audio/soundFX/Step1.wav"
        show rolf heh at right:
            linear 0.5 zoom 0.95 yalign 0.25 xalign 1.50
        pause 0.5
        show rolf heh at right:
            zoom 0.95 yalign 0.25 xalign 1.50
    with vpunch
    pause 0.6
    window show
    play music "audio/Tavern+Brawl+-+320bit.mp3" fadein 5.0 volume 0.2
    me " Hold on a second..."
    show rolf belly
    show rol pout2 at right:
        zoom 0.95 yalign 0.25 xalign 1.50
    with dissolve
    rolf " What?"
    me "...Explain."
    show rol pout at right:
        zoom 0.95 yalign 0.25 xalign 1.50
    with dissolve
    rolf "... "
    rolf "Fine. "
    #play music "audio/1.+Grundar+-+320bit.mp3" fadein 0.1 volume 0.7

    show rolf calm
    hide rol
    with dissolve
    rolf " Its simple... Just think about it for a moment. "
    "..."
    me"???"
    show rol close at right:
        zoom 0.95 yalign 0.25 xalign 1.50
    with dissolve
    rolf "Guess I'll have to spell it out for ya..."
    rolf " So..."
    hide rol with dissolve

    show rolf rock with dissolve
    rolf "Which word comes to your mind when you think of a rock? "
    me "Hmm... Hard or maybe sturdy?"
    show rolf calm with dissolve
    rolf "Yes."
    show rolf scissors with dissolve
    rolf " Now what about scissors? "
    show rol concern at right:
        zoom 0.95 yalign 0.25 xalign 1.50
    with dissolve
    rolf "And keep it to one word! "

    me "Sharp."
    hide rol with dissolve
    show rolf paper
    with dissolve
    rolf "And paper? "
    me "... Thin?"
    me " Maybe kinda brittle... Scrunchable."
    show rolf knuckles
    show rol angry at right:
        zoom 0.95 yalign 0.25 xalign 1.50
    with dissolve
    with hpunch
    rolf " I said to keep it to one word!"
    me " Okay, okay..."
    show rolf base
    hide rol
    with dissolve
    rolf " So... If you had to pick one of the three when going into battle which one would ya pick?"
    window hide
    menu:
        with dissolve


        " I'd pick a big rock.":
            window show
            me " I'd pick a big rock."
            show rolf knuckles
            show rol heh at right:
                zoom 0.95 yalign 0.25 xalign 1.50
            with dissolve
            rolf " Exactly."
            rolf " A good rock can bash in the head of just about anyone if you're strong enough."
            rolf " Doesn't even matter if your opponent is in armor with a big ol' helmet on his head. "
            show rolf fist
            hide rol
            with dissolve
            with hpunch

            rolf "Just crack the helmet to pieces with it!!"
            "...Rolf makes that sound so easy."




        " I'd pick a sharp pair of scissors.":# This skips a lot of his explanation.
            window show
            me " I'd pick a sharp pair of scissors."
            show rolf belly
            show rol close at right:
                zoom 0.95 yalign 0.25 xalign 1.50
            with dissolve
            rolf "Hmm, yes... Decent choice."
            rolf " Most strong men pick the rock. But I suppose some scissors might be better for a scrawny fella like yourself."
            show rolf scissors
            hide rol
            show roleye intense at right:
                zoom 0.95 yalign 0.25 xalign 1.50
            with dissolve
            with hpunch
            rolf " Aim for the neck and you've got a chance even against a bigger opponent!"



        "I'd pick a piece of paper.":
            window show
            me "I'd pick a piece of paper."
            show rolf knuckles at right:
                zoom 0.95 yalign 0.25 xalign 1.50
            show rol angry at right:
                zoom 0.95 yalign 0.25 xalign 1.50
            with dissolve
            rolf " Bullshit!"
            rolf "..."
            show rolf think
            hide rol
            with dissolve
            rolf " Unless you're trying to be smart and you're talkin' diplomacy or something..."
            rolf " Writing a peace proposal on the paper and sending it as a letter to avoid the battle entirely..."
            show roleye front at right:
                zoom 0.95 yalign 0.25 xalign 1.50
            with dissolve
            rolf " But you don't strike me as very educated!"
            me " Hey now..."
            hide roleye
            show rol pout at right:
                zoom 0.95 yalign 0.25 xalign 1.50
            show rolf  base
            with dissolve
            rolf " Good luck making peace with a pack of bloodthirsty wolves!"
            show rol angry
            show rolf knuckles
            with dissolve
            rolf " In that situation you'd be better off writing your last will and testament on your little piece of paper cus you'd be staring death right in the face!"


    show rolf belly
    hide roleye
    show rol pout at right:
        zoom 0.95 yalign 0.25 xalign 1.50
    with dissolve
    rolf " Anyways, most people answer the rock or the scissors, and they're right!"
    show roleye intense at right:
        zoom 0.95 yalign 0.25 xalign 1.50
    show rolf base
    play sound "audio/soundFX/Dun.wav" volume 0.4
    with vpunch
    rolf" BUT!"
    rolf "The psychology of rock, paper, scissors is different!"
    show rolf paper
    hide rol
    with dissolve
    rolf " Paper might be useless in a real fight..."
    rolf " But it's physically and psychologically the most aggressive move in rock, paper, scissors!"
    me " ??"
    rolf " It requires you to open and expose your whole hand to your opponent!"
    show rolf calm with dissolve
    rolf " I've done my research on this!"
    me " I bet you have..."
    show rolf rock with dissolve
    rolf " Most people open with rock! "
    rolf " Some claim it's because a rock is \" associated with strength \". "
    pause 0.2
    with vpunch
    rolf " But that's a big fat lie! "
    play sound "audio/soundFX/FX5/rolfknuckles.wav" volume 0.3
    show rolf knuckles
    with vpunch

    rolf "{size=+2}IT'S COWARDICE!{/size}"
    rolf " You're too afraid of opening yourself up!"
    rolf " And if you want any chance at winning in a fight, you need offense!"

    show roleye intenseside2
    show rolf paper
    with dissolve
    rolf " So we have paper-"
    rolf " A full-on assault! No defense!"
    me " Okay, okay. I think I get it... "
    " He's rambling!"
    me " Rock is too defensive, and paper is entirely offensive."
    me "...But what about scissors?"
    show rolf scissors
    with dissolve
    rolf" Playing scissors would land you somewhere in the middle! "
    rolf " ..."
    show roleye intense
    show rolf paper
    with dissolve
    rolf " All the best warriors I've tried this with back in the war opened paper! They're aggressive and fearless! "


    show rolf angryy
    hide rol
    with vpunch
    rolf " A true warrior ALWAYS opens paper!"

    if RPS == "Rock":
        show rolf belly
        show rol grin at right:
            zoom 0.95 yalign 0.25 xalign 1.50
        with dissolve
        rolf" So it makes sense you opened rock! You're a big softie!"
        me " Oh yeah?"
        me " Maybe I won't open rock next time."
        show rol pout at right:
            zoom 0.95 yalign 0.25 xalign 1.50
        show rolf base at right:
            zoom 0.95 yalign 0.25 xalign 1.50
        with dissolve
        rolf " Hmpf."
        rolf " Only the first game between two people matters! After that it's just infinite mind games."
        show rol pout with dissolve
        rolf " So there's your explanation... "
        window hide
        menu:
            with dissolve


            " I'm sure I can beat you in a best-of-three!":
                window show
                me " I'm sure I can beat you in a best-of-three!"
                show rol heh with dissolve
                rolf " Oh yeah?"
                hide roleye
                show rolf calm
                with dissolve
                rolf " Unfortunately for you, this isn't a best-of-three."
                me " ... Not feeling confident?"
                show roleye intense at right:
                    zoom 0.95 yalign 0.25 xalign 1.50
                with dissolve
                stop music fadeout 1.0
                rolf " ..."
                show rolf fist
                show roleye squint
                with dissolve
                rolf " I'll fuck you up."
                window hide
                hide roleye
                hide rol
                show rolf fist
                with dissolve

                play sound "audio/soundFX/Step1.wav"
                show rolf fist at right:
                    linear 0.4 zoom 1.2 yalign 0.30 xalign 2.20
                with vpunch
                jump RPSBO3
            " I'm not sure I believe all this... But let's get a move on.":
                window show
                me " I'm not sure I believe all this... But let's get a move on."
                rolf " Yes."


                jump nobo3


    if RPS == "Paper":
        show rolf apologetic
        show rol angryzz at right:
            zoom 0.95 yalign 0.25 xalign 1.50
        hide roleye
        with dissolve
        rolf " So I must have miscalculated somewhere!"
        rolf " There's just no way you've got a warrior's spirit..."
        me " I think I do."
        if perfscore == True:
            me " I'm an amazing warrior on top of being a perfect assistant!"
            " I couldn't help but bring that back up..."
            me "Don't judge a book by its cover! "
            show rolf base
            show rol pout at right:
                zoom 0.95 yalign 0.25 xalign 1.50
            with dissolve
            rolf " ... Time will tell."
            rolf " Well, there's your explanation... "
            window hide
        else:
            me " Don't judge a book by its cover! "
            show rolf base
            show rol pout at right:
                zoom 0.95 yalign 0.25 xalign 1.50
            with dissolve
            rolf " ... Time will tell."
            rolf " Well, There's your explanation... "
            window hide


        menu:
            with dissolve


            " I think we need to settle the game with a best-of-three to see who's the best.":
                window show
                me " I think we need to settle the game with a best-of-three to see who's the best."
                show rol closed
                show rolf calm
                with dissolve
                rolf " I don't have time for silly games."
                me " Not very warrior-like to turn down a challenge..."
                stop music fadeout 1.0
                show rolf knuckles
                show rol angryz
                with dissolve
                rolf "... "
                rolf " Have it your way, twerp! I'll show you who's boss!"
                rolf " And just so you know... The psychology I've laid out only matters in the first game between two people! So now it's all mind games!"
                window hide
                hide roleye
                hide rol
                show rolf fist
                with dissolve

                play sound "audio/soundFX/Step1.wav"
                show rolf fist at right:
                    linear 0.4 zoom 1.2 yalign 0.30 xalign 2.20
                with vpunch
                jump RPSBO3

            " Let's get a move on.":
                window show
                me " Let's get a move on."
                rolf " Yes."


                jump nobo3


    if RPS == "Scissors":
        show rolf belly
        hide roleye
        with dissolve
        rolf" So... You opening scissors sort of puts you in the middle... "
        me " Isn't a balance of defense and offense ideal?"
        show rolf think2
        with dissolve
        rolf " Time will tell... People who open with scissors are unpredictable since they can shift from defense to offense at a moment's notice... "
        rolf " They're the hardest type to predict."
        rolf " We'll have to wait and see to find out where you stand."
        " He's really thought hard about all this..."
        show rolf base with dissolve
        rolf " So there's your explanation. "
        me " I have my doubts, but okay..."
        show rolf apologetic
        show rol sidewary3 at right:
            zoom 0.95 yalign 0.25 xalign 1.50
        with dissolve
        rolf " Now... We said it was a best-of-three, didn't we?"
        "He never mentioned that..."
        window hide
        menu:
            with dissolve


            " I don't think so. \n But fine, I'll accept the best-of-three and beat you again!":
                window show
                me " I don't think so. But fine, I'll beat you again!"
                stop music fadeout 1.0
                show rolf knuckles
                show rol heh
                with dissolve
                rolf " 1-0 to you. "
                rolf " Now for my big comeback! "
                window hide
                hide roleye
                hide rol
                show rolf fist
                with dissolve

                play sound "audio/soundFX/Step1.wav"
                show rolf fist at right:
                    linear 0.4 zoom 1.2 yalign 0.30 xalign 2.20
                with vpunch
                jump RPSBO3

            " No way, I won fair and square! \n Being a sore loser isn't very warrior-like!":
                window show
                me " No way, I won fair and square! Being a sore loser isn't very warrior-like!"
                show rol think
                show rolf belly
                with dissolve
                rolf " Hmmf... I don't have time for silly games anyways."
                "Rolf grumbles and looks defeated."


                jump nobo3





    $ RPSrolf = 0
    $ RPSscore = 0


#--------------------------------- S E C O N D          R O U N D         BEST  OF  THREE -----------------------------------------------------------------------------------------------------
label RPSBO3:

    #Rolf Steps Forward and we see his face.



    #Rolf's order now is paper again to try and mindfuck you since he said it only matters once. then rock, then scissors again. His strat is that he can bait you into
    window hide
    stop music fadeout 1.0
    #play music "audio/7.+Stöðvar+-+320bit.mp3" fadein 0.1 volume 0.7
    play music "audio/1.+Grundar+-+320bit.mp3" fadein 0.1 volume 0.7
    with hpunch
    show interrogate hateh with fade

    pause 0.3
    window show
    rolf " Let's do this!"
    $ playbestof3 = True
    window hide
    scene rpsbg with fade
    show blackshake at truecenter behind rpsbg
    show rpsrolf rock with easeinright
    show rpsprotag rock with easeinleft
    window show

    if RPS == "Rock":
        $ WonFirst = False
        $ RPSrolf +=1
        if RPS =="Rock":
            rolf " But it's 1-0 in my favor. Lose once more and you've got to own it."
            " I guess that's fair... Rolf was generous enough to grant me the best-of-three!"
            me " Fine."




    if RPS == "Scissors":
        $ WonFirst = True
        $ RPSscore +=1
        if RPSscore ==1:
            #"{nw}"
            " I only need one more win to take this home!"



    " What should my next move be?"
    window hide
    with dissolve
    show darkenbehindall with dissolve
    jump showingRPSChoice2

label showingRPSChoice2:
    show screen RPSChoice2 with dissolve
    $ renpy.pause(hard=True)
    jump showingRPSChoice2

screen RPSChoice2:

    add "gui/RPS/whobeatswho.png"

    imagebutton:
        idle "gui/RPS/paperidle.png"
        hover "gui/RPS/paperhover.png"
        focus_mask True
        activate_sound "audio/UIsounds/cluck.wav"
        hover_sound "audio/UIsounds/hover.wav"
        mouse "hover"
        action Show(screen="RPSConfirm2", transition=Dissolve(0.5), RPSChosen="Paper")

    imagebutton:
        idle "gui/RPS/rockidle.png"
        hover "gui/RPS/rockhover.png"
        focus_mask True
        activate_sound "audio/UIsounds/cluck.wav"
        hover_sound "audio/UIsounds/hover.wav"
        mouse "hover"
        action Show(screen="RPSConfirm2", transition=Dissolve(0.5), RPSChosen="Rock")

    imagebutton:
        idle "gui/RPS/scissorsidle.png"
        hover "gui/RPS/scissorshover.png"
        focus_mask True
        activate_sound "audio/UIsounds/cluck.wav"
        hover_sound "audio/UIsounds/hover.wav"
        mouse "hover"
        action Show(screen="RPSConfirm2", transition=Dissolve(0.5), RPSChosen="Scissors")

screen RPSConfirm2(RPSChosen):
    modal True

    add "gui/RPS/" + RPSChosen + "chosen.png"

    imagebutton:
        idle "gui/RPS/rpsyesidle.png"
        hover "gui/RPS/rpsyeshover.png"
        focus_mask True
        activate_sound "audio/UIsounds/cluck.wav"
        hover_sound "audio/UIsounds/hover.wav"
        mouse "hover"
        if RPSChosen == "Rock":
            action Hide("RPSConfirm2", transition=Dissolve(0.5)), Hide("RPSChoice2", transition=Dissolve(0.5)), SetVariable("RPS2", "Rock"), SetVariable("RPSrolf", RPSrolf+1), Jump("BO3one")
        elif RPSChosen == "Scissors":
            action Hide("RPSConfirm2", transition=Dissolve(0.5)), Hide("RPSChoice2", transition=Dissolve(0.5)), SetVariable("RPS2", "Scissors"), SetVariable("RPSscore", RPSscore+1), Jump("BO3one")
        else:
            action Hide("RPSConfirm2", transition=Dissolve(0.5)), Hide("RPSChoice2", transition=Dissolve(0.5)), SetVariable("RPS2", "Paper"), Jump("BO3one")

    imagebutton:
        idle "gui/RPS/rpsnoidle.png"
        hover "gui/RPS/rpsnohover.png"
        focus_mask True
        activate_sound "audio/UIsounds/cluck.wav"
        hover_sound "audio/UIsounds/hover.wav"
        mouse "hover"
        action Hide("RPSConfirm2")

label BO3one:


    hide darkenbehindall with dissolve
    hide rpsrolf
    hide rpsprotag
    show fists
    window show
    $ renpy.block_rollback()
    show fists:
        yoffset 0
        linear 0.3 yoffset -20
        yoffset -20
        linear 0.1 yoffset 20

    me "{size=50} ROCK!{/size}{w=0.7}{nw}"

    show fists:
        yoffset 20
        linear 0.3 yoffset -20
        yoffset -20
        linear 0.1 yoffset 20

    rolf " {size=60}PAPER!{/size}{w=0.7}{nw}"

    show fists:
        yoffset 20
        linear 0.3 yoffset -20
        yoffset -20
        linear 0.1 yoffset 20

    me "{size=70}SCISSORS!{/size}{w=0.7}{nw}"
    window hide
    show fists:
        yoffset 20
        linear 0.3 yoffset -30
        yoffset -30
        linear 0.1 yoffset 25
#--------------------------------------------- ROUND       TWO       EVALUATION -----------------------------------------------------------------------------------------------------------------------------------------
    pause 0.6
    hide fists
    play sound "audio/soundFX/Get.mp3"
    show rpsrolf paper:
        yoffset 25
    if RPS2 == "Rock":
         show rpsprotag rock:
             yoffset 25

    if RPS2 == "Paper":
         show rpsprotag paper:
             yoffset 25

    if RPS2 == "Scissors":
         show rpsprotag scissors:
             yoffset 25
    with dissolve
    with vpunch
    pause 0.8
    window show



    if RPS2 == "Rock": #RolfJustWon
        play sound "audio/soundFX/FX2/pig-grunt-double.wav"
        rolf " Baited! Didn't expect me to pull the same move twice, huh?"
        rolf " Heh... I'm pretty good at this game."
    if RPS2 == "Paper":#WeTied
        if RPS == "Paper":
            me "Another tie?!"
            play sound "audio/soundFX/FX2/pig-snort-3-96khz.wav"
            rolf "...Tsk! Let's go again!"
            rolf " I'll win this next one for sure!"
            jump BO3two
        else:
            me " A tie..."
            play sound "audio/soundFX/FX2/pig-snort-3-96khz.wav"
            rolf " You trying to match my aggression with that paper? Hmpf."
            $ PaperTie = True

            rolf "...Let's go again."
            jump BO3two
        jump BO3two

    if RPS2 == "Scissors":#I won
        play sound "audio/soundFX/FX2/pig-grunt.wav"

        rolf " Agh!"
        if RPS == "Paper":
            rolf " I... Gave you that one for free! "
            rolf " To give you a glimpse of hope... "
            rolf" So I can rip it away from you with a big comeback!"
            jump BO3two





    if RPSrolf ==2:
        rolf " I knew I'd win. I've honed these skills for years!"
        me " Sure... Congrats."
        $ RPSwin = False
        window hide
        stop music fadeout 1.0
        jump afterRPS


    if RPSscore ==2:
        rolf " Shit!"
        rolf " ..."
        rolf " This game is mostly just luck anyways..."
        rolf " But congrats..."
        $ RPSwin = True
        window hide
        stop music fadeout 1.0
        jump afterRPS

    if RPSrolf ==1:
        if RPSscore ==1:
            rolf " We're at 1-1! Whoever gets the next one takes it!"
            $ SuddenDeath = True #This means he won't say ' next winner takes it! ' in the future
            jump BO3two
        else:
            rolf "...Let's go again."
            jump BO3two

    if RPSscore ==1:
        if RPSrolf ==1:
            rolf " We're at 1-1! Whoever gets the next one takes it!"
            $ SuddenDeath = True #This means he won't say ' next winner takes it! ' in the future
            jump BO3two
        else:
            rolf "...Let's go again."
            jump BO3two

    if RPSrolf ==0:
        rolf "...Let's go again."
        jump BO3two

    if RPSscore ==0:
        rolf "...Let's go again."
        jump BO3two

#--------------------------------- T H I R D           R O U N D         BEST  OF  THREE -----------------------------------------------------------------------------------------------------
label BO3two:
    window hide

    show rpsrolf rock
    show rpsprotag rock
    with dissolve
    show darkenbehindall with dissolve
    jump showingRPSChoice3

label showingRPSChoice3:
    show screen RPSChoice3 with dissolve
    $ renpy.pause(hard=True)
    jump showingRPSChoice3

screen RPSChoice3:

    add "gui/RPS/whobeatswho.png"

    imagebutton:
        idle "gui/RPS/paperidle.png"
        hover "gui/RPS/paperhover.png"
        focus_mask True
        activate_sound "audio/UIsounds/cluck.wav"
        hover_sound "audio/UIsounds/hover.wav"
        mouse "hover"
        action Show(screen="RPSConfirm3", transition=Dissolve(0.5), RPSChosen="Paper")

    imagebutton:
        idle "gui/RPS/rockidle.png"
        hover "gui/RPS/rockhover.png"
        focus_mask True
        activate_sound "audio/UIsounds/cluck.wav"
        hover_sound "audio/UIsounds/hover.wav"
        mouse "hover"
        action Show(screen="RPSConfirm3", transition=Dissolve(0.5), RPSChosen="Rock")

    imagebutton:
        idle "gui/RPS/scissorsidle.png"
        hover "gui/RPS/scissorshover.png"
        focus_mask True
        activate_sound "audio/UIsounds/cluck.wav"
        hover_sound "audio/UIsounds/hover.wav"
        mouse "hover"
        action Show(screen="RPSConfirm3", transition=Dissolve(0.5), RPSChosen="Scissors")

screen RPSConfirm3(RPSChosen):
    modal True

    add "gui/RPS/" + RPSChosen + "chosen.png"

    imagebutton:
        idle "gui/RPS/rpsyesidle.png"
        hover "gui/RPS/rpsyeshover.png"
        focus_mask True
        activate_sound "audio/UIsounds/cluck.wav"
        hover_sound "audio/UIsounds/hover.wav"
        mouse "hover"
        if RPSChosen == "Rock":
            action Hide("RPSConfirm3", transition=Dissolve(0.5)), Hide("RPSChoice3", transition=Dissolve(0.5)), SetVariable("RPS3", "Rock"), Jump("BO3three")
        elif RPSChosen == "Scissors":
            action Hide("RPSConfirm3", transition=Dissolve(0.5)), Hide("RPSChoice3", transition=Dissolve(0.5)), SetVariable("RPS3", "Scissors"), SetVariable("RPSrolf", RPSrolf+1), Jump("BO3three")
        else:
            action Hide("RPSConfirm3", transition=Dissolve(0.5)), Hide("RPSChoice3", transition=Dissolve(0.5)), SetVariable("RPS3", "Paper"), SetVariable("RPSscore", RPSscore+1), Jump("BO3three")

    imagebutton:
        idle "gui/RPS/rpsnoidle.png"
        hover "gui/RPS/rpsnohover.png"
        focus_mask True
        activate_sound "audio/UIsounds/cluck.wav"
        hover_sound "audio/UIsounds/hover.wav"
        mouse "hover"
        action Hide("RPSConfirm3")

label BO3three:


    hide darkenbehindall with dissolve
    hide rpsrolf
    hide rpsprotag

    show fists:
        yoffset 25
    window show
    $ renpy.block_rollback()
    show fists:
        yoffset 25
        linear 0.3 yoffset -20
        yoffset -20
        linear 0.1 yoffset 20

    me "{size=50} ROCK!{/size}{w=0.7}{nw}"

    show fists:
        yoffset 20
        linear 0.3 yoffset -20
        yoffset -20
        linear 0.1 yoffset 20

    rolf " {size=60}PAPER!{/size}{w=0.7}{nw}"

    show fists:
        yoffset 20
        linear 0.3 yoffset -20
        yoffset -20
        linear 0.1 yoffset 20

    me "{size=70}SCISSORS!{/size}{w=0.7}{nw}"
    window hide
    show fists:
        yoffset 20
        linear 0.3 yoffset -30
        yoffset -30
        linear 0.1 yoffset 25

    pause 0.6
    hide fists
    play sound "audio/soundFX/Get.mp3"
    show rpsrolf rock:
        yoffset 25
    if RPS3 == "Rock":
         show rpsprotag rock:
             yoffset 25

    if RPS3 == "Paper":
         show rpsprotag paper:
             yoffset 25

    if RPS3 == "Scissors":
         show rpsprotag scissors:
             yoffset 25
    with dissolve
    with vpunch
    pause 0.8
    window show



    if RPS3 == "Rock": #WeTied

        if RPS == "Paper":
            if RPS2 == "Paper":
                play sound "audio/soundFX/FX2/pig-grunt-5-deep-96khz.wav"
                rolf " Enough! Stop copying my moves, squirt!"
                rolf " Again!"

                jump BO3random
        else:
            if PaperTie == True:
                play sound "audio/soundFX/FX2/pig-grunt-5-deep-96khz.wav"
                rolf "Two ties in a row? Stop that! "
                rolf " Again!"

                jump BO3random
        rolf " Again!"

        jump BO3random
    if RPS3== "Paper":#I win
        play sound "audio/soundFX/FX2/pig-scream-loud-oink.wav"
        rolf " !!"
        rolf "ECHH!"
        if RPSscore ==1:
            rolf " Ya got me on that one."
            if RPSrolf ==0:
                rolf " But don't get cocky just cus ya won once, I can still come back!"


    if RPS3 == "Scissors":#he won
        play sound "audio/soundFX/FX2/pig-grunt-double.wav"
        rolf " Got ya!"


    if RPSrolf ==2:
        rolf " I knew I'd win. I've honed these skills for years!"
        me " Sure... Congrats."
        $ RPSwin = False
        window hide
        stop music fadeout 1.0
        jump afterRPS

    if RPSscore ==2:
        rolf " Shit!"
        rolf " ..."
        rolf " This game is mostly just luck anyways..."
        rolf " But congrats..."
        $ RPSwin = True
        window hide
        stop music fadeout 1.0
        jump afterRPS


    if RPSrolf ==1:
        if RPSscore ==1:
            if SuddenDeath == False:
                rolf " We're at 1-1! Whoever gets the next one takes it!"
                jump BO3random
            else:
                rolf "Again!"
                jump BO3random
        else:
            rolf " Again!"
            jump BO3random

    if RPSscore ==1:
        if RPSrolf ==1:
            if SuddenDeath == False:
                rolf " We're at 1-1! Whoever gets the next one takes it!"
                jump BO3random
            else:
                rolf "Again!"
                jump BO3random
        else:
            rolf " Again!"
            jump BO3random



label BO3random:#------------------------------------------------------------------ KEEP LOOPING BELOW UNTIL VICTOR    ------------------------------------------------------------------------------------------------------------------------------------

    window hide
    show rpsrolf rock
    show rpsprotag rock
    with dissolve
    show darkenbehindall with dissolve


#vvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvv ROLF RANDOM ROLL vvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvv
    $rollresult = renpy.random.randint(1, 3)
    $RPSrandom = ""
    if rollresult == 1: #rock
        $ RPSrandomROLF = "Rock"
    elif rollresult == 2: #paper
        $ RPSrandomROLF = "Paper"
    elif rollresult == 3: #scissors
        $ RPSrandomROLF = "Scissors"

#^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ ROLF RANDOM ROLL #^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^



#vvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvv PLAYER CHOICE  vvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvv
    jump showingRPSChoice4

label showingRPSChoice4:

    show screen RPSChoice4 with dissolve
    $ renpy.pause(hard=True)
    jump showingRPSChoice4

screen RPSChoice4:

    add "gui/RPS/whobeatswho.png"

    imagebutton:
        idle "gui/RPS/paperidle.png"
        hover "gui/RPS/paperhover.png"
        focus_mask True
        activate_sound "audio/UIsounds/cluck.wav"
        hover_sound "audio/UIsounds/hover.wav"
        mouse "hover"
        action Show(screen="RPSConfirm4", transition=Dissolve(0.5), RPSChosen="Paper")

    imagebutton:
        idle "gui/RPS/rockidle.png"
        hover "gui/RPS/rockhover.png"
        focus_mask True
        activate_sound "audio/UIsounds/cluck.wav"
        hover_sound "audio/UIsounds/hover.wav"
        mouse "hover"
        action Show(screen="RPSConfirm4", transition=Dissolve(0.5), RPSChosen="Rock")

    imagebutton:
        idle "gui/RPS/scissorsidle.png"
        hover "gui/RPS/scissorshover.png"
        focus_mask True
        activate_sound "audio/UIsounds/cluck.wav"
        hover_sound "audio/UIsounds/hover.wav"
        mouse "hover"
        action Show(screen="RPSConfirm4", transition=Dissolve(0.5), RPSChosen="Scissors")

screen RPSConfirm4(RPSChosen):
    modal True

    add "gui/RPS/" + RPSChosen + "chosen.png"

    imagebutton:
        idle "gui/RPS/rpsyesidle.png"
        hover "gui/RPS/rpsyeshover.png"
        focus_mask True
        activate_sound "audio/UIsounds/cluck.wav"
        hover_sound "audio/UIsounds/hover.wav"
        mouse "hover"
        if RPSChosen == "Rock":
            action Hide("RPSConfirm4", transition=Dissolve(0.5)), Hide("RPSChoice4", transition=Dissolve(0.5)), SetVariable("RPSrandom", "Rock"), Jump("RPSBO3Randomlabel")
        elif RPSChosen == "Scissors":
            action Hide("RPSConfirm4", transition=Dissolve(0.5)), Hide("RPSChoice4", transition=Dissolve(0.5)), SetVariable("RPSrandom", "Scissors"), Jump("RPSBO3Randomlabel")
        else:
            action Hide("RPSConfirm4", transition=Dissolve(0.5)), Hide("RPSChoice4", transition=Dissolve(0.5)), SetVariable("RPSrandom", "Paper"), Jump("RPSBO3Randomlabel")

    imagebutton:
        idle "gui/RPS/rpsnoidle.png"
        hover "gui/RPS/rpsnohover.png"
        focus_mask True
        activate_sound "audio/UIsounds/cluck.wav"
        hover_sound "audio/UIsounds/hover.wav"
        mouse "hover"
        action Hide("RPSConfirm4")

#^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ PLAYER CHOICE  ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^


#vvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvv LETS GO  vvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvv

label RPSBO3Randomlabel:


    hide darkenbehindall with dissolve
    hide rpsrolf
    hide rpsprotag
    show fists:
        yoffset 25
    window show
    $ renpy.block_rollback()
    show fists:
        yoffset 25
        linear 0.3 yoffset -20
        yoffset -20
        linear 0.1 yoffset 20

    me "{size=50} ROCK!{/size}{w=0.7}{nw}"

    show fists:
        yoffset 20
        linear 0.3 yoffset -20
        yoffset -20
        linear 0.1 yoffset 20

    rolf " {size=60}PAPER!{/size}{w=0.7}{nw}"

    show fists:
        yoffset 20
        linear 0.3 yoffset -20
        yoffset -20
        linear 0.1 yoffset 20

    me "{size=70}SCISSORS!{/size}{w=0.7}{nw}"
    window hide
    show fists:
        yoffset 20
        linear 0.3 yoffset -30
        yoffset -30
        linear 0.1 yoffset 25

    pause 0.6
    hide fists
    play sound "audio/soundFX/Get.mp3"
#vvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvv ROLF SHOW  vvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvv
    if RPSrandomROLF == "Rock":
         show rpsrolf rock:
             yoffset 25

    if RPSrandomROLF == "Paper":
         show rpsrolf paper:
             yoffset 25

    if RPSrandomROLF == "Scissors":
         show rpsrolf scissors:
             yoffset 25

#vvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvv PROTAG SHOW  vvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvv

    if RPSrandom == "Rock":
         show rpsprotag rock:
             yoffset 25

    if RPSrandom == "Paper":
            show rpsprotag paper:
             yoffset 25

    if RPSrandom == "Scissors":
            show rpsprotag scissors:
             yoffset 25
    with dissolve
    with vpunch
    pause 0.8
    window show



    if RPSrandom == "Rock":
        if RPSrandomROLF == "Rock":
            " It's a tie!"
            play sound "audio/soundFX/FX2/pig-snort-3-96khz.wav"
            rolf " Again!"
            jump BO3random
        if RPSrandomROLF == "Paper":
            play sound "audio/soundFX/FX2/pig-grunt-double.wav"
            rolf " Boom!"
            $ RPSrolf +=1
        if RPSrandomROLF == "Scissors":
            play sound "audio/soundFX/FX2/pig-squeak.wav"
            rolf" FFht!"
            $ RPSscore +=1



    if RPSrandom == "Paper":
        if RPSrandomROLF == "Rock":
            play sound "audio/soundFX/FX2/pig-squeak.wav"
            rolf " Ech!"
            $ RPSscore +=1
        if RPSrandomROLF == "Paper":
            " We tie!"
            play sound "audio/soundFX/FX2/pig-snort-3-96khz.wav"
            rolf " Again!"
            jump BO3random
        if RPSrandomROLF == "Scissors":
            play sound "audio/soundFX/FX2/pig-squeak.wav"
            rolf" Yes! Snipped!"
            $ RPSrolf +=1


    if RPSrandom=="Scissors":
        if RPSrandomROLF == "Rock":
            play sound "audio/soundFX/FX2/pig-squeak.wav"
            rolf" Smashed!"
            $ RPSrolf +=1
        if RPSrandomROLF == "Paper":
            play sound "audio/soundFX/FX2/pig-squeak.wav"
            rolf " Agh!"
            $ RPSscore +=1
        if RPSrandomROLF == "Scissors":
            " A tie!"
            play sound "audio/soundFX/FX2/pig-snort-3-96khz.wav"
            rolf " Again!"
            jump BO3random


# EITHER WINS-----------------------------------------------------------------
    if RPSrolf ==2:
        rolf " I knew I'd win. I've honed these skills for years!"
        me " Sure... Congrats."
        $ RPSwin = False
        window hide
        stop music fadeout 1.0
        jump afterRPS

    if RPSscore ==2:
        rolf " Shit!"
        rolf " ..."
        rolf " This game is mostly just luck anyways..."
        rolf " But congrats..."
        $ RPSwin = True
        window hide
        stop music fadeout 1.0
        jump afterRPS





#ONE WINS------------------------------
    if RPSrolf ==1:
        if RPSscore ==1:
            if SuddenDeath == False:
                rolf " We're at 1-1! Whoever gets the next one takes it!"
                $ SuddenDeath = True
                jump BO3random
            else:
                rolf "Again!"
                jump BO3random
        else:
            rolf " Again!"
            jump BO3random

    if RPSscore ==1:
        if RPSrolf ==1:
            if SuddenDeath == False:
                rolf " We're at 1-1! Whoever gets the next one takes it!"
                $ SuddenDeath = True
                jump BO3random
            else:
                rolf " Again!"
                jump BO3random
        else:
            rolf " Again!"
            jump BO3random















    # Here I need Rolf to pull random moves. And it needs to loop if you get tie after tie.
    #If Rolf wins he goes " Hah!" if he loses he goes " Grr!"
    #If you both tie Rolf goes " Again!"
    # if RPSscore == 1  & RPSrolf == 1       Rolf will say " 1-1! next winner takes it all!"


label ifeveryonehastiedsofar:
    #Add text here for when a player gets their first win. if every move so far has been a tie.

label ifmoreties:
    #rolf " What's with all these ties?!"



label ifoneone:
    if RPSrolf ==1:
        if RPSscore ==1:
            if SuddenDeath == False:
                rolf " We're at 1-1! Whoever gets the next one takes it!"
                jump BO3random
            else:
                rolf "Again!"
                jump BO3random
        else:
            rolf " Again!"
            jump BO3random

    if RPSscore ==1:
        if RPSrolf ==1:
            if SuddenDeath == False:
                rolf " We're at 1-1! Whoever gets the next one takes it!"
                jump BO3random
            else:
                rolf "Again!"
                jump BO3random




label eitherplayerwins:
    if RPSrolf ==2:
        rolf " I knew I'd win. I've honed these skills for years!"
        me " Sure... Congrats."
        $ RPSwin = False
        window hide
        stop music fadeout 1.0
        jump afterRPS

    if RPSscore ==2:
        rolf " ..."
        rolf " This game is mostly just luck anyways..."
        rolf " But congrats..."
        $ RPSwin = True
        window hide
        stop music fadeout 1.0
        jump afterRPS

        jump BO3random #< this shoots you back to the BO3random label. so it has to be repeatable.

#---------------------------------------------------------------------------------------------------------------------------------------------------------------- LOOP    ENDS ----------------------------------------------------------------------------------------------------------------------------------------------------------------

label afterRPS:
    scene black with fade
    window show
    " Rolf takes a step back."
    window hide
    scene tailorsmith
    show blackshake at truecenter behind tailorsmith
    show rolf base at right:
        zoom 1.2 yalign 0.30 xalign 2.20

    with fade
    pause 0.3
    play sound "audio/soundFX/Step1.wav"
    show rolf base at right:
        linear 0.5 zoom 0.95 yalign 0.25 xalign 1.50

    pause 0.5
    show rolf base at right:
        zoom 0.95 yalign 0.25 xalign 1.50

    window show
    play music "audio/Tavern+Brawl+-+320bit.mp3" if_changed fadein 2.0 volume 0.2

    if playbestof3 == True:
        if RPSwin == True:
            if RPSrolf ==1:
                show rol think at right:
                    zoom 0.95 yalign 0.25 xalign 1.50
                with dissolve
                rolf "You barely won that..."
                rolf " If it was a best of five I would've won for sure, I was just figuring you out."
                me " Suuure."

            if RPSrolf ==0:
                show rol closed at right:
                    zoom 0.95 yalign 0.25 xalign 1.50
                with dissolve

                rolf " 2-0 to you..."
                show rol angryzz at right:
                    zoom 0.95 yalign 0.25 xalign 1.50
                with dissolve
                rolf " But uuuh... like I said... It's not about winning or losing! It's about the psychology of it!"
                if RPS == "Paper":
                    show rol angry at right:
                        zoom 0.95 yalign 0.25 xalign 1.50
                    show rolf knuckles
                    with dissolve
                    rolf " And only time will tell if you can live up to that warrior's opener..."
                    me " I definitely will!"
                else:
                    me " Suuure..."
        if RPSwin == False:
            show rol heh at right:
                zoom 0.95 yalign 0.25 xalign 1.50
            with dissolve
            rolf " Hehehe!"
            if RPSscore ==1:
                me " It was close!"
                show rol calm at right:
                    zoom 0.95 yalign 0.25 xalign 1.50
                with dissolve
                rolf " No way. I got twice as many points."
                me " ... That's one way to frame it."
            if RPSscore ==0:
                show rol smiley at right:
                    zoom 0.95 yalign 0.25 xalign 1.50
                with dissolve
                rolf " Too easy. "
                me " Yeah, yeah..."
    #if playbestof3 == False:
    #^ If I want special dialogue for not doing best of 3
label nobo3:
    rolf " ..."
    show rol base at right:
        zoom 0.95 yalign 0.25 xalign 1.50
    show rolf base
    with dissolve
    rolf "Now I've got a patrol shift at the beach to get to."
    "Oh right, I need to get there too! "
    " Billy told me I could get directions from Per."
    "But... I don't remember the way to the gate!"
    me "... Where exactly is this beach?"
    show rol pout2 at right:
        zoom 0.95 yalign 0.25 xalign 1.50
    with dissolve
    rolf "... I thought you were some special assistant, no? "
    show roleye intense at right:
        zoom 0.95 yalign 0.25 xalign 1.50
    with dissolve
    rolf " You should know this stuff!"
    me "!!"
    hide roleye
    show rol concern
    show rolf belly
    with dissolve
    rolf " ... Ugh. Just follow me and we'll get there soon."
    window hide
    stop music fadeout 1.0
    play sound "audio/soundFX/run2r.wav"
    hide rolf
    hide rol
    with easeoutright
    show rockpic #These show things are just for the gallery
    show paperpic
    show scissorpic
    scene black
    with fade
    window show
    "I follow Rolf as he briskly walks through the city."
    " Nobody greets him and people do their best to stay out of his way."

    jump Gatebeach

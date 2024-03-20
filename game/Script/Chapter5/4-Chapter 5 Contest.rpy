label BikiniContest:

    window show
    stop music fadeout 1.0
    " We follow Maple as she hurries off."
label kinistart:
    if playnormal == False:
        $ maple_name = "Maple"

    window hide
    scene bg bikinicontest
    show blackshake at truecenter behind bg
    show bikinigroup
    show bikinigrouplook
    show bikinipiggies
    show bikinigrp2
    show bikinigrp3
    show bikinigrp4
    with fade
    pause 1.2
    play sound "audio/soundFX/run2.wav"
    show maps basec:
        xoffset -200
    with easeinleft
    pause 0.2
    show maf ofoa:
        xoffset -200
    with dissolve
    window show

label swimsuitcomp:
    play music "audio/beachlong.mp3" fadein 1.0 volume 0.36 noloop
    queue music "audio/beachlong2.mp3" fadein 1.0 volume 0.36 loop

    maple " I gotta get up on stage! Wish me luck!"
    me " You've got this, Maple!"
    window hide
    if playnormal == False:

        menu:
            with dissolve
            "Emelie is wearing her Blue Swimsuit!":
                $ modest = True

            "Emelie is wearing her Melon Bikini!":
                $ modest = False


    play sound "audio/soundFX/run2.wav"
    show emeswim normal at right:
        yalign -0.20 xalign 1.0
        zoom 0.95


    with easeinright
    if playnormal == False:

        menu:
            with dissolve
            "Play whole scene!":
                pause 0.1


            "Skip to Cannonball!":
                $ cannonballskip = True
                jump NadiaChoice

    show maf baseface
    show mapeye right:
        xoffset -200
    show emf smile at right:
        yalign -0.20 xalign 1.0
        zoom 0.95
    show emeye side1 at right:
        yalign -0.20 xalign 1.0
        zoom 0.95
    with dissolve
    window show
    emelie " Go get 'em!"
    window hide
    hide maps
    hide maf
    hide mapeye
    with dissolve
    play sound "audio/soundFX/poke_1.wav" volume 0.3
    show bikinigrp1 behind bikinigrp2 with dissolve
    pause 0.4
    window show
    "Maple runs up on stage and greets the onlookers! "
    hide emeye
    show emeswim out behind emf at right:
        yalign -0.20 xalign 1.0
        zoom 0.95
    show emf surprise
    with dissolve
    emelie " Wow! Look at all these people!"
    window hide
    hide emf
    show emeswim normal
    with dissolve
    show emeswim normal at right:
        linear 0.5 zoom 1.1 yalign 0.0 xalign 1.1
    pause 0.5
    show emeswim normal at right:
        zoom 1.1 yalign 0.0 xalign 1.1
    show beachsmokeemelie behind emeswim with dissolve
    window show
    "Emelie steps a bit closer and lowers her voice."
    show emf pout at right:
        zoom 1.1 yalign 0.0 xalign 1.1
    with dissolve
    emelie " {alpha=*0.95}{size=-2}It looks like some people have signs to \" score \" the bikinis!{/alpha}{/size}"
    show emeswim think
    show emf think
    with dissolve
    emelie "{alpha=*0.95}{size=-2}Or girls?{/alpha}{/size}"
    emelie " {alpha=*0.95}{size=-2}I honestly don't really know what they're scoring in these competitions...{/alpha}{/size}"
    show emeswim hips
    show emf laugh
    with dissolve
    emelie "{alpha=*0.95}{size=-2}But I do like looking at pretty girls!{/alpha}{/size}"
    show emeswim out
    show emf gross
    with dissolve
    emelie "{alpha=*0.95}{size=-2} Rating people makes me feel sort of icky though!{/alpha}{/size}"
    show emf insecure
    with dissolve
    emelie "{alpha=*0.95}{size=-2}So let's just talk among ourselves about what we think!{/alpha}{/size}"
    "Me and Emelie quiet down as the crowd's attention shifts."
    $ announcer_name = " ???"
    window hide
    show blackopacity with dissolve
    show cowannouncer
    show cowhand
    with dissolve
    with vpunch
    pause 0.2
    window show
    announcer " Welcome, everyone, to Hog Haven's annual Bikini Contest!"
    $ announcer_name = " Isabelle"
    hide cowhand with dissolve
    announcer " My name is Isabelle and I'll be your announcer today!"
    hide coweyeclose
    hide cowhand
    show cowlookdown
    show cowpapers
    with dissolve

    announcer " The contestants have all provided me with some brief information about themselves too!"

    announcer " This year we have a contest-regular as well as some first-timers!"
    hide cowlookdown
    with dissolve
    announcer " Now..."
    announcer " Before we start..."
    show cowhand
    show coweyeclose
    with dissolve
    with vpunch
    announcer " {size=+3}AAARE YOOUUU READYYY!?"
    play sound "audio/soundFX/Crowd/donnacheer2.wav"  volume 0.3 fadein 0.6
    with hpunch
    crowd " {size=+5}YES WE ARE!"
    " The crowd sure is eager!"
    show cowlookdown
    hide cowhand
    hide coweyeclose
    with dissolve
    announcer " First up are our non-pig contestants!"
    hide cowlookdown
    hide cowpapers
    with dissolve
    announcer " We start off with last years winner... Maple!!"
    window hide
    hide blackopacity
    hide cowhand
    hide cowlookdown
    hide cowannouncer
    with dissolve
    pause 0.3
    show emf wide with dissolve
    window show
    emelie " Woah, Maple won last year? "
    show emf biggersmile
    show emear high at right:
        zoom 1.1 yalign 0.0 xalign 1.1
    show emeswim hips
    with dissolve
    emelie " I'm excited to see what her modeling routine is like!!"
    window hide

    show bikinimaple1 with fade
    with vpunch
    pause 1.0
    window show
    "Everyone shifts their focus to Maple!"
    "She strikes a daring pose, and moves her hands to start tugging at her bikini!"
    play sound "audio/soundFX/Crowd/cheerclap3.wav" volume 0.4 fadein 0.3
    crowd " {size=+1}Oooh!"
    announcer " As you all know, Maple lives here in Hog Haven! "
    announcer "She likes fashion and social gatherings! Especially parties!"
    maple " I sure do! And I love putting on a show!"
    window hide
    show bikinimaple2 with dissolve
    with vpunch
    pause 1.5
    window show
    "Maple pulls on her bikini, revealing golden piercings on each side of the tight fabric covering her nipples!"
    play sound "audio/soundFX/Crowd/cheerclap2.wav" volume 0.2 fadein 0.6
    crowd " {size=+1}Aaaah!!"
    "The crowd gets way louder! "
    "Me and Emelie both join in to cheer her on!"
    window hide
    play sound "audio/soundFX/Crowd/cheerclap1.wav" volume 0.4 fadein 0.6
    show blackopacity with dissolve
    show holdsign
    show scoresign high
    with dissolve
    with vpunch
    pause 0.3
    window show
    " Everyone raises their score signs! It looks like Maple got a good score!"
    "Me and Emelie shift our focus back to each other, and Maple thanks the audience."
    window hide
    hide blackopacity
    hide holdsign
    hide scoresign high
    with dissolve
    pause 0.3
    window show
    maple " Thank you, everyone!"
    hide bikinimaple1
    hide bikinimaple2
    with fade
    pause 0.3
    window show
    #Show emelie back again
    show emf surprise
    show emeswim out
    with dissolve
    window show
    emelie " Whew! Maple sure is pretty!"
    show emf insecure with dissolve
    emelie " And that bikini... somehow got even more revealing..."
    me " It.. sure is."
    show emf normalblush
    show emeswim bellu
    with dissolve
    emelie " What do you think about her swimsuit?"
    window hide
    menu:
        with dissolve


        " The skimpier the better! \n I love it!":
            window show
            me " The skimpier the better! I love it!"
            if modest == True:
                show emf surprise with dissolve
                emelie "Really? You picked a pretty modest swimsuit for me!"
                show emf laugh with dissolve
                emelie "Maybe you did it to keep others from looking, hmm? Haha!"
            else:
                show emf laugh with dissolve
                emelie " Haha, I figured!"
                show emf sooth with dissolve
                emelie " Seeing as you picked this bikini out for me!"




        "Maple is pushing it a bit... \n Her nipple piercings and areolas are showing!":
            window show
            me " Maple is pushing it a bit... Her nipple piercings and areolas are showing!"
            if modest == True:
                show emf surprise with dissolve
                emelie "Oho, Maybe you prefer more left to the imagination!"
                emelie "You did pick this fairly modest swimsuit out for me, after all!"
                show emf insecure
                emelie " At least it would've been fairly modest had it not been for the small size."
            else:
                show emf laugh with dissolve
                emelie " Haha, I can see that!"
                show emf sooth with dissolve
                emelie " But you still picked this skimpy bikini out for me, didn't you?"
    show emeswim think
    show emf think
    hide emear
    with dissolve
    emelie " Hmm..."
    emelie " After that crowd reaction, I don't really think it's the swimsuits they're rating..."
    show emf wide
    show emeswim out
    with dissolve
    emelie "Since they got a whole lot louder once Maple revealed her piercings!"
    emelie " I think this might be more like a beauty contest!"
    me " Yeah, that seems more like it!"
    show emf normalblush
    show emeswim normal
    with dissolve
    emelie " I really love Maple's sense of fashion, but she's really pretty besides that too, don't you think?"
    "I don't know how far I can go with complimenting other ladies in front of Emelie..."
    me " Uuuuh, I agree!"
    show emeswim hips
    show emf sooth
    with dissolve
    emelie "Her body is both fit and curvy, and she's super bubbly and social... And always wearing sexy outfits on top of all that!"
    show emf insecure
    with dissolve
    emelie " I get a little jealous seeing her sometimes."
    show emf concern
    show emeswim normal
    with dissolve
    emelie " But I've heard some people call her a \" Blonde Bimbo \"... "
    emelie "I don't really know what that means. It sometimes sounds like an insult, and sometimes like a compliment."
    show emeswim think
    show emf think
    with dissolve
    emelie " Maybe it's a description of her hair, figure, or clothing style? "
    show emeye normal at right:
        zoom 1.1 yalign 0.0 xalign 1.1
    with dissolve
    emelie"Or personality maybe? Hmm."
    window hide
    hide emeye
    show emf wide
    show emeswim out
    with dissolve
    with vpunch
    window show
    emelie " I wonder if I'm a blonde bimbo?!"
    emelie" I've heard my hair referred to as \" Pale Blonde \" before. So maybe I qualify!"
    show emeswim hips
    show emf normalblush
    with dissolve
    emelie " Anyways... Do you like really confident girls like her who show their \"assets\" off? "
    # You did pick a very revealing outfit for me...
    window hide
    menu:
        with dissolve
        "I like really confident women who show off!":
            window show
            me "I like really confident women who show off!"
            if modest == True:
                show emf smile with dissolve
                emelie " I see! In skimpy bikinis like hers, it must be hard NOT to show off! "
            else:
                show emf wide with dissolve
                emelie " In this bikini it's hard NOT to show off!"
            show emf insecure with dissolve
            emelie " But I agree, I like it a lot too! Even if I get a little envious of all that confidence!"

        "I think I generally prefer more \" modest \" girls!":
            window show
            me "I think I generally prefer more \" modest \" girls!"
            #if
            if modest == True:
                show emf smile with dissolve
                emelie " I understand!"
            else:
                show emf yeaa with dissolve
                emelie "And yet you picked such a revealing bikini for me, huh?..."
                "... She caught me in a lie."
            show emf normalblush with dissolve
            emelie " I personally like the confidence! Even if it makes me a little envious, haha!"



    window hide
    show blackopacity with dissolve
    show cowannouncer
    show cowpapers
    with dissolve
    pause 0.2
    window show
    announcer " And it seems our next contestants are all here from another part of the world!"
    show cowhand
    show coweyeclose
    with dissolve
    announcer" Show them your love, Hog Haven!"
    play sound "audio/soundFX/Crowd/cheerclap4.wav" volume 0.5 fadein 0.6
    with hpunch
    crowd " Whoo!"
    show cowlookdown
    hide coweyeclose
    with dissolve
    announcer " The first of our new contestants iiiis... "
    hide cowlookdown
    show coweyeclose
    with dissolve

    announcer "Imara!!"
    window hide
    hide blackopacity
    hide cowannouncer
    hide cowhand
    hide cowpapers
    hide coweyeclose
    with dissolve
    pause 0.2
    window show
    show emf surprise with dissolve
    emelie " A new competitor!!"

    window hide
    show bikinigiraffe1 with fade
    with vpunch
    pause 0.4
    window show

    play sound "audio/soundFX/Crowd/gasp.wav" volume 0.6 fadein 0.4
    crowd " Hoaah!?"
    "She immediately pulls her top open!"
    emelie " Whoah! That's the tallest woman I've ever seen!"
    announcer " M-miss! Nudity isn't allowe-"
    imara " I'm not in the nude~ Take a good, close look!"
    announcer " O-oh, you're right! I apologize!"
    "Isabelle clears her throat. "
    announcer" Imari is a giraffe! And they're known as the tallest animals in the world!"

    announcer " She loves playing instruments, and has an incredible fondness of her close friend Nadia!"
    maple " Woaaah! I love your style!"
    show bikinigiraffe1b with dissolve
    imara " Thank you!~ I'm a big fan of yours, too!"
    imara " And I love the piercings- I've got a few myself. "
    maple "Ahh, yes! I love your earrings!"
    imara " That's not all~"
    window hide
    show bikinigiraffe2 with dissolve
    play sound "audio/soundFX/Dun.wav" volume 0.5
    with vpunch
    pause 1.5
    window show
    play sound "audio/soundFX/Crowd/suddengasp.wav" volume 0.3 fadein 0.4
    "She sticks her long tongue out, making the crowd gasp even louder!"
    maple " Whaaa! "
    maple " Tongue piercings?! I hadn't considered that before!!"
    maple " Gosh, that is so cool!!"
    play sound "audio/soundFX/Crowd/cheerclap2.wav" volume 0.2 fadein 0.6
    crowd " Amazing!"
    "The crowd roars, also seeming to enjoy the display!"
    window hide
    play sound "audio/soundFX/Crowd/cheerclap1.wav" volume 0.5 fadein 0.5
    show blackopacity
    with dissolve
    show holdsign
    show scoresign mixed
    with dissolve
    pause 0.3
    window show
    " But the resulting score is a bit mixed!"
    "Emelie pokes me for a discussion."
    window hide
    hide blackopacity
    hide holdsign
    hide scoresign high
    with dissolve

    pause 0.2
    show bikinigiraffe1c with dissolve
    window show
    imara " Thanks, all~ "
    window hide
    pause 0.3
    hide bikinigiraffe1
    hide bikinigiraffe1c
    hide bikinigiraffe1b
    hide bikinigiraffe2
    with fade
    pause 0.2


    show emf waa
    show emear high at right:
        zoom 1.1 yalign 0.0 xalign 1.1
    show emeswim out
    with dissolve
    window show
    emelie " Wow, that tongue sure was a big surprise, huh?"
    me " Yes! Almost made me jump."
    hide emear
    show emf pout
    with dissolve

    emelie " Do you like taller women?"
    window hide
    menu:
        with dissolve
        "I love taller women!":
            window show
            me "I love taller women!"
            show emf gross with dissolve
            emelie "O-oh, I see!... Maybe I still have one final growth spurt left in me!"
            show emf wide with dissolve
            emelie " But I only seem to be getting wider around the hips and bust. Maybe it's all those pancakes."
            me " Haha, maybe we should go again someday, I have yet to try them!"
            show emf smile with dissolve
            emelie " For sure!"
        "I prefer shorter ladies!":
            window show
            me "I prefer shorter ladies!"
            show emf normalblush with dissolve
            emelie " That's good to hear!"
        "I don't really have a height preference.":
            window show
            me "I don't really have a height preference."
            show emf normalblush with dissolve
            emelie " That's cool!"
    show emf insecure
    show emeswim normal
    with dissolve
    emelie " I don't think I have a big preference personally..."
    show emeye side1 at right:
        zoom 1.1 yalign 0.0 xalign 1.1
    show emeswim out
    with dissolve
    emelie " but I'm really short so almost everyone is taller than me! "
    emelie "It can be a bit annoying with people petting me on the head and crouching down whenever they talk to me."
    hide emeye with dissolve
    emelie " Makes me feel like I'm being talked down to!"
    show emf wide with dissolve
    emelie "..."
    show emeswim think
    show emf think
    with dissolve
    emelie " I guess I really am being talked down to in the literal sense if they're taller. "
    show emeye normal at right:
        zoom 1.1 yalign 0.0 xalign 1.1
    with dissolve
    emelie "But when they crouch down to \" get on my level \" is when it feels bad!"
    me " I'll keep that in mind!"
    show emeswim normal
    show emf normal
    hide emeye
    with dissolve
    emelie " You're right around Maple's and Victoria's height!"
    show emeswim out
    show emf normalblush
    with dissolve
    emelie " With Bronwen being a bit taller!"
    emelie "..."
    show emeswim think
    show emf think
    with dissolve
    emelie "  And wider... musclier... stronger..."
    show emeye normal at right:
        zoom 1.1 yalign 0.0 xalign 1.1
    show emf wide
    show emeswim out
    with dissolve
    emelie " She'd probably beat you up in a fight."
    window hide
    menu:
        with dissolve

        "Yeah, she'd kick my ass for sure.":
            window show
            me "Yeah, she'd kick my ass for sure."
            show emeswim hips
            show emf laugh
            hide emeye
            with dissolve
            emelie " Haha! Try not to give her a good reason to!"
            me  "I'll do my best!"
            me " Tipping her well definitely improved her mood earlier!"
            me " But now I'm out of gold..."
            show emf smile with dissolve
            emelie " If we ever need her service again I'll make sure to give you some money so you can pay her up-front instead!"
            show emf wide with dissolve
            emelie " We wouldn't want her to break that pretty nose of yours!"



        "No way. I'd win.":
            window show
            me "No way. I'd win."
            show emeswim hips
            show emf yeaa
            hide emeye
            with dissolve
            emelie " Suuuure... And I read a stat about how 5 percent of male piggies think they have what it takes to fight a grizzly unarmed."
            emelie " I think some of you boys have an inflated sense of your fighting prowess, haha! "
            show emeswim out
            show emf surprise
            with dissolve
            emelie " Rolf once told me some grizzly's came to aid the hogs in the war when he served. And he claims they were twice his size!"
            show emeye scared at right:
                zoom 1.1 yalign 0.0 xalign 1.1
            with dissolve
            emelie " Can you imagine? TWICE THE SIZE OF ROLF?"
            " Maybe she has a point... Bronwen probably weighs twice as much as me too... "
            me " ... Okay maybe she'd win if she got lucky."
            hide emeye
            show emeswim hips
            show emf laugh
            with dissolve
            emelie " Haha!"
            emelie " Don't let her hear that or maybe she'll challenge you."





    window hide
    show blackopacity with dissolve
    show cowannouncer
    show cowpapers
    show cowhand
    with dissolve
    pause 0.2
    window show
    announcer " Next up we haaave... "
    window hide
    hide blackopacity
    hide cowhand
    hide cowannouncer
    hide cowpapers
    with dissolve
    pause 0.2
    show emeswim bellu
    show emf normalblush
    with dissolve
    window show
    emelie " Ooh! Let's pay attention!"


label NadiaChoice:
    window hide
    show blackopacity
    show vignette
    with dissolve

    show nadiapusspeen01
    show nadiapusspeen02
    with dissolve

    show screen NadiaPeenPuss
    hide nadiapusspeen01
    hide nadiapusspeen02
    $ disableAFMbutton = True
    $ preferences.afm_enable = False
    $ _skipping = False
    $ renpy.pause(hard=True)

    screen NadiaPeenPuss:
        #add "gui/choices/RolfInterrogationUI.png"

        imagebutton:
            style "mainmenunew"
            idle "images/Chapter5/BikiniContest/nadiapusspeen01.png"
            hover "images/Chapter5/BikiniContest/nadiapusspeen01hover.png"
            action Show(screen="ConfirmChoices", YesAction=Jump("pussnadia"), Choice="nadialeft", NoAction=Show(screen="NadiaPeenPuss"), transition=dissolve)

        imagebutton:
            style "mainmenunew"
            idle "images/Chapter5/BikiniContest/nadiapusspeen02.png"
            hover "images/Chapter5/BikiniContest/nadiapusspeen02hover.png"
            action Show(screen="ConfirmChoices", YesAction=Jump("peennadia"), Choice="nadiaright", NoAction=Show(screen="NadiaPeenPuss"), transition=dissolve)

    screen ChoicenadialeftDark:
        add "images/Chapter5/BikiniContest/nadiapusspeen01chosen.png"

    screen ChoicenadiarightDark:
        add "images/Chapter5/BikiniContest/nadiapusspeen02chosen.png"
label peennadia:
    hide screen NadiaPeenPuss
    hide blackopacity
    hide vignette
    with dissolve
    $ nadiapeen = True
    $ _skipping = True
    $ disableAFMbutton = False
    if cannonballskip == True:
        jump waterconvo

    show bikinizebra1 with fade
    with vpunch
    pause 1.0
    window show
    announcer "Nadia!"
    "!!"
    "Is that a bulge in her bikini?!"
    " We couldn't see that from where we were standing until she changed her pose!"
    announcer " Nadia is a zebra who loves running in the rain, and adores spending time with our previous contestant Imara! "
    play sound "audio/soundFX/Crowd/cheerclap1.wav" volume 0.5 fadein 0.5
    crowd " So striking!"
    "Nadia pulls on her bikini strings, making her bulge bounce behind the fabric."
    window hide
    play sound "audio/soundFX/FX4/clothing2.wav"
    show bikinizebra2 with dissolve
    with vpunch
    pause 1.0
    window show
    "The bulge grew!"
    play sound "audio/soundFX/Crowd/gaspcheer.wav" volume 0.3 fadein 0.5
    crowd " Ghaa!"
    emelie " Wha?!"
    me " I didn't see that coming!"
    emelie " Nudity may not be allowed but it sure seems you can push things pretty far!!"
    jump afternadia

label pussnadia:
    hide screen NadiaPeenPuss
    hide blackopacity
    hide vignette
    with dissolve
    $ nadiapeen = False
    $ _skipping = True
    $ disableAFMbutton = False
    if cannonballskip == True:
        jump waterconvo

    show bikinizebra1z with fade
    with vpunch
    pause 1.0
    window show
    announcer "Nadia!"
    "!!"
    play sound "audio/soundFX/Crowd/cheerclap1.wav" volume 0.5 fadein 0.5
    crowd " So striking!"
    "She's tugging at her tight bikini bottoms, and her slit shows through the fabric!"
    announcer " Nadia is a zebra who loves running in the rain, and adores spending time with our previous contestant Imara! "
    window hide
    play sound "audio/soundFX/FX4/clothing2.wav"
    show bikinizebra2z with dissolve
    with vpunch
    pause 1.0
    window show
    "Nadia pulls on her bikini strings, making that tight fabric slide in between her outer labia!"
    play sound "audio/soundFX/Crowd/gaspcheer.wav" volume 0.3 fadein 0.5
    crowd " Ghaa!"
    me " Wha?!"
    emelie " J-jeez! "
    emelie " Nudity may not be allowed but it sure seems you can push things pretty far!!"
    jump afternadia


label afternadia:




    window hide
    play sound "audio/soundFX/Crowd/cheerclap4.wav" volume 0.5 fadein 0.6
    show blackopacity
    with dissolve
    show holdsign
    show scoresign mid
    with dissolve
    pause 0.3
    window show

    " Looks like she got a positive response!"
    "Me and Emelie both cheer and clap!"
    window hide
    hide blackopacity
    hide holdsign
    hide scoresign mid
    with dissolve
    window show
    pause 0.2
    nadia " Thank you, thank you!"
    window hide
    hide bikinizebra1z
    hide bikinizebra2z
    hide bikinizebra1
    hide bikinizebra2
    with fade
    show emeswim out
    show emf biggersmile
    with dissolve
    window show

    emelie " So elegant! Very unique look! "
    show emf normalblush
    show emeswim normal
    with dissolve
    emelie "Just look at all those sharp, dark stripes!"
    emelie " I haven't seen anything like that before!"
    me " Yeah, me neither!"
    show emeswim hips
    show emf bigsmile
    with dissolve
    emelie " Her figure is pretty similar to Maples' too!"

    if nadiapeen == True:
        show emeswim bellu
        show emf wide
        with dissolve
        emelie " Well... Except for some noticeable differences."

        hide emeye
        show emf pout
        with dissolve
        emelie " What do ya think about her look? "
        show emf smile with dissolve
        emelie "And what about... \" packages \" bulging out like that in a bikini?"
        window hide
        menu:
            with dissolve
            "She's got beautiful curves, and bulges are super sexy!":
                window show
                me "She's got beautiful curves, and bulges are super sexy!"

                show emf laugh

            " She's got a great figure! \n The bulge makes no difference either way.":
                window show
                me "She's got a great figure! The bulge makes no difference either way."

                show emf laugh

            "She's very pretty but I'm not usually into bulges down there unless they're my own! ":
                window show

                me "I'm not really into bulges down there unless they're my own!"
                show emf normal



        hide emblush
        show emeswim out
        with dissolve
        emelie " I see!"
        show emeswim bellu
        show emf crotch
        with dissolve
        emelie " I will have to admit that I've been... paying a lot of attention to your bulge today~ "
        "Emelie looks down to my shorts, making me blush."

    if nadiapeen == False:
        show emeswim bellu
        show emf wide
        with dissolve
        emelie " And they both sure love tight bottoms that get all up in there."
        emelie " I've heard it referred to as a \" Camel Toe \" before..."
        emelie " But the term always confused me!"

        show emeswim thinky
        show emf think
        with dissolve
        emelie " Even now that I know what \" toes \" are I can't really say I see the resemblance."
        show emeswim bellu
        hide emeye
        show emf pout
        with dissolve

        emelie " What do ya think about her look? "
        show emf smile with dissolve
        emelie "And what about those super tight bikini bottoms ?"
        window hide
        menu:
            with dissolve
            "She's got great curves, and \"camel toes\" are sexy!":
                window show
                me "She's got beautiful curves, and camel toes are sexy!"

                show emf laugh

            " She's very pretty! \n The tightness of her bottoms doesn't matter much either way!":
                window show
                me "She's got a great figure! The bulge makes no difference either way."

                show emf laugh

            "She looks good but I prefer a bit more left to the imagination!" :
                window show

                me "She looks good but I prefer a bit more left to the imagination!"
                show emf normal



        hide emblush
        show emeswim out
        with dissolve
        emelie " I see!"
        window hide
        show emf wide
        show emeye down4 at right:
            zoom 1.1 yalign 0.0 xalign 1.1
        with dissolve
        play sound "audio/soundFX/Dun.wav" volume 1.0
        with vpunch
        pause 0.2
        window show
        emelie " I-It seems I've got a bit of a \" camel toe \" going on down there myself!"
        hide emeye with dissolve
        emelie " I blame the size for being slightly too small!"
        show emeswim bellu
        show emf crotch
        with dissolve
        emelie " But when it comes to tight bottoms... I've got to admit I've been paying a lot of attention to yours today~ "
        "Emelie looks down to my bulging shorts, making me blush."
    window hide
    show blackopacity with dissolve
    show cowannouncer
    show cowpapers
    show cowlookdown
    with dissolve
    pause 0.2
    window show

    announcer " And now for our final contestant... "
    hide cowlookdown
    show cowhand
    with dissolve

    announcer " Donna, the hippo!"
    window hide
    hide cowpapers
    hide cowhand
    hide cowlookdown
    hide blackopacity
    hide cowannouncer
    with dissolve
    pause 0.2
    show emeswim out
    show emf wide
    with dissolve
    window show
    emelie " Ooh, I've been waiting for her!"
    "Me and Emelie put our focus back toward the stage!"
    play sound "audio/soundFX/FX5/donna.wav" volume 0.7
    show bikinihippo1
    with hpunch
    donna " BRAAAHH!"
    "Holy shit, she's loud!"
    " The crowd erupts with a loud roar!"
    play sound "audio/soundFX/Crowd/donnacheer.wav" volume 0.5 fadein 0.5
    crowd " YOU ARE GORGEOUS!"
    announcer " Donna loves swimming, good food and Hog Haven!"
    show bikinihippo2 with dissolve
    with hpunch

    donna " I love you all! AND I love your snacks!"
    play sound "audio/soundFX/Crowd/cheerclap3.wav" volume 0.4 fadein 0.3
    crowd " And we love YOU!!"
    window hide
    show blackopacity
    with dissolve
    show holdsign
    show scoresign alls
    with dissolve
    with vpunch
    pause 0.3
    window show
    "Wha-"
    " A lot of perfect tens all of a sudden!?"
    play sound "audio/soundFX/Crowd/cheerclap1.wav" volume 0.6 fadein 0.2
    crowd " YEEES! "
    crowd "Look at those teeth! Those curves! That's the most beautiful woman I've ever seen!"
    "People love her!"
    " Me and Emelie cheer and clap, then look to each other."
    window hide
    hide blackopacity
    hide holdsign
    hide scoresign
    with dissolve
    window show
    donna " Thank you, sweeties~"
    window hide
    hide bikinihippo1
    hide bikinihippo2
    hide cowannouncer
    with fade
    pause 0.2
    show emf surprise
    show emblush at right:
        zoom 1.1 yalign 0.0 xalign 1.1
    with dissolve
    window show
    emelie " Wow! The crowd sure loves her!"
    show emeswim hips
    show emear high at right:
        zoom 1.1 yalign 0.0 xalign 1.1
    show emf surprise2

    with dissolve
    emelie " Especially all the pigs! They all gave her perfect tens! "
    hide emear
    hide emblush
    show emeswim think
    show emf think
    with dissolve
    emelie " Maybe they have a type..."
    #crowdguy " Miss Elephant.. why aren't you on stage? You're a perfect 10 too! Your curves, tusks, and THAT SNOUT!"
    #elephant " I weigh too much. A ton."
    #elephant " I'd break the stage."
    #crowdguy " How much?"
    #elephant " A literal ton. over 1000 pounds."
    #elephant " And I'm on a diet."
    #crowdguy " !! Ohh mama!"
    emelie " Piggies are known to love a little extra chub... and big tusks!"
    show emeye normal at right:
        zoom 1.1 yalign 0.0 xalign 1.1
    with dissolve
    emelie " What do you think about big, toothy gals?"
    hide emeye
    show emeswim normal
    show emf wide
    with dissolve
    emelie "Do you like when girls can overpower you physically and are bigger than you?"
    show emeswim bellu
    show emf yeaa
    with dissolve
    emelie " Or do you like smaller ladies you can boss around with your strength?"
    window hide
    menu:
        with dissolve
        "I like physically bigger gals who can overpower me!":
            window show
            me "I like physically bigger gals who can overpower me!"
            show emeswim out
            show emf laugh
            with dissolve
            emelie " Interesting! I'll have to start doing push-ups or something so I can pin you down, haha!"
            " We both chuckle at the idea."

        " No real preference!":
            window show
            me " No real preference!"
            show emf really
            show emeswim out
            with dissolve
            emelie "..."
            emelie " That's sort of a boring answer."
            me "!!"
            show emf laugh with dissolve
            emelie "But I shouldn't blame you for liking a variety of things!"
        "I like to be physically bigger and stronger!":
            window show
            me "I like to be physically bigger and stronger!"
            show emf sooth
            show emeswim out
            with dissolve
            emelie " Hmm... You do seem to like to apply a little force..."

    window hide
    show blackopacity with dissolve
    show cowannouncer
    show cowpapers
    show coweyeclose
    with dissolve
    pause 0.2
    window show
    announcer " Wooonderful! "
    hide coweyeclose
    show cowlookdown
    with dissolve
    announcer "It seems we have our results! "
    window hide
    hide blackopacity
    hide cowannouncer
    hide cowpapers
    hide cowlookdown
    with dissolve
    show emeswim out
    show emf wide
    with dissolve
    window show
    emelie " Ooh! I'm so curious!! "
    show emf insecure
    show emeye side1 at right:
        zoom 1.1 yalign 0.0 xalign 1.1

    with dissolve
    emelie " I don't think I could choose a favorite fairly... I'm really biased toward Maple with her being a Hog Haven local and all!"
    hide emeye with dissolve
    emelie "  Who was your favorite? "
    window hide
    menu:
        with dissolve
        "Maple!":
            window show
            me "Maple!"
            show emf laugh
            show emear high at right:
                zoom 1.1 yalign 0.0 xalign 1.1
            with dissolve
            emelie " Same taste as me, then! Woo!"

        "Imara!":
            window show
            me "Imara!"
            show emf surprise with dissolve
            emelie " Going for the long lady, huh? Long legs, long neck, long tongue! "
            show emf bigsmile
            show emear high at right:
                zoom 1.1 yalign 0.0 xalign 1.1
            with dissolve
            emelie " I like it!"
        "Nadia!":
            window show
            me "Nadia!"
            show emf normalblush with dissolve
            emelie " Oooho! Yeah, she sure put on a unique performance!"
            show emf laugh
            show emear high at right:
                zoom 1.1 yalign 0.0 xalign 1.1
            with dissolve
            emelie " Or maybe you just like those stripes? Haha!"
        "Donna!":
            window show
            me "Donna!"
            show emf smile with dissolve
            emelie " Same taste as the crowd it seems! "
            show emf laugh
            show emear high at right:
                zoom 1.1 yalign 0.0 xalign 1.1
            with dissolve
            emelie " Makes sense... That's a whole lot of woman to love!"

label results:
    #announcer " And the winners aaaare-"
    window hide
    show blackopacity with dissolve
    show cowannouncer
    show cowpapers
    with dissolve
    pause 0.2
    window show
    announcer " And the winner iiiiis- "
    #drumroll
    show coweyeclose
    hide cowpapers
    show cowhand
    with dissolve
    with vpunch
    announcer "Donna!!"
    hide coweyeclose
    show cowpapers
    hide cowhand
    show cowlookdown
    with dissolve
    announcer " Followed by Maple, Nadia, then Imara!"
    window hide


    show black with fade
    window show
    "The contestants give the audience a final thank you and start walking off the stage."
    window hide
    show hippotrophy with fade
    play sound "audio/soundFX/Crowd/donnacheer2.wav"  volume 0.2 fadein 0.5
    with vpunch
    pause 1.0
    window show
    donna " Wahoo! You're far too generous, Hog Haven!"
    maple " Good job, everyone!"
    announcer " It was a pleasure seeing you all compete!"
    imara " {size=-2}... Last place, huh?"
    nadia " You're MY number one, sweetie!"
    "Maple cheerfully approaches me and Emelie."

    window hide
    hide hippotrophy
    hide cowannouncer
    hide coweyeclose
    hide emear
    hide cowhand
    hide cowlookdown
    hide cowpapers
    hide cowsurprise
    hide bikinigrp1
    hide bikinigrp2
    hide bikinigrp3
    hide bikinigrp4
    hide emf
    hide emeye
    hide blackopacity
    show bikinigrouplookem behind emeswim
    show afterkinipic behind emeswim
    hide bikinigrouplook
    show emeswim normal behind emf at right:
        zoom 1.1 yalign 0.0 xalign 1.1
    hide black
    with fade
    pause 0.3
    show emeswim normal behind emf at right:
        linear 0.5 yalign -0.20 xalign 1.0 zoom 0.95
    pause 0.5
    show emeswim normal behind emf at right:
        yalign -0.20 xalign 1.0 zoom 0.95
    play sound "audio/soundFX/Run2.wav"
    show maps base:
        xoffset -200
    with easeinleft
    pause 0.3
    show maps cheerup
    show maf shiny :
        xoffset -200
    with dissolve
    show emeye side1 at right:
        yalign -0.20 xalign 1.0 zoom 0.95
    with dissolve
    window show
    #Gold medal! Silver Medal! Tied bronze medal!"
    #announcer " Hippo,Maple,Nadia,Raffe!"


    #Maple has trophy

    maple " Woo! Second place!"
    show maf closeyes with dissolve
    maple " I'm glad people liked my new bikini design!"
    show mapeye right :
        xoffset -200
    with dissolve
    maple " Tough competition this year though, huh?"
    show emf biggersmile behind emeye at right:
        yalign -0.20 xalign 1.0 zoom 0.95
    with dissolve
    emelie " You did great! Pretty close to getting the trophy too, I think!"
    show maps out
    hide mapeye
    with dissolve
    maple " Not really. But that's okay! "
    show mapeye right :
        xoffset -200
    show maf grintongue
    with dissolve
    maple " I won last year after all, so I've already got one at home gathering dust!"
    maple "I'm not really in it to win anyways, but it's flattering when it happens!"
    show maf happydown2
    show maps tidup
    with dissolve
    maple " Now DID YOU SEE the giraffe girl Imara?! Such an amazing style!"
    show maps tiddown
    show maf insecure
    with dissolve
    maple " I can't believe she got last place. "
    show maf gloss
    show maps cheerup
    with dissolve
    maple "She was so hot! And did you see that tongue? She had three piercings in it! I never even thought of putting a single one there!"
    show emeswim out
    show emf fluster
    with dissolve
    emelie " Y-you sure revealed some piercings on yourself too, Maple... "
    show emf sooth
    with dissolve
    emelie "That's pretty hot."
    #emelie " Or what do you think, Protag?"
    #me " Uuuh-"
    #Choice
    hide mapeye
    show maf closeyes
    with dissolve
    maple " Haha, glad you like!"
    show maps hips
    show maf opentongue
    with dissolve
    maple " I'm going to have to try piercing my own tongue later!"
    show emf weirdo2
    show emeswim panic
    show emeye side3
    show emear high at right:
        yalign -0.20 xalign 1.0 zoom 0.95
    with dissolve
    emelie " W-wha isn't that a scary thought?"
    show mapeye right :
        xoffset -200
    with dissolve
    maple " Not really!"
    show maps out
    show maf openn
    with dissolve
    maple " Did you know I was a hairdresser a few years back before I moved to Hog Haven? I would groom fur and all sorts of things! "
    show emeye side1
    show emeswim out
    show emf pout
    hide emear
    with dissolve
    emelie "I had no idea! "
#    maple " As a hairdresser a lot of people want their ears pierced! And I've pierced so many different styles of ears that a tongue should be no problem!"
    #emelie " You sure do have great hair, Maple! So that makes sense! Very volumous! "
    #me " What made you change proffession?"
    show maf shy
    show maps hips
    with dissolve
    maple "But I had to change profession... Piggies don't have fur the same way canines do and a lot of the men seem to lose their hair pretty young!"
    show maf hapigrin with dissolve
    maple "Back home I had these two poodle regulars who made me a fortune, haha!"
    #me " Oh that's interesting! "
    " Poo...dle?"
    #"She looks confused."
    show emf smile
    show emeye side2
    show emeswim hips
    with dissolve
    emelie " You sure do have great hair, Maple! So that makes sense! Very volumous! "
    hide mapeye
    show maf closeyes
    with dissolve
    maple " Thank you! "
    maple " As a hairdresser, I learned how to pierce people's ears too! "
    show mapeye right :
        xoffset -200
    show maf lookbod
    show maps back
    with dissolve
    maple " It's quick enough and can serve as a really nice accent to certain hairstyles!"
    maple "Then one day I got a little experimental on myself... "
    show maps tidup
    show mapeye rightwink
    show maf fronty
    with dissolve
    maple " I figured nipples would look kinda pretty pierced too. "
    show emf insecure
    show emeye side1
    show emeswim bellu
    with dissolve
    emelie " But didn't it hurt?... I kinda wanted my ears pierced for a while but I got a little scared."
    show mapeye right
    show maf lookright
    with dissolve
    maple " Oh, it doesn't hurt much! No need to worry!"
    show mapeye rightwink
    show maps out
    show maf grin
    with dissolve
    maple " If you change your mind in the future you know where to find me!"
    show emf pout
    show emeswim out
    with dissolve
    emelie " I'll think about it!! "

label PigShowcase:

    announcer " Next up.. Time for the pig contestants!"
    window hide

    hide beachsmokeemelie
    hide emf
    hide emeye
    show mapeye right
    with dissolve
    show emeswim hips with dissolve
    show emeswim hips at right:
        linear 0.4 yalign -0.20 xalign 0.55 zoom 0.95
    pause 0.4
    show emeswim hips at right:
        yalign -0.20 xalign 0.55 zoom 0.95
    show mapeye down with dissolve
    show emf smile at right:
        yalign -0.20 xalign 0.55 zoom 0.95
    with dissolve
    window show
    emelie " I've been waiting to see what my fellow piggies have to offer!"
    window hide
    show bikinipiggies2 behind emeswim , emelon
    show isab2 behind emeswim , emelon
    with dissolve
    window show
    piggirl " ... We can't follow that performance! "
    piggirl "Donna got perfect ten's across the board! My physique is nothing compared to hers!"
    piggirl2 " Y-yeah... I think I'm pulling out too..."
    show isab3 behind emeswim , emelon
    with dissolve
    announcer " N-nobody??... We usually have at least a few contestants!"
    show emf sad at right:
        yalign -0.20 xalign 0.55 zoom 0.95
    show emeswim out
    with dissolve
    emelie " Oh no... It sounds like the other pig girls are getting cold feet! "
    emelie "They think they'll disappoint going up after Donna!"
    show maps tiddown
    show maf biggrinz
    with dissolve
    maple " Jeez! Following a perfect performance would be pretty daunting!"
    show emf gross with dissolve
    emelie " Yes..."
    show emf decided
    show emeswim normal
    with dissolve
    emelie "But as the princess of this kingdom... "
    emelie "I think it's my duty to go up there and instill some confidence in the girls!"
    emelie " Even if I do poorly they need to see a fellow piggy on stage! "
    show emeswim hips
    show emf decided2
    with dissolve
    emelie "To show that we pig girls are brave and confident in our bodies!"
    me " That's a great idea!"
    show maf biggrin
    show maps out
    with dissolve
    maple " Yes, Emelie! That sounds like an amazing goal!"
    window hide
    show emf panic
    show emeswim panic
    show emear high at right:
        yalign -0.20 xalign 0.55 zoom 0.95
    with dissolve
    #play sound "audio/soundFX/Dun.wav" volume 0.5
    with vpunch
    window show
    emelie " But... I don't know how to pose! "
    emelie "I'm so nervous!! "
    show emf panic2
    with dissolve
    with hpunch
    emelie "Showing my body in front of everyone is embarrassing!"
    " Her confidence quickly shattered!"
    me " You'll do great!"
    hide mapeye
    show maf closeyes
    show maps cheerup
    with dissolve
    maple " The sexier the pose the better!"
    show emeye maple at right:
        yalign -0.20 xalign 0.55 zoom 0.95
    show emf insecure
    show emeswim out
    hide emear
    with dissolve
    emelie " R-really? "
    emelie "I'll... see how I feel when I get on stage..."
    hide emeye
    show emf concern
    with dissolve
    emelie " What do you think I should do, [Protagonist]?? "
    emelie "Strike a sexy pose or not-"
    hide isab3
    show isab2 behind emeswim , emelon
    with dissolve
    with vpunch
    announcer " Last chance!"
    show emf panic
    show emear high at right:
        yalign -0.20 xalign 0.55 zoom 0.95
    with dissolve
    emelie " Eek!! I'm up!"
    window hide
    hide emf
    hide emear
    hide emeswim
    hide beachsmokeemelie
    with dissolve
    pause 0.2
    play sound "audio/soundFX/poke_1.wav" volume 0.3
    if modest == True:
        show bikiniemeliebl with dissolve
    if modest == False:
        show bikiniemelie with dissolve

    hide isab2
    with dissolve
    hide bikinipiggies2
    show bikinipiggies3b
    hide afterkinipic
    with dissolve
    pause 0.3
    window show
    "Before I can answer, Emelie runs up on stage!"
    announcer " There we go! Welcome!"
    show bikiniemelieface2 with dissolve
    emelie "T-thank you!"
    announcer " And what's your name? You don't seem to have signed up beforehand!"

    emelie " My name is Emel-"
    window hide
    play sound "audio/soundFX/Dun.wav" volume 1.0
    $ renpy.music.set_volume(0.80, delay=0, channel='music')
    pause 0.1
    $ renpy.music.set_volume(0.60, delay=0, channel='music')
    pause 0.1
    $ renpy.music.set_volume(0.40, delay=0, channel='music')
    pause 0.1
    $ renpy.music.set_volume(0.20, delay=0, channel='music')
    pause 0.1
    $ renpy.music.set_volume(0.00, delay=0, channel='music')
    hide bikiniemelieface2
    show bikiniemelieface3
    with dissolve
    with vpunch
    window show
    emelie " Uhhh..."
    "Oh shit, she wasn't supposed to expose herself as the princess!"
    hide bikiniemelieface3
    show bikiniemelieface3b
    with dissolve
    with vpunch
    emelie "-ia!"
    emelie "My name is Emelia!"

    crowd " Hmm... She looks familiar but I can't put my finger on it..."
    announcer " Aha! Beautiful name!"
    $ renpy.music.set_volume(0.20, delay=0, channel='music')
    pause 0.1
    $ renpy.music.set_volume(0.40, delay=0, channel='music')
    pause 0.1
    $ renpy.music.set_volume(0.60, delay=0, channel='music')
    pause 0.1
    $ renpy.music.set_volume(0.80, delay=0, channel='music')
    pause 0.1
    $ renpy.music.set_volume(1.00, delay=0, channel='music')
    hide bikiniemelieface3b
    show bikiniemelieface3c
    with dissolve
    "Emelie relaxes. "
    hide mapeye
    show maf ofoa
    show maps base
    with dissolve
    maple " Puuh, she just barely saved it!... "
    #maple "What do you think about her?"
    #me " She's perfect!"
    #maple " Aww!"

    announcer " Now show us what you've got!"
    hide bikiniemelieface3c with dissolve
    "Emelie nods and readies herself!"
    window hide
    if modest == True:
        show embikiniposebl with fade
    if modest == False:
        show embikinipose with fade
    with vpunch
    pause 0.6
    window show
    "She strikes a pose!"
    me " {size=+2}Woo, that's great!!{/size}"
    maple " {size=+2}Amazing!!{/size}"
    "Maple lowers her voice. "
    maple " {alpha=*0.88}{size=-4} D-Double thumbs up? Really? {/alpha}{/size}"
    "We do our best to cheer her on but the crowd reaction isn't anything crazy."
    play sound "audio/soundFX/Crowd/cheerclap4.wav" volume 0.5 fadein 0.6
    crowd " She's cute!"

    maple "{alpha=*0.88}{size=-4}You're really looking at those curves, huh?{/alpha}{/size}"
    me " {alpha=*0.88}{size=-4}It's... Because your swimsuit looks so good on her!{/alpha}{/size}"
    maple " {alpha=*0.88}{size=-4}I agree! so let's see her really model it!{/alpha}{/size}"
    with vpunch
    maple " {size=+2}Come on, girl! Work it! You can go sexier!{/size}"
    show embikiniposeface2 with dissolve

    "Emelie looks over to me with a questioning look, checking in with me to see if she should escalate things or not!"
    window hide
    menu:
        with dissolve


        "You can push the sexiness more! \n It's what the others have done and the crowd loves it!":
            window show
            me"You can push the sexiness more! It's what the others have done and the crowd loves it!"
            window hide

            if modest == True:
                show embootybikini01bl with fade
            if modest == False:
                show embootybikini01 with fade
            play sound "audio/soundFX/Dun.wav" volume 0.7
            with vpunch
            pause 0.6
            window show
            "Emelie strikes a butt-presenting pose!"
            play sound "audio/soundFX/Crowd/cheerclap2.wav" volume 0.2 fadein 0.6
            crowd " Ghaah, yes!"
            " The crowd loves it! The scores are getting higher!!!"
            #crowd " More!!"
            "Emelie throws me yet another questioning look."
            " I wonder if pushing things just a little further will grant even better scores and might instill more confidence in the other pig ladies!"
            window hide
            menu:
                with dissolve
                "You got it! Push it even further!":
                    window show
                    me " You got it! Push it even further!"
                    window hide
                    play sound "audio/soundFX/Dun.wav" volume 0.7

                    if modest == True:
                        show embootybikini02bl with dissolve
                    if modest == False:
                        show embootybikini02 with dissolve
                    with vpunch

                    pause 0.6
                    window show
                    "!!"
                    " I don't know what else I expected! I guess Emelie didn't have many other ways to escalate things! "
                    maple " {alpha=*0.88}{size=-4} W-woah, not bad! Seems she learned a thing or two from observing me and the girls, huh?!{/alpha}{/size}"

                    play sound "audio/soundFX/Crowd/donnacheer2.wav" volume 0.4 fadein 0.6
                    crowd " Woooo!!"
                    show embootysmile with dissolve
                    "Emelie smiles as she hears the crowd go wild!"
                    window hide
                    show blackopacity
                    with dissolve
                    play sound "audio/soundFX/Crowd/cheerclap3.wav" volume 0.4 fadein 0.3
                    show holdsign
                    show scoresign alls
                    with dissolve
                    pause 0.3
                    window show
                    $ emcompetition = " high "
                    "Woah! Perfect tens! The crowd loves it!"

                "I think that's enough! Amazing!":
                    window show
                    hide blackopacity
                    me "I think that's enough! Amazing!"
                    window hide
                    show blackopacity behind holdsign
                    with dissolve
                    play sound "audio/soundFX/Crowd/cheerclap4.wav" volume 0.5 fadein 0.6
                    show holdsign
                    show scoresign high
                    with dissolve
                    pause 0.3
                    window show
                    "She gets a good score!!"
                    $ emcompetition = " middle "


        "I think that's good enough! Great job!":
            window show
            me"I think that's good enough! Great job!"
            hide embikiniposeface2 with dissolve
            "Emelie smiles as I encourage her."
            window hide
            show blackopacity
            with dissolve
            play sound "audio/soundFX/Crowd/cheerclap1.wav" volume 0.5 fadein 0.6
            show holdsign
            show scoresign mid
            with dissolve
            pause 0.3
            window show
            $ emcompetition = " low "
            "She gets a pretty decent score, even with the modest pose!"
    window hide
    hide blackopacity
    hide holdsign
    hide scoresign mid
    with dissolve
    pause 0.3
    if emcompetition == " middle ":
        show embootysmile with dissolve
    window show
    emelie " T-thank you, everyone!"
    window hide

    hide embikiniposeface2
    hide embootybikini01bl
    hide embootysmile
    hide embootybikini02bl
    hide embootybikini01
    hide embootybikini02
    hide embikiniposebl
    show bikinipiggies3
    hide bikinipiggies3b
    show black
    with fade
    window show
    #Emelie gets a pretty solid score, even with the modest pose!"
    announcer " Aaaand the winner of the pig competition is... Emelia!"
    play sound "audio/soundFX/Crowd/cheerclap4.wav" volume 0.5 fadein 0.6
    if emcompetition == " high ":
        crowd "Deserved! Sexiest piggy ever!!"

    if emcompetition == " middle ":
        crowd "Great job!!"

    if emcompetition == " low ":
        crowd "Brave of you to step up on your own!"

    "We all cheer for Emelie as she receives her trophy!"

    window hide
    if modest == True:
        show bikiniemeliebltrophy
    if modest == False:
        show bikiniemelietrophy
    hide bikiniemeliebl
    hide embikinipose
    hide embikiniposebl
    hide bikiniemelie
    show maf hapuface
    hide black
    with fade
    pause 0.4
    hide bikiniemeliebltrophy
    hide bikiniemelietrophy
    with dissolve


    show emeswim trophy at right:
        yalign -0.20 xalign 0.55 #1.25
        zoom 0.95
    show emf insecure at right:
        yalign -0.20 xalign 0.55 #1.25
        zoom 0.95
    show emblush at right:
        yalign -0.20 xalign 0.55 #1.25
        zoom 0.95
    show afterkinipic behind maps
    with dissolve
    #show beachsmokeemelie behind emeswim with dissolve
    #show maps base:
        # linear 0.5 xoffset -100
    pause 0.3
    window show

    emelie " Phew... that was embarrassing!"
    show mapeye down :
        xoffset -200
    show maf biggrin
    with dissolve
    maple " You did amazing, hun!"
    show emeye maple behind emblush at right:
        yalign -0.20 xalign 0.55 #1.25
        zoom 0.95
    with dissolve
    emelie " Really?"
    if emcompetition == "low":
        maple " I would've probably pushed it a little more buuuut-"
    me " Yeah you did incredible! "
    show emf normalblush
    hide emeye
    with dissolve
    emelie " T-thanks, you two!"
    window hide
    hide emblush
    hide mapeye
    show bikinipiggies4 behind emeswim , emelon
    hide bikinipiggies3
    with dissolve
    window show
    "The two pig girls in the back look toward each other."
    piggirl " I... think I want to be on stage after all! "
    piggirl "Even if the competition is over!"
    piggirl2 " Me too!"
    window hide
    hide afterkinipic
    hide bikinipiggies
    hide bikinipiggies4
    hide bikinipiggies3b
    with dissolve
    hide maf
    hide emf
    hide emblush
    play sound "audio/soundFX/poke_1.wav" volume 0.3
    show bikinipiggies5 behind maps
    with dissolve
    show emeswim:
        linear 0.5 xoffset 150
    pause 0.5
    show emeswim:
        xoffset 150
    show maps:
        linear 0.5 xoffset -260
    pause 0.5
    show maps:
        xoffset -260
    show emeye side1 behind emblush at right:
        yalign -0.20 xalign 0.55 #1.25
        zoom 0.95 xoffset 150
    show mapeye right:
        xoffset -260
    with dissolve
    window show
    " They run up on stage and dance!"
    show isab4 with dissolve

    play sound "audio/soundFX/Crowd/cheerclap3.wav" volume 0.4 fadein 0.3
    crowd " Yaaaaayy!"
    piggirl " I don't know why we were so insecure! This is so much fun! "
    piggirl2 " Yes! Next year we'll compete for sure!"
    me " Wow, Emelie! You really inspired them!"
    show maf gloss:
        xoffset -260
    show maps tiddown
    hide mapeye
    with dissolve
    maple " Aw that is so sweet!"
    show emf laugh at right:
        yalign -0.20 xalign 0.55 #1.25
        zoom 0.95 xoffset 150
    hide emeye
    with dissolve
    emelie " Yay!"
    "Emelie looks proud and happy!"
    show emf wide with dissolve
    emelie " And I got a trophy!"
    show emf surprise2 with dissolve
    emelie " But I'm not sure if I should be happy about it or not... since I was the only competitor."
    me " Be proud! It takes courage to step on stage in front of people, no matter what!"
    show emf normalblush with dissolve
    emelie " O-okay! That's a good way of seeing it! "
    show maps out
    show maf closeyes
    with dissolve
    maple " And [Protagonist] sure loved the view!"
    maple " He couldn't keep his eyes off ya!"
    show emblush at right:
        yalign -0.20 xalign 0.55 #1.25
        zoom 0.95 xoffset 150
    show emf insecure
    with dissolve
    "Emelie blushes and sweats a little. "
    show emeye side1 behind emblush at right:
        yalign -0.20 xalign 0.55 #1.25
        zoom 0.95 xoffset 150
    with dissolve

    emelie " Seems this whole thing got me all nervous and sweaty!"
    " A drop of sweat falls down my own forehead. "
    "Trying not to pop a boner this whole time has put a real strain on me!"
    me " Y-yeah, me too!"
    me " Must be the sun!"
    show emf biggersmile with dissolve
    emelie " Let's go for a dip!"
    me " Sounds like a good idea!!"
    show mapeye down:
        xoffset -260
    show maps hips
    with dissolve
    maple " I'll follow along!"
    window hide

    scene black with fade
    window show
    "We take a stroll back to the beach."
    window hide
    scene bg bigbeach
    show blackshake at truecenter behind bg
    show bgbeach1
    show bgbeachactive2
    with fade
    pause 0.2
    play sound "audio/soundFX/run2.wav"
    show maps base
    with easeinright
    play sound "audio/soundFX/run2.wav"
    show emeswim trophy at right:
        yalign -0.20 xalign 1.00
        zoom 0.95
    with easeinright
    show beachsmokeemelie behind emeswim
    with dissolve


    pause 0.5
    window show

    "As we arrive on the beach I spot Nadia, Imara, and Donna taking a nice dip of their own!"
    #maple " Oh there's nadia and giraffe! I wanted to talk to them! I'll go have a lil swim! See you in the water or later!"
    show maps out
    show maf bigg
    with dissolve
    maple " That contest was so inspiring!"
    show maf closeyes with dissolve
    maple " I'll be on my way back to the shop right away!"
    show emf smile at right:
        yalign -0.20 xalign 1.00
        zoom 0.95
    show emeye side1 at right:
        yalign -0.20 xalign 1.00
        zoom 0.95
    show emeswim hips
    with dissolve
    "Emelie puts her trophy down."
    emelie " That's great, Maple!"
    show maps tidup
    show maf baseface
    show mapeye right
    with dissolve

    maple" I just can't wait to try some of these new fashion ideas out!"
    hide mapeye
    with dissolve
    maple " Come by any time, cuties!"
    #Next day she has tongue pierced"
    me " Sure, Maple!"
    show emf bigsmile
    show emeswim out
    with dissolve
    emelie " Yes yes! Have fun!"
    show maf wink2
    show maps peacehigh
    with dissolve
    maple " Buhbye, sweethearts!~"
    window hide
    play sound "audio/soundFX/run2.wav"
    hide maps
    hide maf
    with easeoutleft
    pause 0.5
    hide emeye
    show emeswim bellu
    show emf pout
    with dissolve
    window show
    emelie " Whew, I'm really happy Maple showed up so we didn't miss out on all that!"
    me " Yeah, was a feast for the eyes for sure!"
    show emf yeaa
    show emeswim normal
    with dissolve
    emelie " Oh yeah? I bet it was real comfy just standing back to watch while I was freaking out on stage."
    show emeswim hips
    show emf grin
    with dissolve
    emelie " I think it's about time we add a category for men so you can get your cute butt up there next year!"
    show emf laugh
    show emeswim out
    with dissolve
    emelie " I'll get on that first thing in the morning! Hahaha!"
    me " Only if I can bring Billy! "
    me " He'll protect me from the crowd's lustful gaze..."
    show emeswim normal
    show emf yeaa
    with dissolve
    emelie " Yeah? "
    emelie "If armor is allowed on stage he might be there to save ya... but if not then there's no way you're getting him up there!"
    window hide
    show emeswim hips
    show emf evil
    show emear high behind emf at right:
        yalign -0.20 xalign 1.00
        zoom 0.95
    with dissolve
    play sound "audio/soundFX/Dun.wav" volume 0.7
    with vpunch
    window show
    emelie " And as the princess, I can write the rules however I want!!! "
    emelie "Mwahaha!"
    "I've never seen Emelie look so scary before!!"
    show emeswim normal
    show emf sleep
    hide emear
    with dissolve
    emelie "But a princess also needs to show restraint. It'd be wrong to abuse all the power that comes with the crown."
    show emf normalblush with dissolve
    emelie "So you're safe for now!"
    me " Puh! I almost made a run for it!"
    show emf laugh
    show emeswim out
    with dissolve
    emelie " Haha!"
    show emeswim bellu
    show emf pout
    with dissolve
    emelie "Hmm... But I do wonder what Billy is up to-"
    window hide
    show billys veggies at left:
        yalign 0.4 xalign -0.16
    show bill cryy at left:
        yalign 0.4 xalign -0.16
        xoffset 65
    show billyblush at left:
        yalign 0.4 xalign -0.16
        xoffset 65
    with easeinleft
    with vpunch
    pause 0.3
    window show
    billy " Buuuddyyyyyy..."
    me " B-Billy!"
    show emeye side1 at right:
        yalign -0.20 xalign 1.00
        zoom 0.95
    show emeswim normal
    show emf pout
    with dissolve
    " He's got my produce stuffed into just about every crevice of his armor!"
    hide emblush
    show bill drool
    with dissolve
    billy " Your veggies are just THE BEST!"
    billy " And I recognize the taste of these carrots! "
    billy " Maybe you're the reason why Hog Haven has such incredible carrot cakes! "
    billy " You certainly deserve some time off for all the hard work you've put into your farm!"
    me " Haha, thank you, Billy!"
    me " My body sure enjoys some rest from all the manual labor!"
    show bill baseface
    hide billyblush
    with dissolve
    billy " I bet!"
    show bill laughface with dissolve
    with hpunch
    billy " OoOoh!~ And what's that down there, princess? A trophy?"
    "Emelie reaches down for her trophy."
    play sound "audio/soundFX/Get.mp3"
    hide emeye
    show emf laugh
    show emeswim trophy
    with dissolve
    emelie " Yes! I won one! "
    show emeye side1 at right:
        yalign -0.20 xalign 1.00
        zoom 0.95
    show emf insecure
    with dissolve
    emelie "Not that I had much competition... or any competition, really."
    me " You would've won either way!"
    hide emeye
    show emf normalblush
    with dissolve
    emelie " Haha! You're sweet."
    show bill squint with dissolve
    billy " It's beautiful! I'm so proud of you!"
    show bill waa at left:
        yalign 0.4 xalign -0.16
        xoffset 65
    with dissolve
    billy" I'll run and get it to safety right away!"
    window hide
    show billys veggiescucumber with dissolve
    play sound "audio/soundFX/Get.mp3"
    show emeswim normal
    show billys veggiestrophy
    hide bill
    with dissolve

    window show

    "He puts the big pumpkin down and grabs the trophy."
    billy" Be right back!"
    window hide
    stop music fadeout 0.3
    play sound "audio/soundFX/FX5/ricochet.wav" volume 0.6
    show billys:
        linear 0.2 xoffset -1500
    pause 0.2
    show billys:
        xoffset -1500
    show billypoof
    show emeswim out
    show emf wide
    show emeye side3 at right:
        yalign -0.20 xalign 1.00
        zoom 0.95

    with hpunch
    pause 0.4
    hide billypoof with dissolve
    pause 0.3
    window show
    #billy " Now I need to take a dip.. I got so sweaty."

    "Billy blitzes off with the trophy at lightning speed!"
    hide emeye
    show emf wide
    show emeswim normal
    with dissolve
    emelie " Woah! Those veggies sure energized him, huh?"
    play music "audio/Seagul.wav" fadein 5.0 volume 0.4
    show emf normalblush
    show emeswim hips
    with dissolve
    emelie "He should be back soon! "
    show emf laugh with dissolve
    emelie " Let's take a little dip in the meantime!"
    me " Okay!"

    #bath scene of swimming and stuff with Emelie
    window hide
    scene black with fade
    window show
    " We slowly walk out into the ocean water."
    stop music fadeout 2.0
    window hide
label waterconvo:
    scene bg swimmingem
    show blackshake at truecenter behind bg
    if nadiapeen == True:
        show swimgroup one
    else:
        show swimgroup onez
    show emeswim bellu at right:
        yalign 0.16 xalign 1.26
        zoom 1.20
    show emf normalblush at right:
        yalign 0.16 xalign 1.26
        zoom 1.20
    show bgswimem


    show bgswimdock
    play sound "audio/soundFX/FX2/water-slosh-spashing-3.wav" volume 0.5

    with fade
    play music "audio/starting-out-waltz-vivace-by-kevin-macleod-from-filmmusic-io.mp3" fadein 0.1 volume 0.3
    pause 0.3
    window show

    "We stop as the water hits Emelie's belly."
    show emf smile
    with dissolve
    play sound "audio/Seagul.wav" fadein 1.0 volume 0.8
    emelie " I always take it slow when walking out into the ocean!"
    emelie " The water is warm today but I still like some time to adjust!"
    show emf wide
    with dissolve
    emelie " And to make sure nothing spooky is lurking below the surface!"
    show emeswim hips
    show emf really
    with dissolve
    emelie " Like that mean blowfish from yesterday..."
    me " Are you holding a grudge against all blowfish now because of that statue mishap?"
    show emeswim bellu
    show emf pout
    with dissolve
    emelie " ... kinda."
    show emeswim hips
    show emf laugh
    with dissolve
    emelie " But I'm sure you're happy it blew our spoon out of my hand... "
    show emf sooth behind emblush
    show emblush at right:
        yalign 0.16 xalign 1.26
        zoom 1.20
    with dissolve
    emelie " Resulted in a different kinda dessert for me..."
    me " You're definitely right about that..."
    me " I think I owe my life to blowfish-kind after that experience!"
    hide emeye
    show emf laugh
    show emeswim normal
    with dissolve
    emelie " Haha!"
    show emf normalblush with dissolve
    emelie " Every day has been great since you've been here! "
    #stop music fadeout 0.6
    emelie "I never thought I'd gather the courage to go on stage and show off my body like that..."

    #play music ("audio/TrailsQuiet.mp3") fadein 0.0 volume 0.3


    show emeswim bellu
    show emf insecure
    hide emeye
    with dissolve
    emelie " But I think you've made me feel more confident about myself as of late... after all the {i}fun stuff{/i} we've been up to!"
    show emf smile
    show emeswim hips
    show emblush at right:
        yalign 0.16 xalign 1.26
        zoom 1.20
    with dissolve
    emelie " Modeling for you last night was a big confidence booster and served as a good warm-up for today!"
    show emf fluster
    show emeswim bellu
    with dissolve
    emelie "But also just the way you've been looking at me and stuff..."
    me " I've had an amazing time since I arrived here, too. "
    me "Especially with you! "
    me "Besides all the {i}fun stuff{/i} you're also just great to be around! "
    show emf insecure
    show emeye side1 behind emblush at right:
        yalign 0.16 xalign 1.26
        zoom 1.20
    with dissolve
    emelie " Oh, I don't know..."
    " She's blushing."
    me " It's true! "
    me " You said earlier that you're afraid of messing something up when your parents are away... "
    me "But seeing you take the stage earlier just to inspire the other girls, even if it was scary, really showed what a giving and responsible person you are!"
    window hide
    show emf aww
    hide emeye
    with dissolve
    pause 0.6
    window show
    "Emelie tears up a little."
    emelie " Thank you, [Protagonist]."
    show emf insecure
    show emeswim normal
    hide emblush
    with dissolve
    emelie " It can get pretty lonely when my parents are away... Especially now that all my old friends are out studying abroad and stuff..."
    emelie " Billy is great company but he's got a lot of other guard duties throughout the day, so I end up spending a lot of time by myself."
    show emf concern
    show emeswim bellu
    with dissolve
    emelie " That's another reason why I don't like being up in my tower room when my parents are away... It makes everyone else feel extra distant."
    me " Well, now I can keep you company! "
    me " And maybe if Billy keeps all that energy he got from my veggies... he can carry the things you like in the tower down to your other room!"
    show emf laugh
    show emeswim hips
    with dissolve
    emelie " Haha, now that'd be a sight! Billy sprinting up and down those stairs carrying all that furniture!"
    "We both laugh."
    show emeswim think
    show emf think
    with dissolve
    emelie " Speaking of Billy... "
    stop music fadeout 1.5
    play sound "audio/soundFX/FX5/billy_first_few_steps.mp3" volume 1.0

    show emeye normal at right:
        yalign 0.16 xalign 1.26
        zoom 1.20
    with dissolve
    emelie " Do you hear that sound?-"
    play sound "audio/soundFX/FX5/Run_and_Jump_short.mp3" volume 0.8
    window hide
    show emeswim normal
    show emeye panic at right:
        yalign 0.16 xalign 1.26
        zoom 1.20
    show emf wide
    with dissolve
    with hpunch
    pause 0.1
    with hpunch
    pause 0.1
    with hpunch
    # BILLY BOMB
    scene cannonballbilly
    show blackshake at truecenter behind cannonballbilly
    with vpunch

    pause 1.0
    window show
    billy "{size=+4} CANNONBAAAAAALLL!"
    "{size=+3}!!?!"
    emelie " {size=+3}OH MY GO-"
    window hide
    play sound "audio/soundFX/FX5/Splash_test.mp3" volume 0.78
    show cannonballbilly2 with dissolve
    with vpunch
    with vpunch
    pause 1.0
    window show
    " Billy's impact creates a massive splash!"
    emelie " {size=-2}Blrblrlblrgl!"
    window hide
    pause 1.0
    show black with fade
    window show
    "The big waves from the splash slowly settle."
    window hide

    show bg swimmingem
    show secondhippo
    if nadiapeen == True:
        show swimgroup aftersplash1

    else:
        show swimgroup aftersplash1z



    show bgswimdock2
    show bgswimtrickle
    show emeswim spurted at right:
        yalign 0.16 xalign 1.26
        zoom 1.20

    show emf panic at right:
        yalign 0.16 xalign 1.26
        zoom 1.20
    #show emelon hips at right:
    #    yalign 0.16 xalign 1.32
    #    zoom 1.25
    show bgswimem
    with fade
    play sound "audio/soundFX/FX5/water_driplets_test.mp3" volume 1.0

    pause 0.5
    play music "audio/Seagul.wav" fadein 1.0 volume 0.8




    #Pic of a bunch of embarassed ladies with their tops off
    pause 0.8
    window show
    "!!"

    "So many tits!"
    emelie " Kyaa!"
    show emf panic2 with dissolve
    emelie " J-jeez! That really messed my swimsuit up!"
    hide bgswimtrickle
    show emeswim hidee
    show emeye side2 at right:
        yalign 0.16 xalign 1.26
        zoom 1.20
    show emf wide
    with dissolve
    emelie " And seems I'm not alone!"
    "Emelie shifts focus to the visiting contestants from earlier."


    if nadiapeen == True:
        show swimgroup aftersplash2 with dissolve
        imara " That really got us both, huh?"
        show swimgroup aftersplash3 with dissolve
        nadia " I didn't know pigs were such a threat in the water..."
        show swimgroup aftersplash3zz with dissolve
        nadia " ..."
        "Nadia's eyes follow Imara's curves."
        show swimgroup aftersplash3zzz with dissolve
        nadia " My my... "
        window hide
        play sound "audio/soundFX/Get.mp3"
        show swimgroup aftersplash4 with dissolve
        pause 0.6
        window show
        "!!"

        "Her cock suddenly grew immensely!"
        show swimgroup aftersplash5 with dissolve
        imara " Maybe that big splash wasn't such a bad thing after all..."
        show swimgroup aftersplash6 with dissolve
        "Imara longingly looks at the throbbing member, and slowly moves a hand down to play with her crotch!"
        show swimgroup aftersplash7 with dissolve
        nadia " I think you're right... And you always do look damn good when dripping wet~ "
        "Now they're both playing with themselves!!"
        #imara " Mhmm- Now I'm just worried you'll get that pretty thing sunburnt."
        imara " You should try your best to find a nice place to hide that pretty thing."
        nadia " Yeah? Think you can help me with that, sweetie?"
        show swimgroup aftersplash7b with dissolve
        "Imara slips her long tongue out, making the zebra blush!"
        stop music fadeout 5.0
        imara " I can think of a place or two that I'm sure your big tool would love disappearing into~"
        show secondhippo2 behind bgswimdock2 with dissolve
        " They both giggle and slowly continue playing with their privates."
    else:
        show swimgroup aftersplash2z with dissolve
        imara " That really got us both, huh?"
        show swimgroup aftersplash3z with dissolve
        nadia " I didn't know pigs were such a threat in the water..."
        window hide
        play sound "audio/soundFX/Get.mp3"
        show swimgroup aftersplash4z with dissolve
        pause 0.6
        window show
        "!!"

        "Her bikini bottoms slide down and reveal a wet string connecting her pussy to the silky fabric! "
        show swimgroup aftersplash5z with dissolve
        imara " It seems that big splash got you wet in more ways than one..."
        show swimgroup aftersplash6z with dissolve
        "Her eyes fixate on Nadia's wet slit, and she slowly moves a hand down to play with herself!"
        show swimgroup aftersplash7z with dissolve
        nadia " I think you're right... But I'm sure we can find a way to make it even wetter~ "
        "Now they're both playing with themselves!!"
        #imara " Mhmm- Now I'm just worried you'll get that pretty thing sunburnt."
        show swimgroup aftersplash7zb with dissolve
        imara " I think I have exactly what it takes to get even the deepest parts of you nice and wet."
        "Imara slips her long tongue out, making the zebra blush!"
        stop music fadeout 5.0
        nadia " Mhmmm~"
        show secondhippo2 behind bgswimdock2 with dissolve
        " They both giggle and slowly continue playing with their privates."




    #emelie " You should apologize to ME and all the ladies around here!"
    #Switch to emelie being nude and covering up
label billyup:
    window hide
    play sound "audio/soundFX/FX5/BillyResurface.mp3" volume 1.0

    show bgswimbillysplash with dissolve
    show bgswimbillysplash2 with dissolve
    hide aftersplashlook
    hide swimgroup aftersplash7
    if nadiapeen == True:

        show swimgroup aftersplash8 behind bgswimdock2
        with dissolve

    else:
        show swimgroup aftersplash8z behind bgswimdock2
        with dissolve
    show emeye down4b
    show emf panic
    with dissolve

    pause 0.3
    window show
    "Billy resurfaces!"
    play music "audio/adventures-in-adventureland-by-kevin-macleod-from-filmmusic-io.mp3" fadein 0.1 volume 0.3
    hide bgswimbillysplash2
    show bgswimbillysplash3
    with dissolve

    billy " W-woops... Sorry!"
    " If it wasn't for Billy I wouldn't have been blessed with this display! I should be thanking him!"

    show emf panic2 with dissolve
    emelie " We're getting out of here quick!"
    hide emeye with dissolve
    emelie " Let's find a place to get dressed again!"
    window hide
    play sound "audio/soundFX/FX2/splash.wav" volume 0.85
    scene black with fade
    window show

    "We run behind a bush at an empty part of the beach!"
    $ unlock("S8")
    if playnormal == False:
        show black with fade
        $ renpy.end_replay()
    window hide

label chapter6start:
    scene fightpits
    show blackshake at truecenter behind fightpits
    with fade
    pause 0.3
    play sound "audio/soundFX/run2.wav"
    show emeswim hidee at right:
        yalign -0.20 xalign 1.00
        zoom 0.95
    show emf panic at right:
        yalign -0.20 xalign 1.00
        zoom 0.95
    with easeinleft
    pause 0.2
    window show
    #End of chapter 4.5
    #Scene is behind a bush with the arena visible behind
    #billy is covering his eyes and gives Emelie her swimsuit.
    emelie " Gosh! Billy blew all our clothes off!"
    show emf concern with dissolve
    emelie " Except yours, [Protagonist]..."
    window hide
    play sound "audio/soundFX/run2.wav"
    show billys drenched2 at left:
        yalign 0.4 xalign -0.16
    with easeinleft
    pause 0.3
    window show
    billy " Sorry about that, princess!"

    if modest == False:
        "Emelie adjusts her bikini."
        play sound "audio/soundFX/FX4/clothing3.wav"
        show emeswim out with dissolve

    if modest == True:
        "Emelie adjusts her swimsuit."
        show emeswim spurted with dissolve
        play sound "audio/soundFX/FX4/clothing3.wav"
        show emeswim hips
    show emeye side1 at right:
        yalign -0.20 xalign 1.00
        zoom 0.95
    show emf insecure
    with dissolve
    emelie "I'm okay!"
    show emf gross
    show emeswim out
    with dissolve
    emelie " Just try not to ONLY aim for the ladies next time, Billy!"
    window hide
    show billys drenched with dissolve
    play sound "audio/soundFX/Get.mp3"
    with hpunch
    show billys fists with dissolve
    window show

    "Billy giggles and shakes the water off his armor."
    show billys thumbb with dissolve
    billy " Noted! I'll aim for [Protagonist] next time!"
    me "?!"
    me " I'm never getting into the water again!"
    show billys base
    hide emeye
    show bill laughface at left:
        yalign 0.4 xalign -0.16
    show emf laugh
    with dissolve
    "Billy and Emelie both laugh."
    window hide







    hide bill with dissolve
    play sound "audio/soundFX/runn.wav" volume 0.3
    show billys base at left:
        linear 0.4 yalign 0.4 xalign -0.90
    pause 0.4
    show billys base at left:
        yalign 0.4 xalign -0.90
    show fightpitsshout behind billys
    show emeye side2 at right:
        yalign -0.20 xalign 1.00
        zoom 0.95
    show emf surprise
    show emear high at right:
        yalign -0.20 xalign 1.00
        zoom 0.95
    with dissolve
    play sound "audio/soundFX/Crowd/bigcheersoft.wav"
    with vpunch
    window show
    "A crowd roars in excitement!"
    show emeye scared at right:
        yalign -0.20 xalign 1.00
        zoom 0.95
    hide emear
    show emf wide
    with dissolve

    emelie " Woah, that is LOUD! "
    emelie " Something exciting must be happening! And it's coming from the Pig Pit right behind us!"
    show emf pout
    show emeswim normal
    hide emeye
    with dissolve
    emelie " Let's check it out!"
    window hide
    hide bill
    show billys wary
    with dissolve
    play sound "audio/soundFX/runn.wav" volume 0.3
    show billys wary at left:
        linear 0.3 yalign 0.4 xalign -0.16
    pause 0.3
    show billys wary at left:
        yalign 0.4 xalign -0.16

    show bill wary at left:
        yalign 0.4 xalign -0.16
    with dissolve
    window show
    billy " The Pig Pit?? "
    billy " Not for me!"
    billy " I think I need a quick nap after all that eating and swimming... "
    show billys fists
    show bill hapiface
    with dissolve
    billy " And then maybe I'll have some ice cream, too! Hee hee! "
    show emeye side1 at right:
        yalign -0.20 xalign 1.00
        zoom 0.95
    show emf smile
    show emeswim hips
    with dissolve
    emelie " Okay, Billy! Enjoy yourself!"

    show emf normal
    with dissolve
    emelie " As a princess, I can't shy away from parts of our entertainment and culture!"
    show billys base
    show bill laughface
    with dissolve
    billy "Yes, yes! I'll come find you later!"
    me " Okay, Billy! We'll catch up soon!"
    window hide
    play sound "audio/soundFX/run2.wav"
    hide bill
    hide billys
    with easeoutleft
    stop music fadeout 3.0
    pause 0.3
    hide emeye
    show emeswim out
    show emf wide
    with dissolve
    window show
    emelie " Now I'm super curious! Let's hurry!"
    window hide
    scene black with fade
    window show
    "We hurry into the arena!"
    window hide
    # We go there.
    jump fightpits

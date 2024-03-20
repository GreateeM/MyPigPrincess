label startch7:
    play music "audio/Birds.wav" fadein 5.0 volume 0.5
    scene tailorsmith
    show blackshake at truecenter zorder -100
    show bgtailorsmithsunsetnoppl
    show tailorsmithdoorcloseday
    #show bronsw base:
    #    yalign -11.5 xalign -37.5 zoom 0.89
    with fade
    play sound "audio/soundFX/runn.wav" volume 0.7
    show bronsw base at left:
        yalign 2.2 xalign -1.0
        zoom 0.87
    with easeinleft

    pause 0.5
    show bronsw hips
    show bron leftlook at left:
        yalign 2.2 xalign -1.0
        zoom 0.87
    show broneye lookright at left:
        yalign 2.2 xalign -1.0
        zoom 0.87
    with dissolve
    window show
    #Show up outside Bronwen's place "
    bron "Huh... "
    bron "'Place is pretty empty for this time of day. "
    me "I guess everyone's at the beach. "
    hide broneye
    show bronsw think
    hide bron
    with dissolve
    bron "That's probably it... "
    show bronsw base
    show bron grin at left:
        yalign 2.2 xalign -1.0
        zoom 0.87
    with dissolve
    bron "Let's head inside."
    window hide
    scene black with dissolve
    show blackshake at truecenter zorder -100
    pause 0.3
    play sound "audio/soundFX/OpenDoor 1.wav" volume 0.5
    pause 0.2
    play music "audio/Alexander Nakarada - Collection - Celtic & Medieval - 12 Vopna.mp3" fadein 2.0 volume 0.2
    scene bg smithy
    show blackshake at truecenter zorder -100
    show smithyanvil
    with fade
    play sound "audio/soundFX/run2.wav" fadeout 0.2 volume 0.7
    show bronsw base behind smithyanvil  at left:
        yalign -1.0 xalign -0.0
        zoom 0.9
    with easeinright
    pause 0.5
    window show
    "I follow Bronwen inside and am immediately hit by the dense, warm air in the room."
    show bronsw knuckles
    show bron donefor2 at left:
        yalign -1.0 xalign -0.0
        zoom 0.9
    with dissolve
    bron "Now, I need to go upstairs and change real quick... "
    show bron pout with dissolve
    bron "It'll only take a sec, but make yourself comfortable."
    "I look around, not seeing a single comfortable spot in the entire room."
    show bronsw hips
    show bron questioning2
    with dissolve
    bron "... As comfortable as you can. "
    me "Alright, tell me when you're done."
    show bronsw base
    show bron grin
    with dissolve
    bron  "Yus."
    window hide
    pause 0.1
    play sound "audio/soundFX/run2.wav" fadeout 0.2 volume 0.7
    hide bronsw
    hide bron
    with easeoutleft
    pause 0.1
    play sound "audio/soundFX/run2r.wav" fadeout 0.1 volume 0.2
    pause 0.1
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
    $ renpy.music.set_volume(0.25, delay=0, channel='music')
    pause 0.1
    $ renpy.music.set_volume(0.20, delay=0, channel='music')
    pause 0.1
    $ renpy.music.set_volume(0.15, delay=0, channel='music')
    pause 0.1
    $ renpy.music.set_volume(0.10, delay=0, channel='music')
    pause 0.1
    $ renpy.music.set_volume(0.05, delay=0, channel='music')
    pause 0.1
    $ renpy.music.set_volume(0.00, delay=0, channel='music')
    window show
    "Bronwen nods and stomps upstairs."
    window hide
    pause 1.5
    window show
    "..."
    window hide
    play sound "audio/soundFX/FX2/crickets.wav" fadein 2.5 volume 0.3
    pause 2.0
    window show
    "....."
    window hide
    pause 2.5

    stop sound fadeout 0.5
    window show
    "...Well, this is boring."
    window hide
    pause 0.1
    show seeschematics with dissolve
    $ renpy.music.set_volume(0.05, delay=0, channel='music')
    pause 0.1
    $ renpy.music.set_volume(0.10, delay=0, channel='music')
    pause 0.1
    $ renpy.music.set_volume(0.15, delay=0, channel='music')
    pause 0.1
    $ renpy.music.set_volume(0.20, delay=0, channel='music')
    pause 0.1
    $ renpy.music.set_volume(0.30, delay=0, channel='music')
    pause 0.1
    $ renpy.music.set_volume(0.40, delay=0, channel='music')
    pause 0.1
    $ renpy.music.set_volume(0.50, delay=0, channel='music')
    pause 0.1
    $ renpy.music.set_volume(0.60, delay=0, channel='music')
    pause 0.1
    $ renpy.music.set_volume(0.70, delay=0, channel='music')
    pause 0.1
    $ renpy.music.set_volume(0.80, delay=0, channel='music')
    pause 0.1
    $ renpy.music.set_volume(1.00, delay=0, channel='music')
    pause 0.2
    window show
    "Ooh, I can see a stack of papers lying on the table!"
    "I'll have a quick look to waste some time!"

    window hide
    hide seeschematics with dissolve
    pause 0.1
    play sound "audio/soundFX/swof.mp3" volume 0.3
    show hidebronart with dissolve
    pause 0.2
    show blackopacity
    with dissolve

    show bronwart4
    show bronwart3
    show bronwart2
    show bronwart1
    with dissolve
    play sound "audio/soundFX/get.mp3" volume 0.4
    with vpunch
    pause 0.5
    window show
    "These are Bronwen's blacksmithing plans!"
    "...I remember drawing that atrocious-looking buttplug..."
    "I can't believe I messed the smiley face up that badly."
    "Maybe I'd do better now after I had that painting practice with Emelie."
    "Let's see what's next!"
    window hide
    play sound "audio/soundFX/PageTurn.wav" volume 0.7
    hide bronwart1
    with dissolve
    pause 0.8
    window show

    "Ooh."
    "It seems like Bronwen's been forced to make some armor adjustments to accommodate for Billy's big... muscles."
    "And woah, Rolf's old armor from the war was HUGE!"
    "Makes me wonder how he ended up so scarred... "
    "Bronwen's drawings are really realistic and accurate just like her dad's!"
    "Hmm..."
    "I wonder what's hiding under this one."

    window hide
    play sound "audio/soundFX/PageTurn.wav" volume 0.4
    hide bronwart2
    with dissolve
    pause 0.8
    window show
    "Whoops-"
    "Bronwen's drawn herself completely nude!"
    "She looks pretty scary and intense with all those muscles..."
    "But kinda pretty at the same time."
    "This armor design for a female pig looks cool! "
    "Bronwen looks a lot more badass in that than the other round piggies do in their armor..."
    "And the picture to the right is really nice. It looks like she put a lot of effort into it."
    "Okay, let's see what follows!"
    window hide
    play sound "audio/soundFX/PageTurn.wav" volume 0.6
    hide bronwart3
    with dissolve
    pause 0.2
    play sound "audio/soundFX/Dun.wav" volume 0.3
    with vpunch
    pause 0.8
    window show
    "{size=+10}!!?"
    "These images keep getting naughtier!"
    "...Damn... "
    "Looks like Bronwen's been asked to make a ton of different \" toys \" !"
    "Some of these things look absolutely crazy. "
    "And hmm... "
    "\" The Hunk \" must be a human-inspired toy now that \"Humane Hunk\" is selling so well!"
    "But Bronwen doesn't seem to know what it should look like."
    window hide
    pause 0.1
    play sound "audio/soundFX/funpig.mp3" volume 0.7
    stop music fadeout 0.5
    with vpunch

    hide bronwart4
    hide blackopacity
    with dissolve
    window show
    play music "audio/Birds.wav" fadein 2.0 volume 0.2

    bron "{size=+10} HEY!!"

    me "Huh?!"
    bron "I'm done up here!"
    me "Okay, I'm coming right up!"
    window hide
    play sound "audio/soundFX/swof.mp3" volume 0.5
    hide hidebronart with dissolve
    pause 0.3
    window show
    "I put the paper stack down and start moving up the stairs-"
    window hide
    pause 0.1
    show black with dissolve
    play sound "audio/soundFX/FX7/stepsupxx.wav" volume 0.6
    pause 2.3
    scene bg smithyupstairs with fade

    show blackshake at truecenter zorder -100
    pause 1.5
    stop music fadeout 2.0
    window show

    "Bronwen's room is pretty small and cluttered. "
    "But the air is surprisingly clear compared to the room downstairs, with heat from below making the floorboards really warm against my feet."
    "It feels cozy!"
    play music "audio/Alexander Nakarada - Collection - Celtic & Medieval - 13 Norður.mp3" fadein 0.0 volume 0.2
    window hide
    play sound "audio/soundFX/runn.wav" volume 0.7
    show broncas base at left:
        yalign -1.0 xalign -1.0
        zoom 0.9
    with easeinleft
    pause 0.9
    window show
    me "Woah!"
    show broncas hips
    show bron huhh at left:
        yalign -1.0 xalign -1.0
        zoom 0.9
    with dissolve
    bron "...What's with the expression?"
    show broncas knuckles
    show bron cooldown
    with dissolve
    bron "Ugh. "
    show bron done with dissolve
    bron "'Thought I'd dress even skimpier now that we're alone? "
    me "..."
    "She can't blame me... almost every outfit I've seen in Hog Haven has been super revealing!"
    show broncas hips
    show bron grin
    with dissolve
    bron"Ooooor-"
    window hide
    play sound "audio/soundFX/softget.wav" volume 0.7
    show broncas pull
    show bron smileee
    with dissolve
    pause 0.5
    window show
    "Bronwen grabs and pulls the back of her shirt to tighten it. "
    me "?!"
    "I blush."
    show bron grun with dissolve
    bron"Maybe you expected something a bit more form-fitting?"
    "Her curves look so good with her shirt like that!"
    window hide
    menu:
        with dissolve


        "{size=+3}I didn't expect anything!{/size} \n I like the big, casual shirt!":
            window show
            me "I didnt expect anything! "
            me "I like the big, casual shirt!"
            show broncas hips
            show bron poutz
            with dissolve
            bron "... Hmpf, that's good. "
            show broncas knuckles
            show bron questioning2
            with dissolve
            bron "'Wouldn't wanna dress uncomfortably just for people to stare at my ass all day."

        "{size=+3}Yeaah...{/size} \n I expected something a bit more daring.":
            window show
            me "Yeaah... I expected something a bit more daring."
            show broncas knuckles
            show bron meanface2
            with dissolve
            bron "I knew it, perv!"
            bron "But I don't dress to be uncomfortable unless I have to!"
            show broncas hips
            show bron questioning2
            with dissolve
            bron "And I don't want people to just stare at my ass all day."
    me "Your bikini was pretty skimpy to be fair..."

    show broncas fist
    show bron rageface
    with dissolve
    play sound "audio/soundFX/funpig.mp3" volume 0.5
    with hpunch
    bron "That's because I made it myself and wanted to save on materials!!"
    me "Suure."
    show broncas hips
    show bron huhh
    with dissolve
    bron "Whatever."
    show bron baseface with dissolve
    bron "Anyway, hope you're OK with the messy room."
    window hide

    menu:
        with dissolve


        "{size=+2}I don't mind it! {/size}\n You've got a nice room.":
            window show
            me "I don't mind! "
            me "You've got a nice room."
            show broncas think
            show bron thunk
            with dissolve
            bron "You think?..."
            show broncas base
            show bron questioning
            with dissolve
            bron "Wow, you must live in a dump."
            me "... No comment."
            show broncas hips
            show bron pout
            with dissolve
            bron "Well, it's good to hear you haven't become too spoiled by the Princess' quarters to appreciate a normal-looking room..."


        "{size=+2}It is kinda messy...  {/size}\nYou should clean up before inviting guests over!":
            window show
            me "It is kinda messy... You should clean up before inviting guests over!"
            show broncas knuckles
            show  bron meanface
            with dissolve
            bron "PFF! You're lucky I even invited you!"
            show  bron meanface2
            with dissolve
            bron "And it isn't THAT bad!"
            show broncas hips
            show bron huhh
            with dissolve
            bron "Ugh, two days in the kingdom and you've become an upper-class brat, eh?"
            me "... Maybe."
            show broncas think
            show bron thunk
            with dissolve
            bron "..."
            bron "'Suppose I could clean up a thing or two..."

        "{size=+2}You call this messy? {/size} \n You should see my room back home!!":
            window show
            me "You call this messy? It's nice! "
            me "You should see my room back home..."
            show broncas hips
            show bron questioning
            with dissolve
            bron "... I don't think I want to."
            show broncas think
            show bron pull
            with dissolve
            bron "Unless you make the visit worthwhile, of course..."
            "What is that supposed to mean?"
            show broncas hips
            show bron hehh
            with dissolve
            bron "Anyways, it's good to hear you haven't become too spoiled by the Princess' quarters to appreciate a normal looking room..."



    "My eyes move to the corner of the room."
    me "Is that a... statue of Billy in the corner?"
    show broncas behindd
    show bron rightlook
    with dissolve
    bron "Oh... uh... yeah. "
    bron "'Something I've been working on."
    me "What's it for? "
    me "Or do you just want him there to protect you as you sleep?"
    show broncas hips
    show bron laugh2
    with dissolve
    bron "Hah! "
    show bron grin2 with dissolve
    bron "Funny."
    show broncas base
    show bron smile
    with dissolve
    bron"Nah, it isn't for me."
    show broncas think
    show bron thunk2
    with dissolve
    bron "It's a gift for his birthday that's coming up in a few weeks. "
    me "Ahh, I didn't know! "
    show broncas hips
    show bron smileeee
    with dissolve
    bron "A sculpture of him living his best life, about to eat a biiiig and juicy carrot cake!"
    show bron smileee
    with dissolve
    bron "That's what it'll be when it's finished, at least... "
    show broncas think
    show bron thunk3
    with dissolve
    bron "I think I'll make the statue's cake hollow-"
    show broncas knuckles
    show bron wick
    with dissolve
    bron "-So that when I give it to him, he'll lift the lid up and a REAL carrot cake will be there to surprise him!"
    play sound "audio/soundFX/Dun.wav" volume 0.3
    with hpunch
    show broncas fist
    show bron wick2
    with dissolve
    bron "Mwahaha, he'll bawl his eyes out with happiness!"
    me "You're really giving this your all, huh? "
    me "It's sort of scary."
    show broncas hips
    show bron hehh
    with dissolve
    bron "Well, his birthday is only a couple of weeks away- "
    show bron cooldown with dissolve
    bron "And throughout the year he always gives me these really thoughtful gifts that I've gotta outdo when I finally gift him back on his birthday."
    show bron done with dissolve
    bron "I'm his older cousin, so I can't have him outdo me in the art of gift-giving."
    "She sure is competitive."
    me "What kinda stuff does he usually get you?"
    show broncas base
    show bron leftlook
    with dissolve
    bron "... I'll show you the most recent thing."
    window hide
    play sound "audio/soundFX/run2.wav" fadeout 0.2 volume 0.7
    hide broncas
    hide bron
    with easeoutleft
    pause 0.5
    play sound "audio/soundFX/runn.wav" volume 0.7
    show broncas holdbilly at left:
        yalign -1.0 xalign -1.0
        zoom 0.9
    with easeinleft
    window show
    "Bronwen grabs a piece of paper off the wall."
    bron "He drew me this the other day."
    window hide
    show broncas base
    show bron pout at left:
        yalign -1.0 xalign -1.0
        zoom 0.9
    with dissolve
    show blackopacity with dissolve
    play sound "audio/soundFX/Get.mp3"
    show billysart at center:
        yalign 0.15
        zoom 0.94
    with dissolve
    with vpunch
    pause 2.0
    window show
    me "Oh god..."
    me "That's-"
    bron "The cutest damn thing you've ever seen, right?..."
    me "... Yes."
    "\" Thank you so much for fixing my helmet \" "
    "He must've drawn this after Rolf banged his helmet in two days ago!"
    "It's so wholesome..."
    "I lose myself in the art a bit longer before putting it down."
    window hide
    hide billysart
    with dissolve
    hide blackopacity
    with dissolve
    pause 0.5
    window show
    me "That's tough to beat, but I'd say you're well on the way with your big sculpture. "
    me "It's looking amazing so far!"
    show broncas behindd
    show bron poutz at left:
        yalign -1.0 xalign -1.0
        zoom 0.9
    with dissolve
    bron "Thanks. "
    show broncas hips
    show bron rightlook
    with dissolve
    bron "I try to chip away at it a little bit after work every day. "
    window hide
    hide bron with dissolve
label buttsitscene:
    if playnormal == False:
        window hide
        $ bronwen_name = "Bronwen"
        show black with dissolve
        pause 0.2
        scene bg smithyupstairs
        show blackshake at truecenter zorder -100
        show broncas base at left:
            yalign -1.0 xalign -1.0
            zoom 0.9
        with fade
        pause 0.3
    play sound "audio/soundFX/runn.wav" fadein 0.7 fadeout 0.8 volume 0.3

    show broncas at left:

        yalign -1.0 xalign -1.0
        zoom 0.9
        linear 0.3 yalign -1.0 xalign 6.0
        zoom 0.9
    pause 0.5
    show broncas at left:
        yalign -1.0 xalign 6.0
        zoom 0.9

    window show
    bron "Anyway... "
    show broncas knuckles
    show bron donefor2 at left:
        yalign -1.0 xalign 6.0
        zoom 0.9
    with dissolve
    bron "As for YOUR gift."
    me "R-Right!"
    me"That's why we're here..."
    show broncas think
    show bron pull
    with dissolve
    bron "Have a seat and I'll get things started."
    me "Yess-"
    "I'm excited!"
    stop music fadeout 1.5
    window hide
    scene black with fade
    show blackshake at truecenter zorder -100
    pause 0.2
    window show
    "I take a few steps forward and lower myself onto the bed-"
    bron " {size=+2}Who said you could sit on the BED?!"
    play music "audio/Alexander Nakarada - Collection - Celtic & Medieval - 08 Now We Feast.mp3" fadein 0.0 volume 0.2
    window hide
    play sound "audio/soundFX/FX5/stepknuck.wav" volume 0.4
    show blackshake at truecenter zorder -100
    with vpunch
    scene bronstepbase
    show blackshake at truecenter zorder -100
    show bronstepf scary

    with vpunch
    pause 1.0
    window show
    me "Aghk!"
    "She forces me to the ground with her powerful hoof!"
    bron "You seem to be expecting quite a bit..."
    window hide
    play sound "audio/soundFX/grab.wav" volume 1.0
    show bronstepdick with dissolve

    with vpunch
    show bronstepdickhands with dissolve
    pause 0.5
    window show
    bron "Pervert!"
    me "Bh-ah!"
    "She steps on my crotch!"
    me "Careful!"
    hide bronstepdickhands
    with dissolve
    hide bronstepf scary
    with dissolve
    #There are some things degenerates like you tend to enjoy... ( hint at bj? )
    bron "Y'know..."
    show bronstepdickx
    hide bronstepdick
    show bronstepf thinkx
    with dissolve
    bron "Most people like you who come visit me for buttplugs don't just stop there... "
    bron "There are a few other common things people like to get!"
    show bronstepf grin
    hide bronstepdickx
    show bronstepdick
    with dissolve
    with vpunch
    bron  "I was going to charge you big time for it like the plug! "
    bron "Hah! "
    "She grins wickedly."
    show bronstepf grin2 with dissolve
    bron "You sure paid extra for that!"
    me "...I had a feeling."
    show bronstepf sidee with dissolve
    bron "But after what you did for my dad back there I thought I'd give you a freebie to make up for all that... "
    me "So this isn't really a reward after all?! "
    me"You're just trying to make up for scamming me earlier! "
    show bronstepdickx
    hide bronstepdick
    show bronstepf thinkx
    with dissolve
    bron "Tsss... After giving you this item we're more than square!"
    bron "'Figured I could just give it to you as a surprise, buuuut... "
    hide bronstepdickx
    show bronstepdick
    hide bronstepf
    with dissolve
    bron "Fit is key for this men's item, so I thought I might as well check real quick to make sure it's the right size. "
    window hide
    scene black with fade
    play sound "audio/soundFX/Sit Pillow.wav" volume 0.4
    scene pantremovebase
    show blackshake at truecenter zorder -100
    show pantremovevignette zorder 100
    with fade
    pause 0.5
    window show
    "She sprawls next to me-"
    play sound "audio/soundFX/swof.mp3" volume 0.5
    show pantremove pull
    with dissolve
    bron "Now let me just size you up real quick-"
    me "??"
    me "Size me u-"
    window hide
    show pantremovelookd with dissolve
    pause 0.3
    play sound "audio/soundFX/get.mp3" volume 0.4
    show pantremove hold
    show pantremovedicksurprise
    show bigeyebronz
    with dissolve
    pause 0.2
    play sound "audio/soundFX/Dun.wav" volume 0.5
    with vpunch
    hide bigeyebronz with dissolve
    pause 0.2
    window show
    "She pulls my dick out!"
    bron "O-Oh!"
    "It quickly swells in her hand, gaining a fair bit of size."
    me "Fhu-"
    show pantremovedicksurprise2
    hide pantremovedicksurprise
    with dissolve
    bron "{size=-8}{alpha=*0.80}So this is what it looks like, eh..."
    bron "{size=-8}{alpha=*0.80}Pretty traditional shape, just... a lot bigger..."
    me "...What are you whispering about?"
    hide pantremovebasesideeye2
    hide pantremovedicksurprise2
    hide pantremovebigeyedown
    show pantremovedickgrump
    with dissolve
    bron "Nothing!"
    "She gives the base of my cock a gentle squeeze."
    window hide
    hide      pantremovedickgrump
    show pantremovelookdownn
    with dissolve
    play sound "audio/soundFX/grabby.wav" volume 0.8
    with hpunch
    pause 0.3
    window show
    bron "Hmmf... I think it should fit..."
    bron "But it might be a little tight..."
    window hide
    play sound "audio/soundFX/FX7/spit.wav" volume 0.4
    show pantremovef spit
    with dissolve
    with vpunch
    pause 0.3
    hide pantremovef spit
    show pantremovedspit
    with dissolve
    show pantremovebasesideeye2
    hide pantremovelookdownn
    with dissolve
    pause 0.3
    window show


    "She spits on my dick!"
    me "Ahh- That feels good!"
    "I always thought Bronwen was sexy..."
    bron "Mhhn..."
    "I feel her spread the saliva around my cock with her hand."
    show pantremovemouthopen
    hide pantremovebasesideeye2
    with dissolve
    bron "Now, close your eyes~"
    window hide
    show black with fade
    window show
    "I do as she says and imagine just how good her tongue will feel on my cock."
    window hide
    pause 0.2
    play sound "audio/soundFX/FX5/rolfknuckles.wav" volume 0.4
    $ renpy.music.set_volume(0.0, delay=0, channel='music')
    show blackshake at truecenter zorder -100
    hide pantremovemouthopen
    show pantremovegloomy peen3
    hide pantremovedspit
    hide pantremove
    hide black
    with vpunch
    pause 0.2
    window show
    me "{size=+2}GHAHN!?"
    bron "Perfect fit! "
    "{size=+5}?!"
    "She's slid some kind of ring onto my dick!"
    me "What?!"
    $ renpy.music.set_volume(0.15, delay=0, channel='music')
    pause 0.1
    $ renpy.music.set_volume(0.30, delay=0, channel='music')
    pause 0.1
    $ renpy.music.set_volume(0.60, delay=0, channel='music')
    pause 0.1
    $ renpy.music.set_volume(0.80, delay=0, channel='music')
    pause 0.1
    $ renpy.music.set_volume(1.00, delay=0, channel='music')
    show pantremovegloomy peen2 with dissolve
    bron "Damn... You're pretty hung, huh? "
    bron "You're lucky I brought ya along or I would've gone two sizes smaller!"

    me "What is it?!"
    show pantremovegloomy peen1 with dissolve
    bron "Isn't that obvious?"
    bron "A cock ring. "
    window hide
    scene black with fade
    window show
    "Bronwen stands up in front of me-"
    window hide
    scene peenprofilebase at left
    show blackshake at truecenter zorder -100
    with fade
    window show
    bron "It's the reward I was talking about..."
    me "W-What?"
    me "I thought you were about to perform the reward!?"

    window hide
    show peenprofileball stomp2 at left
    with dissolve
    play sound "audio/soundFX/softget.wav" volume 1.0
    show peenprofileball stomp1 at left
    show peenprofilestand at left  behind peenprofileball
    with dissolve
    with vpunch
    window show
    "She taps her hoof on my balls!"
    bron "Hah, what?!"
    bron "Thought I'd bless you with a blowjob? "
    bron "Dream on, honey."
    window hide
    play sound "audio/soundFX/swof.mp3" volume 0.3
    hide peenprofileball
    hide peenprofilestand
    with dissolve
    window show
    bron "But I hope you'll enjoy your cock ring with that special someone you bought the plug for."
    window hide
    scene bronstepbase
    show blackshake at truecenter zorder -100
    show bronstepdick out
    show bronstepf think
    with fade
    pause 1.0
    window show
    bron "Probably Emelie, huh?"
    me "..."
    show bronstepf thinkxx with dissolve
    bron " She was walking a lil' funny today at the beach. Don't think I didn't notice."

    show bronstepf think with dissolve

    bron "The ring makes your dick harder and makes you last longer."
    hide bronstepf with dissolve

    bron "Fun stuff, and I bet you could use it!"
    show bronstepf grin2 with dissolve
    bron "Hahah!"

    "She laughs at her own comment."

    me "It's... making me so veiny!"
    hide bronstepf
    show bronstepf lookdown
    with dissolve
    bron "Yeah!"
    bron"Working wonders, isn't it?"

    "It does feel kinda nice..."

    me"M-Maybe I'll end up giving it a try sometime..."
    window hide
    show bronstepfdopacity zorder 100
    with dissolve
    show blackshake at truecenter zorder -100
    show bronstepdickjerk3a with dissolve
    pause 1.2
    window show
    "I grip the ring and give it a tug."
    window hide
    play sound "audio/soundFX/get.mp3" volume 0.6
    show bronstepdickjerk3 with dissolve
    with vpunch
    pause 0.3
    hide bronstepfdopacity with dissolve
    pause 0.2
    hide bronstepdickjerk3 with dissolve
    window show
    "It won't come off?!"
    "My heart starts racing. "
    show bronstepf smile with dissolve
    bron "So... We're all good, right?"
    me "W-Wait-"
    me "How do I get this thing off?! "
    me "It's too tight! "
    show bronstepf sidee with dissolve
    bron "Uhh... Maybe I did get the size a little wrong..."
    bron "W-Whoops."
    hide bronstepf with dissolve
    bron "'Guess you're just gonna have toooo- "
    window hide
    show bronstepf scary with dissolve
    $ renpy.music.set_volume(0.0, delay=0, channel='music')
    play sound "audio/soundFX/Dun.wav" volume 0.3
    with vpunch
    window show
    bron "{size=+10}Cum."
    "{size=+3}?!"
    $ renpy.music.set_volume(0.15, delay=0, channel='music')
    pause 0.1
    $ renpy.music.set_volume(0.30, delay=0, channel='music')
    pause 0.1
    $ renpy.music.set_volume(0.60, delay=0, channel='music')
    pause 0.1
    $ renpy.music.set_volume(0.80, delay=0, channel='music')
    pause 0.1
    $ renpy.music.set_volume(1.00, delay=0, channel='music')
    me "How?!"
    bron "Just jerk yourself off real quick and get out of here!"
    me "..."
    window hide
    show bronstepfdopacity zorder 100
    with dissolve
    show bronstepdick jerk2
    hide  bronstepdickjerk3a
    with dissolve
    pause 0.3
    hide bronstepdick jerk2
    show  bronstepdickjerk3a
    with dissolve
    pause 0.3
    show bronstepdick jerk2
    hide  bronstepdickjerk3a
    with dissolve
    pause 0.3
    hide bronstepdick jerk2
    show  bronstepdickjerk3a
    with dissolve
    pause 0.3
    show bronstepdick jerk2
    hide  bronstepdickjerk3a
    with dissolve
    pause 0.5
    hide bronstepfdopacity
    with dissolve
    window show
    "I try my best to jerk off but I'm too freaked out to get any pleasure out of it!"
    me "I can't get in the mood!"
    window hide
    show bronstepfdopacity zorder 100
    with dissolve
    hide bronstepdick jerk2
    show  bronstepdickjerk3a
    with dissolve
    pause 0.3
    show bronstepdick jerk2
    hide  bronstepdickjerk3a
    with dissolve
    hide bronstepdick jerk2
    show  bronstepdickjerk3a
    with dissolve
    pause 0.2
    show bronstepdick jerk2
    hide  bronstepdickjerk3a
    with dissolve
    pause 0.5
    hide bronstepfdopacity
    with dissolve
    window show
    me "It's hopeless..."
    window hide
    show blackopacity
    show facecloseup
    with dissolve
    play sound "audio/soundFX/brongrunt.wav" volume 0.9
    with vpunch
    pause 0.5
    window show
    bron "...You sure are pathetic, huh?" # concern
    me "You're the one who put me in this situation!"
    bron "I gave you a gift and now you're complaining and asking for more!"

    bron"I should probably beat you up instead, come to think of it..."

    bron "With you trying to have other girls suck you off when Emelie's not around!"
    me "You really think I'd do that if I thought it would hurt her feelings?!"

    window hide
    hide facecloseup
    with dissolve
    hide blackopacity
    with dissolve
    show bronstepf thinkz with dissolve
    pause 0.5
    window show



    bron "... Maybe not."



    "She actually believed me?"
    show bronstepf lookdown with dissolve

    bron "Yes, I do believe you... "
    window hide
    play sound "audio/soundFX/Dun.wav" volume 0.2
    with hpunch
    window show
    "What the fu-"
    show bronstepf grin2 with dissolve
    bron "You're the easiest person to see through in the whole kingdom, hah!"
    show bronstepf smile with dissolve
    bron "Probably because you think with your dick as much as with your head."
    me "Rude. "
    "But probably true..."

    "I thought Bronwen's ability to read me would be a recipe for disaster, but it served me well in this situation!"
    me "So, will you help me out or what?..."

    show bronstepf lookdown with dissolve
    bron "Can't have you stuck in this thing forever."
    show bronstepf thinkz with dissolve
    bron "Hmm... "
    bron "I did see you check Emelie's ass out when we were at the beach. "
    show bronstepf think with dissolve
    bron"So maybe a simple visual will do the trick."
    window hide
    hide bronstepf with dissolve
    pause 0.2
    show black with dissolve
    pause 0.2
    play sound "audio/soundFX/FX4/clothing2.wav" volume 0.8
    scene bronbuttshow with fade
    show blackshake at truecenter zorder -100
    pause 0.5
    window show
    "Bronwen turns around and rests her hands on her hips, pulling her shirt up slightly."
    #She shows her ass. "
    bron "How's that?"
    "I slowly jerk my cock to the view of her round hips."
    me "That helps..."
    bron "'Knew it... "
    bron "'Ya gettin' close yet, perv?"
    me "I'll need a lot more time than this!"
    "..."
    bron "C'mon, we don't have all day!"
    me "Then I'm going to need something else!"
    bron "..."
    bron "I won't strip for you."
    me "Okay, okay. "
    "Hmm-"
    "I was almost able to look up her shirt earlier... "
    "Maybe if she steps just a bit closer I can get a good enough view to do the trick!"
    me "Can you step a little closer? "
    me"I can't see very well."

    bron "..."

    window hide
    show black with dissolve
    pause 0.2
    play sound "audio/soundFX/FX6/trip.wav" volume 0.6
    scene sitface01 at truecenter:
        zoom 0.88 ypos 540
    with fade
    show blackshake at truecenter zorder -100
    pause 0.5
    window show
    "Bronwen takes a couple of steps back and places a leg on either side of my body."
    bron "'This better?"
    me "Yes!"
    "I just wish her tail would move out of the way..."


    me "Do you think you could move your tail, maybe?"


    window hide
    play sound "audio/soundFX/FX4/clothing3.wav" volume 0.9
    show sitface02 at truecenter:
        zoom 0.88 ypos 540
    with dissolve
    pause 0.5
    window show
    bron "Like this?"
    "What a view!"
    me "Hyes, that's it!"
    "That ass is amazing! "

    window hide
    stop music fadeout 0.1
    play sound "audio/soundFX/FX7/bwamrec.wav" volume 0.7

    show blackshake at truecenter zorder -100
    show sitface03 at truecenter:
        zoom 0.88 ypos 540
    with dissolve
    with vpunch
    show sitface03 at truecenter:
        zoom 0.88 ypos 540
        linear 0.3 zoom 1.02 ypos 455
    with vpunch
    pause 0.7
    show sitface03 at truecenter:
        zoom 1.02 ypos 455
    show sitfaced srs at truecenter:
        zoom 1.02 ypos 455
    with dissolve
    window show
    bron "{size=+15}I know what you're up to!"
    "!!"

    bron "Why not take an even closer look!?"

    window hide
    show sitfaced smush with dissolve
    play music "audio/Blacksmith+-+320bit.mp3" fadein 0.0 volume 0.3
    pause 0.3
    play sound "audio/soundFX/FX7/facesit.wav" volume 0.7

    show assdown1 at truecenter:
        zoom 1.02 ypos 455
    with dissolve
    with vpunch
    pause 0.7
    window show
    #Ass down"

    me "Hmphf!?"
    window hide
    show bronfacesitfront
    show bronfacesitt var1
    show bronfacesiteye down
    show bronfacesitfrontd
    with fade
    play sound "audio/soundFX/FX7/facesit2.wav" volume 0.5
    with vpunch
    pause 1.4
    window show
    me "Bfph!"
    "She sits on my face!!"
    me "{size=-8}{alpha=*0.80}I can't breathe!"
    show bronfacesiteye bigu with dissolve
    bron "What's that? "
    bron "'That TOO close? "
    "Bronwen's pussy clenches around my tongue- "
    show bronfacesiteye bigux with dissolve
    bron "That's what you get for scoring a sneaky upskirt on me, perv!"
    "Her warm pussy mushes up against my nose and lips, filling my senses with her feminine sweat."
    me "{size=-8}{alpha=*0.80}Bmhp-!"
    "As I try to breathe her pussy lips press up against my open mouth, my wet tongue coating her warm folds."
    me "{size=-8}{alpha=*0.80}Mmfhhp-"
    hide bronfacesiteye with dissolve
    bron "Mmh-"
    bron "Trying to get some air, boy? "
    window hide
    scene black with dissolve
    play sound "audio/soundFX/move2.wav" volume 0.8
    show blackshake at truecenter zorder -100
    pause 0.3
    show assdown2 at truecenter:
        zoom 1.02 ypos 455
    with fade
    with vpunch
    pause 0.7
    window show
    "She moves back up to let me breathe."
    window hide
    play sound "audio/soundFX/swof.mp3" volume 1.0
    scene sitface03 at truecenter:
        zoom 1.02 ypos 455
    show blackshake at truecenter zorder -100
    show pussydripface at truecenter:
        zoom 1.02 ypos 455
    show sitfaced evil at truecenter:
        zoom 1.02 ypos 455
    with dissolve
    with vpunch
    pause 0.7
    window show
    me "Phahk-kah-"
    "I cough as her fluids drip down on my face!"
    me "One secon-"
    bron "Oh, I don't think so!"
    show sitfaced evil2 at truecenter:
        zoom 1.02 ypos 455
    with dissolve
    bron "That mouth of yours is only getting you in trouble!"
    bron "You should thank me for shutting you up-"
    "Her face is absolutely menacing, and I don't think she'll give me long!"
    "I need to make the most of when she gets back down on me-"
    window hide
    menu:
        with dissolve

        "Continue licking her pussy!":
            $ bronahole = False

        "Adjust to her ass!":
            $ bronahole = True

    window hide
    show assdown2 at truecenter:
        zoom 1.02 ypos 455
    with dissolve
    play sound "audio/soundFX/FX7/facesit.wav" volume 0.2
    with vpunch
    scene bronfacesitfront
    show blackshake at truecenter zorder -100
    if bronahole == True:
        show bronfacesitanal
    else:
        show bronfacesitfront
    show bronfacesitt var2
    show bronfacesiteye down
    show bronfacesitfrontd
    show bronfacesiteye big
    with fade
    play sound "audio/soundFX/FX7/facesit2.wav" volume 0.8
    with vpunch
    pause 1.4
    window show
    if bronahole == True:
        "I arch my back, adjusting my posture so my tongue slides up against her warm asshole-"
        #Change lewd
        show bronfacesiteye lewdoo with dissolve
        bron "Hahhn?!"
        bron "Naughty boy..."
        me "{size=-8}{alpha=*0.80}Mpphhl-"
        "Her tight anal ring squeezes my tongue."
        play sound "audio/soundFX/move.wav" volume 0.8
        with vpunch
        "She pushes her thick cheeks down on me harder!"
        show bronfacesiteye lewdoox with dissolve
        bron "Thaat's it... Dig your slippery tongue in there~"
        bron "You're a real ass lover, aren't you? "
    else:
        "Her thick ass smacks down on me again, and my tongue enters her warm pussy."

        show bronfacesiteye lewdoo with dissolve
        bron "Hahh- "
        bron "Going deeper this time, huh?~"
        me "{size=-8}{alpha=*0.80}Mpphhl-"
        "Her wet pussy squeezes my tongue."
        play sound "audio/soundFX/move.wav" volume 0.8
        with vpunch
        show bronfacesiteye lewdoox with dissolve
        bron "Thaat's it... Get right in there~"
        "She pushes her thick cheeks down on me harder!"
        bron "You love licking pussy, don't you? "
    play sound "audio/soundFX/move.wav" volume 0.8
    with vpunch
    me "{size=-8}{alpha=*0.80}Nnhpf-"
    show bronfacesiteye big with dissolve
    bron "Ffuck, it's hot in here!"
    "Bronwen holds her shirt between her teeth, letting some of her sweat trails down her body and onto my face."
    "I need to take back some control!"

    window hide
    show blackshake at truecenter zorder -100
    if bronahole == False:
        show bronfaceshakegrablicc
    else:
        show bronfaceshakegrabliccanal

    show bronfaceshaked
    hide bronfacesitfrontd
    show bronfacesitfrontd
    with dissolve
    play sound "audio/soundFX/get.mp3" volume 0.7
    with vpunch
    show bronfacesiteye downbig with dissolve
    pause 0.5
    window show
    bron "Hnnf?!"
    if bronahole == True:
        "I grab her thighs and vigorously circle my tongue around her opening-"

    else:
        "I grab her thighs and vigorously move my tongue up and down her clit!"
    window hide
    play sound "audio/soundFX/swof.mp3" volume 0.6
    hide bronfacesitt with dissolve
    queue sound "audio/soundFX/slap.wav" volume 0.3
    with vpunch
    pause 0.2
    show bronfacesitt var3
    hide bronfacesiteye
    show bronfacesitt var4xxx
    with dissolve
    pause 0.5
    window show
    "I hear her heavy tits flop down against her chest!"
    bron "Haahn!-"
    "She might be losing her composure a bit!"
    show bronfacesitt var4xxxx with dissolve
    bron "Ah-ahh-"
    "But I'm running out of air! I can't-"
    window hide
    show black with dissolve
    play sound "audio/soundFX/move2.wav" volume 0.8
    scene assdown2 with fade
    show blackshake at truecenter zorder -100
    with vpunch
    pause 0.3
    play sound "audio/soundFX/swof.mp3" volume 0.5
    show sitfacenudez
    show sitfacenudezd
    with dissolve
    pause 0.3
    window show
    bron "A-Aahh~"
    "Bronwen moans loudly, her big tits swinging back and forth."
    me "Pwaahn! "
    "Her legs shake-"
    window hide


label chaptseven2:
    window hide
    show black with dissolve
    pause 0.3
    scene assclap
    show blackshake at truecenter zorder -100
    show twer rk1
    show twerx wideeye2
    if bronahole == True:
        show assclapanal
    with fade
    play sound "audio/soundFX/FX7/facesit.wav" volume 0.3
    with vpunch
    pause 1.4
    window show
    if bronahole == True:
        "And she falls forward onto my chest, my tongue escaping her warm ass."
    else:
        "And she falls forward onto my chest, my tongue escaping her warm pussy."
    me "W-Was that too much for you?"
    show twerx angry with dissolve
    bron "Pfeh..."
    bron "'Think I lost my cool? "
    me "Sure looks like it. "
    show twerx angry2 with dissolve
    bron "I'm just letting you breathe! "
    show twerx close2
    show twerx base
    with dissolve

    bron "Now take a moment to get some air in those lungs, boy... 'cus I'm going on top for more soon!"
    "Bronwen starts shaking her ass teasingly, her thick cheeks clapping in front of me."
    window hide

    show twer rk2
    hide assclapanal
    with dissolve

    play sound "audio/soundFX/FX7/twerk2.wav" volume 0.4
    show twer rk3 with dissolve
    pause 0.3

    show twer rk1 with dissolve
    pause 0.3
    show twer rk2 with dissolve

    play sound "audio/soundFX/FX7/twerk.wav" volume 0.4
    show twer rk3 with dissolve
    pause 0.3

    show twer rk1 with dissolve
    pause 0.3
    show twerx bigeye with dissolve
    show twerx bigeye2
    with dissolve
    window show

    bron "Worried you won't be able to handle more of this big, strong ass?"

    window hide
    #show twer rk1 with dissolve
    show twer rk2 with dissolve
    #show twer rk1 with dissolve
    play sound "audio/soundFX/FX7/twerk2.wav" volume 0.4
    show twer rk3 with dissolve
    pause 0.3
    #show twer rk2 with dissolve
    show twer rk1 with dissolve
    pause 0.3
    show twer rk2 with dissolve
    #show twer rk1 with dissolve
    play sound "audio/soundFX/FX7/twerk.wav" volume 0.4
    show twer rk3 with dissolve
    pause 0.3
    #show twer rk2 with dissolve
    show twer rk1 with dissolve
    pause 0.3
    show twer rk2 with dissolve
    #show twer rk1 with dissolve
    play sound "audio/soundFX/FX7/twerk2.wav" volume 0.4
    show twer rk3 with dissolve
    pause 0.3
    #show twer rk2 with dissolve
    show twer rk1 with dissolve
    pause 0.3
    window show

    "She continues shaking it up and down, making her big muscles jiggle."
    me "Fhhnn-"
    if bronahole == True:
        "Seeing her cheeks smack together in front of her wet ass is hypnotic!"

    else:
        "Seeing her cheeks smack together in front of her wet pussy is hypnotic!"
    show twerx close2 with dissolve
    bron "Hah- "
    show twerx base2 with dissolve
    bron "You like those sounds, boy?"

    window hide

    show twer rk2 with dissolve

    play sound "audio/soundFX/FX7/twerk2.wav" volume 0.4
    show twer rk3 with dissolve
    pause 0.3

    show twer rk1 with dissolve
    pause 0.3
    show twer rk2 with dissolve

    play sound "audio/soundFX/FX7/twerk.wav" volume 0.4
    show twer rk3 with dissolve
    pause 0.3

    show twer rk1 with dissolve
    pause 0.3
    show twerx bigeye2
    with dissolve
    show twerx bigeye with dissolve
    window show
    bron "I just hope the view didn't distract you from breathing-"
    bron "'Cus my patience has run out!"
    "!!"
    "She thinks I'm some pushover she can do whatever she wants to! "
    "I need to get back in control somehow!"


    window hide
    play sound "audio/soundFX/swof.mp3" volume 1.0
    show bronfaceridebase
    show bronfaceridhand two
    show bronfacerid lookbac
    with fade
    play sound "audio/soundFX/FX7/facesit2.wav" volume 0.5
    with hpunch
    pause 0.5
    window show
    bron "Fheeh?!"
    "I forcefully pull her ass up into my face, my cock sliding in between her tits!"
    #dirty talk
    show bronfaceridhand down with dissolve
    me "Dhu whu lhiyke dhat you thhurty shlut?" # bad pronounciation
    show bronfacerid dafak with dissolve
    bron "W-What?"
    "She can't hear me... I gotta assert my dominance in some other way!"
    window hide
    show bronfaceridhand one
    with dissolve
    play sound "audio/soundFX/FX2/spank.wav" volume 0.6
    with vpunch
    show bronfacerid ahegaoangry with dissolve
    pause 0.7
    show bronfacerid ahegao
    with dissolve
    pause 0.3
    window show


    "I smack her ass hard!"
    show bronfaceridhand down
    show bronfaceridebasespank
    with dissolve
    bron "Haaah-"
    "She moans loudly-"
    show bronfacerid lookbac with dissolve
    bron "You fucker!"
    window hide
    show bronfaceridhand one
    show bronfaceridebasespank2
    with dissolve
    play sound "audio/soundFX/FX2/spank.wav" volume 0.6
    with vpunch
    pause 0.2
    show bronfacerid ahegao
    with dissolve
    pause 0.8
    play sound "audio/soundFX/FX6/20131__gezortenplotz__31arrow-shot.wav" volume 0.7
    show bronfaceridpeen zero
    show bronfaceridpeenzero
    with dissolve
    show bronfacerid surprise
    hide bronfaceridpeenzero
    with dissolve
    pause 0.5
    window show
    bron "Gah?-"
    "My cock flops out as Bronwen's body shakes from my second smack!"
    window hide
    hide bronfaceridpeenzero
    show bronfaceridhand down
    hide bronfaceridebasespank2
    show bronfaceridebasespankdouble
    with dissolve
    pause 0.5
    show bronfacerid angry0 with dissolve
    window show
    bron "Ehh-"
    me "Heheh..."
    "I can't help but chuckle after eharing her moan again!"
    "My dick is throbbing right in front of her face."
    #switch to biting dick angle
    show bronfacerid hnn with dissolve
    bron "Getting bold, are we?"
    bron "Think you're suddenly in control just 'cus you got a single moan out of me?"
    show bronfacerid grr with dissolve
    bron "..."
    bron "I'll make you whimper..."
    me "Y-Yeah?"
    "I'm getting excited!"
    #screenshake
    window hide
    show blackopacity with dissolve
    play sound "audio/soundFX/swof.mp3" volume 0.9
    show bronbite bite1 with dissolve
    pause 0.5
    window show
    bron "Mhmm~"
    "I feel her breath on my cock!"
    show bronbite bite2 with dissolve
    bron "Let's get this skin up, aaaand-"
    "Is the blowjob finally coming?!"
    window hide
    $ renpy.music.set_volume(0.0, delay=0, channel='music')
    play sound "audio/soundFX/FX6/crunchbite2.wav" volume 0.3
    show bronbite bite3 with vpunch
    pause 0.3
    window show
    bron "{size=+5}{i}*CHEW*"
    me "EhnnMmnf!!"
    "She bit the tip of my dick!!"
    window hide
    $ renpy.music.set_volume(0.15, delay=0, channel='music')
    pause 0.1
    $ renpy.music.set_volume(0.30, delay=0, channel='music')
    pause 0.1
    $ renpy.music.set_volume(0.60, delay=0, channel='music')
    pause 0.1
    $ renpy.music.set_volume(0.80, delay=0, channel='music')
    pause 0.1
    $ renpy.music.set_volume(1.00, delay=0, channel='music')
    show bronbite bite4 with dissolve
    window show
    bron "Was that a whimper?"
    me "Ghahh, n-no!"
    me "Let go!"
    "I'll smack her ass again to make her let go!"
    window hide
    pause 0.1
    play sound "audio/soundFX/FX2/spank.wav" volume 0.6
    with vpunch
    show bronbite bite5
    with dissolve
    window show
    "She moans and lets her lips close on my dick."
    bron "Mmmhh-"
    me "Th-That's more like it!"
    window hide
    show bronfacerid droolx
    show bronfaceridpeen two behind bronfacerid

    hide bronbite
    with dissolve
    hide blackopacity with dissolve
    pause 0.5
    window show
    "She pulls her lips off the tip of my dick, a bit of spit connecting her mouth to my cock."
    #pull back lost composure twerk2-pose but now shes messy and like she orgasmed."
    bron "Hahhh..."
    "Bronwen's pussy twitches and leaks over my face-"
    window hide
    scene assclapdown
    show blackshake at truecenter zorder -100
    show twerx xahegao
    if bronahole == True:
        show assclapdowncum
    else:
        show assclapdowncumnoanal

    with fade
    play sound "audio/soundFX/move2.wav" volume 0.9
    with vpunch
    pause 0.5
    window show
    bron "Puuhff-"
    "Her thick ass is a sloppy mess."
    hide twerx with dissolve
    bron "Th-This won't do..."
    me"Did you just...?"
    me "I thought you were supposed to make ME get off! "
    window hide
    show twerx xhate behind assclapdowncum, assclapdowncumnoanal
    show assclapdowncumx
    with dissolve
    play sound "audio/soundFX/Dun.wav" volume 0.3
    with hpunch
    pause 0.3
    window show
    bron "OH?"
    "She looks pissed!"
    bron "Well, you asked for it!"
    window hide
    show black with fade
    pause 0.5
    window show
    #blackbg
    "She violently flips me around!"
    window hide
    play sound "audio/soundFX/FX5/stepknuck.wav" volume 0.3
    with hpunch
    scene rearnakedstrokebase
    show blackshake at truecenter zorder -100
    show rearnakedstrof grin
    with fade
    with vpunch
    pause 0.5
    window show
    #rearnakedstroke
    "Bronwen locks my hips in place with her strong arms, her aggressive face looking down on me."
    bron "Now, now..."
    me "GHA-"
    "I feel so exposed like this!!"

    show rearnakedstrof grin2 with dissolve
    bron "Let's see if you can take THIS!"
    window hide
    play sound "audio/soundFX/swof.mp3" volume 0.3
    show rearnakedstroke up with dissolve
    pause 0.5
    hide rearnakedstroke up with dissolve
    pause 0.5
    show rearnakedstroke up with dissolve
    pause 0.5
    hide rearnakedstroke up with dissolve
    pause 0.5
    window show

    "She slowly starts jerking my cock up and down. "
    me "Ahhg-"
    show rearnakedstrof bite
    with dissolve
    bron "'You like that, do you?"
    "She giggles with a scary look over her face."
    bron "Then reach the finish line already -"
    show rearnakedstrof close with dissolve
    bron "This \"gift\" of mine has taken long enough!"
    window hide
    play sound "audio/soundFX/swof.mp3" volume 0.3
    show rearnakedstroke up with dissolve
    pause 0.8
    hide rearnakedstroke up with dissolve
    pause 0.5
    show rearnakedstroke up with dissolve
    pause 0.8
    show rearnakedstrof grin with dissolve
    window show

    bron "Now be a good boy and cum already! "
    me "You'll have to work harder to make THAT happen!"
    window hide
    play sound "audio/soundFX/swof.mp3" volume 0.3
    hide rearnakedstroke up with dissolve
    hide rearnakedstrof with dissolve
    window show
    bron "Yeah?"
    "Her tongue reaches out and licks my buttcheek!"
    me "Uwhaa?!"
    show rearnakedstroke finger0 with dissolve
    bron "Can you dish it as well as take it, pervert?"
    "She loosens her grip slightly, trailing her finger along my cock to my cockring, her digit on its way to my butt!"
    "And I'm about to cum at any moment!"
    "But her grip seems far looser now that she isn't holding me with both arms, I may have some wiggle room to turn the tables!"
    window hide
    menu:
        with dissolve


        "{size=+2}You wish, NO WAY! \n {alpha=*0.80} {size=-3} *Wiggle free and take control!*":
            window show
            me "You wish, NO WAY!"
            window hide
            show black with fade
            play sound "audio/soundFX/FX6/trip.wav" volume 0.7
            with hpunch
            jump overpowercum




        "Do your best, I can take it! \n {alpha=*0.80} {size=-3} * Let her continue to your butt*":
            window show
            me "Do your best, I can take it!"
            window hide
            scene buttprodbase
            show blackshake at truecenter zorder -100
            show buttprodnormal
            show buttprohand softslap
            with fade
            pause 0.3
            window show
            bron "Oh yeah...? "
            bron "Not one to turn down a challenge, eh?"
            "I can't let her get the better of me, even if I feel like I'm so close to busting!"
            show buttprodnormal2x with dissolve
            bron "I was going to spank you as revenge..."
            "That'd hurt..."
            show buttprodnormal2 with dissolve
            bron "But on second thought-"
            window hide
            play sound "audio/soundFX/swof.mp3" volume 0.3
            hide buttprohand with dissolve
            pause 0.3
            hide buttprodnormal
            hide buttprodnormal2
            hide buttprodnormal2x
            show buttprodbase
            with dissolve
            pause 0.3
            window show
            if bronahole == True:
                bron "Since you played with my holes..."
            else:
                bron "Since you played with my hole... "
            bron "I should play with yours!"
            "She's terrifying!!"
            window hide
            menu:
                with dissolve



                "I can take your finger, EASY!":
                    window show
                    me "I can take your finger, EASY!"
                    show buttpro tonguewide
                    with dissolve
                    bron "Hah! "
                    bron "Let's find out-"
                    window hide
                    show buttprohand sharp
                    with dissolve
                    pause 0.5
                    show buttprohand sharp2
                    with dissolve
                    #play sound "audio/soundFX/swof.mp3" volume 0.2
                    with vpunch
                    pause 0.6
                    window show
                    me "GAH-"
                    "The first digit of her finger slips inside my ass, making my muscles squeeze her tight-"
                    bron "There, there~"
                    window hide
                    show buttprohand sharp with dissolve
                    pause 0.3
                    show buttprohand sharp2 with dissolve
                    pause 0.3
                    show buttprohand sharp with dissolve
                    pause 0.3
                    show buttprohand sharp2 with dissolve

                    show buttprodnormal with dissolve
                    pause 0.5
                    jump bronfingerass



                "On second thought, fuck this!{alpha=*0.80} {size=-3} *Wiggle free and take control!*":
                    window show
                    me "On second thought, fuck this!"
                    window hide
                    show black with fade
                    play sound "audio/soundFX/FX6/trip.wav" volume 0.7
                    with hpunch
                    jump overpowercum
            #Choice to have her spank you or finger.



label bronfingerass:
    scene rearnakedstrokebase
    show blackshake at truecenter zorder -100

    show rearnakedstroke finger2x


    with fade
    play sound "audio/soundFX/swof.mp3" volume 0.3
    with vpunch
    pause 0.4
    window show
    me "Aahgh!"
    show rearnakedstroke finger2 with dissolve
    bron "Thaat's it-"
    show rearnakedstroke finger2x with dissolve
    pause 0.2
    show rearnakedstroke finger2x1 with dissolve
    "Her finger gets deeper and pushes against my prostate."
    "It feels strange- but it shoots a strange pleasure through my whole system!"
    "And it's about to send me over the edge!"
    window hide
    show rearnakedstroke finger2 with dissolve
    pause 0.2
    show rearnakedstroke finger2x2 with dissolve
    window show
    bron "Just let go, pervert~"
    "I can't hold back much longer!"





    window hide
    menu:
        with dissolve


        "{size=+3}That's enough! \n {alpha=*0.80} {size=-3} *Push free and take control!*":
            window show
            me "You wish, NO WAY!"
            $ cumonselfbron = False
            window hide
            show black with fade
            play sound "audio/soundFX/FX6/trip.wav" volume 0.7
            with hpunch
            jump overpowercum


        "{size=+2}I'm cumming!  \n {alpha=*0.80} {size=-3} *Let go and cum on the spot!*":
            window show
            me "I'm cumming!"
            window hide
            pause 0.2
            show rearnakedstroke fingercum1 with dissolve
            pause 0.3
            show white at truecenter zorder 100 with dissolve
            hide white with dissolve
            show rearnakedstroke fingercum1x with dissolve
            with vpunch
            pause 0.4
            show rearnakedstroke fingercum1xx with dissolve
            pause 0.5
            window show
            "My cock spasms and I cum all over my own chest, feeling the warm fluid splash against my body and up toward my face-"
            $ cumonselfbron = True
            bron "Hahah!"
            "I notice Bronwen's strong grip weaken as she laughs, so I press my hands against the ground while arching my back forward-"
            window hide
            scene black with dissolve
            show blackshake at truecenter zorder -100
            play sound "audio/soundFX/FX6/trip.wav" volume 0.7
            with hpunch
            window show
            "And I use all my strength to explosively push her backward!"
            window hide
            with vpunch
            jump cumonbron




label overpowercum:

    with vpunch
    show black
    window show
    "I muster up all my strength and use my arms to push my body forward off the ground!"
    window hide
    play sound "audio/soundFX/FX6/twirl.wav" volume 0.3
    with hpunch
    scene brontop
    show blackshake at truecenter zorder -100
    show bronto surprise zorder 100
    show brontopvignette
    with fade
    play sound "audio/soundFX/get.mp3" volume 0.6
    with vpunch
    pause 0.5
    window show
    "I end up on top of her hips with my cock between her tits!"
    bron "Y-You're pretty strong-"
    show bronto surpriseew with dissolve
    bron "I mean-"
    bron "Not as weak as I thought..."
    window hide
    show brontopsqueeze with dissolve
    play sound "audio/soundFX/grab.wav" volume 0.8

    with hpunch
    pause 0.2

    show bronto grit
    with dissolve
    pause 0.3
    window show
    "I give her tits a firm squeeze in response-"
    hide brontopsqueeze with dissolve
    me "Yeah? "
    show bronto bite2 with dissolve
    bron "Mhn-"
    me "Well, now I'm in charge!"
    show bronto bite3 with dissolve
    bron "..."
    show bronto eeh with dissolve
    bron "'Guess you've earned your spot."
    show bronto giveit with dissolve
    bron "So show me what you've got, silly boy."
    "Fhhuck, she's suddenly accepting her position!"
    window hide

    menu:
        with dissolve


        "Take it! \n {alpha=*0.80} {size=-3} *Cum over her face and tits!*":

            window show
            label cumonbron:
            if cumonselfbron == True:
                scene brontop
                show blackshake at truecenter zorder -100
                show bronto surprise zorder 100
                show brontopvignette
                with fade
                play sound "audio/soundFX/get.mp3" volume 0.6
                with vpunch
                pause 0.5
                window show
                "And I end up on top of her hips with my cock between her tits!"
                bron "Y-You're pretty strong-"
                show bronto surpriseew with dissolve
                bron "I mean-"
                show bronto bite2 with dissolve
                bron "Not as weak as I thought..."
                me "Now I'm in charge!"
                show bronto bite3 with dissolve
                bron "..."
                show bronto eeh with dissolve
                bron "'Guess you've earned your spot."
                show bronto giveit with dissolve
                bron "So show me what you've got, silly boy."
                "Fhhuck, she's suddenly accepting her position!"

            $ broncuminmouth = False

            me "T-Take it! "
            if cumonselfbron == True:
                "My cock spasms a second time-"
            else:
                "My cock spasms-"
            window hide
            show white at truecenter zorder 100 with dissolve
            pause 0.2
            hide white with dissolve
            with vpunch
            hide bronto
            show brontocu um1 at truecenter zorder 99
            show bronto wha behind brontocu
            with dissolve
            pause 0.5

            hide brontocu
            show brontoc on1  at truecenter zorder 98
            with dissolve
            pause 0.3
            show bronto surpriseew with dissolve
            window show


            if cumonselfbron == True:
                "My second shot lands on her face-"
            else:
                "My first shot lands on her face-"
            bron "Egh-"

            window hide

            with vpunch
            show brontocu um3 at truecenter zorder 99
            with dissolve
            pause 0.3
            hide brontocu
            show brontoco on2
            show bronto bitecumx
            with dissolve
            pause 0.4
            window show
            if cumonselfbron == True:
                "And I finish off on her chest!"
                #Add some comement about strength if this is true below ------------------------------------------------
            else:
                "My second shot favors her chest-"

            show bronto bitecum with dissolve
            bron "D-Damnn, that's... more than I expected-"
            show bronto bitecum2 with dissolve
            bron "So warm..."
            bron "It doesn't feel too bad on me~"
            window hide
            show brontopflaccx
            with dissolve

            window show
            "My cock softens a bit on her belly."


        "{size=+4}Not yet!{/size} {space=6}{size=+1} Open up, slut.{/size} \n {alpha=*0.80} {size=-3} * Make her open up to cum in her mouth! *":
            window show
            $ broncuminmouth = True
            me "Not yet! "
            me "Open your mouth, slut. "
            show bronto worst with dissolve
            bron "You wish!"
            window hide
            show brontopsqueeze

            with dissolve
            play sound "audio/soundFX/grab.wav" volume 0.4
            with hpunch
            show bronto lilopenz
            with dissolve
            pause 0.4
            hide brontopsqueeze
            with dissolve
            window show
            "I squeeze her tits hard again!"
            show bronto lilopen with dissolve
            bron" Ehnf-"
            "She opens her mouth a tiny bit with a slight whimper."
            me "Come on, now!"
            window hide
            show brontopsqueeze with dissolve
            play sound "audio/soundFX/grab.wav" volume 0.5
            with hpunch
            show bronto lilopenzx with dissolve
            pause 0.4
            hide brontopsqueeze with dissolve
            window show
            "I squeeze them hard again!"
            me "Let that tongue out!"
            bron "!!"
            "She glares at me-"
            show bronto mouthopen with dissolve
            bron "Mlaa~"
            "Then fully opens up. "
            me "Good girl!"
            bron "..."
            "Making her submit to my desire finally sends me over the edge!"
            #*cumcum*
            window hide
            show white at truecenter zorder 100  with dissolve
            pause 0.2
            hide white with dissolve
            with vpunch
            show brontocu um1 at truecenter zorder 100
            with dissolve
            pause 0.2

            hide brontocu
            show bronto mouthopencum
            with dissolve
            pause 0.3
            window show

            "My first shot lands in her mouth-"
            bron "Ugk-"
            window hide

            with vpunch
            show brontocu um2 at truecenter zorder 99
            show  bronto mouthopencum zorder 98
            with dissolve

            hide brontocu
            show brontoc on1 at truecenter zorder 100
            with dissolve
            show  bronto mouthopencum2 zorder 98 with dissolve
            pause 0.3
            window show
            "And I cover her face with the rest!"
            bron "Ghll-"
            me "Now, now..."
            me "Swallow it all down like a good pig!"
            show bronto mouthopencum2a with dissolve
            bron "..."
            show bronto mouthopencum2ab with dissolve
            "She closes her mouth, grimacing with her cheeks filled with my warm cum. "
            bron "Mmh-"
            show bronto mouthopencum2abc with dissolve
            with vpunch
            bron "*Gulp*"
            show bronto mouthopen with dissolve
            bron"Puaah-"
            bron "There!"
            me "That's what I like to see."
            window hide
            pause 0.1


            show brontopflacc

            with dissolve
            pause 0.5
            show bronto mouthopencum2abcd with dissolve
            pause 0.5

            window show

            "My cock softens a bit on her belly."



    #choice
    stop music fadeout 6.5
    queue music  "audio/Birds.wav" fadein 8.0 volume 0.1

    show brontoglare zorder 99 with dissolve
    bron "Now, take that ring off..."
    show bronto mouthopencum2abcde
    hide brontoglare
    with dissolve
    bron "'Cus if you get stuck again, I won't let you slip out-"
    me "*Gulp*"
    "I swallow hard as she stares me down."
    window hide
    scene black with fade
    show blackshake at truecenter zorder -100
    window show
    "I roll over onto my back-"
    play sound "audio/soundFX/move2.wav" volume 0.6
    window hide
    scene peenprofilebase2:
        xalign -0.0
    show blackshake at truecenter zorder -100
    show peenprofile ringhalf:
        xalign -0.0
    with fade
    pause 0.5
    window show
    "And get the ring off my flaccid cock as fast as I can!"
    window hide
    pause 0.1
    play sound "audio/soundFX/move.wav" volume 0.4
    show peenprofile ringhalf2:
        xalign -0.0
    with dissolve
    pause 0.7
    play sound "audio/soundFX/Jar Open2.wav" volume 0.8
    show peenprofile ringhalf3:
        xalign -0.0
    with dissolve


    pause 0.6
    play sound "audio/soundFX/FX2/dat-s-right.wav" volume 0.6
    window show
    me "Phew!"
    me "I finally got it off!"
    window hide
    scene black with fade
    show blackshake at truecenter zorder -100
    window show

    bron "Don't make a mess out of my carpet!"
    play sound "audio/soundFX/grabby.wav" volume 0.9
    stop music fadeout 1.0
    queue music "audio/Alexander Nakarada - Collection - Celtic & Medieval - 13 Norður.mp3" fadein 4.0 volume 0.3
    with hpunch
    "Bronwen picks me up-"
    window hide





    #"ghaa cum. either on her or on yourself."
    window hide
    scene black with dissolve
    show blackshake at truecenter zorder -100
    pause 0.3
    play sound "audio/soundFX/Sit Pillow.wav" volume 0.8
    scene black
    if cumonselfbron == True:
        scene broncummedondude at truecenter:
            zoom 0.72 ypos 440
        show blackshake at truecenter zorder -100

        show black
        with fade
        show broncummedondude at truecenter:
            zoom 0.72  ypos 440
            linear 6.5 zoom 0.72 ypos 610
        hide black with dissolve
        pause 6.5
        show broncummedondude at truecenter:
            zoom 0.72 ypos 610
        window show
        jump chosenbroncum




    if broncuminmouth == False:
        scene broncummedon at truecenter:
            zoom 0.72 ypos 440
        show blackshake at truecenter zorder -100

        show black
        with fade
        show broncummedon at truecenter:
            zoom 0.72  ypos 440
            linear 6.5 zoom 0.72 ypos 610
        hide black with dissolve
        pause 6.5
        show broncummedon at truecenter:
            zoom 0.72 ypos 610
        window show
        jump chosenbroncum

    if broncuminmouth == True:
        scene broncummedonface at truecenter:
            zoom 0.72 ypos 440
        show blackshake at truecenter zorder -100

        show black
        with fade
        show broncummedonface at truecenter:
            zoom 0.72  ypos 440
            linear 6.5 zoom 0.72 ypos 610
        hide black with dissolve
        pause 6.5
        show broncummedonface at truecenter:
            zoom 0.72 ypos 610
        window show
        jump chosenbroncum

    #now relaxing together


label chosenbroncum:
    scene bronlaybase at truecenter:
        zoom 0.72 ypos 610
    show blackshake at truecenter zorder -100
    if cumonselfbron == True:
        show bronlaycumbron zorder 100 at truecenter:
            zoom 0.72 ypos 610
        show bronlaycumguy zorder 99 at truecenter:
            zoom 0.72 ypos 610
        show bronlays closeg at truecenter:
            zoom 0.72 ypos 610
        jump nexttimebronbed

    if broncuminmouth == False:
        show bronlaycumbron zorder 100 at truecenter:
            zoom 0.72 ypos 610
        show bronlays closeg at truecenter:
            zoom 0.72 ypos 610
        jump nexttimebronbed

    if broncuminmouth == True:
        show bronlaycumface zorder 100 at truecenter:
            zoom 0.72 ypos 610
        show bronlays closeg at truecenter:
            zoom 0.72 ypos 610
        jump nexttimebronbed
label nexttimebronbed:


    "And she crams me into her bed!"
    show bronlays opengao with dissolve
    bron "Huuughh-"
    show bronlays sideeye with dissolve
    bron "I didn't expect that load... "
    bron "..."
    show bronlays smileside with dissolve
    bron "Or your size."
    show bronlayd squish2 at truecenter:
        zoom 0.72 ypos 610
    with dissolve
    me "{size=-8}{alpha=*0.80}I'm phull of surphrises."
    "I do my best to speak with absolutely no room, her arm and shoulder squishing my face-"
    show bronlays sidesnark with dissolve
    bron "Hmph, I guess. "
    bron "But you sure seem inexperienced... "
    show bronlays sideeye with dissolve
    bron "'Gotta learn how to get yourself off-"
    show bronlays smilex with dissolve
    bron "That way you'll always have a good time, heh!"
    show bronlayd squish with dissolve
    me "{size=-8}{alpha=*0.80} Ishn't thaking a long thime a good thingk? "
    show bronlays sidesnark2 with dissolve
    bron "The goal was to get the ring off quickly!"
    hide bronlayd with dissolve
    me "{size=-6}{alpha=*0.85}That's on you! "
    me "{size=-6}{alpha=*0.85}You're just mad you couldn't make me cum faster!"
    show bronlays sidesnark3 with dissolve

    bron "I barely tried! "
    show bronlays sidesnark2 with dissolve
    bron "And It's gotta be because the cockring made your dick numb... "
    show bronlays sidesnark with dissolve
    bron "That's what it's for after all."
    "Sounds like I struck a nerve-"
    show bronlayd squish2 at truecenter:
        zoom 0.72 ypos 610
    with dissolve
    me "{size=-4}{alpha=*0.85}Fine..."

    #SHAKESHAKESHAKE"

    window hide
    stop music fadeout 0.1
    play sound "audio/soundFX/Step1.wav" volume 0.3
    with vpunch
    pause 0.3
    play sound "audio/soundFX/Step2.wav" volume 0.4
    with vpunch
    pause 0.3
    play sound "audio/soundFX/Step1.wav" volume 0.5
    with vpunch
    play music "audio/Mega+Heavy+Suspense+-+320bit.mp3" fadein 1.0 volume 0.3
    show bronlays surprise1 with dissolve
    pause 0.6
    window show
    bron "!!"# o.o
    show bronlayd aah with dissolve
    me "{size=-4}{alpha=*0.90} I-Is that Rolf?"
    play sound "audio/soundFX/FX2/pig-scream-loud-oink.wav" volume 0.9
    rolf "{size=+3}Bronwen!?"
    rolf"{size=+5}'You up there?!"

    "{size=+3}SHIT! "
    "That's DEFINITELY Rolf!"
    play sound "audio/soundFX/FX2/pig-squeak.wav" volume 0.8
    rolf "{size=+7}I'm coming up!"
    window hide
    play sound "audio/soundFX/Step1.wav" volume 0.7
    with vpunch
    pause 0.2
    play sound "audio/soundFX/Step2.wav" volume 0.8
    with vpunch
    pause 0.2
    play sound "audio/soundFX/Step1.wav" volume 0.9
    with vpunch
    show bronlays surprise2 with dissolve
    show bronlays surprise2x with dissolve
    window show
    bron "!!!" #O.O
    me "{size=-2}{alpha=*0.90}What do we do!?"
    window hide
    #*bronwen looks to me-*
    scene black with fade
    show blackshake at truecenter zorder -100
    play sound "audio/soundFX/OpenDoor 2.wav"
    stop music fadeout 0.4
    with hpunch
    pause 0.5
    #*black*
    play sound "audio/soundFX/grabby.wav" volume 1.0
    scene throwoutbase at center:
        zoom 1.0 yoffset 103
    show blackshake at truecenter zorder -100
    show throwoutbron first at center:
        zoom 1.0 yoffset 103

    show throwoutbronstuff at center:
        zoom 1.0 yoffset 103

    with vpunch


    pause 0.5
    window show
    #*loud sound cut to being thrown out!*
    me "GHAH!"
    "She threw me out the window!!"
    #bron looks to door pose
    show throwoutbron first2 with dissolve
    bron "ONE SECOND, DAD!"
    play sound "audio/soundFX/FX4/clothing2.wav" volume 0.1
    show throwoutbron first3 with dissolve
    pause 0.3
    show throwoutbron first4 with dissolve
    #looks to me
    bron "Enjoy your gift, [Protagonist]!!"
    #Splash
    window hide
    play sound "audio/soundFX/Door Slam.wav" volume 0.8
    hide throwoutbron
    with hpunch
    hide throwoutbronstuff
    show throwoutbasex at center:
        zoom 1.0 yoffset 103
        linear 0.5 zoom 1.0  yoffset 0
    pause 0.5
    play sound "audio/soundFX/FX7/fallsplash.wav" volume 0.6
    queue sound "audio/soundFX/FX5/water_driplets_test.mp3" volume 0.2
    show throwoutbasex at center:
        zoom 1.0  yoffset 0
    show splaash with dissolve
    with vpunch
    pause 0.3
    show black with dissolve
    pause 0.2
    scene bigsplash with fade
    show blackshake at truecenter zorder -100
    pause 0.5
    window show
    "I'm in the water!"
    "The current pulls me to the bridge where I grab the ladder to climb back up-"
    window hide

    if playnormal == False:
        scene black with fade
        pause 0.3

    $ unlock("S10")
    $ renpy.end_replay()
    show black with dissolve
    pause 0.2
    play sound "audio/soundFX/FX5/BillyResurface.mp3" volume 0.6
label meetmaplevic:
    scene bg tailorsmithsunset
    show blackshake at truecenter zorder -100
    show bgtailorsmithdoorclose
    show bgsunsetsplash
    show bgsunsetsplashface
    show messwater
    with fade
    pause 0.3
    hide messwater with dissolve
    pause 0.6
    play music "audio/birds.wav" fadein 3.5 volume 0.1
    window show
    #bgchange
    me "Phuuuh-"
    "I quickly pull my shorts back on and put the cursed cockring in my pocket."
    if cumonselfbron == True:
        "'Nice to have all that cum cleaned off... But this water's pretty icky!"
    stop music fadeout 1.0
    window hide
    play sound "audio/soundFX/get.mp3" volume 0.4
    with hpunch
    hide bgsunsetsplashface with dissolve
    pause 0.4
    window show
    "I shake the water off my body."
    #i dont have cum on myself if I did
    play music "audio/Tavern+Brawl+-+320bit.mp3" fadein 7.0 volume 0.2
    "That got way too intense in every way!"
    "Bronwen's so intimidating and she really wanted to do things her way..."
    "At least I was able to turn the tables on her at the very end!"
    "I need to find a strategy to give me the upper hand if I end up in a similar situation in the future."
    "But that'd have to be in another location, I can't risk Rolf showing up again!"
    "If Bronwen hadn't thrown me into the canal and he'd found us in the nude..."
    "I don't even want to think about it!"
    window hide
    pause 0.2
    play sound "audio/soundFX/OpenDoor 2.wav" volume 0.5
    hide bgtailorsmithdoorclose with hpunch
    #*dingding*
    pause 0.5
    window show
    "Maple's door smacks open!"
    window hide
    show maps base :
        zoom 0.99 yoffset 11
    with dissolve
    play sound "audio/soundFX/Door Slam2.wav" volume 0.6
    show bgtailorsmithdoorclose behind maps,vicsu,vicmel  with dissolve
    show maps peacehigh
    show maf opensmile:
        zoom 0.99 yoffset 11
    with dissolve
    pause 0.3
    window show
    jump findemelie

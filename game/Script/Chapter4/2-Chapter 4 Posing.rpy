label posingstart:
    play sound "audio/soundFX/Blanket Move.wav"
    scene positbed
    show posit crosslegs
    with fade

    play music "audio/Em_theme.mp3" fadein 0.1 volume 0.3
    pause 1.0

    if playnormal == False:
        menu:
            with dissolve
            "Play Art Section!":
                window show
            "Jump to Sex!":
                jump gallerysex

    window show
    "Whew!"
    "Those stockings sure are pretty..."
    show positx sitexp1 with dissolve
    emelie " So! "
    emelie " Just grab that brush and give it a go!"
    me " What?"
    me " You're supposed to teach me!"
    show positx sitexp2 with dissolve
    emelie " I want to see what you've got first!"
    emelie " Then I can give you feedback!"
    me " O-okay."
    show positxbrowfrown with dissolve
    emelie " You look a little anxious... "
    me " Yeah, I am..."
    hide positx
    hide positxbrowfrown
    with dissolve
    emelie " Just try to have fun and don't worry about the result!"
    me " Alright, I'll do my best!"
    window hide
    pause 0.3
    show canvaspaint with easeinbottom
    pause 0.3
    show blackopacity behind canvaspaint with dissolve
    window show
    " Here we go...."
    window hide
    play sound "audio/soundFX/FX4/stroke4.wav"
    show black with dissolve
    pause 0.3
    window show
    " My heart is racing but I do my best to paint her body and face."
    show canvasart first behind black
    pause 0.6
    " Time flies and I end up with a final result!"
    window hide
    hide black with dissolve
    pause 0.5
    window show

    me " I'm done!"
    emelie " That was quick!"
    show compart one at truecenter:
        yalign 0.0 xalign 0.0 zoom 1.0
    hide canvaspaint
    hide canvasart first
    show compart one
    with dissolve
    me " I think I did pretty good! "
    me " At least the colors turned out pretty nice."
    emelie " Let me see!"
    me " Okay!"
    window hide
    hide compart one with easeoutbottom
    hide blackopacity with dissolve
    window show
    " I flip the canvas around to show it to her."
    window hide

    show canvasshow with easeinbottom
    show positxeye down
    show positxbrow up
    with dissolve
    window show
    " She looks over my art."
    hide positxeye down
    hide positxbrow up
    show positx surprise
    with dissolve
    emelie " Wow!"
    emelie " That's not bad at all!"
    show positxeye down
    show positxbrow up
    hide positx surprise
    with dissolve
    emelie " It's got a really unique look to it! "
    me " Thanks!"
    show positx sitexp8 with dissolve
    emelie " Very modern."
    " I put the painting down."
    window hide
    hide canvasshow with easeoutbottom
    hide positx
    hide positxeye
    with dissolve
    window show
    emelie " But!"
    show positx sitexp3 with dissolve
    emelie" You were keeping your eyes fixed to the canvas instead of looking at your subject-"
    emelie "-ME!"
    me " Shit, you're right!"
    " Once I started painting I barely looked over to Emelie!"
    me " I must've gotten tunnel vision! "

    show positx sitexp2 with dissolve
    emelie "Yeah! It can happen pretty easily!"
    show positx sitexp1 with dissolve
    emelie " Give it another go!"
    emelie " But this time, try to really observe your subject!"
    hide positx with dissolve
    emelie " Don't paint what you instinctively THINK an eye or a leg looks like! "
    emelie "Take a moment to really look and paint what you see!"
    me " Okay, that makes sense!"
    me " I'll give it a go!"
    #BarelyVisible
    window hide
    show canvaspaint at center:
        yoffset 850
    with easeinbottom
    play sound "audio/soundFX/FX4/stroke3.wav"
    pause 0.8
    window show
    " I keep my canvas low, switching my focus back and forth between Emelie and the canvas."
    " It takes me a bit longer, but Emelie comes off very relaxed and patient so I keep my nerves calm and complete my painting!"
    window hide
    hide canvaspaint
    show compart two at center:
        yoffset 850
    with dissolve
    show compart two at center:
        yoffset 850
        linear 1.0 yoffset 0
    with easeinbottom
    show blackopacity behind compart with dissolve
    pause 0.5
    window show
    "Wow! This turned out a lot better!"
    " Maybe I'm just really bad at drawing from imagination when put on the spot!"
    emelie " How did it go? "
    hide compart two
    show canvashold
    show canvasart second
    show canvasartgallery behind positbed
    show canvasartgallery2 behind positbed
    with dissolve
    me " Your tips really helped!"
    window hide
    hide canvashold
    hide canvasart second
    with easeoutbottom
    hide blackopacity with dissolve

    pause 0.2

    show canvasshow with easeinbottom
    pause 0.3
    show positxeye down
    show positxbrow up
    with dissolve
    window show
    "I show her the painting and she carefully inspects it."
    hide positxeye
    show positx surprise2
    with dissolve
    emelie " Woaah, you're a natural!"
    show positx sitexp1
    show positxeye down
    with dissolve
    emelie " Incredible improvement, I'm impressed!"
    me " Thank you! "
    " That feels really good to hear!!"
    window hide
    hide canvasshow with easeoutbottom
    window show

    show positx sitgrin
    hide positxeye
    with dissolve
    emelie " But, now..."
    emelie " Let's make things a bit more fun!"
    window hide
    pause 0.2
    play sound "audio/soundFX/FX4/clothing2.wav" volume 0.4
    show posit spreadlegs
    hide positx
    with dissolve
    pause 0.5
    window show
    " She spreads her legs!"
    emelie " Drawing the same subject over and over can get a little tiring so..."
    window hide
    pause 0.2
    play sound "audio/soundFX/FX4/clothing2b.wav" volume 0.8
    show posit undress with dissolve
    pause 0.5
    window show

    emelie " I'll make it easier for you to keep your eyes focused on me~ Hihi."
    "She starts removing her bra!"
    window hide
    pause 0.2
    play sound "audio/soundFX/FX4/clothing3.wav" volume 0.7
    show posit topless with dissolve
    pause 0.5
    window show
    emelie " There!"

    " She's entirely topless!"

    me " I'm... definitely still focused!"
    "She smiles and settles with her new pose."
    show positx sitexp2 with dissolve
    emelie " This time, you can try and combine your artistic instincts with your new observational skills!"
    emelie " To create something kinda new!"
    me " Like you did with the painting of the pear?"
    me " Combining creativity with observation."
    show positx sitexp4 with dissolve
    emelie " Exactly!"
    emelie " Or you can try to paint me even more accurately as a challenge!"

    me " Sounds like fun!"
    me "But I don't know where to start..."
    show positx sitexp5 with dissolve
    emelie "Then go from top-to-bottom! Facial features first and then the rest!"
    me " Okay!"


    window hide
    show canvaspaint with easeinbottom
    show blackopacity behind canvaspaint with dissolve
    pause 0.3
    window show
    "So..."
    " Do I get really creative, or do I try my best to capture her likeness?"
    "Hmm..."
    " I don't think I'm skilled enough to get her likeness down on my first attempt even if I try to."
    " So let's just get painting!"
label painting:
    $ artscore = 0
    if redoart == True :


        hide mou
        hide leg
        hide hed
        hide eye
        hide bod
        hide canvashold
        with easeoutbottom
        hide blackopacity with dissolve
        window show
        me " I'm going again on a new canvas!"
        emelie "Yes! Give it your best!"
        window hide
        show canvaspaint
        with easeinbottom
        show blackopacity behind canvaspaint with dissolve
        window show




    menu:
        with dissolve
        "How should I approach her head?"

        "Long!":
            $ arthead = "longer"

            "I'll paint her with a long head!"

        "Wide!":
            $ arthead = "wide"

            "I'll paint her with a wide head!"


        "Round!":
            "I'll paint her with a round head!"
            $ arthead = "normal"
            $ artscore +=1


        "Heroic!":
            "I'll paint her with a heroic head shape!"
            $ arthead = "heroic"


        "Fluffy!":
            "I'll paint her with a fluffy head!"
            $ arthead = "fluffy"

label head:
    window hide
    $ renpy.block_rollback()
    play sound "audio/soundFX/FX4/stroke1.wav" volume 0.8

    if arthead == "longer":
        show hed longer behind eye with dissolve
    if arthead == "wide" :
        show hed wide behind eye with dissolve
    if arthead == "normal":
        show hed normal behind eye with dissolve
    if arthead == "heroic" :
        show hed heroic behind eye with dissolve
    if arthead == "fluffy":
        show hed fluffy behind eye with dissolve

    pause 0.6
    window show

    menu:
        with dissolve
        "Now what about her eyes?"

        "Big!":
            $ arteye = "big"
            $ artscore +=1

            "Let's go for big eyes!"

        "Small!":
            $ arteye = "small"

            "Let's go with small eyes!"

        "Angry!":
            $ arteye = "angry"

            "Let's go with a pair of angry eyes!"

        "Tired!":
            $ arteye = "tired"

            "Let's go with some tired-looking eyes!"

        "Wide-set!":
            $ arteye = "wide"

            "Let's go with wide-set eyes!"

label eyes:
    window hide
    $ renpy.block_rollback()
    play sound "audio/soundFX/FX4/stroke3.wav" volume 0.7

    if arteye == "small":
        show eye small with dissolve
    if arteye == "big" :
        show eye big with dissolve
    if arteye == "angry":
        show eye angry with dissolve
    if arteye == "tired" :
        show eye tired with dissolve
    if arteye == "wide":
        show eye wide with dissolve


    pause 0.6
    window show


    " Hmm..."




    menu:
        with dissolve
        " And her mouth?"

        "Pouting!":
            $ artmouth = "pout"


            "Let's draw her mouth pouting!"

        "Smiling!":
            $ artmouth = "smile"
            $ artscore +=1

            "Let's draw her with a smiling mouth!"

        "Teethy!":
            $ artmouth = "teeth"

            "Let's go with clenching teeth!"

        "Grumpy":
            $ artmouth = "small"

            "Let's draw her with a grumpy mouth!"

        "Snout!":
            $ artmouth = "snout"

            "Maybe a snout will look good!"

label mouth:
    window hide
    $ renpy.block_rollback()
    play sound "audio/soundFX/FX4/stroke1.wav" volume 0.8
    if artmouth == "pout":
        show mou pout with dissolve
    if artmouth == "smile":
        show mou normal with dissolve
    if artmouth == "teeth" :
        show mou teeth with dissolve
    if artmouth == "small" :
        show mou small with dissolve
    if artmouth == "snout" :
        show mou snout with dissolve
    pause 0.6
    window show
















    menu:
        with dissolve
        "Now for her body..."

        "Muscly!":
            $ artbody = "muscly"

            "A muscly body might work!"

        "Droopy!":
            $ artbody = "droopy"

            "A droopy body could be interesting!"

        "Curvy!":
            $ artbody = "curvy"
            $ artscore +=1

            "A curvy body will be nice!"

        "Slim!":
            $ artbody = "slim"

            "A slim body could be different!"

        "Wide!":
            $ artbody = "wide"

            "A wide body could be cool!"
label body:
    window hide
    $ renpy.block_rollback()
    play sound "audio/soundFX/FX4/stroke3.wav" volume 0.6
    if artbody == "muscly":
        show bod muscly behind hed with dissolve
    if artbody == "droopy" :
        show bod droopy behind hed with dissolve
    if artbody == "curvy":
        show bod normal behind hed with dissolve
    if artbody == "slim" :
        show bod slim behind hed with dissolve
    if artbody == "wide" :
        show bod wide behind hed with dissolve
    pause 0.6
    window show













    menu:
        with dissolve
        "And finally her legs!"

        "Beastly!":

            $ artlegs = "beastly"

            "I'll go with some beastly legs to finish it off!"

        "Strong calves!":
            $ artlegs = "calves"

            "I'll go with some muscly calves to finish it off!"

        "Bulging!":
            $ artlegs = "bulgey"

            "I'll go with some bulging legs to finish it off!"

        "Shapely!":
            $ artlegs = "normal"
            $ artscore +=1

            "I'll go with some shapely calves to finish it off!"
        "Skinny!":
            $ artlegs = "skinny"

            "I'll go with some skinny legs to finish it off!"
label legs:
    window hide
    $ renpy.block_rollback()
    play sound "audio/soundFX/FX4/stroke1.wav" volume 0.7
    if artlegs == "beastly":
        show leg beastly with dissolve
    if artlegs == "calves" :
        show leg calves with dissolve
    if artlegs == "normal":
        show leg normal with dissolve
    if artlegs == "bulgey" :
        show leg bulgey with dissolve
    if artlegs == "skinny":
        show leg slim with dissolve

    pause 0.5

    hide canvaspaint
    show canvashold behind bod
    with dissolve
    pause 0.5
    window show
    $ renpy.block_rollback()

    if artscore == 5:
        "Damn!"
        with vpunch
        play sound "audio/soundFX/FX2/dat-s-right.wav"
        " It looks just like her!"
        " A pretty flattering depiction I think! "
        " Should I give it another go or show her the art?"
    else:
        "Woah!"
    if artscore == 3:
        "I took some creative liberties here and there."
        " But stayed true to her appearance in other areas."
        " Pretty uncanny!"
    if artscore == 4:
        "It's very close to looking just like her!"
        " I only drew one feature off. "
        "Hmm."
    if artscore == 1:
        "This sure turned out... interesting..."
        " I took a lot of creative liberties!"
    if artscore == 2:
        "This sure turned out... interesting..."
        " I took a lot of creative liberties!"
    if artscore == 0:
        " This looks absolutely crazy.  "
        " But pretty funny!"



    if redoart == False:
        if artscore == 5:
            "I could try again with a more creative approach."
        else:
            " Fun first attempt with this approach!"
        " Should I give it another go or show her the art?"

    if redoart == True:
        " Should I give it yet another go or show her the art?"



    window hide
    menu:
        with dissolve


        "{size=+5}Let's give it another go!{/size}":
            window show
            "I'll give it another go!"
            window hide
            $ redoart = True
            jump painting

        "I'm satisfied!":
            window show


            me "I'm satisfied!"
            window hide
            hide blackopacity
            with dissolve
            hide mou
            hide leg
            hide hed
            hide eye
            hide bod
            hide canvashold
            with easeoutbottom









#Head
# -HeadSquishy
# -Head
# -HeadBig
#eyes
#mouth and nose
#chest and belly
#legs and feet'

#3x choices each option.
#so a total of 15 PARTS.


    window show
    show blackshake behind positbed
    emelie " Awesome!"
    emelie " Not gonna show it to me?"
    me " Oh right..."
    window hide
    show canvasshow with easeinbottom
    if artscore == 5:
        show positx surprise with dissolve
        with hpunch
        window show
        emelie " Woaaah! What a pretty painting of me!!"
        show positxbrowfrown with dissolve
        emelie " You tried your best to draw me as flattering as possible, huh?"
        me " Yeah."
        show positx sitexp8
        hide positxbrowfrown
        with dissolve
        emelie " That's so cute of you! "
        emelie " And you did such a good job!"
        show positx sitexp1 with dissolve
        emelie " Even if I would've been okay with some craziness, haha!"
        jump afterpaint


    if artscore == 4:
        show positx surprise with dissolve
        with hpunch
        window show
        emelie "Oooh! Well done!"
        show positx sitexp8 with dissolve
        emelie " And pretty accurate too! "



    if artscore == 3:
        show positx surprise with dissolve
        with hpunch
        window show
        emelie "Nicely done!"
        show positx sitexp8 with dissolve
        emelie " Largely looks like me! "
        show positx sitexp7 with dissolve
        emelie " But you took a few creative liberties too which is fun."

    if artscore == 2:
        show positx sitexp9 with dissolve
        play sound "audio/soundFX/Dun.wav" volume 0.5
        with hpunch
        window show
        "!!"
        emelie " Waah!"
        show positx sitexp9b with dissolve
        emelie "Hahaha! "
        show positx surprise with dissolve
        emelie " What an interesting combination!"

    if artscore == 1:
        show positx sitexp9 with dissolve
        play sound "audio/soundFX/Dun.wav" volume 0.5
        with hpunch
        window show

        emelie " !!"
        emelie " Wha-"
        show positx sitexp9b with dissolve
        emelie " You sure went creative with this one, haha!"
        show positx surprise with dissolve

        emelie " A lot is going on here for sure!"

    if artscore == 0:
        show positx sitexp9 with dissolve
        play sound "audio/soundFX/Dun.wav" volume 0.5
        with hpunch
        window show

        emelie " What the he-"
        emelie "..."
        show positx sitexp9b with dissolve
        emelie " Hahaha!"
        "Emelie laughs."
        show positx surprise with dissolve
        emelie " That's really really good!! But crazy!"


    show positx sitexp6 with dissolve
    #EyeComment------------------
    if arteye == "small":
        emelie " Look at those beady little eyes!"

    if arteye == "big":
        emelie "Such big sparkly eyes! "
        emelie "They look like mine on a good day!"

    if arteye == "tired":
        emelie "I look so tired! "
        emelie "Those classes earlier must've taken their toll!"


    if arteye == "angry":
        emelie "I look pissed off! "
        emelie "Or maybe I'm just really focused on my posing!"


    if arteye == "wide":
        emelie " I can probably see my whole surroundings with those eyes, haha!"





    #MouthComment----------------
    if artmouth == "pout":
        emelie " And what juicy lips! "
        show positx sitexp2 with dissolve
        emelie "A bit big but maybe it's how you remember them from earlier today, hihi."

    if artmouth == "smile":
        emelie "And what a warm smile! Very cute!"

    if artmouth == "teeth":
        show positx sitexp9 with dissolve
        emelie "And you better watch out for those sharp teeth!"

    if artmouth == "small":
        emelie "And that's such a grumpy little mouth!"

    if artmouth == "snout":
        emelie "And what a nice snout with big strong tusks! "




    show positx surprise with dissolve
    #HeadComment---------------
    if arthead == "longer":
        emelie " All those features smacked on top of a really elongated head!"

    if arthead == "wide":
        emelie " All those features smacked onto an oddly wide head!"

    if arthead == "normal":
        emelie "All those features placed right in my round face!"

    if arthead == "heroic":
        emelie " All those features smacked onto a nice chiseled face!"
        emelie "What a jaw-line!"

    if arthead == "fluffy":
        emelie " All those features smacked onto a nice fur-covered face!"





    show positx sitexp7 with dissolve
    #BodComment--------------
    if artbody == "muscly":
        emelie " I kinda like those muscles! I should start exercising."

    if artbody == "droopy":
        emelie " I'm not sure how I feel about that saggy mid-section, haha."

    if artbody == "curvy":
        emelie " I've got some nice curves, too!"

    if artbody == "slim":
        emelie " I lost some weight since last I checked...Or you slimmed me down!"

    if artbody == "wide":
        emelie " I must've had a few too many pancakes earlier! That's a very round belly, haha!"


    show positx surprise2 with dissolve

    #LegComment------------
    if artlegs == "beastly":
        emelie " And finally, those feet sure look... long! "
        show positx sitexp8 with dissolve
        emelie "Is that how you humans see our pig legs?"

    if artlegs == "calves":
        emelie " And finally, those legs sure look muscular!"
        show positx sitexp8 with dissolve
        emelie " Must be all those stairs!"

    if artlegs == "normal":
        emelie " And finally, those nice legs!"
        show positx sitexp8 with dissolve
        emelie " Nice and soft!"


    if artlegs == "bulgey":
        emelie " And finally, those legs...."
        show positx sitexp8 with dissolve
        emelie " I know my clothes get tight sometimes but does my chub really squeeze out like that?"

    if artlegs == "skinny":
        emelie " And finally, those legs sure look..."
        show positx sitexp8 with dissolve
        emelie " Y'know I don't think I could walk with those!"





    #She comments on each of your choices.

label afterpaint:
    show positx sitexp9b with dissolve
    "She laughs."
    show positx sitexp5 with dissolve
    emelie " Great work!"
    hide canvasshow with easeoutbottom
    " I put the canvas down."
    show positx sitexp4 with dissolve
    emelie " All in all I feel like you've improved immensely! "
    emelie " If you ever need to make a descriptive drawing again I'm sure you'll do a fantastic job!"
    me " I hope so!"
label gallerysex:


    show positbed
    show positx sitgrin with dissolve
    play music "audio/Em_theme.mp3" fadein 0.1 volume 0.3 if_changed

    if playnormal == False:
        window hide
        menu:
            with dissolve
            "I fingered Emelie's butt in the bath.":
                $ buttprod = True
                $ buttprodsuccess = True
                window show
            "I fingered Emelie's pussy in the bath.":

                window show
    emelie " Now... I want to try a different pose!"
    window hide

    play sound "audio/soundFX/Blanket Move.wav"
    hide positx
    hide positxbrow up
    show posit doggy
    with dissolve
    pause 0.5
    window show
    "She gets on all fours."

    emelie " I hope I can hold this one... "

    window hide
    show canvaspaint at center:
        yoffset 850
    with easeinbottom
    pause 0.5
    window show
    " I grab a new canvas and get ready to paint her in the new pose!"
    window hide
    show positx doggymoan with dissolve
    pause 0.5
    window show
    emelie "Sometimes you get really tired when posing!"
    emelie " Especially when supporting your own weight like this..."
    " Her expression looks a little strained."
#Then she wants to pose again, but quickly falls.

    emelie " A-Ahh!"
    " She moans out!"
    window hide
    stop music fadeout 2.0
    play sound "audio/soundFX/Sit Pillow.wav"
    show posit fallen
    show positx fallmoan
    with dissolve
    with vpunch
    pause 0.5
    hide canvaspaint
    with easeoutbottom
    window show
    play music "audio/birds.wav" fadein 0.1 volume 0.1
    "She fell in just a second or two!"
    me " Are you okay??"
    hide positx with dissolve
    emelie " Ahhn~"
    me " It sounds like you're in pain!"
    show positx fallsidemoan with dissolve
    emelie " N-no I..."
    me "That must've been a REALLY demanding pose!"
    " I approach her."
    hide positx with dissolve
    with vpunch
    emelie " Ahh!"
    emelie " I'm... not in pain!"
    window hide
    jump plugsex

label drinks:
    window hide
    scene bg lineeveryone
    show blackshake at truecenter zorder -100
    show bglineall behind bg
    show bggranny
    show bgvic v1

    with fade
    hide bglineall
    pause 0.8
    play sound "audio/soundFX/FX2/water-swimming-4.mp3" volume 0.7
    show emline base
    show emlineface smile
    if modest == True:
        show emlinebluekini

    with dissolve
    pause 0.2
    with hpunch
    show emline out
    show emlineout
    show emlineface surprise
    with dissolve
    pause 0.3
    window show

    # Long line
    emelie "Whaaa!"
    emelie"This line is so long!"
    show emline base
    show emlineface pout
    with dissolve
    emelie "We're all the way out in the water..."
    me "Yeah! Seems a lot of people had the same craving."
    me "Guess we'll just have to wait..."
    show emlineface tense
    show emlineye sidee
    hide emlineout

    with dissolve
    "Emelie still looks tense from the action before."
    "The line moves a bit upfront. "
    window hide
    pause 0.2
    hide bgvic v1
    show bgvicv2
    with dissolve
    pause 0.6
    window show
    "Huh... Is that Victoria?"
    "It is! "
    window hide
    show bgvicaltv1 with dissolve
    pause 0.3
    window show
    "She spots me from the very front and waves! "
    window hide
    pause 0.2
    show bgvicalt v2 with dissolve
    pause 0.4
    window show
    "She points to the counter with a questioning look. "
    show emlineface smile
    hide emlineye sidee
    with dissolve
    emelie "'You recognize someone up front?"
    me "Yes! Victoria!"
    show emline think
    show emlineface ooo
    show emlineout
    with dissolve
    emelie "Ooo! Signal her to buy something for us!"
    window hide
    show linefingers with dissolve
    show linefingersshadow behind linefingers with dissolve
    pause 0.4
    window show
    "I raise two fingers in her direction!"
    window hide
    play sound "audio/soundFX/FX2/correct.mp3" volume 0.4
    show bgvicalt v3 with dissolve
    pause 0.5
    window show
    "She gives me a thumbs-up!"
    window hide
    hide linefingersshadow with dissolve
    hide linefingers with dissolve
    pause 0.4
    show bgvicv2bc
    hide bgvicalt
    with dissolve
    window show
    me "I think she's ordering something!"
    show emline base with dissolve
    show emlineye sidee
    show emlineface smile
    hide emlineout
    with dissolve
    emelie "Awesome!!"
    window hide

    hide bgvicalt
    hide bgvicaltv1
    hide bgvicv2
    hide bgvicv2bc
    show bgvicv2b
    hide bgvic
    with dissolve
    pause 0.3
    play sound "audio/soundFX/FX2/water-slosh-spashing-3.wav" volume 0.5
    show vicsuit wineholdz:
        zoom 0.90 xalign 1.35 yalign 1.05
    show vic lash:
        zoom 0.90 xalign 1.35 yalign 1.05
    with dissolve
    pause 0.3
    show emlineye vic with dissolve
    #show bglinesmokevic behind vicsuit with dissolve

    window show
    vic "Here's your booze!"
    window hide
    with hpunch
    pause 0.3
    show viceye lookback:
        zoom 0.90 xalign 1.35 yalign 1.05
    show vic wide
    with dissolve

    window show
    vic "Oh hey, Emelie! Didn't see ya back there!"
    show emlineface laugh
    with dissolve
    emelie "Heya, Victoria! "
    show emlineface ooo with dissolve
    emelie "Yeah, we're waaay back here."
    me "Thanks for buying for us! "
    show vic laugh
    hide viceye
    with dissolve
    vic "My pleasure!"
    hide emlineout
    show emlineface tense
    with dissolve
    emelie "I didn't wanna stay in this long line! Especially when all tense like this!"
    show vic sad
    show viceye lookback:
        zoom 0.90 xalign 1.35 yalign 1.05
    with dissolve
    vic "Aw, what making you so tense, dear?"
    show emline out
    show emlineface surprise
    with dissolve
    emelie "We were checking out the Pig Pit and I got scared! "
    show emlineout
    show emlineface tense
    with dissolve
    emelie "I didn't want to see Rolf get hurt while fighting! "
    window hide
    play sound "audio/soundFX/Dun.wav" volume 0.5
    with hpunch
    show vic surprise with dissolve
    window show

    vic "Rolf had a fight?!"
    show emline base
    show emlineface pout
    hide emlineout
    with dissolve
    emelie "Yeah! And now I need a relaxing place with some drinks to calm down!"
    #Or ' There was a big verbal fight and things got unpleasant back by the fighting pits!"
    hide vic with dissolve
    vic "My stuff's at a nice and secluded spot! "
    show vic smile :
        zoom 0.90 xalign 1.35 yalign 1.05
    hide viceye
    with dissolve
    vic "I'd love for you two to tag along and tell me all about it!"
    me "S-Sounds good!"
    show emlineface laugh
    show emlineout
    with dissolve
    emelie "Great! Lead the way!"
    window hide
    scene black with dissolve
    show blackshake at truecenter zorder -100
    "Me and Emelie both follow Victoria's lead up a path to a nearby hill."
    window hide
    scene bg drinkspot with fade
    show blackshake at truecenter zorder -100
    pause 0.5
    play sound "audio/soundFX/run2.wav" volume 0.8
    show emeswim normal at center:
        yalign -0.15 xalign 0.46 zoom 0.95
    with easeinright
    play sound "audio/soundFX/runn.wav" volume 0.8
    show vicsuit wineholdz  at right:
        ypos 1150 xpos 2020  zoom 1.0
    show vic lash at right:
        ypos 1150 xpos 2020  zoom 1.0
    with easeinright
    pause 0.4
    show emf bigsmile at center:
        yalign -0.15 xalign 0.46 zoom 0.95
    show emeye right2 at center:
        yalign -0.15 xalign 0.46 zoom 0.95
    with dissolve
    window show






    # Find spot up the hill
    emelie "This really is a nice and calm spot!"
    show vic closed at right:
        ypos 1150 xpos 2020  zoom 1.0
    with dissolve
    vic "I know!"
    show vic wide at right:
        ypos 1150 xpos 2020  zoom 1.0
    with dissolve
    vic "So- I bought ya some drastically different stuff!"
    hide vic
    show viceye lookem at right:
        ypos 1150 xpos 2020  zoom 1.0
    with dissolve
    vic "Some orange cider and rum! ... The strong stuff."
    show emf laugh
    hide emeye
    with dissolve
    emelie "Yess! That cider's my favorite!!"
    show vic closed behind viceye at right:
        ypos 1150 xpos 2020  zoom 1.0
    hide viceye
    with dissolve
    vic "Great! "
    show vic smile behind viceye at right:
        ypos 1150 xpos 2020  zoom 1.0
    with dissolve
    vic "The bottle of wine is for me, but we can all share!"
    vic "I tried buying polar opposites to maximize my chances of at least one drink being to your liking!"
    show emf bigsmile at center:
        yalign -0.15 xalign 0.46 zoom 0.95
    show emeye right2 at center:
        yalign -0.15 xalign 0.46 zoom 0.95
    show emeswim hips
    show emear high at center:
        yalign -0.15 xalign 0.46 zoom 0.95
    with dissolve
    emelie "Smart!"
    hide emeye
    show emf normalblush
    with dissolve
    me "I'm not very familiar with drinks like these, but I'm sure they're great!"
    me "I've only tried other farmers' cheap moonshine... "
    show vic closed at right:
        ypos 1150 xpos 2020  zoom 1.0
    with dissolve
    vic "Haha, I see!"
    show vic wide at right:
        ypos 1150 xpos 2020  zoom 1.0
    show emeye right2 at center:
        yalign -0.15 xalign 0.46 zoom 0.95
    with dissolve
    vic "Well, let's have a seat and I'll go over them for ya!"
    window hide
    hide emear
    hide emeswim
    hide emear
    hide emeye
    hide emf
    hide vic
    hide viceye
    hide vicsuit
    with dissolve
    play sound "audio/soundFX/move.wav" volume 0.9
    show bgdrinkspotbottle
    with dissolve
    pause 0.3


    show bgdrinkspotgals
    play sound "audio/soundFX/Sit Pillow.wav" volume 0.9
    if modest == True:
        show bgdrinkspotgalsblue
    with dissolve
    pause 0.1
    play sound "audio/soundFX/move2.wav" volume 1.0
    show bgdrinkspotdrinks
    with dissolve
    pause 0.3
    window show
    "Emelie and Victoria sit down and grab some glasses." # NEW FACES
    show bgdrinkspotgalsvic with dissolve
    vic "But first, tell me what happened with Rolf!"
    show bgdrinkspotgalsem with dissolve
    emelie "Okay, so when we first got there-"
    "Emelie starts explaining what went down in the Pig Pit."
    window hide

    scene black with fade
    show blackshake at truecenter zorder -100
    window show
    "I get comfortable on the blanket with the girls pouring up some drinks."
    play sound "audio/soundFX/Blanket Move.wav" volume 1.0
    window hide
    pause 0.1
    scene sitdrinkbase
    show blackshake at truecenter zorder -100
    show sitdrinkfeet
    show sitdrinkemlow
    show sitdrinkwine
    show sitdrinkviceeh
    show sitdrinkem waa
    show sitdrinkeardown
    if modest == True:
        show sitdrinkblue base

    with fade
    pause 0.8
    window show
    vic "Sheesh, the bull's teeth went flying all over from a single punch?"
    emelie "Y-Yeah!"
    vic "Ouch, that must've been painful! "
    show sitdrinkviceeh2 with dissolve
    vic "Though it's a little difficult for me to relate... having no teeth myself-"
    show sitdrinkem oh
    hide sitdrinkeardown
    with dissolve
    emelie "Oh, right!"
    show sitdrinkbasevic3
    hide sitdrinkwine
    hide sitdrinkviceeh2
    hide sitdrinkviceeh
    show sitdrinkvicclose behind sitdrinkbasevic3
    show sitdrinkbasevic2 behind sitdrinkbasevic3

    with dissolve
    vic "But you don't need teeth to drink!"
    hide sitdrinkem
    show sitdrinkbod drink
    with dissolve
    emelie "True!"
    vic "So-"
    show sitdrinkem smilu
    hide sitdrinkvicclose
    show sitdrinklookusvic
    with dissolve
label drinksstart:
    if playnormal == False:

        menu:
            with dissolve
            "Emelie is wearing her Blue Swimsuit!":
                $ modest = True
                scene sitdrinkbase# This crazy string is just me adding all the previous expressions after eachother
                show blackshake at truecenter zorder -100
                show sitdrinkfeet
                show sitdrinkemlow
                show sitdrinkwine
                show sitdrinkviceeh
                show sitdrinkem waa
                show sitdrinkeardown
                if modest == True:
                    show sitdrinkblue base
                show sitdrinkviceeh2
                show sitdrinkem oh
                hide sitdrinkeardown
                show sitdrinkbasevic3
                hide sitdrinkwine
                hide sitdrinkviceeh2
                hide sitdrinkviceeh
                show sitdrinkvicclose behind sitdrinkbasevic3
                show sitdrinkbasevic2 behind sitdrinkbasevic3
                hide sitdrinkem
                show sitdrinkbod drink
                show sitdrinkem smilu
                hide sitdrinkvicclose
                show sitdrinklookusvic
                with fade
                play music "audio/Tavern+Brawl+-+320bit.mp3" fadein 3.0 volume 0.2
                window show

            "Emelie is wearing her Melon Bikini!":
                $ modest = False
                scene sitdrinkbase
                show blackshake at truecenter zorder -100
                show sitdrinkfeet
                show sitdrinkemlow
                show sitdrinkwine
                show sitdrinkviceeh
                show sitdrinkem waa
                show sitdrinkeardown
                show sitdrinkviceeh2
                show sitdrinkem oh
                hide sitdrinkeardown
                show sitdrinkbasevic3
                hide sitdrinkwine
                hide sitdrinkviceeh2
                hide sitdrinkviceeh
                show sitdrinkvicclose behind sitdrinkbasevic3
                show sitdrinkbasevic2 behind sitdrinkbasevic3
                hide sitdrinkem
                show sitdrinkbod drink
                show sitdrinkem smilu
                hide sitdrinkvicclose
                show sitdrinklookusvic
                with fade
                play music "audio/Tavern+Brawl+-+320bit.mp3" fadein 3.0 volume 0.2
                window show

    vic "Time to pour something for you, [Protagonist]!"
    vic "I'll go over the bottles, and you just pick what sounds the most interesting!"
    hide sitdrinkbasevic3
    show sitdrinkwine
    hide sitdrinkbasevic2
    show sitdrinkbasevic1
    with dissolve
    vic "First off we haaave-"
    window hide
    hide sitdrinkbod drink with dissolve
    show sitdrinbottle wine
    show sitdrinkeardown
    with dissolve
    pause 0.3
    window show
    "Emelie picks up one of the bottles and shows it to me- "

    window hide
    show bottledarken with dissolve
    show middlebottle with dissolve
    pause 0.8
    window show
    emelie "The Hog Haven classic!"
    vic "\"S-Plus Wine\"!"
    emelie "Wha- "
    emelie "I always thought it was \"Swine\"!"
    vic "O-Oh, you're probably right!"
    vic "Made out of premium quality grapes from just outside of Hog Haven!"
    me "Oooh, interesting! "
    "I know some grape fields really close to my farm!"
    window hide
    hide middlebottle with dissolve
    hide bottledarken with dissolve
    pause 0.3
    hide sitdrinbottle
    show sitdrinkem poutu
    with dissolve
    pause 0.3
    window show
    emelie "I hear they stomp on the grapes to squeeze the juices out of them to make wine! Is that true?"
    me "I've heard that too, but I've never seen it."
    show sitdrinkem laugh
    show sitdrinkbod drink
    with dissolve
    emelie "If you stomped on grapes with those strange little \" toes\" you'd get half the yield stuck in between 'em!"
    me "Ha-ha, very funny. "
    me"... But you've got a point."
    show sitdrinkvicclose
    hide sitdrinkwine
    show sitdrinkbasevic3
    show sitdrinkbasevic2 behind sitdrinkbasevic3
    with dissolve
    vic "I'm not actually sure how grapes are pressed these days! New methods are always being developed for these things."
    vic "But maybe feet add to the flavor. Phuk-huk-hukaa!"
    "We all chuckle and the girls drink some more."
    window hide
    hide sitdrinkbod drink with dissolve
    hide sitdrinkvicclose
    show sitdrinkwine
    hide sitdrinkbasevic3
    hide sitdrinkbasevic2 behind sitdrinkbasevic3
    show sitdrinkem smilu
    with dissolve
    show sitdrinbottle cider with dissolve
    window show
    vic "Next up, we haave-"
    window hide
    pause 0.3


    show bottledarken with dissolve
    show middlebottle with dissolve
    pause 0.3
    show rightbottle with dissolve
    pause 0.8
    window show
    vic "\" Cloud City Cider\"! "
    emelie "I love this one!"
    vic  "It's very sweet, and made from oranges!"
    "I've tried oranges a few times, but they're really hard to grow in the climate around Hog Haven."
    me "I've only ever tried apple and pear cider before!"
    vic "I see! "
    window hide
    hide middlebottle
    hide rightbottle
    with dissolve
    hide bottledarken
    with dissolve
    hide sitdrinbottle with dissolve
    pause 0.3
    hide sitdrinkbasevic1
    show sitdrinkvicclose
    show sitdrinkbasevic4
    with dissolve
    window show
    vic "Oranges are a specialty of \"Cloud City\", and I've got family that lives there! "
    hide sitdrinkbasevic4
    hide sitdrinkvicclose
    with dissolve
    vic "The city gets its name from the architecture  being so vertical!"
    hide sitdrinklookusvic
    show sitdrinkbasevic3
    show sitdrinkem smile
    with dissolve
    vic "Imagine your room in the tower, Emelie... But even taller! "
    hide sitdrinkwine
    hide sitdrinkbasevic3
    hide sitdrinkbasevic4
    show sitdrinkbasevic2
    with dissolve
    vic "Large structures built into giant trees, with rope bridges connecting them all!"
    hide sitdrinkeardown
    show sitdrinkem waa
    with dissolve

    emelie "Waaa, sounds scary!"
    vic "Us avians tend to handle heights very well! "
    show sitdrinkem pout with dissolve
    emelie "I even get vertigo from looking out of my tower sometimes... "
    show sitdrinkeardown
    show sitdrinkem poutu
    show sitdrinkbod drink
    with dissolve
    emelie "I'm glad I'm so short, it makes it less scary to look down the edge of the balcony knowing I won't accidentally fall off!"
    show sitdrinkvicclose behind sitdrinkbasevic2 with dissolve
    vic "Haha, that's a good point!"
    hide sitdrinkvicclose
    hide sitdrinkbasevic2
    show sitdrinklookusvic
    show sitdrinkwine
    with dissolve
    vic "[Protagonist], are you afraid of heights?"

    window hide

    menu:
        with dissolve

        "I handle heights well!":
            window show
            me "I handle heights well!"
            hide sitdrinklookusvic
            hide sitdrinkbod drink
            show sitdrinkem waau
            with dissolve
            emelie "Must be a tall-person thing to handle heights well..."
            show sitdrinkem waryu with dissolve
            emelie "I'm so close to the ground all day that when I finally get a few meters up, I panic!"
            show sitdrinkvicclose with dissolve
            vic "Haha, maybe you're on to something!"

        "I'm terrified of heights!":
            window show
            me "I'm terrified of heights!"
            hide sitdrinklookusvic
            hide sitdrinkbod drink
            show sitdrinkem waau
            with dissolve
            emelie "Really? You, too? "
            show sitdrinkem smilu2 with dissolve
            emelie "What kinda heights have you experienced?"
            me "I climbed a really tall tree, once!"
            me "Took maybe two or three minutes to climb up, then what felt like two hours to climb back down!"
            show sitdrinkem laugh with dissolve
            emelie "Haha, 'sounds like something I'd do!"
            show sitdrinkviceeh2 with dissolve
            vic "Poor thing!"
    show sitdrinklookusvic
    hide sitdrinkvicclose
    hide sitdrinkviceeh2
    show sitdrinkbasevic1
    show sitdrinkem smile
    with dissolve
    vic "The place where our last bottle comes from might be more up your alley if you're afraid of heights!"
    show  sitdrinbottle rum
    show sitdrinkem smilu
    with dissolve
    emelie "!"
    window hide
    show bottledarken with dissolve
    show middlebottle
    show rightbottle
    with dissolve
    pause 0.3
    show leftbottle with dissolve
    pause 1.0
    window show
    vic "\"Reptilia Rum\" !"
    vic "From the great underground city of \"Reptilia\"! "
    emelie "I tried this one once... Not for me!"
    emelie "First and last time I'm ever having rum!"
    vic "It's a LOT of alcohol for the price- but you can hardly call it \"rum\"..."
    vic "The cold-blooded denizens of Reptilia love the stuff."
    emelie "But don't some of them also have poisonous fangs?... Maybe they're just desensitized to the taste-"
    vic "Haha, that'd explain it!"
    window hide

    hide middlebottle
    hide rightbottle
    hide leftbottle
    with dissolve
    hide bottledarken with dissolve
    pause 0.3
    hide sitdrinbottle with dissolve
    window show
    me "It's poisonous?!"
    show sitdrinkviceeh3
    with dissolve
    vic "You can get alcohol poisoning from any booze if you drink too much... So remember to drink in moderation!"
    hide sitdrinkviceeh3
    hide sitdrinkbasevic1
    hide sitdrinkwine
    show sitdrinkbasevic3
    show sitdrinkbasevic2 behind sitdrinkbasevic3
    with dissolve
    vic "The rum's perfectly safe and high quality, it's just incredibly strong and doesn't taste anything like rum!"
    show sitdrinkem smilu2
    hide sitdrinkeardown
    with dissolve
    emelie "So,[Protagonist]... Which one are you the most interested in trying?"

    #Pick Drink Here

    window hide
    show wines behind sitdrinkbase
    show bottledarken with dissolve

    show middlebottle
    show rightbottle
    show leftbottle
    with dissolve
    pause 0.2
    window show
    "Hmm, what should I pick? "
    window hide



    hide wines
    show vignette behind bottledarken with dissolve
    hide middlebottle
    hide rightbottle
    hide leftbottle

    show screen drinkchoice
    $ disableAFMbutton = True
    $ preferences.afm_enable = False
    $ _skipping = False
    $ renpy.pause(hard=True)


    $ drink = "none"


screen drinkchoice:
    #add "gui/choices/RolfInterrogationUI.png"

    imagebutton:
        style "mainmenunew"
        idle "images/Chapter6/2Wine/leftbottle.png"
        hover "images/Chapter6/2Wine/leftbottleselect.png"
        action Show(screen="ConfirmChoices", YesAction=Jump("ifrum"), Choice="drinkleft", NoAction=Show(screen="drinkchoice"), transition=dissolve)

    imagebutton:
        style "mainmenunew"
        idle "images/Chapter6/2Wine/middlebottle.png"
        hover "images/Chapter6/2Wine/middlebottleselect.png"
        action Show(screen="ConfirmChoices", YesAction=Jump("ifwine"), Choice="drinkmiddle", NoAction=Show(screen="drinkchoice"), transition=dissolve)

    imagebutton:
        style "mainmenunew"
        idle "images/Chapter6/2Wine/rightbottle.png"
        hover  "images/Chapter6/2Wine/rightbottleselect.png"
        action Show(screen="ConfirmChoices", YesAction=Jump("ifcider"), Choice="drinkright", NoAction=Show(screen="drinkchoice"), transition=dissolve)

screen ChoicedrinkleftDark:
    add "images/Chapter6/2Wine/leftpick.png"

screen ChoicedrinkmiddleDark:
    add "images/Chapter6/2Wine/middlepick.png"

screen ChoicedrinkrightDark:
    add "images/Chapter6/2Wine/rightpick.png"





label ifwine:
    $ disableAFMbutton = False
    $ _skipping = True
    $ drink = "wine"
    hide screen drinkchoice
    hide screen ChoicedrinkleftDark
    hide screen ChoicedrinkmiddleDark
    hide screen ChoicedrinkrightDark
    hide vignette
    with dissolve
    hide bottledarken
    with dissolve
    play sound "audio/soundFX/FX6/glassound.wav" volume 0.6
    show sitdrink glass with dissolve
    window show
    me "I'll try some of the wine!"
    show sitdrinkvicclose behind sitdrinkbasevic2 with dissolve
    vic "Great choice!"

    "I've never grown grapes myself, but I'm curious what the finished product from my fellow farmers tastes like!"
    window hide

    show sitdrinbottle wine behind sitdrink with dissolve
    play sound "audio/soundFX/FX6/575734__lexyismarchhare__sipsh.wav" volume 0.6
    show sitdrink glass2
    with dissolve
    window show
    emelie "Theere ya go!"
    me "Thank you!"
    emelie "Hope you like Hog Haven wine!"
    hide sitdrinbottle with dissolve




    jump afterdrinkchoice

label ifcider:
    $ disableAFMbutton = False
    $ _skipping = True
    $ drink = "cider"
    hide screen drinkchoice
    hide screen ChoicedrinkleftDark
    hide screen ChoicedrinkmiddleDark
    hide screen ChoicedrinkrightDark
    hide vignette
    with dissolve
    hide bottledarken
    with dissolve

    play sound "audio/soundFX/FX6/glassound.wav" volume 0.6
    show sitdrink glass with dissolve

    window show
    me "I'll have some of the cider!"
    emelie "Great choice! "
    window hide

    show sitdrinbottle cider behind sitdrink with dissolve
    play sound "audio/soundFX/FX6/575734__lexyismarchhare__sipsh.wav" volume 0.6
    show sitdrink glass3
    with dissolve
    show sitdrinkorange far with dissolve
    window show
    emelie "There ya go!"
    me "Thank you!"
    emelie "Hope you like it just as much as I do!"
    hide sitdrinbottle with dissolve



    jump afterdrinkchoice


label ifrum:
    $ disableAFMbutton = False
    $ _skipping = True
    $ drink = "rum"
    hide screen drinkchoice
    hide screen ChoicedrinkleftDark
    hide screen ChoicedrinkmiddleDark
    hide screen ChoicedrinkrightDark
    hide vignette
    with dissolve
    hide bottledarken
    with dissolve
    play sound "audio/soundFX/FX6/glassound.wav" volume 0.6
    show sitdrink glass with dissolve
    window show
    me "I want the rum!"
    with hpunch
    show sitdrinkem waau with dissolve
    emelie "Waaaa-"
    vic "Brave!"
    window hide

    show sitdrinbottle rum behind sitdrink with dissolve
    play sound "audio/soundFX/FX6/575734__lexyismarchhare__sipsh.wav" volume 0.6
    show sitdrink glass1
    with dissolve
    show sitdrinkem poutu with dissolve
    window show
    emelie "E-Enjoy your poison!"
    me "Thank you, I will!"
    hide sitdrinbottle with dissolve



    jump afterdrinkchoice


label afterdrinkchoice:

    if drink == "rum":
        window hide
        show sitdrink glassup1 with dissolve
        pause 0.7
        window show
        "I take a small sip of the \"rum\"..."
        play sound "audio/soundFX/FX6/575734__lexyismarchhare__siploud.wav" volume 1.0
        with vpunch
        me "EUGHK-"
        "I instinctively swallow the moment the liquid hits my tongue, and I feel the alcohol burn all the way down into my stomach."
        show sitdrinkem waau with dissolve
        emelie "'Told ya! It's so bad!"
        show sitdrinkviceehu
        hide sitdrinkbasevic3
        hide sitdrinkbasevic2
        with dissolve
        vic "Aw, you don't like it either? "
        "Victoria bought this for me... So I'd feel bad complaining about it!"
        me "N-No, it's good!"
        "I force a smile."
        hide sitdrinkviceehu
        show sitdrinkvicclose
        show sitdrinkbasevic2 behind sitdrinkbasevic3
        show sitdrinkbasevic3
        with dissolve
        vic "Puh!"
        show sitdrinkeardown
        show sitdrinkem macho
        with dissolve
        emelie "Tsk... Macho tough guy~"
        me "I sure am!"
        show sitdrinkem laugh2
        show sitdrinkbod drink behind sitdrink
        with dissolve
        emelie "Haha!"
        "We laugh and keep drinking."
        show sitdrink glass1
        with dissolve
    if drink == "wine":
        window hide
        show sitdrink glassup2 with dissolve
        pause 0.7
        window show
        "I take a small sip of the wine..."
        play sound "audio/soundFX/FX6/575734__lexyismarchhare__siploud.wav" volume 1.0
        with hpunch
        me "Mmhn!"
        "The taste is really complex and rich! And even if aged, it somehow has an underlying smell of freshly plucked grapes!"
        hide sitdrinkvicclose with dissolve
        vic "Good, right?!"
        me "Yeah, I like it a lot!"
        vic "You've got classy taste, like me!"
        show sitdrinkem pout with dissolve
        emelie "H-Hey, now..."
        show sitdrinkviceeh behind sitdrinkbasevic2
        hide sitdrinkbasevic3
        hide sitdrinkbasevic2
        with dissolve
        vic "!- "
        show sitdrinkviceeh2 behind sitdrinkbasevic2 with dissolve
        vic "You've got classy taste, too, Emelie! "
        hide sitdrinkviceeh
        hide sitdrinkviceeh2
        show sitdrinkbasevic1b behind sitdrinkbasevic2
        with dissolve
        vic "That's high-brow cider from Cloud City!"
        show sitdrinkbod drink behind sitdrink
        show sitdrinkem oh
        with dissolve
        emelie "... I think I just like it because it doesn't taste anything like alcohol..."
        show sitdrinkvicclose behind sitdrinkbasevic2
        hide sitdrinkbasevic1b
        show sitdrinkem laugh2
        show sitdrinkbasevic3
        show sitdrinkbasevic2
        with dissolve
        "We laugh and keep drinking."

        show sitdrink glass2
        with dissolve
    if drink == "cider":
        window hide
        show sitdrink glassup3
        show sitdrinkorange close
        with dissolve
        pause 0.7
        window show
        "I take a small sip of the cider."
        play sound "audio/soundFX/FX6/575734__lexyismarchhare__siploud.wav" volume 1.0
        with hpunch
        me "Mnnnniii-"
        "It's nice and sweet, but the surprising sourness makes me grimace!"
        emelie " It hits you pretty hard, I know!"
        show sitdrinkviceeh2
        hide sitdrinkbasevic3
        hide sitdrinkbasevic2
        with dissolve
        vic "Really? It isn't very strong."
        show sitdrinkem smile
        show sitdrinkeardown
        with dissolve
        emelie "The taste, I mean! "
        me "Yeah. It's like a big fistful of sugar and sourness!"
        show sitdrinkbod drink behind sitdrink
        show sitdrinkem laugh2
        with dissolve
        emelie "Haha, I love it!"
        show sitdrinkem poutu with dissolve
        emelie "Maybe because it hides the taste of alcohol..."

        show sitdrinkem laugh3

        show sitdrinkbasevic2
        show sitdrinkbasevic3
        show sitdrinkvicclose behind sitdrinkbasevic2
        with dissolve
        show sitdrink glass3
        show sitdrinkorange far
        with dissolve

        "We laugh and keep drinking."
    show sitdrinkem base
    hide sitdrinkeardown
    with dissolve
    emelie "This spot's really is nice and distant from everyone else, Victoria!"
    show sitdrinkem smile
    hide sitdrinkbod drink
    show sitdrinkeardown
    with dissolve
    emelie "I feel much calmer now!"
    show sitdrinkwine
    hide sitdrinkvicclose
    hide sitdrinkbasevic3
    hide sitdrinkbasevic2
    show sitdrinkcoy

    with dissolve
    vic "Oh, good!"
    show sitdrinkviceeh2
    hide sitdrinkcoy
    with dissolve
    vic "I thought the beach was pretty crowded, too!"
    vic "I enjoy having people around, but I prefer smaller, more quiet gatherings."
    show sitdrinkviceeh4
    show sitdrinkbasevic5
    with dissolve
    vic "Maybe it's because I've spent so much quiet time in the library..."
    me "It's fun to have you join us!"
    me "Are you not working today?"
    show sitdrinkviceeh3 behind sitdrinkbasevic5  with dissolve
    vic "I'd normally be working, but I didn't have a single customer today."
    hide sitdrinkbasevic5
    show sitdrinkbasevic1
    with dissolve
    vic "Business is usually slow on warm summer days, but today was completely empty! "
    vic "So I went and checked in with Maple, but she had the opposite problem! "
    hide sitdrinkbasevic1
    hide sitdrinkviceeh4
    hide sitdrinkviceeh2
    hide sitdrinkviceeh3
    hide sitdrinkbasevic5
    with dissolve
    vic "Apparently, her entire stock of beach-wear sold out!"
    me "Oh? I was there earlier and there were barely any items left! 'Lucky I got there when I did!"
    vic "Yeah! She told me it was due to this beach gathering, so I figured I might as well check it out myself!"
    show sitdrinkbod drink behind sitdrink
    hide sitdrinkeardown
    show sitdrinkem oh
    with dissolve
    emelie "Ohoo, I see!"
    hide sitdrinkem
    with dissolve
    emelie "What've you been up to so far?"
    hide sitdrinklookusvic with dissolve

    vic "Not much! When I got here I just set things up-"

    show sitdrinkbasevic5 behind sitdrink
    hide sitdrinkwine
    show sitdrinkvicclose behind sitdrinkbasevic5
    with dissolve
    vic "Then I took a stroll down the beach and ended up at the bar! "
    show sitdrinklookusvic
    hide sitdrinkvicclose
    with dissolve
    vic "A glass of wine with a good book is just the best!"
    "I catch myself not drinking nearly as much as the girls, so I bring my glass back to my lips and start sipping."
    if drink == "cider":
        show sitdrink glassup3
        show sitdrinkorange close
        with dissolve
        "It's really easy to gulp down, and as I drink more the sliiightest taste of alcohol just completely disappears."
        window hide
        play sound "audio/soundFX/FX6/575734__lexyismarchhare__siploud.wav" volume 1.0
        show sitdrink glassup with dissolve
        with vpunch
        pause 0.5
        window show
        "I feel a tiny bit tipsy as my glass empties... And the girls have been drinking this whole time!"

        show sitdrink glass
        show sitdrinkorange far
        with dissolve
        "I pour myself some more and snap my attention back to the girls."
        window hide
        play sound "audio/soundFX/FX6/575734__lexyismarchhare__sipsh.wav" volume 0.6
        show sitdrink glass3 with dissolve

    if drink == "wine":
        show sitdrink glassup2
        with dissolve
        "This wine is fairly strong, and Victoria is just downing it!"
        "It makes sense she'd be used to drinking if she does it while reading in her free time..."
        window hide
        play sound "audio/soundFX/FX6/575734__lexyismarchhare__siploud.wav" volume 1.0
        show sitdrink glassup with dissolve
        with vpunch
        pause 0.5
        window show
        "I feel a tiny bit tipsy as my glass empties... And the girls have been drinking this whole time!"
        show sitdrink glass with dissolve
        "I pour myself some more and snap my attention back to the girls."
        window hide
        play sound "audio/soundFX/FX6/575734__lexyismarchhare__sipsh.wav" volume 0.6
        show sitdrink glass2 with dissolve


    if drink == "rum":
        show sitdrink glassup1
        with dissolve
        with hpunch
        "ECH- It's horrible!"
        "But I'll power through so I'm not sitting here all stiff as a board!"
        window hide
        play sound "audio/soundFX/FX6/575734__lexyismarchhare__siploud.wav" volume 1.0
        show sitdrink glassup with dissolve
        with vpunch
        pause 0.5
        window show
        "I feel a bit tipsy as my glass empties... And the girls have been drinking this whole time!"
        show sitdrink glass with dissolve
        "I pour myself some more and snap my attention back to the girls."
        window hide
        play sound "audio/soundFX/FX6/575734__lexyismarchhare__sipsh.wav" volume 0.6
        show sitdrink glass1 with dissolve

    pause 0.3
    hide sitdrinkbod drink
    show sitdrinkeardown
    show sitdrinkem smile
    with dissolve
    window show
    emelie "So, what have you been reading?"
    hide  sitdrinkvicclose
    hide sitdrinklookusvic
    hide sitdrinkbasevic5
    show sitdrinkcoy2
    with dissolve
    show sitdrinkblushvic with dissolve
    vic "Just got through the middle of Humane Hunk..."
    hide sitdrinkem with dissolve
    emelie "A-Aah!"
    show sitdrinkem laugh2 with dissolve
    emelie "Me too!! It's REALLY difficult to put down!"
    hide sitdrinkcoy2 with dissolve
    vic "It sure is! And I'm glad at least one book is driving some sales this summer!"
    show sitdrinkem poutu2
    show sitdrinkbod drink behind sitdrink
    with dissolve
    emelie "I don't see any boys reading it though... "
    show sitdrinkbasevic5

    show sitdrinkcoy behind sitdrinkblushvic
    with dissolve
    vic "Oh, there are definitely some male fans!"
    show sitdrinklookusvic behind sitdrinkblushvic
    with dissolve
    vic "They sneak into the shop right before closing time, wearing disguises while asking what the new book releases are... "
    show  sitdrinkvicclose behind sitdrinkblushvic
    hide sitdrinklookusvic
    with dissolve
    vic "Then claim to have read all the other books, haha!"
    show sitdrinkem smilebu with dissolve
    emelie "Haha! Is that what you would do, [Protagonist]?"
    me "Hmm..."
    "When I got the buttplug from Bronwen, I DID try to talk around the subject... "
    "But Bronwen has a really scary aura. Maybe I'd feel different in a regular store if they sold naughty items?"

    window hide

    menu:
        with dissolve

        "If a store is selling something naughty, I don't think buying it is anything to be embarrassed about!":
            window show
            me "If a store is selling something naughty, I don't think buying it is anything to be embarrassed about!"
            hide sitdrinkvicclose
            show sitdrinklookusvic behind sitdrinkblushvic
            show sitdrinkbasevic1 behind sitdrinkblushvic
            with dissolve
            vic "Mhm!"
            show sitdrinkem poutu2
            hide sitdrinkbod drink
            with dissolve

            emelie "That thought makes sense... But I still feel sort of embarrassed!"



        "I'd be extremely embarassed to outright purchase something raunchy from a store!":
            window show
            me "I'd be extremely embarassed to outright purchase something raunchy from a store!"
            hide sitdrinkvicclose
            show sitdrinklookusvic behind sitdrinkblushvic
            show sitdrinkbasevic1 behind sitdrinkblushvic
            with dissolve
            vic "Really?"
            show sitdrinkem poutu2
            hide sitdrinkbod drink
            with dissolve
            emelie "Yeah, me too!"
            show sitdrinkem poutu
            with dissolve
            emelie "I'm lucky Rita sent me a copy!"

    hide sitdrinklookusvic
    hide sitdrinkbasevic1
    with dissolve

    vic "As a store owner, you get so used to seeing people buy those items that you stop thinking about it!"
    show sitdrinkem smileb
    show sitdrinkbod drink behind sitdrink
    with dissolve
    emelie "That's good to know!"

    show sitdrinkem smilebu
    with dissolve
    emelie "[Protagonist] seems kinda interested in Humane Hunk, too... "
    me "Pfff."
    me "M-maybe..."
    #
    hide sitdrinkbasevic5
    hide sitdrinkvicclose
    show sitdrinklookusvic behind sitdrinkblushvic
    with dissolve
    vic "That doesn't surprise me! He's a curious one, for sure~ "

    hide sitdrinkem
    show sitdrinkemblush
    hide sitdrinkbod
    with dissolve
    emelie "Haha! How so??"
    show sitdrinkbasevic4
    hide sitdrinklookusvic
    with dissolve
    vic "Well, he had a lot of questions about different species mating and things like that... "
    vic "And if the two of you have been spending time together... I can see why~ "
    with hpunch
    "!?... I think she's getting drunk!"
    show sitdrinkemblush2
    hide sitdrinkemblush
    show sitdrinkem eee behind sitdrinkemblush2
    show sitdrinkbod drink behind sitdrink
    with dissolve
    "Emelie raises an eyebrow."
    emelie " O-oh?"
    emelie "What kinda questions did he have? "

    if drink == "cider":
        show sitdrink glassup3
        show sitdrinkorange close
        with dissolve

    if drink == "wine":
        show sitdrink glassup2

        with dissolve

    if drink == "rum":
        show sitdrink glassup1

        with dissolve
    "I grumble a bit in embarrassment while sipping on my drink"

    hide sitdrinkbasevic4
    show sitdrinklookusvic behind sitdrinkblushvic
    show sitdrinkbasevic1 behind sitdrinkblushvic
    show sitdrinklookusvic bee behind sitdrinkblushvic

    with dissolve
    vic "Well, he must've missed a lot of anatomy lessons growing up! "
    hide sitdrinklookusvic
    hide sitdrinkbasevic1
    show sitdrinkvicclose behind sitdrinkblushvic
    with dissolve
    vic "For one, he thought I could fly! "

    show sitdrinkem laugh2
    hide sitdrinkeardown
    with dissolve
    emelie "Hahaha!"
    show sitdrinkem smile
    show sitdrinkeardown
    hide sitdrinkbod
    with dissolve
    emelie "That's funny. I bet you wish that was true!"
    vic "Absolutely!"
    play sound "audio/soundFX/FX6/575734__lexyismarchhare__siploud.wav" volume 1.0
    show sitdrink glassup with dissolve
    "I gulp the rest of my drink down."
    hide sitdrinkvicclose
    show sitdrinkbasevic5 behind sitdrink
    with dissolve
    vic "He didn't know avians could develop breasts either- "
    vic "So I gave him a big lesson all about it!"
    window hide
    with hpunch
    if drink == "cider":
        show sitdrink glass
        show sitdrinkorange far
        with dissolve

    if drink == "wine":
        show sitdrink glass

        with dissolve

    if drink == "rum":
        show sitdrink glass

        with dissolve
    play sound "audio/soundFX/FX3/water-spraying.wav" volume 0.52
    show sitdrinkspit
    with dissolve
    window show
    me "PFFT!"
    hide sitdrinkspit
    with dissolve
    "I spit out some of my drink- "
    "This conversation's getting a bit private!"
    show sitdrinkem smileb with dissolve
    emelie "Really? "
    show sitdrinkem pout with dissolve
    emelie "I don't know too much about avian anatomy, myself..."
    show sitdrinkem base
    hide sitdrinkeardown
    hide sitdrinkbod
    with dissolve
    emelie "Give me a quick lesson, too!"
    hide sitdrinklookusvic
    hide sitdrinkbasevic5
    with dissolve
    vic "Well, avian breast anatomy is nearly identical to porcine breast anatomy- "
    show sitdrinkvicclose behind sitdrinkblushvic
    with dissolve
    vic "So a busty girl like yourself will know the basics! "
    hide sitdrinkvicclose
    show sitdrinklookusvic behind sitdrinkblushvic
    with dissolve
    vic "I just gave [Protagonist] a quick explanation of the various parts of the breast-"
    show sitdrinkvicclose behind sitdrinkblushvic
    with dissolve
    vic "And let him touch them here and there-"
    window hide
    play sound "audio/soundFX/Dun.wav" volume 0.5
    with vpunch
    jump naughtydrinks

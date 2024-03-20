label findemelie:

    maple "Oh hey, [Protagonist]! "
    me "Hey, Maple! "
    show maps thinking
    show maf think:
        zoom 0.99 yoffset 11
    with dissolve
    maple "I-Is everything okay?"
    show maf think2 with dissolve
    maple "You smell kinda funky-"
    me "I... fell into the canal."
    "'Can't tell her I was thrown in or she'd start asking questions!"
    show maps cheerup
    show maf ech
    with dissolve
    maple "Ech, I did that too once!"
    maple "Tried walking over the bridge in a pair of stiletto high heels- "
    show maps tid
    show maf shy
    with dissolve
    maple "Big mistake!"
    me "\"Sdidetto\"?"
    show maps base
    show maf hapiface
    with dissolve
    maple "Never mind- It's a type of shoe!"
    me "Aha, you should show me sometime!"
    show maps out
    show maf hapigrin
    with dissolve
    maple "Will do!"
    show maps tid
    show maf fronty

    with dissolve
    maple "Anyways, I was just gonna check in on Bronnie."
    maple "I need her to craft some belt buckles and barbells for me! "
    show maps hips
    show maf grin
    with dissolve
    maple "'She home?"
    me "She's home alright..."
    "Probably freaking out and trying to act all-natural to her dad!"
    show maps cheerup
    show maf bigg
    with dissolve
    maple "Great!"
    #victoria shows up "
    window hide
    play sound "audio/soundFX/runn.wav" volume 0.7

    show vicuswim pull at center behind maps:
        zoom 0.98 yoffset 1 xoffset -5
    show vic scaru at center behind maps:
        zoom 0.98 yoffset 1 xoffset -5
    with easeinright

    pause 0.5
    window show
    vic "H-Hello, you two!"
    #shy
    show maps peacehigh
    show maf lookright
    with dissolve
    maple "Hiya, Vicky!"
    "Vicky? "
    "Maple's got a nickname for all her friends..."
    me "You two know each other?"
    show maps cheerup
    show maf openn
    with dissolve
    maple "Yes!"
    show vicuswim think
    show vic insecure
    with dissolve
    vic "We're both entrepreneurs  here in Hog Haven, so we like to compare notes on which days and times are the best for business!"
    me "Right, that's convenient!"
    show vicuswim out
    show vic lash
    with dissolve
    vic "Mhm!"
    show maps tiddown
    show maf shy
    with dissolve
    maple "...And she helps me with my taxes " #sweats
    show vicuswim back
    show vic smile
    show viceye sidee at center behind maps:
        zoom 0.98 yoffset 1 xoffset -5
    with dissolve
    vic "In return for some free tailoring on my clothes. "
    show vicuswim out
    show vic laugh
    hide viceye
    with dissolve
    vic "It's a great arrangement!"
    show maps hips
    show maf lookright
    with dissolve
    maple "'Sure is! "
    show maps thinking
    show maf think
    show mapeye down:
        zoom 0.99 yoffset 11
    with dissolve
    maple "Victoria has a hard time finding tops that fit her-"
    #camera shake
    show maps cheerup
    show maf happydown2
    hide mapeye
    with dissolve
    maple "Speaking of which-"
    "Maple looks at Victoria's chest."#maybe custom big eyes face
    window hide
    play sound "audio/soundFX/Dun.wav" volume 0.5
    with hpunch
    show maps blinded3
    show maf blinded
    with dissolve
    window show
    if modest == True:

        maple "Isn't that Emelie's swimsuit?"
    else:
        maple "Isn't that Emelie's bikini?"
    window hide
    with vpunch
    play sound "audio/soundFX/FX2/chicken2.wav" volume 0.3
    show vicuswim flap
    show vic surprise
    show viceye sidesurprise at center behind maps:
        zoom 0.98 yoffset 1 xoffset -5
    with dissolve
    window show
    vic "It is-"
    show vic sad
    show vicuswim out
    show viceye sidee at center behind maps:
        zoom 0.98 yoffset 1 xoffset -5
    with dissolve

    vic "Emelie wanted to try mine on since hers was a bit tight! "

    show vic scaru
    hide viceye
    with dissolve
    vic "So, I figured I might as well try it on since it looked cute on her..."
    show vicuswim pull
    show vic sad
    show vicblush at center behind maps:
        zoom 0.98 yoffset 1 xoffset -5
    with dissolve
    vic "But it's definitely too small!"
    window hide
    menu:
        with dissolve


        "I think it fits you amazingly!":
            window show
            me "I think it fits you amazingly!"
            show maps cheerup
            show maf frontystar
            with dissolve
            maple"[Protagonist]'s got an eye for fashion!"
            show maf lookright with dissolve
            maple "The fit is great! Very trendy!"
            show vicuswim out
            show vic surprise
            show viceye sidee at center behind maps:
                zoom 0.98 yoffset 1 xoffset -5
            hide vicblush
            with dissolve
            vic "I-If you say so..."
            show maps back
            show maf baseface
            show mapeye right:
                zoom 0.99 yoffset 11
            with dissolve
            maple "But you've gotta feel comfortable in what you wear, so if it makes you feel weird you should pick something else!"
            show vicuswim pull
            show vic insecure
            with dissolve
            vic "Yeaaaah, I don't think I'll hop on this trend in particular..."
            show maps hips
            show maf closeyes
            hide mapeye
            with dissolve
            maple "At least you gave it a shot, so now you know how it feels and looks on you!"
            show vicuswim out
            show vic lash
            with dissolve
            vic "Yeah!"
            show vicuswim flap
            hide viceye
            show vic insecure
            show vicblush at center behind maps:
                zoom 0.98 yoffset 1 xoffset -5
            with dissolve
            vic "But now I think I'll hurry on home before everyone comes running from the beach-"


        "Yeah, that must be uncomfortable.":
            window show
            me "Yeah, that must be uncomfortable."
            show vicuswim think
            show vic insecure
            hide vicblush
            with dissolve
            vic "It definitely is!"
            show maps back
            show maf insecure
            with dissolve
            maple "C'moon, you two! "
            show maf shiny
            show maps base
            with dissolve
            maple "A bit of discomfort is worth it if it makes you look fabulous!"
            show maps cheerup
            show maf wink
            show mapeye right:
                zoom 0.99 yoffset 11
            with dissolve
            maple "Doesn't that sexiness make you feel confident?"
            show vicuswim flap
            show vic scaru
            hide viceye
            show vicblush at center behind maps:
                zoom 0.98 yoffset 1 xoffset -5
            with dissolve
            vic "In this, I mostly feel self-conscious."
            show maps hips
            show maf shy
            hide mapeye
            with dissolve
            maple "Aw- "
            me "Well, at least you gave it a shot! "
            show maps out
            show maf shiny
            with dissolve
            maple "Exactly!"
            show maps base
            show maf frontystar
            with dissolve
            maple "Experimenting with new looks is super important if you want to dress to impress!"
            show vicuswim pull
            show vic insecure
            hide vicblush
            show viceye sidee at center behind maps:
                zoom 0.98 yoffset 1 xoffset -5
            with dissolve
            vic "That's true, but now I think I'll hurry on home before everyone comes running from the beach-"

    show maps thinking
    show maf think
    show mapeye right:
        zoom 0.99 yoffset 11
    with dissolve
    maple "Good thinking, and I should continue over to Bronnie!"
    show maps back
    show maf baseface
    hide mapeye
    with dissolve
    maple "Oh, and [Protagonist]... Come by again soon, 'kay? "
    show maps cheerup
    show maf sly
    with dissolve
    maple "And bring Emelie along!"
    me "I will!"
    me "Speaking of which... where is she?"
    show vicuswim out
    hide viceye
    hide vicblush
    show vic lash
    with dissolve
    vic "She said she was running off to the baths to wash the ocean salt off her body!"
    show vic bigsmile with dissolve
    vic "I think you'll find her there now if you hurry on over!"
    me "Aha, then I'll get a move on right away!"
    me "Have a good evening, you two!"
    show maps dubpeacehigh
    show maf closeyes
    with dissolve
    maple "Byebye, cutie~"
    show vicuswim back
    show vic laugh
    with dissolve
    vic "Have fun!"
    window hide
    stop music fadeout 4.0
    queue music  "audio/Birds.wav" fadein 3.0 volume 0.1
    show black with dissolve
    pause 0.2
    scene bg fountainsunset with fade
    show blackshake at truecenter zorder -100
    pause 0.5
    window show
    "I dash back to the fountain-"

    window hide
    scene bg corridorbath
    show blackshake at truecenter zorder -100
    show bathbusy
    with fade
    pause 0.5
    window show
    "Then hurry on to the baths."

    #i show up to baths"
    "Emelie is probably where we were last time!"
    "I should knock. "
    #knockknock
    window hide
    pause 0.2
    play sound "audio/soundFX/FX7/knock.wav" volume 0.3
    with hpunch
    with hpunch
    window show
    me "[Protagonist] here!"
    emelie "One second!"

label hairfoam:

    window hide
    pause 0.2
    play sound "audio/soundFX/OpenDoor 1.wav"
    show bathcorridoropensunset with dissolve
    window show
    emelie "Come on in!"
    window hide
    scene bg BathRoomEmpty
    show blackshake at truecenter zorder -100
    show roomtowel
    with fade
    play sound "audio/soundFX/FX2/lock-the-door-2.wav" volume 0.1
    window show
    "Emelie locks the door."
    window hide
    play music "audio/starting-out-waltz-vivace-by-kevin-macleod-from-filmmusic-io.mp3" fadein 0.1 volume 0.3
    play sound "audio/soundFX/runn.wav" volume 0.4
    show emshampoo a1 at right:
        yalign 0.08 xalign 0.6 zoom 1.07
    with easeinright

    pause 0.3
    show emshampoo a2 at right:
        yalign 0.08 xalign 0.6 zoom 1.07
    with dissolve
    window show

    emelie "Hey hey, sweetie! "
    window hide
    show emshampoo a2 at right:
        yalign 0.08 xalign 0.6 zoom 1.07
        linear 0.4 yalign 0.14 xalign 0.6 zoom 2.15
    pause 0.2
    show emeliehugkiss2 with dissolve
    play sound "audio/soundFX/FX3/kiss.wav"
    with hpunch
    pause 0.3
    window show
    "Emelie runs up and hits me with a quick kiss!"
    window hide
    show emshampoo a2 behind emeliehugkiss2 at right:
        yalign 0.14 xalign 0.6 zoom 2.15
        linear 0.4 yalign 0.08 xalign 0.6 zoom 1.07


    hide emeliehugkiss2
    with dissolve
    show emshampoo a2 at right:
        yalign 0.08 xalign 0.6 zoom 1.07


    show emshampoo a2 at right:
        yalign 0.08 xalign 0.6 zoom 1.07
        linear 0.4 zoom 1.00 yalign 0.06 xalign 0.9
    pause 0.5
    hide emshampoo
    show emvs base at right:
        yalign 0.06 xalign 0.9 zoom 1.00
    show emf bigsmile at right:
        yalign 0.06 xalign 0.9 zoom 1.00
    show emvsconditioner at right:
        yalign 0.06 xalign 0.9 zoom 1.00
    window show
    me "H-Hey there! "
    me "Woah, you look great in that swimsuit!"
    show emvs hips
    show emf biggersmile
    show emear highz at right:
        yalign 0.06 xalign 0.9 zoom 1.00
    with dissolve
    emelie "Thank you!"
    show emf normalblush with dissolve
    emelie "I'm really glad you got to see me in it-"
    show emvs out
    show emf laugh
    hide emear
    with dissolve
    emelie "'Cus I was going to take it off after washing all this shampoo out of my hair!"
    me "Sham...poo?"
    show emvs think
    show emf think
    hide emeye
    with dissolve
    emelie "Oh, uh... "
    show emeye scared at right:
        yalign 0.06 xalign 0.9 zoom 1.00
    with dissolve
    emelie "It's like soap but for your head!"
    me "Aha, I see."
    "Must be a pig thing..."
    hide emeye
    show emf normalblush
    show emvs base
    with dissolve
    emelie "So-"
    show emvs hips
    hide emeye
    show emf smile
    with dissolve
    emelie "I heard ya met up with Billy? "
    if drink == "cider":
        show emvs panic
        show emf surprise
        show emear highz at right:
            yalign 0.06 xalign 0.9 zoom 1.00
        with dissolve
        emelie "He ran up to me with a glass of water and said he drank some horrible drink made up of spoiled oranges!"
        me "Ahh, yeah! "
        me "He had a sip of your cider and wasn't a fan..."
        show emvs out with dissolve
        emelie "Whoops!"
        emelie "Well, at least he didn't drink anything stronger! "
        show emvs base with dissolve
        emelie "Puh, he's lucky"

    if drink == "wine":
        show emvs panic
        show emf surprise
        show emear highz at right:
            yalign 0.06 xalign 0.9 zoom 1.00
        with dissolve
        emelie "He up ran to me with a glass of water and said he drank some nasty grape juice or something!"
        me "Ahh, yeah! "
        me "He had a glass of wine and wasn't a fan..."

    if drink == "rum":
        show emvs panic
        show emf surprise
        show emear highz at right:
            yalign 0.06 xalign 0.9 zoom 1.00
        with dissolve
        emelie "He up ran to me in a panic, holding a glass of water and screaming about drinking poison or something!"
        me "O-Oh, yeah... "
        me "He had some really strong alcohol and didn't take it too well."
        show emvs out
        show emf surprise2
        with dissolve
        emelie "A-Aha! "
    show emvs hips
    show emf insecure
    hide emear
    with dissolve
    emelie "Jeez, you've gotta be careful with that stuff around Billy! "
    show emf pout with dissolve
    emelie "He gets super curious and excited over food he hasn't tried, and will always be up for a taste!"
    me "Good to know."
    me "He offered me some of his ice cream, so I would've felt bad not sharing what I had!"
    show emvs base
    show emf smile
    with dissolve
    emelie "Aw, that's considerate!"
    show emvs think
    show emf surprisethink
    show emear highz at right:
        yalign 0.06 xalign 0.9 zoom 1.00
    with dissolve
    emelie "Speaking of-"
    show emf normalblushthink with dissolve

    emelie "He said Bronwen was in a really good mood and wanted to give you something in return for helping her dad? "
    show emvs hips
    show emf bigsmile
    hide emear
    with dissolve
    emelie "'She give you anything nice?"
    #* sass *"
    window hide
    menu:
        with dissolve


        "We had fun!":
            $ bronfun = True
            window show
            me "We had fun."
            show emvs base
            show emf yeaa
            with dissolve
            emelie "Mhm?"
            show emf bite

        "...She basically tortured me.":
            $ bronfun = False
            window show
            me "...She basically tortured me."
            show emvs out
            show emf surprise2
            show emear highz at right:
                yalign 0.06 xalign 0.9 zoom 1.00
            with dissolve
            emelie "O-Oh?"
            show emf really
            show emvs base
            hide emear
            with dissolve
            emelie "Well..."
            show emf yeaa

    show emvs behindd
    with dissolve
    emelie "You look all shy talking about it-"
    me "..."
    me "Y'know how \"Humane Hunk\" had that page in it with all those toys for girls?"

    me "Well, she made me another type of... {i}toy..."
    me "But for my crotch."
    show emvs out
    show emf widez
    show emear highz at right:
        yalign 0.06 xalign 0.9 zoom 1.00
    with dissolve
    emelie "W-Wait- "
    show emf biggersmile
    with dissolve
    emelie "So it's something naughty the two of us can use? "
    "She seems excited."
    me "N-No way! "
    me "It got stuck, and she had to get me out of it!"
    show emvs hips
    show emf yeaa
    hide emear
    with dissolve
    emelie "Ahaa- I get the picture."
    "Emelie gives me a cheeky grin, seemingly understanding what must've happened."
    show emvs base
    show emf pout
    with dissolve
    emelie "Well, not every toy can be a winner."
    if bronfun == True:
        show emvs think
        show emf thinksass
        with dissolve
        emelie "'Glad you had fun at least!"
        me "Yeah! "
        me "And you and I will hopefully find a toy that's less scary in the future."
    if bronfun == False:
        show emvs hips
        show emf insecure
        with dissolve
        emelie "A shame it wasn't more enjoyable for you!"
        me "Yeah! "
        me "But you and I will hopefully find a toy that's less scary in the future."
    play sound "audio/soundFX/FX2/leave-water.wav" volume 0.5
    show bg BathRoom behind roomtowel with dissolve
    "The bath fills up-"
    show emvs out
    show emf surprise
    show emear highz at right:
        yalign 0.06 xalign 0.9 zoom 1.00
    with dissolve
    emelie "Ooo- "
    show emf wide with dissolve
    emelie "I'm sure you could use a bath after all of today, too."
    show emvs hips
    hide emear
    show emf sooth
    with dissolve
    emelie "Me and Victoria made a sloppy mess out of you earlier..."
    show emf normalblush
    show emvs out
    with dissolve
    emelie "And your hair must be salty from the ocean water, just like mine is!"
    "I wish that's all it was... but It's covered in fishy canal water, too!"
    me "Yeah, I definitely need a bath as well!"
    show emvs base
    show emf laugh
    show emear highz at right:
        yalign 0.06 xalign 0.9 zoom 1.00
    with dissolve
    emelie "Wohoo! "
    emelie "Let's hop in!"
    show emf decided2
    hide emear
    show emvs hips
    with dissolve
    emelie "But we've gotta be quick 'cus we don't have too long until the next guests come!"
    window hide
label bathscenebeforepeek:
    show black with fade
    if playnormal == False:
        window hide

        menu:
            with dissolve
            "Play Emelie's bath scene.":
                jump romance


            "Play peeking scene.":
                window hide
                jump corridorlewds2
    stop music fadeout 0.5
    queue music "audio/Em_theme.mp3" fadein 0.1 volume 0.3
    "Me and Emelie climb into the water together."
    window show


label romance:
    window hide
    play sound "audio/soundFX/FX2/water-swimming-4.mp3" volume 0.5
    scene emscrubbase
    show blackshake at truecenter zorder -100
    show emscruborder
    with fade
    hide emscruborder with dissolve
    pause 0.5
    window show
    "Her squishy butt sits down on my lap, and I slowly move my hands to her head."
    "If my crotch wasn't so abused I'd probably be horny right now..."
    "But instead, I'm just thinking about how good and cozy it feels to finally spend some more time with Emelie!"
    "I run my fingers through her foamy hair, and a nice flowery scent hits my nose."
    me "Mhh, this really does smell good."
    show emscrubf hapiscrub with dissolve
    emelie "Mmh! "
    emelie "And it feels even better!"
    show emscrubf hapiscrubz with dissolve
    emelie "I had a really fun day today-"
    me "Me too!"
    show emscrubf hapiscrub2 with dissolve
    emelie "I'm really glad you found me here in the baths, I was really starting to miss you!"
    me "Aww, I missed you too!"
    me "The last few days have been so eventful."
    me "I'm used to just having the same old routine day in and day out... "
    me "It feels like time is moving both fast and slow at the same time! "
    show emscrubf hapiscrubzx with dissolve
    emelie "I agree!"
    show emscrubf hapiscrub with dissolve
    emelie"I'm getting so many new fun memories to think back on, but time is also moving quickly since I'm having so much fun!"
    me "Exactly!"
    show emscrubf hapiscrub2 with dissolve
    emelie "I just hope it isn't stressing you out too much!"
    me "Not at all, it's really great."
    show emscrubf hapiscrub3 with dissolve
    emelie "Y-Yay!"
    show emscrubf peek with dissolve
    emelie "And I'm good at relieving your stress if you ever need me to~"
    "She gives me a cheeky wink."
    me "...You sure are."
    show emscrubnosoap with dissolve
    "Some of the foam is absorbed into her hair, and the rest of it falls into the water."
    hide emscrubf with dissolve
    emelie "That should be enough for my hair! "
    me "Okay! "
    me "Then I think it's time we move on tooo-"
    window hide
    pause 0.1
    play sound "audio/soundFX/swof.mp3" volume 0.8
    show emscrub pos1
    show emscrubf surpriis
    with dissolve
    queue sound "audio/soundFX/FX2/water-slosh-spashing-3.wav" volume 0.7
    with hpunch
    pause 0.3
    window show
    me "These!"
    emelie "!! "
    show emscrubf sidelook with dissolve
    emelie "R-Right, time to wash the rest of me..."
    show emscrubf hnmmm3 with dissolve
    emelie "Just be careful 'cus my skin's a bit sore-"
    window hide
    show emscrubf hnmmm with dissolve
    pause 0.2
    play sound "audio/soundFX/swof.mp3" volume 0.5
    show emscrub pos2 with dissolve
    queue sound "audio/soundFX/smacktit.wav" volume 0.6
    with vpunch
    hide emscrubf with dissolve

    pause 0.3
    window show
    "Emelie's heavy breasts smack against her chest as I give her top a tug-"
    emelie "Ahn!"
    me "Woah, you're so sunburnt!"
    show emscrubf hnmmm4 with dissolve
    emelie "Y-Yeah!"
    show emscrubf sass with dissolve
    emelie "After trying her swimsuit on Victoria's reading made me fall asleep in the sun!"
    show emscrubf bikin with dissolve
    emelie "So now I've got these tan lines where her bikini was..."
    window hide
    menu:
        with dissolve


        "It looks really sexy, I love it! ":
            window show
            me "It looks really sexy, I love it! "
            show emscrubf hnmmm3 with dissolve
            emelie "R-Really? "
            emelie "It'll look a bit like I'm wearing a bikini even if I'm not!"
            me "Exactly, and bikinis are hot!"
            show emscrubf sass with dissolve
            emelie "...If you say so~"
            me "Anyway, don't worry!"
            me "I'll be gentle-"


        "Ow, those must hurt.":
            window show
            me "Ow, those must hurt!"
            show emscrubf hnmmm3 with dissolve
            emelie "Mhm, they do!"
            me "I'll make sure to be gentle!"



    window hide
    pause 0.1
    queue sound "audio/soundFX/grabby.wav" volume 0.8
    show emscrub pos3 with dissolve
    with hpunch
    show emscrubf surpriseex with dissolve

    pause 0.3
    window show
    "I grip her soft breasts in my hands and slowly squeeze them."
    emelie "M-Mhhnn-"
    "I use the soap and shampoo in the water to give her a good rinse."
    hide emscrubf with dissolve
    emelie "H-Hey now, we don't have the time to  get frisky in here like we did the other day!"
    me "Okay, okay-"
    show emscrubf surpriisg with dissolve
    emelie "Buuut..."
    emelie "I have something I want to show you as soon as we're done in here, so let's finish up!"
    me "Alright, I'm excited!"
    stop music fadeout 1.5
    window hide
    scene black with dissolve
    show blackshake at truecenter zorder -100
    pause 0.3
    window show
    "We clean up in the baths and spend some extra time making sure our swimwear is nice and spotless-"
label nomakeupbath:
    window hide
    play sound "audio/soundFX/FX2/splash.wav" volume 0.4
    scene bg BathRoom
    show blackshake at truecenter zorder -100
    show roomtowel
    with fade

    show emaf  base at right:
        yalign 0.10
        zoom 1.0
    with dissolve
    pause 0.5
    show emaf hips
    show emfn normalblush at right:
        yalign 0.10
    show emear high at right:
        yalign 0.10
    with dissolve
    window show
    queue music "audio/starting-out-waltz-vivace-by-kevin-macleod-from-filmmusic-io.mp3" fadein 1.0 volume 0.3
    emelie "Ahhh, it always feels so refreshing to be newly bathed!"

    "I look at Emelie's curly hair, also noticing her face looks a bit less intense than usual-"
    show emaf out
    show emfn insecure
    with dissolve
    emelie "Geez, my hair looks awfully messy, doesn't it?"
    show emfn sad
    with dissolve
    emelie "And my makeup's all gone!"
    me "No, no-"
    me "You look amazing like this!"
    me "I love the hair, and your face is as pretty as ever!"
    show emaf base
    hide emear
    show emfn insecure
    with dissolve
    emelie "..."
    show emaf think
    show emfn think2
    with dissolve
    emelie "...You sure know how to flatter a girl~"
    show emaf base
    show emfn normalblush
    with dissolve
    emelie "Now, grab a towel and let's get out of here!"
    window hide
    hide emfn with dissolve
    show emaf  base at right:
        yalign 0.10
        zoom 1.0
        linear 0.5 xoffset -200
    pause 0.8
    show emaf  base at right:
        yalign 0.10
        zoom 1.0
        xoffset -200

    hide roomtowel with dissolve
    play sound "audio/soundFX/FX4/clothing2.wav" volume 0.7
    show emtow behindd at right:
        yalign 0.10
        zoom 1.0
        xoffset -200
    hide emaf
    with dissolve
    pause 0.4
    show roomnotowel behind emtow with dissolve
    pause 0.1
    play sound "audio/soundFX/get.mp3" volume 0.6
    with vpunch
    show emtow base at right:
        yalign 0.10
        zoom 1.0
        xoffset -200
    with dissolve
    pause 0.3

    window show


    "We both grab a towel and wrap it around our bodies."
    show emtow hips
    show emfn smile at right:
        yalign 0.10
        zoom 1.0
        xoffset -200
    show emear high at right:
        yalign 0.10
        zoom 1.0
        xoffset -200
    with dissolve
    emelie "That should do it for now since we don't have anything to change to-"




label corridorlewds:
    window hide
    show black with dissolve
label corridorlewds2:
    if playnormal == False:
           window hide
           show black
    play sound "audio/soundFX/OpenDoor 1.wav"
    scene bg corridorbath
    show blackshake at truecenter zorder -100
    show bathcorridoropensunset

    with fade
    pause 0.1
    show emtow hips at right:
        yalign 0.06 xalign 0.9

        zoom 1.0
    show emfn normalblush at right:
        yalign 0.06 xalign 0.9

        zoom 1.0
    with dissolve
    play sound "audio/soundFX/Door Close 2.wav" volume 0.8
    hide  bathcorridoropensunset  with dissolve
    pause 0.5
    window show
    emelie "Let's hurry down this corridor and get changed in my room!"
    stop music fadeout 0.3
    play sound "audio/soundFX/FX7/moany.wav" volume 1.0
    window hide
    with hpunch
    pause 0.2
    window show
    $ moom_name = "???"
    $ moog_name = "???"
    $ deeg_name = "???"
    $ deem_name = "???"
    play music "audio/Birds.wav" fadein 2.0 volume 0.2
    moog "{size=-1}{alpha=0.90}Mmhn-"
    deeg "{size=-1}{alpha=0.90}{i}*Giggles*"
    show emtow out
    show emfn wide at right:
        yalign 0.06 xalign 0.9

        zoom 1.0
    show emear high at right:
        yalign 0.06 xalign 0.9

        zoom 1.0
    with dissolve
    emelie "?!"
    me "You heard that too?"
    show emfn insecure at right:
        yalign 0.06 xalign 0.9

        zoom 1.0
    with dissolve
    emelie "Y-Yeah! "
    show emfn insecure at right:
        yalign 0.06 xalign 0.9

        zoom 1.0
    show emtow base
    hide emear
    show emeyen sidee at right:
        yalign 0.06 xalign 0.9

        zoom 1.0
    with dissolve
    emelie "What's that sound??"
    #peek or not
    if peekingtom1 == True:
        me "I... think something naughty might be going on in one of those rooms!"
        show emtow hips with dissolve
        emelie "What makes you think that?"
        "...Because I took a peek the first day I got here after hearing similar sounds."
        "But I can't tell her that!"
        me "I've just got a feeling based on the sounds!"
    else:
        me "Not sure... "
        me "I heard something similar two days ago but I didn't investigate."
    play sound "audio/soundFX/FX7/moany2.wav" volume 1.0
    with vpunch
    deem "{size=-1} {alpha=0.90}Mhhh-"
    show emtow panic
    hide emeyen
    show emfn surprise
    with dissolve
    emelie "Is that a third voice?!"
    me "Sounds like it might b-"
    with vpunch
    moom "{size=-1} {alpha=0.90}Aghn~"
    show emfn surprise2 with dissolve
    emelie "A FOURTH?!"



    show emtow out
    show emfn surprise
    show emeyen side2 at right:
        yalign 0.06 xalign 0.9

        zoom 1.0
    with dissolve
    emelie "They sound like they... uuuh... "
    show emtow base
    hide emeyen
    show emfn insecure
    hide emear
    with dissolve
    emelie "Might be struggling!"
    show emtow think
    show emfn think
    with dissolve
    emelie "Maybe we should... "
    show emeyen sidee at right:
        yalign 0.06 xalign 0.9

        zoom 1.0
    show emfn think2
    show emblush at right:
        yalign 0.06 xalign 0.9

        zoom 1.0
    with dissolve
    emelie "Have a quick little peek to see if everything's okay??"
    if peekingtom1 == True:
        "...She's a degenerate just like me."
    else:
        "Emelie sure is bold!"
        "Should we really be doing this?"
    window hide
    menu:
        with dissolve


        "{size=+3}Yeah, let's have a peek!!":
            window show
            me "Yeah, let's have a peek!!"
            show emtow out
            show emfn insecure
            show emear high  at right:
                yalign 0.06 xalign 0.9

                zoom 1.0
            hide emeyen


            with dissolve
            emelie "O-Okay, I'll go first!"
            jump wepeekmoose

        "{size=+1}I'll investigate alone! \n 'Wouldn't want you to see anything scary...":
            window show
            me "I'll investigate alone!"
            me "'Wouldn't want you to see anything scary..."
            show emtow out
            show emfn wide at right:
                yalign 0.06 xalign 0.9

                zoom 1.0
            show emear high at right:
                yalign 0.06 xalign 0.9

                zoom 1.0
            hide emeyen
            with dissolve
            emelie "..."
            show emfn angry
            hide emblush
            with dissolve
            emelie "Really?!"
            show emfn grump
            hide emear
            show emtow base
            with dissolve
            emelie "If you say so."
            show emtow think
            show emfn think
            show emeyen sideex at right:
                yalign 0.06 xalign 0.9

                zoom 1.0
            with dissolve
            emelie "But you better tell me what's happening in there!"
            me "I will."
            $ moom_name = "Moose Man"
            $ moog_name = "Moose Lady"
            $ deem_name = "Deer Guy"
            $ deeg_name = "Deer Girl"

            jump peekalonebaths



        "I don't think we should.":
            window show
            me "I don't think we should."
            show emtow behindd
            hide emeyen
            show emfn insecure
            with dissolve
            emelie "Y-You're probably right... "
            show emtow base
            show emfn wide
            hide emblush
            with dissolve
            emelie "It wouldn't be very becoming of a princess!"
            if playnormal == False:
                window hide
                scene black with fade
                pause 0.3
            $ renpy.end_replay()
            jump nopeeking

label wepeekmoose:
    window hide
    hide emtow
    hide emeyen
    hide emblush
    hide emear
    hide emfn
    with dissolve
    pause 0.1
    play sound "audio/soundFX/swof.mp3" volume 0.4
    show empeek0 with dissolve
    pause 0.5
    window show
    "Emelie crouches down and peeks in through the keyhole."
    window hide
    pause 0.3
    play sound "audio/soundFX/Dun.wav" volume 0.8
    with hpunch
    show empeek
    hide empeek0
    with dissolve
    pause 0.3
    window show
    emelie "{i}*GASPS*"
    emelie "..."
    show empeek3
    hide empeek
    hide empeek0
    with dissolve
    emelie "Tss!"
    window hide
    hide empeek3 with dissolve
    pause 0.1
    show emtow out at right:
        yalign 0.06 xalign 0.9

        zoom 1.0
    show emfn wide at right:
        yalign 0.06 xalign 0.9

        zoom 1.0
    show emblush at right:
        yalign 0.06 xalign 0.9

        zoom 1.0
    show emear high at right:
        yalign 0.06 xalign 0.9

        zoom 1.0
    with dissolve
    pause 0.3
    window show
    emelie "G-Go take a look!"


    $ moom_name = "Moose Man"
    $ moog_name = "Moose Lady"
    $ deem_name = "Deer Guy"
    $ deeg_name = "Deer Girl"



    me "...If you say so."
    "I'm a little scared..."
    window hide
    scene black with fade
    play sound "audio/soundFX/Get.mp3"
    window show
    "I step up to the door and start aligning my eye to the keyhole-"
    window hide
    play music "audio/Farm+-+320bit.mp3" fadein 2.0 volume 0.3
    scene deerfuccbase
    show blackshake at truecenter zorder -100
    show keyholesecondtime
    with fade
    with vpunch
    pause 0.5
    window show
    "!!"
    me "{size=-1}{alpha=0.85}Woa-"
    if peekingtom1 == True:
        "It's the same two couples I saw last time!"
        "It looks like things have really escalated between the two moose!"
        "And the two deer are making out in the back!"
    else:
        "It looks like a moose couple is getting naughty!"
        "And two deer are making out in the back!"
    show mooses fex with dissolve
    moom "Ungh-"
    "He's fucking her thigh gap!"
    show mooses fexx with dissolve
    moog "MMhhnn, nice and slippery~"
    "The moose man ups his pace!"
    window hide
    play sound "audio/soundFX/grabby.wav" volume 0.8
    with vpunch
    show mooses fuckstart with dissolve
    pause 0.3
    show deers surprise behind keyholesecondtime with dissolve
    pause 0.5
    window show
    moom "Nhhg... That's it-"
    moog "Ahhn, it's rubbing against my clit..."
    show moosex with dissolve
    moom "Fffhuck, you're so wet!"
    show mooses fuckstart2 with dissolve
    moog "Heheh... "
    moog "Any rougher than that and you just might might slip inside!"
    show mooses fuckstart2x
    hide moosex
    with dissolve
    moom "...I'll be careful."
    show mooses fuckstart2xx with dissolve
    moog "I'm not asking you to be~"
    show mooses fuckposehorny0 with dissolve
    moom "!"
    me "{i}{size=-1}{alpha=0.85}*Gulp*"
    "I swallow hard."
    #Scene outside

    emelie "{size=-1}{alpha=0.85} W-What's happening?"
    window hide
    play sound "audio/soundFX/swof.mp3" volume 0.8
    show black with dissolve
    scene bg corridorbath
    show emtow hips at right:
        yalign 0.06 xalign 0.9

        zoom 1.0
    show emfn angry at right:
        yalign 0.06 xalign 0.9

        zoom 1.0
    show emear high at right:
        yalign 0.06 xalign 0.9

        zoom 1.0
    with fade
    show blackshake at truecenter zorder -100
    pause 0.3
    window show
    emelie "You're spending way more time peeking than me!"
    show emtow base
    hide emear
    show emfn grin
    show emeyen sideex at right:
        yalign 0.06 xalign 0.9

        zoom 1.0
    show emblush at right:
        yalign 0.06 xalign 0.9

        zoom 1.0
    with dissolve
    emelie "My turn!"
    "Emelie heads back to the door-"
label emeliepeeks:
    window hide
    hide emear
    hide emblush
    hide emfn
    hide emeyen
    hide emtow
    with dissolve
    pause 0.2
    play sound "audio/soundFX/swof.mp3" volume 0.4
    show empeek0 with dissolve
    pause 0.6
    window show
    emelie "..."
    window hide
    with hpunch
    show empeek2 with dissolve
    window show
    emelie "Haaahh!! "
    "She blushes bright red."
    emelie "N-No way!"
    me "Let me see!"
    "This is making me way too curious!"
    window hide
    scene black with fade
    show blackshake at truecenter zorder -100
    window show
    "I hurry back to the keyhole, pushing Emelie to the side to get a better view-"
    window hide
    play sound "audio/soundFX/Get.mp3"
    with hpunch
    window show
    emelie "{alpha=0.85}{size=-1}Not fair!"
    window hide
    scene deerfuccbase
    show blackshake at truecenter zorder -100
    show deers hornyz
    show moosesfuckpose1

    show keyholesecondtime
    show deersurprooss
    show supad
    with fade
    play sound "audio/soundFX/Dun.wav" volume 0.4
    with vpunch
    pause 0.6
    window show
    "WOAH!"
    deem "Wh-"
    deeg "Eek!"
    "They started fucking in front of the deer couple!"
    show mooses fuckposehng with dissolve
    moog "Aaahn!"
    show mooses fuckposegao with dissolve
    moom "Ffhuuck, you're tight!"
    show mooses fuckposegaox with dissolve
    moog "I love it!"
#    moog " I love it, daddy!"

    window hide
    pause 0.1
    hide supad
    with dissolve
    pause 0.3
    hide deersurprooss
    with dissolve
    pause 0.3
    window show
    "And now the deer guy's getting a boner!?"
    deeg "M-Maybe I should..."
    window hide
    play sound "audio/soundFX/softget.wav" volume 0.3
    hide deers
    show deers succ
    hide keyholesecondtime
    show keyholesecondtime
    with dissolve
    with vpunch
    pause 0.4
    window show
    me "{size=-1}{alpha=0.85} What thee-"
    "Now the two deer are getting into it!"
    emelie "{size=-1}{alpha=0.85}What's happening?!"
    me "{size=-1}{alpha=0.85}Just ooone second-"
    show moosax with dissolve
    moom  "I-I'm cumming!"
    show ghaahhn
    with dissolve
    deem "M-Me too!"
    hide mooses
    hide moosax
    with dissolve
    moog "Nnh-"
    show cmonboys with dissolve
    moog "Let it all go, boys!~"
    window hide
    pause 0.1
    play sound "audio/soundFX/smacktit.wav" volume 0.3
    with vpunch
    show moosesboth cum behind keyholesecondtime
    show mooses fuckposehng
    with dissolve

    pause 0.3
    window show
    moom "Ahg!"
    window hide
    pause 0.1
    play sound "audio/soundFX/move.wav" volume 0.3
    show moosesbothcum behind keyholesecondtime

    with dissolve
    with vpunch
    pause 0.3
    window show
    deem "Gaah!"
    "They both cum!"
    show mooses fuckposegaoxx with dissolve
    moog "NNhaah!"
    "And the moose lady really got off, too!"
    window hide
    show black with dissolve
    play sound "audio/soundFX/swof.mp3" volume 0.6
    scene bg corridorbath
    show blackshake at truecenter zorder -100



    show emtow out at right:
        yalign 0.06 xalign 0.9

        zoom 1.0

    show emtow out
    show emfn surprise at right:
        yalign 0.06 xalign 0.9

        zoom 1.0
    with fade
    show emtow panic
    show emfn surprise2
    show emear high at right:
        yalign 0.06 xalign 0.9

        zoom 1.0
    show emblush
    with dissolve
    window show
    emelie "That sounded like screaming!"
    show emblush at right:
        yalign 0.06 xalign 0.9

        zoom 1.0
    show emfn sad
    show emeyen side2 at right:
        yalign 0.06 xalign 0.9

        zoom 1.0
    with dissolve
    emelie "What happened in there?!"
    me "...Let's have a look together."
    window hide
    show emtow out
    show emeyen sidee
    show emfn insecure
    hide emear
    with dissolve
    hide emear
    hide emblush
    hide emeyen
    hide emfn
    hide emtow
    with dissolve
    pause 0.2
    play sound "audio/soundFX/move.wav" volume 0.3
    show empeek0 with dissolve
    pause 0.3
    window show
    "She sits down again and I follow right behind-"
    window hide
    show black with dissolve
    play sound "audio/soundFX/get.mp3" volume 0.4
    pause 0.2
    scene deerfuccendcum
    show keyholesecondtime
    show deerorny
    with fade
    pause 0.4
    window show
    moog "Ghh, that was fun..."
    moom "Phuhh... Yeah."
    show moosemanlookside
    hide deerorny
    with dissolve
    moog "And you two sure look... satisfied back there~"
    show gulpdeer with dissolve
    deeg "{i}*Gulp* "
    "She's swallowing it all!"
    moog "Hah!"
    show gulpdeer2 with dissolve
    deeg "Bweeeh-"
    show deeriboo with dissolve
    moog "You're a good slut... "
    moog "Swallowing aaaall that warm cum down."
    show leggooo
    show deeriboox
    with dissolve
    moom "Now... Push all that out so we can get moving-"
    moom "I don't want the next guests to... see who made this mess."
    show mocummz with dissolve
    moog "Yes, sir~"
    window hide
    pause 0.1
    show mocumm with dissolve
    pause 0.2
    window show
    me "{size=-1}{alpha=0.85}Shiet- We should hurry!"
    emelie "{size=-1}{alpha=0.85}Mhm!"


    stop music fadeout 1.0
    queue music "audio/Birds.wav" fadein 2.0 volume 0.1
    window hide
    show black with dissolve
    play sound "audio/soundFX/swof.mp3" volume 0.6
    pause 0.3
    scene bg corridorbath
    show emtow out at right:
        yalign 0.06 xalign 0.9

        zoom 1.0
    show emfn wide at right:
        yalign 0.06 xalign 0.9

        zoom 1.0
    show emear high at right:
        yalign 0.06 xalign 0.9

        zoom 1.0
    with fade
    show blackshake at truecenter zorder -100
    pause 0.3
    window show
    emelie "That was crazy..."
    if playnormal == False:
        window hide
        scene black with fade
        pause 0.3
    $ unlock("S11")
    $ renpy.end_replay()
    show emtow think
    hide emear
    show emeyen sideex at right:
        yalign 0.06 xalign 0.9

        zoom 1.0
    show emblush at right:
        yalign 0.06 xalign 0.9

        zoom 1.0
    show emfn think

    with dissolve
    emelie "I thought that deer girl looked so shy and innocent-"
    window hide


    show emtow panic
    hide emeyen
    hide emblush
    show emear high at right:
        yalign 0.06 xalign 0.9

        zoom 1.0
    show emfn surprise
    with dissolve
    play sound "audio/soundFX/Dun.wav" volume 0.3
    with hpunch
    window show
    emelie "Then WHAM!"
    show emfn wide
    hide emear
    show emtow out
    with dissolve
    emelie "She started really going for it!"
    me "...I thought you looked pretty shy and innocent when we first met, too..."
    me "Then WHAM!"
    show emtow behindd
    show emfn angry
    show emblush at right:
        yalign 0.06 xalign 0.9

        zoom 1.0
    with dissolve
    emelie "H-Hey!"
    show emfn insecure
    show emtow hips
    with dissolve
    emelie "We were just... massaging each other back then. "
    emelie "And all that was in private!"
    me "..."
    me "If you say so."
    "She won't admit to being naughty herself!"
    show emtow base
    show emfn wide
    show emear high at right:
        yalign 0.06 xalign 0.9

        zoom 1.0
    hide emblush
    with dissolve
    emelie "Anyways, let's hurry back to my room!"

    jump afterpeek

label nopeeking:
    show emtow out
    show emfn surprise
    show emear high at right:
        yalign 0.06 xalign 0.9

        zoom 1.0
    with dissolve
    emelie "And what if someone had seen us peeking!? "
    show emtow base
    show emfn insecure
    hide emear
    with dissolve
    emelie "We should hurry to my room before anyone catches us in the hallway without any clothes on!"

    jump afterpeek



label peekalonebaths:
        "I curiously approach the door-"
        window hide
        scene black with fade
        play sound "audio/soundFX/Get.mp3"
        window show
        "And align my eye to the keyhole-"
        window hide
        play music "audio/Farm+-+320bit.mp3" fadein 2.0 volume 0.3
        scene deerfuccbase
        show blackshake at truecenter zorder -100
        show keyholesecondtime
        with fade
        with vpunch
        pause 0.5
        window show
        "!!"
        me "{size=-1}{alpha=0.85}Woa-"
        if peekingtom1 == True:
            "It's the same two couples I saw last time!"
            "It looks like things have really escalated between the two moose!"
            "And the two deer are making out in the back!"
        else:
            "It looks like a moose couple is getting naughty!"
            "And two deer are making out in the back!"
        show mooses fex with dissolve
        moom "Ungh-"
        "He's fucking her thigh gap!"
        show mooses fexx with dissolve
        moog "MMhhnn, nice and slippery~"
        "The moose man ups his pace!"
        window hide
        play sound "audio/soundFX/grabby.wav" volume 0.8
        with vpunch
        show mooses fuckstart with dissolve
        pause 0.3
        show deers surprise behind keyholesecondtime with dissolve
        pause 0.5
        window show
        moom "Nhhg... That's it-"
        moog "Ahhn, it's rubbing against my clit..."
        show moosex with dissolve
        moom "Fffhuck, you're so wet!"
        show mooses fuckstart2 with dissolve
        moog "Heheh... "
        moog "Any rougher than that and you just might slip inside!"
        show mooses fuckstart2x
        hide moosex
        with dissolve
        moom "...I'll be careful."
        show mooses fuckstart2xx with dissolve
        moog "I'm not asking you to be~"
        show mooses fuckposehorny0 with dissolve
        moom "!"
        me "{i}{size=-1}{alpha=0.85}*Gulp*"
        "I swallow hard."
        #Scene outside

        emelie "{size=-1}{alpha=0.85}W-What's happening?"
        window hide
        play sound "audio/soundFX/swof.mp3" volume 0.8
        show black with dissolve
        scene bg corridorbath
        show emtow hips at right:
            yalign 0.06 xalign 0.9

            zoom 1.0
        show emfn angry at right:
            yalign 0.06 xalign 0.9

            zoom 1.0
        show emear high at right:
            yalign 0.06 xalign 0.9

            zoom 1.0
        with fade
        show blackshake at truecenter zorder -100
        pause 0.3
        window show
        emelie "You're blushing!"
        show emfn wide
        show emtow out
        with dissolve
        emelie "Just what is happening in there??"
        window hide
        menu:
            with dissolve


            "Just some old, wrinkly piggy taking a bath. \n {alpha=*0.85} {size=-2}* Lie to continue looking by yourself! *":
                window show
                me "Just some old, wrinkly piggy taking a bath!"
                me " Those other voices must've come from outside or something..."

                show emtow think at right:
                    yalign 0.06 xalign 0.9

                    zoom 1.0
                show emfn think at right:
                    yalign 0.06 xalign 0.9

                    zoom 1.0
                hide emear
                with dissolve
                emelie "R-Really?"
                show emfn ew with dissolve
                emelie "...Then why were you staring so longingly?"
                me "I'm... uuh..."
                "Shit."
                me "I'm just making sure he's safe!"
                me "It looked like he was about to slip on a bar of soap- "
                me "So I should get back there to make sure he's okay!"
                show emfn dafak
                show emtow hips
                with dissolve
                emelie "{size=-5}...W-Wha?"
                "Emelie looks completely confused, so now's my chance to get back to peeking!!"


            "Two couples are getting frisky in there!\n {alpha=*0.85} {size=-2} * Let Emelie peek with you. * ":
                window show
                $ lateempeek = True
                me "Two couples are getting frisky in there!"
                show emtow panic
                show emfn surprise2
                show emear high at right:
                    yalign 0.06 xalign 0.9

                    zoom 1.0
                show emblush at right:
                    yalign 0.06 xalign 0.9

                    zoom 1.0
                with dissolve
                emelie "Whaaa?!"
                show emfn surprise
                show emeyen side2 at right:
                    yalign 0.06 xalign 0.9

                    zoom 1.0
                with dissolve
                emelie "I wanna see!"
                jump emeliepeeks

        window hide
        scene black with fade
        show blackshake at truecenter zorder -100
        window show
        "I hurry back to the keyhole-"
        window hide
        play sound "audio/soundFX/Get.mp3"
        pause 0.3
        scene deerfuccbase
        show blackshake at truecenter zorder -100
        show deers hornyz
        show moosesfuckpose1

        show keyholesecondtime
        show deersurprooss
        show supad
        with fade
        pause 0.2
        play sound "audio/soundFX/Dun.wav" volume 0.4
        with vpunch
        pause 0.6
        window show
        "WOAH!"
        deem "Wh-"
        deeg "Eek!"
        "They started fucking right in front of the deer couple!"
        show mooses fuckposehng with dissolve
        moog "Aaahn!"
        show mooses fuckposegao with dissolve
        moom "Ffhuuck, you're tight!"
        show mooses fuckposegaox with dissolve
        moog "I love it!"
    #    moog " I love it, daddy!"

        window hide
        pause 0.1
        hide supad
        with dissolve
        pause 0.3
        hide deersurprooss
        with dissolve
        pause 0.3
        window show
        "And now the deer guy's getting a boner!?"
        deeg "M-Maybe I should..."
        window hide
        play sound "audio/soundFX/softget.wav" volume 0.3
        hide deers
        show deers succ
        hide keyholesecondtime
        show keyholesecondtime
        with dissolve
        with vpunch
        pause 0.4
        window show
        me "{size=-1}{alpha=0.85}What thee-"
        "Now the two deer are getting into it!"
        emelie "{size=-1}{alpha=0.85}What's happening?!"
        me "{size=-1}{alpha=0.85}Just ooone second-"
        show moosax with dissolve
        moom  "I-I'm cumming!"
        show ghaahhn
        with dissolve
        deem "M-Me too!"
        hide mooses
        hide moosax
        with dissolve
        moog "Nnh-"
        show cmonboys with dissolve
        moog "Let it all go, boys!~"
        window hide
        pause 0.1
        play sound "audio/soundFX/smacktit.wav" volume 0.3
        with vpunch
        show moosesboth cum behind keyholesecondtime
        show mooses fuckposehng
        with dissolve

        pause 0.3
        window show
        moom "Ahg!"
        window hide
        pause 0.1
        play sound "audio/soundFX/move.wav" volume 0.3
        show moosesbothcum behind keyholesecondtime

        with dissolve
        with vpunch
        pause 0.3
        window show
        deem "Gaah!"
        "They both cum!"
        show mooses fuckposegaoxx with dissolve
        moog "NNhaah!"
        "And the moose lady really got off, too!"
        window hide
        show black with dissolve
        play sound "audio/soundFX/swof.mp3" volume 0.6
        scene bg corridorbath
        show blackshake at truecenter zorder -100



        show emtow out at right:
            yalign 0.06 xalign 0.9

            zoom 1.0

        show emtow out
        show emfn surprise at right:
            yalign 0.06 xalign 0.9

            zoom 1.0
        with fade
        show emtow panic
        show emfn surprise2
        show emear high at right:
            yalign 0.06 xalign 0.9

            zoom 1.0
        show emblush
        with dissolve
        window show
        emelie "That sounded like screaming!"
        show emblush at right:
            yalign 0.06 xalign 0.9

            zoom 1.0
        show emfn sad
        show emeyen side2 at right:
            yalign 0.06 xalign 0.9

            zoom 1.0
        with dissolve
        emelie "D-Did the old man slip on the soap?!"

        me "U-Uuuhh..."
        me "..."
        "What do I say?!"
        me "I-I shut my eyes just as he stepped on it because I got scared!"
        me "I'll hurry back real quick to make sure all is well!"
        show emtow out
        hide emear
        hide emblush
        hide emeyen
        show emfn ew2
        with dissolve
        emelie "O-Okay..."
        window hide
        show black with dissolve
        play sound "audio/soundFX/get.mp3" volume 0.4
        pause 0.2
        scene deerfuccendcum
        show keyholesecondtime
        show deerorny
        with fade
        pause 0.4
        window show
        moog "Ghh, that was fun..."
        moom "Phuhh... Yeah."
        show moosemanlookside
        hide deerorny
        with dissolve
        moog "And you two sure look... satisfied back there~"
        show gulpdeer with dissolve
        deeg "{i}*Gulp* "
        "She's swallowing it all!"
        moog "Hah!"
        show gulpdeer2 with dissolve
        deeg "Bweeeh-"
        show deeriboo with dissolve
        moog "You're a good slut... "
        moog "Swallowing aaaall that warm cum down."
        show leggooo
        show deeriboox
        with dissolve
        moom "Now... Push all that out so we can get moving-"
        moom "I don't want the next guests to... see who made this mess."
        show mocummz with dissolve
        moog "Yes, sir~"
        window hide
        pause 0.1
        show mocumm with dissolve
        pause 0.2
        window show
        "Shiet- I need to get out of here!"


        stop music fadeout 1.0
        queue music "audio/Birds.wav" fadein 2.0 volume 0.1
        window hide
        show black with dissolve
        play sound "audio/soundFX/swof.mp3" volume 0.6
        pause 0.3
        scene bg corridorbath
        show emtow out at right:
            yalign 0.06 xalign 0.9

            zoom 1.0
        show emfn wide at right:
            yalign 0.06 xalign 0.9

            zoom 1.0
        show emear high at right:
            yalign 0.06 xalign 0.9

            zoom 1.0
        with fade
        show blackshake at truecenter zorder -100
        pause 0.3
        window show
        emelie "So, what happened?!"
        with hpunch
        show emfn surprise
        show emeyen side2  at right:
            yalign 0.06 xalign 0.9

            zoom 1.0
        with dissolve
        emelie "Did he slip on that bar of soap!?"
        if playnormal == False:
            window hide
            scene black with fade
            pause 0.3
        $ unlock("S11")
        $ renpy.end_replay()
        me "Oh-uh-yeah!"
        me "He slid around all over the place-"
        me "But he's doing good now!"
        show emtow base
        show emfn insecure
        hide emeyen
        hide emear
        with dissolve
        emelie "Pheww- "
        me "But sliding around in soap like that made him SUPER clean, so he'll be coming out any second now!"
        show emtow panic
        show emfn surprise2
        show emeyen side2  at right:
            yalign 0.06 xalign 0.9

            zoom 1.0

        show emear high at right:
            yalign 0.06 xalign 0.9

            zoom 1.0
        with dissolve
        emelie "R-Really?!"
        hide emeyen
        show emfn surprise
        show emtow out
        with dissolve
        emelie "Then let's hurry on over to my room!"
        me "Yeah!"
        "I feel a bit bad for lying through my teeth like that..."
        "But I wanted the view all to myself!"

        jump afterpeek







label afterpeek:
    window hide
    show black with dissolve
    scene bg doorsunset with fade
    show blackshake at truecenter zorder -100
    play sound "audio/soundFX/runn.wav"
    play music "audio/starting-out-waltz-vivace-by-kevin-macleod-from-filmmusic-io.mp3" fadein 0.1 volume 0.3
    show emtow base at right:
        yalign -0.07
        xalign 0.5
        zoom 0.95
    with easeinleft
    pause 0.3
    show emtow out
    show emfn normalblush at right:
        yalign -0.07
        xalign 0.5
        zoom 0.95
    with dissolve
    window show
    emelie "Puuh, we made it without being spotted-"
    me "Lucky!"
    show emtow hips
    show emfn smile
    show emear high at right:
        yalign -0.07
        xalign 0.5
        zoom 0.95
    with dissolve
    emelie "Noooow, you head in first!"
    emelie "I want to show you something."
    me "Alright!"
    window hide
    #jump Ending
    play sound "audio/soundFX/OpenDoor 1.wav" volume 0.5
    show  bg doorsunsetopen with dissolve
    scene bg emroomsunset with fade
    show blackshake at truecenter zorder -100
    pause 0.5
    window show
    me "Woah, this place looks a bit different!"
    window hide
    play sound "audio/soundFX/runn.wav"
    show emtow base at right:
        yalign 0.05
        xalign 0.85
        zoom 1.0
    with easeinleft
    pause 0.3
    show emfn normalblush at right:
        yalign 0.05
        xalign 0.85
        zoom 1.0
    show emtow hips
    with dissolve
    window show
    emelie "Yeah?"
    show emtow behindd
    show emfn smile
    show emear high at right:
        yalign 0.05
        xalign 0.85
        zoom 1.0
    with dissolve
    emelie "It's your new room!!"
    #emelie " I made some tweaks to it!"
    window hide
    stop music fadeout 0.2
    play sound "audio/soundFX/Dun.wav" volume 1.0
    with vpunch
    window show
    me "{size=+2}What?!"
    window hide
    pause 0.3
    jump Ending
    return

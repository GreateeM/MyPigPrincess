label fightpits:
    play music "audio/beachfundrums.mp3"  fadein 4.0 volume 0.27
    scene crowdbronbase
    show blackshake at truecenter zorder -100
    show crowdbron fistdown
    show crowdbronn beerhold
    show crowdrolf two
    with fade
    $ bull_name = "Bull"
    $ ref_name = "Referee"
    pause 0.5
    window show
    rolf "Holy shit, the little guy is really doing it!"
    bron "You've got thiss!!"
    window hide
    show pitchoke one with fade
    with hpunch

    pause 0.5
    window show
    #Northern cat is choking out bull man.
    #rolf " And I thought open weight contests were stupid, the bigger man wins 99% of the time!"
    "Woah, so that's why they're all cheering!"
    "Ilves is doing good!!"
    window hide
    hide pitchoke

    show crowdrolf three
    with fade
    pause 0.3
    window show
    rolf "Big guy's gotta fight the hands! What an amateur."
    bron "Choke him out!"
    #NameIsBull
    window hide
    show pitchoke one with fade
    pause 0.3
    window show
    bull "Ghhnnf-"
    cat "Just go to sleep! Relaaax!"
    window hide
    show pitchoke two with dissolve
    #play sound "audio/soundFX/FX3/trip-on.wav" volume 0.6
    play sound "audio/soundFX/crack_2.wav" volume 0.8
    with hpunch
    pause 0.4
    window show
    bull "Khhf!-"
    "The bull looks like he's just about to pass out! "
    window hide



    #Bull pokes eyes and things go crazy.
    stop music
    pause 0.1
    play sound "audio/soundFX/FX6/stabmeow.wav" volume 0.7
    show pitchoke three
    with dissolve
    show blackshake at truecenter zorder -100
    with vpunch
    pause 0.2
    play sound "audio/soundFX/FX3/clean-record-scratch.wav" volume 0.6
    pause 0.3
    window show
    cat "Meow!"
    "{size=+4}WHAT!?"
    "He poked Ilves in the eyes!"
    window hide
    pause 0.3
    show black with fade
    window show
    #Loud Whistle "
    ref "FOOOUL!"
    window hide
    hide pitchoke
    hide crowdbronn beerhold
    hide black
    show crowdbronbase
    show crowdrolf four
    show crowdb rage behind crowdrolf
    show crowdbronn rage behind crowdrolf
    show crowdbronbasebeer behind crowdrolf
    with dissolve
    pause 0.3
    window show

    #cuttorolf
    bron "What the fuck was that?!"
    rolf "Cheating bastard! "
    window hide
    play sound "audio/soundFX/run2r.wav" volume 1.0
    hide crowdrolf with dissolve


    pause 0.4
    window show
    "Rolf gets up and trudges down to the pit. "
    emelie "Jeez, [Protagonist]! "
    me "Hmm?"
    emelie "My legs get all weak when I'm nervous..."
    emelie "I'm taking a seat! "
    me "Okay!"
    window hide

    play sound "audio/soundFX/Sit Pillow.wav"
    #play sound "audio/soundFX/Get.mp3"
    if modest == True:
        show crowdemesuit with dissolve
    else:
        show crowdemelon with dissolve
    show crowdb eyeside
    hide crowdbronn
    show crowdbouth pout
    with dissolve
    pause 0.4
    window show
    bron "Hey, Em."
    show crowdemlookbron with dissolve
    emelie "H-Hello!"
    "Emelie looks tense!"
    #pic of arena and goat being there
    window hide
    scene bg pits
    show blackshake at truecenter zorder -100
    show bgpits people
    show rounds one
    show goatbg base
    show bullb neck at left:
        yalign 0.6 xalign -0.25 zoom 0.80
    show ilv rub at right:
        yalign -3.0 xalign 1.2 zoom 0.88
    with fade
    pause 0.6
    hide goatbg base
    with dissolve
    pause 0.2
    show goat handdown at center:
        xalign 0.47 yalign 4.5 zoom 0.83
    show goatf blow at center:
        xalign 0.47 yalign 4.5 zoom 0.83
    with dissolve
    play sound "audio/soundFX/FX6/78508__joedeshon__referee_whistle_02.wav"volume 0.7

    with hpunch
    window show

    ref "{size=50}{i}*WHISTLES*{/i}{/size}"#TOOOT
    play music "audio/MPP_-_Brewing_Tension_Pre-Fight_FINAL_2.mp3"  noloop fadein 0.0 volume 0.18
    queue music "audio/MPP_-_Brewing_Tension_Pre-Fight_VERSE.mp3" loop  fadein 0.0 volume 0.13
    show ilv ow with dissolve
    cat "M-My eyes!"
    "Ilves' eyes are swollen shut!"
    show goatf teeth
    show goateye left at center:
        xalign 0.47 yalign 4.5 zoom 0.83
    show goat hol
    with dissolve
    ref "'The hell did you do that for?!"

    $ bull_name = "Bull-y"
    bull "...Ugkh!"
    show bulleye rightdown at left:
        yalign 0.6 xalign -0.25 zoom 0.80
    show bullb base
    with dissolve
    bull "'Little shit went for my neck!"
    show goat handdown
    show goatf think
    hide goateye
    with dissolve
    ref "Choke holds are legal in the pits!"
    window hide
    show ilv sadd with dissolve
    play sound "audio/soundFX/run2r.wav" volume 1.0
    pause 0.2


    show rolf point2 behind ilv at right:
        zoom 0.85 yalign 1.0 xalign 1.1
    show rol angerpoint behind ilv at right:
        zoom 0.85 yalign 1.0 xalign 1.1
    with easeinright
    show bulleye right2
    show bullf done2 behind bulleye at left:
        yalign 0.6 xalign -0.25 zoom 0.80
    with dissolve
    pause 0.3
    window show
    #rolf slides in
    rolf "And eye pokes aren't!"
    rolf "Two more seconds and you would've been OUT!"
    show goateye right at center:
        xalign 0.47 yalign 4.5 zoom 0.83
    show goat handup
    with dissolve
    ref "Don't get any closer!"
    "Rolf's pissed!"
    show rolf base
    show rol angerfrank
    with dissolve
    rolf "..."

    show goat think
    show goateye left

    with dissolve
    ref "Well, Alfred? "
    $ bull_name = "Alfred"
    show bullf done behind bulleye at left:
        yalign 0.6 xalign -0.25 zoom 0.80

    show bulleye frank at left:
        yalign 0.6 xalign -0.25 zoom 0.80
    show bullb crack
    with dissolve
    bull "That was no eye poke, Frank. "
    show bullb knuckle
    show bullf grin
    show bulleye rightdown
    with dissolve
    bull "It was a clean punch to the face!"
    $ ref_name = "Referee Frank"

    show rol omegarage
    show rolf knucklez
    with dissolve
    #with hpunch
    rolf "A punch?! That's bullshit!"
    show bullb knuckles
    show bullf bullshit behind bulleye
    hide bulleye right
    with dissolve
    #with vpunch
    bull "B-Bullshit?!"
    window hide
    show goatf scream
    show goat handdown
    hide goateye
    with dissolve
    with hpunch
    window show
    ref "Shut it, both of you!"
    #both relax
    window hide
    show bullb base
    show rolf base
    show rol angerfrank
    hide bullf
    hide bulleye
    show bulleye frank at left:
        yalign 0.6 xalign -0.25 zoom 0.80
    with dissolve
    show goat isaw
    hide goatf
    hide goateye
    with dissolve
    window show
    ref "I saw the fingers! "
    show bullf done
    show bullb hips
    show bulleye closedd
    with dissolve
    bull "... Accidental foul, then. "
    show bullf done behind bulleye at left:
        yalign 0.6 xalign -0.25 zoom 0.80
    with dissolve
    bull "I was going for a palm strike and my fingers might've grazed him a little..."
    show goat handdown
    show goatf think at center:
        xalign 0.47 yalign 4.5 zoom 0.83
    show goateye right at center:
        xalign 0.47 yalign 4.5 zoom 0.83

    with dissolve

    show rolf point2
    show rol angerscreamnotnude
    with dissolve
    #with hpunch


    rolf "Oh, so it's a {i}\"palm strike\"{/i} now, is it?!"
    show bullb base
    hide bulleye
    show bullf bullshit
    with dissolve
    show rolf knucklez
    show rol angerpoint
    with dissolve
    rolf "'The hell are you doing in the open weight bracket anyways!? "
    rolf "You look like you're pushing the weight limit of a heavyweight! "
    show rolf base
    show rol angerpoint2
    with dissolve
    rolf "And Hog Haven has one of the most reputable heavyweight divisions in the world!"
    show bullb crack
    show bullf done
    show bulleye right at left:
        yalign 0.6 xalign -0.25 zoom 0.80
    with dissolve
    bull "... Those fatties who do nothing but lay on you in the mud?"
    show rolf knuckles
    show rol angerscreamnotnude
    with dissolve
    rolf "Pigs are great wrestlers!"
    rolf "If you can't defend a bloody takedown, go back to training!"
    show rolf point2
    show rol angerpoint
    with dissolve
    rolf "Don't use it as an excuse to beat up on the little guys!"
    show goat handup
    show goatf scream at center:
        xalign 0.47 yalign 4.5 zoom 0.83
    hide goateye
    with dissolve
    show blackshake at truecenter zorder -100
    with vpunch
    ref "I said SHUT IT!"
    hide bullf
    hide bulleye
    show bulleye frank at left:
        yalign 0.6 xalign -0.25 zoom 0.80
    show bullb hips
    show rolf base
    show rol angerfrank
    with dissolve
    show goat think
    show goatf thinkhard
    with dissolve
    ref "Quiet while I make my decision!"
    ref "Hmmm..."
    "Frank deliberates for a moment."
    show goateye ilves at center:
        xalign 0.47 yalign 4.5 zoom 0.83
    with dissolve
    ref "So, Ilves-"
    show ilv ow with dissolve
    cat "Myes?"
    ref "Can you see?"
    show ilv base
    show ilveye shut at right:
        yalign -3.0 xalign 1.2 zoom 0.88
    with dissolve
    cat "I can fight!"
    show goatf think
    show goat handdown
    show goateye ilves2
    with dissolve
    ref "But can you SEE? "
    show ilv rub
    hide ilveye
    with dissolve
    cat "..."
    show ilv close
    show ilveye shut at right:
        yalign -3.0 xalign 1.2 zoom 0.88
    with dissolve
    cat "Soon, maybe."
    hide goateye
    with dissolve
    ref "Ugh..."
    #CrossArms
    window hide
    stop music fadeout 0.2
    play sound "audio/soundFX/FX5/rolfknuckles.wav" volume 0.2
    show goat timeout
    hide goatf
    with dissolve
    with hpunch
    play music "audio/Seagul.wav" fadein 2.0 volume 0.25
    pause 0.7
    window show
    ref "The fight's off! "
    ref "Alfred's disqualified due to a blatant foul."
    show bullb base
    show bullf brr2 at left:
        yalign 0.6 xalign -0.25 zoom 0.80
    with dissolve
    bull "W-What?!"
    show goat handup
    show goatf hapiilves at center:
        xalign 0.47 yalign 4.5 zoom 0.83
    with dissolve
    ref "Ilves gets the win. "
    "Yes!"
    show ilv ow
    hide ilveye
    with dissolve
    cat "Wha-?!"
    with hpunch
    hide bullf
    show bulleye rightdown at left:
        yalign 0.6 xalign -0.25 zoom 0.80
    show rol belly2
    show ilv owcry
    hide ilveye
    with dissolve
    cat "N-NOO!"
    "Ilves is tearing up for some reason?!"
    show ilv base
    show ilveye shut2 at right:
        yalign -3.0 xalign 1.2 zoom 0.88
    with dissolve
    cat "This isn't how a warrior wins! "
    show ilvf noo2 at right:
        yalign -3.0 xalign 1.2 zoom 0.88
    show ilveye shut at right:
        yalign -3.0 xalign 1.2 zoom 0.88
    with dissolve
    cat "A battle only ends when one side's broken or surrenders!"
    show ilv close
    show ilveye shut at right:
        yalign -3.0 xalign 1.2 zoom 0.88
    hide ilvf
    with dissolve
    cat "I can't accept this!"
    window hide
    pause 0.2
    show goat handdownsurprise
    hide goatf
    hide goateye
    play sound "audio/soundFX/Dun.wav" volume 0.5

    with hpunch
    pause 0.8
    window show
    ref "WHAT?!"
    "He's too stubborn for his own good!"
    show bullb base
    show bullf grin behind bulleye at left:
        yalign 0.6 xalign -0.25 zoom 0.80
    show bulleye frank
    show bullb hips
    with dissolve
    bull "Hah! If he won't protest this imaginary \"foul\" which led to the stoppage..."
    show bullb knuckles
    show bulleye frank2
    with dissolve
    with hpunch
    bull "{size=+6}Then it's a no-contest! "
    show bullb crack
    show bulleye closed at left:
        yalign 0.6 xalign -0.25 zoom 0.80
    with dissolve
    bull "Those are the rules!"
    show ilv rub
    hide ilvf
    hide ilveye
    with dissolve
    "Ilves desperately rubs his eyes, trying to regain his eyesight! "
    cat "Wait, wait, wait..."
    cat "I'll be in fighting shape soon, just give me a second!"
    #pickup
    show rol closed
    show rolf belly
    with dissolve
    rolf "..."
    window hide

    show ilvescarry with fade
    play sound "audio/soundFX/Get.mp3"
    show blackshake at truecenter zorder -100
    with vpunch
    pause 0.3
    play sound "audio/soundFX/FX6/220018__chocktaw__fiji-meow-02.wav" volume 1.0

    window show
    cat "Meow?"
    rolf "Easy, now..."
    rolf "You're just making those eyes worse. "
    cat "B-But... "
    cat "The enemy is still standing!"
    show ilvescarrylookdown with dissolve
    rolf "Have a rest and leave it to your fellow soldier!"
    cat "Fellow soldie-"
    window hide
    pause 0.2

    play sound "audio/soundFX/FX2/tada2.wav" volume 0.8
    show ilvescarry2 with dissolve
    pause 0.3
    window show
    #Military sound
    cat "Aye, aye!"
    #"Wha- That nugget of information sure changed his mind quick!"
    cat "I'll be better soon! And we'll switch when you need me, brother!"
    hide ilvescarrylookdown with dissolve
    rolf "Understood."
    "... These military men are something else."
    window hide
    show black with dissolve
    window show
    "Rolf moves Ilves over to the stands."
    window hide
    hide rolf
    hide rol
    hide ilv
    show bulleye right
    show bullf
    hide bullf
    hide black
    hide ilvescarry
    hide ilvescarry2
    hide ilvescarrylookdown
    play music "audio/MPP_-_Brewing_Tension_Pre-Fight_VERSE.mp3" loop  fadein 2.6 volume 0.13
    show goat handdown at center:
        xalign 0.47 yalign 4.5 zoom 0.83
    show bullb base  at left:
        yalign 0.6 xalign -0.25 zoom 0.80
    show bullb hips
    with fade
    pause 0.3
    show rolf base behind goat at right:
        zoom 0.85 yalign 1.0 xalign 1.1
    show rol angerpoint2 behind goat at right:
        zoom 0.85 yalign 1.0 xalign 1.1
    with easeinright
    pause 0.3
    show rol angerpoint
    show rolf point2
    show bulleye right2
    show bullf done2 behind bulleye at left:
        yalign 0.6 xalign -0.25 zoom 0.80
    with dissolve

    window show

    rolf "{size=+6}I'LL FIGHT YOU! "
    with hpunch
    show rol angerscreamnotnude
    with dissolve
    rolf "{size=+6}As Ilves' replacement!"
    #with hpunch
    show bullb base
    show bullf bullshit at left:
        yalign 0.6 xalign -0.25 zoom 0.80
    hide bulleye
    with dissolve
    bull "!"
    show goat think at center:
        xalign 0.47 yalign 4.5 zoom 0.83
    show goatf thinkhard at center:
        xalign 0.47 yalign 4.5 zoom 0.83
    with dissolve

    ref "Hmmm... Let me think."
    show bullb crack
    show bullf done behind bulleye
    show bulleye ugh2 at left:
        yalign 0.6 xalign -0.25 zoom 0.80
    with dissolve
    bull "A bit old for a scrap, aren't ya, granpa?"
    show rolf knucklez
    show rol angerpoint
    with dissolve
    rolf "... I'd beat the shit out of you with my hands tied behind my back."
    show bullf bullshit2
    hide bulleye
    show bullb base
    with dissolve
    bull "!"
    show bullb knuckle
    show bullf bullshit2
    with dissolve
    bull "Well- I'd beat the shit out of YOU with my hands AND FEET tied behind MY back!"
    show goat handdown
    show goatf scream at center:
        xalign 0.47 yalign 4.5 zoom 0.83
    hide goateye
    with dissolve
    show blackshake at truecenter zorder -100
    with vpunch
    ref "Would you two shut up already and let me figure this out?!"
    window hide
    hide bullf
    hide bulleye
    show bulleye frank at left:
        yalign 0.6 xalign -0.25 zoom 0.80
    show bullb hips
    show rolf base
    show rol angerfrank
    with dissolve
    pause 0.3
    window show
    "For such a small guy he's doing a good job keeping the big boys in check..."
    show goat think
    show goatf think
    with dissolve


    ref "... Damn it."
    show goatf thinkhard
    show goateye right at center:
        xalign 0.47 yalign 4.5 zoom 0.83
    with dissolve
    ref "If Ilves won't accept the disqualification win, we'll end up with a no-contest..."
    ref "Stopping either fighter from moving on in the tournament bracket. "
    show goatf think
    show goat handdown
    hide goateye
    with dissolve
    ref "... What a messy situation."
    #Lower score
    show goat thumbs
    show goatf sad1

    with dissolve
    #Slight cry
    ref "{alpha=*0.80}{size=-4}... And I feel so bad for the lil' guy... {/alpha}{/size}"

    ref "{alpha=*0.80}{size=-4}He's so polite and came into the tournament all excited... "
    #Small smile
    show goatf sad2 with dissolve
    ref "{alpha=*0.80}{size=-4}He even painted me a picture for explaining the rules to him..."
    ref "{alpha=*0.80}{size=-4}I'd really like to see him continue, but he's just so stubborn!"
    ref "{alpha=*0.80}{size=-4}{i}*sniffles* {/i}{/alpha}{/size}"
    #^^
    window hide
    show rolf belly
    show rol belly
    with dissolve
    pause 0.5
    window show
    rolf "... So, what do you say? "
    show bullb crack
    show bullf brr behind bulleye at left:
        yalign 0.6 xalign -0.25 zoom 0.80
    hide bulleye
    with dissolve
    bull "Just give ME the win already. "

    bull"It was clearly a punch and not a poke!"

    show goat handdown
    hide goatf
    show goateye left at center:
        xalign 0.47 yalign 4.5 zoom 0.83
    with dissolve
    ref "Tell you what-"
    show goatf think behind goateye at center:
        xalign 0.47 yalign 4.5 zoom 0.83
    show goateye right
    show goat think
    with dissolve
    ref "Since you're both {i}sooo{/i} eager to fight, and since neither Ilves nor Alfred had a match prior to this one..."
    show goatf think
    hide goateye
    with dissolve

    ref "I'll let Rolf act as Ilves' replacement for this fight only."
    show goat handup
    show goatf scream
    show goateye ilves2 at center:
        xalign 0.47 yalign 4.5 zoom 0.83
    with dissolve
    with hpunch
    ref "On the condition that if Rolf wins, Ilves ACCEPTS this victory as his own!"
    hide goatf
    show goat handdown
    show goateye right
    with dissolve
    ref "Deal?"
    show bulleye right2 at left:
        yalign 0.6 xalign -0.25 zoom 0.80
    show rolf knucklez
    show rol angerfrank
    with dissolve

    rolf "Deal."
    show goateye ilves2 at center:
        xalign 0.47 yalign 4.5 zoom 0.83
    show goat think
    with dissolve
    ref "Ilves?"
    #PicOfIlvesOnSide
    window hide
    show ilvescrowdbase
    show ilvescrowd swollen
    with fade
    pause 0.3
    window show
    cat "A fellow soldier's victory is my victory!"
    show ilvescrowd swollenhappy with dissolve
    cat  "Deal!"
    window hide
    hide ilvescrowdbase
    hide ilvescrowd
    with fade
    pause 0.3
    hide goateye
    show goatf think at center:
        xalign 0.47 yalign 4.5 zoom 0.83
    with dissolve
    show bulleye frank at left:
        yalign 0.6 xalign -0.25 zoom 0.80
    with dissolve
    pause 0.3
    window show
    ref "Then it's settled."
    with hpunch
    show bullb iwin
    show bullf grin
    show bulleye frank2
    with dissolve
    bull "And what about when {size=+3}I{/size} win?"
    hide goatf
    show goateye left at center:
        xalign 0.47 yalign 4.5 zoom 0.83
    show goat think
    with dissolve
    ref "I'll count it as you winning this first match, and you'll move on in the tournament bracket."
    show bullb hips
    hide bullf
    show bulleye closed
    with dissolve
    bull "Hmm-"
    window hide
    pause 0.1
    play sound "audio/soundFX/Get.mp3" volume 0.2
    show rolf armoroff

    show rol meangrin at right:
        zoom 0.85 yalign 1.0 xalign 1.1
    with dissolve
    show bulleye right2
    show goateye right
    with dissolve
    pause 0.3
    window show
    rolf "Then what are we waiting for?"

    "Rolf starts unbuckling his armor."
    window hide
    $ renpy.music.set_volume(0.80, delay=0, channel='music')
    pause 0.1
    $ renpy.music.set_volume(0.60, delay=0, channel='music')
    pause 0.1
    $ renpy.music.set_volume(0.30, delay=0, channel='music')
    pause 0.1
    $ renpy.music.set_volume(0.15, delay=0, channel='music')
    pause 0.1
    $ renpy.music.set_volume(0.00, delay=0, channel='music')
    show rolfarm with fade
    play sound "audio/soundFX/FX3/trip-on.wav" volume 0.3
    show blackshake at truecenter zorder -100
    with vpunch
    pause 0.8
    play sound "audio/soundFX/FX2/pig-scream-loud-oink.wav"
    window show
    rolf "I'M READY TO GO WHEN YOU ARE!"
    #ROAR
    bull "!!"
    "Look at those scars! "
    #show crowdbronbase
    #show crowdemelon
    #with dissolve
    $ renpy.music.set_volume(0.15, delay=0, channel='music')
    pause 0.1
    $ renpy.music.set_volume(0.30, delay=0, channel='music')
    pause 0.1
    $ renpy.music.set_volume(0.50, delay=0, channel='music')
    pause 0.1
    $ renpy.music.set_volume(0.60, delay=0, channel='music')
    pause 0.1
    $ renpy.music.set_volume(0.70, delay=0, channel='music')
    pause 0.1
    $ renpy.music.set_volume(0.80, delay=0, channel='music')
    pause 0.1
#    $ renpy.music.set_volume(1.00, delay=0, channel='music')
#    pause 0.1
    emelie "That poor arm!"
    bron "Dad hates the attention it gets... "
    bron "He must really be pissed to be showing it off in front of this crowd!"
    rolf "Where'd that confidence go now, boy?! "
    rolf "Not used to facing someone your own size, 'that it!?"
    "Rolf's anger is palpable!"
    bull "U-Uuhh..."
    #scene of both
    show blackshake at truecenter zorder -100
    window hide
    hide rolf
    hide rolfarm
    hide rol

    show rolfn base at right behind goat:
        zoom 0.85 yalign 1.2 xalign 1.2
    show rol angerpoint at right:
        zoom 0.85 yalign 1.2 xalign 1.2
    show bullb base
    show goatf nodx behind goateye at center:
        xalign 0.47 yalign 4.5 zoom 0.83
    show bullf brr behind bulleye at left:
        yalign 0.6 xalign -0.25 zoom 0.80
    show bulleye shit at left:
        yalign 0.6 xalign -0.25 zoom 0.80
    with fade
    pause 0.5
    show bulleye shitz with dissolve
    window show
    bull "Y'know..."
    show bullb hips
    with dissolve
    show bullb iwin
#    show bullf grin
#    show bulleye ugh2 at left:
#        yalign 0.6 xalign -0.25 zoom 0.80
    show bulleye right2
    show bullf done
    with dissolve
    bull "I would fight you."
    show bullb poin
    show bulleye shit at left:
        yalign 0.6 xalign -0.25 zoom 0.80
    show bulleye ugh2 at left:
        yalign 0.6 xalign -0.25 zoom 0.80
    show bullf grin at left:
        yalign 0.6 xalign -0.25 zoom 0.80
    with dissolve
    bull "BUT-"
    show rolfn knuckles
    show rol angerpoint2
    with dissolve
    rolf "What?!"
    show bullb poin
    show bullb hips
    show bulleye closed
    with dissolve
    bull "Each fighter needs a cutman in a sanctioned bout." # Grin
    window hide
    play sound "audio/soundFX/FX3/clean-record-scratch.wav" volume 0.4

    $ renpy.music.set_volume(0.70, delay=0, channel='music')
    pause 0.1
    $ renpy.music.set_volume(0.60, delay=0, channel='music')
    pause 0.1
    $ renpy.music.set_volume(0.30, delay=0, channel='music')
    pause 0.1
    $ renpy.music.set_volume(0.15, delay=0, channel='music')
    pause 0.1
    $ renpy.music.set_volume(0.00, delay=0, channel='music')

    show goat dafak
    hide goateye
    hide goatf
    show rol angerfrank
    with dissolve
    show blackshake at truecenter zorder -100
    with vpunch
    pause 0.5
    window show
    ref "!"
    "Frank looks taken aback!"

    #$ renpy.music.set_volume(0.80, delay=0, channel='music')
    show goat thumbsz with dissolve
    ref "{alpha=*0.80}{size=-4}...R-Right..."
    ref "{alpha=*0.75}{size=-6}... I absolutely remembered that."
    window hide


    show crowdbronbase
    if modest == True:
        show crowdemesuit
    else:
        show crowdemelon
    show crowdbron fistup
    show crowdem pout
    with fade
    show blackshake at truecenter zorder -100

    with vpunch
    $ renpy.music.set_volume(0.15, delay=0, channel='music')
    pause 0.1
    $ renpy.music.set_volume(0.20, delay=0, channel='music')
    pause 0.1
    $ renpy.music.set_volume(0.25, delay=0, channel='music')
    pause 0.1
    $ renpy.music.set_volume(0.30, delay=0, channel='music')
    pause 0.1
    $ renpy.music.set_volume(0.50, delay=0, channel='music')
    pause 0.1
    pause 0.3
    window show
    bron "I've got ya, pops! "
    show crowdbron fistdown
    show crowdb angry2
    with dissolve
    bron "'Be right down- "
    bron "Let's fuck him up!"
    window hide
    hide crowdbronbase
    hide crowdemelon
    hide crowdemesuit
    hide crowdbouth
    hide crowdb
    hide crowdem pout
    hide crowdbron

    with fade
    show goatf alf at center:
        xalign 0.47 yalign 4.5 zoom 0.83
    with dissolve
    pause 0.1
    show bullf dark2
    show bullb base
    hide bulleye
    with dissolve
    pause 0.5

    window show
    bull "..."
    "The bull grins wickedly!"
    window hide
    $ renpy.music.set_volume(0.40, delay=0, channel='music')
    pause 0.1
    $ renpy.music.set_volume(0.35, delay=0, channel='music')
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
    show bullb knuckles
    with dissolve
    play sound "audio/soundFX/Dun.wav" volume 0.3
    with hpunch
    window show
    bull "{size=+4}CUT...{/size}"
    window hide
    show bullb crack
    show bullf dark3
    with dissolve
    play sound "audio/soundFX/Dun.wav" volume 0.8
    show blackshake at truecenter zorder -100
    with vpunch
    window show
    bull "{size=+14}{i}MAN!{/size}"
    bull "Sorry, honey. But you don't qualify!"
    show bullb hips
    show bullf dark2
    with dissolve
    #$ renpy.music.set_volume(1.00, delay=0, channel='music')
    bull "So just stay over there and keep looking pretty, ok?"
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
    with fade
    pause 0.3
    $ renpy.music.set_volume(0.15, delay=0, channel='music')
    pause 0.1
    $ renpy.music.set_volume(0.30, delay=0, channel='music')
    pause 0.1
    $ renpy.music.set_volume(0.60, delay=0, channel='music')
    pause 0.1
    $ renpy.music.set_volume(0.80, delay=0, channel='music')
    pause 0.1
    window show
    bron "Son of a bi-"
    window hide
    with hpunch
    hide crowdbronn rage

    show crowdbron fistup
    show crowdb rage
    with dissolve
    show crowdemlookbron
    hide crowdem pout
    with dissolve
    pause 0.2
    window show
    bron "I'LL BEAT YOU UP MYSELF, FUCKER!"
    #"Emelie jumps in to calm bronwen down!"
    window hide
    pause 0.3
    hide crowdbronbase
    hide crowdemelon
    hide crowdb
    hide crowdemesuit
    hide crowdem
    hide crowdemlookbron
    hide crowdemlookbron
    hide crowdbron
    hide crowdbouth
    show rol fuming at right:
        zoom 0.85 yalign 1.2 xalign 1.2
    with fade
    pause 0.3
    window show
    "Rolf looks absolutely fuming. And now I'm getting pissed, too!"
    show goat handdown
    with dissolve
    ref "Awfully particular about the rules all of a sudden for someone who so willingly skirts them when it suits you, huh?..."
    show goat think
    show goatf think
    show goateye left at center:
        xalign 0.47 yalign 4.5 zoom 0.83
    with dissolve
    ref "And hold on... Where's YOUR cutman? "
    show bullb base
    show bulleye closed at left:
        yalign 0.6 xalign -0.25 zoom 0.80
    hide bullf
    with dissolve
    bull "Glenn."
    $ glenn_name = "Glenn"
    window hide
    play sound "audio/soundFX/runn.wav"
    show vulture baseside at left:
        yalign 0.6 xalign -0.23 zoom 0.80
    with easeinleft
    pause 0.4
    show vulture base with dissolve
    pause 0.3
    window show
    glenn "... H-Hello."
    show bulleye frank
    show bullf grin behind bulleye at left:
        yalign 0.6 xalign -0.25 zoom 0.80
    show bullb hips
    with dissolve
    bull "HE is my cutman. "
    show bullb crack
    show bullf hateglenn at left:
        yalign 0.6 xalign -0.25 zoom 0.80
    hide bulleye
    with dissolve
    bull "Isn't that right?"
    show vulture spookup with dissolve
    "Glenn looks up at Alfred with an uncertain expression."
    glenn "Yes?"
    show bulleye frank
    show bullf grin behind bulleye
    show bullb hips
    show bulleye closed at left:
        yalign 0.6 xalign -0.25 zoom 0.80
    with dissolve
    bull "Good boy. "
    show bullb crack
    show bullf hateglenn
    hide bulleye
    with dissolve
    bull "Now get out of here!"
    window hide

    with hpunch
    show vulture spook with dissolve
    window show

    glenn "Eek!"
    window hide
    play sound "audio/soundFX/run2.wav"
    hide vulture with easeoutleft
    pause 0.3
    hide bullf
    show bulleye frank at left:
        yalign 0.6 xalign -0.25 zoom 0.80
    with dissolve
    pause 0.2
    show goat handdown
    show goatf think
    hide goateye
    with dissolve
    window show
    ref "Well, okay then... "
    hide goatf
    with dissolve
    ref "So..."
    show goatf crowd2 at center:
        xalign 0.47 yalign 4.5 zoom 0.83
    with dissolve
    "Frank looks to the crowd."
    show goat thumbs
    with dissolve
    ref "'Anyone willing to step up?"
    window hide
    $ renpy.music.set_volume(0.70, delay=0, channel='music')
    pause 0.1
    $ renpy.music.set_volume(0.60, delay=0, channel='music')
    pause 0.1
    $ renpy.music.set_volume(0.30, delay=0, channel='music')
    pause 0.1
    $ renpy.music.set_volume(0.15, delay=0, channel='music')
    pause 0.1
    $ renpy.music.set_volume(0.00, delay=0, channel='music')
    play sound "audio/soundFX/FX2/crickets.wav" fadein 3.5 volume 0.1
    show bullb base
    hide bulleye
    show bullf crowd at left:
        yalign 0.6 xalign -0.25 zoom 0.80
    show rolfn base
    show rol crowd
    with dissolve

    pause 3.5 # silence sound
    stop sound fadeout 3.5
    pause 3.5 # silence sound

    window show
    "The crowd is dead silent..."
    window hide
    play music "audio/Seagul.wav" fadein 3.0 volume 0.25
    $ renpy.music.set_volume(0.15, delay=0, channel='music')
    pause 0.1
    $ renpy.music.set_volume(0.30, delay=0, channel='music')
    pause 0.1
    $ renpy.music.set_volume(0.60, delay=0, channel='music')
    pause 0.1
    $ renpy.music.set_volume(0.80, delay=0, channel='music')
    pause 0.1
    $ renpy.music.set_volume(1.00, delay=0, channel='music')

    show bullf grin at left:
        yalign 0.6 xalign -0.25 zoom 0.80
    show bullb hips
    show bulleye right3b at left:
        yalign 0.6 xalign -0.25 zoom 0.80
    with dissolve
    with hpunch
    show goateye left2 at center:
        xalign 0.47 yalign 4.5 zoom 0.83
    show goatf think
    with dissolve
    window show
    bull "Hah! "
    bull "Not the most popular guy, are you? "
    show rol pout2
    show rolfn knuckles
    show roleye franky at right:
        zoom 0.85 yalign 1.2 xalign 1.2
    with dissolve
    rolf "Hmpf!-"
    pause 0.1
    "Come to think of it... "
    "I remember when Rolf and I were walking out of the city."
    "Nobody stopped to greet him, and most people just looked sort of afraid as he passed by..."
    show bullf dark2
    show bulleye right4 at left:
        yalign 0.6 xalign -0.25 zoom 0.80
    show bullb base
    with dissolve
    "Alfred's awful smile gets wider and wider."
    #bull " 'You leave those friends back in the war? "
    bull "{cps=*0.2} {size=+5}Did the poor old man lose all those buddies back in the war?{/cps}"
    window hide
    hide rol
    hide roleye
    show rolfn sad2
    with dissolve
    show goateye rightsad with dissolve
    pause 0.5
    window show
    rolf " ..."
    "Rolf's anger dissipates."
    window hide
    show crowdbronbase
    show crowdbron fistdown
    show crowdb sad

    if modest == True:
        show crowdemesuit
    else:
        show crowdemelon
    show crowdem sad
    with fade
    pause 0.3
    window show
    bron "D-Dad..."
    emelie "..."
    "Bronwen and Emelie look really sad."
    window hide
    hide crowdbronbase
    hide crowdbronn
    hide crowdbron
    hide crowdem
    hide crowdb
    hide crowdemesuit
    hide crowdemelon
    show bullf dark3
    hide bulleye
    show bullf darklaugh at left:
        yalign 0.6 xalign -0.25 zoom 0.80
    show bullb hips
    with fade
    show blackshake at truecenter zorder -100
    with vpunch
    window show
    bull "KHAHAHA!"
    "Alfred lets out a vile laugh."
    "And as his confidence grows..."
    "So does my anger!"
    window hide


    show handup1 with fade
    stop music
    play sound "audio/soundFX/Dun.wav" volume 0.7
    show blackshake at truecenter zorder -100
    with vpunch
    pause 1.1
    play music "audio/Seagul.wav" fadein 6.0 volume 0.2
    pause 0.5
    window show
    me "{size=+6}I'll be Rolf's cutman!"
    play sound "audio/soundFX/Crowd/suddengasp.wav"  volume 0.3
    "Everyone's eyes turn to me!"
    window hide
    show handup2 with dissolve
    $ renpy.music.set_volume(0.10, delay=0, channel='music')
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
    pause 1.2
    window show
    #play sound "audio/soundFX/FX6/103428__confusion_music__bull-6-c.wav"  volume 0.5
    bull "MOO!?"
    rolf "?!"
    ref "Yesss!"
    bull "And who the fuck are YOU?!"
    me "I'm the princes-"
    "Oh shit, I almost just told him I'm the princess' assistant- "
    "Which would give Emelie's identity away!"
    window hide
    hide handup1
    hide handup2
    show rol surprise at right:
        zoom 0.85 yalign 1.2 xalign 1.2
    show rolfn base
    show bullb base
    show goat fyeah2
    hide goatf
    hide goateye
    show bullf openeyes2
    with fade
    play music "audio/MPP_-_Brewing_Tension_Pre-Fight_FINAL_2.mp3"  noloop fadein 2.0 volume 0.13
    queue music "audio/MPP_-_Brewing_Tension_Pre-Fight_VERSE.mp3" loop  fadein 2.0 volume 0.13


    show bullb knuckle
    show bullf rage
    with dissolve
    with hpunch
    show goateye left2 at center:
        xalign 0.47 yalign 4.5 zoom 0.83
    with dissolve
    window show

    bull "Well?! Who are you??"
    window hide
    menu:
        with dissolve


        "I'm [Protagonist], a hard-working farmer!":
            window show
            me "I'm [Protagonist], a hard-working farmer!"
            show bullb crack
            show bullf baa
            with dissolve
            bull "Oh, so it's YOUR nasty fuckin' wares I've been carrying around day in and day out?! "
            window hide
            show blackopacity
            with dissolve
            show bullflash
            with dissolve
            pause 0.4
            window show
            "Oh right, I recognize him from when I first entered the gates! He was carrying boxes of produce!"
            "Is this piece of shit insulting my profession now, too?!"
            window hide
            hide bullflash
            with dissolve
            hide blackopacity
            with dissolve
            window show
            me "There's nothing wrong with my veggies... Unless your stench rubbed off on them!"

            show rolfn pant
            show rol surprisen
            with dissolve
            rolf "HAH!"
            show bullb crack
            show bullf done behind bulleye
            show bulleye ugh2z at left:
                yalign 0.6 xalign -0.25 zoom 0.80
            with dissolve

            bull "Well, then..."

        "I'm [lie_name], a Hog Haven guard!" if liename == True:
            window show
            me "I'm [lie_name], a Hog Haven guard!"
            show bullf surprise
            show bullb base
            with dissolve
            bull "R-Really?"
            show bullf done2
            show bullb hips
            with dissolve
            bull "... I shouldn't be surprised..."
            show bulleye right2 at left:
                yalign 0.6 xalign -0.25 zoom 0.80
            show bullf done
            with dissolve
            bull "The Hog Haven guard is a complete fucking joke these days..."
            show rol angerpoint
            show rolfn pointup
            with dissolve
            rolf "Watch it. "
            rolf "Every single one of my men would give you a beating!"
            show bulleye right3b
            show bullf offended
            show bullb knuckles
            with dissolve
            bull "I'd like to see them try! "
            show bullf bullshit
            hide bulleye
            with dissolve
            bull "I'm the STRONGEST man in the whole KINGDOM!"
            me "I doubt it. You ducked the whole heavyweight bracket, coward!"
            hide bulleye
            show bullf done2
            with dissolve
            show rolfn knuckles
            show rol surprisen
            with dissolve
            rolf "HAH!"
            show bullb crack
            show bullf done behind bulleye
            show bulleye ugh2z at left:
                yalign 0.6 xalign -0.25 zoom 0.80
            with dissolve
            bull "Well, then..."

        "I'm Rolf's friend!":
            window show
            me "I'm Rolf's friend!"
            show rol surprisez
            show rolfn basehigh
            with dissolve
            with hpunch
            rolf "!?"
            show bullf aww
            show bullb hips
            with dissolve
            bull "Aww, isn't that cute- "
            show bullf awwz with dissolve
            bull "'This guy a new member of your little crew of dimwits? Helmed by that fat idiot Billy?"
            with hpunch
            me "Billy is my bestie, and he'd easily beat the crap out of you, too! "
            show bullf done2
            with dissolve
            me "But I bet you'd try to hide behind some stupid rule to avoid fighting HIM as well... Or anyone who's even half your own size!"
            show rolfn knuckles
            show rol surprisen
            with dissolve
            rolf "HAH!"
            show bullb crack
            show bullf done behind bulleye
            show bulleye ugh2z at left:
                yalign 0.6 xalign -0.25 zoom 0.80
            with dissolve
            bull "Well, then..."



        "That's none of your business, fuckhead!":
            window show
            me "That's none of your business, fuckhead!"
            show bullf offended
            show bullb base
            with dissolve
            with hpunch
            bull "!!"
            show rolfn knuckles
            show rol surprisen
            with dissolve
            rolf "HAH!"
            show bullf done2
            show bullb hips
            with dissolve

            bull "Grrr!- You don't look like you're worth giving a shit about anyways!"
            show bullb crack
            show bullf done behind bulleye
            show bulleye ugh2z at left:
                yalign 0.6 xalign -0.25 zoom 0.80
            with dissolve
            bull "So..."



    show bullb base
    show bulleye ugh2 at left:
        yalign 0.6 xalign -0.25 zoom 0.80
    show bullf brr behind bulleye at left:
        yalign 0.6 xalign -0.25 zoom 0.80
    with dissolve
    bull "I guess the fight is on, granpa."
    show rol meangrin at right:
        zoom 0.85 yalign 1.2 xalign 1.2
    with dissolve
    show blackshake at truecenter zorder -100
    with vpunch
    show goat handup
    show goatf crowd2 at center:
        xalign 0.47 yalign 4.5 zoom 0.83
    hide goateye
    with dissolve
    #ref " Then it's official!!"
    ref "Then the contest's official!"
    "Oh crap, what did I just sign on to do again??"
    show goat think
    show goatf thinkhard at center:
        xalign 0.47 yalign 4.5 zoom 0.83
    with dissolve
    ref "Now, step back and get ready! The fight begins in just a moment!"
    window hide
    play sound  "audio/soundFX/run2r.wav" volume 0.7
    hide rolfn
    hide rol
    with easeoutright
    play audio  "audio/soundFX/run2r.wav" volume 0.7
    hide bullb
    hide bullf
    hide bulleye
    with easeoutleft
    window show
    "Rolf and Alfred walk to their respective sides of the pit."
    show goat handdown
    show goateye me at center:
        xalign 0.47 yalign 4.5 zoom 0.83
    show goatf crowd
    with dissolve
    stop music fadeout 2.0
    queue music "audio/Seagul.wav" fadein 2.0 volume 0.25
    ref "[Protagonist], come with me for a moment..."
    window hide
    hide goat
    hide goatf
    hide goateye
    with dissolve
    pause 0.2
    show goatbg base2 with dissolve
    pause 0.3
    window show
    "I follow Frank as he walks back to the bell."
    window hide

label goattalk:
    scene goatclosebase with fade
    show blackshake at truecenter zorder -100
    show goatclosebase:

        linear 0.4 zoom 1.03 yalign 1.0 xalign 1.0
    pause 0.4
    show goatclosebase:
        zoom 1.03 yalign 1.0 xalign 1.0
    show goatclosef grin:

        zoom 1.03 yalign 1.0 xalign 1.0
    with dissolve
    window show
    ref "Glad ya stepped up."
    ref "'Would've done so myself if I could, but I can't serve as referee and cutman at the same time."
    me "I was getting heated and my hand moved on its own!"
    show goatclosef grump with dissolve
    ref "Understandable. "
    ref "'Used to be a fighter myself back in the day and just can't stand cheaters."
#    ref " Anyways, It's not my position to make assumptions about your credentials or anything..."
    #ref "But I figure you may need a quick rundown in the event that you're needed."
    #me " Sounds good."
    show goatclosef cred with dissolve
    ref "Anyways, It's not my position to make assumptions about your credentials or anything..."
    ref "{alpha=*0.80}{size=-4}I'm sure you're qualified-"
    play music "audio/MPP_-_Fight_Loopround.mp3" fadein 0.0 volume 0.17
    show goatclosef grinz with dissolve
    ref "But I still figure you could use a rundown of the basic fight rules in the Pig Pit!"
    window hide
    scene rulesign
    show blackshake at truecenter zorder -100
    show rulesignnr2
    with fade
    pause 0.3
    window show
    ref "So!"
    window hide
    show rulesignpoint:
        ypos -130
    with dissolve
    window show
    ref "A fight is TWO rounds, with each being two minutes long."
    me "That's short."
    ref "Y-Yeah... Pigs hate cardio."
    ref "There's a minute break between each round!"
    window hide
    show rulesignpoint:

        linear 0.3 ypos -30
    pause 0.4
    window show
    ref"There's no clawing, biting, or horn-skewering allowed. "
    ref "Ilves did a great job controlling his claws when applying his choke earlier."
    ref "Lynxes have big claws and can easily rip through someone's neck!"
    window hide
    show rulesignpoint:

        linear 0.3 ypos 140 xpos -20
    pause 0.4
    window show
    ref"Eye gouging and groin strikes are also big no-no's. "
    window hide
    show rulesignpoint:

        linear 0.3 ypos 280 xpos -30
    pause 0.4
    window show
    ref"I'll be the one deciding the winner if a fight goes to a decision. I'm scoring the action throughout."
    ref"If a fighter gets KO'd, severely hurt, or submits- I'll end the fight. "
    window hide
    show rulesignpoint:

        linear 0.3 ypos 480 xpos -40
    pause 0.4
    window show
    ref"Lastly, you can't leave the raised edge of the pit at any time during the fight-\n Or you're IMMEDIATELY disqualified! "
    me "I see, I see!"
    window hide
    hide rulesignpoint with dissolve
    pause 0.2
    #LIsts them
    scene goatclosebase:
        zoom 1.03 yalign 1.0 xalign 1.0
    show blackshake at truecenter zorder -100
    with fade
    pause 0.3
    window show
    ref "There's a big ol' book with ALL the rules written down in it, but it's rarely used. "
    show goatclosef cred:
        zoom 1.03 yalign 1.0 xalign 1.0
    with dissolve
    ref "Seems Mr.Cheater over there has them all memorized... "
    ref "So he can skirt them to his benefit!"
    show goatclosef ugh with dissolve
    ref "Ugh."
    show goatclosef sigh with dissolve
    ref "I honestly forgot all about the need for a cutman ... "
    ref "Pigs specialize in wrestling, so cutmen aren't needed most of the time."
    show goatclosef cred with dissolve
    ref "But who knows what might happen with this guy."
    show goatclosef bigeye with dissolve
    ref "So, are ya really up to this? Not sensitive to bloody wounds or anything, I hope?"
    window hide
    menu:
        with dissolve


        "Don't worry, I'm not squeamish. \n{size=+2}I've got this!{/size}":
            window show
            me "Don't worry, I'm not squeamish. I've got this!"
            show goatclosef grinz with dissolve
            ref "Faantastic!"
            show goatclosef sweat with dissolve

        with dissolve
        "I am kinda sensitive to blood, actually... \n{size=+2}But I'll do my best!{/size} \n{alpha=*0.8}{size=-5}{i}* Censors some blood in the Pig Pit. *{/i}{/size}{/alpha} ":
            window show
            $ bloodcensor = True
            me "I am kinda sensitive to blood, actually... But I'll do my best!"
            show goatclosef sweat with dissolve
            ref "No worries, that's normal!"
            ref "Just squint really hard if anything happens and you'll be fine!"
            show goatclosef basic with dissolve


    #ref " So, you got any other questions before I give you the cutman rundown?"

    #window hide
    #menu:
    #    with dissolve


        #"Can you explain how the tournament is proceeding again? If Rolf wins, will Ilves move on in the tournament bracket?":
            #window show
            #me "Can you explain how the tournament is proceeding again? If Rolf wins, will Ilves move on in the tournament bracket?"
            #ref " Yes.  And he would've won had he just taken the damn disqualification win earlier. Ugh."
            #ref " So I thought I'd let Rolf step in as a replacement. Replacements arent unheard of in high stakes tournaments, but they usually have to sign up alongside the main fighter, and then if the main fighter pulls out due to injury or whatever else, the replacement is in."
            #ref " A replacement can never replace a fighter after the fighter has had their first match... So this isn't really by the books..."
            #ref " But since it's the first fight of the tournament and Ilves was eligeble for the win anyways... I figure this will work. "
            #ref " If Rolf wins I'll put it down as Ilves accepting his DQ win. Which is fair! And if Ilves eyes get better he can continue in the upcoming matches."
            #ref " If Alfred wins though... I'll write it down as him winning against Rolf acting as Ilves assistant... And Ilves is out of the tournament."

        #" Is there a losers bracket for the fighters who lose? Can they still win? What normally happens during no contest fights?":
            #window show
            #me " Is there a losers bracket for the fighters who lose? Can they still win? What normally happens during no contest fights?"
            #ref " The fight pits is a 1 day tournament, and like most 1 day fighting tournaments, there is no losers bracket, since if a fighter loses by KO for example, having them pressured to fight in the losers bracket would be questionable."
            #ref " With no contests we usually just pit the fighters up against eachother again if they can both still fight. If not, the one who CAN fight moves forward."
            #ref " With the current situation though, that would lead Alfred to moving forward, since the rematch can't happen right away due to Ilves' eyes."
            #ref " Which would really suck, because it would mean Alfred would be pushed forward in the tournament for cheating..."




        #" Tell me about yourself.":
        #    window show
        #    ref "... This isn't really the time, but I'll give it to ya quick!"
        #    ref " I'm in my fourties and was part of the war effort as a weapons trainer."
        #    ref "Over many years I prepared others for battle, without ever truly seeing it myself."
        #    ref " So when the war ended I felt like I had to prove to myself that I could walk the walk as a fighter myself.. "
        #    ref " So I fought in martial-arts tournaments all over the world. 'Won a few prizes, but never got to the very top. "
        #    "Huh, he seems like a well-traveled fighter much like Ilves! Maybe that's why he thought up a way to get him further in the tournament."
        #    ref " I suppose it's strange... Picking up more scars after the war than during it."
        #    ref " But now I'm too old to chase trophies, so I teach martial arts to both the military and to fighters looking to prove themselves in the Pig Pits! "
        #    ref " On days like this I help to organize and ref the tournament. "
        #    me " Thanks for telling me about yourself!"

        #" Can't you just give Ilves the victory even if he won't accept it?":
        #    window show
        #    me " Can't you just give Ilves the victory even if he won't accept it?"
        #    ref " I unfortunately can't. It's just part of Hog Haven culture. "
        #    ref "Being graceful in accepting your defeat is almost as important as winning. "
        #    ref " So this type of situation is very rare, but not unheard of..."


        #" Give me the basics of being a cutman!":
        #    window show
        #    me " Give me the basics of being a cutman!"
        #    ref " Okay... "

    ref "So, to start off... "
    ref "You do know the basics of what a cutman IS, right?"
    window hide
    menu:
        with dissolve


        "I've got a decent idea!":

            show goatclosef grin with dissolve
            window show
            ref "Good!"
            show goatclosef corner with dissolve
            ref "The table over by your corner has your supplies on it."

        "Not really. \n Care to elaborate on why I'm needed?":

            show goatclosef sigh with dissolve
            window show
            ref "Okay..."
            show goatclosef basic with dissolve
            ref "The rules say that a fighter has to be able to intelligently defend themselves AT ALL TIMES! "
            ref "So if an injury occurs that hampers a fighter's ability to do this... "
            show goatclosef bigeye with dissolve
            ref "I will end the fight! "
            ref "Resulting in a loss by technical knockout!"
            show goatclosef grump with dissolve
            ref "Your job as a cutman is to handle injuries in between rounds, so that a fight doesn't have to be stopped."
            show goatclosef corner with dissolve
            ref "Ilves' eyes got swollen back there, so I ended the fight. "
            show goatclosef basic with dissolve
            ref "Letting a fighter go out there without being able to see is a no-go, no matter how willing they are."
            me "I see. But it wasn't ruled a technical knockout with Ilves since his injury was caused by an illegal move?"
            show goatclosef grin with dissolve
            ref "Exactly."
            me "Ok, I understand!"
            show goatclosef corner with dissolve
            ref "The table over by your corner has your supplies on it."



    window hide
    pause 0.2
    show cutkit with fade
    pause 0.9
    window show
    me "I see!"
    ref "You're free to use anything on it that you need."
    window hide
    show goatclosef grump
    hide cutkit
    with fade
    pause 0.2
    play sound "audio/soundFX/Dun.wav" volume 0.5
    show goatclosef grr with dissolve
    with hpunch
    window show

    ref "So, LISTEN CLOSELY!"
    show goatclosef basic with dissolve
    ref "There are TWO common injuries that may happen during a fight that need your attention!"
    ref "Swellings, and cuts!"
    ref "Time is short in between rounds, so you need to know how to prioritize your time!"

    window hide

    show goatfing up1:
        zoom 1.03 yalign 1.0 xalign 1.0
    with dissolve
    pause 0.1
    show goatclosef bigeye with dissolve
    pause 0.3
    window show
label reexplain:
    ref "Swelling is treated by one-"
    window hide
    show cutkit with fade
    show cutkitiron with dissolve
    show cutkitironb with dissolve
    pause 0.3
    window show
    ref "The use of an Eye-Iron. "
    if reexplaincut == False:
        ref "Despite the name, you can use it on any part of the body."
        ref "You basically just grip it by the handle and press it against the affected area for as long as you can."
    if reexplaincut == True:
        ref "You can use it on any part of the body."
        ref "Just grip it by the handle and press it against the affected area for as long as you can."
    window hide
    scene goatclosebase:
        zoom 1.03 yalign 1.0 xalign 1.0
    show blackshake at truecenter zorder -100
    show goatfing up1:
        zoom 1.03 yalign 1.0 xalign 1.0
    if reexplaincut == False:
        show goatclosef bigeye:
            zoom 1.03 yalign 1.0 xalign 1.0
    else:
        show goatclosef ugh:
            zoom 1.03 yalign 1.0 xalign 1.0
    with fade
    pause 0.2
    show goatfing up2:
        zoom 1.03 yalign 1.0 xalign 1.0
    with dissolve
    pause 0.3
    window show
    ref "Then two- "
    window hide
    show cutkit with fade
    show cutkitvaseline with dissolve
    show cutkitvaselineb with dissolve
    pause 0.3
    window show
    ref "You make sure to get some vaseline onto the swollen area so punches slide off it if they're hit again."
    if reexplaincut == False:
        me "Okay, okay. "
    window hide
    scene goatclosebase:
        zoom 1.03 yalign 1.0 xalign 1.0
    show blackshake at truecenter zorder -100
    if reexplaincut == False:
        show goatclosef grump:
            zoom 1.03 yalign 1.0 xalign 1.0
    else:
        show goatclosef ugh:
            zoom 1.03 yalign 1.0 xalign 1.0
    with fade
    pause 0.2
    window show
    if reexplaincut == False:
        ref "Treating a cut on the other hand..."
        show goatclosef bigeye with dissolve
        ref "Has three steps-"
    else:
        ref "Treating a cut has three steps."
    window hide
    show goatfing up1:
        zoom 1.03 yalign 1.0 xalign 1.0
    with dissolve
    pause 0.3
    window show
    ref "One. Swipe away the blood."
    window hide
    show cutkit with fade
    show cutkittowel with dissolve
    show cutkittowelb with dissolve
    pause 0.3
    window show

    ref "You can use the big white towel for that."
    window hide
    scene goatclosebase:
        zoom 1.03 yalign 1.0 xalign 1.0
    show blackshake at truecenter zorder -100
    if reexplaincut == False:
        show goatclosef bigeye:
            zoom 1.03 yalign 1.0 xalign 1.0
    else:
        show goatclosef ugh:
            zoom 1.03 yalign 1.0 xalign 1.0
    show goatfing up1:
        zoom 1.03 yalign 1.0 xalign 1.0
    with fade
    pause 0.2
    show goatfing up2 with dissolve
    pause 0.3
    window show
    ref "Two. If the area is clean but the cut is big and won't stop bleeding- "
    window hide
    show cutkit with fade
    show cutkitswab with dissolve
    show cutkitswabb with dissolve
    pause 0.3
    window show
    ref "Press one of the cotton swabs into the wound."
    if reexplaincut == False:
        ref "They're drenched in a special ointment that constricts the blood vessels. It's good stuff."

    window hide
    scene goatclosebase:
        zoom 1.03 yalign 1.0 xalign 1.0
    show blackshake at truecenter zorder -100
    if reexplaincut == False:
        show goatclosef bigeye:
            zoom 1.03 yalign 1.0 xalign 1.0
    else:
        show goatclosef ugh:
            zoom 1.03 yalign 1.0 xalign 1.0
    show goatfing up2:
        zoom 1.03 yalign 1.0 xalign 1.0
    with fade
    pause 0.2
    show goatfing up3 with dissolve
    pause 0.3
    window show
    ref "Then three- "
    window hide
    show cutkit with fade
    show cutkitvaseline with dissolve
    show cutkitvaselineb with dissolve
    pause 0.3
    window show
    ref "Grab that container of vaseline-"
    ref "And smush some RIGHT INTO the wound! "
    if reexplaincut == False:
        me "Eww."
        ref "It'll help with the bleeding. Trust me. "

    window hide
    hide cutkitvaseline
    hide cutkitvaselineb
    with dissolve
    show cutkitbandage with dissolve
    show cutkitbandageb with dissolve
    pause 0.3
    window show
    ref "Bandages and stuff aren't allowed during the fight, that stuff is for the aftermath. "
    if reexplaincut == False:
        ref "I can't let you send a fighter out all wrapped up in bandages."
        me "Makes sense. "

    window hide
    scene goatclosebase:
        zoom 1.03 yalign 1.0 xalign 1.0
    show blackshake at truecenter zorder -100
    if reexplaincut == False:
        show goatclosef bigeye:
            zoom 1.03 yalign 1.0 xalign 1.0
    else:
        show goatclosef ugh:
            zoom 1.03 yalign 1.0 xalign 1.0
    show goatfing up3:
        zoom 1.03 yalign 1.0 xalign 1.0
    with fade
    pause 0.3
    hide goatfing with dissolve
    if reexplaincut == False:
        hide goatclosef
        with dissolve
    pause 0.3
    window show
    if reexplaincut == False:
        stop music fadeout 2.0
        ref "So... You got all that?"
        window hide
        menu:
            with dissolve


            "Got it, I'm ready!":
                play music "audio/MPP_-_Brewing_Tension_Pre-Fight_FINAL_2.mp3" fadein 0.0 volume 0.13
                window show
                me "Got it, I'm ready!"
                show goatclosef grinz:
                    zoom 1.03 yalign 1.0 xalign 1.0
                with dissolve
                ref "Great! Then let's get this started!"

            "Can explain it to me one more time, please?":
                play music "audio/MPP_-_Brewing_Tension_Pre-Fight_FINAL_2.mp3" fadein 0.0 volume 0.13
                window show
                me "Can explain it to me one more time, please?"
                show goatclosef sigh:
                    zoom 1.03 yalign 1.0 xalign 1.0
                with dissolve
                ref "Fine..."
                with hpunch
                show goatclosef ugh with dissolve
                ref "But pay attention this time!"
                $ reexplaincut = True
                show goatfing up1:
                    zoom 1.03 yalign 1.0 xalign 1.0
                with dissolve
                jump reexplain
    if reexplaincut == True:
        show goatclosef cred:
            zoom 1.03 yalign 1.0 xalign 1.0
        with dissolve
        ref "Hope you got all that, cus the crowd is getting impatient!"
        me "Thanks! I hope so, too..."
        show goatclosef basic:
            zoom 1.03 yalign 1.0 xalign 1.0
        with dissolve
    ref "To your corner, [Protagonist]!"
    window hide
    scene black with fade
    show blackshake at truecenter zorder -100
    pause 0.3
    window show
    "I go to the edge of the pit near Rolf, Emelie & Bronwen. "
    window hide
    scene crowdbronbase
    show blackshake at truecenter zorder -100
    show crowdb angry
    if modest == True:
        show crowdemesuit
    else:
        show crowdemelon
    show crowdbron fistdown
    with fade
    pause 0.3
    window show
    bron "About time."
    if modest == True:
        show crowdemesuit2
        hide crowdemesuit
    else:
        show crowdemelon2
        hide crowdemelon
    with dissolve
    emelie "I'm so nervous!"
    hide crowdb angry with dissolve
    bron "Fuck him up, dad!"
    window hide
    scene bg pits
    show blackshake at truecenter zorder -100
    show bgpits people
    show rounds one
    show goatbg base2

    with fade

    pause 0.1
    hide goatbg base2 with dissolve

    show goat handdown at center:
        xalign 0.47 yalign 4.5 zoom 0.83
    with dissolve
    pause 0.3
    show goatf scream at center:
        xalign 0.47 yalign 4.5 zoom 0.83
    with dissolve
    window show
    ref "Fighters, come to the center!"
    window hide

    show goat handout
    with dissolve
    play audio  "audio/soundFX/run2r.wav" volume 0.7
    show rolfn base at right behind goat:
        zoom 0.85 yalign 1.0 xalign 1.1
    show    rol angerpoint at right behind goat:
        zoom 0.85 yalign 1.0 xalign 1.1
    with easeinright
    play sound  "audio/soundFX/run2r.wav" volume 0.7
    show bullb base at left behind goat:
        yalign 0.6 xalign -0.25 zoom 0.80
    show    bullf brr at left behind goat:
        yalign 0.6 xalign -0.25 zoom 0.80
    show    bulleye right3b at left behind goat:
        yalign 0.6 xalign -0.25 zoom 0.80

    with easeinleft
    hide goatf with dissolve
    pause 0.3
    window show
    ref "Gentlemen, I want a clean fight!"
    show goatf think at center:
        xalign 0.47 yalign 4.5 zoom 0.83
    with dissolve
    ref "If there are no other questions, you can show each other respect before-"
    window hide
    show versus1 with fade

    pause 0.5
    window show
    rolf "This one doesn't know the meaning of the word \" respect \"!"
    bull "'Think a few big scars make you deserving of it? "
    window hide
    show versus2 with dissolve
    pause 0.3
    window show
    bull "That's good. Cus I'll give you new ones!"
    rolf "You can try!"
    window hide


    show versustext
    with dissolve
    show versusbar
    with dissolve
    play sound "audio/soundFX/Dun.wav" volume 0.9
    show blackshake at truecenter zorder -100
    with vpunch
    pause 0.7
    window show
    ref "TO YOUR CORNERS!"
    window hide
    hide versusbar
    hide versustext
    hide versus2
    hide versus1
    show goat handout at center:
        xalign 0.47 yalign 4.5 zoom 0.83
    show rolfn base at right behind goat:
        zoom 0.85 yalign 1.0 xalign 1.1
    show bullb base at left behind goat:
        yalign 0.6 xalign -0.25 zoom 0.80
    with fade
    play sound  "audio/soundFX/run2r.wav" volume 0.7
    hide rolfn
    hide roleye
    hide rol
    with easeoutright
    play audio  "audio/soundFX/run2r.wav" volume 0.7
    hide bullb
    hide bulleye
    hide bullf
    with easeoutleft
    pause 0.3
    show goat handdown at center:
        xalign 0.47 yalign 4.5 zoom 0.83
    with dissolve
    hide goat
    hide goatf
    with dissolve
    show goatbg base2
    with dissolve
    pause 0.3
    window show
    "The fighters each step back to their corners, with Frank moving to the bell-"
    window hide

    show goatbg base with dissolve
    pause 0.2
    window show
    ref "FIGHTERS READY?!"

    window hide
    scene eyeconfront1
    show blackshake at truecenter zorder -100
    show eyeconfront2b
    with fade
    pause 0.5
    window show
    bull "I'm always ready."
    window hide
    show eyeconfront1b with dissolve
    pause 0.3
    window show
    rolf "Let's get this started."
label letsget:
    window hide
    pause 0.2
    scene dong1 with fade
    show blackshake at truecenter zorder -100
    stop music fadeout 0.2
    play sound "audio/soundFX/FX6/singlebell.wav" volume 0.6
    show dong2 with hpunch


    pause 0.3
    window show



    "The bell goes off!"
    window hide
    scene dong1 with dissolve
    show blackshake at truecenter zorder -100
    pause 0.3
    scene black with fade
    show blackshake at truecenter zorder -100
    show crowdgallery0 behind black
    show crowdgallery1 behind black
    show crowdgallery2 behind black
    show crowdgallery3 behind black
    show crowdgallery4 behind black
    show crowdgallery5 behind black
    show crowdgallery6 behind black
    show crowdgallery7 behind black
    show crowdgallery8 behind black






    jump fightstart

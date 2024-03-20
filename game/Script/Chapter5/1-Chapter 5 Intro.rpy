
label ch5:
    "{alpha=*0.90}{size=-3} A comfortable feeling spreads throughout my body and I slowly fall asleep."
    window hide
    pause 1.5
    window show
    "{alpha=*0.80}{size=-4} ..."
    window hide
    pause 0.3
    $ playnormal = True
    play sound "audio/soundFX/Door Slam.wav"
    pause 0.3
    play sound "audio/soundFX/FX3/trip-on.wav" volume 0.45
    scene billywakeup
    show blackshake at truecenter behind billywakeup
    play music "audio/adventures-in-adventureland-by-kevin-macleod-from-filmmusic-io.mp3" fadein 0.1 volume 0.3
    with vpunch
    window show
    billy " BUDDYYY!"
    me " ?!"
    me " Billy what are you-"
    billy " Rise and shiiine!~"
    billy " There's a big beach gathering today! With a lot of fun festivities and snacks!"
    billy " Can we go, [Protagonist]? Pleaaase? "
    billy " It'll be so much fun!"
    me " I guess we can-"
    window hide
    pause 0.2
    play sound "audio/soundFX/Blanket Move.wav"
    show emeliewakeup a1 with dissolve
    pause 0.3
    window show
    emelie " Uuuuughh..."
    show emeliewakeup a2 with dissolve
    emelie " ...What's with all this noise?-"
    show emeliewakeup a3 with dissolve
    emelie "!"
    show emeliewakeup a4 with dissolve
    emelie " Billy... "
    window hide
    show emeliewakeup a5 with dissolve
    play sound "audio/soundFX/Dun.wav" volume 1.0
    with vpunch
    pause 0.2
    window show
    emelie " You can't just barge in like this without knocking!"
    window hide
    play sound "audio/soundFX/Blanket Move.wav"
    show emeliewakeup a7 with dissolve
    pause 0.3
    window show
    emelie " I'm naked!!"
    show billywakeup3 with dissolve
    " Billy suddenly blushes a deep red."
    show billywakeup2 behind billywakeup3 with dissolve
    billy " Oh right- Whoops!"
    billy " I'll give you a moment!"
    window hide
    show bilwakeup1
    show bilwakeup2
    show bilwakeup3
    show bilwakeup4
    scene black
    with fade
    window show
    play sound "audio/soundFX/FX4/clothing3.wav"
    " Emelie quickly throws her lingerie on and we get out of bed."
    window hide
    scene bg emroomday
    show blackshake at truecenter behind bg
    show eml normal at right:
        yalign -0.1
        zoom 0.95
    show billy base at left:
        yalign 0.4 xalign -0.08
    with fade
    pause 0.3
    show eml hips
    show emeye side1 at right:
        yalign -0.1
        zoom 0.95
    with dissolve
    window show
    emelie " Now what's up, Billy?"
    show billy laugh with dissolve
    billy " There's a big beach gathering today!"
    show billy ooo with dissolve
    billy " And a huge ship's come by too! "
    show billy laugh with dissolve
    billy " It's been on a long cruise aaaall across the world!"
    #Maybe the boats can be seen in the distance on the other side of the ocean water near the castle silhouette
    show emf biggersmile behind emeye at right:
        yalign -0.1
        zoom 0.95
    show eml normal
    with dissolve
    emelie " Oh, how fun!! I haven't been to the beach in a long time, we should totally go!"
    hide emeye
    show emf insecure
    with dissolve
    emelie " But I need a new bikini... "
    show emf bigsmile with dissolve
    emelie " And [Protagonist], you'll need some nice swimming trunks!"
    me " Right!"
    show emf normalblush with dissolve
    emelie " You'll also need to pay Bronwen for the plug- "
    window hide
    play sound "audio/soundFX/Dun.wav" volume 0.5
    with vpunch
    show emf panic
    show eml out
    with dissolve
    window show
    emelie " Uuuhh... {i}Thing {/i} you got for me yesterday!"
    show emeye side2 at right:
        yalign -0.1
        zoom 0.95
    show eml normal
    with dissolve
    show billy bellyhapi
    with dissolve
    billy " Oh right! [Protagonist] fixed that golden heart up real good for you! "
    billy " What a wholesome surprise gift, huh? "
    show emf insecure
    show eml proper
    with dissolve
    emelie " V-very wholesome... "
    show billy laugh with dissolve
    billy " HOLE-some, even! Teehee!"
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
    with vpunch
    show eml panic
    show emf panic
    show emear high at right:
        yalign -0.1
        zoom 0.95
    show emf panic2
    show emeye side3
    show emblush at right:
        yalign -0.1
        zoom 0.95
    with dissolve
    window show
    emelie " !!"
    me " Wha-!?"
    " A naughty joke!? From Billy?!"
    " Me and Emelie both tense up and blush bright red."
    show billy wary with dissolve
    billy  " It had made a hole in your dress, no?"
    show billy clench with dissolve
    billy " ... Was my joke that bad? That really killed the mood..."
    show eml out
    show emeye side2
    show emf think
    hide emear
    with dissolve
    emelie " O-oh right!"
    show eml hips
    hide emeye
    show emf laugh
    with dissolve
    $ renpy.music.set_volume(0.20, delay=0, channel='music')
    pause 0.1
    $ renpy.music.set_volume(0.40, delay=0, channel='music')
    pause 0.1
    $ renpy.music.set_volume(0.60, delay=0, channel='music')
    pause 0.1
    $ renpy.music.set_volume(0.80, delay=0, channel='music')
    pause 0.1
    $ renpy.music.set_volume(1.00, delay=0, channel='music')
    emelie " Phuuuhaha!"
    " Me and Emelie both let out a relieved sigh and start chuckling!"
    show billy bellyhapi with dissolve
    billy " Hah! So it did land, just took you two a moment!"
    me " Haha, yeah that was a great one, Billy!"
    " Phew, I thought that hole-pun was related to something else!"
    hide emblush
    hide emf
    show eml normal
    with dissolve
    emelie " A-anyways-"
    window hide
    hide eml with easeoutright
    pause 0.5
    show eml coin at right:
        yalign -0.1
        zoom 0.95
    show emf smile at right:
        yalign -0.1
        zoom 0.95
    with easeinright
    pause 0.3
    window show
    emelie " Here's some money that should cover both Bronwen and the swimsuit!"
    " She hands me the small bag."
    window hide
    show eml normal
    show emf normalblush
    with dissolve
    play sound "audio/soundFX/FX5/CoinBag.wav" volume 1.0
    with vpunch
    pause 0.2
    window show
    emelie " That's filled with gold coins!"
    emelie " One gold is worth a hundred silver!"
    show emf bigsmile
    show eml out
    with dissolve
    emelie " And remember to tip an extra coin or two for good work! "
    show billy wary with dissolve
    billy " Emelie... Is that enough gold for a pair of trunks for me too?"
    " Billy looks worried."
    show billy clench with dissolve
    billy " I'm getting my salary tomorrow and I spent all my money on carrot cake..."
    show emf normal
    show eml hips
    show emeye side1 at right:
        yalign -0.1
        zoom 0.95
    with dissolve
    emelie " Of course, Billy! "
    show emf normalblush
    show eml proper
    with dissolve
    emelie " You know I always tell you to come to me if you're in need of a favor!"
    show billy belly
    show billylaughface at left:
        yalign 0.4 xalign -0.08
    with dissolve
    billy " Yes yes, princess! Thank youu!"
    " Emelie gives Billy a cheerful nod."
    show emf wide
    hide emeye
    with dissolve
    emelie " Now... I've got to get dressed and make sure everything is in order with the city watch!"
    emelie " Since my parents are still on their trip it's up to me to double-check everything! "
    show emf insecure with dissolve
    emelie " I always worry I'll mess something up when they're away... "
    show eml normal
    show emf normalblush
    with dissolve
    emelie " But I should be quick!"
    emelie " Meanwhile, it's up to you two to go get things sorted and bring me a bikini or a swimsuit!"
    hide billylaughface
    show billy thumbup
    with dissolve
    billy " Yes, princess!"
    me " Okay, I'll see you again soon!"
    show eml out
    show emf surprise
    with dissolve
    emelie " And when it comes to my bikini size, just pick one with a slightly larger bust than average! Pig-size!"
    me " That's easy enough to remember!"
    #The bikini ends up being quite small up top later.. maybe em's grown since her last bikini.
    show billy laugh
    with dissolve
    billy " Then let's get going, buddy!"
    me " Yes! Let's go!"
    show eml proper
    show emf biggersmile
    with dissolve
    emelie " Good luck!"
    window hide
    scene black with fade
    window show
    play sound "audio/soundFX/FX4/stairs3.wav" volume 1.0
    " We walk down the stairs. "
    window hide
    scene bg stairs
    show blackshake at truecenter behind bg
    show billy base at left:
        yalign 0.4 xalign -0.08
    with fade
    pause 0.3
    show bill squint at left:
        yalign 0.4 xalign -0.08
    with dissolve
    window show
    billy " Sorry about that up there!"
    billy " When I heard about the beach gathering I knew I had to run and tell my best buddy right away! "
    show bill starsmile
    show billy casualaugh
    with dissolve
    billy "To maximize our time in the sun! "
    #Menu to tell him it's OK or to say he should probably knock next time, since he might walk in on some private stuff...
    me " That's all good, Billy!"
    show billy finger
    show bill casualface
    with dissolve
    billy " Now, I know just the place where we'll find some nice swimming trunks for ourselves and a swimsuit for Emelie!"
    billy " And it's right by Bronwen's shop, too!"
    me "Oh really? Let's go!"
    show bill laughface
    show billy base
    with dissolve
    billy " Yess!"
    window hide
    play sound "audio/soundFX/Run2.wav"
    hide bill
    hide billy
    with easeoutleft
    pause 0.2
    scene black with fade
    window show
    " We walk through the park, over to the shops."
    window hide




    scene tailorsmith with fade
    show blackshake at truecenter behind tailorsmith
    play sound "audio/soundFX/Run.mp3"
    show billy base at left:
        yalign 0.4 xalign -0.08
    with easeinleft
    pause 0.2
    window show
    billy " So, where do you want to go first?"
    me "Hmmm... It's a little earlier than twelve o'clock and Bronwen hates being interrupted."
    me " Let's wait until the clock tower rings and she's on break to deliver the money! "
    show bill laughface at left:
        yalign 0.4 xalign -0.08
    show billy casualaugh
    with dissolve
    billy" Sounds like a plan! "
    billy "Tailor shop first it is! "
label shopping:
    window hide
    stop music fadeout 1.0
    scene black with fade
    window show
    play sound "audio/soundFX/FX2/shop-door-bell.wav" volume 0.5
    " We enter the store."
    window hide
    play music "audio/Tavern+Brawl+-+320bit.mp3" fadein 2.0 volume 0.4
    scene bg tailor
    show blackshake at truecenter behind bg
    show tailorbikini
    show tailorspeedo
    show tailorswimsuit
    show sewmachine
    show sewmeasure
    show sewbottoms
    with fade
    pause 0.8
    window show
    me " ...Hello there!"
    window hide

    play sound "audio/soundFX/Run2.wav"
    show billy base at left with easeinleft:
        yalign 0.4 xalign -0.35
    show billy wary with dissolve
    pause 0.1
    window show
    billy " [Protagonist]... Those are mannequins you're talking to..."
    me " ... I totally knew that."
    show billy clench
    show bill waa at left:
        yalign 0.4 xalign -0.35
    with dissolve
    billy " Ooooo!"
    billy " Look at those trunks! They look great!"
    window hide
    hide tailorspeedo with dissolve
    hide bill
    play sound "audio/soundFX/Get.mp3"
    show billy trunkshold
    with dissolve
    pause 0.3
    show billy trunkshold:
        linear 0.5 yalign 0.4 xalign 0.4
    pause 0.4
    show billy trunkshold2 with dissolve
    window show
    billy " Oh, I just CAN'T WAIT to these on!"
    billy " See ya soon, [Protagonist]!"
    window hide
    play sound "audio/soundFX/Run2.wav"
    hide billy with easeoutright
    pause 0.6
    window show
    maple " W-Woah- Hiya, Billy! "
    " An unfamiliar voice is heard over by the dressing rooms!"
    maple " 'You going to the beach, huh?"
    billy " Yes yes! Me and my best bud!"
    maple " How fun!"
    maple " Tell me if ya need anything, kay?"
    window hide
    play sound "audio/soundFX/Run2.wav"
    show mapc base behind sewmachine at center with easeinright
    pause 0.3
    #show tailorsmoke behind mapc with dissolve
    show maf bigg
    with dissolve
    window show
    maple " And there you are!!"
    " A scantily clad canine around my height shows up!"
    show mapc tid
    show maf opensmile2
    with dissolve
    maple " Billy's best bud, huh?"
    me " That's me! Hello!"
    show maf closeyes
    with dissolve
    maple " Heya! Very nice to meet'cha!"
    $ maple_name = "Maple"
    play sound "audio/soundFX/FX5/ding.wav" volume 0.4
    show maf hapigrin
    show mapc peace
    with dissolve
    maple " I'm Maple!"
    me " And I'm [Protagonist]!"
    show maf lookbod
    show mapc hips
    with dissolve
    maple " Ooh, and would'ya look at those clothes? "
    "She looks me up and down."
    show maf hapuface
    with dissolve
    maple " Puh, they fit you well!"
    "??"
    me " Oh...uhh... Thanks!"
    #;)
    show maf closeyes
    show mapc cheer
    with dissolve
    maple " I made them, in case you weren't aware!"

    show maf biggrin
    with dissolve
    maple " Billy came by to buy them for \" A new friend \" the other day!"
    me " Huh, I didn't know!"
    me " Thank you, they do fit really well!"
    show maf frontystar
    show mapc out
    with dissolve

    maple " Yay! That's great to hear! "
    " Her tail starts wagging!"
    show maf biggrin with dissolve
    maple " I've never made clothes for a human before, you see! "
    show mapc tid
    show maf hapiface
    with dissolve
    maple " So I got really nervous I might've missed something important!"
    maple " It's very rare for me to make pants without a special hole for the tail, for example! Haha!"
    me " Oh!"
    " Huh... I guess it's true that almost everyone else has some sort of tail!"
    me " You didn't miss anything from what I've noticed! "
    show maf biggrintongue
    show mapc hips
    with dissolve
    maple " Good! You don't look too crazy, just sort of handsome."
    show mapc out
    show maf sniff1
    with dissolve
    show maf sniff2 with dissolve
    " She starts sniffing the air. "
    window hide
    show maf sniff1 with dissolve
    show maf sniff2 with dissolve
    show maf sniff1 with dissolve
    show maf sniff2 with dissolve
    show mapc out
    show maf baseface
    with dissolve
    window show
    maple " And you smell really nice!"
    me " Ehhh, thank you!"
    show maf wideeye
    show mapc hips
    with dissolve
    maple " So what are you looking for today, hmm? "

    maple " You going to the beach, yeah?"
    me " Yes! I'm looking for a pair of trunks for myself and a bikini!"
    me " The bikini size I'm looking for is a regular pig-size with a slightly bigger bust!"
    show maf fronty
    show mapc base
    with dissolve
    maple " I see! "
    hide maf
    show mapc thinking
    with dissolve
    maple " Hmm, I've sold most of my beachwear today already!"

    maple " But I still have one bikini and one swimsuit of that size."
    show maf hapuface
    show mapc hips
    with dissolve
    maple " Which style do you like more? Swimsuit or Bikini?"
    me " Hmm... Not entirely sure what the difference is."
    show maf bigg
    show mapc back
    with dissolve
    maple " Oh?"
    show maf closeyes
    with dissolve
    maple " I'd gladly model them for you! So you can make your best choice!"
    me " Oh really? That would be great!"
    show mapc base
    show maf biggrintongue
    with dissolve
    maple " Okay! Let me just pick them off the wall and I'll run off and get changed!"





    #She runs off and comes back in the blue swimsuit."
    window hide
    hide tailorswimsuit
    with dissolve
    play sound "audio/soundFX/Get.mp3"
    show mapc holding
    hide maf
    show mapholdswim behind sewmachine
    with dissolve
    pause 0.4
    window show

    maple " One second!"
    window hide
    play sound "audio/soundFX/Run2.wav"
    hide mapc holding
    hide mapholdswim
    hide maf
    with easeoutright
    pause 0.7
    play sound "audio/soundFX/Run2.wav"
    show mapswimsuit back behind sewmachine
    with easeinright
    pause 0.3
    show maf hapuface with dissolve
    with vpunch
    window show


    maple " This is the swimsuit!"
    " !!"
    show maf opensmile2 with dissolve
    maple " Simple! Modest! Comfortable!"
    me " That's nice!"
    show maf biggrin with dissolve
    maple " And as you can see, it's just one piece of blue fabric to cover both the breasts and crotch!"
    me " Aha!"
    hide maf with dissolve
    maple " Meanwhiiiile."
    window hide
    hide tailorbikini with dissolve
    play sound "audio/soundFX/Get.mp3"
    show mapswimsuit holdmelon behind sewmachine  with dissolve
    pause 0.3
    window show
    maple " Just a sec-"
    window hide
    play sound "audio/soundFX/Run2.wav"
    hide mapswimsuit holdmelon with easeoutright
    pause 0.7
    play sound "audio/soundFX/Run2.wav"
    show mapskinimelon back behind sewmachine with easeinright
    pause 0.3
    show maf closeyes with dissolve
    with vpunch
    window show
    #She runs off and comes back with the bikini."

    maple " This is the bikini!"
    " Woah!"
    show maf biggrin with dissolve
    maple " Daring! Skimpy! Sexy!"
    show maf biggrintongue with dissolve
    maple " Everyone will want to check those \"melons\" out, hihi!"
    " Damn, that doesn't leave much to the imagination!"
    me " Aha!"
    show maf bigg with dissolve
    maple " So the main difference is the amount of fur- or skin that's revealed!"
    maple  " Now just a second and I'll get dressed."
    window hide
    hide maf with dissolve
    play sound "audio/soundFX/Run2.wav"
    hide mapskinimelon with easeoutright
    pause 0.7
    play sound "audio/soundFX/Run2.wav"
    show mapc holding behind sewmachine
    show mapholdboth behind sewmachine
    with easeinright
    window show
    #She runs off and comes back again
label kinichoice:


    maple " So which one are ya leaning toward?"
    window hide
    show blackopacity
    with dissolve
    show swimsuitleft
    show bikiniright
    with dissolve
    window show
    " Hmm... Emelie is the princess of this kingdom. So the more modest one might be good!"
    " But then again... The skimpy bikini is kinda daring and hot..."
    " Emelie will probably go with her hair band today instead of her crown so she shouldn't be recognized by the public!"
    " And all of her outfits so far have been plenty revealing too! She might just really like skimpy clothes!"
    " Ugh, hard decision! I've never really bought clothes before!"
    " Maybe I should just go with the one I like more?"
    #Option to choose
    #Image of both choices appear


    window hide
    show vignette behind swimsuitleft with dissolve
    hide swimsuitleft
    hide bikiniright

    show screen BikiniChoice
    $ disableAFMbutton = True
    $ preferences.afm_enable = False
    $ _skipping = False
    $ renpy.pause(hard=True)

screen BikiniChoice:
    #add "gui/choices/RolfInterrogationUI.png"

    imagebutton:
        style "mainmenunew"
        idle "images/Chapter5/swimsuitleft.png"
        hover "images/Chapter5/swimsuitlefthover.png"
        action Show(screen="ConfirmChoices", YesAction=Jump("bluekini"), Choice="suitleft", NoAction=Show(screen="BikiniChoice"), transition=dissolve)

    imagebutton:
        style "mainmenunew"
        idle "images/Chapter5/bikiniright.png"
        hover "images/Chapter5/bikinirighthover.png"
        action Show(screen="ConfirmChoices", YesAction=Jump("melonkini"), Choice="suitright", NoAction=Show(screen="BikiniChoice"), transition=dissolve)

screen ChoicesuitleftDark:
    add "images/Chapter5/bikinidarkright.png"

screen ChoicesuitrightDark:
    add "images/Chapter5/swimsuitdarkleft.png"

label bluekini:
    hide screen BikiniChoice
    hide screen ChoicebookleftDark
    hide blackopacity
    hide vignette
    with dissolve
    window show
    me " I'll go with the blue swimsuit! "
    show maf biggrin with dissolve
    maple " Great choice!"
    window hide
    play sound "audio/soundFX/Get.mp3"
    show mapc cheer
    hide mapholdboth
    show tailorbikini behind mapc
    with dissolve
    with vpunch
    window show
    $ disableAFMbutton = False
    $ _skipping = True
    $ modest = True
    jump afterswimsuitchoice



label melonkini:
    hide screen BikiniChoice
    hide screen ChoicebookrightDark
    hide blackopacity
    hide vignette
    with dissolve
    window show
    me " I'll go with the melon bikini! "
    show maf biggrin with dissolve
    maple " Great choice!"
    window hide
    play sound "audio/soundFX/Get.mp3"
    show mapc cheer
    hide mapholdboth
    show tailorswimsuit behind mapc
    with dissolve
    with vpunch
    window show
    $ disableAFMbutton = False
    $ _skipping = True
    $ modest = False
    jump afterswimsuitchoice


label afterswimsuitchoice:
    if modest == False:
        " She hands me the bikini!"
    if modest == True:
        " She hands me the swimsuit!"
    show maf hapuface with dissolve
    maple " Now that we have that sorted..."
    show maf lookbod
    show mapc base
    with dissolve
    maple " What size do you need for the trunks?"
    me " Oh, uuh..."
    me " They're for me. But I don't really know my size!"
    show maf wideeye
    show mapc tid
    with dissolve
    maple " Oh! Well, hmm... "


    maple " I can usually eyeball pig-sizes since I do it all day... "
    show mapc thinking
    hide maf
    with dissolve
    maple " But I'm not entirely sure when it comes to you!"
    maple " And swimming trunks are sort of stretchy and stuff."
    me " I see... Do you have a few I could try on maybe?"
    show mapc back
    show maf insecure
    with dissolve
    maple " It seems Billy grabbed the last pair..."
    show mapc proper
    show maf closeyes
    with dissolve
    maple " Tell ya what- I'm actually working on some right now! "
    window hide
    play sound "audio/soundFX/Get.mp3"
    show mapc holding behind sewmachine
    show mapholdtrunks behind sewmachine
    hide sewmeasure
    hide sewbottoms
    show maf biggrin
    with dissolve
    pause 0.5
    window show
    maple " Orange-colored with medium-length legs!"
    show maf bigg with dissolve
    maple " If that sounds OK to you then how about we measure your waist real quick and I'll custom-fit them to ya?"
    me " Yeah, that sounds great! Thank you!"
    show maf lookright with dissolve
    maple " I usually charge extra for this, but... "
    show maf biggrintongue with dissolve

    maple " I gotta serve my first human well!"
    maple " Wouldn't ya agree, hun?~"
    me " -Uuuhh..."
    " ...She's very flirty."
    show maf closeyes with dissolve
    maple " Haha, well then let's get to it! Follow me!"
    window hide
    play sound "audio/soundFX/Run.mp3"
    hide mapc
    hide mapholdtrunks
    hide maf
    with easeoutright
label measurestart:
    if playnormal == False:
        $ maple_name = "Maple"
    scene bg dressingroom
    show blackshake at truecenter behind bg
    show dressroom closed
    with fade
    pause 0.3
    show mapc holding:
        zoom 1.1
    show mapholdtrunks:
        zoom 1.1
    show maf closeyes:
        zoom 1.1
    with easeinleft
    pause 0.3
    show maf baseface with dissolve
    window show
    maple " Now hop on into this room and strip!"
    show maf bigg with dissolve
    maple " Then simply measure your waist!"
    window hide
    play sound "audio/soundFX/FX5/curtain.wav"
    show dressroom openn
    with dissolve
    pause 0.3
    stop music fadeout 1.0
    show black with fade
    window show
    play music "audio/Heartbeat+-+320bit.mp3" volume 0.4
    play sound "audio/soundFX/FX4/clothing3.wav"
    if modest == True:
        " I step inside and put the swimsuit down before removing my clothes."
    if modest == False:
        " I step inside and put the bikini down before removing my clothes."
    window hide
    scene boothbase with fade
    show blackshake at truecenter behind boothbase
    pause 0.5
    window show
    maple " Here's your measuring band!"
    window hide
    play sound "audio/soundFX/FX4/clothing3.wav"
    show maphandmeasure with dissolve
    window show
    me " Thanks!"
    window hide
    play sound "audio/soundFX/FX4/clothing2.wav"

    show maphand
    hide maphandmeasure
    with dissolve
    show measure

    with dissolve
    play sound "audio/soundFX/FX4/clothing2b.wav"
    hide maphand
    hide maphandmeasure
    with dissolve
    pause 0.5
    window show
    me "So... How exactly do I go about this?"
    maple "You kinda just pull it around the section between the... uuhh... buttcheek crease and waist area."
    maple "... I'm not great at explaining things! "
    me " Okay... I might be a... size 21?"
    me " If I'm doing this right."
    maple " A pig-size 21 sounds about right! "
    maple "But if you're uncertain I can check real quick from out here."
    me " Yeah, that might be for the best!"
    window hide
    show maphand behind measure
    with dissolve
    hide measure
    with dissolve
    play sound "audio/soundFX/FX4/clothing3.wav"
    show maphandmeasure
    hide maphand
    with dissolve
    window show
    maple " Okay just stay turned away and I'll measure real quick. "
    hide maphandmeasure with dissolve
    maple "I won't be able to see anything but that cute butt, I promise!"
    window hide
    play sound "audio/soundFX/Get.mp3"
    show boothmaple with dissolve
    pause 0.3
    window show
    "Maple scoots in and I feel her bust smush against my lower leg."
    window hide
    play sound "audio/soundFX/FX4/clothing2.wav"
    show boothmaplehands
    show measure soft
    with dissolve
    pause 0.3
    window show

    "She wraps the measuring tape around my waist and butt."
    " The strap is placed a fair bit lower than when I measured, and it softly presses against my member."
    window hide
    show mebex down with dissolve
    pause 0.3
    window show
    maple " Okay, soooo... "
    maple "That's a pig-size 22!"
    window hide
    show mebex up with dissolve
    pause 0.3
    window show
    maple " You probably measured a little higher up your waist! "
    maple "Very close, good job!"
    "Her bust pressing against my leg makes my cock swell! "
    window hide
    play sound "audio/soundFX/FX4/clothing2.wav" volume 0.8
    show dick medium behind measure
    show measure mediumslideb
    with dissolve
    show mebex ohdown behind measure
    with dissolve
    pause 0.3
    window show
    maple " No- wait up! "
    " The measuring band slid up along my dick!"
    maple  "A size 23!"
    me " Uuuhhh..."
    show mebex happyclosed behind measure , boothmaplehands with dissolve
    maple " Let me wrap this around again just in case!"
    window hide
    play sound "audio/soundFX/FX4/clothing2b.wav"
    show measure medium1
    show mebex hmmdown
    with dissolve
    pause 0.3
    window show
    " She wraps the band around my waist again, strapping it around my boner!"
    maple " Wha?! Now you're at a size 27!"
    maple " Almost a 27,5..."
    show mebex surprisegrin with dissolve
    maple " What the heck is happening here??"
    " Shit!!"
    " My cock grows further!"
    window hide
    play sound "audio/soundFX/FX4/clothing2.wav" volume 0.8
    show dick hard
    show measure hard2b

    with dissolve
    pause 0.3
    show mebex grum
    with dissolve
    window show
    maple " And after a pull, it's back down to a size 23 again!"
    show mebex grump with dissolve
    maple " ONE more time!"
    play sound "audio/soundFX/FX4/clothing2b.wav"
    show  measure hard1 with dissolve
    " The band rests on my throbbing cockhead."
    show mebex waaa with dissolve
    pause 0.2
    show mebex grumpu with dissolve
    maple " Now it's at a size 31!! "
    " My cock starts throbbing and twitching!"
    show mebex grum with dissolve
    maple " What the..."
    window hide

    show measure hard3
    play sound "audio/soundFX/FX2/spank3.wav"
    with hpunch
    pause 0.2
    window show
    me " AAHG!"
    " The measuring band snaps back against my balls!"
    show mebex grump
    show mebblush
    with dissolve
    maple " Hmm?!"
    maple " And now you're making crazy sounds??"
    show mebex grump2 with dissolve
    maple " That's it- You must be pranking me!"
    me " I-I'm really not!"

    window hide
    show mebex upstern
    show mebexm behind boothmaplehands
    with dissolve
    play sound "audio/soundFX/FX4/clothing3.wav"
    hide measure
    hide boothmaplehands
    with dissolve
    pause 0.7
    scene mapleboothbg
    show blackshake at truecenter behind mapleboothbg
    show protagdick
    show protagdickskin
    with fade
    pause 0.7
    window show
    maple " Just what are you doing in here?!"
    window hide
    play sound "audio/soundFX/runn.wav"
    $ renpy.music.set_volume(0.80, delay=0, channel='music')
    pause 0.1
    $ renpy.music.set_volume(0.60, delay=0, channel='music')
    pause 0.1
    $ renpy.music.set_volume(0.40, delay=0, channel='music')
    pause 0.1
    $ renpy.music.set_volume(0.20, delay=0, channel='music')
    pause 0.1
    $ renpy.music.set_volume(0.00, delay=0, channel='music')
    show mapleconfront behind protagdick with easeinright
    pause 0.3
    window show

    " She barges in!"
    window hide
    show mapex surprise behind protagdick with dissolve
    play sound "audio/soundFX/Dun.wav" volume 1.0
    with vpunch
    window show
    maple " !!"
    " She looks right at my exposed cock!"
    maple " O-OH."
    show mapex lookaway
    with dissolve
    maple " That explains things..."
    maple " S-Sorry! I haven't measured any humans before and-"
    me " No- It's my fault, don't worry!"
#    maple " A pig-22 it is!"
#    maple " I'll be riight ou--"
    " My dick throbs and a drop of precum forms at my tip, exposing my glans. "

    window hide
    $ renpy.music.set_volume(0.20, delay=0, channel='music')
    pause 0.1
    $ renpy.music.set_volume(0.40, delay=0, channel='music')
    pause 0.1
    $ renpy.music.set_volume(0.60, delay=0, channel='music')
    pause 0.1
    $ renpy.music.set_volume(0.80, delay=0, channel='music')
    pause 0.1
    $ renpy.music.set_volume(1.00, delay=0, channel='music')
    play sound "audio/soundFX/Get.mp3" volume 0.6
    hide protagdickskin
    show protagdicksteam
    with dissolve
    show mapex lookhead with dissolve
    pause 0.6
    window show
    maple " Hnnh?"
    " Maple starts sniffing the air."
    window hide
    show mapsniff2
    with dissolve
    hide mapsniff2
    with dissolve
    show mapsniff2
    with dissolve
    hide mapsniff2
    with dissolve
    pause 0.5
    show mapex horny with dissolve
    window show
    maple " What a... lovely scent~"
    show mapexblush with dissolve
    " She blushes! "
    show mapex hornyxx with dissolve
    maple " It's sort of familiar, and... "
    maple " Smells faintly of a royal, girly perfume..."
    " What?! Is she smelling Emelie on me?! That sense of smell is crazy!"
    " ... And is she drooling?!"
    " I shift my hips to the side!"
    window hide
    play sound "audio/soundFX/Get.mp3"
    hide protagdicksteam
    hide protagdick
    show protagdickturn
    with dissolve
    pause 0.3
    show mapex hornyz with dissolve
    pause 0.3
    window show
    " Part of me wanted to grab my cock and stroke it in front of her... "
    " Her eyes even looked like she wanted me to!"
    " But I can't! Emelie called me her boyfriend yesterday and I really care about her..."
    " I'd need to know how she feels about this stuff before making moves like that or she might feel hurt!"
    show mapex woopsz
    hide mapexblush
    with dissolve
    maple " U-uuhhh... Where was I?"
    show mapex woopszzx with dissolve
    maple " Right! Size 22, was it? One second!"
    window hide
    play sound "audio/soundFX/run2.wav"
    hide mapex
    hide mapexblush
    hide mapleconfront
    with easeoutright
    pause 0.3
    scene black with fade
    window show
    play sound "audio/soundFX/FX5/Sew.wav" volume 0.8

    " My cock calms down a bit and I hear the sound of Maple's sewing machine go off."
    window hide
    scene boothbase with fade
    show blackshake at truecenter behind boothbase
    pause 0.2
    play sound "audio/soundFX/FX4/clothing3.wav"
    show maphandshorts with dissolve
    window show
    maple " Here!"
    " I grab the trunks."
    play sound "audio/soundFX/Get.mp3"
    show maphand
    hide maphandshorts
    with dissolve
    hide maphand
    with dissolve
    me " Let's see how these fit!"
    window hide
    play sound "audio/soundFX/FX4/clothing2.wav"
    show shortson
    with dissolve
    pause 0.7
    window show
    " I put the trunks on and they fit really well!"
    me " Very comfortable!"
    window hide
    stop music fadeout 1.0
    pause 0.2
    scene black with fade
    window show
    " I step outside."
    window hide
    play music "audio/Tavern+Brawl+-+320bit.mp3" fadein 2.0 volume 0.4
    play sound "audio/soundFX/FX5/curtain.wav"
    scene bg dressingroom
    show blackshake at truecenter behind bg
    show dressroom openn
    show mapc base:
        zoom 1.1
    with fade
    pause 0.3
    window show

    #Pic of pants
    show mapc out:
        zoom 1.1
    show maf lookbod2:
        zoom 1.1
    with dissolve
    maple " Oohlala! Looking good!"
    me " Thank you!"
    show maf biggrin with dissolve
    maple " And how's the fit?"
    me " They fit great!"
    show mapc cheer
    show maf closeyes
    with dissolve
    maple "Yay! "
    hide maf
    show mapc base
    with dissolve
    maple " Then let's head back!"
    window hide
    play sound "audio/soundFX/run.mp3"
    hide mapc with easeoutleft
    $ unlock("S7")
    if playnormal == False:
        show black with fade
        $ renpy.end_replay()
    pause 0.2
    scene bg tailor
    show blackshake at truecenter behind bg
    show sewmachine
    show sewmeasure
    with fade
    show mapc base behind sewmachine
    with easeinright
    pause 0.3
    show mapc backdown
    show maf insecure
    with dissolve
    pause 0.2
    window show

    maple " I'm sorry about all that in there."
    me " It was my bad!"
    show maf wince with dissolve
    maple "No, I messed up and made things kinda awkward. "
    show maf fronty
    show mapc base
    with dissolve

    maple " But at least our little mishap informed me on how to best tailor your trunks!"
    show maf lookbod with dissolve
    maple " I made them a bit stretchier up front-"
    show maf lookbod2
    show mapc tidup
    with dissolve
    maple " To account for that... big bone."
    show mafblush with dissolve
    " She blushes."
    window hide
    play sound "audio/soundFX/run2.wav"
    show billy trunks at left:
        yalign 0.5 xalign 1.08
    if modest == True:
        show trunkblue at left:
            yalign 0.5 xalign 1.08
    if modest == False:
        show trunkmelon at left:
            yalign 0.5 xalign 1.08
    with easeinright
    show maf lookbillyy behind billy
    with dissolve
    pause 0.2
    show bill surpriseface at left:
        yalign 0.5 xalign 1.08
    with dissolve
    window show
    billy " Big what?"
    show maf shy
    show mapc backdown
    hide mapeye
    with dissolve
    maple " N-nothing! "
    maple "Did the trunks fit well, Billy?"
    hide mafblush
    show bill laughface
    with dissolve
    billy " Absolutely!"
    show bill starsmile with dissolve
    billy " And wow! Those are some awesome trunks, [Protagonist]!" #*O*
    me " Thank you, Billy!"
    show maf bigg
    show mapc out
    with dissolve
    maple " They really do fit him perfectly!"
    me " Oh, and I see you brought my clothes from the dressing room!"
    show maf baseface
    show mapeye close
    show bill casualface
    with dissolve
    billy " Yes! I figured you'd forgotten them in there."
    me " That's right, woops! "
    show bill laughface with dissolve
    if modest == True:
        billy " I like the swimsuit you picked, too! Such a pretty blue! "
    else:
        billy " I like the bikini you picked, too! I love watermelon! "
    me " Was a tough choice! I'm glad you like it!"

    show bill surpriseface with dissolve
    billy " Now I've got to run back home to change and stuff!"
    " Does that mean I'll finally get to see what Billy looks like without his armor on later!?"
    show bill baseface with dissolve
    if modest == True:
        billy " I figure I can take your ol' clothes with me so you don't have to take a trip back? And I'll deliver the swimsuit too!"
    else:
        billy " I figure I can take your ol' clothes with me so you don't have to take a trip back? And I'll deliver the bikini too!"

    show bill hapiface with dissolve
    billy " That way you just go right to the beach after you get Bronwen her money!"
    me " Great idea!"
    show bill laughface with dissolve
    billy " Woo!"
    billy " Remember Per by the outer gates? He'll point you to the beach! It's really close by!"
    me " I see, yes!"
    hide bill baseface with dissolve
    billy " See you there later, [Protagonist]!"
    me " Yes! We'll catch up soon!"
    window hide
    hide billy
    hide bill
    hide trunkblue
    hide trunkmelon

    if modest == True:
        show happyholdblue  at left:
            yalign 0.5 xalign 1.08
        show happyholdblue  at left:
            linear 0.5 xalign -0.8 yalign 0.5
    if modest == False:
        show happyholdmelon  at left:
            yalign 0.5 xalign 1.08
        show happyholdmelon  at left:
            linear 0.5 xalign -0.8 yalign 0.5

    pause 0.3
    show mapeye left behind happyholdblue , happyholdmelon
    show maf baseface
    with dissolve
    if modest == True:
        hide happyholdblue
        show happyholdblue2 at left:
            xalign -0.8  yalign 0.5
    else:
        hide happyholdmelon
        show happyholdmelon2 at left:
            xalign -0.8  yalign 0.5
    with dissolve
    window show
    billy " And you have a good one, Maple!"
    play sound "audio/soundFX/FX5/ding.wav" volume 0.4
    show mapc peacehigh
    show maf biggrin
    with dissolve
    maple " You too, Billy!"
    window hide
    hide billy
    hide bill
    if modest == True:
        hide happyholdblue2
    else:
        hide happyholdmelon2
    hide trunkblue
    with easeoutleft
    window show
    billy " And here's the money bag for this purchase and for Bronwen!"
    play sound "audio/soundFX/FX5/CoinBag.wav" volume 0.9
    with vpunch
    " Billy hands me Emelie's coin pouch on his way out."
    billy " You left it in the dressing room!"
    billy "Buhbye, now!"
    play sound "audio/soundFX/Run2.wav"
    window hide
    hide mapeye
    show maf hapigrin
    show mapc out
    with dissolve
    pause 0.3
    window show
    maple " Wow, you two have a beautiful friendship!!"
    show maf sly with dissolve
    maple " That'll be forty silver all in all!"
    show maf wink with dissolve
    maple " The custom fitting is on me!"
    me " Okay!"
    "Hmm... Emelie told me to tip generously for good work, and I sure got that!"
    "I guess I'll just throw in an extra coin!"
    me " Here you go! "
    window hide
    play sound "audio/soundFX/FX5/coin2.wav"

    show maplecoin1
    show maplecoin2
    with dissolve
    pause 0.3
    show maf fardown with dissolve
    pause 0.3
    window show
    "I hand her two gold coins."
    show maf fardown2 with dissolve
    maple " Jeez! "
    show maf insecure with dissolve
    show mapc holdsingle
    show mapcholdsingle
    hide maplecoin2
    with dissolve
    maple " Very generous, but please save a coin and come by again soon, kay?"
    show maf frontystar with dissolve
    maple " Making clothes for humans is exciting!"
    window hide
    hide mapcholdsingle with dissolve
    play sound "audio/soundFX/FX5/coin1.wav"
    with vpunch
    show mapc base
    show maf wink2
    with dissolve
    window show
    "She gives one of the coins back and throws me a wink."
    me " O-okay!"
    show mapc back
    show maf biggrin
    with dissolve

    maple " I have to improve my skills so I can live up to being \"man's best friend\" after all! Haha!"
    me " What??"
    show mapc hips
    show maf biggrin2
    with dissolve
    maple " Never heard the saying? It exists for a reason, y'know!"
    me " I haven't!"

    window hide
    #Question her about human/dog history
    menu:
        with dissolve


        " Tell me more about human & canine history!":
            window show
            me " Tell me more about human & canine history!"
            show maf biggrin
            show mapc out
            with dissolve
            maple "Dogs and humans have a long, historic bond!"
            maple "I heard us dogs were all wolves once! Waaaaaaaaay back in the day!"
            show mapc tid
            show maf wince
            with dissolve
            maple" Wolves were known to be loyal to each other, but extremely ruthless to outsiders!"
            show maf ofoa with dissolve
            maple" But one day some of the more gentle wolves fled from their aggressive leaders, hoping to find a life with less conflict."
            show maf hapuface with dissolve
            maple" These wolves struggled to find a new home for a long time, but eventually found themselves among humans, where they thrived together in perfect harmony!"
            show mapc thinking
            hide maf
            with dissolve
            maple" I don't think we know why humans were so accepting of these wolves..."
            maple" Maybe we realized we could help each other in various ways... "
            maple "Canines benefitting from human infrastructure, and humans benefitting from our great sense of smell and tracking skills!"
            show mapc out
            show maf closeyes
            with dissolve
            maple"Or maybe you just happen to find us really cute!"
            show maf gloss
            show mapc overheadup
            with dissolve
            maple" Do these big, warm eyes and wagging tail do anything for you? "
            window hide
            play sound "audio/soundFX/Dun.wav" volume 0.3
            with hpunch
            window show
            "I choke on my spit!"
            me " Chekgh!"
            show maf closeyes
            with dissolve
            maple " Haha!"
            show maf hapigrin
            show mapc out
            with dissolve
            maple" Dogs certainly look very different from wolves these days! "
            show mapc hips
            show maf ofoa
            with dissolve
            maple " And we look really different from each other, too!"
            show maf closeyes with dissolve
            maple "We've got strong and courageous mastiffs, as well as handsome lil' beagles!"
            show mapc thinking
            hide maf
            with dissolve
            maple " I'm not sure how to explain all that variety."
            maple " Or how we came from wolves..."
            me " I think I might know!"
            show maf bigg
            show mapc base
            with dissolve
            maple " Really?"
            me " It's called... \"Evodution\"!"
            me " ... Or something like that. "
            show maf ofoa
            show mapc tid
            with dissolve
            maple "??"
            me " I heard it explained to me recently!"
            me " You see, for a long time, birds didn't have breasts-"
            me "... "
            show maf biggrinz
            show mapc hips
            with dissolve
            maple " What?"
            me " Y'know what, I think you're better off asking Victoria to explain it to you over at the library."
            me " I'm not sure if I remember all of it correctly!"
            #When Victoria shows up at the beach later, she could mention that Maple asked her about 'Evodution' and she heard you were going to the beach! So she took the rest of the day off.."
            show maf closeyes
            show mapc out
            with dissolve
            maple " I'll definitely do that! I'm curious now!"
            hide maf
            show mapc thinking
            with dissolve
            maple " \"Eboglution\", huh?"
            show mapc base
            show maf hapigrin
            with dissolve
            maple " But yeah! Humans and dogs share a close bond all over the world!"
            me " Very interesting, I had no idea! "
            me " If your goal is to be \" man's best friend \" then maybe I can be \"dog's best friend!\""
            show maf closeyes
            show mapc out
            with dissolve
            maple " Haha, well you're on a good path after today, I'd say!"
            "Maple and I both chuckle."
            me " And so are you! "
            show maf hapigrin
            with dissolve
            maple " Yay!"
            me "But now I've got to get going! I have some money that needs delivering!"



            #Collar and leash = old bonding exercise?

        " I should get going, I have some money that needs delivering!":# This skips a lot of his explanation.
            window show
            me " I should get going, I have some money that needs delivering!"




    #Question her about herself and about working in Hog Haven. How did she start?







    show maf biggrin
    show mapc base
    with dissolve
    maple " Aha, I understand! "
    show maf bigg
    show mapc cheer
    with dissolve
    maple "I'm going down to the beach soon myself when I run out of swimwear to sell!"
    me " Great! Try to find me!"
    show maf sly
    show mapc tidup
    with dissolve
    maple " Yes! My nose will track ya down~ "
    me " And thank you for all the help!"
    show maf wink
    show mapc dubpeacehigh
    with dissolve
    maple " No problem at all, stud! See ya later!"

    window hide
    scene black with fade
    play sound "audio/soundFX/FX2/shop-door-bell.wav" volume 0.4

    window show
    " I wave Maple goodbye and leave the shop."
    window hide
    scene tailorsmith with fade
    show blackshake at truecenter behind tailorsmith
    window show
    " Phew, she sure was friendly!"

label smithypayoff:
    window hide
    stop music fadeout 0.3
    pause 0.2

    play sound "audio/soundFX/FX2/church-bell-fischerhude-short.wav"
    with vpunch
    pause 0.3
    window show

    " The bells ring, great timing!"
    window hide
    scene black with fade
    window show
    " I hurry on into the smithy."
    play sound "audio/soundFX/FX3/hammer-on-anvil.wav" volume 1.0
    #Sound effect of anvil hammering
    window hide
    scene black with fade
    pause 0.3
    window hide
    play music "audio/Blacksmith+-+320bit.mp3" fadein 1.0 volume 0.4
    scene bg smithy
    show blackshake at truecenter behind bg
    show smithysmoke
    show bronwen hammer behind broneye at left:
        yalign -0.0 xalign 1.3
        zoom 0.9
    show smithyanvil
    show anvilhammer
    show broneye lookdown at left:
        yalign -0.0 xalign 1.3
        zoom 0.9
    with fade
    pause 0.2
    hide broneye with dissolve

    window show

    bron " There you are!"
    show bronwen finger
    show bron downpull  at left:
        yalign -0.0 xalign 1.3
        zoom 0.9
    with dissolve
    bron " Hah, what's with the trunks? "
    bron " Did'ya sell the rest of your clothes to afford paying me back, hmm?"
    show bronwen base
    show bron laugh
    with dissolve
    bron " Hahah!"
    me " That's not it! I'm going to the beach today."
    me " Seems a lot of people are going for some big event."
    show bronwen finger at left:
        yalign -0.0 xalign 1.3
        zoom 0.9
    hide bron
    with dissolve
    bron " ...Really?"
    me " That's what I heard! Now how much for the buttplu-"
    me " Uuuhh... {i}accessory{/i}... you made for me yesterday?"
    show bronwen hips
    show bron hehh at left:
        yalign -0.0 xalign 1.3
        zoom 0.9
    with dissolve
    bron " Ten gold."
    window hide
    play sound "audio/soundFX/Dun.wav" volume 0.7
    with vpunch
    pause 0.4
    window show
    me " WHA-"
    me " Isn't that a bit high? I just paid forty silver for three pieces of clothing..."
    me " And you hammered that thing together in like five seconds."
    show bron questioning
    show bronwen base
    with dissolve
    bron " Oh yeah? Well I also put a gem and some extra gold on there! "
    bron " And you won't find anyone else for miles who can do the type of high-quality work I do! "
    show bron cooldown with dissolve
    bron " Just because I'm fast doesn't mean my prices should be cheaper. "
    bron " Reliability and a quick turnaround is part of the price calculation!"
    me " Fine, fine... That does make sense!"
    " I can't tell if I'm being ripped off or not. "
    " Oh well, it isn't my money and the royal family probably has a lot to spare! "
    " And it WAS damn good work! Led to a night I'll never forget."
    window hide
    play sound "audio/soundFX/FX5/coin1.wav" volume 0.9
    show anvilcoins behind anvilhammer
    with dissolve
    pause 0.3
    show bron smilee
    show broneye lookdown2 at left:
        yalign -0.0 xalign 1.3
        zoom 0.9
    show bron grin
    with dissolve
    pause 0.2
    window show
    me " Here you go. Thank you!"
    " I pay her a total of eleven gold, remembering what Emelie said about tipping."
    " Now I'm entirely broke..."
    show bron grin
    hide broneye
    with dissolve
    bron " Heh. "
    " Bronwen grins."
    show bronwen hips with dissolve
    bron " Not bad. We should definitely do more business together..."
    #When you ask her to forge a ring for you, she first makes one too big. Cockring scene. She teases the player all like " Well well... can't let you cum on some other hog right before your wedding, can I? etcetc "
    show bron grin2 with dissolve
    bron " Y'know maybe with this nice tip I'm able to take some time off and go check the beach out myself... "
    show bron smilee with dissolve
    bron " There are some action-packed events there from time to time!"
    play sound "audio/soundFX/Run2r.wav"
    show rolf takeout at right:
        zoom 0.97 yalign 0.51 xalign 1.39
    show roleye lookside at right:
        zoom 0.97 yalign 0.51 xalign 1.39
    with easeinright
    show broneye lookright2b at left:
        yalign -0.0 xalign 1.3
        zoom 0.9
    with dissolve
    rolf " Here's your food, dear!"
    window hide
    play sound "audio/soundFX/Get.mp3"
    show rolf base
    show anviltakeout behind anvilhammer
    with dissolve
    pause 0.3
    window show
    " Oh shit, I forgot Rolf always shows up with lunch!"
    hide broneye
    show bron laugh
    with dissolve
    bron " Thanks, dad!"
    hide roleye with dissolve
    $ renpy.music.set_volume(0.80, delay=0, channel='music')
    pause 0.1
    $ renpy.music.set_volume(0.60, delay=0, channel='music')
    pause 0.1
    $ renpy.music.set_volume(0.40, delay=0, channel='music')
    pause 0.1
    $ renpy.music.set_volume(0.20, delay=0, channel='music')
    pause 0.1
    $ renpy.music.set_volume(0.00, delay=0, channel='music')
    play sound "audio/soundFX/FX5/stepknuck.wav"
    show rolf base at right:
        zoom 0.97 yalign 0.51 xalign 1.39
    show rolf knuckles at right:
        zoom 0.97 yalign 0.51 xalign 1.39
        linear 0.3 zoom 1.04 yalign 0.41 xalign 1.39
    with hpunch

    rolf " You again?! "
    rolf " Getting REAL friendly with my daughter are ya?!'"
    me " I'm just-!"
    show bron huhh
    show broneye lookright at left:
        yalign -0.0 xalign 1.3
        zoom 0.9
    with dissolve
    show bron rageface2
    show bronwen knuckles

    hide broneye
    play sound "audio/soundFX/FX5/rolfknuckles.wav" volume 0.2
    with hpunch
    bron " Lay off it, dad! "
    bron " He's PAYING me! "
    show bron cooldown with dissolve
    bron " Tipping damn generously too, I might add!"
    show bron donefor
    show bronwen base
    show broneye lookright at left:
        yalign -0.0 xalign 1.3
        zoom 0.9
    with dissolve
    bron " And thanks to this generous tip... I've decided to take the rest of the day off! "
    window hide
    show rolf sidewary2 with dissolve
    show rolf sidewary2 at right:
        linear 0.5 zoom 0.97 yalign 0.51 xalign 1.39
    pause 0.5
    show rolf sidewary2 at right:
        zoom 0.97 yalign 0.51 xalign 1.39
    $ renpy.music.set_volume(0.20, delay=0, channel='music')
    pause 0.1
    $ renpy.music.set_volume(0.40, delay=0, channel='music')
    pause 0.1
    $ renpy.music.set_volume(0.60, delay=0, channel='music')
    pause 0.1
    $ renpy.music.set_volume(0.80, delay=0, channel='music')
    pause 0.1
    $ renpy.music.set_volume(1.00, delay=0, channel='music')
    with dissolve
    window show
    rolf " ... Really? "
    show bron grin with dissolve
    bron " Mhm!"
    show rolf base
    show rol smiley at right:
        zoom 0.97 yalign 0.51 xalign 1.39
    with dissolve
    rolf " That's great!"
    " Rolf looks overjoyed."
    show roleye looksidehapi at right:
        zoom 0.97 yalign 0.51 xalign 1.39
    show rolf belly
    with dissolve
    rolf " I'm working a short shift as security down by the beach in just a bit! "
    rolf " Maybe we can spend some time together right after?"
    show bron laugh with dissolve
    bron " Sure!"
    show bronwen knuckles
    show bron donefor2
    show broneye squintside
    with dissolve
    bron"  You know if there's any action this year? "
    show rol laugh
    show roleye looksidehapi2 at right:
        zoom 0.97 yalign 0.51 xalign 1.39
    with dissolve
    rolf " Not sure, but I hope so!"
    show bron laugh
    show bronwen base
    hide broneye
    with dissolve
    " They both look really excited."
    show broneye squintside at left:
        yalign -0.0 xalign 1.3
        zoom 0.9
    show bron grin
    with dissolve
    bron " I've got a few things to take care of after lunch. Then I'll be right down!"
    show bron baseface with dissolve
    hide broneye with dissolve
    bron " So off you two go!"
    hide roleye with dissolve
    rolf " Okay, sweetie! See you later!"
    show bron pout
    show broneye squintside at left:
        yalign -0.0 xalign 1.3
        zoom 0.9
    with dissolve
    bron " And be chill with [Protagonist], dad... "
    show rol pout
    show rolf calm
    with dissolve
    rolf " ..."
    " Rolf looks back to me with a snarl."
    show bron grin
    show broneye lookright
    show bronwen hips
    with dissolve
    bron " If it wasn't for him I'd be slaving away at work all day like usual. "
    show rolf belly
    hide roleye
    with dissolve
    rolf "...Fine."
    me " O-okay, uuuh... Thank you for your business and maybe I'll bump into you again later!"
    hide broneye with dissolve
    bron " Right. Bye now."
    show rol smiley
    show roleye looksidehapi at right:
        zoom 0.97 yalign 0.51 xalign 1.39
    show rolf base
    with dissolve
    rolf " Byebye! Enjoy your meal!"
    window hide
    play sound "audio/soundFX/Run2r.wav"
    hide rolf
    hide rol
    hide roleye
    with easeoutright
    pause 0.2
    jump RPSS

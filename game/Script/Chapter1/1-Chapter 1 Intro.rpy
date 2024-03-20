# The script of the game goes in this file.
# The game starts here.
define config.mouse = { "default" : [ ("gui/pointer.png", 0.0, 0.0)], "hover" : [("gui/pointerclick.png", 0, 0)] }
#define config.mouse = { "HoverMouse" : [ ("gui/pointerclick.png", 0.0, 0.0)] }


init python:#This is for the menu buttons that are in main menu like the save squares and stuff.
    style.button.activate_sound = "audio/UIsounds/cluck.wav"
    style.button.hover_sound = "audio/UIsounds/hover.wav"
    style.button.mouse = "hover"

label start:

    screen input(prompt):
        style_prefix "input"
        window:
            vbox:
                xalign 0.35  yalign 0.53
                text prompt style "input_prompt" outlines [(4, "#0B0509", 0, 0)] color "#C7C7D2" size 39 #question color
                input id "input" outlines [(5, "#0B0509", 0, 0)] color "#FCDC90" size 48 #Player name that I type out color




    # högre yalign = högre upp på skärmen. 0.0 är bas värdet.
    # SHift + R resettar renpy builden. om du vill se ngt ändras live måste du gå tillbaka till rätt del
    #t.ex. om du ändrar zoom och zill se det ändras när du trycker shift+r måste du gå till delen då bilden zoomas i koden.
    scene black with dissolve
    stop music fadeout 0.5
    play music "audio/Trails.mp3" fadein 0.2 volume 0.3
    play sound "audio/soundFX/Dirt Dig.wav"
    $ renpy.pause(4.0, hard=True)
    scene bg farm with dissolve
    play sound "audio/soundFX/Crack_2.wav"
    show blackshake at truecenter behind bg
    with hpunch
    $ ComeAlong = "neutral"

    $ playnormal = True





    "Augh!"
    "Summer just started and my back's already killing me!"
    "It usually takes a few more months of hard work for my body to get this worn out."
    "Maybe all the years of working these fields is finally catching up to me."
    "...I could really use a break."
    show blackopacity
    show carriage
    with dissolve
    "At least I'm well ahead of today's schedule. My cart's all filled up!"
    "Now's a good time to take a breather and refresh."
    "I've worked as a farmer for as long as I can remember, and while it's hard labour there's one upside..."
    "You can always sneak in a quick snack!"
    "The sun's really starting to burn. I'll grab one of these thick ol' cucumbers and find some shade!"

    window hide
    scene bg hill with fade
    pause 0.2
    window show
    "That tree over on the hill is the only one still standing proud on my little patch of land."
    "All the other ones were cut down for firewood or to make space for more farms before I moved here a couple' summers back."
    "The large rock underneath has been my go-to spot for a while now. There's always a chill breeze and plenty of shade."
    "But best of all..."
    window hide
    pause 0.1
    scene bg castle with fade
    window hide
    pause 0.2
    window show
    "The view is incredible!"
    "That great castle over there is Hog Haven, where most of my wares are sold to, and the reason a lot of farmers like myself come here for work."
    "Pigs have a great appetite and love to buy in bulk, and who can blame them? These farm lands produce some damn good veggies."

    "I bite into the freshly picked cucumber and gulp down what's mostly water."
    window hide
    pause 0.2
    show blackshake at truecenter behind bg
    play sound "audio/soundFX/FX3/crunch.wav"volume 0.7
    with vpunch
    pause 0.4
    window show
    "Puah, that's good!"

    "You'd think I'd get tired of the same old produce day in and day out, but anything tastes good when you're thirsty and aching all over."

    # Glint effect
    window hide
    play sound "audio/soundFX/Glint2.wav"
    show white with dissolve
    stop music fadeout 0.2


    pause 0.3
    window show
    "Ah! My eyes!"
    window hide
    scene bg castle2 with dissolve
    with Pause(1.0)
    window show
    play music "audio/Birds.wav" fadein 7.0 volume 0.2

    "What the hell was that?!"
    "There's some sort of big reflective ball moving in the distance."
    "Must be a piece of shiny metal being transported or something..."
    window hide
    scene bg castle3 with dissolve
    with Pause(0.8)
    window show
    "...Or wait a minute... "
    "...It's got legs... And It's getting closer!"
    window hide
    scene bg castle with dissolve
    with Pause(0.5)

    show billy base at left with dissolve:
        zoom 0.9
        yalign 0.4 xalign -0.08
    stop music fadeout 1.0
    play music "audio/adventures-in-adventureland-by-kevin-macleod-from-filmmusic-io.mp3" fadein 0.1 volume 0.3
    window show
    "!!"
    "It's one of those pig guards from the castle! And a big, ROUND one at that!"
    "I've never seen one taller than me before. Pigs tend to be on the shorter side."
    "What's he doing way out here?"

    show billy base at left:
        zoom 0.9
        yalign 0.4 xalign -0.08
        linear 0.2 yalign 0.4 xalign -0.08 zoom 1.0
    $ billy_name = "???"

    billy "Oh, there you are!"

    "...Is he talking to me?"
    show billy high
    with dissolve

    billy "Hello, hello!"

    billy "Hope I'm not disturbing ya!"
    show billy casual with dissolve
    "He grips and adjusts his struggling belt, the heavy armor creaking as he moves."
    billy "The name's Billy!"

    $ billy_name = "Billy"
    billy "What's {i}your{/i} name?"
label nameprotagonist:

    $ Protagonist = renpy.input ("What is my name?{space=70}{space=0} {alpha=0.85} {size=-5}{i}Type it and press \"Enter\" when done!{/i}{/size}{/alpha}", length=15)
    if Protagonist == "":
        "Hmm I'm pretty sure that's not my name. It's at least two letters long!"
        jump nameprotagonist
    if Protagonist is not None:
        $ check_name = len(Protagonist)
        if check_name == 1:
            "Hmm I'm pretty sure that's not my name. It's at least two letters long!"
            jump nameprotagonist
    $ Protagonist = Protagonist.title()
    play sound "audio/UIsounds/cluck.wav"
    me "Hello! I'm [Protagonist]."
    window hide

    show billy base
    hide bill baseface
    with dissolve

    window show
    billy "Pleased to meet ya, [Protagonist]!"

#SKIPPU
#SKIPPU
    #jump navigate
#SKIPPU
#SKIPPU
    #jump navigate2
#SKIPPU
#SKIPPU

label normalgame:
    "I give him a little nod as I finish my snack."
    window hide
    show blackshake at truecenter behind bg
    play sound "audio/soundFX/FX3/crunch-2.wav"volume 0.4
    with vpunch
    pause 0.5

    show billysurpriseface at left:
        yalign 0.4 xalign -0.08
    with dissolve
    window show
    billy "A-Ahh!"
    show bill laughface at left:
        yalign 0.4 xalign -0.08
    with dissolve
    billy "Nothing's better than the sound of a crispy cucumber!"
    billy "Fresh ones hit the market later today! I can't wai-"
    show billy wary
    show billysurpriseface at left:
        yalign 0.4 xalign -0.08
    hide bill laughface
    with dissolve
    billy "Hold up..."
    "Billy freezes for a long moment."
    billy "You're a cucumber farmer?"
    me "Among other things, sure am!"
    show billy base with dissolve
    billy"Woaah! What else??"
    "He seems very impressed for some reason."
    me "Potatoes, tomatoes, lettuce..."
    me "And a whole lot of carrots."
    show bill laughface at left:
        yalign 0.4 xalign -0.08
    with dissolve
    billy "CARROTS ARE THE BEST!"
    show billy belly with dissolve
    billy "Especially carrot cake! Mmmmhhhh..."
    me "Oh? I'll need to try it sometime!"
    hide bill laughface
    hide billysurpriseface
    show billy wary
    with dissolve
    billy "You... haven't tried carrot cake?"
    "His voice turns somber for a moment and a little sniffle escapes his helmet."
    show billy clench with dissolve
    billy "You know, I really appreciate you and the other farmers for your work!"
    billy "Working so hard day in and day out."
    billy "Your resolve is beyond remarkable! If I had all these fresh veggies around me I'd-"
    show bill baseface at left:
        yalign 0.4 xalign -0.08
    with dissolve
    billy "Oh crap, I almost forgot!!"
    me "Hmm?"
    show billy finger
    hide bill baseface
    with dissolve
    billy "I'm here by royal order, there are some things YOU need to clear up!"
    "?!"
    "This sounds bad!"
    show billy casual with dissolve

    billy "No need to turn pale, you're not in any trouble!"
    billy "Once you answer a few questions you'll be free to leave. Pinkie promise!"

    "\"Pinkie promise\"? That's not something I'd expect to hear from a guard."

    "Actually, neither is his generally gentle demeanor. He seems really harmless and speaks his mind very bluntly."
    "Hmm..."
    "... That's odd."
    " It looks like he isn't carrying any weapons with him either. If I was in any real trouble he'd surely be armed."
    "But why is he looking for {i}me{/i} in particular?"
    show billy base with dissolve

    billy "So... what do you say?   Ready to come along?"
    window hide
    menu:
        with dissolve



        "Can you explain what you need me for?":
            window show
            me "Can you explain what you need me for?"
            $ ComeAlong = "neutral"
            show billy finger with dissolve
            billy "Like I said - I've been ordered to bring you in to clear something up. "
            billy" I can't say much more than that, sorry!"
            me "That sounds pretty bad."
            show billy casual with dissolve
            billy "I'm telling you, it's not!"
            show billy belly
            show bill baseface at left:
                yalign 0.4 xalign -0.08
            with dissolve
            billy "Trust me, bud! I wouldn't allow such a dedicated farmer to go out of business! Or carrot cake supply might run low, haha!"
            "I don't imagine I have a choice either way. Even if Billy lets me go for now they'd surely send backup if I'm some sort of person of interest."
            "And if so... they'd likely be armed and with an attitude."
            "I've got to trust Billy and hope for the best."
            me "Okay, lead the way."
            hide bill baseface

        "Sure, I needed a break from work anyway. Lead the way!":
            window show
            me "Sure, I needed a break from work anyway. Lead the way!"
            $ ComeAlong = "break"


        "Fine, but I better get paid for lost work hours!":
            window show
            me "Fine, but I better get paid for lost work hours!"
            $ ComeAlong = "paid"
            me "And if someone steals my crops when I'm away I'll want compensation for that too!"
            show billy belly with dissolve
            billy "Sorry buddy, but that's way above my paygrade!"
            "It was worth a shot. "
            show billy base with dissolve
            billy "Worst case scenario, I'll make sure to get you some carrot cake!"
            "Better than nothing, I guess."
            me "Fine. Lead the way!"
    show billy casual
    show bill laughface at left:
        yalign 0.4 xalign -0.08
    with dissolve
    billy "Great!"


    "Billy takes the lead and wiggles along at a leisurely pace."
    window hide
    show sky
    show blackopacity
    show Butterfly
    with fade
    window show
    "As I follow him he pays more attention to flowers and butterflies than making sure I'm keeping up."
    "I feel like my heart should be racing, but Billy's carefree attitude coupled with the pleasant weather sets me at ease."
    "If this is how he treats a royal order, I really wonder how he'd treat a routine patrol..."
    window hide
    scene gateall
    with fade
    pause 0.2
    window show
    #"whatthefuck"

    "We finally arrive at one of the gates."
    "I’ve carried stuff here from the farm a few times, but never stepped foot inside."
    show billy base at left with dissolve:
        yalign 0.4 xalign -0.09

    billy "That was fast! Time sure flies when you're in a good mood!"
    billy "Now just look friendly and don't fidget too much and we'll be let in no problem!"
    me "Alright."
    show billy casual with dissolve
    billy "Good, good! "
    billy "And stay close so they know you're with me!"
    "I give Billy a nod and we quickly approach the guards at the gate."
    window hide
    hide billy with dissolve
    scene gateall:
        zoom 1.0
        linear 0.5 zoom 1.15 xalign 0.3
    $ renpy.pause(0.5, hard=True)
    show billy base at left:
        zoom 0.9
        alpha 0.0
        yalign 0.4 xalign -0.08
        linear 0.5 alpha 1.0
    $ renpy.pause(0.5, hard=True)
    show bg gate behind billy:
        alpha 0.0
        zoom 1.15  xalign 0.3
        linear 0.5 alpha 1.0
    $ renpy.pause(0.5, hard=True)
    show per sweat at center with dissolve:
        zoom 0.9
        yalign 0.4 xalign 1.15
        linear 0.5
    $ renpy.pause(0.5, hard=True)
    window show

    billy "Hey hey, Per!"
    billy "How's it goin' this lovely day?"
    per "..."
    per "Hey hey, Billy..."
    "Per looks like your average pig guard. He's armed and a bit shorter than myself."
    "He's sweating profusely."
    show per sweat2 with dissolve
    per "You know how this damn spot gets in the summer. Sun's turning this armor into a bleedin' oven."
    per "I really don't understand how you keep your visor down all day, I'd drown in my own sweat."
    show billy thumbup
    show bill laughface at left:
        zoom 0.9
        yalign 0.4 xalign -0.08
    with dissolve
    billy "Safety first, Per! Like I always say~"

    "Per grumbles quietly with his eyes closed."
    show per sweat with dissolve
    per "I wouldn't call constant heat strokes very safe..."
    show billy base
    hide bill laughface
    with dissolve

    billy "Anyways, I'm bringing [Protagonist] here into the city!"
    play sound "audio/soundFX/Get.mp3"
    with vpunch

    "Billy puts a hand on my shoulder."
    me "...Hey hey!"
    $ renpy.music.set_volume(0.00, delay=0, channel='music')
    show per surprise:
        zoom 0.9
        yalign 0.4 xalign 1.15
        linear 0.2 yalign 0.4 xalign 1.15 zoom 1.0


    play sound "audio/soundFX/Pig Oink.wav"
    per "!!!"
    per "What the he-"

    show per surprise:
        zoom 1.0
        yalign 0.4 xalign 1.15
        linear 0.2 yalign 0.4 xalign 1.15 zoom 0.9
    pause 0.2
    show per surprise:
        yalign 0.4 xalign 1.15 zoom 0.9

    show per apologetic with dissolve
    $ renpy.music.set_volume(0.10, delay=0, channel='music')
    pause 0.2
    $ renpy.music.set_volume(0.20, delay=0, channel='music')
    pause 0.2
    $ renpy.music.set_volume(0.30, delay=0, channel='music')
    pause 0.2
    $ renpy.music.set_volume(0.40, delay=0, channel='music')
    pause 0.2
    $ renpy.music.set_volume(0.50, delay=0, channel='music')
    pause 0.1
    $ renpy.music.set_volume(0.60, delay=0, channel='music')
    pause 0.1
    $ renpy.music.set_volume(0.70, delay=0, channel='music')
    pause 0.1
    $ renpy.music.set_volume(0.80, delay=0, channel='music')
    pause 0.1
    $ renpy.music.set_volume(1.00, delay=0, channel='music')

    per "Ahem, I didn't see ya there!"
    "Per looks uneasy for some reason. "
    "I remember what Billy said and put on a wide smile, trying to look as friendly as possible."
    show per weird
    show pereye sidee at center:
        yalign 0.4 xalign 1.15 zoom 0.9
    with dissolve
    per "Hmm... And what's the reason for this, Billy?"
    per "Bringing a human into the capital... "
    per "I might have to check with someone higher up before letting you through-"
    show billy finger with dissolve
    billy "No need! This is a royal order from the very top!"
    hide pereye
    show per surprise
    with dissolve
    per "Oh, I-I see!"
    show per base with dissolve
    per "Well if that's the case, just stroll on in."
    "Per grumbles again."
    show per weird
    show pereye sidee at center:
        yalign 0.4 xalign 1.15 zoom 0.9
    with dissolve
    per "Just make sure this doesn't come back to bite me in the ass!"
    "What's that supposed to mean?"
    show billy casual with dissolve
    billy "'Course not!"
    hide pereye
    show per base
    with dissolve

    per "And hey... [Protagonist], was it?"
    me "That's right."
    show per apologetic with dissolve
    show per apologetic:
        zoom 0.9
        yalign 0.4 xalign 1.15
        linear 0.2 yalign 0.4 xalign 1.15 zoom 0.93

    per "Sorry for the... unprofessional reaction..."
    per "Heat's gettin' to me and I'm not sure a human's ever passed through these gates before!"
    window hide
    menu:
        with dissolve
        "No worries!":
            window show
            me "No worries!"
            show per:
                zoom 0.93
                yalign 0.4 xalign 1.15
                linear 0.2 yalign 0.4 xalign 1.15 zoom 0.90
            pause 0.2
            show per:
                yalign 0.4 xalign 1.15 zoom 0.90
            show per base with dissolve
            per "Puh! Good, good! "
            per "Wouldn't want to be known as the guy tryin'a stand in the way of a royal order, hehe!"
            per "I hope you'll enjoy your stay!"
            me "Thanks!"


        "Really? How long have you been working this post?":
            window show
            me "Really? How long have you been working this post?"
            show per:
                zoom 0.93
                yalign 0.4 xalign 1.15
                linear 0.2 yalign 0.4 xalign 1.15 zoom 0.90
            pause 0.2
            show per:
                yalign 0.4 xalign 1.15 zoom 0.90
            show per base with dissolve
            per "Hmm... Give or take fifteen years now."
            me "fifteen years, and you've never let a human through? Or had one ask to be let through?"
            per "Correct."
            "Huh..."
            show billy wary with dissolve
            billy "Ooo, now you're both making it sound like I'm part of a big event or something!"
            show billy belly
            show bill laughface at left:
                zoom 0.9
                yalign 0.4 xalign -0.08
            with dissolve
            billy "Or maybe Per's just too busy dozing off in the sun to register who comes and goes, haha!"
            show per sweat2 with dissolve
            per "Very funny, Billy. Now move along and let me suffer in silence!"
            show per base with dissolve
            per "Enjoy your stay, [Protagonist]!"
            me "Thanks!"
            hide bill laughface

    show billy high
    with dissolve
    billy "Have a good one, Per!"

    show per base
    show pereye sidee at center:
        yalign 0.4 xalign 1.15 zoom 0.9
    with dissolve
    per "You too."
    show per weird with dissolve
    per "And stay out of trouble!"

    show billy casual with dissolve

    stop music fadeout 1.3
    "Per steps aside and we hurry on through."

    "I'm finally about to see the inside of the castle for the first time!"
    window hide


    play music "audio/9.+We+Are+Victorious+-+320bit.mp3" fadein 0.1 volume 0.3 noloop
    queue music "audio/Tavern+Brawl+-+320bit.mp3" fadein 0.1 volume 0.3

    scene bg bullman with fade
    pause 1.5
    window show
    "Woah!"
    "The city's really buzzing!"
    "The smell of freshly baked bread and pastries fills my nose."
    "The castle walls look even bigger from the inside."
    "There are houses everywhere, with some built directly into the walls!"
    "It seems a majority of the population consists of pigs, but I can see a few other animals, too."
    "Like that huge bull carrying crates around!"
    "They’re probably full of produce from one of the neighboring farms."
    window hide
    scene bg chicken with fade
    pause 1.5
    window show
    "A chicken lady appears to be wheeling her eggs somewhere."
    "Compared to the farm everyone's got fairly clean clothes here. I feel sort of rugged with my patchy, dirty overalls."
    "But if Per’s correct, and humans really are such a rare sight around these parts, it’s not gonna be my clothes that draw people’s attention."
    "I'm not getting a whole lot of dirty looks, though. Maybe the guards are just taught to be extra cautious?"
    "If that's the case then Billy must've missed that class..."
    window hide
    scene fountain with fade
    pause 0.3
    window show
    "We stop behind a big fountain and Billy exhales."
    show billy base at left with dissolve:
            yalign 0.4 xalign -0.08
    billy "Puh, now we're almost there! "
    billy "Just need to enter that building to the right, on the other side of the fountain!"
    me "Sweet!"
    billy "Now, before we proceed..."
    show billy helmet with dissolve
    billy "I'm gonna need you to wear this!"
    me "A guard helmet?!"
    show bill baseface at left with dissolve:
            yalign 0.4 xalign -0.08
    billy "Yes! I tried to find one small enough to fit someone a bit less... wide."
    billy "This is the best I could find!"
    me "Why'd you need me to wear that...?"
    me "Billy, are you up to something?"
    billy "Not at all! I'm just trying to complete my task! "
    billy "And I think this will... maximize our chances of success!"
    show billysurpriseface at left with dissolve:
            yalign 0.4 xalign -0.08
    billy "Per is a nice guy, but you saw his reaction."
    billy "Some guards here can get a bit... well..."
    me "But would there really be a problem if you have a royal order like you say?"
    show bill baseface at left:
            yalign 0.4 xalign -0.08
    hide billysurpriseface
    with dissolve
    billy "You're right, there shouldn't be any issues!"
    billy "..."
    billy "But wear it just in case!"
    "This is really fishy, but so far Billy's been nothing but nice to me, and Per didn't question him further once he heard his explanation."
    "I'll just go along with his plan."
    billy "So, you got any questions before we enter? Nice city, isn't it?"

    $ bq1seen = False
    $ bq2seen = False
    window hide
    label BillyQuestions1:
        window hide
        menu:
            "Tell me about yourself!" if bq1seen == False:
                window show
                me "Tell me about yourself!"
                show bill surpriseface at left:
                    yalign 0.4 xalign -0.08
                with dissolve
                billy "!"
                billy "..."
                show bill baseface with dissolve

                billy "Sure!"
                billy "Summer is my favorite season of the year. I just love all the pretty flowers and bugs!"
                show bill laughface with dissolve
                billy "It gets a little sweaty, but there's a lot of tasty things to drink to cool off! I personally really adore apple juice."
                billy "I told you earlier how I love carrots, they're my favorite vegetable! "
                billy "That said, I don't really like carrot juice! I prefer something much sweeter to drink!"
                billy "Sweet drinks are great, and there's so many good choices!"
                billy "Hot chocolate is the one thing making the winter tolerable!"
                show bill casualface with dissolve
                billy "Chocolate is great and warm drinks are so cozy on a cold night!"
                "He just keeps talking about food."
                me "I was curious about how you got into guard work? You don't really strike me as the type!"
                show bill surpriseface  with dissolve
                billy "O-oh!"
                show bill baseface with dissolve
                billy "My family has been in the military for generations. "
                billy "And I was always big for my age and told to protect the smaller piggies!"
                billy "So going on to become a guard seemed like the perfect fit for me! "
                show bill laughface with dissolve
                billy "And best of all, military life comes with a free buffet thrice a day!"
                billy " That’s breakfast, lunch, AND dinner!"

                billy "The one thing that's lacking is good desserts, but I just buy some with the money I make!"
                "Aand he's back to talking about food..."

                $ bq1seen = True
                show bill baseface with dissolve
                jump BillyQuestions1
            "Tell me about the city!" if bq2seen == False:
                window show
                me "Tell me about the city!"
                show bill casualface at left:
                    yalign 0.4 xalign -0.08
                with dissolve
                billy "Sure! This is Hog Haven, the capital of this great kingdom!"
                billy "The city is well known for its imports of various wares from all over the world!"
                billy "And the farmland just outside the gates provides us with a constant supply of fresh produce! "
                show bill laughface with dissolve
                billy "But you know all about that, being one of the great farmers!"
                "I know the sight of endless farmlands all too well..."
                me "There's one thing I've always wondered."
                me "Why is the city so heavily defended?"
                me "The gates are massive with lots of guards, but things seem pretty peaceful outside."
                show bill surpriseface with dissolve
                billy "This city was originally just a small fort built right before the Wolf Wars started."
                show bill baseface with dissolve
                billy "But the location turned out to be ideal, and the fort quickly expanded into this thriving city!"
                billy "So the emphasis on defense has been core to this place since the very beginning, making it a real safe haven for us hogs just like the name implies!"
                me "I never knew, thanks for telling me!"
                "The Wolf Wars finally ended just before I was born. They're the main reason why humans ended up spread thin all across the world. "

                $ bq2seen = True
                jump BillyQuestions1

            "{alpha=*0.8}Continue{/alpha}" :

                pass
        window show

    #General Questions about age of city, the fountain, Billy himself.
    me "That should be it! "
    billy "Great! Now let's see how this helmet fits!"

    window hide
    $ renpy.pause(0.5, hard=True)
    hide bill baseface
    show billy base
    show helmet:
        alpha 0.0
        alpha 1.0
    with dissolve
    play sound "audio/soundFX/Get.mp3"
    show blackshake at truecenter behind bg
    with vpunch
    pause 1.0
    show billy base at left:
            yalign 0.4 xalign -0.08
            linear 0.2 yalign 0.13 xalign -0.02
    pause 0.5

    show billy casualaugh:
        yalign 0.13 xalign -0.02

    with dissolve
    window show
    billy "Perfect! We're brothers in arms now, haha! *grunt*"
    "This helmet is way too big for me! There's a ton of empty space all around my head."
    "I imagine pigs need some space for those thick necks, double chins and big jowls."
    "The eye holes are a good distance apart so I can still see, but my eyes are so far from the holes that my vision is limited!"
    billy "So! You go first and I'll have your back, [Protagonist]!"
    show billy casual
    hide bill laughface
    with dissolve
    billy "Let me do all the talking, and we'll get through in no time!"
    show billy finger with dissolve
    billy "Oh, and one last thing!"
    billy "If anyone asks you any questions on the way in, I’ll tell you what to answer like this-"
    show billy base with dissolve
    play sound "audio/soundFX/poke_1.wav"
    "Billy pokes me with his finger."
    show billy finger with dissolve
    billy "One tap means \"yes\"."
    billy "And two taps means \"no\"!"
    show billy base with dissolve
    billy "Ya got it?"
    me "Okay, that sounds easy enough."
    "Billy inhales deeply and holds it for a few seconds before exhaling."
    show billysurpriseface behind helmet with dissolve:
        yalign 0.13 xalign -0.02

    billy "Well alright, let's do it!"
    "I slowly waddle my way towards the building to my right, making sure the helmet doesn't fall off."

    window hide
    scene stairs
    show helmet
    with fade
    window show
    $ lars_name = "???"
    "We're right by the door, and I can see a flight of stairs inside."
    show lars base at left behind helmet with easeinleft:
            yalign 0.4 xalign -0.4

    lars "Morning, Billy!"
    billy "Heya, Lars!"
    $ lars_name = "Lars"
    "Another guard shows up! He's got a big smile and a friendly tone to his voice."
    lars "And who's this? New recruit?"
    billy "S-sure is!"

    play sound "audio/soundFX/poke_1.wav"
    "Billy pokes my back once, urging me to say yes."
    "We're lying right off the bat?!"
    me "Yes!"
    "Lars reaches out to shake my hand."
    show lars laugh with dissolve
    lars "Well, what's your name, recruit?"
    me "..."
    play sound "audio/soundFX/poke_1.wav"
    "Billy taps my back a single time again."
    me "Y-yes!..."
    show lars concern with dissolve
    lars "Your name's... yes?"
    "Shit, I don't know what to do!"
    play sound "audio/soundFX/poke_2.wav"
    "Billy taps my back twice!"
    me "No!"
    lars "Then what is it?"
    play sound "audio/soundFX/poke_3.wav"
    "Billy pokes my back lots of times!"
    me "I... Uuuuhh..."
    show blackshake at truecenter behind bg


    window hide
    menu:
        with dissolve
        "I'm [Protagonist]!":
            window show
            me "I'm [Protagonist]!"
            show lars base with dissolve
            lars "Ah! Nice to meet ya, [Protagonist]!"
            "I reach my hand out, and he gives it a firm, eager shake."
            window hide
            play sound "audio/soundFX/Get.mp3" volume 0.3
            with vpunch
            pause 0.3
            window show


        "Quickly make up new a pig guard alias name!":
            window show
            "Oh crap, think quickly!... What's a good name for a pig?"
            $ liename = True
            window hide
            menu:
                with dissolve
                "Oinky":
                    $ lie_name = "Oinky"
                    window show
                    me "Oinky."
                    lars "Oinky?!"
                    lars "*Ahem* I mean... That's one I haven't heard before!"
                    show lars laugh with dissolve
                    lars "Only ever heard piglets make a noise quite like that! "
                    lars "Did ya happen to name yourself? Mwahaha!"
                "Chubbs" :
                    $ lie_name = "Chubbs"
                    window show
                    me"It's Chubbs."
                    lars "Chubbs?!"
                    lars "That's definitely... A name."
                    show lars laugh with dissolve
                    lars "Gotta say you don't live up to it! "
                    lars "At least not next to big boys like me and Billy! Hah!"
                "Hamlet" :
                    $ lie_name = "Hamlet"
                    window show
                    me"Hamlet."
                    lars "Hamlet?!"
                    lars "Never heard that name before!"
                    lars "Why'd your folks name you that?"
                    window hide
                    menu:
                        with dissolve
                        "I burn easily.":
                            window show
                            me"I burn easily."

                        "I took a real liking to my mom growing up.":
                            window show
                            me"I took a real liking to my mom growing up."

                        "I was named after my father, the king!":
                            window show
                            me "I was named after my father, the king!"

                    play sound "audio/soundFX/poke_4.wav"
                    "Billy frantically pokes my back!"
                    billy "Hah.. Haa haa! This one's a real joker!"
                    lars "..."
                    show lars laugh with dissolve
                    lars "Heh...Hah...Mwahaha!"
            show lars strange with dissolve

            "Lars gives Billy a questioning look. "
            billy "He's not from this kingdom, you see! His name's... really common where he's from!"
            show lars base with dissolve
            lars "O-Oh, I see!"
            lars "Well, it's nice to meet ya... [lie_name]!"
    show lars base with dissolve


    lars "Been a while since we had a new recruit in this district!"
    lars "Welcome to the team!"
    me "Th-Thank you!"

    show lars laugh with dissolve
    lars "Other than Billy there's just a bunch of jaded old-timers around here! Haha!"

    billy "Absolutely!"
    billy "It's his first day so I'm just showin' him around the city!"
    show lars base with dissolve
    lars "Aha!"
    lars "I remember my own first day as a guard. "
    lars "A lot to take in for sure, but you'll get the hang of it in no time!"

    "I don’t know what Billy was so worried about!"
    "Lars is about the same size as Per, but all-around more pleasant. "
    "I don't imagine he'd react much worse to me being human."

    billy "I was just about to give him a tour of the royal quarters!"
    show lars laugh with dissolve
    lars "Oh, I see! Go right ahead!"
    #expression changes and screen shake and foot noises.
    stop music fadeout 0.1
    show blackshake at truecenter
    window hide
    play sound "audio/soundFX/Step1.wav"
    with vpunch
    $ renpy.pause(0.9, hard=True)
    play sound "audio/soundFX/Step2.wav"
    with vpunch
    $ renpy.pause(0.9, hard=True)
    play sound "audio/soundFX/Step1.wav"
    with vpunch
    show lars strange with dissolve
    window show
    "...What are those footsteps?"
    "Billy and Lars both tense up as they get closer."
    window hide
    play sound "audio/soundFX/Step2.wav"
    with vpunch
    $ renpy.pause(0.7, hard=True)
    play sound "audio/soundFX/Step1.wav"
    with vpunch
    $ renpy.pause(0.7, hard=True)
    play sound "audio/soundFX/Step2.wav"
    with vpunch
    show lars scared
    with dissolve
    show rolfshadow at right behind helmet:
        yalign 0.75 xalign 1.8
    show rolf base at right behind helmet,rolfshadow:
        yalign 0.75 xalign 1.8
    show rolfbeer at right behind helmet:
        yalign 0.75 xalign 1.8
    with easeinright
    play music "audio/7.+Stöðvar+-+320bit.mp3" fadein 0.1 volume 1.0

    show rolf knuckles with dissolve
    window show

    $ rolf_name = "?!?"

    rolf "What's goin' on here?!"
    "!!!"
    "Th-that's by far the biggest pig I've ever seen!"
    show rolf base with dissolve
    "He’s gruff, and reeks of alcohol."

    lars "G-Good morning, Rolf!"
    $ rolf_name = "Rolf"
    billy "M-Morning, uncle!"
    "He's Billy's uncle? That explains his size!"
    show rolf concern with dissolve
    rolf "So, who the hell is THIS?"
    "He motions towards me."
    if liename == False:
        show lars strange with dissolve
        lars "Th-This is our latest recruit, [Protagonist]! "
        show rolf knuckles with dissolve
        rolf "We're recruiting TWIGS now?!"
        show lars weird with dissolve
        rolf "Where's the rest of his armor? I bet it'd flatten him!"
        window hide
    else:
        show lars strange with dissolve
        lars "This is our new recruit! His, uuh... His name's [lie_name]."
        show rolf gross with dissolve
        rolf "[lie_name] ?! What mockery of a name is that?! "
        "Billy moves to my side."
        "It seems we've dropped the whole back-poking plan after it made things messy with Lars!"
        show lars weird with dissolve
        lars "R-Rolf... He's not from around here, you see!"
        show rolf knuckles with dissolve
        rolf "Just look at him! We're recruiting TWIGS now?!"
        rolf "And where's the rest of his armor? I bet it'd flatten him!"
        window hide
    menu:

        with dissolve

        "I'm quick and nimble, I don't need armor!":
            window show
            me  "I'm quick and nimble, I don't need armor!"
            rolf "Huh?! Stand too close and a SNEEZE could kill ya, twig!"

        "I haven't had breakfast today, that's why I'm looking a bit thin. ":
            window show
            me "I haven't had breakfast today, that's why I'm looking a bit thin."
            rolf "Looks like you haven't had a plate of breakfast your whole life!"

        "You're not carrying your full armor either!":
            window show
            me "You're not carrying your full armor either!"
            rolf "My HIDE is thicker than your whole damn body, twig!"

    billy "He's from outside the city, so he hasn't had a chance to bulk up yet!"
    billy "Not everyone has access to a buffet three times a day like us guards!"
    show rolf gross with dissolve
    rolf "Ugh!"
    rolf "Back in my day you needed some damn muscle and toughness to be a guard! 'Wasn't just an easy gig for free grub!"
    "Rolf takes a drink from his heavy mug."
    hide rolfbeer
    show rolf beer
    with dissolve
    rolf "And this fuckin' heat... I'm gonna need another beer..."
    show rolf drink with dissolve
    "He downs it all in one big gulp, spilling beer over his neck and chest before belching loudly-"

    show rolf burp with dissolve
    play sound "audio/soundFX/FX2/pig-scream-loud-oink.wav"
    with vpunch
    rolf "*BWRAAP!*"
    show rolf beer2 with dissolve
    rolf "You boys better toughen this one up, or I'll do it myself!"
    lars "..."
    billy "..."
    hide rolf
    hide rolfshadow
    with easeoutright
    "As Rolf walks past me he smacks the butt of his keg against the side of my helmet-"
    window hide
    stop music fadeout 0.1
    play sound "audio/soundFX/Helmet_bonk_2.wav"
    with hpunch
    with Pause(0.5)
    window show
    "My brain rattles and I do my best stay upright."
    "Now I see why this helmet might've been a good idea!"
    show lars concern with dissolve
    play music "audio/Tavern+Brawl+-+320bit.mp3" fadein 10.0 volume 0.3
    lars "Well now..."
    if liename == False:
        lars "Sorry about that, [Protagonist]."
    else:
        lars "Sorry about that, [lie_name]."


    me "D-Don't worry about it!"
    show lars base with dissolve
    lars "Alright!"
    lars "And hey, you've still got a tour to look forward to!"
    lars "Hope you enjoy the sights, 'twas nice meeting ya!"
    me "Nice to meet you too!"
    billy "See ya later, Lars!"

    scene black with fade
    "I follow Billy as we stumble our way up the stairs and down a few hallways."

    window hide
    scene door
    show helmet

    show billy base at left behind helmet:
        yalign 0.4 xalign -0.08
    with fade
    window show
    billy "We're finally here!"
    billy "Now, let's get this off."
    play sound "audio/soundFX/Get.mp3"
    hide helmet with dissolve
    "He lifts my helmet and exposes my sweaty forehead."
    me "*Puaah!*"
    me "That was damn scary back there, Billy!"
    me "You should've told me about the whole \"new recruit\" angle! "
    me "If I knew I could've prepared better!"
    show billy wary with dissolve
    billy "I panicked!"
    billy "I'm a terrible liar so I just went with Lars' assumption!"
    show billy clench with dissolve
    billy "...Sorry."
    if liename == True:
        show billy base
        show billysurpriseface:
            yalign 0.4 xalign -0.08
        with dissolve
        billy "And you scared the heck out of me with the whole fake name thing!"
        show bill casualface:
            yalign 0.4 xalign -0.08
        with dissolve
        billy "\"[lie_name]\", really?"
        show billy belly
        show bill laughface:
            yalign 0.4 xalign -0.08
        hide billysurpriseface
        with dissolve
        billy" Hahaha!"
        "I can't help but join in with a chuckle as I shake my head."
        me "Guess I panicked too."
        show bill surpriseface  with dissolve:
            yalign 0.4 xalign -0.08
        billy "...Unless..."
        billy " \" [lie_name] \" is your real name... and \" [Protagonist] \" is your fake name!"
        hide bill surpriseface
        with dissolve
        billy "... Hmm..."

        show billy base
        with dissolve
        billy "But anyways, I think all in all we did pretty good back there!"

    else:
        show billy base
        show billysurpriseface:
            yalign 0.4 xalign -0.08
        with dissolve
        billy "At least uncle Rolf didn't find out about you being a human!"
        me "He doesn't seem very welcoming to new people."
        billy "Well, he's a little... {i}old-fashioned{/i}, is all!"
        hide billysurpriseface
        show billy casual
        with dissolve
        billy "Spending most of your life in the military will do that to ya!"
        me "I see."
        billy "But hey, all in all we did pretty good back there!"
    show billy high with dissolve
    "Billy holds his hand up for a high five."
    $ Friendship = 0
    window hide
    menu:
        with dissolve
        "High five!":


            #High five sound#
            play sound "audio/soundFX/Slap.wav"
            show billystar:
                yalign 0.4 xalign -0.08
            show blackshake at truecenter
            with hpunch
            window show
            $ Friendship +=1

            "Our hands clash with a satisfying SMACK!"
            hide billystar with dissolve
            show bill laughface:
                yalign 0.4 xalign -0.08
            show billy clench
            with dissolve
            billy "Oww yeah!"
            hide bill laughface
            show billy casual
            show bill baseface:
                yalign 0.4 xalign -0.08
            with dissolve
            billy "But enough celebrating, It's time I get you to your destination!"

        "Leave him hanging.":
            window show
            "..."
            show bill sadface with dissolve:
                yalign 0.4 xalign -0.08
            "Billy lowers his hand to my shoulder, offering a couple of reassuring pats instead."
            show billy clench with dissolve
            billy "I'll try to inform you better going forward! "
            hide bill sadface
            show billy base
            with dissolve
            billy "Speaking of which, it's time I get you to your destination!"

    show billy finger with dissolve
    billy "We're going in here! "
    "He points towards the ornate door."
    show billy base with dissolve
    billy "Just make sure to be polite, no swearing or naughty words... And hmmm..."
    window hide
    play sound "audio/soundFX/Swipe Clothes.wav"
    pause 1.0
    window show
    "Billy gives me a quick pat-down, shaking the dirt and dry mud out of my overalls."
    show billy casual
    hide bill baseface
    with dissolve
    billy "And you're all good!"
    play sound "audio/soundFX/OpenDoor 1.wav"
    pause 0.4
    stop music fadeout 1.0
    "He opens the door before circling around and pushing me through."
    window hide
    jump emelieintro

    "END OF \"SCRIPT\" FILE"


label navigate:
    window hide
    menu:

        with dissolve
        "Play normal":
            window show
            "Playing normal."
            jump normalgame
        "Jump to emelieintro":
            window show
            "Playing emelieintro."
            jump emelieintro
        "Jump to handjobmassage":
            window show
            "Playing massage."
            jump handjobmassage
        "jump to cumtits":
            window show
            "Playing cumtits"
            window hide
            menu:
                "I lied to Lars about my name.":
                    $ liename = True
                    $ lie_name = "Hamlet"
                    window show
                    "I lied to Lars about my name, he and Rolf know me as [lie_name]."
                    $ emelie_name = "Emelie"
                    $ lars_name = "Lars"
                    $ rolf_name = "Rolf"
                    $ billy_name = "Billy"

                    jump cumchoice

                "I told Lars my real name.":
                    window show
                    "I did not lie about my name, it's just [Protagonist]."
                    $ liename = False

                    $ emelie_name = "Emelie"
                    $ lars_name = "Lars"
                    $ rolf_name = "Rolf"
                    $ billy_name = "Billy"
                    jump cumchoice

        "Jump to interrogation":
            $ liename = True
            $ lie_name = "Hamlet"
            window show
            "Playing interrogation, Lars and Rolf know me as [lie_name]."
            "I also came on EMelie's face."
            $ cumface = True
            $ emelie_name = "Emelie"
            $ lars_name = "Lars"
            $ rolf_name = "Rolf"
            $ billy_name = "Billy"

            jump interrogation

        "Jump to passquestions":
            $ perfscore = True
            $ liename = True
            $ lie_name = "Hamlet"
            window show
            "I came on face and got perf score."
            $ cumface = True
            $ emelie_name = "Emelie"
            $ lars_name = "Lars"
            $ rolf_name = "Rolf"
            $ billy_name = "Billy"
            $ HardQuestions = True
            $ Failed +=1


            jump passquestions

        "Jump to Bath":
            $ perfscore = True
            $ liename = True
            $ lie_name = "Hamlet"
            window show
            "Playing Bath, Lars and Rolf know me as [lie_name]."
            "I also came on Emelie's face."
            $ cumface = True
            $ emelie_name = "Emelie"
            $ lars_name = "Lars"
            $ rolf_name = "Rolf"
            $ billy_name = "Billy"

            jump Bath


        "Jump to after CH2":
            $ perfscore = True
            $ liename = True
            $ lie_name = "Hamlet"
            window show
            "Playing Bath, Lars and Rolf know me as [lie_name]."
            "I also came on Emelie's face."
            $ cumface = True
            $ emelie_name = "Emelie"
            $ lars_name = "Lars"
            $ rolf_name = "Rolf"
            $ billy_name = "Billy"

            jump afterch2

        "Next.":
            "Next."


label navigate2:
    $ buttprodsuccess = True
    $ perfscore = True
    $ liename = True
    $ lie_name = "Hamlet"
    $ cumface = True
    $ emelie_name = "Emelie"
    $ lars_name = "Lars"
    $ rolf_name = "Rolf"
    $ billy_name = "Billy"
    $ moom_name = "Moose Man"
    $ moog_name = "Moose Lady"
    $ deem_name = "Deer Guy"
    $ deeg_name = "Deer Girl"
    $ vic_name = "Victoria"

    window hide
    menu:
        with dissolve
        "Play normal":
            window show
            "Playing normal "
            jump normalgame


        "Play DinnerDay":
            window show
            "Playing DinnerDay."
            menu:
                "I read scary book.":
                    $ scarybook = True

                    jump DinnerDay

                "I read sex book.":
                    $ scarybook = False

                    jump DinnerDay
        "Play Dessert":
            window show
            "Granny is Granny."
            $ GrannyName = True
            scene bg cafe
            show cafetable
            with dissolve
            jump dessert
        "Play Blowjob":
            window show
            "Playing Blowjob Scene."
            jump beejstart

        "Play AfterBlowjob":
            window show
            $ GrannyName = True
            $ roughbj = True
            $ Grub = True
            "Playing After Blowjob Scene."
            "Bj was rough, Granny is Granny. "
            " I ate a grubstick "
            jump afterbeejay

        "Play AfterSmithy":
            window show
            $ GrannyName = True
            $ roughbj = True
            $ Grub = True
            "Playing After Smithy."
            "Bj was rough, Granny is Granny. "
            " I ate a grubstick "
            jump aftersmithy

        "Play Vicboobscene":
            window show
            $ GrannyName = True
            $ roughbj = True
            $ Grub = True
            "Playing vic boobascene."
            "Bj was rough, Granny is Granny. "
            " I ate a grubstick "
            jump vicboobscene

        "Play AfterCh3":
            window show
            $ GrannyName = True
            $ roughbj = True
            $ Grub = True
            $ vicmilk = True
            "Playing vic boobascene."
            "Bj was rough, Granny is Granny. "
            " I ate a grubstick "
            jump afterch3

        "Jump ch4. ":
            window show
            $ Friendship = 4
            jump ch4

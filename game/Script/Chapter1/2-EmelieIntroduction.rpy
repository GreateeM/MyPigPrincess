label emelieintro:
    scene emelieroom with fade
    window show
    $ emelie_name = "???"
    $ billy_name = "Billy"
    play music "audio/starting-out-waltz-vivace-by-kevin-macleod-from-filmmusic-io.mp3" fadein 0.1 volume 0.3
    billy "We're here!"
    "Oh wow, this room is so pretty!"
    window hide

    show em normal behind emf at right with easeinright:
        yalign 0.0
        zoom 0.90
    pause 0.4
    window show
    "!!"
    "And so is she!"
    $ emelie_name = "???"

    show emf smile at right:
        yalign 0.0
        zoom 0.90

    show emear high at right:
        yalign 0.0
        zoom 0.90
    with dissolve


    emelie "Woah! You really found one!!"
    window hide

    show billy base at left with easeinleft:
            yalign 0.4 xalign -0.08
    pause 0.2
    window show
    billy "Yes, yes! You know I always deliver, princess!"
    $ emelie_name = "Princess?"
    show em proper
    show emf normal
    show emeye side1 at right:
        yalign 0.0
        zoom 0.90
    with dissolve
    emelie "You sure do! I knew I could trust you with this!"


    emelie "You can leave on a well deserved break now, Billy!"
    show billy wary with dissolve
    billy "B-But princess! I don't think I should leave you all alone with an outsider-"
    show em hips behind emf
    show emf normalblush
    with dissolve

    emelie "Oh it's fine, Billy! Just wait outside and I'll shout if I need ya!"
    show emf smile
    show emeye side2 at right:
        yalign 0.0
        zoom 0.90
    with dissolve
    emelie "And guess what? I just told granny to bake you your favorite thing...!"
    show billy clench
    show billybaseface:
        yalign 0.4 xalign -0.08
    with dissolve
    billy "Hm?"
    hide emf bigsmile
    show emeye side1
    with dissolve
    emelie "Carrot cake!"
    show em normal
    hide emear
    with dissolve
    emelie "It should arrive right outside the door in just a minute or so, you don't wanna miss it!"
    show billy laugh
    hide billybaseface
    with dissolve
    billy  "Oh, wow!"
    billy "You're the best, princess! I'll be right outside!"
    window hide
    play sound "audio/soundFX/Run.mp3"

    show billy:
        yalign 0.4 xalign -0.08
        linear 0.5 yalign 0.4 xalign -2.08
    $ renpy.pause(0.2, hard=True)
    hide billy with dissolve
    window show
    "Billy bolts out of the room with excitement."
    billy "Talk to ya later, buddy!"
    play sound "audio/soundFX/Door Slam.wav"
    "The door slams shut." with vpunch
    hide emeye with dissolve
    show em normal at right:
        yalign 0.0 zoom 0.90
        linear 0.2 yalign 0.15 zoom 1.0

    "She steps a bit closer."

    show em normal at right:
        yalign 0.15
        zoom 1.0

    show emf smile at right:
        yalign 0.15
        zoom 1.0
    with dissolve
    emelie "You're not as tall as I expected!"
    window hide
    menu:
        with dissolve
        "What did you expect?":
            window show
            me "What did you expect?"

            show em proper
            show emf normal
            with dissolve
            emelie "I've never met a human before so I wasn't really sure!"
            emelie "I was guessing maybe 8 feet or so!"
            show emf laugh with dissolve
            emelie "And overflowing with muscles, haha! *snort*"

        "Neither are you!":
            window show
            me "Neither are you!"
            hide emf smile
            show em grumpy
            with dissolve
            emelie "H-hey! I'm average height! At least for a piggy!"
            me "And I'm pretty average for a human! I think... It's been a while since I last saw one."
            show em normal with dissolve
            emelie "Hmm, well... You're the first human I've ever met, so I guess I'll take your word for it!"
            show emf smile at right:
                yalign 0.15
                zoom 1.0
            with dissolve
            emelie "You'd be really tall if you were a piggy! Rolf and Billy are the only pigs I can think of who're taller."
        "I'm pretty tall!":
            window show
            me "I'm pretty tall!"
            hide emf smile
            show em think
            with dissolve
            emelie "Hmm you're the first human I've met so I guess I'll have to take your word for it!"
            show em normal
            show emf smile at right:
                yalign 0.15
                zoom 1.0
            with dissolve
            emelie "You'd be really tall if you were a piggy! Rolf and Billy are the only pigs I can think of who're taller."

    hide emf
    show em out at right:
        yalign 0.15
        zoom 1.0
    with dissolve
    emelie "!"
    emelie "Oh, how rude of me!"
    show em wave with dissolve
    emelie "I'm Emelie! Nice to meet'cha!"
    $ emelie_name = "Emelie"
    emelie " Sorry for the late introduction!"
    show em proper with dissolve
    emelie "What's your name? ...If humans have names, that is."
    window hide
    menu:
        with dissolve
        "Introduce myself with a handshake.":
            window show
            me "We do have names. Mine's [Protagonist]!"
            "I present my hand and Emelie begins reaching for it."
            show em normal
            show emf pout at right:
                yalign 0.15
                zoom 1.0
            with dissolve
            emelie " [Protagonist], huh? Gosh, that’s not as crazy as I thought!"
            emelie "Unless you’ve got some funny way of spelling it?"
            show emf laugh at right:
                yalign 0.15
                zoom 1.0
            with dissolve
            emelie "I know what that’s like. "
            emelie "People spell my name wrong ALL the time, you know. "
            emelie " It’s E-M-E-L-I-E!"
            show emf normal with dissolve
            "Her hand finally grips mine with a gentle squeeze. "
            "It’s small and soft, with dainty, manicured fingers. I’m a little self-conscious of my calluses all of a sudden."
            window hide
            menu:
                with dissolve
                "Kiss her hand":
                    window show
                    me "*Smooch* "
                    show em out
                    show emf insecure
                    show emblush at right:
                        yalign 0.15
                        zoom 1.0
                    with dissolve
                    emelie "W-Wow! You're really oldschool, haha!"
                "Shake her hand":
                    "I give her hand a gentle shake before letting go."



        "Introduce myself with a bow.":
            window show
            me "We do have names! Mine's [Protagonist]!"

            "I do a little bow the way we do at the farm."
            show emf laugh at right:
                yalign 0.15
                zoom 1.0
            with dissolve

            "Emelie grins."

            show em out
            show emf smile
            with dissolve
            emelie "[Protagonist], huh? I expected something really crazy sounding!"
            emelie "Maybe it's got a unique human way of spelling it!"
            show emf laugh at right:
                yalign 0.15
                zoom 1.0
            with dissolve
            emelie "People spell my name wrong all the time. It's E.M.E.L.I.E!"
            show emf normal with dissolve
            emelie "You need to teach me that human bowing technique later! It's very interesting."

    hide emblush
    show em proper
    show emf insecure at right:
        yalign 0.15
        zoom 1.0
    with dissolve
    emelie "I hope being brought here wasn't too big of a disturbance!"
    if ComeAlong == "neutral":
        me "It's okay! I'm just really curious what this is all about."
        me "I tried to ask Billy, but all he said was I needed to \"clear something up\". "

    if ComeAlong == "break":
        me "It's okay, I needed a break from work anyways! "
        me "But I'm still just really curious what this is all about."

    if ComeAlong == "paid":
        me "As long as nobody steals my cart of veggies while I'm gone I should be good!"
        me "Actually, Billy said that in the worst case scenario he'd pay me with some carrot cake..."
        show em hips
        hide emf
        with dissolve
        emelie "Really? Haha I'm pretty sure he's already done eating it all right outside the door!"
        emelie  "If anything happens to your cart I'll compensate you for the trouble!"
        me "That's nice to know! I'm still just really curious what this is all about."
    show em normal
    hide emf
    with dissolve
    emelie "Well, see, I need a human to clear something up for me! "
    emelie "Any human would do, but... It seems you’re the only one in the whole kingdom! "
    emelie "So... without further ado... "
    emelie "The big question I've brought you here to answer is..."
    "Here it comes, I really hope I'm not in trouble!"
    window hide
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
    pause 0.2
    $ renpy.music.set_volume(0.20, delay=0, channel='music')
    pause 0.2
    $ renpy.music.set_volume(0.10, delay=0, channel='music')
    pause 0.2
    $ renpy.music.set_volume(0.00, delay=0, channel='music')
    window show
    show em grin at right:
        yalign 0.15 zoom 1.0
        linear 0.2 yalign 0.15 zoom 1.05

    $ renpy.pause(0.2, hard=True)

    play sound "audio/soundFX/Dun.wav"

    emelie "Just what exactly..."
    window hide
    $ renpy.pause(0.2, hard=True)


    show em grin  at right:
        yalign 0.15 zoom 1.05
        linear 0.2 yalign 0.15 zoom 1.10

    $ renpy.pause(0.2, hard=True)
    play sound "audio/soundFX/Dun.wav"

    window show
    emelie "... are..."
    window hide
    $ renpy.pause(0.2, hard=True)

    show em grin at right:
        yalign 0.15 zoom 1.10
        linear 0.2 yalign 0.15 zoom 1.20
    pause 0.1
    show em grin2 at right:
        yalign 0.15 zoom 1.20
    with dissolve
    window show
    $ renpy.pause(0.2, hard=True)
    play sound "audio/soundFX/Dun.wav"
    emelie "TOES?"
    window hide
    pause 1.0
    window show
    me "... What?"
    window hide
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
    $ renpy.music.set_volume(0.90, delay=0, channel='music')
    pause 0.1
    $ renpy.music.set_volume(1.00, delay=0, channel='music')
#PauseStatement^
    show em grin2 at right:
        yalign 0.15 zoom 1.15
        linear 0.2 yalign 0.15 zoom 1.0
    pause 0.1

    show em normconcern at right:
        yalign 0.15
        zoom 1.0
    with dissolve
    window show
    emelie "You don't know either?! Gosh!"
    me "No... wait... "
    me "Are we thinking of the same thing? Toes?"
    show em proper
    show emf pout at right:
        yalign 0.15
        zoom 1.0
    with dissolve
    emelie "Yes, yes! Toes! "
    emelie "I read it's something humans have, but what exactly ARE they?"
    me "Oh. Well... "
    me "They're kinda like fingers, I guess. But for our feet."

    show em out
    show emf weirdo2
    with dissolve
    emelie "...What?!"
    show emf wide with dissolve
    emelie "That's weird! "
    emelie "Can you grab stuff with them?!"
    show emf weirdo
    show emeye down at right:
        yalign 0.15
        zoom 1.0

    with dissolve
    "She looks down towards my feet."
    emelie " Hmm..."
    show em think
    hide emf
    hide emeye
    with dissolve
    emelie "Why would you be wearing shoes if that's the case?"
    window hide
    menu :
        with dissolve
        "To protect them.":
            window show
            me "To protect them."
            me "Stepping on a sharp rock hurts a ton! And if you step on some rusty metal or something you could get an infection."
            show em normal with dissolve
            emelie "That makes sense!"

        " *Tease* Toes are very private! Humans only show them to people they really trust!":
            window show
            me "Toes are very private! Humans only show them to people they really trust!"
            show em out with dissolve
            emelie "R-Really??"
            show emf insecure at right:
                yalign 0.15
                zoom 1.0
            with dissolve
            emelie "Huh... I've heard about foot fetishes before but I had no idea humans all hide their feet for decency."
            show em think
            hide emf
            with dissolve
            emelie "Wait, does that mean..."
            show emblush at right:
                yalign 0.15
                zoom 1.0
            show emeye scared at right:
                yalign 0.15
                zoom 1.0
            with dissolve
            emelie "There's lingerie for toes, too?? "
            "I crack up at her question."
            show em out
            hide emeye
            hide emblush
            with dissolve
            me "Haha, there sure is!"
            emelie "..."
            show em hips with dissolve
            emelie "You're messing with me! You almost had me there for a second!"
            emelie "Good one... I'll have to get you back sometime."
            $ toes = "private"
    hide emf
    show em proper
    with dissolve
    emelie "So, you got me all curious now!!"
    emelie "Do you think you could... show me these toes?"
    "Is the princess really asking to see my dirty farmer toes right now? This day just gets weirder and weirder."
    "I'll do what she asks. She seems extremely curious for whatever reason."
    me "Sure, give me a second."
    window hide

    show blackopacity
    show feet
    with dissolve
    play sound "audio/soundFX/crack_1.wav"
    pause 0.3
    window show
    "My back cracks strangely as I bend over."
    me "Let's just get these off."
    play sound "audio/soundFX/Get.mp3"
    show feetbare
    with dissolve
    hide feet
    "Phew... Let's hope she doesn't want to smell 'em too."
    me "There we go! "
    window hide
    hide feetbare
    hide blackopacity
    with dissolve
    pause 0.2
    show em panic
    show emeye scared at right:
        yalign 0.15
        zoom 1.0
    with dissolve
    window show
    emelie "WHAA!"
    emelie "THEY REALLY ARE LIKE FINGERS!!"
    emelie "But extra stubby!"
    hide emeye
    show em out
    show emf weirdo2 at right:
        yalign 0.15
        zoom 1.0
    with dissolve
    emelie "You've got four hands, mister!"
    show emf wide
    with dissolve
    emelie "Wait..."
    emelie "Does that mean... humans have 4 arms?! Is a leg only a leg if it ends in a foot?"
    hide emf
    show em think
    with dissolve
    emelie "If you had feet for hands, would your arms be considered legs??"
    "Her mind is racing."
    show em normal
    show emf gross at right:
        yalign 0.15
        zoom 1.0
    with dissolve
    emelie "So now I know... toes are just... foot fingers... CREEPY!"
    window hide
    menu:
        with dissolve
        "What kinda feet do you have then?...":
            window show
            me "What kinda feet do you have then?..."
            show em normal
            hide emf
            with dissolve
            emelie "Normal ones!"
            emelie "Okay, have a look..."
            $ feet = "normal"

        "Don't call them creepy! I bet YOUR feet are creepy!":
            window show

            me "Don't call them creepy! I bet YOUR feet are creepy!"
            hide emf
            show em grumpy
            with dissolve
            emelie "No way! I'll show you!"
            $ feet = "creepy"
    show em normal
    show emf bigsmile at right:
        yalign 0.15
        zoom 1.0
    with dissolve
    emelie "Who needs toes when you have..."
    "Emelie proudly steps out of one of her high heels."
    window hide
    show blackopacity
    show emfoot
    with dissolve
    pause 0.5
    window show
    emelie "Hooves!"
    me "..."
    "I already knew that pig feet looked different. "
    me "Aren't those toes? Two on each foot?"
    emelie "No, these are cloven hooves!"
    emelie "Pig hooves generally have two \"nails\" at the front. Some have four in total with two extra nails around the heel!"
    emelie "Horses, on the other hand, don't have nails. They just have one big chunky hoof at the front of their feet!"
    "That's confusing."
    me "Huh... I guess us humans use different words for this stuff."

    emelie "So... What do you think?"
    if feet == "normal":
        emelie "Perfectly normal feet, right?"
    if feet == "creepy":
        emelie "Not creepy at all, right?"
    window hide
    hide emfoot
    hide blackopacity
    with dissolve

    menu:
        with dissolve
        "I guess they're kinda cute." :
            window show
            me "I guess they're kinda cute."
            hide emf
            show em hips
            with dissolve
            emelie "Aww, thank you!"
            emelie "..."
            show em insecure
            show emf concern at right:
                yalign 0.15
                zoom 1.0
            with dissolve
            emelie "Wait, now I feel bad for calling yours creepy..."
            emelie "Sorry about that. I got a bit surprised is all!"
            emelie "'Wasn't sure what to expect!"
            me "No worries."
        "They're totally creepy. " :
            window show
            me "They're totally creepy. "
            hide emf
            show em hips
            with dissolve
            emelie"Hahaha, no way!"
            emelie "..."
            show em insecure
            show emf concern at right:
                yalign 0.15
                zoom 1.0
            with dissolve
            emelie "Maybe they are kinda creepy..."
            emelie "..."
            hide emf
            show em normal
            with dissolve
            emelie "I shouldn't have called your toes creepy! I guess we're just different! "
    hide emf
    show em proper
    with dissolve
    emelie "And, y'know, us piggies have something else that I don't think humans do!"
    "A snout? Tusks?"
    me "Oh yeah? And what's that?"
    "Emelie does a quick spin-"
    window hide
    show blackopacity
    show embutt
    with dissolve
    pause 0.5
    window show
    emelie "A tail!"
    "!!"
    "I already knew pigs have a lil curly tail."
    "What's surprising's just..."
    "...Those..."
    "Curves!"
    "I thought her dress was revealing before, but the backside is even more so!"
    emelie "So what do you think? Cute, right?"
    "Emelie bounces a little in place to make her tail wiggle, in turn making her butt bounce up and down under the form-fitting dress."
    "My eyes remain fixed to her as she jiggles."
    "Those thighs are sort of moving too..."
    emelie "Hmm?"
    me "Uhh, yeah, uhh- Wow! That's such a cute tail!"
    "My voice cracks and I swallow hard."
    "Emelie turns around again."
    hide embutt
    hide blackopacity
    with dissolve

    emelie "Now we're even! You taught me something and I taught you something! "
    "I nod, hoping she doesn’t notice the beads of sweat forming at my brow. In my head, her butt just keeps bouncing and bouncing..."
    me "F-For sure! "
    show emf bigsmile at right with dissolve:
        yalign 0.15
        zoom 1.0
    emelie "Woo! Now I don't feel as guilty for having such a silly question!"
    me "Wait... You never told me HOW you got the question about toes to begin with?"
    show em normal
    hide emf
    with dissolve
    emelie "Oh... well..."
    show em insecure
    show emblush at right:
        yalign 0.15
        zoom 1.0
    with dissolve
    emelie "Okay, don't tell anyone, but... I've been reading this book that just came out!"
    show em out
    with dissolve
    emelie "It's gotten super popular here in the kingdom! EVERYONE is reading it! "
    show em insecure
    show emeye side1 behind emblush at right:
        yalign 0.15
        zoom 1.0
    with dissolve
    emelie "Well... All the ladies are, at least. "
    me "What's it about? "
    hide emeye with dissolve
    emelie "... I guess you can have a peek at it. "
    window hide
    show bg emelieroomnobook behind em
    show em book
    hide emblush
    show emf insecure at right:
        yalign 0.15
        zoom 1.0
    show emblush at right:
        yalign 0.15
        zoom 1.0
    with dissolve
    pause 0.5
    window show
    "Emelie picks up the book from her bed and hands it to me."
    window hide
    play sound "audio/soundFX/Get.mp3"
    show blackopacity
    show ritabook
    hide emblush
    with dissolve
    pause 1.0
    window show
    emelie "So, here it is! "
    me "W-what? "
    me "\" Humane Hunk\"??"
    emelie "I... Uuuuhh..."
    "This book looks... interesting... "
    "Let's read the synopsis."
    emelie "I wouldn't be reading it if it wasn't for the fact that everyone else is!"
    me "\"In but a single winter’s night, one sweet stray pig girl goes from fighting for her life–\""
    emelie "Th-Thats about all you need to know-"
    me "\"–to fighting her most primal urges. Can she stay true to her vows, or will she succ–\""
    emelie "You can hand me the book back now-"
    me "\"–umb to the flame of desire that her tall and swarthy savior ignites within her?\""
    me "\"The award-winning Rita Blomberg returns with another installment in the shudderingly salacious \”Guilty Pleasures\” collection–\""
    "She rips the book from my hands."
    window hide
    play sound "audio/soundFX/Get.mp3"
    hide blackopacity
    hide ritabook
    show em book
    show emf insecure at right:
        yalign 0.15
        zoom 1.0
    with dissolve
    hide emblush
    pause 0.3
    window show
    emelie "Now... I know it might sound a little..."
    me "Raunchy?"

    show emblush at right:
        yalign 0.15
        zoom 1.0
    with dissolve
    emelie "EeeEeehhHHhh... "
    show emeye side2 behind emblush at right:
        yalign 0.15
        zoom 1.0
    with dissolve
    "Emelie is blushing like crazy. "
    hide emeye with dissolve
    emelie "A-A-Again, I’m only reading it ‘cause everybody else is!"
    show emf pout
    hide emblush
    with dissolve
    emelie "And this copy was sent to me straight from Rita Blomberg herself"
    show emf normal
    with dissolve
    emelie "She and I used to go to school together!"
    show emf insecure with dissolve
    emelie "We were besties, but she wanted to pursue a more creative career and went to study in a neighbouring kingdom..."
    show emf concern with dissolve
    emelie "I wish I could've gone with her! But I have my \"Royal Duties\" as a princess..."
    emelie " In a few days I've got a biig test coming up that's supposedly really important! "
    emelie "So I have to attend these boring-ass \"Princess Classes\"!"
    show emf grumpy with dissolve
    emelie "They're just the worst!"
    emelie " Did you know there are TEN different types of spoon that a \"well-mannered young lady\" is supposed to use in a single dinner?"
    show emf weirdo with dissolve
    emelie "Mom and dad don't even use all the dang cutlery themselves... They just use your basics like any other pig!"
    emelie "But apparently when you visit other royal families you have to be \"civilized\" and use the \"proper spoon\"."
    show emf grumpy with dissolve
    emelie "Ugh. "
    show emf normalblush with dissolve
    emelie "I'm super happy Rita is successful doing what she loves though! Her work really takes me to another world when I read it! "
    hide emf with dissolve
    "Her eyes start skimming the pages."
    emelie "The story is actually pretty good once you get into it..."
    emelie "The characters are compelling too..."
    emelie "And y'know..."
    play sound "audio/soundFX/PageTurn.wav"
    show em book2 with dissolve
    emelie "It gets pretty steamy here and there, if you know what I mean!"
    me "...I think I do."
    show emblush at right:
        yalign 0.15
        zoom 1.0
    with dissolve
    "She starts blushing after only a few sentences. "
    me "And you're saying toes are mentioned in the book? "
    hide emblush
    show em book
    show emf normal at right:
        yalign 0.15
        zoom 1.0
    with dissolve
    emelie "Right, haha! This part here!"
    show emf pout with dissolve
    emelie "So... They’re waiting out a snowstorm in this cave, and they’re huddled together for warmth and stuff."
    emelie "And so it reads- *ahem*"
    hide emf with dissolve
    emelie "\"With his skin against hers, sharing precious body heat between the both of them, he could feel the sensation gradually returning to his toes.\""
    show emf normal at right:
        yalign 0.15
        zoom 1.0
    with dissolve
    emelie "..."
    me "That's it? "
    show emf insecure at right:
        yalign 0.15
        zoom 1.0
    with dissolve
    emelie "Yes! And I got so confused! "
    emelie "But now I get it... He spent the whole last chapter carrying her through the snow, so..."
    show emf normal at right:
        yalign 0.15
        zoom 1.0
    with dissolve
    emelie "Poor guy’s feet must’ve been frozen solid after all that! "
    show emf laugh at right:
        yalign 0.15
        zoom 1.0
    with dissolve
    emelie "Now I can finally read on! "
    show emf smile with dissolve
    emelie "Gosh, I just hate it when there’s something I don’t understand like that, even if it’s just a tiny detail."
    emelie "It feels like I’m missing out on part of the story! "
    "Emelie puts the book back down. "
    hide emf
    show em normal
    show bg emelieroom behind em
    with dissolve
    pause 0.5
    show em out with dissolve
    emelie "Oh and speaking of frozen toes- You can put your shoes back on now if you want to!"
    show em hips with dissolve
    emelie "If they're prone to cold and all! Haha!"
    me "Right! "
    show blackopacity
    show feetbare
    show em normal
    with dissolve
    "I bend forward. Phew, that all went smoothly!"
    "Let's get these shoes back on- "
    window hide
    show blackshake at truecenter behind bg
    play sound "audio/soundFX/crack_2.wav"
    stop music fadeout 0.1
    with vpunch
    pause 0.2
    window show
    "OH NO. MY BACK-"

    window hide
    play sound "audio/soundFX/crack_3.wav"
    with vpunch
    window show
    "*CRACKCRACK*"
    hide blackopacity
    hide feetbare
    play sound "audio/soundFX/Crack_3_small.wav"
    pause 0.2
    window show
    me "Aagh! I think I just threw my back out!" with vpunch
    play music "audio/starting-out-waltz-vivace-by-kevin-macleod-from-filmmusic-io.mp3" fadein 60.0 volume 0.1
    show em panic
    show emear high
    with dissolve
    emelie "Oh no! Jeez, get over here!"
    emelie "I didn't know putting on shoes was so physically demanding for you humans! "
    emelie "I bet trying to cram all those toes in there is tricky! "
    "I waddle my way over to her."
    show em out
    show emf concern at right:
        yalign 0.15
        zoom 1.0
    with dissolve
    emelie "I know my way around a back! Me and my mom massage each other's achey backs all the time!"
    show emf insecure with dissolve
    emelie "That's the big downside of having such massive breas-"
    show emf wide at right:
        yalign 0.15
        zoom 1.0
    show emblush at right:
        yalign 0.15
        zoom 1.0
    with dissolve
    "Emelie cuts herself off mid-sentence."
    hide emeye
    show em hips
    show emf insecure
    with dissolve
    emelie "Just get those clothes off and lie face down on the bed and I'll get you sorted in no time!"

    me "W-What??"
    show emf normal with dissolve
    emelie "It’s important to COMPLETELY expose the area you’re massaging, so you can work the muscles directly. "
    me "..."
    hide emblush
    show emf insecure
    with dissolve
    emelie "It’s the least I can do after dragging you all this way!"
    "I can't expose myself in front of the princess like that! I'd get in big trouble! "
    me "I-I can't get down to my undies like tha-"
    show emf laugh with dissolve
    emelie "No undies either, silly! If they're too tight they could restrict blood flow to your lower back!"
    show emf normal with dissolve
    emelie "  I'll give you a towel, don't worry!"
    "!!"
    "I know I shouldn't... But my back feels like it's burning up more and more with every passing moment!"
    me "...O-Okay let's do this!"
    scene black with fade

    "Emelie throws me a medium-sized white towel and turns around."
    "I quickly dispose of my overalls and underwear before lying face-down on her bed, flinging the towel back over my butt. "
    window hide
    stop music fadeout 1.0
    play sound "audio/soundFX/Sit Pillow.wav"

    jump handjobmassage

    "END END"
    "END END"
    "END END"
    "END END"

    return

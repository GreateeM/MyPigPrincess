label Bath:
    window show

    "I follow Emelie down one of the hallways!"

    play music "audio/birds.wav" fadein 0.1 volume 0.2
    window hide
    scene bg BathHalls with fade

    show em oilhole at right:
        yalign 0.09 xalign 0.9

        zoom 1.0

    show emf insecure at right:
        yalign 0.09 xalign 0.9

        zoom 1.0
    if cumface == True:
        show Emoil barefacial at right:
            yalign 0.09 xalign 0.9

            zoom 1.0
    if cumface == False:
        show Emoil cum at right:
            yalign 0.09 xalign 0.9

            zoom 1.0
    with dissolve
    window show
    emelie "Here we are! It's a workday so the baths should be clear for a couple of hours!"
    emelie "I have my own personal bath up in the tower but we'd definitely get spotted running all the way there!"
    show emf surprise with dissolve
    emelie "Let's hurry on in!"
    window hide
    hide Emoil
    hide emf
    hide em
    hide emelie
    show bathcorridoropen
    play sound "audio/soundFX/OpenDoor 1.wav"
    with dissolve
    pause 0.3
    window show
    "Emelie quickly runs inside one of the rooms, leaving the door open for me."
    "I hurry on inside."
    window hide

    scene white with dissolve
    play sound "audio/soundFX/FX2/leave-water.wav"
    pause 0.2
    window show
    "Warm steam blasts my face the moment I enter!"
    me "I can't see anything!"
    emelie "Just give it a second!"
    pause 0.2
    play sound "audio/soundFX/FX2/lock-the-door-2.wav" volume 0.3
    "I hear her voice right next to me as she locks the door before taking a step back."
    window hide
    scene bg BathRoomEmpty
    play music "audio/starting-out-waltz-vivace-by-kevin-macleod-from-filmmusic-io.mp3" fadein 1.0 volume 0.3
    show BathClothes
    show emblush at right:
        yalign 0.15
        zoom 1.0
    show emn cover at right:
        yalign 0.15
        zoom 1.0
    show emf pout at right:
        yalign 0.15
        zoom 1.0


    with dissolve
    window show
    emelie"Pheeew!"
    emelie "We're safe!"
    "Wow!"
    "She's completely nude!"
    show emf insecure
    show emeye side1 at right:
        yalign 0.15
        zoom 1.0

    with dissolve
    emelie "D-Dont stare like that!"

    me "S-Sorry..."
    hide emeye side1 with dissolve
    emelie "It's okay!"
    show emn shy
    show emf pout
    with dissolve
    emelie "I did my best to rub the... fluids off with my dress!"
    emelie "Now I'm just waiting for the water to fill up so we can clean up properly!"

    show emf insecure at right:
        yalign 0.15
        zoom 1.0
    with dissolve
    #menu to compliment her?
    emelie "I'm really sorry about all that back there!"
    #Don't worry about it!"
    #Only apologize for what happened after the door smashed open!"
    show emf normalblush at right:
        yalign 0.15
        zoom 1.0
    with dissolve
    emelie "Rolf can go a bit crazy sometimes... Especially when my dad's out of town!"
    me "How so?"
    show emf surprise
    show emear high at right:
        yalign 0.15
        zoom 1.0
    with dissolve
    emelie"Believe it or not but Rolf is the king's most trusted right-hand man!"
    emelie"They go way back, and Rolf doesn't respect anyone else to the level he does my dad!"
    me "Huh..."
    window hide
    menu:
        with dissolve


        "He seems sort of aggressive and unhinged.":
            window show
            me "He seems sort of aggressive and unhinged."
            hide emear
            show emn proper
            show emf insecure
            with dissolve
            emelie "Yeeaaah..."

        "He's an absolute dick.":
            window show
            me "He's an absolute dick."
            hide emear
            show emf weirdo
            with dissolve
            emelie "..."
            show emn cover
            show emf grumpy
            with dissolve
            emelie "He gave you a tough time back there but Rolf is a war hero!"
            emelie "If it wasnt for soldiers like him this city might not be standing today! He deserves some respect!"
            emelie "And he was just looking after me."
            me "That's true..."
            show emn proper
            show emf gross
            with dissolve
            emelie "But he does get a bit overprotective that's for sure..."
            me "It really seemed like he had it in for me from the very beginning!"
            me "Even when I was disguised as a guard."
            show emf laugh
            show emear high at right:
                yalign 0.15
                zoom 1.0
            with dissolve
            emelie "Haha maybe you're lucky he's drinking on the job or I don't imagine the disguise would've worked!"


    show emf normal
    hide emear
    with dissolve
    emelie" When my dad's here he keeps Rolf busy with all sorts of different tasks and stuff!"
    show emf pout with dissolve
    emelie "And in the downtime they bicker!"
    emelie"Maybe he just gets a bit restless when left with nothing to do."
    show emf smile with dissolve

    emelie"But my parents should come back from their trip in a few days! "
    emelie "I'm sure that'll reel Rolf back a bit."
    me "I would hope so!"
    show emn shy
    show emf normal
    with dissolve
    emelie "They're currently attending a royal marriage in another kingdom!"
    emelie"It's considered good manners if the king and queen bring gifts and join in to spectate!"
    show emf surprise
    show emear high at right:
        yalign 0.15
        zoom 1.0
    with dissolve
    emelie "I could join too if I really wanted to... "
    show emf gross

    with dissolve
    emelie "But it's often really awkward!"
    hide emear
    with dissolve
    emelie "A lot of bachelor princes attend from other kingdoms... And their parents always try matching 'em with me!"
    me "That does sound awkward."
    show emn proper
    show emf insecure
    with dissolve
    emelie "Yeah but I guess I get it..."
    emelie "Marriage would join our families together and they'd have access to our great army and farmlands."
    show emf concern with dissolve
    emelie "But most princes aren't interested in marrying a pig..."
    show emf sad with dissolve
    emelie "They apparently find the idea sort of unflattering."
    emelie "..."
    show emf wide with dissolve
    emelie "But a few years back a Skunk prince got very pushy!"
    emelie "I think they have a similar unflattering reputation..."
    #Smell question
    window hide
    menu:
        with dissolve
        "How did he smell?":
            window show
            me "How did he smell?"
            show emf weirdo2 with dissolve
            emelie "Hey, that's not cool! Those are the kinda negative assumptions I'm sure they make about us piggies!"
            show emf gross with dissolve
            emelie "How we smell weird and bathe in mud and stuff!"
            emelie "..."
            show emf wide
            show emeye side2 at right:
                yalign 0.15
                zoom 1.0
            with dissolve
            emelie "I did give him a lil' whiff though when he wasnt looking..."
            me "Aaand?"
            hide emeye
            show emf laugh
            show emear high at right:
                yalign 0.15
                zoom 1.0
            with dissolve
            emelie "Haha he smelled just fine!"
            emelie "Unlike us right now! "
            window hide
            pause 0.3




            show bg BathRoom with dissolve
            play sound "audio/soundFX/FX2/leave-water.wav" volume 0.5
            pause 0.6
            show emn proper at right:
                yalign 0.15
                zoom 1.0
            show emf bigsmile at right:
                yalign 0.15
                zoom 1.0
            with dissolve
            pause 0.3
            window show

            emelie "Oh nice, the water's finished!"
        "I don't find pigs unflattering at all!":
            window show
            me "I don't find pigs unflattering at all!"
            show emf normalblush
            show emear high at right:
                yalign 0.15
                zoom 1.0
            with dissolve
            emelie "Really? Haha, that's nice to hear!!"
            hide emear
            show emf insecure
            with dissolve
            emelie "A lot of outsiders think we bathe in mud and sniff dirt after truffles all day."
            show emf normal
            emelie "But truffle hunting is a very specialized, well-respected skill you see!"
            emelie "Very few piggies are born with the right nose for it!"
            show emf laugh with dissolve
            emelie "And we only do mud baths like... three times a year TOPS!"
            window hide
            scene white with dissolve

            play sound "audio/soundFX/FX2/leave-water.wav" volume 0.5
            pause 0.6

            scene bg BathRoom
            show BathClothes
            show emn cover at right:
                yalign 0.15
                zoom 1.0
            show emf bigsmile at right:
                yalign 0.15
                zoom 1.0
            with dissolve
            pause 0.3
            window show
            emelie "Speaking of which, the bath is finally ready!"






    window hide
    hide emn
    hide emf
    hide emear
    hide emblush
    with dissolve
label bathgallery:
    if playnormal == False:
        show bg BathRoom
        show BathClothes
        show emn cover at right:
            yalign 0.15
            zoom 1.0
        show emf bigsmile at right:
            yalign 0.15
            zoom 1.0
        with fade

        play music "audio/starting-out-waltz-vivace-by-kevin-macleod-from-filmmusic-io.mp3" fadein 2.0 volume 0.2
        window show
        emelie "The bath is finally ready!"
        window hide
        pause 0.2
        hide emn
        hide emear
        hide emblush
        hide emf
        with dissolve


    play sound "audio/soundFX/FX2/water-swimming-4.mp3" volume 0.5
    show BathEmelie
    with dissolve

label bathtopic2:


    pause 0.5
    window show
    "Emelie does a careful little hop into the water."
    emelie "You just gonna watch?"
    "She gives me a shy smile."
    "I swallow hard and undress before jumping in myself."
    stop music fadeout 3.0
    window hide
    play sound "audio/soundFX/FX2/water-slosh-spashing-3.wav" volume 0.5
    scene black with dissolve
    pause 0.2
    window show

    "The water is nice and warm against my legs and I swiftly sit down on the fairly shallow bath floor."

    window hide


    scene Embath Frontbase
    show embathhands
    with dissolve
    pause 0.2
    window show
    play music "audio/Farm+-+320bit.mp3" fadein 0.2 volume 0.4 if_changed
    me "This feels really nice!"
    me "I don't know if I've ever taken a bath this warm before."
    show emb embathsmiles with dissolve
    emelie "I love warm baths! Even on the warmest day of the year the ocean just doesn't get close."
    me "So far I think I agree!"
    me "But the ocean definitely beats scooping up snow to melt over a fire like we do in winter back at the farm."
    hide emb with dissolve
    emelie "That really does sound like a lot of work!"
    show emb embathoo with dissolve
    emelie "Wait..."
    emelie "Speaking of work..."
    show emb embathsmiles with dissolve
    emelie"You're like... my personal assistant now!"
    "I give her a questioning look."
    emelie "Or that's what I told Rolf back when he asked why you were in my room!"
    me "Oh right!"
    show emb embathsurprise with dissolve
    emelie "I was freaking out and had to come up with a reason why I'd be changing clothes with you in the room!"
    show emb embathsado with dissolve
    emelie "I hope you didn't take offense..."
    me "Don't worry, it ended up clearing me in the end!"
    me "And I don't think telling him the truth wouldnt have served me well..."
    show emb embathlaugh with dissolve
    emelie "Haha, that's probably true!"
    hide emb with dissolve
    emelie "..."
    emelie"Well... Do you want the job?"
    me "What?"
    show emb embathsad with dissolve
    emelie "I mean... You could go back to your farm right away now if you want to but... "
    emelie "I'd kinda like to hang out some more!"
    "She's asking me to be her personal assistant?!"
    window hide
    menu:
        with dissolve
        "I definitely want the job!":
            window show
            me "I definitely want the job!"


        "Are you going to send Rolf after me if I decline?":
            window show
            me "Are you going to send Rolf after me if I decline? "
            show emb embathsmiles with dissolve
            emelie "Haha, maybe!"
            "I jokingly give her a scared look."
            me "Okay if that's the case I'll have to accept your offer!"

    #emelie happy in bath
    play sound "audio/soundFX/FX2/water-slosh-spashing-3.wav" volume 0.5
    hide embathhands
    show emb embathlaugh
    with dissolve
    emelie"Woo!"
    emelie "Mom will be really happy too!"
    show emb embathsmiles with dissolve
    emelie "She's been pushing me to get an assistant for a long time."
    emelie "We'll just have to think of a way to tell her how it came to be!"
    show emb embathsmilebite with dissolve
    emelie "While leaving out some of the details of course... hihi!"
    me "That's probably for the best!"
    hide emb with dissolve
    emelie "Speaking of assistance..."
    show emb embathsad with dissolve
    emelie "I'm feeling super stiff!"
    show emb embathsado with dissolve
    emelie "My shoulders got really worn out from carrying my heavy breasts back when we... Y'know!"
    show emb embathlaugh
    show embathhands
    with dissolve
    emelie "And cramping up in that dark wardrobe just made things worse! Haha."
    me "It's only fair I give you a massage after the one you gave me earlier!"
    me "Just tell me where to focus my attention and I'll do my best!"
    show emb embathsmilebite with dissolve
    emelie "That sounds good!"
label BathSmex:
    window hide
    play sound "audio/soundFX/FX2/water-swimming-4.mp3" volume 0.4
    scene Embath Backbase with dissolve
    pause 0.3
    window show
    emelie "You can start with my shoulders!"
    "I put my hands on her shoulders and start pressing down."
    show EmbathHands back1 with dissolve
    emelie "that feels nice..."
    me "I can't say I've given many massages before."
    me "Let me know if you want something specific!"
    "I squeeze and rub her shoulders for a few moments."
    emelie "I think my shoulders are good now!"
    emelie  "Y'know washing your own back can be sort of tricky!"
    emelie"  Hard to reach the middle sometimes when you don't have any help..."
    me "I'm on it!"
    "I move my hands down a bit."
    show EmbathHands back2 with dissolve
    emelie "Ahh, that's good! Being thorough when washing your skin is very important."
    emelie "But scrubbing your entire back's a bit of a chore!"
    emelie "Are you thorough when you bathe?"
    window hide
    menu:
        with dissolve
        "Not very... {space=9}But I make sure to give my pits and privates extra attention!":
            window show
            me "Not very... But I make sure to give my pits and privates extra attention!"
            emelie "Haha, I appreciate your honesty!"
            emelie "I bathe really often just because it feels good!"
            emelie "But sometimes I get a little lazy with the vigorous scrubbing..."

        "I'm very thorough!{space=9} I make sure to scrub clean all over!":
            window show
            me "I'm very thorough! I make sure to scrub clean all over!"

            emelie "Haha, really? You were a little dirty earlier..."
            me "I'm a farmer! I literally work in the dirt!"
            emelie "Haha right, that'd explain it!"
            emelie "If I were a human I'd probably be way too lazy to clean in between all those little \" toes \" ! "
            me "You get used to it."
    "After washing her back I rub my thumbs into the muscles around her shoulder blades."
    "It's something she did back when giving me a massage!"
    emelie "Ahh, that feels good!"

    emelie "This is a lot nicer than going at it alone!"
    emelie"..."
    emelie "Maybe you can rub me down a little lower too?"
    "Emelie stands to stand up in the bath!"

    window hide
    hide EmbathHands with dissolve
    pause 0.3
    play sound "audio/soundFX/FX2/splash.wav" volume 0.4

    show Embath Buttbase with dissolve
    pause 0.3
    window show

    "W-Wow!"
    "Her big butt is on full display!"
    "I remember back when she showed me her tail and I saw those curves under her dress..."
    "But now It's all out in the open for me to see!"
    emelie "I-is there a problem?"
    me "O-oh not at all!"
    "I move my hands to the sides of her butt."
    show EmbathHands butt1 with dissolve
    "Her voluptuous and soapy cheeks squish together as I give it a gentle press."

    "Those water droplets trailing down her skin make me lose track of time. "

    emelie "Mmmmhh~"
    emelie "A little closer to the center under the cheeks would be nice too!"
    "!!"

    show EmbathHands butt2 with dissolve
    "I lift her meaty butt and make some side-to-side motions around the area where her buttcheeks tuck in."
    emelie "Ahh, that's so good!"
    "She presses her butt back against my hands slightly."
    "I'm not sure if she's doing it consciously or not."
    stop music fadeout 2.5
    emelie "Y'know what..."
    hide EmbathHands with dissolve
    "She walks forward a bit toward the edge of the bath"
    window hide




    play sound "audio/soundFX/FX2/water-slosh-spashing-3.wav" volume 0.4
    play music "audio/Heartbeat+-+320bit.mp3" fadein 8.0 volume 0.3
    scene EmLean1 with fade
    pause 0.6
    window show

    "!!!"
    emelie" I figure this might give you better access..."
    show EmLean2 with dissolve
    emelie "For scrubbing and massaging of course!"
    emelie "This is strictly so you can... help me wash easier!"
    emelie "As an assistant!"
    emelie"..."
    me "O-of course! Leave it to me!"
    me "I take a few steps closer "
    window hide

    play sound "audio/soundFX/FX2/water-swimming-4.mp3" volume 0.3
    scene CloseAss1 with fade
    pause 0.7
    window show

    "With this view my dick's starting to throb like crazy!."
    "But I gotta keep things... professional..."
    emelie "You can... see a bit more now than when I was standing, right?"
    emelie "Should make it easier for you to help me with all those... hard to reach spots!"

    scene CloseAss2 with dissolve
    "I move my hands to the same region they were at when she was standing."
    emelie "Ah~"
    emelie "If you can't get a proper view or reach everything... don't be afraid to spread my cheeks a little!"
    window hide

    scene CloseAss3 with dissolve
    pause 0.7
    window show
    "I immediately take her up on the offer and spread her cheeks!"
    emelie "Oink!"
    emelie "I mean...!"
    emelie "G-good! Now you can really help!"
    "I'm pretty sure this isn't all just about helping her with difficult to reach spots anymore..."
    emelie "And maybe... massage a bit too!"
    "Yep. She definitely wants more!"

    scene CloseAss4 with dissolve
    me "Okay just tell me if it's too much!"
    "So... what do I do?"
    $ buttprod = False
    window hide
label fingerin:

    menu:
        with dissolve
        "Prod her butthole.":
            $ buttprod = True
            window show
            me"I think this place could use some attention."

            show CloseAss ButtFinger1 with dissolve
            "I hold my finger over her asshole before slowly bending it forward."
            show CloseAss ButtFinger2 with dissolve
            emelie "A-ahh..."
            "I slowly nudge the upper digit inside with some resistance"
            emelie "Ow!"
            "Her ass tenses up and I pull my finger back out."
            show CloseAss ButtFinger1 with dissolve
            me "Sorry!"

            "It won't go in any further without anything to help my finger glide!"
            emelie "Maybe that'd work if we still had some of that oil..."

            hide CloseAss with dissolve
            me "Don't fret, princess! There are other places to massage!"
            show CloseAss PussyFinger0 with dissolve
            "I slowly spread her wet labia."
            "This place looks quite slippery by comparison!"
            jump fingerpuss



        "Prod her pussy.":
            show CloseAss PussyFinger0 with dissolve
            window show
            "I slowly spread her wet labia."
            me"Maybe I should focus some attention here."
            jump fingerpuss

label fingerpuss:


    emelie "M-Mmhh that sounds good!"
    show CloseAss PussyFinger1 with dissolve
    "I slowly push my fingers forward against her slippery folds."
    show CloseAss PussyFinger2 with dissolve
    emelie "Ahh! "
    "They slide inside with ease!"
    show CloseAss PussyFinger3 with dissolve

    "Before I realize it my fingers are entirely enveloped by her."
    "Her warm pussy gives my fingers a little squeeze as she lets out a soft moan."
    emelie "A-Ahh keep going!"
    me "Of course, princess."
    show CloseAss PussyFinger2 with dissolve

    "Her hole is making a wet, slippery mess of my fingers."

    show CloseAss PussyFinger3 with dissolve
    "She eagerly invites my fingers once again, breathing happily as I slide in and out for a few more moments"
    show CloseAss PussyFinger2 with dissolve
    pause 0.2
    show CloseAss PussyFinger3 with dissolve
    pause 0.2
    show CloseAss PussyFinger2 with dissolve
    pause 0.2
    show CloseAss PussyFinger1 with dissolve

    "The moment I pull my fingers all the way out she rocks her hips back towards me."
    emelie "Mhhh, don't stop!"
    show CloseAss PussyFinger4 with dissolve
    "I spread her pussy again"
    emelie "Or do you want to try something else?"
    if buttprod == True:
        emelie "Your fingers must be pretty slick by now~"
    "The natural lubricant covering my fingers catches the light."
    "!"
    if buttprod == True:
        "I can probably give her butthole another try now!"
    else:
        "With fingers this slippery I might be able to massage her other hole!"
        "Or maybe I can introduce another finger to what I've been doing to increase the intensity!"
    window hide
    menu:
        with dissolve
        "Play with her ass.":
            window show
            if buttprod == True:
                "Let's see if it works better this time."


            "I'll start small."
            show CloseAss WetButtFinger1 with dissolve
            "I press my slippery finger against her butthole."
            if buttprod == True:
                emelie "Trying that again?..."
            emelie "Mhhh?"
            if buttprod == True:
                me "Is this okay? My fingers are pretty slippery now."
            else:
                me "Is this okay?"
            emelie "I don't think you're supposed to play with that spot!"
            emelie "But I suppose an assistant isn't supposed to be playing with his princess' other parts either~"
            "She giggles"
            emelie "You do have a way with your hands that's for sure!"
            emelie "And I like trying new things..."
            emelie "Especially if you're curious!"
            emelie "Maybe it'll feel really good there too..."
            emelie"..."
            emelie "Let's give it a try~"
            me "I'll go slow and we'll see if you like it!"
            "Emelie gives me a little nod and raises her butt a little."
            "I slowly bend my pointer finger forward against her ass."

            show CloseAss WetButtFinger2 with dissolve
            "It slips inside without much resistance"
            emelie "Ahha, that kinda tickles a little!"
            me "Is that a good thing?"
            emelie "Hmm not sure yet... maybe try a bit more!"
            show CloseAss WetButtFinger1 with dissolve
            "I retract my finger."
            "It went in really easy with her juices lubricating it!"
            "I still have a fair amount on my index finger too..."
            "I should make use of it before it trickles down into the water!"


            show CloseAss ButtFingerDouble1 with dissolve
            "I raise my other slick finger to her ass too."

            "I slowly press both fingers against her."
            emelie "A-Ahhh!"
            "She lets out an eager moan "
            "Her body and asshole tense up a bit."
            me "Remember to breathe slowly and relaaax."
            "I speak in a soft tone, remembering what she told me to do back when she gave me that back massage!"
            emelie "Mmhhhm."
            show CloseAss ButtFingerDouble2 with dissolve
            "My fingers slowly slip inside as her hole relaxes for a moment"
            emelie "Ahhn! "
            emelie "That... feels strange!"
            me "Want me to stop?"
            emelie "No! Please don't..."
            emelie "It's a good kinda strange!"
            "Emelie's hole tenses up and relaxes again, giving my fingers a little squeeze."
            "I can't believe I'm playing with the princess' ass like this!"

            show CloseAss ButtFingerDouble1 with dissolve
            "I pull out and circle the outside of her anus before pushing in again."
            show CloseAss ButtFingerDouble2 with dissolve
            emelie "Mmmhhh~"
            emelie "That doesn't just feel like a tickle anymore..."
            emelie "It's getting better every second!"
            show CloseAss ButtFingerDouble1 with dissolve
            show CloseAss ButtFingerDouble2 with dissolve
            "My fingers slide in and out for a bit longer."
            emelie "Aaahhh"
            "She takes a deep breath and her body relaxes completely."


            show CloseAss ButtFingerDouble3 with dissolve
            "My fingers suddenly slip all the way inside!"
            emelie "Hnn!"
            "She lets out a quivering moan."
            show blackopacity
            show EmBathMoanCloseup with dissolve
            emelie "I.. never thought this could feel so good!"
            emelie "And the idea sounded so naughty!"


            window hide
            menu:
                with dissolve
                "Being naughty is fun!{space=9} As your assistant, I'll gladly help you enjoy this hole more and more.":
                    window show
                    "Being naughty is fun! As your assistant, I'll gladly help you enjoy this hole more and more."

                    emelie "A-are you saying you want to... train my ass?"
                    $ trainass = True
                    me "If you'd be interested I'd love to."
                    emelie "That sounds -ahh!- nice~"
                    hide blackopacity
                    hide EmBathMoanCloseup with dissolve

                    "She continues moaning with deep breaths, her ass gently squeezing my fingers as they slide in and out with ease."
                    emelie "I definitely want to do this more often!"

                "I'm glad you enjoy being naughty!":
                    window show
                    me "I'm glad you enjoy being naughty!"
                    emelie "Y-Yes!"
                    hide blackopacity
                    hide EmBathMoanCloseup with dissolve
                    "She continues moaning with deep breaths, her ass gently squeezing my fingers as they slide in and out with ease."
                    emelie "I definitely want to try new things and do this more often!"

            show CloseAss ButtFingerDouble2 with dissolve
            show CloseAss ButtFingerDouble1 with dissolve
            "I pull out and spread her asscheeks again!"
            hide CloseAss with dissolve
            show CloseAss3
            show CloseAss used1
            with dissolve
            pause 0.3
            show CloseAss used2 with dissolve
            pause 0.3
            show CloseAss used1 with dissolve
            pause 0.3
            show CloseAss used2 with dissolve
            "Her played with asshole quivers a bit."
            "My boner is absolutely raging looking at Emelie's glistening parts. "
            $ buttprod = True
            $ buttprodsuccess = True




        "Not as interested in her ass,{space=3} keep fingering pussy!":
            window show
            "She really seems to be enjoying my fingers down here!"
            "They're slipping in and out with such ease now..."
            "She's gotten really wet."
            "Maybe she'll enjoy a bit more..."
            show CloseAss PussyFingers1 with dissolve
            "I put another finger up against her dripping pussy."
            show CloseAss PussyFingers2 with dissolve
            "My three fingers start to slide in with a little squeeze from Emelie's inner walls."
            emelie "Ahh yes... that feels amazing!"
            show CloseAss PussyFingers3 with dissolve
            "As my fingers reach their end she grinds her butt against my knuckles."
            "I take the hint and slowly move the tips of my fingers in gentle circular motions inside."
            show blackopacity
            show EmBathMoanCloseup
            with dissolve
            emelie "Ahhh, yes! That's the spot!"
            emelie "I've never had someone else give me this type of massage before!"
            me "Never?"
            emelie "Well, I've done it on myself a few times..."
            emelie "But that's different!"
            emelie"And my fingers are... -ah!-... much smaller!"
            "Emelie's legs start shaking a little, her pussy starting to squeeze me tighter"

            hide blackopacity
            hide EmBathMoanCloseup with dissolve

            pause 0.3
            show CloseAss PussyFingers2 with dissolve
            pause 0.3
            show CloseAss PussyFingers3 with dissolve

            "I slide in and out and continue using my fingers in the way she responds the most to."

            emelie "N-nyaah!... "
            emelie "T-that's enough for n-now!"
            me "Yesyes, okay!"
            show CloseAss PussyFingers2 with dissolve
            pause 0.2
            show CloseAss PussyFingers1 with dissolve
            pause 0.2
            hide CloseAss
            show CloseAss3
            show CloseAssWetPuss
            with dissolve
            "I pull my fingers back out and see her hole tightening and opening slightly."
            emelie "M--MmhhhhHh! I almost lost my composure right then!...."
            "She might've just barely held back a full orgasm!"
            "Maybe she doesn't feel comfortable enough to fully give in to her pleasure yet."
            $ almostorgasm = True
            me "S-sorry!"
            emelie "I don't mean that in a bad way!"
            emelie "Y'know you're REALLY good with your fingers..."
            "My boner is absolutely raging looking at Emelie's glistening pussy!"
            $ buttprodsuccess = False


    "I find myself panting like a madman. "

    emelie "Everything okay with you back there?"
    me "Oh- Yes- Absolutely!"
    "I groan out, the tip of my cock nudging against her thigh"
    emelie "O-Oh!"
    emelie "We've been focusing on just me for quite some time, huh..."
    emelie "But if your... penis is all tense again..."
    emelie "Maybe you can use my buttcheeks the way you used my breasts before?"
    emelie "If you want some relief and you enjoy looking at my butt that is!"
    "She's inviting me to rub my dick against her ass!"
    "I've been imagining how my cock would feel inside her all this time..."
    "And while she doesn't seem ready to go all the way yet, I'm dying to slide my cock against any part of her perfectly pink skin!"
    window hide
    play sound "audio/soundFX/FX2/splash.wav" volume 0.4
    scene HotDog1 with fade
    pause 0.4
    window show
    "I stand up close to her and look down at those lovely cheeks."
    "Seems her butt looks great from all angles!"
    scene HotDog2 with dissolve
    "My cock slaps down on her butt."
    scene HotDog3  with dissolve

    if buttprod == True:
        "The bottom of my shaft nudges against her slippery asshole as I slide my cock up her buttcrack"
    else:
        "The sensation of sliding it forward against her wet skin is divine. "
    window hide
    show EmHotdogBase
    show EmHotdogCumface
    with fade
    pause 0.3
    window show
    emelie "T-That's it!"
    emelie"Now squeeze my cheeks together!"
    me "Okay!"
    window hide

    scene HotDog3  with fade

    pause 0.3

    scene HotDog4a with dissolve
    window show
    "I squish her shapely cheeks together and they grab my shaft nicely!"


    scene HotDog4b with dissolve
    "I pull back a bit, her wet skin and soft cheeks feeling so nice against me."
    scene HotDog4a with dissolve
    "I push forward again and feel a bead of precum trickle out from my tip, helping to lube my cock up for easier motion!"
    scene HotDog4c with dissolve
    "With that, I thrust all the way forward until my balls slap against her wet pussy!"
    emelie "Ahh!"

    window hide
    show EmHotdogLookBack with fade
    pause 0.2
    window show
    emelie "You're really going at it!"
    me "It feels amazing!"
    emelie "Mmhh for me too!"


    window hide
    scene HotDog4a with fade
    pause 0.3
    scene HotDog4b with dissolve

    scene HotDog4a with dissolve

    pause 0.3


    scene HotDog4c with dissolve
    window show
    "I continue thrusting and panting, seeing that ass jiggle with each movement."
    "A moan escapes her lips each time my balls collide against her!"
    window hide

    scene HotDog4a with dissolve
    pause 0.2

    scene HotDog4b with dissolve
    pause 0.2
    scene HotDog4a with dissolve
    pause 0.2
    scene HotDog4c with dissolve
    window show

    me "Ahh!"
    window hide
    show EmHotdogLookBack with fade
    pause 0.3
    window show
    emelie "Yes! Keep going! give it to me!"
    emelie "Mhaah!"
    emelie "I love when those heavy balls slap against me!"
    "She really loves the feeling of my hard thrusts against her ass... "
    "Maybe she'd like something else too..."
    show blackshake at truecenter behind EmHotdogLookBack
    window hide

    menu:
        with dissolve
        "Spank her ass!":
            $ SpankAss = True
            show blackopacity

            show EmCloseSpank
            with dissolve
            play sound "audio/soundFX/FX2/spank.wav" volume 0.6
            with hpunch
            window show
            "*Smack!*"
            show EmHotdogSpankHand behind blackopacity

            "I give one of her fat cheeks a hard slap, watching it jiggle as water droplets spatter off the surface."
            window hide
            hide blackopacity
            hide EmCloseSpank
            with dissolve
            show EmHotdogCumface with dissolve
            window show
            emelie "Ahh, yes!"
            window hide
            menu:
                with dissolve
                "You're such a naughty piggy!":
                    window show
                    me "You're such a naughty piggy!"
                    window hide
                    show blackopacity

                    show EmCloseSpank
                    show EmHotdogSpankHand2 behind blackopacity
                    with dissolve
                    play sound "audio/soundFX/FX2/spank2.wav" volume 0.6
                    with hpunch
                    window show
                    "*Smack!*"
                    "Another heavy slap hits the same spot, making Emelie moan even louder."

                    emelie "Ahhn! Yes, I am!"
                    window hide

                    hide blackopacity
                    hide EmCloseSpank
                    with dissolve


                    show EmHotdogSpank2
                    show EmHotdogSkinBack
                    with dissolve
                    window show

                    "She's really into it!"
                    window hide
                    scene HotDog5 with fade
                    window show

                    "Her pink ass is looking even rosier after the spanking."
                    me "You've got a great ass, piggy!"
                    emelie "Mmhh and you've got a great cock!"

                "You've been a naughty princess!":
                    me "You've been a naughty princess!"
                    window hide
                    show blackopacity

                    show EmCloseSpank
                    show EmHotdogSpankHand2 behind blackopacity
                    with dissolve
                    play sound "audio/soundFX/FX2/spank2.wav" volume 0.6
                    with hpunch
                    window show
                    "*Smack!*"
                    "Another heavy slap hits the same spot, making Emelie moan even louder."
                    show EmHotdogSpankHand2 behind blackopacity
                    emelie "Ahhn, yes! I've been a naughty little princess!"
                    window hide

                    hide blackopacity
                    hide EmCloseSpank
                    with dissolve

                    show EmHotdogSpank2
                    show EmHotdogSkinBack
                    with dissolve
                    window show

                    "She's really into it!"
                    window hide
                    scene HotDog5 with fade
                    window show
                    "Her pink ass is looking even rosier after the spanking."
                    me "You've got a great ass, princess!"
                    emelie "Mmhh and you've got a great cock!"
            "She hadn't used that word until now!"
            "Hearing the princess respond that way to me calling her naughty and spanking her ass almost sends me over the edge immediately!"
            window hide
            scene EmHotdogSpank2
            show EmHotdogSkinBack
            with fade
            pause 0.3
            window show

            me "Ahhh!"
            "I clench all the muscles in my crotch up!"
            scene EmHotdogLookBack
            show EmHotdogSpankHand2
            show EmHotdogCumface
            with dissolve
            me "I'm getting close!"



        "Don't spank.":
            window show
            $ SpankAss = False
            "On second thought I'm not really into that."
            "I can't help but admire her jiggling cheeks."

            me "Your ass is so perfectly soft, princess!"
            show EmHotdogCumface with dissolve
            emelie "Mmhh and you've got a nice and hard... thing!"
            emelie "..."
            me "You don't have to call it a \"thing\", y'know!"
            emelie "I'm just used to mom scolding me for saying bad words!"
            emelie "W-what would you want me to call it?"

            window hide
            menu:
                with dissolve
                "\"Cock\",\"Dick\" or \"Penis\" all work!":

                    window show
                    me "\"Cock\",\"Dick\" or \"Penis\" all work!"
                    emelie "Mhh, okay!"
                    emelie "..."
                    emelie "You've got a nice and hard cock!"

                "You know what it's called, right?":
                    window show
                    me "You know what it's called, right?"
                    emelie "Of course I do!"
                    emelie"..."
                    emelie "You've got a nice and hard cock!"
            show EmHotdogCumfaceoo with dissolve
            emelie "I love the feeling of that slippery thick shaft sliding up and down my cheeks!"
            "!!"
            "Hearing the princess use such naughty words all of a sudden almost sends me over the edge immediately!"
            me "Ahh! I'm getting close!"


    emelie "Y-yes!"

    show EmHotdogLookBack
    hide EmHotdogCumfaceoo
    hide EmHotdogCumface

    if SpankAss== True:
        show EmHotdogSpankHand2

    with dissolve
    emelie "I want to feel it all over me!"
    "Hearing her desire to feel my cum cover her is enough to send me beyond the point of no return!"
    "My cock throbs hard and my balls clench!"
    window hide

    show white with dissolve



    scene EmHotdogCum
    if SpankAss== True:
        show EmHotdogSpankHand2
    with dissolve
    pause 0.5
    window show
    me "Ahhhhhhn!"
    emelie "Mmhhnn!"
    window hide
    show white with dissolve
    pause 0.2
    scene EmHotdogCum2

    if SpankAss== True:
        show EmHotdogSpankHand2

    with dissolve
    pause 0.3
    window show

    "My thick cum lands on her back as my orgasm comes to an end."
    if SpankAss== True:
        "I take a couple of steps back and observe as my load slowly drips down over her extra rosy cheeks."
    else:
        "I take a couple of steps back and observe as my load slowly drips down over her cheeks."
    window hide

    scene EmLean Cum3

    if SpankAss== True:
        show EmLeanSpankdAss

    with fade
    pause 0.3
    window show

    emelie "W-wow you really got me good this time!"
    me "Phew, I definitely did!"
    emelie "It feels so warm over my entire back..."
    if perfscore == True:
        me "That's one of the benefits of having the worlds best assistant!~ "
        emelie "Haha, don't get too full of yourself just because you got that perfect score!"
    emelie "Good thing we're in a bath or this would be one heck of a mess to take care of!"
    emelie "Let's clean up before Rolf has the chance to barge in again!"
    stop music fadeout 2.0

    scene black with dissolve
    "We laugh and take a few moments to clean up."
    $ unlock("S2")
    $ renpy.end_replay()
    play sound "audio/soundFX/FX2/splash.wav" volume 0.4
    #END OF CHAPTER 2
label afterch2:


    scene bg BathRoom
    show BathClothes
    show emn normal at right:
        yalign 0.15
        zoom 1.0
    with dissolve
    play music "audio/starting-out-waltz-vivace-by-kevin-macleod-from-filmmusic-io.mp3" fadein 1.0 volume 0.3
    emelie "Finally all clean! "
    show emf normalblush at right:
        yalign 0.15
        zoom 1.0
    with dissolve
    emelie "And my body really feels nice and relaxed after all that!"
    me "Same here!"
    me "Really hit the spot after that stressful interrogation..."
    show emn hips
    show emf laugh
    with dissolve
    emelie "Haha, I bet!"
    show emn out
    show emf concern
    with dissolve
    emelie "Crap now I realized I totally forgot to bring a clean set of clothes in here."
    emelie "Guess I'll sneak back to my room in a towel and look for something to wear-"

    window hide
    stop music fadeout 0.3
    pause 0.2

    play sound "audio/soundFX/FX2/church-bell-fischerhude-short.wav"

    with vpunch
    show emn panic
    show emf panic
    show emear high at right:
        yalign 0.15
        zoom 1.0
    with dissolve

    pause 0.5
    window show

    emelie "Oh crap!"
    emelie "It's 12'o clock!"
    show emf panic2 with dissolve
    emelie "I'm late for my princess classes!!"
    emelie "I've gotta run and find something QUICK!"
    "She looks mortified at the prospect of being late."
    me "Okay, I hope you find something to wear!"
    show emn out
    show emf wide
    with dissolve
    play music "audio/birds.wav" fadein 0.1 volume 0.2
    emelie "Yesyes!"

    show emn normal
    show emf insecure
    with dissolve
    emelie "Just wait here for a little while and I'll catch up with you later!"
    window hide


    hide emn
    hide emf
    hide emear
    with easeoutright
    hide BathClothes with dissolve
    window show
    "She grabs her clothes and rushes out!"
    "..."
    "Hmm... being late for class can't be that bad, can it?"
    "I wonder what she wants me to wait for?"
    "Speaking of which..."
    "Guess I'll do my best to clean my own rags up before I get dressed."

    play sound "audio/soundFX/run2.wav"
    play music "audio/adventures-in-adventureland-by-kevin-macleod-from-filmmusic-io.mp3" fadein 0.1 volume 0.3
    show billy holdclothes at left:
        yalign 0.4 xalign -0.08
    with easeinleft


    billy "Hey hey, partne-"
    show bill embarassface at left:
        yalign 0.4 xalign -0.08
    show billybigblush at left:
        yalign 0.4 xalign -0.08
    with dissolve
    billy "!!!"
    window hide
    menu:
        with dissolve
        "Cover junk.":
            window show
            "I quickly cover my exposed peen!"
            me "Billy!"
            me "You look healthy again!"
            show bill baseface with dissolve
            billy "Yes yes! "
        "Stand proud and exposed!":
            window show
            "I fight the instinct to cover myself up, this is a bath after all!"
            show bill wtfface with dissolve
            billy "I should've knocked, shouldn't I?"
            me "It's okay, Billy."
            me "I'm just glad to see you looking healthy again!"
            show bill baseface with dissolve
            billy "Daw, you're too sweet, [Protagonist]! "
    hide billybigblush with dissolve
    billy "This armor keeps me safe and sound! "
    billy "My helmet took the brunt of the damage and the smith fixed it right up!"

    me "That's great to hear!"
    show bill surpriseface with dissolve
    billy "Me and Rolf just got back to replace the door and found Emelie panicking on the way to her classes! "
    billy "She was in a hurry but took me aside and said you were here and to keep you company for the day!"
    "Phew, she must've found something to wear really quickly right before they arrived! "
    show bill laughface with dissolve
    billy "I also brought these for ya!"

    window hide
    show blackopacity
    show billy base at left:
        yalign 0.4 xalign -0.08
    show NewClothes
    play sound "audio/soundFX/Get.mp3"
    with dissolve
    window show
    billy "Hope I got the right sizes!"

    me "New clothes? For me?!"

    window hide
    play sound "audio/soundFX/Sit Pillow.wav"
    hide blackopacity
    hide NewClothes
    with dissolve
    window show

    show billy thumbup
    show bill casualface
    with dissolve
    billy "You got it, buddy!"
    show billy belly with dissolve
    billy "I thought you might want an outfit to match your new job!"
    billy "Back when you were being questioned I heard something about you being an assistant now!"
    show billy laugh
    hide bill
    with dissolve
    billy "Congratulations!"
    billy "That means we'll be able to spend lots of time together!"
    "I try the clothes on and it all fits surprisingly well!"

    me "Wow, Billy, I can't remember the last time I had brand-new clothes!"
    me "Thank you so much!"
    show bill starsmile at left:
        yalign 0.4 xalign -0.08
    with dissolve
    billy "You look dashing!~"
    show billy finger
    hide bill
    with dissolve
    billy "Also, Emelie told me you can sleep in her room tonight!"
    me "!!"
    show billy wary with dissolve
    billy "What's with that blushing expression? "
    billy "You won't be sleeping in the same bed as the princess, silly!"
    show billy base with dissolve
    billy "Her main room is way up in the tower! "
    "Oh..."
    show billy casual with dissolve
    billy "But you should probably wait a few hours 'til Rolf is done fixing up the door!"
    billy "But I have an idea of what we can do in the meantime!"
    show bill laughface at left:
        yalign 0.4 xalign -0.08
    with dissolve
    billy "Meet me down by the fountain in a bit! "
    billy "I'll take care of your old clothes."
    me "Sure, Billy!"
    window hide
    play sound "audio/soundFX/Run.mp3"
    hide bill
    hide billy
    with easeoutleft
    window show
    "He wobbles out the door with my old ragged clothes."
    "I head outside after giving my hair a final rub-down."

    jump Chapter2AndHalf

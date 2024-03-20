

label DinnerDay:
    $ renpy.pause(2.0, hard=True)
    $ bronwen_name = "???"
    $ granny_name = "???"
    #Sound
    #BLAM
    play sound "audio/soundFX/Door Slam.wav"
    window show
    " The door whips open with a bang and I jolt out of bed!"
    window hide
    scene bg emelieroomnobook
    show emc panic at right:
        yalign 0.15
        zoom 1.0
    show emear high at right:
        yalign 0.15
        zoom 1.0
    show emf panic2 at right:
        yalign 0.15
        zoom 1.0
    with fade
    play music "audio/starting-out-waltz-vivace-by-kevin-macleod-from-filmmusic-io.mp3" fadein 0.1 volume 0.3
    with hpunch
    window show
    emelie " I'm SO sorry!"
    show emf gross with dissolve
    emelie " 'Was gonna catch up with you yesterday but I showed up late to my classes and ended up in detention!"
    show emc out

    with dissolve
    emelie " Helga kept me there for HOURS!"
    show emc proper
    show emf concern
    with dissolve
    emelie " When I finally got to my room in the tower to drop my books off I crashed on the bed!"
    emelie " I woke up just half an hour ago and ran here immediately!"
    me " Detention for hours?!"
    me " Now I see why you got so worried when you heard the bells ring yesterday!"
    hide emear
    show emf insecure
    with dissolve
    emelie "Yeah... And sorry for waking you up just now!"
    me " No worries!"
    me " I might've slept better than ever... "
    me "You've got a really comfy bed."
    show emc proper

    show emf laugh
    with dissolve
    emelie " Haha! Happy to hear that!"
    " I look her up and down, my head finally clear after just waking up."
    show emc normal
    show emf insecure
    show emblush at right:
        yalign 0.15
        zoom 1.0
    with dissolve
    emelie " Oh...eeh."
    emelie " Since my dress got all messed up I had to go with a more casual outfit today..."
    window hide
    menu:
        with dissolve
        "You look great!":

            window show
            me "You look great!"
            show emf bigsmile
            show emc out
            show emear high at right:
                yalign 0.15
                zoom 1.0
            with dissolve
            emelie " Thank you!"


        "The more casual look suits you!":
            window show
            me "The more casual look suits you!"
            show emf bigsmile
            show emc out
            show emear high at right:
                yalign 0.15
                zoom 1.0
            with dissolve
            emelie " Thank you! "
            emelie "It's pretty nice not having to balance a crown on my head all day too!"

        "Those panties showing is really hot.":
            window show
            me "Those panties showing is really hot."
            hide emblush
            show emf panic
            show emc panic
            with dissolve
            emelie "W-whaa!"
            show emeye down at right:
                yalign 0.15
                zoom 1.0
            with dissolve
            "She looks down and notices "
            show emc proper
            show emf insecure
            show emblush
            show emear high at right:
                yalign 0.15
                zoom 1.0
            show emeye side2 at right:
                yalign 0.15
                zoom 1.0
            with dissolve
            emelie " It's... not on purpose! "
            emelie " These shorts are just really tiny so they end up showing!"
            me " Right..."
            show emf bigsmile
            show emc out
            hide emear high
            hide emeye
            with dissolve
            emelie " B-but thank you!"
    window hide
    show black with dissolve
    window show
    play sound "audio/soundFX/Get.mp3"
    "I put my new clothes on and get out of bed."
    play sound "audio/soundFX/Blanket Move.wav"

    window hide
    hide black with dissolve
    hide emear
    show emc think
    show emf normalblushthink
    with dissolve
    window show
    emelie " And you sure look dashing today too!"
    me " T-thanks! "
    me "Billy bought me some new clothes."
    show emc normal
    show emf bigsmile
    hide emblush
    with dissolve
    emelie " Oh, I'm glad to hear he found you yesterday!"
    emelie " I told him to keep you company as I was rushing to class!"
    me " He bumped into me when I was naked."
    show emf laugh with dissolve
    emelie " Haha! "
    show emf normal with dissolve
    emelie "..."
    show emf wide
    show emc out
    with dissolve
    emelie " Then what? "
    show emf grin with dissolve
    "She grins."
    show emc hips with dissolve
    emelie " Did things get steamy between you two as well ooor-"

    me "N-no!"
    me " He took me to the library and we read for a bit!"
    show emf laugh with dissolve
    emelie "That sounds fun! "
    show emf bigsmile with dissolve
    emelie "You must've met Victoria then?"
    me " Yep! "
    me "She was very friendly."
    show emc normal
    show emf normal
    with dissolve
    emelie " Yeah, she's got a real passion for her job!"
    emelie " What did you end up reading? "
    if scarybook == True:
        me " A book about a wolf blowing some pig houses down."
        me " Billy found it really scary, but it was all build-up with a super abrupt ending. "
        me " It had some gruesome pictures in it at least!"



    if scarybook == False:
        me " A really weird educational book..."
        show emf surprise with dissolve
        emelie " Oh? What was it about? "
        window hide
        menu:
            with dissolve
            "Sex.":
                window show
                me "Sex."
                show emc out
                show emf wide
                show emeye scared at right:
                    yalign 0.15
                    zoom 1.0
                with dissolve
                emelie "!!"
                hide emeye
                show emf weirdo2
                with dissolve
                emelie " Doesn't sound like something Billy would pick out..."
                show emf grumpy
                show emc hips
                with dissolve
                emelie " I'm sure you were the one who picked it!"
                me " Yeah..."
                me " But he sure seemed to like it! He spent over an hour staring at all the pictures... "

            "Nature... stuff...":
                window show
                me "Nature... stuff..."
                show emf bigsmile with dissolve
                emelie " Nature is interesting!"

                emelie " And Billy loves the outdoors!"
                me " Yeah, he sure seemed to like it! He spent over an hour staring at all the pictures... "


    show emf surprise
    show emc proper
    with dissolve
    emelie " Oh? I love when books include pictures!!"
    show emf normalblush with dissolve
    emelie " \"Humane Hunk\" has a few pictures in it too! I'll show you an interesting one!"
    window hide
    hide emc
    hide emf
    with easeoutright


    play sound "audio/soundFX/Open Drawer.wav"
    window show
    "She grabs the book."
    window hide

    show emc book at right:
        yalign 0.15
        zoom 1.0
    with easeinright
    window show

    emelie "Here, take a look! "
    window hide
    show emf normal at right:
        yalign 0.15
        zoom 1.0
    with dissolve
    pause 0.3
    show emc normal

    with dissolve
    play sound "audio/soundFX/Get.mp3"
    show blackopacity
    show ritabookopen1
    with dissolve
    pause 0.3
    window show
    emelie " See?? "
    me " Woah."

    emelie " I only just got to this part yesterday!"
    emelie "Did some sneaky reading during my detention when Helga left the room!"
    emelie " I don't really know what all these things are for though!"
    emelie "Looks like a blindfold and some rope... "
    emelie " It seems like they're going to be used for some naughty acts!"
    emelie "I've heard about people who like being tied up and stuff."
    emelie " I kinda get the appeal of giving up control, but what's with the blindfold!? "
    emelie " I would wanna see the action!"
    emelie " What do you think?"
    window hide

    menu:
        with dissolve
        "I agree. I wouldn't wanna miss out on the visuals!":

            window show
            me "I agree. I wouldn't wanna miss out on the visuals!"
            emelie " Exactly!"


        "I think it sounds pretty fun! Experiencing unpredictable physical sensations.":
            window show
            me "I think it sounds pretty fun! "
            me "Experiencing unpredictable physical sensations."
            emelie " Maybe! "
            emelie "But I think I'd just get paranoid!"
            me " Haha yeah, it'd be kinda scary if you didn't trust your partner!"

    emelie " And then there's this... plug thing."
    " I put the book back down."
    window hide
    play sound "audio/soundFX/Get.mp3"
    hide blackopacity
    hide ritabookopen1
    with dissolve

    show emf think
    show emc think
    with dissolve
    window show

    emelie " I don't know what it does yet but they call it a \"buttplug\"!"
    me " Oh..."
    me " I think I can figure out where it goes with a name and shape like that."
    show emc out
    show emf surprise
    with dissolve
    emelie "What do you mean?"
    show emf wide with dissolve
    emelie "..."
    show emf surprise

    show emc panic
    show emear high at right:
        yalign 0.15
        zoom 1.0
    show emeye scared at right:
        yalign 0.15
        zoom 1.0
    show emblush at right:
        yalign 0.15
        zoom 1.0
    with dissolve

    emelie "!"
    show emc out
    hide emeye
    hide emear
    show emf insecure

    with dissolve
    emelie " Oh... Of course!"
    emelie " That's pretty interesting!"
    if buttprodsuccess == True:
        show emf bite with dissolve
        emelie " I kinda want one... after how good your fingers felt there yesterday!"
    else:

        emelie "Hmm..."
    show emf concern
    hide emblush
    with dissolve
    emelie " I wish I could get stuff like that... But everyone knows my face!"
    show emf insecure with dissolve
    emelie "I can't ask the smith to make one for me."
    emelie " I'd be recognized immediately!"
    show emc proper
    show emf bigsmile
    show emblush at right:
        yalign 0.15
        zoom 1.0
    with dissolve
    emelie " Wouldn't want rumors of the \" Princess' huge buttplug \" spreading around town!"
    show emf laugh
    with dissolve
    emelie " And I can't ask Billy for something like that, he's too innocent haha!"
    " I could probably get her some stuff! "
    me " Well now that I'm your assistant..."
    window hide
    play sound "audio/soundFX/FX3/bellyrumble.wav" volume 0.4
    with hpunch

    window show

    " My stomach rumbles before I can finish my sentence."
    show emc panic
    hide emblush
    show emear high at right:
        yalign 0.15
        zoom 1.0
    show emf panic
    with dissolve
    emelie " Oh no!"
    emelie " You must be starving!"

    show emc out
    show emf sad
    with dissolve
    emelie " You're my guest and I haven't given you anything to eat ever since we met!!"
    me " Don't worry I'm okay-"
    show emf concern
    show emeye side2 at right:
        yalign 0.15
        zoom 1.0
    with dissolve
    emelie " And I'm hungry too! "
    hide emeye with dissolve
    emelie " I missed out on both dinner and supper yesterday."
    show emc hips
    show emf smile
    with dissolve
    emelie  " Let's get some breakfast!"
    emelie " Follow me!"
    stop music fadeout 1.0
    window hide
label walktodinner:
    scene black with fade
    window show
    "I follow Emelie outside."
    window hide
    play music "audio/Birds.wav" fadein 2.0 volume 0.9
    scene bg fountain
    show emc normal at right:
        yalign 0.1 xalign 1.05
        zoom 1.0
    with dissolve
    pause 0.3
    window show

    emelie " I'm pretty happy I dressed so casually! "
    show emf insecure at right:
        yalign 0.1xalign 1.05
        zoom 1.0
    with dissolve
    emelie "I don't like attracting a bunch of attention..."
    show emc hips
    show emf smile at right:
        yalign 0.1 xalign 1.05
        zoom 1.0
    with dissolve
    emelie " See that building back there to the left? "
    emelie "That's where we're going!"
    show emf bigsmile with dissolve
    emelie " Got the best pancakes in town!"
    window hide
    show blackopacity
    show tavern
    with dissolve
    window show
    "We start walking and I look up towards the diner and spot people eating!"
    "The pleasant smell of various spices fills my nose as we approach the open door."
    play sound "audio/soundFX/OpenDoor 1.wav" volume 0.5
    play music "audio/Tavern+Brawl+-+320bit.mp3" fadein 2.0 volume 0.4
    window hide
    pause 0.5
    play sound "audio/soundFX/FX2/shop-door-bell.wav" volume 0.5

    scene bg dinerback

    show granny down at left:
        yalign 1.2 xalign 0.2
        zoom 0.9
    show gran smile at left:
        yalign 1.2 xalign 0.2
        zoom 0.9
    show granshadow at left:
        yalign 1.2 xalign 0.2
        zoom 0.9
    show dinerdesk
    show dinercleaver
    with fade

    window show
    granny " Welcome welcome! "
    show granny up
    show gran base
    with dissolve
    granny " How can I serve you today? "
    show emc normal at right:
        yalign 0.10
        zoom 1.0
    show emf smile at right:
        yalign 0.10
        zoom 1.0
    show emeye side1 at right:
        yalign 0.10
        zoom 1.0

    with dissolve
    emelie " Good day, granny!"
    show emf bigsmile at right:
        yalign 0.10
        zoom 1.0
    show emc hips
    hide emeye
    with dissolve
    emelie " Me and [Protagonist] here are starving!"
    show gran laugh with dissolve

    granny " Well hello, Emelie!"
    granny " Almost didn't recognize you!"
    show gran teethy with dissolve

    granny " And what a handsome young man! "
    show gran smile with dissolve
    granny "The name's Margaret but most piggies around here call me \"Granny!\" "

    menu:
        with dissolve
        "Call her \"Granny\".":

            window show
            $ GrannyName = True
            me "Nice to meet you, Granny!"
            $ granny_name = "Granny"


        "Call her \"Margaret\".":
            window show
            $ GrannyName = False
            me "Nice to meet you, Margaret!"
            $ granny_name = "Margaret"
    granny "[Protagonist], was it? "
    granny "Nice to meet you too!"
    me " It smells really great in here!"
    show gran laugh with dissolve

    granny "I'm glad to hear that! "
    show granny down with dissolve
    granny " We've got three different dishes on today's menu."
    " I look up at the menu above. "
    window hide
    show blackopacity
    show dinersign
    with dissolve
    pause 0.4
    window show
    granny " We've got some crispy \" Grub Sticks \" and big juicy \"Craburgers\"!"
    granny" And of course my famous pancakes, but they're always on the menu!"
    emelie " I'll have a shortstack with extra syrup!"
    emelie " What will you have, [Protagonist]? "
    window hide
    hide blackopacity
    hide dinersign
    with dissolve
    window show
    show emc normal
    show emf smile

    with dissolve
    emelie "You had any of these dishes before?"
    me " I've had pancakes but not the other ones!"
    show emc out
    show emf laugh
    with dissolve
    emelie " Gran makes the best pancakes! "
    emelie "I'll let you try some of mine!"
    show emc hips
    show emf bigsmile
    with dissolve
    emelie " But you should get one of the other meals for yourself!"

    emelie "To get a real taste of Hog Haven cuisine! "
    show emc proper
    show emf pout
    with dissolve
    emelie " Victoria loves grub sticks... but they're not really my thing!"
    emelie " I loved craburgers as a kid though! They're so fun!"
    me " Hmmm..."
    show granny up
    show gran base
    with dissolve
    granny " You should listen to your gut, [Protagonist]!"

    granny " What will it be? "
    window hide
    menu:
        with dissolve
        "A \"Grub Stick\"!":

            window show
            $ Grub = True
            me "I'll have a \"Grub Stick\"!"


        "A \"Craburger\"!":
            window show
            $ Grub = False
            me "I'll take a \"Craburger\"!"
    show granny up
    show gran teethy
    with dissolve
    granny " Great! I'll get right to it! "
    show gran laugh with dissolve
    granny "You two sweethearts go find yourselves a table and I'll prepare your meals!"
    show emf smile with dissolve
    emelie " Yes yes!"
    me " Okay!"
    window hide
    show black with fade
    window show
    " I follow Emelie out back to a free table."
    window hide
    play sound "audio/soundFX/Sit Pillow.wav" volume 0.7

    scene bg cafe
    show emc sit at right:
        yalign 0.15
        zoom 1.0
    show cafetable
    with dissolve
    window show
    emelie " This will do!"
    show emf smile at right:
        yalign 0.15
        zoom 1.0
    with dissolve
    emelie " The weather is so great! I love being able to dine outside."
    me " Same! "
label hypothetical:
    show emf normal with dissolve
    emelie " So while we wait... "
    emelie "Let's do a quick hypothetical!"
    me " A what?"
    show emf laugh with dissolve
    emelie " I'll ask you a crazy question and you gotta give me an answer!"
    me " Oh..."
    me "Okay, hit me!"
    show emc sitthink
    show emf think
    with dissolve
    emelie " Would you rather have..."
    show emeye side2 at right:
        yalign 0.15
        zoom 1.0
    with dissolve
    emelie " One GIANT super strong arm..."
    show emeye scared with dissolve
    emelie " Or SIX long skinny arms??"
    window hide
    menu:
        with dissolve
        "One big giant arm!":

            window show

            me "One big giant arm!"
            hide emeye
            show emc sit
            show emf laugh
            with dissolve
            emelie " Haha, really? "
            show emf smile with dissolve
            emelie "I suppose you'd be able to lift some really heavy stuff with it!"
            show emf surprise with dissolve
            emelie " And maybe you could start a professional career as an arm wrestler!"
            show emc sitthink
            show emf think
            with dissolve
            emelie " I wonder if there's any money in arm wrestling..."
            show emeye side2 at right:
                yalign 0.15
                zoom 1.0
            with dissolve
            emelie " I guess if you chose six arms and you trained really, really hard you could arm wrestle six different people at once."
            show emc sit
            hide emeye
            show emf smile
            with dissolve
            emelie " I bet you'd be able to make some money that way!"
            " She's thinking hard about this. "
            show emf bigsmile
            show emear high at right:
                yalign 0.15
                zoom 1.0
            with dissolve
            emelie " And with six arms you could paint walls or lay bricks super fast!"
            show emf biggersmile with dissolve
            emelie "You could be super efficient at anything you choose!"
            me " That's true."
            me " But nobody could mess with me if I had a giant super-arm! "
            me "And what if I choose the six arms but they're so long and frail that they break really easily?"
            me " Then I'd be screwed!"
            hide emear
            show emc sitthink
            show emf think
            show emeye normal at right:
                yalign 0.15
                zoom 1.0
            with dissolve
            emelie " That's true!"
            show emeye side2 with dissolve
            emelie " I guess it depends on just how strong the six arms are. "
            me " Farming would certainly be a lot more efficient with six normal-strength arms!"
            me "I could dig, plant, collect and brush dirt off veggies all at the same time!"
            hide emeye
            show emc sit
            show emf smile
            with dissolve
            emelie " Smart!"
            me " But I still think I choose one huge arm!"
            me " Maybe I wouldn't even need a shovel anymore, I could just scoop the dirt up with my hand!"
            show emf laugh with dissolve
            emelie " Haha yeah, maybe you could just use your brute strength instead of a bunch of tools!"
            #emelie " Y'know a lot of us pigs use our snouts for digging!"

            show emf insecure
            show emeye side1 at right:
                yalign 0.15
                zoom 1.0
            show emblush at right:
                yalign 0.15
                zoom 1.0
            with dissolve
            emelie " But now that you're my assistant... "
            hide emeye
            with dissolve
            emelie "I worry about what future massages would be like with that crazy huge arm!"
            "She blushes at the thought of my mega arm \" massaging \" her."
            show emc normal with dissolve

            emelie " I'm not sure if I could handle a massage like the one you gave me yesterday if your arm was outrageous in size..."
            show emf bite with dissolve
            emelie " It was intense enough already!"
            me " That's a relief. "
            me "Means I won't have to start doing hundreds of daily one-armed pushups."
            hide emblush
            show emf laugh
            show emc sit
            show emear high at right:
                yalign 0.15
                zoom 1.0
            with dissolve
            emelie " Haha, yeah I don't think that's necessary!"



        "Six skinny arms!":
            window show

            me "Six skinny arms!"
            hide emeye
            show emc sit
            show emf laugh
            with dissolve
            emelie " Haha really? You'd be like a spider then! With 8 limbs!"
            show emc panic
            show emf panic
            with dissolve
            emelie " Spiders are scary!"
            show emc sit
            show emf normal
            with dissolve
            emelie " I think I'd choose 6 too! "
            emelie "Then I could get a bunch of work done at once! "
            show emf bigsmile
            show emear high at right:
                yalign 0.15
                zoom 1.0
            with dissolve
            emelie " I could apply my makeup and brush my hair and scratch my own back all at once! "
            emelie "And I'd still have 3 arms left! "
            show emf biggersmile with dissolve
            emelie " And maybe if I use all 6 arms at once they'd be just as strong as the single super-strong arm! "
            emelie "Win-win choice!"
            hide emear
            show emc normal
            show emf wide
            with dissolve

            emelie " But I bet my teacher Helga would force me to work three times harder if I had three times as many arms..."
            show emf gross with dissolve
            emelie " That sounds rough! "
            show emc sit
            show emf grin
            with dissolve
            emelie " So now I changed my mind! "
            show emf grin2 with dissolve
            emelie "With one big arm maybe she'd ease up on me!"
            emelie " And if not I could hold her off using my new super-strength!"
            me  "I think six arms would help more with farming than one giant arm! "
            show emf normal with dissolve
            emelie " Oh?"
            me " To use a shovel you use your feet and stuff, so crazy strength with just one arm might not help very much... but with six arms I could do lots!"
            hide emeye
            show emc sit
            show emf smile
            with dissolve
            emelie " Smart!"
            me " And if I got dirt under my nails and I only had the one giant arm... It'd be a pain in the ass to get rid of it!"
            me " That's why I choose six arms!"
            show emf insecure

            show emblush at right:
                yalign 0.15
                zoom 1.0
            with dissolve

            emelie " Or now that you're my assistant... "
            show emeye side1 behind emblush at right:
                yalign 0.15
                zoom 1.0
            with dissolve
            emelie "You could give me a super intense massage with six arms!"
            me "... I bet you'd like that. "
            show emf normalblush
            hide emeye
            with dissolve
            emelie " Haha maybe! "
            "She blushes at the thought of my six arms \" massaging \" her."
            show emf laugh with dissolve
            emelie "But I like you plenty as is! "
            show emf wide
            show emc normal
            hide emblush
            with dissolve
            emelie "I think you might look kinda creepy with so many arms... "
            show emf bite
            show emc sit
            show emblush at right:
                yalign 0.15
                zoom 1.0
            with dissolve
            emelie " And your technique is great as is!"
            me " That's a relief! "
            me "Or I'd have to start using all these \"creepy toes\" as well as my hands!"
            "I give her feet a little poke with my own under the table."
            show emear high at right:
                yalign 0.15
                zoom 1.0
            show emf laugh
            hide emblush
            with dissolve
            emelie " Haha!"
            show emf biggersmile with dissolve
            emelie " Yeah, I don't think that's necessary! "
    hide emear
    hide emeye
    show emf normal
    show emc sit
    with dissolve

    emelie " Anyways I think hypotheticals like this are fun because they make ya think and problem-solve and stuff!"
    show emf smile with dissolve
    emelie " The answer you land on isn't too important!"
    emelie " I'm really happy you engaged with it!"
    show emf sad with dissolve
    emelie " A lot of people don't think my hypotheticals are grounded enough in reality..."
    show emeye normal at right:
        yalign 0.15
        zoom 1.0
    with dissolve
    me " That's a shame, I found it fun! "
    me " If you ever think of another one you can rely on me to answer it!"
    show emf normalblush with dissolve
    "Emelie nods and looks happy!"
label eatfood:
    window hide
    play sound "audio/soundFX/run2.wav"
    show granny down behind cafetable at left:
        yalign 7.7 xalign -0.1
        zoom 1.0
    show gran smile behind cafetable at left:
        yalign 7.7 xalign -0.1
        zoom 1.0
    with easeinleft
    pause 0.5
    play sound "audio/soundFX/FX3/dinner-plate-impact.wav"
    show cafecutlery
    show cafecutleryfork
    if Grub == True:
        show grubstick
    if Grub == False:
        show craburger
    with dissolve
    window show
    granny " Here's your food!"

    if GrannyName == True:
        "Granny puts our meals and some drinks on the table."
    else:
        "Margaret puts our meals and some drinks on the table."
    show gran teethy at left:
        yalign 7.7 xalign -0.1
    with dissolve
    granny " I hope you'll enjoy!"

    show granny up
    show gran laugh
    with dissolve
    granny " Just give yours a minute to cool off or you might burn your mouth, [Protagonist]!"

    me " Okay, thank you!"
    show emf smile
    show emeye side1 at right:
        yalign 0.15
        zoom 1.0
    with dissolve
    emelie " Looks lovely! "
    show emf bigsmile with dissolve
    emelie "Thanks, granny!"

    show gran smile with dissolve
    " She nods and wiggles back inside."
    window hide
    play sound "audio/soundFX/run2.wav"
    hide granny
    hide gran
    with easeoutleft
    hide emeye
    show emf bigsmile

    with dissolve
    window show
    emelie " So you've never eaten this stuff before, huh? "
    show emf surprise with dissolve
    emelie " What does dinner on your farm typically look like?"

    me "Us farmers often trade with each other."
    me "So ends up being a lot of different raw ingredients like veggies and potatoes and stuff like that."
    me " It's pretty basic stuff, but always really fresh!"
    show emf normal with dissolve
    emelie "I see!"
    show emf smile with dissolve
    emelie " A lot of our meals are based on veggies and stuff too! "
    emelie "And since we're right by the coast we also get a lot of things from the ocean! "
    show emf pout with dissolve
    emelie " Around this time of the year a lot of insects are on the menu too!"
    play sound "audio/soundFX/FX3/plate-with-cutlery.wav"
    pause 0.2
    hide cafecutleryfork
    show emc siteatlow
    show emf normalblush
    with dissolve
    "She picks her fork up, leaving the knife on the table."
    emelie " Well, I think it's about time we dig in! "
    show emc siteat
    show emfeatopen at right:
        yalign 0.15
        zoom 1.0

    show emf laugh
    with dissolve
    emelie "Don't want to risk the food getting cold!"
    show emfeatclosed behind craburger at right:
        yalign 0.15
        zoom 1.0
    hide emfeatopen
    with dissolve
    me " Yes yes!"
    " I'm a little worried about my meal of choice but let's give it a go. "
    " I don't think I need to use any cutlery for this!"
    if Grub == True:
        window hide
        play sound "audio/soundFX/Get.mp3"
        show blackopacity
        show grub one
        with dissolve
        window show
        "It's a giant grilled grub on a stick. I don't know what else I expected."
        " I've barely eaten insects before, and definitely not a big juicy larva {i}thing{/i} like this!"
        "But I guess there's a first for everything..."
        "I gather some courage and take a  bold bite "
        play sound "audio/soundFX/FX3/crunch.wav"volume 0.7
        show grub two with dissolve
        " My mouth fills with incredibly hot, stringy goo!"
        " The change in texture is very odd. "
        " The outside's crispy with a nice snap to it..."
        " But then the inside is like melted cheese!"
        "..."
        "Part of my brain wants to reject the food..."
        "But my taste buds are begging for more!"
        "It's surprisingly really good!"
        "I munch down more. Slurping all of the grub's insides down."
        "Stringy grub guts dangle from my chin as I go rabid."
        " I haven't eaten anything this rich and complex in flavor before!"
        show black with dissolve
        hide grub
        hide blackopacity
        "My mind goes blank, and I come back with my plate completely clean and my glass empty!"
        hide black
        play sound "audio/soundFX/FX3/fork-bing.wav"
        hide cafecutlery
        hide craburger
        hide grubstick


        show emc siteatlow behind cafetable at right:
            yalign 0.15
            zoom 1.0
        hide emeye
        show emf panic2 at right:
            yalign 0.15
            zoom 1.0
        show emeye panic at right:
            yalign 0.15
            zoom 1.0
        hide emfeatclosed
        show cafedirtydishesforkless
        with dissolve
        me " Puh... That was amazing."
        "Emelie looks at me in horror "
        hide emeye
        show emf gross
        with dissolve
        emelie " I've never seen anyone gawk down a grub stick like that before... "
        emelie " Except maybe Victoria... but she has a different technique."
        show emc siteatlow
        hide emfeatclosed
        show emf insecure
        with dissolve

        emelie " I finished my pancakes too! "
        show emf laugh with dissolve
        emelie "Yummy like always!"
    if Grub == False:
        window hide
        play sound "audio/soundFX/Get.mp3"
        show blackopacity behind craburger
        show craburger one
        with dissolve
        pause 0.3
        window show
        " It's a giant burger oozing with ingredients!"
        "It's made to resemble a crab, with two crab claws sticking out from the center!"
        " The patty looks to be made out of crab meat. "
        "I take a bite "
        play sound "audio/soundFX/FX3/crunch.wav"volume 0.7
        show craburger two with dissolve
        "My teeth easily cut through the bun, with the following textures being varied with both crispy, soft and snappy parts!"
        " It's really good and juicy!"

        " I eat the... \"eyes\". "
        play sound "audio/soundFX/Jar Open.wav" volume 0.3
        pause 0.2
        play sound "audio/soundFX/Jar Open.wav"volume 0.4
        pause 0.2
        play sound "audio/soundFX/FX3/crunch-2.wav"volume 0.4
        show craburger three with dissolve

        " They're a nice contrast in flavor to the other parts of the burger!"
        " But the burger lost a bit of charm with them gone..."
        show black with dissolve
        "My mind goes blank as I start slurping on the crab claws to savor every last part of the burger. "
        " I come back with my plate completely clean and my glass empty!"
        hide black
        play sound "audio/soundFX/FX3/fork-bing.wav"
        hide cafecutlery
        hide craburger
        hide grubstick
        hide blackopacity
        show emf laugh
        hide emfeatclosed
        show emfeatopen behind craburger at right:
            yalign 0.15
            zoom 1.0
        show emc siteat
        show cafedirtydishesforkless
        with dissolve
        me " Puh... That was amazing."
        show emfeatclosed behind craburger at right:
            yalign 0.15
            zoom 1.0
        with dissolve
        show emc siteatlow
        hide emfeatopen
        hide emfeatclosed
        show emf eat
        with dissolve
        emelie " I know! And the presentation is just so fun! "
        show emf bigsmile with dissolve
        emelie " As a kid I would always save the \" eyes\"  for last because of the added personality!"
    window hide

    play sound "audio/soundFX/FX3/plate-with-cutlery.wav"
    hide cafedirtydishesforkless
    show cafedirtydishes
    hide emfeatclosed
    show emc sit

    with dissolve
    pause 0.2
    play sound "audio/soundFX/run2.wav"
    show granny down behind cafetable at left:
        yalign 7.7 xalign -0.1
        zoom 1.0
    show gran smile  behind cafetable at left:
        yalign 7.7 xalign -0.1
        zoom 1.0
    with easeinleft
    pause 0.2
    show emeye side1 at right:
        yalign 0.15
        zoom 1.0
    hide gran
    with dissolve
    window show
    granny " Everything taste okay?"
    me " Amazing, thank you!"
    if Grub == True:
        me " My first grub stick, but hopefully not my last!"
    else:
        me " And the presentation was really fun!"
    show emear high at right:
        yalign 0.15
        zoom 1.0
    show emf smile
    with dissolve
    emelie " Your pancakes are just the best!"
    show gran laugh behind cafetable at left:
        yalign 7.7 xalign -0.1
        zoom 1.0
    with dissolve
    granny " Oh, that makes me really happy!"
    granny "I'll take care of your plates!"
    hide emear
    show emf biggersmile
    with dissolve
    emelie " Thank you!"
    play sound "audio/soundFX/FX3/dinner-plate.wav"
    hide cafedirtydishes
    with dissolve
    play sound "audio/soundFX/run2.wav"
    hide gran
    hide granny
    with easeoutleft
    hide emeye with dissolve
    emelie " ..."

    emelie " She likes you! "
    show emf wide with dissolve
    emelie " Oh right, I've got to go pay for the food!"
    emelie "Just one second and I'll be right back!"
    play sound "audio/soundFX/Sit Pillow.wav" volume 0.7
    hide emf
    show emc normal at right:
        yalign 0.25
        zoom 1.0
    with dissolve
    play sound "audio/soundFX/run2.wav"
    hide emc with easeoutleft

    if GrannyName == True:
        "Emelie hurries off after Granny."
    else:
        "Emelie hurries off after Margaret."
    " I take the time to stretch and let a burp slip."
label dessert:
    "Phew! "
    "That meal really filled me with energy!"
    play sound "audio/soundFX/run2.wav"
    show emc creamdown behind cafetable at right:
        yalign 0.25 xalign 0.5
        zoom 1.0

    show emear high behind cafetable at right:
        yalign 0.25 xalign 0.5
        zoom 1.0
    show emf biggersmile behind cafetable at right:
        yalign 0.25 xalign 0.5
        zoom 1.0
    show icecream full behind cafetable at right:
        yalign 0.25 xalign 0.5
        zoom 1.0
    with easeinleft

    emelie " [Protagonist]! "
    with hpunch
    emelie "Look what Gran made us!"
    show emeye down behind cafetable at right:
        yalign 0.25 xalign 0.5
        zoom 1.0
    show emf smile
    show emc creamscoop
    with dissolve
    emelie "A giant ice cream to share for dessert!!"
    me " Woah!"
    me " That looks insane!"
    hide emeye with dissolve
    emelie " It's got chocolate, vanilla & strawberry!"
    show emf laugh with dissolve
    emelie " With actual strawberries and crispy waffles, topped off with chocolate sauce!"
    me " I've never seen anything like that before!"
    show emf insecure
    hide emear
    with dissolve
    emelie " I guess the waffles were my breakfast... and this will count as lunch!"
    show emeye side2 behind cafetable at right:
        yalign 0.25 xalign 0.5
        zoom 1.0
    with dissolve
    emelie " Maybe not the healthiest morning in the world but I think that's okay every now and then..."
    hide emeye
    show emf normalblush
    with dissolve
    emelie "Granny knows I have a real sweet tooth! "
    me " I'm excited to try it!"
    show emf smile with dissolve
    emelie " My favorite layer is the strawberry one!"
    me " Oh, that's probably the flavor I'm most used to! "
    me "You can have it when we get to it."
    show emf laugh with dissolve
    emelie " Aw thanks! "
    show emf grin with dissolve
    emelie "But we gotta work together to reach it! "
    show emf pout
    show emc creamdown
    with dissolve
    emelie " Let's go for a walk in the park while we eat! "
    emelie "It's right here back behind the hedges!"
    window hide

    show sky
    show blackshake at truecenter behind sky
    show blackopacity
    show handhold
    with fade
    play sound "audio/soundFX/Get.mp3"
    with vpunch

    window show
    " Emelie grabs my hand and we start walking towards the center of the park."
    "Her hand feels so gentle in my grip. "
    " She scoops me some ice cream as I hold the big glass cup with my other arm. "
    " The cold ice cream and rich chocolate taste incredible!"
    " We come to a stop at our destination. "
    window hide
    scene bg whale
    show emc creamdown at right:
        yalign 0.15
        zoom 1.0

    show icecream full at right:
        yalign 0.15
        zoom 1.0
    with fade
    window show
    me " Woaah! A giant fountain depicting some sort of animal!"
    show emf smile at right:
        yalign 0.15
        zoom 1.0
    with dissolve
    emelie " Cool, right??"
    show emf bigsmile with dissolve
    emelie " I wanted to show you this!"
    show emf biggersmile with dissolve
    emelie " This park has all sorts of amazing statues! "
    show emf surprise with dissolve
    emelie "They say these sculptures depict actual ocean animals!"
    emelie " I've never seen anything this big with my own eyes though!"
    " I look in awe at the fountain as Emelie spoons down some more ice cream."
    window hide
    hide emf with dissolve
    pause 0.3
    show emc creamscoop with dissolve
    window show
    emelie " They say this big one is of a \" Blue whale \" !"
    play sound "audio/soundFX/FX3/plate-with-cutlery.wav"
    window hide
    show emc creameat with dissolve
    show emf eat at right:
        yalign 0.15
        zoom 1.0
    show emc creamscoop
    show icecream half


    with dissolve
    window show



    emelie " Apparently the biggest mammal we know of right now!"
    show emf insecure with dissolve
    emelie "... I thought it was some kinda fish when I first saw it."
    window hide
    menu:
        with dissolve
        "It's an easy mistake to make! They do have fins and swim all day.":
            window show
            me "It's an easy mistake to make! They do have fins and swim all day."
            show emc creamdown at right:
                yalign 0.15
                zoom 1.0
            show emf laugh
            with dissolve
            emelie " Yeah exactly!"

        "Wait... It's not a fish? It looks like a fish to me!":
            window show
            me "Wait... It's not a fish? It looks like a fish to me!"
            show emf wide
            show emc creamdown at right:
                yalign 0.15
                zoom 1.0
            with dissolve
            emelie " I know, right?! "
    show emf think with dissolve
    emelie " I think fish have scales and don't need to breathe air or something?"
    show emeye normal at right:
        yalign 0.15
        zoom 1.0
    with dissolve
    emelie " Maybe they lay eggs? Or most of them do at least?"
    hide emeye
    show emf sleep
    with dissolve
    emelie " I'll have to ask Victoria next time I see her..."
    emelie "She knows all about this stuff!"
    show emf biggersmile with dissolve
    emelie " The older I get the more amazed I am by nature! "
    show emf laugh with dissolve
    emelie " And I just love the sounds of the little waterfalls and fountains here!"
    window hide
    hide emf with dissolve
    pause 0.3
    show emc creamscoop with dissolve
    window show
    "We eat some more ice cream."
    play sound "audio/soundFX/FX3/plate-with-cutlery.wav"
    window hide
    show emc creameat with dissolve
    show emf eat at right:
        yalign 0.15
        zoom 1.0
    show emc creamscoop
    show icecream little
    with dissolve
    window show
    me " That chocolate is so good!"
    me " But now I'm full."
    emelie  "Let's check one of the small statues out a bit closer!"


    hide emc
    hide emf
    hide icecream
    with dissolve
    show blackshake at truecenter behind bg
    show bgwhaleblowfish
    with dissolve
    "Emelie runs off and kneels in front of one of the statues!"

    show blackopacity
    show blowfish one
    with dissolve
    emelie " Look at this guy!"
    emelie " He's always looked a bit grumpy."
    emelie " I think this is called a \"Blowfish\"!"
    emelie " Maybe he'd like some ice cream too, haha!"
    show blowfish two
    with dissolve
    "Emelie jokingly raises the spoon toward the statue. "
    emelie " Open up, cutie!"
    show blowfish three with dissolve
    play sound "audio/soundFX/FX3/water-spraying.wav"
    with vpunch


    emelie " Waa!"
    "The weird fish statue turned out to be a fountain as well!"
    "It spat the spoon right out of her hand, sending it flying far from sight!"
    show blowfish four with dissolve
    emelie "..."
    emelie " This one has no manners! "
    emelie "No ice cream for you!"
    window hide
    hide blowfish
    hide blackopacity
    with dissolve
    hide bgwhaleblowfish
    with dissolve
    show emc casualcream at right:
        yalign 0.15
        zoom 1.0
    show icecream little at right:
        yalign 0.15
        zoom 1.0
    show emf gross at right:
        yalign 0.15
        zoom 1.0
    with dissolve
    window show
    emelie " That sure took me by surprise!"
    emelie " I think I saw where the spoon landed, follow me!"
    scene black with dissolve
    "We follow a thin path back behind some hedges. "
    window hide
    play sound "audio/soundFX/FX3/shaken-bush.wav"
    show bg hedge
    show blackshake at truecenter behind bg
    show emc casualcream at right:
        yalign 0.15
        zoom 1.0
    show icecream little at right:
        yalign 0.15
        zoom 1.0
    show emf insecure at right:
        yalign 0.15
        zoom 1.0
    with fade
    with hpunch
    window show
    emelie " Aw, I can't find the spoon! "
    emelie "And we're right at the strawberry layer I love so much!"
    show emf surprise with dissolve
    emelie  " Oh well, can't be helped."
    hide emf with dissolve
label BeejGallery:
    play music "audio/Tavern+Brawl+-+320bit.mp3" volume 0.4 if_changed
    show bg hedge
    show blackshake at truecenter behind bg
    show emc casualcream at right:
        yalign 0.15
        zoom 1.0
    show icecream little at right:
        yalign 0.15
        zoom 1.0
    if playnormal == False:
        with fade
        window show
    emelie "Bottoms up!"
    window hide
    hide icecream
    show emc drinkcream
    with dissolve
    pause 0.4
    window show
    " She raises the cup and slurps down the last bit of ice cream!"
    window hide

    show emc casualcream
    show emf eat at right:
        yalign 0.15
        zoom 1.0
    show emcreamcheek at right:
        yalign 0.15
        zoom 1.0
    show emeye close at right:
        yalign 0.15
        zoom 1.0
    with dissolve
    window show
    emelie " Yum! "
    hide emeye
    show emf insecure
    show emblush at right:
        yalign 0.15
        zoom 1.0
    with dissolve
    emelie " Maybe not the most princess-like behavior... "
    emelie "But nobody will know!"
    me " Your secret ice cream techniques are safe with me!"
    show emf laugh
    hide emblush
    with dissolve
    emelie " Haha, that's good!"
    me " But you got some on your cheek!"
    show emf fluster with dissolve
    emelie " O-oh? Where? "
    show emf licc with dissolve
    "She licks around her lips trying to find the sneaky ice cream."
    "She misses it completely. "
    show emf concern with dissolve
    emelie " Did I get it? "
    me " Not yet. "
    show emf licc with dissolve
    emelie " Aw shucks! "
    show emf fluster with dissolve
    emelie "Would you lend me a hand? "
    stop music fadeout 1.0
    me " Sure. "

label beejstart:
    #Mouthfingerin----------------------------------------------------
    play music "audio/6.+Tranquil+Fields+-+Peaceful+-+320bit.mp3" fadein 2.0 volume 0.3

    " I approach her."
    window hide
    scene emouthbase
    show blackshake at truecenter behind emouthbase
    show emouth mess1
    with fade
    pause 0.3
    window show
    "She definitely made a bit of a mess..."
    emelie" Where is it?"
    show emouth mess2 with dissolve
    emelie "Here? I'm trying to get it!"
    emelie" Help me out!"
    show emouth mess3 with dissolve
    me " Here, it's just out of reach."
    emelie " Now scoop it here!"
    "Wha-"
    " I guess I'll... give it to her"
    show emouth mess4 with dissolve
    " I scoop the leftover ice cream into her mouth, placing it on her tongue."
    emelie " Thank you!"
    show emouth mess5 with dissolve
    emelie " Mwuah!"
    "She sucks on my finger!"
    show emouth mess4 with dissolve
    emelie " I... kinda like that..."
    emelie " I think you got some on your other finger too?"
    me " Really?"
    show emouth mess6 with dissolve
    "I slowly slide my other finger along her tongue as well"
    emelie " Ahhn~"
    "She lets out a little moan."
    emelie " Thass ithhh~"
    " I  think she's getting off on having her mouth played with!"
    window hide
    menu:
        with dissolve

        "... You really like that ice cream, huh?":
            window show
            me "... You really like that ice cream, huh?"

        " You like having your mouth toyed with, don't you?":
            window show
            me " You like having your mouth played with, don't you?"


    " She tries nodding but struggles a bit as my fingers restrict her."

    show emouth mess7 with dissolve
    "I slide my fingers to the sides of her tongue, squishing it slightly."
    "This is definitely turning me on too! "
    "I feel my pants starting to stretch..."
    me " I uuh... think that's it!"

    me " I pull my hand back."
    show emouth mess8 with dissolve
    emelie " Phaaaaa... "
    emelie " I liked that very much! "
    emelie "Tasty tasty~"
    emelie "Thank you!"



    window hide
    show emkneesbase with fade
    pause 0.3
    window show
    emelie " But what's this? "
    emelie "Another treat?"
    "She suddenly kneels in front of my straining belt!"
    window hide
    show emk nees1 with dissolve
    pause 0.6
    window show
    emelie " Let's find out just what's hiding down here."
    me "... I think you know exactly what-"
    show emk nees2 with dissolve
    emelie "Ahaaa?"
    emelie " Want me to stoooop?"
    " She's teasing me!"
    me " N-no but... What if someone walks by?"
    emelie " This part of the park is pretty remote, especially at this hour when most piggies are at work~"
    emelie " I'll just have a quick little look~"
    window hide
    play sound "audio/soundFX/Blanket Move.wav"
    show emk nees3 with dissolve
    with vpunch
    pause 0.4
    window show
    emelie " !!"
    emelie "Whoa! So big!"
    emelie " It's casting this intimidating shadow on me!"
    me " It's the same size as yesterday!"
    emelie " But I wasn't THIS close to it with my face before!"
    me " You did get pretty close-"

    window hide

    show emballsuck1 with fade
    pause 1.0
    window show
    "!!"
    " She's licking my balls!"
    "Her tongue slowly motions around them with her hand moving up to rub my shaft."
    emelie " You like it when I do this??"
    emelie "I want to taste every part of it~"
    emelie " I'm such a hungry piggy~"
    "Her lips press against my balls as she slowly starts creating suction against them."

    " Maybe pigs really are a bit gluttonous..."
    " Or maybe Emelie just got really horny from me playing with her tongue just now."
    "I breathe deeply and moan as her lips move from one testicle to the other, making wet and sloppy plop sounds as she pulls away."
    window hide
    show emsidelicca with fade
    pause 0.4
    window show
    emelie " And now for this part~"
    "She slowly licks her way from my balls to my tip "
    emelie " So looong and thick... I love the weight of it resting on my face!"
    "Her saliva trails down her tongue and coats my balls even more, making a big mess already!"
    window hide
    menu:
        with dissolve



        "Keep going just like that!":
            window show
            me "Keep going just like that!"
            emelie " Mmmhh I hope I'll make it feel even better~"

        "I love that sloppy mouth!":
            window show
            me "I love that sloppy mouth!"
            emelie " I'll be sure to make it nice and wet~"
    window hide
    show blackopacity
    show jerk2
    with dissolve
    pause 0.4
    window show
    "She slowly licks the underside of my cocktip, holding my shaft in her hand."
    emelie " Mmmhhhn, I don't think all of this wetness is from me!"
    emelie" You're producing some of it yourself!"
    me " Y-yeah."
    me "You're making me leak some precum..."


    window hide
    show jerk1

    with dissolve
    pause 0.2
    window show
    " She pulls my foreskin down, her tongue now tickling my frenulum."
    me " A-Ahhh!"
    emelie " Mmmh but I like the taste~ "
    emelie " This is so fun to play with! "
    window hide
    hide jerk1
    show jerk2
    with dissolve
    pause 0.2
    window show
    emelie " I'm glad you like it~"
    emelie " Mmhh I want more..."
    window hide

    show jerk1
    hide jerk2
    with dissolve
    pause 0.4
    hide jerk1
    show jerk2
    with dissolve
    pause 0.4
    show jerk1
    hide jerk2
    with dissolve
    pause 0.4
    hide jerk1
    show jerk2
    with dissolve
    window show
    me " A-Ahh!"
    emelie " Puaahm~"
    emelie " But I'm craving more..."
    "She jerks my cock, making more precum collect at the tip!"





    window hide

    hide jerk2
    show cheekbulge1
    with dissolve
    with hpunch
    pause 0.4
    window show
    #Make cock look a bit bigger outside cheek
    "Then quickly takes my cocktip into her mouth!"
    emelie " Hmmgh!"
    "It bumps up against the side of her cheek!"
    emelie " Mblwaa?"
    window hide
    hide cheekbulge1
    show cheekbulge2
    with dissolve
    pause 0.4
    window show
    " She drools all over the place."
    emelie " Sho bhiggg..."
    " Her speech understandably isn't very clear..."
    me " T-that feels really good!"
    "She slurps on it for a few moments while looking up at me."
    window hide


    scene emkneesbase
    show blackshake at truecenter behind emkneesbase
    show emk nees4
    with fade
    with vpunch
    pause 0.4
    window show
    "She pulls back and her lips leave my tip with a loud 'pop'!"
    emelie " Phuaaah..."
    emelie " It started moving so excitedly when I put it in my mouth..."
    emelie " Did that feel extra good?"
    me "Yes!"
    emelie " I really like it in there too."
    emelie " With your tip  leaking so much..."
    emelie " The taste and smell gets me going!"
    emelie " But I think I can improve on my technique..."
    window hide
label bleej:
    # 3 paths. Rough facefuck with hands, facefuck with hands with her taking breaks to breathe etc. And no hands her pacing herself and sucking your balls some more etc.
    scene embleej
    show blackshake at truecenter behind embleej
    show embleye closeup
    with fade
    with hpunch
    pause 0.4
    window show
    me " Ahh!"
    emelie " Mmhhn..."
    "She steadies herself and takes my cock in her mouth again."
    me "That feels so good!"
    window hide
    hide embleye with dissolve
    pause 0.2
    window show
    " She opens her eyes and looks up at me as I moan."
    window hide

    show embdick dry2
    show embleye frown
    with dissolve
    pause 0.3
    window show
    " She moves her head forward slowly, trying to take more of my cock while avoiding it bulging her cheek."
    emelie "Hmmhh..."
    window hide
    show embdick wet1
    with dissolve
    window show
    "Her head bobs back again, leaving my shaft wet and dripping before moving forward again."
    window hide
    show embleye half
    show embdick dry2
    with dissolve
    pause 0.2
    window show
    "I thrust forward once more, my tip pressing up against the very opening of her throat."
    " She lets out a muffled groan as I feel her head pushing forward, trying to take more of me into her mouth."
    window hide
    show embdick wet1 with dissolve
    pause 0.7
    show embdick wet2 with dissolve
    pause 0.7
    show embdick wet1 with dissolve
    pause 0.7
    show embdick wet2 with dissolve
    window show
    show blackshake at truecenter behind embleej
    " After continuing to rock my hips back and forth for a bit Emelie lets out a nasal sigh before breathing in."
    window hide
    show embleye squint with dissolve
    with hpunch
    pause 0.3
    window show
    emelie " Hlk!"
    " Her arms shake a little and her back arches as my cocktip prods her soft palate."
    me " A-Ahh!"
    show embleej
    show embleye frown
    with dissolve
    " She looks up at me again."
    window hide
    show blackopacity
    show emeyecloseupnoheart
    with dissolve
    pause 0.2
    window show
    " Those lustful eyes non-verbally begging for more... "
    " She's trying really hard but failing to go deeper."
    "I could take control and grip her head to force her down as I thrust forward... Which could be pretty rough on her."
    " Or I could try to thrust deeper but more slowly while encouraging her to relax, leaving her in more comfortable control of the pace."
    window hide
    menu:
        with dissolve
        "Grab her head and make things rough!":
            $ roughbj = True
            hide blackopacity
            hide emeyecloseupnoheart
            hide embleye frown
            with dissolve
            pause 0.5
            play sound "audio/soundFX/Get.mp3"
            show embhands with dissolve
            with vpunch
            window show

            "I grip her head and hair with both hands, my cock throbbing eagerly in her mouth."
            "The thought of using the princess' pretty face for my own pleasure is just too much..."
            " Emelie blushes bright red, giving me an eager look."
            emelie " Mhmmm~ "
            "I pull back and push forth again."
            window hide
            show embdick wet1 with dissolve
            pause 0.7
            show embleye frown
            show embdick wet2
            with dissolve
            window show
            "This time as my cock hits the opening of her throat I steady my grip behind her head and keep her in place!"
            window hide
            show embdick dry3
            show embleye surprise
            with dissolve
            with vpunch
            show embwetmouth with dissolve
            window show
            emelie"Hlk!"

            "Emelie's eyes open wide as my cock forcefully pushes past the barrier to her throat!"
            with vpunch
            emelie " Unhhf! Gulk! "
            " She swallows around me, accepting my thick cock further down the tight opening."
            show embleye squint with dissolve
            emelie " Mhglk!"
            with vpunch
            " She gags around my cock as I hold her in place, closing her eyes and arching her back."
            show embleye close with dissolve
            " The sensation of her spasming throat squeezing the upper half of my cock makes me moan loudly."
            me " A-Ahhh, yes!"
            show embleye half with dissolve
            "I let her head go and pull back."
            window hide
            hide embhands with dissolve
            show embdick wet2 with dissolve
            pause 0.4
            show embdick wet1 with dissolve
            show emkneesbase
            show emk nees5
            with fade
            window show
            emelie " Puaaah!!"
            emelie " O-oh my god..."
            me " Sorry!"
            show emk nees6 with dissolve
            emelie " N-no I just..."
            " She clears her throat with a little cough."
            emelie "I really didn't think I would be able to take so much of it! "
            emelie "That was a lot..."
            me " Y-yeah It sure was."

            "As I breathe heavily her eyes stay fixed on my cock twitching in front of her."
            show emk nees6b with dissolve
            emelie " But you really loved that, didn't you? "
            emelie "I've never seen you... twitch like this before."
            "Precum and saliva drips down over her panting face."
            me " You really stimulated all of it at once..."
            me " And that tight grip felt so good."
            emelie " It felt really intense having you force that thick cock down my throat like that... "
            show emk nees6 with dissolve
            emelie "But I couldn't stop from choking and gagging."
            emelie " I'm a bit embarrassed making all those weird noises..."
            window hide
            menu:
                with dissolve


                "If you tap my leg when you feel overwhelmed I'll pull back & we can minimize that!":
                    window show
                    me  "If you tap my leg when you feel overwhelmed I'll pull back & we can minimize that!"
                    $ gagger = False

                    show emk nees6b with dissolve
                    emelie "That's a good idea!"
                    emelie " Just pull back when I tap your leg and give me a moment!"
                    me "Sure! And don't feel embarrassed about the sounds."
                    me "You're doing great!"
                    emelie "You too! I like hearing you moan as you use my mouth~"
                    emelie " I think I'm ready for some more!"
                    window hide
                    hide emkneesbase
                    hide emk
                    hide embleye
                    with fade
                    pause 0.3
                    show embhands
                    show embdick wet2
                    show embleye frown
                    show embspithang
                    with dissolve
                    window show
                    emelie " Mmhhh!"
                    "I hit a stop at the barrier to her throat once again, slowing down slightly and giving her a chance to tap my leg if needed."
                    emelie " Mmmmhh~"
                    " She takes a moment to collect herself and relaxes."
                    show embdick wet3
                    show embleye surprise
                    with dissolve
                    with hpunch
                    "I slowly push my cock down her throat again!"
                    show embleye close with dissolve
                    emelie " MMhh!"
                    "Her wet throat feels amazing as it accepts me again!"
                    show embleye half with dissolve
                    " It's so warm and tight, almost like it's hugging me."
                    " I feel Emelie increase the suction with her cheeks closing in tighter around me too!"
                    show embcheek with dissolve
                    "She's just so eager to please!"
                    "She looks up at me and taps my leg!"
                    window hide
                    play sound "audio/soundFX/Get.mp3"
                    show embhands with dissolve
                    with vpunch

                    show embdick wet2

                    with dissolve
                    pause 0.4
                    show embdick wet1
                    show embleye close
                    with dissolve
                    window show
                    " I swiftly let go of her head and move back."

                    "She pulls off."
                    window hide
                    show emkneesbase
                    show emk nees5
                    with fade
                    pause 0.4
                    window show
                    emelie " Phaaah!!"
                    show emk nees6 with dissolve
                    emelie " I did it again! And I was able to hold it there for quite a while without choking or anything!"
                    me " You're improving so quickly!"
                    show emk nees6b with dissolve
                    emelie " You proud of me?~"
                    me " Very proud, princess!"
                    emelie " Hihi!"
                    emelie " I need a second before I go deep again..."
                    me " Of course!"
                    show emk nees6 with dissolve
                    emelie " But I still want to use my mouth on something~"
                    window hide
                    menu:
                        with dissolve
                        "Suck on my balls again!":
                            window show
                            me "Suck on my balls again!"
                            show emk nees6b with dissolve

                            emelie " Gladly~"
                            window hide
                            show emballsuckwet with fade
                            pause 0.3
                            window show
                            " She slowly starts sucking on my balls once again."
                            " This time with my drooled-over shaft twitching right above her"
                            emelie " Mmmhhwbw I love these~"
                            me " You're such a messy girl."
                            emelie " I can't help it! My mouth starts watering just looking at this big cock~"
                            emelie " And I'd say we're both responsible for this mess."
                            me " You're right... I did sort of help by grabbing your head."
                            emelie " Exactly! And I think I'm ready for more of that now-"
                            window hide

                        "Lick my cock again!":
                            window show
                            me "Lick my cock again!"
                            show emk nees6b with dissolve
                            emelie " Gladly~ "
                            window hide
                            show emsideliccawet with fade
                            pause 0.3
                            window show
                            " Emelie quickly starts licking the underside of my shaft again."
                            "Drops of her own spit landing on her face as my cock twitches in front of her."
                            emelie " Mhhh so messy now~"
                            me " You made that mess, you know."
                            emelie "I think we're both responsible for it!"
                            me " You're right... I did sort of help by grabbing your head."
                            emelie " Exactly! And I think I'm ready for more of that now-"
                            window hide


                    scene embleej

                    show embdick wet1
                    with fade
                    pause 0.3
                    window show
                    " She takes my cock back in her mouth!"
                    emelie " Mmhhh~"
                    " She's asking for something..."
                    window hide
                    play sound "audio/soundFX/Get.mp3"
                    show embhands with dissolve
                    with vpunch
                    pause 0.5

                    show blackopacity
                    show emeyecloseuphearthapi
                    with dissolve
                    pause 0.2
                    window show
                    emelie " HmmHmm~"
                    " Her eyes light up as my hands grip her head again."
                    " She takes a deep breath with her nose and gives me a little nod."
                    window hide
                    hide blackopacity
                    hide emeyecloseuphearthapi
                    with dissolve
                    pause 0.2
                    window show
                    me " I'll take it slow and steady just like before..."
                    me " Just tap my leg and I'll let go!"
                    emelie " Mmmmhhh~"
                    " She seems incredibly eager and confident this time..."
                    window hide



                    show embdick wet2 with dissolve
                    show embleye half

                    with dissolve
                    pause 0.7
                    show embleye close
                    show embdick wet3
                    with dissolve
                    window show
                    " My cock slips down her throat with relative ease!"
                    " I still had give it a bit of a push but when my tip hit her soft palate she immediately started swallowing to take it deeper! "
                    " Her technique seems to be improving with every thrust!"

                    " Maybe I can push that final half-inch down too..."
                    " She really seems to want it!"
                    " I take a firmer grip of her hair and pull her towards me-"
                    #DEEPERFUCK-----------------------
                    window hide
                    scene emdeepbase
                    show blackshake at truecenter behind emdeepbase
                    show emdeepclosed

                    show emdeep hands1
                    with fade
                    window show

                    me " GAhh!"
                    " I can't help but moan loudly as I push that final length down her throat, her soft lips kissing my pubes."

                    hide emdeepclosed
                    with dissolve
                    " She looks up at me with lidded eyes."
                    me " Y-You did it! Ahh~"
                    window hide

                    show emdeeptongue with dissolve
                    pause 0.5
                    window show

                    "Emelie lets her tongue out and starts eagerly licking my balls."
                    me "GaaAaah!"
                    me " Now you're really outdoing yourself, princess!"
                    " That feels too good! My entire member is inside her! "
                    window hide
                    show emdeeper behind emdeepmascara
                    show emdeep hands2
                    with dissolve
                    pause 0.1
                    window show
                    "I rock my hips back and forth slightly, pressing the front of my pelvis against her."
                    with vpunch
                    emelie "Mphh!"
                    "My cock is massaged by her throat and the feeling of her lips kissing my pelvis as she circles my balls with her tongue drives me crazy!"
                    " She isn't showing any sign of tapping my leg, so I'll just..."
                    window hide
                    hide emdeeper
                    show emdeep hands1
                    with dissolve
                    pause 0.6
                    show emdeeper
                    show emdeep hands2
                    with dissolve
                    pause 0.6
                    hide emdeeper
                    show emdeep hands1
                    show emdeepclosed
                    with dissolve
                    pause 0.6
                    show emdeeper behind emdeepclosed
                    show emdeep hands2
                    show emdeepclosed
                    with dissolve
                    window show
                    me " Ahhh!"
                    "Grinding against her face with my cock deep in her throat sends me over the edge!"
                    me " I- I'm gonna cum!"
                    emelie " Hmmhhgn!"
                    " Emelie continues eagerly slurping around my balls, her tongue begging me to cum!"
                    " I can't make a mess and cum over her face out in public like this!"
                    " I've got to find another solution!"
                    window hide
                    menu:
                        with dissolve
                        "Pull out slightly and fill mouth with cum! ":
                            show embleej
                            show embleye surprise
                            show embleejcum
                            with fade
                            pause 0.3
                            window show
                            me " Aaahh!"
                            " My tip gets a final squeeze from Emelie's throat as I pull back!"
                            " My cock tenses hard and a large load of cum steadily fills her mouth and cheeks!"
                            emelie " Hmmpb!"
                            me " A-Almost there!"
                            " My orgasm slowly comes to an end and I let go of her head."
                            show black with dissolve
                            "Emelie pulls back, panting and steadying herself on the ground."

                            jump cummouth

                        with dissolve
                        "Keep her down and cum in throat! ":
                            window show
                            me " Aaahh!"
                            window hide
                            show white with dissolve
                            show emthroatcum behind white
                            if gagger == True:
                                show emthroatcumscara behind white
                            hide white with dissolve
                            pause 0.5
                            window show

                            " My cock tenses hard and I unload several thick ropes of my cum directly down her stomach!"
                            with hpunch
                            " She grabs my leg without tapping it, clearly trying to last until I've emptied my entire load!"
                            emelie " G-Ghh!"
                            me " O-One m-more second!"
                            "Emelie's warm throat gives me a final tight squeeze, almost as to milk me from the last of my cum."
                            " I moan out loudly with complete disregard for the fact that we're out in public!"
                            " My orgasm slowly comes to an end and I let go of her head."
                            window hide
                            hide emthroatcum
                            hide emthroatcumscara
                            show emdeepcum
                            with fade
                            hide emdeep hands2 with dissolve
                            pause 0.2
                            window show
                            "I feel my warm, thick cum slowly start to gush down my base and balls."

                            " Emelie makes sure to swallow a couple of final times with her lips pressed firmly around the base of my cock."
                            window hide
                            show black with dissolve
                            window show
                            "She pulls back, gasping loudly and steadying herself on the ground."
                            jump cumthroat
                "I thought it was really hot... I want feel you gag on my cock again.":
                    window show
                    me "I thought it was really hot... I want to feel you gag on my cock again."
                    $ gagger = True
                    show emk nees6b with dissolve
                    emelie " You're so dirty!"
                    emelie " And I like that..."
                    emelie " It feels really... exciting... "
                    emelie "Submitting to your naughty desires."
                    me " You're a naughty piggy too~"
                    me "That extra squeeze when you gag feels so good. "
                    emelie "...Mmmmhh."
                    emelie " Then give it to me again~"
                    window hide
                    hide emkneesbase
                    hide emk
                    hide embleye
                    with fade
                    pause 0.3
                    play sound "audio/soundFX/Get.mp3"
                    show embhands
                    show embdick wet2
                    show embleye frown
                    show embspithang
                    with dissolve
                    window show
                    emelie " Ghh!"
                    "I hit a stop at the barrier to her throat once again, feeling her body tense up."
                    emelie " Mhhhgl!"
                    show embdick wet3
                    show embleye surprise
                    with dissolve
                    with hpunch
                    "I force my cock down her throat once again!"
                    emelie " Gluk!"
                    show embleye squint

                    with dissolve
                    emelie " Hlk!"
                    show embleye close with dissolve
                    "Her wet, tight hole squeezes my shaft again and again!"
                    show embleye half with dissolve
                    " Her eyes start to tear up as she continues gagging around me, her mascara starting to trail down her cheeks."
                    show embleejmascara with dissolve
                    " I feel her increasing her suction with her cheeks closing in tighter around me too!"
                    show embcheek with dissolve
                    "She's just so eager to please!"
                    "I can't bring myself to stop!"
                    window hide
                    show embdick wet2

                    with dissolve
                    pause 0.6
                    hide embcheek
                    show embdick wet3
                    show embleye surprise
                    with dissolve
                    pause 0.6
                    show embcheek
                    show embleye squint
                    show embdick wet2
                    with dissolve
                    pause 0.6
                    show embdick wet1
                    show embleye close
                    with dissolve
                    window show

                    "As I pull my cock back a bit I can hear her starting to inhale through her nose."
                    window hide
                    show embleye half with dissolve
                    pause 0.2
                    show embleye frown with dissolve
                    pause 0.2


                    show blackopacity
                    show emeyecloseupheart
                    with dissolve
                    window show
                    emelie " Hhhhnnn!"
                    me " That's it, princess!"
                    me " Breathe in deep and get ready for more."
                    " She nods with my tip resting on her tongue just behind her lips and breathes in deeply through her nose."
                    window hide
                    hide blackopacity
                    hide emeyecloseupheart
                    with dissolve
                    pause 0.7
                    hide embcheek
                    show embdick wet2
                    with dissolve
                    pause 0.7
                    show embleye squint behind embleejmascara
                    show embdick wet3
                    with dissolve
                    window show
                    " She started swallowing hard the moment my cock bumps against the barrier to her throat."
                    " Her technique seems to be improving even if I'm still having to force it down!"

                    " Maybe I can push that final half-inch down too..."
                    " I take a firmer grip of her hair and pull her towards me-"
                    #DEEPERFUCK-----------------------
                    window hide
                    scene emdeepbase
                    show blackshake at truecenter behind emdeepbase
                    show emdeepclosedtears

                    show emdeep hands1
                    with fade
                    window show

                    me " GAhh!"
                    " I can't help but moan loudly as I push that final length down her throat, her soft lips kissing my pubes."
                    hide emdeepclosedtears
                    show emdeepmascara
                    with dissolve
                    " She looks up at me with lidded eyes."
                    me " Y-You did it! Ahh~"
                    window hide

                    show emdeeptongue behind emdeepmascara with dissolve
                    pause 0.5
                    window show

                    "Emelie lets her tongue out and starts eagerly licking my balls."
                    me "GaaAaah!"
                    me " Now you're really outdoing yourself, princess!"

                    " That feels too good! My entire cock is inside her! "
                    show emdeeper behind emdeepmascara
                    show emdeep hands2
                    with dissolve
                    "I rock my hips back and forth slightly, grinding the front of my pelvis against her."
                    with vpunch
                    emelie " Hlgk!"

                    "My cock is massaged by her flexing throat and the feeling of her lips kissing my pelvis as she circles my balls with her tongue is out of this world!"
                    window hide
                    hide emdeeper
                    show emdeep hands1
                    with dissolve
                    pause 0.6
                    show emdeeper behind emdeepmascara
                    show emdeep hands2
                    with dissolve
                    pause 0.6
                    hide emdeeper
                    show emdeep hands1
                    show emdeepclosedtears
                    with dissolve
                    with vpunch

                    emelie " Ulgk! Hnlg!"
                    me " Mmhh yes, Emelie! I love it when your throat tightens just like that!"
                    " The feeling is so intense even when she stops moving!"
                    with vpunch

                    emelie " Gurkl!"
                    "She gags around me again and again, always immediately following it by kissing my pelvis and circling her wet tongue around my balls."
                    "Those naughty sounds coupled with the intense sensations sends me over the edge!"


                    show emdeeper behind emdeepclosedtears
                    show emdeep hands2
                    show emdeepclosedtears
                    with dissolve
                    window show
                    me " I- I'm gonna cum!"
                    emelie " Hmmhhgn!"
                    " Emelie continues eagerly slurping around my balls, her tongue begging me to cum!"
                    " I can't make a mess and cum over her face out in public like this!"
                    " I've got to find another solution!"
                    window hide
                    menu:
                        with dissolve
                        "Pull out slightly and fill mouth with cum! ":
                            show embleej

                            show embleejcum

                            show embwetmouth
                            show embspithang
                            show embleye surprisetears
                            with fade
                            pause 0.3
                            window show
                            me " Aaahh!"
                            " My tip gets a final squeeze from Emelie's throat as I pull back!"
                            " My cock tenses hard and a large load of cum steadily fills her mouth and cheeks!"
                            emelie " Hmmpb!"
                            me " A-Almost there!"
                            " My orgasm slowly comes to an end and I let go of her head."
                            window hide
                            show black with dissolve
                            "Emelie pulls back, panting and steadying herself on the ground."

                            jump cummouth

                        with dissolve
                        "Keep her down and cum in throat! ":
                            window show
                            me " Aaahh!"
                            window hide
                            show white with dissolve
                            show emthroatcum behind white
                            if gagger == True:
                                show emthroatcumscara behind white
                            hide white with dissolve
                            pause 0.5
                            window show

                            " My cock tenses hard and I unload several thick ropes of my cum directly down her stomach!"
                            with hpunch
                            emelie " Ghhhlr!"
                            me " O-One m-more second!"
                            "Emelie's warm throat gives me a final tight squeeze, almost as to milk me from the last of my cum."
                            " I moan out loudly with complete disregard for the fact that we're out in public!"
                            " My orgasm slowly comes to an end and I let go of her head."
                            hide emthroatcum
                            hide emthroatcumscara
                            show emdeepcum
                            with fade
                            hide emdeep hands2 with dissolve
                            "I feel my warm, thick cum slowly start to gush down my base and balls."

                            " Emelie makes sure to swallow a couple of final times with her lips pressed firmly around the base of my cock."
                            window hide
                            show black with dissolve
                            "She pulls back, gasping loudly and steadying herself on the ground."
                            jump cumthroat
        "Let her be in comfortable control of the pace while encouraging her!":
            me " You're doing great, Emelie!"
            window hide
            $ roughbj = False
            hide blackopacity
            hide emeyecloseupnoheart
            hide embleye frown
            with dissolve
            window show
            me  "That feels so good..."
            me " Just take your time!"


            " Emelie blushes bright red, giving me a small nod."
            emelie " Mhmmmmm~ "
            "She circles my tip with her tongue and my cock throbs eagerly in her mouth."
            "The sight of the princess sucking my cock in public like this is just so hot..."

            "I slowly start thrusting back and forth again."
            window hide
            show embdick wet1 with dissolve
            pause 0.7
            show embleye frown
            show embdick wet2
            with dissolve
            window show
            "This time as my cock hits the opening of her throat I slow down."
            " I feel her press forward once again."
            me " Try and relax those muscles and take it slow!"
            emelie " Mmhhh!"
            me " Swallow and open your throat as best as you can."
            window hide
            with vpunch

            show embdick dry3
            show embleye surprise
            with dissolve
            with vpunch
            show embwetmouth with dissolve
            window show
            emelie"Ghluk!"
            "Emelie's eyes open wide as my cock suddenly slides past the barrier to her throat!"
            show embleye squint with dissolve
            emelie " Mhgl!"
            with vpunch
            " She makes some weird noises around my cock, closing her eyes and arching her back."
            show embleye close with dissolve
            " The sensation of her spasming throat squeezing the upper half of my cock makes me moan loudly."
            me " A-Ahhh, yes!"
            show embleye half with dissolve
            "She starts moving back so I immediately pull out!"
            window hide

            show embdick wet2 with dissolve
            pause 0.4
            show embdick wet1 with dissolve
            show emkneesbase
            show emk nees5
            with fade
            window show
            emelie " Puaaaaaaaah!!"
            emelie " O-oh my god..."
            me " You did it!"
            show emk nees6 with dissolve
            emelie " I-I did!"
            " She clears her throat with a little cough."
            emelie "I really didn't think I would be able to take so much of it! "
            emelie "It seemed like it'd never go down..."
            show emk nees6b with dissolve

            emelie " But then when you told me to swallow it just slid right down!"

            me "I gave it a bit of a push too..."
            emelie " Y-yeah! Thanks~"
            "As I breathe heavily her eyes stay fixed on my cock twitching in front of her."
            emelie " And you really loved that, didn't you? "
            emelie "I've never seen you... twitch like this before."
            "Precum and saliva drips down on her panting face."
            me " You really stimulated all of it at once..."
            me " It felt amazing!"
            emelie " Want me to give it another go?"
            emelie "I wanna see if I have the technique down!"
            me " Yes please!"

            window hide
            hide emkneesbase
            hide emk
            hide embleye
            with fade
            pause 0.3
            show embdick wet2
            show embleye frown
            show embspithang
            with dissolve
            window show
            emelie " Mmmmmhh!"
            "I hit a stop at the barrier to her throat once again."
            " She takes a moment to collect herself and relaxes."
            window hide
            show embdick wet3
            show embleye surprise
            with dissolve
            with hpunch
            window show
            "Swallowing me down again!"
            show embleye close with dissolve
            emelie " MMhh!"
            me "Ahhh, that feels amazing!"
            show embleye half with dissolve
            " It's so warm and tight, it almost feels like it's hugging me."
            " I feel Emelie suck her cheeks in tighter around me too!"
            show embcheek with dissolve
            "She's just so eager to please!"
            window hide

            show embdick wet2

            with dissolve
            pause 0.6
            show embdick wet1
            show embleye close
            with dissolve
            window show

            "She pulls off."
            window hide
            show emkneesbase
            show emk nees5
            with fade
            pause 0.3
            window show
            emelie " Phaaah!!"
            show emk nees6 with dissolve
            emelie " I did it again! And I was able to hold it there for quite a while without choking or anything!"
            me " You're improving so quickly!"
            show emk nees6b with dissolve
            emelie " You proud of me?~"
            me " Very proud, princess!"
            emelie " Hihi!"
            emelie " I need a second before I go deep again..."
            me " Of course!"
            show emk nees6 with dissolve
            emelie " But I still want to use my mouth on something~"
            window hide
            menu:
                with dissolve
                "Suck on my balls again!":
                    window show
                    me "Suck on my balls again!"
                    show emk nees6b with dissolve

                    emelie " Gladly~"
                    window hide
                    show emballsuckwet with fade
                    pause 0.3
                    window show
                    " She slowly starts sucking on my balls once again."
                    " This time with my drooled-over shaft twitching right above her"
                    emelie " Mmmhhwbw I love these~"
                    me " You're such a messy girl."
                    emelie " I can't help it! My mouth starts watering just looking at this big cock~"
                    emelie " And I'd say we're both responsible for this mess."
                    me " I guess I did sort of help with the instructions and thrusting forward."
                    emelie " Exactly! And I think I'm ready for more of that now-"
                    window hide

                "Lick my cock again!":
                    window show
                    me "Lick my cock again!"
                    show emk nees6b with dissolve
                    emelie " Gladly~ "
                    window hide
                    show emsideliccawet with fade
                    pause 0.3
                    window show
                    " Emelie quickly starts licking the underside of my shaft again."
                    "Drops of her own spit landing on her face as my cock twitches in front of her."
                    emelie " Mhhh so messy now~"
                    me " You made that mess, you know."
                    emelie "I think we're both responsible for it!"
                    me " I guess I did sort of help with the instructions and thrusting forward."
                    emelie " Exactly! And I think I'm ready for more of that now-"
                    window hide


            scene embleej

            show embdick wet1
            show embspithang
            with fade
            pause 0.2
            window show
            " She takes my cock back in her mouth!"
            emelie " Mmhhh~"
            window hide

            show blackopacity
            show emeyecloseuphearthapi
            with dissolve
            window show
            emelie " HmmHmm~"
            " She takes a deep breath with her nose."
            " Her eyes suddenly so full of desire and confidence."
            window hide
            hide blackopacity
            hide emeyecloseuphearthapi
            with dissolve
            pause 0.2
            window show
            me " I'll push on slow and steady just like before."
            me " And if you want to you take it down your throat... "
            me " I'll give it a little push when I feel you swallow!"
            emelie " Mmmmhhh~"
            " She seems incredibly eager and confident this time!"
            window hide


            show embdick wet2
            show embleye frown
            with dissolve
            pause 0.4
            show embleye half
            with dissolve
            pause 0.7
            show embcheek
            show embleye half
            show embdick wet1
            with dissolve
            pause 0.7
            hide embcheek
            show embleye half
            show embdick wet2
            with dissolve
            pause 0.7
            show embcheek
            show embleye half
            show embdick wet1
            with dissolve
            pause 0.7
            hide embcheek
            show embleye half
            show embdick wet2
            with dissolve
            pause 0.7
            show embleye squint
            show embdick wet3
            show embwetmouth
            with dissolve
            window show
            " My cock slips down her throat again with relative ease!"
            " Her technique seems to be improving quickly!"
            me " Ahh! Your throat feels so good!"
            me " I love when you take it deep-"

            #DEEPERFUCK-----------------------
            window hide
            scene emdeepbase
            show blackshake at truecenter behind emdeepbase
            show emdeepclosed

            with fade
            window show

            me " GAhh!"
            " She took that last half-inch down too!"
            " I can't help but moan loudly as those soft lips start kissing my pubes."

            hide emdeepclosed
            with dissolve
            " She looks up at me with lidded eyes."
            me " Y-You really took every last inch! Ahh~"
            window hide

            show emdeeptongue with dissolve
            pause 0.5
            window show
            "Emelie lets her tongue out and starts eagerly licking my balls."
            me "GaaAaah!"
            me " Now you're really outdoing yourself, princess!"
            " That feels too good! My entire member is inside her! "
            show emdeeper

            with dissolve
            "I rock my hips back and forth slightly, pressing the front of my pelvis against her."
            with vpunch
            emelie "Mphh!"
            "My cock is massaged by her throat and the feeling of her lips kissing my pelvis as she circles my balls with her tongue drives me crazy!"
            " She isn't showing any sign of stopping, so I'll just..."
            window hide
            hide emdeeper

            with dissolve
            pause 0.6
            show emdeeper

            with dissolve
            pause 0.6
            hide emdeeper

            show emdeepclosed
            with dissolve
            pause 0.6
            show emdeeper behind emdeepclosed

            show emdeepclosed
            with dissolve
            window show
            me " Ahhh!"
            "Grinding against her face with my cock deep in her throat sends me over the edge!"
            me " I- I'm gonna cum!"
            emelie " Hmmhhgn!"
            " Emelie continues eagerly slurping around my balls, her tongue begging me to cum!"
            " I can't make a mess and cum over her face out in public like this!"
            " I've got to find another solution!"
            window hide
            menu:
                with dissolve
                "Pull out slightly and fill her mouth with cum! ":
                    show embleej
                    show embleye surprise
                    show embleejcum
                    with fade
                    pause 0.3
                    window show
                    me " Aaahh!"
                    " My tip gets a final squeeze from Emelie's throat as I pull back!"
                    " My cock tenses hard and a large load of cum steadily fills her mouth and cheeks!"
                    emelie " Hmmpb!"
                    me " A-Almost there!"
                    " My orgasm slowly comes to an end and I let go of her head."
                    window hide
                    show black with dissolve
                    window show
                    "Emelie pulls back, panting and steadying herself on the ground."

                    jump cummouth

                with dissolve
                "Cum down her throat! ":


                    show white with dissolve
                    show emthroatcum behind white
                    hide white with dissolve
                    pause 0.4
                    window show

                    " My cock tenses hard and I unload several thick ropes of my cum directly down her stomach!"
                    me " A-Aahhh!"
                    " She grabs my legs to keep herself down on my cock, clearly trying to last until I've emptied my entire load!"
                    with vpunch
                    emelie " G-Ghlk!"
                    me " O-One m-more second!"
                    "Emelie's warm throat squeezes my cock as she gags on it, almost like it's milking me from the last of my cum!"
                    with vpunch
                    emelie " Hlgk!"
                    " I moan out loudly with complete disregard for the fact that we're out in public!"
                    " My orgasm slowly comes to an end with Emelie letting go of my shaking legs."
                    window hide
                    hide emthroatcum
                    show emdeepcum
                    with fade
                    hide emdeep hands2 with dissolve
                    pause 0.2
                    window show
                    "I feel my warm, thick cum slowly start to gush down my base and balls."

                    " Emelie makes sure to swallow a couple of final times with her lips pressed firmly around the base of my cock."
                    window hide
                    show black with dissolve
                    "She pulls back, gasping loudly and steadying herself on the ground."

                    jump cumthroat

label cummouth:

    # mouthful
    window hide
    scene mouthful base

    show mouthfu full
    show mouthfulbrow down
    show mouthfulsidecum
    if roughbj == True:
        if gagger == True:
            show mouthfulfilth
        if gagger == False:
            show mouthfulfilth2
    with fade
    pause 0.4
    window show
    if roughbj == True:

        window show

        "... Seems going so rough left a stray pubic hair on her face."
        if gagger == True:
            " As well as some smeared mascara under her eyes and some messiness from her nose..."
        if gagger == False:
            " As well as some messiness from her nose..."
        "Should I clean her up a little?"
        window hide
        menu:
            with dissolve
            "Clean her up a little! That's not a good look on a princess! ":
                play sound "audio/soundFX/Get.mp3"
                hide mouthfulfilth
                hide mouthfulfilth2
                with dissolve

                pause 0.7
                window show

                " There we go..."

            "Leave the stray hair and nose untouched! I like the messy look... ":
                window show
                " I'll leave her as is."
    "She tries her best to keep her head upward so as not to spill."
    me " Fff I'm sorry for getting so much on you!"
    "She slowly starts swallowing my big load down."
    window hide
    hide mouthfulsidecum
    show mouthfu fullhalf
    show mouthfulsidecum2
    with dissolve
    pause 0.9


    show mouthfu half
    with dissolve
    pause 0.9
    show mouthfu little with dissolve
    pause 0.9
    show mouthfu openn with dissolve
    window show
    emelie " Aaaaaaahh~ "
    " She looks really proud of finally getting it all down."
    hide mouthfu
    hide mouthfulsidecum2
    show mouthfulbrow up
    with dissolve
    emelie " Puh..."
    emelie" T-That was a lot..."
    " I sure came a lot... Maybe she wouldn't have had such a mouthful had I cum straight down her throat."
    window hide
    jump afterbeejay
label cumthroat:
    # mouthful
    window hide
    scene mouthful base
    show mouthfu little
    show mouthfulbrow down

    show mouthfulsidecum2
    if roughbj == True:
        if gagger == True:
            show mouthfulfilth
        if gagger == False:
            show mouthfulfilth2
    with fade
    window show
    if roughbj == True:

        "... Seems going so rough left a stray pubic hair on her face."
        if gagger == True:
            " As well as some smeared mascara under her eyes and some messiness from her nose..."
        if gagger == False:
            " As well as some messiness from her nose..."

        "Should I clean her up a little?"
        window hide
        menu:
            with dissolve
            "Clean her up a little! That's not a good look on a princess! ":
                play sound "audio/soundFX/Get.mp3"
                hide mouthfulfilth
                hide mouthfulfilth2
                with dissolve
                pause 0.7
                window show

                " There we go..."

            "Leave the stray hair and nose untouched! I like the messy look...  ":
                window show
                " I'll leave her as is."
    " She swallows what little cum is left."
    window hide
    show mouthfu openn
    show mouthfulbrow up
    with dissolve
    pause 0.2
    window show
    emelie " Aaaaaaahh~ "
    " She looks really proud finally getting it all down."
    window hide
    hide mouthfu
    hide mouthfulsidecum2
    with dissolve
    pause 0.2
    window show
    emelie " Puh..."
    emelie" T-That was a lot..."

    " If I didn't cum straight down her throat she'd probably have her whole mouth full..."
    window hide
    jump afterbeejay
label afterbeejay:
    stop music fadeout 1.0
    scene black with dissolve
    window show

    " I do my best to shake all that excess spit and cum off my cock, with Emelie moving in to lick the final bits off from around my base."
    " I pull my pants back on and we both take a moment to clean up. "
    $ unlock("S4")
    $ renpy.end_replay()
    play music "audio/Tavern+Brawl+-+320bit.mp3" fadein 0.1 volume 0.3
    window hide
    scene bg hedge with dissolve
    show emc normal at right:
        yalign 0.15
        zoom 1.0
    show emf full at right:
        yalign 0.15
        zoom 1.0
    show emugh at right:
        yalign 0.15
        zoom 1.0
    with dissolve
    pause 0.3
    window show
    emelie "Uuugh..."
    emelie "I'm so full now."
    me " Sorry!"
    me " I didn't want to make a big mess again now that we're so far from the baths!"
    hide emugh
    show emf wide
    show emc out
    with dissolve
    emelie " Good thinking, it sure complicated things yesterday!"
    window hide

    show blackopacity
    show clocktower
    with dissolve
    pause 0.3
    window show
    "Emelie looks up towards the nearest clocktower "
    emelie " Oh, it's a little past eleven o'clock!"
    emelie " I need to get going to my classes."
    emelie" Helga will kill me if I show up late again! "
    window hide

    hide blackopacity
    hide clocktower
    with dissolve
    show emf normalblush
    show emc proper
    with dissolve
    window show
    emelie " But this was a really fun date."
    show emeye close at right:
        yalign 0.15
        zoom 1.0
    with dissolve
    emelie " I've never been on one before!"
    "She gives me a big smile."
    me " The pleasure is all mine!"
    show emf bigsmile
    hide emeye
    with dissolve
    emelie " We had a meal and ended the whole thing with a kiss!"
    me " I don't think most people call what we just did a kiss-"
    show emc think

    show emf think
    with dissolve
    emelie "Hmm maybe not! "
    show emeye normal at right:
        yalign 0.15
        zoom 1.0
    with dissolve
    emelie "But it isn't too different."
    hide emeye
    show emf bite
    show emc normal
    show emblush at right:
        yalign 0.15
        zoom 1.0
    with dissolve
    emelie "My lips touching you... "
    show emf smile
    show emc out
    with dissolve
    emelie "Just in a different place!"
    hide emf
    hide emc
    hide emblush
    show emcomp blushsmile at right:
        yalign 0.15 zoom 1.0

    with dissolve
    emelie "..."
    show emcomp blushsmile at right:
        yalign 0.15 zoom 1.0
        linear 0.2 yalign 0.14 xalign 0.8 zoom 1.05
    "She takes a step closer "
    emelie " Well then before I go..."
    window hide
    scene emeliehugkiss with fade
    show blackshake at truecenter behind emeliehugkiss
    play sound "audio/soundFX/Sit Pillow.wav"
    with vpunch
    pause 0.3
    window show
    "She lunges towards me!"
    emelie " I'll give ya a proper one!"
    window hide
    show emeliehugkiss2 with fade
    play sound "audio/soundFX/FX3/kiss.wav"
    with hpunch
    pause 0.3

    window show

    "SMOOCH!"
    "Her soft lips press into mine as she lands in my arms."
    "She feels so warm and soft, and those lips make my whole body tingle with warmth."
    "The feeling of them between my legs was incredible..."
    "But this kiss and embrace hits me in a completely different way."
    window hide
    show black with dissolve
    window show
    " I close my eyes and cherish the moment."
    window hide

    scene bg hedge
    show emcomp blushsmile at right:
        yalign 0.14 xalign 0.8 zoom 1.05



    with fade

    show emcomp blushsmile at right:
        yalign 0.14 xalign 0.8 zoom 1.05

        linear 0.2 yalign 0.15 xalign 1.0 zoom 1.0
    window show
    emelie " There!"
    show blackshake at truecenter behind bg
    hide emcomp
    show emc out at right:
        yalign 0.15 zoom 1.0
    show emf smile at right:
        yalign 0.15 zoom 1.0
    with dissolve
    emelie "How's that for a kiss? "
    window hide
    menu:
        with dissolve
        "I'd love more of those! ":
            window show
            me"I'd love more of those!"
            show emc proper
            show emf bigsmile
            with dissolve
            emelie " Noted!"



        "I think I prefer the other kind. ":
            window show
            me " I think I prefer the other kind. "
            show emc hips
            show emf yeaa
            with dissolve

            emelie " Ha-ha... I'm sure you do!"
    show emc normal
    show emf normal
    with dissolve
    emelie " Anyways..."
    show emf pout with dissolve
    emelie " My classes should be done at around four or five!"
    show emf sooth
    show emc proper
    with dissolve
    emelie "You can come meet me in my room just after!"
    show emf smile with dissolve
    emelie "Billy can take you there if you run into him!"
    show emf bigsmile with dissolve
    emelie "Or just talk to Lars! "
    me " Okay! Good luck with your studies!"
    emelie "Thank you!"
    emelie "And have fun in Hog Haven!"
    play sound "audio/soundFX/run2.wav"
    hide emc
    hide emf
    with easeoutright
    " I watch as Emelie skips away. "
    " She's just great..."
    window hide
    stop music fadeout 1.0
    with hpunch
    play sound "audio/soundFX/FX3/rustle.wav"
    pause 0.5
    window show
    "Hmm?!"

    "The bushes rattle behind me! "

    "I turn around quickly!"
    window hide
    with vpunch
    play sound "audio/soundFX/FX3/shaken-bush.wav"
    pause 0.6
    with hpunch

    play sound "audio/soundFX/FX3/bushhit.wav"
    pause 0.5
    play sound "audio/soundFX/FX3/trip-on.wav" volume 0.65
    show blackopacity
    show billyfall
    with dissolve
    with vpunch
    pause 0.3
    window show




    " Billy crashes through the hedge!"
    play music "audio/adventures-in-adventureland-by-kevin-macleod-from-filmmusic-io.mp3" fadein 0.1 volume 0.4
    billy " Owww!!"
    "Billy stumbles for a moment before standing up"
    window hide
    hide blackopacity
    hide billyfall
    with dissolve
    show billy scratchy at left with dissolve:
        yalign 0.4 xalign -0.08
    window show
    billy "That hurt."
    show billy wary with dissolve
    billy " Sorry if I scared ya, buddy!"
    show billy belly with dissolve
    billy " Now I've got to come clean with something..."
    show billy ooo
    show billyblush at left:
        yalign 0.4 xalign -0.08
    with dissolve
    billy " I saw you and Emelie!"
    " Oh no!"
    me "... What do you mean?"
    show billy casual
    hide billyblush
    with dissolve
    billy " Well, I was rummaging around the bushes for some berries! "
    show billy laugh with dissolve
    billy " They're just perfect this time of the year!"
    me"..."
    show billy ooo with dissolve
    billy " Anyways, I heard some strange slurpy sounds so I made my way here!"
    show billy bellyhapi with dissolve
    billy " It kept going for a long time, and it sounded like you were having a really good time!"
    billy " I could've gotten here faster but... there were a lot of berries to eat on the way."
    show billy wary with dissolve
    billy "But then I heard some really desperate sounds... "
    billy "Almost like someone was choking on something!"
    " Shit!"
    show billy clench with dissolve
    billy "So I hurried up a bit-"
    show billy bellyhapi with dissolve
    billy " But then I saw you and Emelie!"
    "!!!"
    show billy laugh with dissolve
    billy " Hugging!"
    show billybigblush at left:
        yalign 0.4 xalign -0.08

    with dissolve
    with hpunch
    billy " And kissing!!"
    me " A-ahh!"
    " Puh! Seems he missed the other part!"
    " But how do I explain the kiss?!"
    me " I- I know I shouldn't have but--"
    show billy clench
    show bill squint at left behind billybigblush:
        yalign 0.4 xalign -0.08
    with dissolve
    billy  " I'm so happy for you two!!"
    me "?"
    show bill hearteyes with dissolve
    billy " Summer love!"
    billy " Blooming like the most beautiful flower!"
    me " You're... not mad?"
    show billy wary
    show bill embarassface
    hide billybigblush
    with dissolve
    billy " Why would I be mad!? "
    show billy laugh
    hide bill
    show billyblush at left:
        yalign 0.4 xalign -0.08
    with dissolve
    billy "You and Emelie are both so sweet! "
    billy "You sure deserve each other!"
    " I don't know why I expected Billy to react differently..."
    " A peasant like me kissing the crown princess is something most people would sneer at..."
    " But Billy doesn't seem to think like that!"
    me " Thank you, Billy! "
    me "I'm happy you're so ... accepting!"
    hide bill
    hide billyblush
    show billy casualaugh
    with dissolve
    billy " Of course! "
    billy "You're my best bud! "
    me " That said I think it's probably best if you don't tell anyone."
    show billy wary with dissolve
    billy " Why is that?"
    billy " Oh... wait... "
    billy "You're right."
    show billy ooo with dissolve
    billy " My uncle almost killed you yesterday for just being in the same room as her!"
    show billy laugh with dissolve
    billy " I'll keep my mouth closed as far as your little romance is concerned!"
    me " You're the best!"

    show billy scratchy with dissolve
    "Billy starts scratching his butt."
    billy " Hold on something's bugging me."
    me " What?"

    billy " Feel like I've got a rock or something stuck up in my armor!"
    "Suddenly something thuds onto the ground!"
    window hide

    show blackopacity
    show dent
    with dissolve
    play sound "audio/soundFX/poke_1.wav"
    with vpunch
    window show
    " Woah!"


    "That's the gold heart from Emelie's dress!"
    me " I think that thing is Emelie's! "
    me "She dropped it from her window yesterday!"
    billy " O-Oh?? "
    billy "I started my berry-eating journey in the hedges right below her window! "
    billy " It must've got lodged in between my armor plates!"
    me "Hmm, it looks a little dented."
    " I pick it up."
    window hide
    play sound "audio/soundFX/Get.mp3"
    hide blackopacity
    hide dent
    with dissolve
    show billy finger with dissolve
    window show
    billy " That's nothing the good ol' smith can't fix! "
    show billy casual with dissolve
    billy " Fixed my own helmet right up yesterday, remember? "
    show billy casualaugh with dissolve
    billy "This is nothing compared to that!"
    billy " I'll show you the way! We'll get there by carrying on through the park!"
    window hide
    scene bg tailorsmith
    with fade
    pause 0.4
    window show
    " I follow Billy and we come to a stop right by a small bridge."
    window hide
    show billy base at left:
        yalign 0.4 xalign -0.08
    with easeinleft
    window show
    billy " This is a great place if you need to buy tools or some clothes! "
    show billy finger with dissolve
    billy "Got a tailor right by the smithy!"
    show billy bellyhapi with dissolve
    window hide

    show billy bellyhapi at left:
        yalign 0.4 xalign -0.08
        linear 0.2 yalign -0.5 xalign -0.9 zoom 1.0
    pause 0.4
    window show
    billy " See that building with the anvil-shaped chimney?"
    billy " That's where you're goin'!"
    show billy bellyhapi at left:
        yalign -0.5 xalign -0.9 zoom 1.0
        linear 0.2 yalign 0.4 xalign -0.08
    show billy bellyhapi with dissolve
    billy " I think I'll wait for ya in the park while you get things sorted! "
    show billy wary with dissolve
    billy "I don't really like how stuffy the air gets in there... Especially when wearing this helmet!"
    me " Okay, Billy! "
    me "But I don't have any money to pay for the service."
    show billy base with dissolve
    billy " Don't worry!"
    show billy finger with dissolve
    billy " You're a royal assistant! "
    billy "You can pay later!"
    me " Really?"
    show billy casualaugh with dissolve
    billy " Absolutely! Now see ya in a bit!"
    me " Okay, see ya soon! "
    window hide
    play sound "audio/soundFX/run2.wav"
    hide billy with easeoutleft
    pause 0.3
    window show
    "Billy wiggles back to the park."
    "Hmm..."
    "I'm a little nervous going at this alone, but so far all the shop owners I've met have been super pleasant!"
    stop music fadeout 1.0

    jump Smithy



label Smithy:
    $ bronwen_name = "???"
    window hide
    scene black with fade

    window show
    play sound "audio/soundFX/FX3/hammer-on-anvil.wav" volume 1.0
    "I walk into the door and am immediately hit by the warm, dense air."

    "The sound of metal clanging against an anvil suddenly stops and the air clears."

    window hide
    play music "audio/Blacksmith+-+320bit.mp3" fadein 1.0 volume 0.4
    scene bg smithy
    show blackshake at truecenter behind bg
    show smithysmoke
    show bronwen hammer at left:
        yalign -0.0 xalign 1.3
        zoom 0.9
    show bronwenshadow at left:
        yalign -0.0 xalign 1.3
        zoom 0.9
    show bronshadyangrier at left:
        yalign -0.0 xalign 1.3
        zoom 0.9
    show bronwenmegashady at left:
        yalign -0.0 xalign 1.3
        zoom 0.9

    show smithyanvil
    show anvilsword
    with fade
    pause 0.4
    hide bronwenmegashady

    with dissolve
    window show
    bron " What?!"
    "!!"
    me "H-hello!"
    "An intimidating figure stares me down!"
    show bronwen hammerhip
    hide bronshadyangrier
    show bron questioning behind bronshady at left:
        yalign -0.0 xalign 1.3
        zoom 0.9
    show bronshady at left:
        yalign -0.0 xalign 1.3
        zoom 0.9
    with dissolve
    bron " ..."
    window hide
    menu:
        with dissolve
        "...":
            window show
            me " ..."



        "?!?!":
            window show
            me "?!?!"
    show bronwen knuckles
    show bronshadyangrier at left:
        yalign -0.0 xalign 1.3
        zoom 0.9


    with dissolve
    bron " Start talking if you're here for something or get lost! "
    show bron baseface with dissolve
    bron "I'm working!"

    me " I... uuuh... "
    me "I'm the princess' new assistant and would like to fix a gold accessory up!"
    show bron pout
    hide bronshadyangrier
    show bronwen hammer
    with dissolve
    bron " Good joke. Now get lost. "
    me " No really, I am!"
    show bronwen raised
    show bronshadyangrier at left:
        yalign -0.0 xalign 1.3
        zoom 0.9
    show bron rageface
    with dissolve
    bron " I said get lost!"
    " She raises her hammer!"
    window hide
    stop music fadeout 0.3
    pause 0.2

    play sound "audio/soundFX/FX2/church-bell-fischerhude-short.wav"
    with vpunch
    window show
    "The bell is heard!"
    hide bronshadyangrier
    show bron pout
    with dissolve
    bron "..."
    play music "audio/Tavern+Brawl+-+320bit.mp3" fadein 1.0 volume 0.3
    show bronwen hammer
    hide bronshady

    with dissolve
    " Her disposition changes completely at the sound of the bells and she immediately looks more relaxed!"

    show bronwen finger
    hide bron
    show broneye squint at left:
        yalign -0.0 xalign 1.3
        zoom 0.9
    with dissolve
    bron " Or it seems we've got some time..."
    show bronwen hips
    show bron pout at left:
        yalign -0.0 xalign 1.3
        zoom 0.9
    with dissolve
    bron " The name is Bronwen."
    $ bronwen_name = "Bronwen"
    me " I'm [Protagonist]!"
    show bron baseface2 at left:
        yalign -0.0 xalign 1.3
        zoom 0.9
    with dissolve
    bron " I can't be slacking off during my scheduled hours, so you gotta be snappy."
    me " Ahh... I'm sorry for disturbing."
    show bron smile with dissolve
    bron " Well, the bells ring at twelve... "
    bron "Which means I've got an hour's break!"
    show bron baseface
    show bronwen knuckles
    with dissolve
    bron " So... What's this tactic of yours? "

    bron " Pretending to be the \" princess' assistant \" so you can get a price cut or something?"
    show bron baseface2
    with dissolve
    bron " Humor me.  "
    me " I'm not lying! "
    me "I really am the princess' assistant."
    show bronwen base
    show bron done
    with dissolve
    bron "... And?"
    me " Well, I was told that meant I could delay my payment..."
    stop music fadeout 0.5

    with hpunch
    play sound "audio/soundFX/poke_1.wav" volume 1.0
    show bronshadyangrier at left:
        yalign -0.0 xalign 1.3
        zoom 0.9
    show bronwen knuckles
    with dissolve
    play music "audio/Blacksmith+-+320bit.mp3" fadein 1.0 volume 0.4
    bron " I KNEW IT!"
    show bron baseface with dissolve
    bron " Always some new ploy to get work for cheap!"
    show bronwen raised
    show bron rageface
    with dissolve
    bron " Now GET LOST!"
    "Shit!"
    " I'm gonna need to go grab Billy to clear this up!"
    window hide
    show rolf takeout at right:
        zoom 0.97 yalign 0.51 xalign 1.39
    show roleye lookside at right:
        zoom 0.97 yalign 0.51 xalign 1.39
    with easeinright
    play sound "audio/soundFX/FX3/braams.wav" volume 1.0
    with hpunch
    window show
    "!!!"
    " As if things weren't bad enough already!!"
    hide roleye with dissolve
    show rol rage at right:
        zoom 0.97 yalign 0.51 xalign 1.39
    with dissolve
    play sound "audio/soundFX/FX2/pig-scream-loud-oink.wav"
    with hpunch
    if perfscore ==True:
        rolf " Well if it isn't the \"perfect assistant\"?!"
    else:
        rolf " Well if it isn't the \" assistant\"?!"

    rolf " The hell are you doing here?!"
    hide bronshadyangrier


    show bronwen hammer
    show bron pout behind broneye
    show broneye squintside at left:
        yalign -0.0 xalign 1.3
        zoom 0.9
    with dissolve
    bron " Oh hey pops."
    "Pops?! Is this Rolf's daughter??"
    show bron surprise
    hide broneye lookright
    with dissolve

    bron " Wait-"
    bron "He's telling the truth about the whole assistant thing??"
    show roleye lookside at right:
        zoom 0.97 yalign 0.51 xalign 1.39
    show rol base
    with dissolve
    rolf " Apparently."


    if liename == False:
        show roleye looksidehapi at right:
            zoom 0.97 yalign 0.51 xalign 1.39

        show rol grin
        with dissolve

        rolf " This is that scrawny git I was tellin' ya about yesterday."
    if liename == True:
        rolf " This is that scrawny git I was tellin' ya about yesterday."
        show roleye looksidehapi at right:
            zoom 0.97 yalign 0.51 xalign 1.39

        show rol grin
        with dissolve
        rolf "\" [lie_name] \"."
    show bron laugh with dissolve
    bron " Hah, I thought you were just making shit up!"

    show bron hips
    show bron smilee
    show broneye squintside at left:
        yalign -0.0 xalign 1.3
        zoom 0.9
    with dissolve
    bron " So, pops. "
    bron "What'd ya get me today?"
    show rol smiley at right:
        zoom 0.97 yalign 0.51 xalign 1.39
    hide roleye
    with dissolve
    rolf " Well, you'll be happy to hear..."
    window hide
    play sound "audio/soundFX/Get.mp3"
    show anviltakeout
    show rolf base behind smithyanvil
    show roleye looksidehapi at right:
        zoom 0.97 yalign 0.51 xalign 1.39
    with dissolve
    pause 0.5
    window show
    rolf " Craburgers!!"
    rolf " Your favorite!"
    show bron biggersmile

    show bronwen hips
    show broneye lookdownside at left:
        yalign -0.0 xalign 1.3
        zoom 0.9
    with dissolve


    bron " Ooo!"

    show rolf fist
    show rol rage
    hide roleye

    with dissolve



    if liename == True:
        rolf " But now to deal with you, \" [lie_name] \"!"
    else:
        rolf " But now to deal with you, [Protagonist]!"
    window hide

    show interrosmith1 with fade
    play sound "audio/soundFX/Get.mp3"
    with hpunch
    hide broneye
    #^ Draw to match boafrontation colors a bit. Orange background and a bit more warm/dank colors.
    pause 0.3
    window show
    " He leaps forward and grabs me by the collar!"
    rolf " I've got some questions as to what exactly you're doing here!!"
    bron " HEY!!"
    window hide


    show interrosmith2 with dissolve
    play sound "audio/soundFX/Get.mp3"
    with hpunch
    stop music
    play sound "audio/soundFX/FX3/clean-record-scratch.wav" volume 1.0

    window show
    bron "I've told you COUNTLESS times!"
    "She pulls Rolf away from me!"

    window hide

    show boarfrontation at truecenter with fade

    window show
    "And presses her hammer against his face!"
    show boarfrontation at truecenter:
        zoom 1.0
        linear 0.2 yalign 0.1 xalign 0.1 zoom 1.03
    play sound "audio/soundFX/Dun.wav"volume 0.7
    with vpunch
    bron "{size=50}DON'T.{/size}"
    show boarfrontation at truecenter:
        zoom 1.03
        linear 0.2 yalign 0.0 xalign 0.0 zoom 1.06
    play sound "audio/soundFX/Dun.wav"volume 0.8
    with hpunch
    bron "{size=60}INTERROGATE.{/size}"
    show boarfrontation at truecenter:
        zoom 1.06
        linear 0.2 yalign -0.02 xalign 0.0 zoom 1.09
    play sound "audio/soundFX/Dun.wav"volume 0.9
    with vpunch
    bron "{size=70}MY.{/size}"
    show boarfrontation at truecenter:
        zoom 1.09
        linear 0.2 yalign -0.01 xalign 0.0 zoom 1.12
    play sound "audio/soundFX/Dun.wav" volume 1.0
    with hpunch
    bron "{size=80}CUSTOMERS!!!{/size}"
    "!!!"
    show boarfrontation at truecenter:
        zoom 1.12 yalign -0.01 xalign 0.0
        linear 0.2 yalign 0.1 xalign 0.1 zoom 1.0
    "She lets him go. "
    play sound "audio/soundFX/Get.mp3"
    window hide
    hide boarfrontation
    hide Interrogate
    hide interrosmith2
    hide interrosmith1
    hide rol
    show rolf sidewary at right:
        zoom 0.97 yalign 0.51 xalign 0.90
    show bronwen fist behind bron
    show bron meanface at left:
        yalign -0.0 xalign 1.3
        zoom 0.9
    show broneye squintside at left:
        yalign -0.0 xalign 1.3
        zoom 0.9

    with fade

    pause 0.3
    show rolf sidewary at right:
        zoom 0.97 yalign 0.51 xalign 0.90
        linear 0.5 zoom 0.97 yalign 0.51 xalign 1.39
    pause 0.3
    show bronwen hips behind bron with dissolve
    $ renpy.pause(0.8, hard=True)
    window show
    play music "audio/Birds.wav" fadein 2.0 volume 0.6

    rolf " B-But!"
    hide rolf
    show rolfcomp fine at right:
        zoom 0.97 yalign 0.51 xalign 1.39

    with dissolve


    rolf " ...Fine."


    show rol pout at right:
        zoom 0.97 yalign 0.51 xalign 1.39
    show roleye sidesad  at right:
        zoom 0.97 yalign 0.51 xalign 1.39
    with dissolve

    rolf " I'll be going then..."
    show bron cooldown
    hide broneye
    with dissolve
    " She takes a deep breath and calms down."
    show bron apologeticside
    show bronwen takeout
    hide anviltakeout
    with dissolve

    bron "Thanks for the food, dad."

    hide rolfcomp
    show rolf belly behind rol at right:
        zoom 0.97 yalign 0.51 xalign 1.39
    show rol smiley at right:
        zoom 0.97 yalign 0.51 xalign 1.39
    hide roleye
    with dissolve
    rolf " Well of course!"
    show bron laugh with dissolve
    bron "Have a great day!"

    show roleye looksidehapi at right:
        zoom 0.97 yalign 0.51 xalign 1.39
    with dissolve
    rolf " You too! "
    rolf "Byebye, dear!"
    " Rolf sounds so wholesome when talking to her."
    show roleye intense
    show rol pout
    show rolf knuckles
    with dissolve
    " But he makes sure to give me the stink eye before walking out the door."
    stop music fadeout 1.0
    hide rolf
    hide rol
    hide roleye
    with easeoutright
    play sound "audio/soundFX/Door Close 2.wav"


    bron "..."
    play music "audio/Tavern+Brawl+-+320bit.mp3" fadein 2.0 volume 0.4
    show bron done with dissolve
    bron " You have no idea how often he does that interrogation thing."
    me " Really?"
    me "Can't be good for business."
    show bron cooldown with dissolve
    bron " Definitely isn't. "
    show bron apologetic with dissolve
    bron " But I think he's just being overly protective..."
    bron " Every single day he grabs me dinner."
    " She puts the food down by the forge."
    window hide
    play sound "audio/soundFX/Get.mp3"
    show bronwen hips
    show bgsmithtakeout behind bronwen
    show bron baseface2
    with dissolve
    pause 0.3
    window show
    bron " I've told him not to... but he keeps doing it anyways."
    show bron pout with dissolve

    bron " So... You wanted some tweaks to a gold accessory was that it?"
    me " Yes!"

    "She removes the blade from her anvil."
    window hide

    hide anvilsword with dissolve
    pause 0.2
    window show
    " I put the golden heart in front of her."
    window hide

    play sound "audio/soundFX/FX3/anvil-hit.wav" volume 0.1
    show goldsmithanvil
    with dissolve
    pause 0.2
    show broneye lookdown at left:
        yalign -0.0 xalign 1.3
        zoom 0.9
    with dissolve
    pause 0.4
    window show

    me " Think you can fix this up?"


    window hide

    show bron questioning

    show bronwen base
    with dissolve
    pause 0.4
    window show
    bron " Well, what is it supposed to be?"
    bron " Some sort of dented ball thingy? "
    show bron pout
    hide broneye
    with dissolve
    bron " Can't shape it into something if I don't know what the end product is supposed to be..."
    "Wait..."
    "I could get her to reshape it into anything I want!"
    "Emelie mentioned she wanted one of those plugs made."
    " This is my opportunity to get her one!"
    "She'd surely be happier with that than just the pendant being returned!"
    me " Actually... "
    me "It's supposed to be this really different-looking shape..."
    me " Kinda like a cone but with a sort of...handle thingy at the bottom and a tapered off top."
    me "..."
    "Crap. I'm horrible at explaining this!"
    hide broneye
    show bronwen paperlook
    show bron done
    with dissolve
    bron " ... You gotta draw it out for me. Take this paper and some coal."
    me " S-sure."

    window hide
    show bronwen base with dissolve
    pause 0.4
    play sound "audio/soundFX/Get.mp3"
    show blackopacity
    show bronwpaper
    with dissolve
    pause 0.3
    window show

    bron " You can draw wherever there's space. "

    me " Did you draw this stuff?"
    bron " Yeah, why? "
    bron" Helps me remember what needs to be done. "
    me " You're pretty good at drawing. "
    me " Your dad is too!"
    hide blackopacity
    hide bronwpaper
    with dissolve
    show bron bigsmile with dissolve
    bron " He taught me."
    hide bron
    show bronwen finger
    with dissolve

    bron " Wait... "
    bron "How do you know he's good at drawing? "
    show bronwen knuckles
    show bron done at left:
        yalign -0.0 xalign 1.3
        zoom 0.9
    with dissolve
    bron " ..."
    bron " Don't answer that."
    show bron surprise with dissolve
    bron " He probably did his interrogation thing on you yesterday too, didn't he? "
    me " Yeaa."
    show bronwen base
    show bron pout

    with dissolve
    bron " Well, show me what you've got and draw the thing already!"
    window hide
    play sound "audio/soundFX/Get.mp3"
    show blackopacity
    show bronwpaper
    with dissolve
    window show
    "I've got this."
    window hide
    play sound "audio/soundFX/FX3/drawing-a-circle.wav" volume 1.0
    show bronwpape one with dissolve
    pause 0.3
    window show
    "..."
    "Shit. "
    "I'm horrible at drawing!"
    "Okay... Comparing my image to hers I think I'll need to add some shading..."
    window hide
    play sound "audio/soundFX/FX3/scribble.wav" volume 1.0
    show bronwpape two with dissolve
    pause 0.3
    window show
    "..."
    "Something else is missing..."
    "Many of the other drawings have some descriptive notes and measurements..."
    "That will help communicate it better!"
    window hide
    play sound "audio/soundFX/FX3/drawing-a-circle.wav" volume 1.0
    show bronwpape three with dissolve
    pause 0.3
    window show
    "Nearly there!"
    "..."
    "Who am I kidding?! "
    "It looks like trash!"
    " I have to find a way to save it..."
    " I have one final idea..."
    window hide

    play sound "audio/soundFX/FX3/drawdots.wav" volume 1.0
    show bronwpape four with dissolve
    pause 0.3
    window show
    "A smiling face!"
    "But I kinda messed that up too... "
    "Ughhh."
    bron " You done or what? "
    me "Y-yeah!"
    "She pulls it from my hands!"
    window hide
    play sound "audio/soundFX/Get.mp3"
    hide bronwpape
    hide bronwpaper
    hide blackopacity
    with dissolve
    show bronwen paperlook at left:
        yalign -0.0 xalign 1.3
        zoom 0.9
    show broneye lookdown at left:
        yalign -0.0 xalign 1.3
        zoom 0.9

    with dissolve
    pause 0.4
    window show
    bron " ?"
    show bron questioning with dissolve
    bron " ???"
    bron " What the..."
    show bron baseface2 with dissolve
    bron " Is that a mushroom or wha--"

    hide broneye
    show bron surprise
    with dissolve
    with vpunch

    bron "!!"
    show bron rageface
    with dissolve
    with hpunch
    bron " ANOTHER DAMN BUTTPLUG!?"
    " Oh no, she knows!!"
    bron " I've been making these damn plugs almost non-stop for like a week now!"
    show bron meanface with dissolve
    bron " Out of all the crazy things you could have me make..."
    show bron done with dissolve
    bron " It's that damn book, isn't it? "
    bron "Hungry Hunk or something?"
    show bron cooldown with dissolve
    bron " Ugh. Trends."
    show bron questioning at left:
        yalign -0.0 xalign 1.3
        zoom 0.9
    with dissolve
    bron " So this is what the princess is up to, huh?"
    me " No- "
    me "I... don't have any more information!"
    window hide
    show bronwen hips
    show broneye lookdown at left:
        yalign -0.0 xalign 1.3
        zoom 0.9
    with dissolve
    pause 0.2
    window show
    " She looks at the gold for a moment."
    bron " She must've really gone at it if she deformed it into this weird smushed thing..."
    hide broneye with dissolve
    bron " Did she say anything else about it?"
    me " No! I'm not even sure what it's for!"
    show bron done with dissolve
    bron " Suuuure..."
    bron" Well, I'll fix it up for ya..."
    show bronwen hammerhip

    show bron pout
    with dissolve
    bron " I'm supposed to be taking a break but this should be quick..."
    bron " Gold is pretty malleable and these plugs have become routine by now..."
    window hide
    show bronwen raised
    show broneye lookdown at left:
        yalign -0.0 xalign 1.3
        zoom 0.9
    with dissolve
    pause 0.2
    show blackshake behind bg

    show bronwenhammering with fade
    play sound "audio/soundFX/FX3/anvil-steel.wav" volume 0.4
    with hpunch
    #Anvil Smack Sound
    pause 0.2
    play sound "audio/soundFX/FX3/anvil-steel.wav" volume 0.4
    with hpunch
    pause 0.2
    play sound "audio/soundFX/FX3/anvil-steel.wav" volume 0.4
    with hpunch
    window show


    "As she hammers away at the anvil one of her shoulder straps snap off and her boob pops out!"
    "She looks really scary and strong when working. "
    "I definitely see some resemblance to Rolf now!"
    hide goldsmithanvil
    bron "One more should do it!"
    window hide
    play sound "audio/soundFX/FX3/anvil-steel.wav" volume 0.8
    with hpunch
    pause 0.4
    #Anvil Smack Sound
    hide black
    hide bronwenhammering
    hide bronwen
    show bronwe holdplug behind smithyanvil at left:
        yalign -0.0 xalign 1.3
        zoom 0.9
    show bron baseface behind smithyanvil at left:
        yalign -0.0 xalign 1.3
        zoom 0.9
    hide broneye
    with fade
    pause 0.3
    window show
    bron " So..."
    bron " I added some extra gold to it and threw a gem on there."
    show bron smilee at left:
        yalign -0.0 xalign 1.3
        zoom 0.9
    with dissolve
    bron " Girly girls love that sparkly shit."
    "I look away."
    show bron done with dissolve
    bron "What? "
    bron "You requested this thing and now you're too embarrassed to look at it? "
    me " I-It's not that..."
    me "Your boob fell out."
    show bron surprise
    show broneye lookdownside at left:
        yalign -0.0 xalign 1.3
        zoom 0.9
    with dissolve
    bron "O-Oh!"
    show bron laugh
    hide broneye
    with dissolve
    bron " HAH! "
    bron "These clothes can't contain all my muscle!"
    me " ..."
    show bron done with dissolve
    bron " Don't make things awkward, it's just a fuckin' boob. "
    show bron smilee with dissolve
    bron "Dad's always running around with one of his nips out but I didn't see you blush like that when he showed up."
    "I turn to face her and do my best to act casually about it."
    me " R-right!"
    show bron smile with dissolve
    bron " Anyways here's your damn plug."
    show bronwe hips with dissolve
    pause 0.2
    play sound "audio/soundFX/Get.mp3"
    show blackopacity
    show bronplug
    with dissolve
    "Woah!"
    show bronplugsparkle with dissolve
    me "It turned out really nice!"
    "And pretty big... Almost as girthy as my peen."
    bron " Picked out a purple gem for it too."
    bron "I'm sure the princess will swoon over it matching her eyes or whatever."
    "I put it in my pocket."
    play sound "audio/soundFX/Sit Pillow.wav"
    hide blackopacity
    hide bronplug
    hide bronplugsparkle
    with dissolve
    me " Thank you!"
    show bron smileside with dissolve
    bron " Don't thank me."
    show bron smilee with dissolve
    bron " You'll be paying extra for the gem and added size! "

    show bronwe knuckles
    show bron laugh
    with dissolve

    bron " Hahaha. "
    me " Oh..."
    show bron smilee with dissolve
    bron " But y'know these kinky broads always come back wanting bigger and bigger sizes..."
    bron " I'm sure little miss royalty is due for an upgrade."
    show bron laugh
    show bronwe hips
    with dissolve
    bron " And she can surely cover the extra cost!"
    me " W- Whatever you say!"
    show bronwe base
    show bron baseface2
    with dissolve
    bron " Well, I'll be expecting the payment tomorrow!"
    play sound "audio/soundFX/Get.mp3"
    show bronwe takeout
    show bron done
    hide bgsmithtakeout
    with dissolve
    bron " Now leave so I can have my dinner before it gets cold!"
    me " O-okay! "
    me "Enjoy your food!"
    me "And thank you for your time!"
    if liename == True:
        show bron smilee with dissolve
        bron " Sure thing, \" [lie_name] \"!"
        show bron laugh with dissolve
        bron " Hahaha!"
        " ... She picked up on the stupid nickname Rolf still calls me."
    else:
        show bron smilee with dissolve
        bron " Don't worry about it."
    stop music fadeout 1.0
    window hide

    #Maybe you forget to bring back money. And bron forces you to do her a favor instead?
    #Or I think emelie just gives you money and its barely discussed.
    #When you come back she says " I know they're good! ;D " and you ask how??
    #Well to be good at your craft you gotta test your own-
    #me " Produce.. yeah "
    #The two of you are pretty similar!
    #bron: what do u know of it?
    #you tell her you're a farmer and you always have to test your own produce to make sure its up to quality!
    # bron " No shot, arent you one of those pampered lil shits barely moving a muscle?
    #Show me those hands!  You show her your callous hands.
    #bron: Huh.. full of surprises, arent ya?
    #She blushes and her disposition changes.
    #Bron :tell you what...
    #Bron " Your payment doesnt cover the expenses!!!
    #Bron "That gem was an amethyst! It's worth.... like double of what most gems cost!"
    #me " What?! hmmm i guess I can go ask for some more gold-"
    #Bron " I wanted it today, remember? You gotta do me a favor instead...
    #bron : Either try one of my creations out for me... or clean the room!"
    #me " Why do I have to try it? didn't you say you try your produce yourself?"
    #Bron " Well.. I don't have the parts required for this thing..."
    #She holds up a cock n balls ring.
    #It's supposed to make you last longer during naughty actions, she jerks u off and maybe rides you or w/e with ur dicc between her muscly thighs, squeezing you hard. Flicks your balls? Kinda toying with you in a dominant way.
    #me " isn't this all a bit sudden?!"
    #bron " What? I gotta take you out for dinner just so you'll drop those pants? Come on... Don't got time for that with my workload.
    #You don't cum.
    #Ruined orgasm? makes you cum on yourself? But then maybe she licks it up off your belly cus she's a lil gluttonous too.


    #bron"If you loosen my muscles up!"
    #bron " You're an assistant, no? You're experts at shit like this!"


label aftersmithy:

    scene black with dissolve
    stop music fadeout 1.0
    play sound "audio/soundFX/Door Close 2.wav"

    window show
    "I hurry back out and feel a lot of stress leave my body."
    window hide
    #scene outside smithy
    play music "audio/Birds.wav" fadein 1.0 volume 0.9
    scene bg tailorsmith with fade
    pause 0.3
    window show
    "Phew! "
    "Got pretty worried there for a second with Rolf staring me down again."
    "I'm glad Bronwen stopped him... "
    "But she's a lot to handle too!"
    "At least I ended up with a nice buttplug! "
    "I hope it'll make Emelie happy."
    window hide
    show black with dissolve
    window show
    "I make my way back to the park."
    window hide
    scene bg whale

    with dissolve
    play music "audio/adventures-in-adventureland-by-kevin-macleod-from-filmmusic-io.mp3" fadein 0.1 volume 0.4
    play sound "audio/soundFX/run2.wav"
    show billy base at left:
        yalign 0.4 xalign -0.08
    with easeinleft
    show billy laugh with dissolve
    window show
    billy " Oh hey, buddy!"
    show billy bellyhapi with dissolve
    billy " I was just about to go check on ya."
    billy " How'd it go?"
    me " Went pretty smoothly all things considered."
    show billy laugh with dissolve
    billy " Awesome!"
    billy " Emelie will be happy to get her lil' golden heart back!"
    me " R-right!"
    me " Are we going to visit her now?"
    show billy finger with dissolve
    billy "There should be a few hours left until she's done with her classes!"
    billy " I can take you there but I've got some guard duties to take care of in the meantime!"
    show billy bellyhapi with dissolve
    billy " Maybe you can kill some time at Victoria's shop while waiting?"

    show billy casualaugh with dissolve
    billy " She seemed to really like you! "
    show billy clench with dissolve
    billy " And I think she gets a little lonely in the shop sometimes, especially in summer now that the big new release is out of stock!"
    show billy casualaugh with dissolve
    billy "I'm sure she'll let you read another book or two!"
    me " Sure!"
    window hide
    show black with dissolve
    window show
    " Billy walks with me to Victoria's shop. "
    window hide
    scene librarysign with dissolve
    pause 0.5
    window show
    billy " Well, here we are again!"
    billy " I'll be waiting by the fountain outside Emelie's room when Victoria closes shop!"
    billy " See ya then, buddy!"
    me " Sounds good, Billy!"
    billy " Have a good one!"
    play sound "audio/soundFX/run2.wav"
    " He hurries off. "
    window hide
    show black with dissolve
    window show
    "I walk through the door."
    stop music fadeout 1.0
    window hide
    play sound "audio/soundFX/FX2/shop-door-bell.wav" volume 0.5
    show black with dissolve
    scene bg library

    show victoria grubstick:
        yalign 1.1 xalign 0.0
    show vic lash:
        yalign 1.1 xalign 0.0
    show librarydesk

    show blackopacity
    show victoriagrubsucc1

    with fade

    pause 0.4
    window show
    show blackshake at truecenter behind bg
    "!!"
    "Victoria is gawking down on a grub stick!"
    play sound "audio/soundFX/FX2/Chicken.wav" volume 0.4
    pause 0.2
    with hpunch
    show victoriagrubsucc2 with dissolve
    vic " !!"
    vic " Mhhgrl!"
    "She quickly swallows the grub down!"
    hide victoriagrubsucc2
    hide blackopacity
    hide victoriagrubsucc1
    with dissolve
    with vpunch
    play music "audio/Tavern+Brawl+-+320bit.mp3" fadein 1.0 volume 0.4
    vic "Ahem!"
    vic " Happy to see you come by again, [Protagonist]!"
    show victoria behindback:
        yalign 1.1 xalign 0.0
    show vic blush
    with dissolve
    vic " Sorry about the visual, I just love those grub sticks."
    if Grub == True:
        me " Don't worry about it! "
        me "I had one myself earlier today and it was delicious!"
        show vic closed with dissolve
        vic " Oh really? That's great!"
        show victoria hiphold
        show vic lash
        with dissolve
        vic "They're very nutritious!"
        show vic smile with dissolve
        vic " But if I'm honest I mostly eat them for the flavor... "
    else:
        me " Don't worry about it!"
        me " I haven't had one yet myself, but I tried a craburger earlier!"
        show vic closed with dissolve
        vic " Oh? They're good too!"
        show victoria hiphold
        show vic blush

        with dissolve
        vic" But there's just something special about those squishy grubs!"
        show vic smile with dissolve
        vic " Maybe it's a bird thing... I have a woodpecker friend who smacks a hole in every tree she can find! Always looking for those juicy creepy crawlies!"
        #Choice about openness to eating bugs
        window hide
        menu:
            with dissolve
            "Bugs or worms aren't really my thing personally!":
                window show
                me "Bugs or worms aren't really my thing personally!"
            "I haven't tried too many insects myself but I'm open to giving em a try!":
                window show
                me "I haven't tried too many insects myself but I'm open to giving 'em a try!"
        show vic bigsmile with dissolve
        vic " I see!"
    show victoria hiphands
    show vic squint
    with dissolve
    vic " So, what brings you here today?"
    window hide
    menu:
        with dissolve
        "Mostly here to kill some time!":
            window show
            me "Mostly here to kill some time!"
            show vic smile with dissolve
            vic " Oh, I see! "
            show victoria glassesup
            show vic lash
            with dissolve
            vic "Well, we have plenty of books! "
            vic " Or maybe you just wanna chat?"
            show vic eeh
            show victoria proper
            with dissolve
            vic " I... read a lot."
        "I wanted to see you!":
            window show
            me "I wanted to see you!"
            show victoria proper
            show vic surpriseblush
            with dissolve
            vic "!?"
            show vic wide with dissolve
            vic " O-oh!"
            show victoria glassesup
            show vic lash
            with dissolve
            vic " Well, that's nice to hear!"
    show victoria handonbooklow
    show vic blush
    show victoriahandonbook:
        yalign 1.1 xalign 0.0
    with dissolve
    vic " When there aren't any customers around I always have my eyes in a book."
    show vic sad with dissolve
    vic " But I get a little antsy some days just reading and reading."
    show vic lash with dissolve
    vic " Sometimes people come to study which is nice! "
    vic "Libraries are full of knowledge and I'm always happy to help!"
    hide victoriahandonbook
    show victoria hiphold
    show vic smile
    with dissolve
    vic " That social side of the job is a nice break!"
    show vic laugh with dissolve
    vic " So I'm happy you're here!"
    show vic bigsmile with dissolve
    vic " Let me know if there's anything you wanna know or chat about!"
    "Hmm..."
    window hide
    show blackopacity
    show chickenmemory
    with dissolve
    pause 0.2
    window show
    " I'm kinda curious about when I saw her yesterday right when I entered the city!"
    " At least I think that was Victoria..."
    window hide
    hide blackopacity
    hide chickenmemory
    with dissolve
    window show
    me "I'm pretty sure I saw you when I first entered the city yesterday!"
    show victoria proper
    show vic wide
    with dissolve
    vic " Oh, you did?"
    me "You were wheeling some eggs around in a stroller?"
    show vic closed with dissolve
    vic "R-right, that's correct! "
    me " Were those your kids? "
    me "Are you a mom?"
    show victoria hiphands
    show vic bigsmile
    with dissolve
    vic " Haha, I'm not a mom, but the eggs were indeed mine! "
    show vic lash with dissolve
    vic " I sell eggs for some extra money on the side! "
    me " ...?!"
    show victoria thinking
    show vic eyesurprise
    with dissolve

    vic " What's with that look?"
    show victoria hiphands
    show vic squint
    with dissolve
    vic " They were unfertilized!"
    vic" I wouldn't sell my own babies. "
    "Puh!"
    show vic proper
    show vic smile
    with dissolve
    vic " Us birds are lucky that way! "
    vic "People use eggs for all sorts of things!"
    show vic closed with dissolve
    vic " Same with milk! "
    " I can't help but glance down toward her cleavage"
    me " Do you... sell milk too?"
    "Shit, I shouldn't have asked that."

    show vic eeh
    with dissolve
    vic "No."
    show victoria behindback
    show vic blush
    with dissolve
    vic "Although I suppose I can understand why you might think so!"
    show vic laugh with dissolve
    vic " Some people are under the impression that all avians can fly and don't have breasts!"
    me "That's... kinda what I thought."
    show vic hiphands
    show vic surprise
    with dissolve
    vic " Really? "
    show vic wide
    with dissolve
label VictoriaLesson:
    if playnormal == False:
        play music "audio/Tavern+Brawl+-+320bit.mp3" fadein 2.0 volume 0.3 if_changed
        show bg library

        show victoria behindback:
            yalign 1.1 xalign 0.0
        show vic wide:
            yalign 1.1 xalign 0.0
        show librarydesk
        with fade
        window show
    vic "Well, then this is a good opportunity for a lesson!"
    if playnormal == False:
        window hide
        menu:
            with dissolve

            "Watch lesson.":
                window show

            "Skip lesson and go to the nudity!":
                jump vicboobscene


    play sound "audio/soundFX/Get.mp3"
    show victoria pointstick
    show vic squint
    with dissolve
    vic " SO!"
    "She grabs a stick and starts pulling on the rolled-up sheet above her quills."
    window hide

    play sound "audio/soundFX/FX3/pickupbook4.wav" volume 0.5
    show pulldown1 behind victoria with dissolve
    pause 0.2
    show victoria draww

    show viceye sidee:
        yalign 1.1 xalign 0.0
    hide librarydesk
    show librarydesknopen
    with dissolve
    pause 0.2
    window show

    "Then picks up the quill in front of her and quickly scribbles on the paper! "
    window hide
    play sound "audio/soundFX/FX3/writing-short.wav" volume 0.4
    show pulldown3 behind victoria
    hide pulldown1
    show vic bigsmile
    with dissolve
    pause 0.2
    window show
    vic " Theere we go! "
    "She's really good at drawing!"
    window hide
    show victoria hiphold
    hide viceye sidee
    show librarydesk
    hide librarydesknopen
    with dissolve
    pause 0.2
    window show
    vic "I read this book about the\"Theory of Evolution\"!"
    vic"It claims that as birds grew bigger they couldn't fly as well at their enlargened size. "
    show victoria glassesup
    show vic lash
    with dissolve
    vic"Over time their wings started resembling hands as more dextrous fingers allowed for the use of various tools!"
    vic"Breasts also seem to have evolved in these flightless avians. "
    show victoria hiphands
    show vic eeh
    with dissolve
    vic"But the jury is still out on how all that came about..."
    "This is a lot to take in!"
    show victoria handonbooklow
    show victoriahandonbook:
        yalign 1.1 xalign 0.0

    show vic bigsmile
    with dissolve
    vic " And as for milk production-"
    " She keeps going!!"
    vic"A broody hen who keeps her fertilized eggs warm will usually start producing milk a couple of weeks before they hatch."
    show vic wide with dissolve
    vic"But some claim you don't even need to have a baby to start lactating! "
    show vic blush with dissolve
    vic"Merely stimulating the breasts and nipples the right way can cause milk to be produced over time!"
    show viceye sidee:
        yalign 1.1 xalign 0.0
    with dissolve
    vic"Our bodies sure are amazing if that's the case... But I'm pretty skeptical! "
    hide viceye
    show vic closed
    hide victoriahandonbook
    show victoria proper
    with dissolve
    vic " Did'ya get all that or am I overwhelming you? "
    me " I think so..."
    me " But this \"evolution\" thing seems a bit random."
    show vic lash with dissolve
    vic " Yeah, I know! But that's what the science says so far at least!"
    "Maybe I shouldn't think too hard about it and just be happy for the boobs."
    show vic eyesurprise with dissolve
    vic " Or what if..."
    show victoria flap
    show vic bigsmile
    with dissolve
    vic " We're just not flapping our arms fast enough to take off!"
    show victoria flaps
    show vic laugh
    with dissolve
    "She laughs and flaps her arms vigorously! "
    vic " Cluck cluck cluck!"
    " Small feathery bits fly everywhere."
    show vic lash
    show victoria glassesup
    with dissolve
    vic "So, do you have any other questions?"
    $ vq1seen = False
    $ vq2seen = False
label VictoriaQuestions1:
    window hide
    menu:
        with dissolve
        "How did you learn how to draw?" if vq1seen == False:
            window show

            me " How did you learn how to draw?"
            show victoria hiphold
            show vic blush
            with dissolve
            vic " It's a bit embarrassing really..."
            show vic lash with dissolve
            vic " As a young child I didn't have any allowance but my parents let me loan a book every month!"
            show victoria proper
            show vic sad
            with dissolve
            vic " I didn't want to give them back to the library."
            show vic wide with dissolve
            vic " So I had a genius idea!"
            vic " One day I grabbed some ink, plucked a feather from my bum, and started copying the contents of the book I had loaned onto some blank paper!"
            show victoria hiphands
            show vic smile
            with dissolve
            vic " I made sure to copy every image and sentence from every book I could get a hold of before returning the original copies! "
            show victoria proper
            show vic bigsmile
            with dissolve
            vic "Slowly building my own collection of copied books!"
            show vic lash with dissolve
            vic " After a while, I would loan the books out to my friends and I became known for it!"
            show victoria behindback
            show vic blush
            with dissolve

            vic " But... it isn't really legal to do so for profit... "
            vic "Since the original author wouldn't get paid."
            show vic lash with dissolve
            vic " But I learned a lot!"
            show vic closed with dissolve
            vic " And when I finally got out of school after working some odd jobs I turned it into a legit business!"
            show victoria hiphold
            show vic smile
            with dissolve
            vic "  All those early years of copying the images from books all day must've helped me!"
            $ vq1seen = True
            jump VictoriaQuestions1


        "Can different species mate and have kids?" if vq2seen == False:
            window show
            me"Can different species mate and have kids?"
            show victoria hiphold
            show vic wide
            with dissolve
            vic " Yes! "
            show vic lash with dissolve
            vic " As you probably know- "
            show victoria hiphands
            show vic blush
            with dissolve
            vic " With same-species sex, pregnancy can happen with just a tiny drop of seminal fluid. "
            vic "So you have to be very careful! "
            show victoria proper
            show vic eeh
            with dissolve
            vic "Simply pulling out before the \"grand finale\" could still result in a pregnancy."
            show victoria glassesup
            show vic lash
            with dissolve
            vic " However!"
            vic "It takes more for pregnancy to occur during cross-species intercourse!"
            show victoria hiphold
            show vic blush
            show vic eyesurprise:
                yalign 1.1 xalign 0.0
            with dissolve
            vic " It requires a very big \"load\". "
            vic " With a huge amount of seminal fluid!"

            show vic smile
            with dissolve
            vic " So the \" pull-out-method \" has an impressive success-rate!"
            me " I see!"
            "That's very convenient and good to know!"
            window hide
            play sound "audio/soundFX/Get.mp3" volume 0.5
            show victoria pointstick
            show vic squint
            with dissolve
            play sound "audio/soundFX/FX3/postit.wav" volume 0.5
            hide pulldown3

            with dissolve
            pause 0.2
            window show
            vic " One second!"
            "She pulls the sheet of paper off onto the ground and drags down a new one!"
            window hide
            play sound "audio/soundFX/FX3/pickupbook4.wav" volume 0.5
            show pulldown1 behind victoria
            with dissolve
            show victoria draww
            show viceye sidee:
                yalign 1.1 xalign 0.0
            hide librarydesk
            show librarydesknopen
            with dissolve
            pause 0.2
            window show
            " She quickly draws on the blank paper."
            window hide
            play sound "audio/soundFX/FX3/writing-short.wav" volume 0.5
            show pulldown2 behind victoria with dissolve
            show vic bigsmile
            with dissolve
            window show
            vic " There!"
            window hide
            show victoria hiphold
            hide viceye sidee
            show librarydesk
            hide librarydesknopen
            with dissolve
            pause 0.2
            window show

            vic " As far as cross-species children are concerned they generally favor the mother a lot as far as physical traits are concerned!"
            show vic laugh with dissolve
            vic " An egg layer like myself couldn't give birth to a piglet or giant elephant for example!"
            " I'm not even sure what an \"elephant \" is. But I have enough information to digest as is! "
            show vic lash with dissolve
            vic " But things like height, hair, eye color, and pesky allergies could still transfer from the father to the child!"
            show victoria proper
            show vic wide
            with dissolve

            vic "So yeah, no piglets with feathers and beaks or anything crazy like that can happen!"
            show vic eyesurprise with dissolve
            vic "..."
            show vic blush with dissolve
            vic " Or well..."
            show vic behindback
            show vic eeh
            with dissolve
            vic " There are claimed sightings of the mystical creature known as the \"Platypus\"..."
            show victoria hiphold
            show vic lash
            with dissolve
            vic "But let's not go there for this lesson!"

            $ vq2seen = True
            jump VictoriaQuestions1


        "{alpha=*0.8}No more questions!{/alpha}":
            me "No more questions!"
            show victoria proper
            show vic smile
            with dissolve
            vic " I bet it's already a lot to take in!"




    me " It is! And I don't think I'm the best student..."
    show vic closed with dissolve
    vic " Oh hush, you're a great listener!"
    vic " And learning is usually just a matter of motivation! "
    show victoria hiphands
    show vic squint
    with dissolve
    vic " You need to feel rewarded for your hard work..."
    show victoria behindback with dissolve
    vic " And I've got juuust the thing I'm sure you'll love!~"
    " She reaches behind her back!"
    me "O-Oh?"
    window hide
    play sound "audio/soundFX/Get.mp3"
    show victoria holdcarrotcakeboob
    show vic laugh
    with dissolve
    with vpunch
    pause 0.3
    window show
    vic " ... Carrot cake!"
    me "..."
    "I'm still absolutely full after my meal and the ice cream, so carrot cake doesn't interest me at all!"
    "But that plate sort of pulls on her dress... making her cleavage even more pronounced!"
    show vic bigsmile with dissolve
    vic " Billy would always study better if he knew some food was waiting as a reward!"
    vic " And I see your mouth is watering too~ "
    show vic closed with dissolve
    vic "Highly motivated!!"
    " I clear my throat and try to look away. "
    me "I-I'm good! "
    me "I just ate before coming here, but thank you very much! "
    show vic sad with dissolve
    vic "..."
    vic " But I swear I saw a spark of motivation in your eyes..."
    show vic downsurprise
    with dissolve
    " She looks down to notice her nipples almost poking out!"
    with hpunch

    vic "!!!"

    vic " Oh... "
    show vic eyesurprise:
        yalign 1.1 xalign 0.0
    with dissolve
    vic "I... think I see what might have been motivating you..."
    show vic grump with dissolve
    vic " Exposed anatomy."
    "Oh crap, she saw me staring!"
    me " Sorry I didn't mean to-"

    show vic blush with dissolve
    vic " No, don't worry..."
    vic " It makes sense, really. "
    " She puts the carrot cake away."
    window hide
    play sound "audio/soundFX/Sit Pillow.wav" volume 0.4
    show victoria behindback
    show viceye sidee:
        yalign 1.1 xalign 0.0
    with dissolve
    pause 0.2
    window show
    vic "You were just learning about this stuff... "
    hide viceye with dissolve
    vic "Of course you'd be interested in the real thing!"

    show vic closed
    with dissolve
    vic " So I'm happy we've found a topic you're passionate about!"

    show victoria hiphands
    show vic lash
    with dissolve
    vic " Breasts sure are interesting."
    window hide
    play sound "audio/soundFX/Get.mp3" volume 0.5

    show victoria pointstick
    show viceye sidee:
        yalign 1.1 xalign 0.0
    with dissolve
    pause 0.3
    play sound "audio/soundFX/FX3/postit.wav" volume 0.5
    hide pulldown2
    hide pulldown3
    hide pulldown4
    hide pulldown1

    with dissolve
    pause 0.3
    play sound "audio/soundFX/FX3/pickupbook4.wav" volume 0.5
    show pulldown1 behind victoria
    with dissolve
    show victoria draww
    hide librarydesk
    show librarydesknopen

    with dissolve
    pause 0.2
    window show
    " She pulls a new sheet of paper down and spends some time on a few anatomy drawings."
    window hide
    play sound "audio/soundFX/FX3/writing-short.wav" volume 0.4
    show pulldown4 behind victoria with dissolve
    show vic bigsmile
    with dissolve
    pause 0.2
    window show
    vic " There we go! "
    hide viceye
    show vic lash
    with dissolve
    vic "That's some of the anatomical breast knowledge I have!"
    me " G-Great!"
    show vic sad
    show victoria proper
    show librarydesk
    hide librarydesknopen
    with dissolve
    vic " But you look a little tired..."
    vic " And I know that look very well."
    show victoria hiphold
    show vic smile
    with dissolve
    vic " It's the look of reading and listening too much!"


    vic "Now... "
    show vic horni

    with dissolve
    vic "While you can learn a lot through pictures and words... "
    vic " A teacher sometimes has to make education more..."
    vic " Engaging."
    stop music fadeout 2.0
    show victoria behindback
    show vic blush
    show viceye sidee:
        yalign 1.1 xalign 0.0
    with dissolve
    vic "Some things can be really tricky to wrap your mind around..."
    window hide
label vicboobscene:
    play music "audio/Farm+-+320bit.mp3" fadein 0.1 volume 0.4
    play sound "audio/soundFX/Blanket Move.wav"
    scene vicundress
    show blackshake at truecenter behind vicundress
    show vicundressblush
    with fade
    pause 0.6
    window show
    vic " Like how something feels... "
    with hpunch
    "!?!?"
    " She's starting to undress!"
    vic " And since you're so motivated to learn..."
    hide vicundressblush with dissolve
    vic " I figure we can have a closer look now with your newly piqued interest!"
    "Her face goes from nervous to relaxed as she reads my expression."
    vic " Just remember to pay close attention, okay?"
    me " I will! "
    me "Very close! "
    window hide
    show vicboobaseandbra at truecenter:
        yalign 1.0

    with fade
    show vicboobaseandbra at truecenter:
        yalign 1.0
        linear 5.0 yalign 0.0

    $ renpy.pause(5.0, hard=True)
    window show
    " I slowly look her up and down."
    window hide
    show vicboobaseandbra at truecenter:
        yalign 0.0
        linear 2.5 yalign 0.45
    $ renpy.pause(2.5, hard=True)
    window show
    " My gaze stops around her chest."
    "Wow, her figure is gorgeous! "
    show vicboobabase at truecenter:
        yalign 0.45
    show vicboob bra at truecenter:
        yalign 0.45
    hide vicboobaseandbra
    with dissolve
    vic " Now take all the time you need!"
    " As I look her over I start thinking about how Emelie might feel about all this."
    " About me... \" inspecting\"  another lady!"
    " I think me and Emelie are sort of dating now... "
    " I'll make sure nothing goes too far until I've talked to her about it! "
    " And this is just a lesson! "
    "Maybe this kinda education is standard practice in a cultured city like Hog Haven!"
    #camera stops at her face
    show vicbace sideshy at truecenter:
        yalign 0.45
    with dissolve
    vic " Now..."
    vic " Do you remember the various parts from my drawings?"
    vic " Like where the nipple and areola are? "
    me " Yeah, I know!"
    hide vicbace sideshy
    with dissolve
    vic "Can you touch the area?"
    me " Touch??"
    me "Well, it's... under your bra. "
    show vicbace mouthclose at truecenter:
        yalign 0.45
    with dissolve
    vic " Mhm!"
    me "And you want me to touch it? "
    vic  "Yes!"
    me " O-okay!"
    window hide

    show vicboob brahandsup at truecenter:
        yalign 0.45
    show vicbace sweat at truecenter:
        yalign 0.45
    show vicboobalookdown at truecenter:
        yalign 0.45
    with dissolve
    play sound "audio/soundFX/Get.mp3"
    with vpunch
    pause 0.3
    window show
    "My mind races as I slide my hands in under her bra!"
    vic " Ahhn!"
    vic " I meant you could touch the area OVER the fabric!"
    " Shit. Of course that's what she meant. "
    " My body reached for them before I had time to think! "
    "I need to control myself better!"
    show vicboob brahands at truecenter:
        yalign 0.45
    hide vicboobalookdown
    with dissolve
    vic " Maybe I should've been clearer... but I don't mind! "
    vic "I was going to ask you to remove the bra after anyways..."
    "!!"
    window hide
    show vicboob bra at truecenter:
        yalign 0.45
    show vicbace mouthclose at truecenter:
        yalign 0.45
    with dissolve
    pause 0.2
    window show
    vic " You need a clear look of the subject or you won't learn as much!"
    vic " And from my experience, most men need a lesson or two in how to unhook a bra..."
    vic " Although this design is about as straight forward as it gets!"
    "I swallow hard and reach for the lil' knot in the middle of her bra!"
    window hide
    show vicboob braunhook
    show vicboobalookdown at truecenter:
        yalign 0.45
    with dissolve
    pause 0.2
    window show
    vic " Keep pulling! "
    window hide
    play sound "audio/soundFX/Get.mp3"
    show vicboob nudehandsup
    show vicboobablush at truecenter:
        yalign 0.45
    hide vicbace
    with dissolve
    with vpunch
    pause 0.6
    window show

    " Her tits fall out with a big bounce!"
    vic " Ahhh!"
    " She breathes heavily "
    hide vicboobalookdown with dissolve
    vic " Now that feels nice! "
    show vicboob nudehands
    show vicbace sweat at truecenter:
        yalign 0.45
    with dissolve
    vic "Bras can get a bit uncomfortable..."
    vic " I might need to go up in size too!"
    window hide
    hide vicboob
    show vicbace sideshy
    with dissolve
    pause 0.3
    window show
    vic " Next... "

    vic "Try to get a feel of their consistency and weight!"
    me " O-okay!"
    window hide
    play sound "audio/soundFX/Blanket Move.wav" volume 0.7
    show vicboob squish at truecenter:
        yalign 0.45
    hide vicbace sideshy

    with dissolve
    pause 0.5
    window show
    " I move my hands forward and squish her boobs together."
    vic " What do you think?"
    #Options to be analytical or more flirty
    me " Very soft!"
    vic " Yes! Now try to get a feel for their weight!"
    window hide
    show vicboob pressboob at truecenter:
        yalign 0.45
    show vicboobalookdown  at truecenter:
        yalign 0.45
    with dissolve
    pause 0.5
    window show
    vic " Mmmh, good good!"

    hide vicboobalookdown
    show vicboobahearteyes at truecenter:
        yalign 0.45

    with dissolve

    vic " What's your conclusion on the weight?"
    me " Really heavy!"
    vic " Any other observation?"
    me "  They're very warm."
    vic " Indeed! "
    vic "Especially after wearing clothes and a bra."
    show vicbace wary at truecenter:
        yalign 0.45
    hide vicboobahearteyes
    with dissolve
    vic " Sorry about the sweat..."
    " ...They are a bit damp."
    me " Don't worry about it! "
    window hide
    hide vicboob with dissolve
    pause 0.3
    window show
    me "Just adds to my knowledge!"
    show vicbace closed
    hide vicboobahearteyes
    with dissolve
    vic " R-right!"
    vic "That's what this is all about after all!"

    show vicbace sideshy
    hide vicboobablush
    with dissolve
    vic " So..."

    vic " Earlier you managed to locate the general area of the nipples and areola under my bra!"
    vic " So it seems you have the basic location down."
    hide vicbace
    show vicboobahearteyes at truecenter:
        yalign 0.45
    with dissolve
    vic " But now try squeezing my nipples specifically!"
    window hide
    play sound "audio/soundFX/Get.mp3"
    show vicboob pinch at truecenter:
        yalign 0.45
    show vicbace cheeki at truecenter:
        yalign 0.45
    show vicboobablush at truecenter:
        yalign 0.45
    with dissolve
    pause 0.5
    window show
    " I grab her large nipples. "
    vic " G-Good!"
    vic " Depending on who you ask, the nipple could be considered very sensitive or barely sensitive at all!"
    show vicbace sideshy with dissolve
    vic " Mine are pretty big and rub against my tight bra all day... "
    vic "So you need to give them a proper pinch to get a reaction out of me!"
    me "... Is that a challenge?"
    window hide
    pause 0.1
    show vicbace wink at truecenter:
        yalign 0.45
    with dissolve
    pause 0.3
    window show
    "She gives me a wink while blushing "
    "Phew, I love Victoria's teaching method!"
    " I give her nipples a decent pinch!"
    window hide
    with vpunch
    show vicboob pinchhands
    show vicbace closed
    with dissolve

    pause 0.3
    window show
    vic " Aah! "
    vic " Just like that!"
    window hide
    with vpunch
    show vicbace hnng
    with dissolve

    pause 0.3
    window show
    "I pinch them again!"
    vic " Ahhn!"
    " She seems to really like it!!"
    window hide

    menu:
        with dissolve
        "Give them a final mega-pinch!":
            with vpunch



            $ vicmilk = True

        "Go ease on the last one.":
            with vpunch


            $ vicmilk = False

    #Pinch soft or pinch hard can be options. hard 2 out of 3 times at least makes her lactate. if you pinch hard on the last one.
    show vicnipsquish with fade


    if vicmilk == True:
        with hpunch
        pause 0.3
        window show
        vic "Ahhhh!!!!"
        window hide
        show vicnipsquishmilk
        show vicnipsquishahegao
        with dissolve
        pause 0.5
        window show
        "!!"
        "Her nipples spray a large amount of milk toward me!"
        vic " A-Aaaahhh!"
        window hide
        hide vicnipsquishmilk with dissolve
        pause 0.4
        hide vicnipsquishahegao with dissolve
        pause 0.4
        window show
        vic " T-That was surprisingly quick! "
        " It's probably because I pinched them so hard!!"
        vic "Maybe avians are more prone to lactation from stimulus due to our egg-laying biology!"
        vic " Or maybe you've just got the right technique~ "

    else:
        with hpunch
        show vicnipsquishahegao
        with dissolve

        pause 0.3
        window show
        vic "Ahhhh!!!!"
        " She moans loudly and I loosen my grip a little!"
        hide vicnipsquishahegao with dissolve
        vic "T-that's enough for now, I t-think!"
        "She breathes and blushes heavily"
        vic " You seem to have your breast anatomy down well! "
        vic "And it seems you know just how to stimulate a woman's nipples in a satisfactory way!"
    stop music fadeout 0.5

    window hide
    scene bg library
    show librarydesk
    show vicpanties behindback:
        yalign 0.5 xalign 0.5 zoom 1.1
    show vic insecure :
        yalign 0.5 xalign 0.5 zoom 1.1

    if vicmilk == True:
        show vicmilky:
            yalign 0.5 xalign 0.5 zoom 1.1

    with fade
    pause 0.3
    window show
    play music "audio/Tavern+Brawl+-+320bit.mp3" fadein 2.0 volume 0.3
    vic " Phew... That was a lot!"
    vic " You know... I really loved sharing my knowledge like that! "
    show vicpanties hiphand

    with dissolve
    vic "Being a teacher was never on my mind growing up but now that I have all this knowledge I just feel really good sharing it!"
    me " I enjoyed the... {i}lesson{/i} too!"
    show vicpanties proper
    show vic lash
    with dissolve
    vic " It's approaching closing time. "

    vic "I'll have to get a few things ready before that!"
    me " Okay! "
    me "I'm supposed to be meeting up with Billy pretty soon myself."
    show vicpanties hiphand
    show vic bigsmile
    with dissolve
    vic " I see! "
    vic "You two being close really warms my heart!"
    window hide
    scene black with fade
    play sound "audio/soundFX/Blanket Move.wav"
    window show
    "Victoria quickly dresses and follows me on my way out."
    window hide
    play sound "audio/soundFX/FX2/shop-door-bell.wav" volume 0.5
    if vicmilk == True:
        show vicmilkywave with fade
    else:
        show vicnomilkywave with fade
    window show
    vic "I hope you had a good look and learned a lot today, dear student!"
    me " Absolutely! "
    if vicmilk == True:
        "Looks like she's still leaking some milk through her top!"
    me "Have a great rest of your day, teacher!"
    vic " Aww."
    vic " Until next time! "
    window hide
    $ unlock("S5")
    $ renpy.end_replay()
    pause 0.2
    stop music fadeout 3.0
    jump ch4

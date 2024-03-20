label ch4:

    scene black with fade
    window show
    " 'Can't believe people get bored of school if that's what your typical lesson is like!"
    "Victoria {i}really{/i} got excited about teaching me things too."

    " I make my way back to the fountain."
    window hide
    play music "audio/adventures-in-adventureland-by-kevin-macleod-from-filmmusic-io.mp3" fadein 0.1 volume 0.4
    scene bg fountainsunset
    show billy base at left:
        yalign 0.4 xalign -0.08
    with fade
    pause 0.3
    show bill laughface at left:
        yalign 0.4 xalign -0.08
    with dissolve
    window show
    billy "Hey hey, buddy! "
    billy " Right on time!"
    me " Hey, Billy!"
    show billy bellyhapi at left:
        yalign 0.4 xalign -0.08
    hide bill
    with dissolve
    billy " You sure look excited!"
    billy "Did'ya have a good read? "
    billy "Or maybe Victoria just taught you something interesting?"
    me " She sure did!"
    me " I learned a lot."
    show billy base with dissolve
    billy " You'll have to tell me all about it sometime!"
    billy " But now It's time I get ya to Emelie!"
    show billy finger with dissolve
    billy " See that tower up there? "
    "I look up to where Billy is pointing."
    window hide
    show blackopacity
    show tower
    with dissolve
    window show
    billy " That's where Emelie's main room is! "
    me " Woah!"
    "I've seen that tower from beyond the gates so many times before but it looks totally different up close!"
    " When having my morning meals on the hill I'd look at those banners flapping in the wind, but I never imagined actually going there!"
    window hide
    hide blackopacity
    hide tower
    with dissolve
    pause 0.3
    show billy casualaugh with dissolve
    window show
    billy " I'll show you the way!"
    me " Okay!"
    window hide
    scene black with fade
    window show
    " I follow Billy inside."
    window hide
    scene bg doorsunset
    with fade
    play sound "audio/soundFX/Run2.wav"
    show billy base at left:
        yalign 0.4 xalign -0.08
    with easeinleft
    window show
    billy " We start off here!"
    billy " Then to the baths!"
    window hide
    play sound "audio/soundFX/Run.mp3"
    hide billy with easeoutright
    scene bg BathHallsSunset
    with fade
    show billy base at left:
        yalign 0.4 xalign -0.08
    with easeinleft
    window show

    billy " Down this corridor!"

    window hide
    scene bg stairs
    with fade
    play sound "audio/soundFX/Run2.wav"
    show billy base at left:
        yalign 0.4 xalign -0.08
    with easeinleft
    pause 0.5
    show billy bellyhapi with dissolve
    window show
    billy " And here we are!"
    show billy finger with dissolve
    billy " Her room is way up these stairs! "
    billy "Then just knock on the big door when you see it! "
    show billy scratchy
    show bill casualface at left:
        yalign 0.4 xalign -0.08
    with dissolve
    "Billy pulls something out from behind his back."
    play sound "audio/soundFX/PageTurn.wav" volume 0.6
    show billy paper
    hide bill
    with dissolve
    billy " While I was waiting by the fountain I made sure to draw ya something so you'd know what to expect!"
    show bill baseface at left:
        yalign 0.4 xalign -0.08
    with dissolve
    billy " Here!"
    " He hands me the paper."
    window hide
    show billy base with dissolve
    pause 0.3
    play sound "audio/soundFX/Get.mp3"
    show blackopacity
    show billypapertower
    with dissolve
    pause 1.0
    window show
    " What the hell?!"
    me " You drew this?"
    billy " Y-yeah."
    " Billy is really good at drawing too!"
    " His style is so cute and colorful..."
    window hide
    menu:
        with dissolve



        "Your art is so cute!":
            window show
            me "Your art is so cute!"
            billy " Aw, thank you!"
            billy " I figured I would take you all the way to your destination but..."
            billy "I really don't feel like taking the stairs."
            billy " There are just TOO many steps! "

        " You drew me all this on a whim just to avoid walking up a couple of stairs??":
            window show
            me " You drew me all this on a whim just to avoid walking up a couple of stairs??"
            billy " It's not just a couple of stairs!"
            billy "It's a nightmare!"
    "I put the picture down."
    window hide
    hide blackopacity
    hide billypapertower
    with dissolve
    window show
    me " I see...  I imagine wearing such heavy armor doesn't help when it comes to climbing stairs either."
    show billy ooo
    hide bill
    with dissolve
    billy " The armor helps a lot! "
    me " What?"
    show billy clench with dissolve
    billy "I fell down the stairs when at the very top once and tumbled all the way back down!!"
    me " Oh no!"
    show billy casual with dissolve
    billy " But I was left without a scratch!"
    billy " All thanks to this armor!"
    me " I see!"
    billy "..."
    show billy belly with dissolve
    billy " Then I had to walk all the way up again... "
    show bill cryy at left:
        yalign 0.4 xalign -0.08
    with dissolve
    billy "Just thinking about it makes me sweat!"
    " He looks distraught at the thought."
    hide bill
    show billy base
    with dissolve
    billy " Anyways-"
    billy " Think you can find your way up on your own?"
    me " I do! Thanks!"
    show billy casualaugh with dissolve
    billy " Great! "
    billy " I should get going myself. Don't want to miss out on supper today too!"
    show billy base with dissolve
    billy " I'll see you tomorrow!"
    show billy high with dissolve

    " Billy raises his hand for a high five."
    if Friendship >=2:
        " I feel our friendship has evolved! "
    window hide
    menu:
        with dissolve

        "High five!":


            #High five sound#
            play sound "audio/soundFX/Slap.wav"
            show billystar:
                yalign 0.4 xalign -0.08
            show blackshake at truecenter behind bg
            with hpunch
            window show
            $ Friendship +=1

            "Our hands clash hard once again!"
            me " Thank you for everything today, Billy!"
            hide billystar with dissolve
            show bill laughface:
                yalign 0.4 xalign -0.08
            show billy clench
            with dissolve
            billy "Of course, buddy!"
            billy " See you tomorrow!"
            me " Yes! Enjoy your supper."
            show billy casualaugh
            hide bill
            show billyblush at left:
                yalign 0.4 xalign -0.08
            with dissolve
            billy "I will! Now don't keep Emelie waiting, heehee! "
            window hide
            play sound "audio/soundFX/run2.wav"
            hide billy
            hide bill
            hide billyblush
            with easeoutleft
            window show
            "Billy giggles and skips away."




        " {size=+5}High TEN!{/size}" if Friendship >= 2:
            $ Friendship +=2
            " I raise both hands up!"
            show bill waa at left:
                yalign 0.4 xalign -0.08
            with dissolve
            billy "!!"
            window hide
            show billy ten
            with dissolve
            play sound "audio/soundFX/FX2/spank.wav" volume 0.6
            with vpunch
            show billytenstar at left:
                yalign 0.4 xalign -0.08
            with dissolve
            hide billytenstar
            with dissolve
            window show
            " Both our hands clash perfectly!"
            show bill starsmile
            with dissolve
            billy " W-Woah!! "
            show billy laugh with dissolve
            billy " That's might be the coolest thing I've ever done!! "
            show bill squint with dissolve
            " He tears up a little."
            show billy base
            show bill sadface
            with dissolve
            billy " I can't wait to hang out tomorrow too, buddy!"
            me " For sure!"
            me " See you tomorrow!"
            show billy casualaugh
            hide bill
            with dissolve
            billy " I absolutely will!"
            show billyblush at left:
                yalign 0.4 xalign -0.08
            with dissolve
            billy "Now don't keep Emelie waiting, heehee! "
            window hide
            play sound "audio/soundFX/run2.wav"
            hide billy
            hide billyblush
            with easeoutleft
            window show
            "Billy giggles and skips away."

        "Leave him hanging."if Friendship <= 1:
            window show
            $ highfive = False
            "..."
            show bill sadface at left:
                yalign 0.4 xalign -0.08
            with dissolve
            "Billy slowly starts lowering his hand. Sadness showing through the holes in his helmet. "
            show billy clench with dissolve
            billy "... "
            billy "I'll try not to ask for high fives going forward..."
            show bill casualface at left:
                yalign 0.4 xalign -0.08
            show billy base
            with dissolve
            billy " But I hope you have a fun evening with Emelie, buddy!"
            billy " See you tomorrow!"


            me " Bye bye."
            window hide
            play sound "audio/soundFX/run2.wav"
            hide billy
            hide bill
            with easeoutleft
            window show
            "Billy runs off."
    stop music fadeout 1.0
    " Guess I'll find out just how tough these stairs are!"
    play music "audio/Mega+Heavy+Suspense+-+320bit.mp3" fadein 1.0 volume 0.3
    window hide

    scene black with fade
    window show
    play sound "audio/soundFX/FX4/stairs1.wav" volume 0.9
    " I start moving up the stairs."
    "..."
    "My legs start aching after walking for over two minutes at a rapid pace."
    "Now I see why Billy chose to draw instead of following me all the way up!"
    play sound "audio/soundFX/FX4/stairs2.wav" volume 0.9
    "..."
    "Uuughh!"
    window hide
    show bgbrix
    show towerdoor
    with dissolve
    pause 0.3
    window show
    " I finally reach the door at the top!"
    me " Puhh..."
    "I wipe the sweat from my forehead and give it a push."

label emtower:
    stop music fadeout 1.0
    "The door opens."
    play sound "audio/soundFX/OpenDoor 1.wav"
    window hide
    scene bg towerroom
    show blackshake at truecenter behind bg
    show towerbook
    show towerchair
    show towermirror
    show towersmoke
    with fade
    play music "audio/starting-out-waltz-vivace-by-kevin-macleod-from-filmmusic-io.mp3" fadein 0.1 volume 0.3
    window show
    " Woah!"
    " Such an open and bright room!"
    window hide
    show emc proper at right:
        yalign 0.15
        zoom 1.0
    with dissolve
    pause 0.1
    show emf smile at right:
        yalign 0.15
        zoom 1.0
    with dissolve
    window show
    emelie " You made it!!"
    window hide
    menu:
        with dissolve



        "Of course! I'm the greatest assistant after all!":
            window show
            me "Of course! I'm the greatest assistant after all!"
            show emf laugh
            show emear high at right:
                yalign 0.15
                zoom 1.0
            with dissolve
            emelie " Haha!"
            emelie " You sure are!"


        "I couldn't wait to see you!":
            window show
            me "I couldn't wait to see you!"
            show emf insecure
            show emear high at right:
                yalign 0.15
                zoom 1.0
            with dissolve
            emelie "Aww! Classes today felt like they took an eternity! "
            show emf pout with dissolve
            emelie " I think because I was counting down the minutes until I could see you again."
    show emf normal
    hide emear
    with dissolve
    emelie " How do you like the room?"
    me " It's really nice and open!"
    show emc out
    show emf normalblush
    with dissolve
    emelie " I'm glad you like it!!"
    emelie " Definitely a bit fancier than my other one downstairs."
    me " Yeah, I guess all those stairs are the price you have to pay for such a nice room!"
    show emc hips
    show emf laugh
    show emear high at right:
        yalign 0.15
        zoom 1.0
    with dissolve
    emelie " Haha, that's one way to see it! "
    show emf bigsmile with dissolve
    emelie " I've gotten somewhat used to them by now since I walk them almost every day!"
    show emf normalblush with dissolve
    emelie " And at my height, the steps probably feel twice as tall as they do for you or Billy, haha!"
    me "I didn't think about that!"
    me " You're strong!"
    show emf bite
    show emc proper
    with dissolve
    emelie " Not very! But maybe it's toned my butt a little~"
    me " Then those stairs might not be so bad after all!"
    show emf bigsmile with dissolve
    emelie " Haha!"
    show emf concern
    hide emear
    with dissolve
    emelie "Billy REALLY hates the stairs."
    show emf smile with dissolve
    emelie " But he'll struggle his way up them whenever duty compels him!"
    emelie " He's very loyal and trustworthy."
    me "He really is!"
    me " And he went out of his way to draw me this pretty picture to motivate me and instruct me on how to get here."
    show emc out
    show emear high at right:
        yalign 0.15
        zoom 1.0
    show emf surprise
    with dissolve
    emelie " Oh?"
    emelie " Let me see!"
    " I pull the carefully rolled-up paper out of my pocket and hand it to her."
    window hide
    play sound "audio/soundFX/PageTurn.wav" volume 0.5
    show emc paper at right:
        yalign 0.15
        zoom 1.0
    show emf normal
    with dissolve

    #Show her the picture
    show emf bigsmile
    show emeye down at right:
        yalign 0.15
        zoom 1.0
    with dissolve
    window show
    emelie " Woaah!"
    show emf biggersmile with dissolve
    emelie " So cuuute!!"
    me " I know!"
    show emf normal
    hide emear
    show emeye close
    with dissolve
    emelie " And he drew me looking absolutely adorable!"

    hide emeye
    show emf normal
    with dissolve
    emelie " Billy has always been much better at drawing than me..."
    show emf smile with dissolve
    emelie " I'm more of a painter!"
    "I see a painting to the left behind her."
    "It looks really good!"
    me " Wait... You do art too?"
    me " Why is everyone in this city so good at drawing or painting?!"
    me "First Rolf & Bronwen, then Victoria & Billy, and now you!"
    show emf think with dissolve
    emelie " Hmmm... Must be a coincidence."
    me " I made a fool out of myself earlier trying to draw a \"buttplug\" properly!"
    show emf wide with dissolve
    emelie " You what???"
    show emc normal with dissolve
    "Emelie gives me Billy's drawing back."
    " I pull the plug out of my pocket and hand it to her. "
    play sound "audio/soundFX/Get.mp3"
    show emc plug
    show emf normal
    with dissolve
    show emf waa
    show emeye down2b at right:
        yalign 0.15
        zoom 1.0
    with dissolve
    me " I got this made for you!"
    with hpunch
    show emeye down3
    show emear high at right:
        yalign 0.15
        zoom 1.0
    with dissolve
    emelie " WOAAAH!"
    show emf biggersmile
    show emear high at right:
        yalign 0.15
        zoom 1.0
    show emeye down4
    with dissolve
    emelie " It's... It's beautiful!!"
    emelie " And the gem! It matches my eyes!"
    hide emeye with dissolve
    emelie " How did you get this?!"
    me " Remember the gold pendant you threw out of your room yesterday?"
    window hide
    show emc plugdown
    hide emear
    show emf smile
    with dissolve
    window show
    emelie " Yeah?"
    me " I found it!"
    me " But it was all bent out of shape. "
    me " I was going to repair it at the smithy but I figured you might like this more!"
    show emf laugh
    show emear high at right:
        yalign 0.15
        zoom 1.0
    with dissolve
    emelie " Absolutely!"
    emelie " It's so pretty I love it!"
    show emf normalblush
    hide emear
    with dissolve
    emelie " So you're saying you sketched it out on paper so Bronwen had a design to go off? "
    me " Yeah! But my drawing was terrible. "
    show emf insecure with dissolve
    emelie " Don't be so hard on yourself! "
    show emf normal with dissolve
    emelie "You only looked at the image of it in the book for a minute at most!"
    me " That's true... And I wanted to be a bit sneaky with my description."
    me " She did a great job with what she got though! "
    show emf pout
    hide emear
    with dissolve
    emelie "She's a relentless worker!"
    emelie " And amazing at what she does!"
    show emf insecure with dissolve
    emelie " But she can be a bit scary to talk to sometimes."
    me " She's definitely intense."
    show emf biggersmile
    show emear high at right:
        yalign 0.15
        zoom 1.0
    show emc plughips
    with dissolve
    emelie " I still can't believe you actually got her to make something like this!"
    emelie " Did you have secret pocket change or something?"
    me " I... have to pay her back for it tomorrow..."
    show emf smile
    hide emear
    with dissolve
    emelie " Oh, that's no problem I can cover it! "
    show emf laugh
    show emc plugdown
    with dissolve
    emelie " I would've paid a fortune to get this made without the embarrassment of asking for one myself! "
    me " I'm really glad you like it!"
    me " Had she followed my drawing closer you would've gotten a pyramid-shaped mushroom thing."
    show emf normalblush with dissolve
    emelie " Haha!"
    emelie "..."
    show emf surprise
    hide emear
    with dissolve
    emelie " Wait!"
    emelie " I have an idea!"
    me " What?"
    show emf wide with dissolve
    emelie " Why don't you give painting a try?"
    show emf normalblush with dissolve
    emelie" And I can give you a few tips!"
    me " Wha- I don't want to waste your paints!"
    show emf pout with dissolve
    emelie " Don't worry!"
    emelie " If you don't use them they dry out anyways!"
    me " Okay, I suppose I can give it a shot!"
    show emf normal
    show emc plughips
    with dissolve
    emelie " As a beginner it's easier to draw or paint from observation! "
    show emf really
    show emc plugdown
    with dissolve
    emelie " In my art classes I'm always forced to do observational paintings of fruit, plants or pottery."
    emelie " It's pretty dull."
    show emf normalblush
    show emc plughips
    with dissolve
    emelie " But I like to spice it up a bit!"
    emelie " So I draw faces on them and stuff after I'm done..."
    " I once again look over to her painting."
    me " That explains the pear having a face and legs!"
    " And a butthole..."
    show emf insecure with dissolve
    emelie " Well, it's difficult to paint things you have no interest in!"
    emelie  " ..."
    show emf sooth
    show emc plugdown
    with dissolve
    emelie " Maybe you'd like to paint me?"
    me " !"
    me " Absolutely!"
    show emf bigsmile
    show emear high at right:
        yalign 0.15
        zoom 1.0
    with dissolve
    emelie " Woo!"
    emelie " Then just give me a second and I'll change into something more eye-catching!"
    window hide
    hide towermirror with dissolve
    play sound "audio/soundFX/FX4/fwunk.wav" volume 0.8
    show towerclosemirror with dissolve
    window show
    " She pulls some sort of folding screen forward from beside her bed."
    hide emf
    hide emear
    with dissolve
    emelie " One moment!"
    window hide
    show emc plugdown at right:
        xalign 1.0 yalign 0.15 zoom 1.0
        linear 0.5 xalign 0.12
    pause 0.8
    window show
    " Emelie spends some time changing."
    " It takes a little while."
    window hide
    pause 0.3
    play sound "audio/soundFX/FX4/clothing2.wav"
    hide emc
    show eml normalb behind towerclosemirror at right:
        yalign 0.15 xalign 0.12
        linear 0.5 xalign 1.0
    with dissolve
    pause 0.4
    window show
    emelie " All done!"
    window hide
    pause 0.2
    hide towerclosemirror with dissolve
    play sound "audio/soundFX/FX4/fwunk.wav" volume 0.1
    show towermirror behind towersmoke with dissolve
    pause 0.3
    window show
    me " Woah! "
    me " That lingerie is so pretty!"
    show eml afterintro4 at right:
        yalign 0.15
        zoom 1.0

    with dissolve
    emelie " Thank you!"
    show eml afterintro5 at right:
        yalign 0.15
        zoom 1.0
    with dissolve

    emelie " What's your favorite part of the look?"
    window hide
    menu:
        with dissolve

        " Your face!":
            window show
            me " Your face!"
            show eml normal
            show emf really at right:
                yalign 0.15
                zoom 1.0
            with dissolve
            emelie " Tsk! "
            show emf yeaa
            show eml hips
            with dissolve
            emelie " A bit of a cowardly answer!"
            emelie " Don't be afraid of commenting on \"the goods\" ~"
            me " F-fine! But your face really is pretty!"
            show emf laugh
            show eml out
            with dissolve
            emelie " Haha!"
            " She blushes."
            show emf normalblush with dissolve
            emelie " Thank you."

        " That bra!":
            window show
            me " That bra!"
            show eml normal
            show emf pout at right:
                yalign 0.15
                zoom 1.0
            with dissolve
            emelie " Oh really? "
            show eml proper
            show emf bigsmile

            with dissolve
            emelie " I like it a lot as well! It's one of my better-fitting ones too..."
            emelie " A little small but still comfy enough!"
            show emf normalblush with dissolve
            emelie " And the lace feels nice against my skin..."

        " Those panties!":
            window show
            me " Those panties!"
            show emf yeaa at right:
                yalign 0.15
                zoom 1.0
            show eml hips
            with dissolve
            emelie " Oh? I'm not surprised..."
            me " Why?"
            show emf bigsmile
            show eml proper
            show emear high at right:
                yalign 0.15
                zoom 1.0
            with dissolve
            emelie " 'Cus they're the most skimpy part of the outfit!"
            " ... She's right. "
            me " What can I say? ...I'm a simple man."
            show emf laugh
            show eml out
            with dissolve
            emelie " Haha, maybe!"
            show emf normalblush
            hide emear
            show eml normal
            with dissolve
            emelie " But that doesn't have to be a bad thing!"



        " Those stockings!":
            window show
            me " Those stockings!"
            show eml normal
            show emf surprise at right:
                yalign 0.15
                zoom 1.0
            show emear high at right:
                yalign 0.15
                zoom 1.0
            with dissolve
            emelie " R-really? "
            show emf insecure
            hide emear
            show eml out
            with dissolve
            emelie " I get a little self-conscious about them... "
            me " Why?"
            show emeye side1 at right:
                yalign 0.15
                zoom 1.0
            show eml proper
            with dissolve
            emelie " My thighs are sort of bulging out at the top..."
            me " That's part of what I like!"
            hide emeye
            show emear high at right:
                yalign 0.15
                zoom 1.0
            show emf surprise
            with dissolve
            emelie " O-oh? Lucky me!"
            show emf smile with dissolve
            emelie " And lucky you, I guess!"
            show emf normalblush
            hide emear
            with dissolve
            emelie " You'll be painting me in them! "
            me " Yess!"




    show emear high at right:
        yalign 0.15
        zoom 1.0
    show eml out
    show emf smile at right:
        yalign 0.15
        zoom 1.0
    with dissolve
    emelie " But let's not wait around! "
    emelie "The lighting is ideal for another hour or so!"
    window hide
    play sound "audio/soundFX/Run2.wav"
    hide eml
    hide emear
    hide emf
    with easeoutleft
    window show
    " Then runs off to a stack of painting supplies."
    window hide
    play sound "audio/soundFX/Run2.wav"
    show eml paint at right:
        yalign 0.15
        zoom 1.0
    show emear high at right:
        yalign 0.15
        zoom 1.0
    with easeinleft
    pause 0.4
    window show
    emelie " Now take these painting tools and sit down on the chair and I'll strike a simple pose!"
    show emf normalblush at right:
        yalign 0.15
        zoom 1.0
    with dissolve
    emelie " I made sure to pick some appropriate colors out for you!"
    window hide
    show eml normal with dissolve
    pause 0.3
    play sound "audio/soundFX/Get.mp3"
    show blackopacity
    show canvaspainttools
    with dissolve
    window show
    " She hands me a stack of various blank canvases, as well as a brush and paint palette."
    emelie " I painted a little self-portrait too! So you can see how I used the colors!"
    me " That's really nice! "
    me " I'll try my best but... I'm not sure if you'll end up flattered!"
    window hide
    hide blackopacity
    hide canvaspainttools
    with dissolve
    show emf laugh
    show emear high at right:
        yalign 0.15
        zoom 1.0
    with dissolve
    pause 0.3
    window show
    emelie " Don't stress out so much about it! "
    emelie "There's no penalty for messing up!"
    show emf smile
    show eml hips
    with dissolve
    emelie " Now have a seat and I'll strike a pose!"
    emelie " You can rest the canvas in your lap as you paint. "
    show emf insecure
    hide emear
    show eml out
    with dissolve
    emelie "Painting on a vertical surface can feel a little unnatural when you're starting out so might as well keep it comfortable!"
    me " Okay sounds good!"
    stop music fadeout 2.0
    hide towerchair
    show emf normal
    with dissolve
    " She moves the little stool closer to me and I take a seat."
    window hide
    scene black with fade
    " Emelie sits down on the bed in front of me. "
    window hide

    jump posingstart

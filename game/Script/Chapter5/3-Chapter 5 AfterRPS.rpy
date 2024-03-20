label Gatebeach:
    window hide
    scene bg gate
    show blackshake at truecenter behind bg
    show perguard
    show larsguard
    show rolf base at right:
        zoom 1.0 yalign 0.25 xalign 1.50
    with fade
    pause 0.3
    window show
    play music "audio/9.+We+Are+Victorious+-+320bit.mp3"  volume 0.4 fadein 1.0
    " We arrive back at the gate I entered the city through a few days ago!"
    show rol calm at right:
        zoom 1.0 yalign 0.25 xalign 1.50
    with dissolve
    rolf " Well, here we are. "
    rolf "And right behind you is the beach-"
    window hide

    play sound "audio/soundFX/FX5/Sand_bonks_1.mp3"
    with vpunch
    pause 0.3
    with vpunch
    show rol surprise3 with dissolve
    pause 0.1
    with vpunch
    pause 0.5
    with vpunch
    pause 0.4
    window show
    #SoundOfRockHittingWood
    rolf " Ohh!"
    " I turn around to look toward the noise!"
    window hide

    show beachlynx with fade
    pause 1.0
    window show
    rolf " Would you look at that!?"
    rolf " A lynx from up north! "
    " A small, fluffy feline is securing his boat into the sand. "
    rolf " Looks like he came all this way by himself!"
    rolf " This could only mean one thing..."
    rolf " The \" Pig Pit \"!"
    me " ...Sweaty pits?"
    rolf " Not those pits, stupid. "
    rolf " These northern fellas are vicious lil' buggers. "
    rolf " No way is he here for some \"rest and recreation\" crap. "
    rolf " There's only one reason why he would've traveled all the way here on his own... And that's to test himself against some fresh bodies!"
    window hide
    hide beachlynx with fade
    pause 0.2
    show rol base
    show rol smiley
    with dissolve
    window show
    rolf " I can't wait!"
    show rol laugh
    show rolf belly
    with dissolve
    rolf " And Bronwen will be happy!"
    me " I hope you two have fun!"
    show rol surprise with dissolve
    rolf " !"
    show rolf sidewary
    show rol sidewary3 at right:
        zoom 1.0 yalign 0.25 xalign 1.50
    with dissolve
    rolf " I hope so too... We haven't spent a day together in so long."
    if liename == True:
        hide rol
        show rolf base
        with dissolve
        rolf " But now my patrol starts. I'll leave you to your business, \" [lie_name] \"! "
        play sound "audio/soundFX/FX2/pig-scream-loud-oink.wav"
        show rol angryz at right:
            zoom 1.0 yalign 0.25 xalign 1.50

        show rolf knuckles
        with dissolve
        with vpunch
        rolf "And stay out of trouble!"
    else:
        hide rol
        show rolf base
        with dissolve
        rolf " But now my patrol starts. I'll leave you to your business! "
        play sound "audio/soundFX/FX2/pig-scream-loud-oink.wav"
        show rol angryz at right:
            zoom 1.0 yalign 0.25 xalign 1.50
        show rolf knuckles
        with dissolve
        with vpunch
        rolf "And stay out of trouble!"
    window hide
    play sound "audio/soundFX/run2r.wav"
    hide rolf
    hide rol
    with easeoutright
    pause 0.2
    window show
    "Rolf lumbers off along the coast."
    window hide
    pause 0.4
    window show
    "Oh, that's Lars & Per by the gate!"
    " I give them a little nod."
    window hide
    hide perguard
    hide larsguard
    with dissolve
    show per sweat at center:
        zoom 0.9
        yalign 0.4 xalign 1.0

    show lars base at left:
        zoom 0.9
        yalign 0.4 xalign -0.4
    with dissolve
    pause 0.3
    window show

    lars " Mornin', [Protagonist]! "
    me " Heya, Lars!"
    show lars bigsmile
    show lareye right at left:
        zoom 0.9
        yalign 0.4 xalign -0.4
    with dissolve
    lars "You met Per?"
    show per smile with dissolve
    per" We've met. G'day to ya."
    me " I didn't know you also guard the gate from time to time, Lars."
    show lars base
    hide lareye
    with dissolve
    lars " I normally don't! "
    show lars bigsmile with dissolve
    lars "But this is a special day with people visiting and lots of festivities on the beach!"
    show lars concern with dissolve
    lars" So we make sure to really up the security, especially around the gates. "
    #Can't have anyone sneak in who might be up to no good!"
    me " I see!"
    show per sweat2 with dissolve
    per " Lars is lucky he doesn't have to endure this damn sun all day. Working in those cold marble halls is easy work..."
    show lars strange
    show lareye right at left:
        zoom 0.9
        yalign 0.4 xalign -0.4
    with dissolve
    lars " ...Always complaining about the damn weather..."
    show per base with dissolve
    per " Well..."
    show per smile with dissolve
    per  "At least today is a good day!"
    window hide
    show per smileside with dissolve
    show perblush at center:
        zoom 0.9
        yalign 0.4 xalign 1.0
    with dissolve
    window show

    "Per blushes and looks over toward the beach."
    window hide
    show hippobeach with fade
    play sound "audio/soundFX/FX5/catcall2.wav" volume 0.9
    with vpunch
    pause 0.5
    window show
    #Hippo
    per " What a beauty!"
    me " What is that?!"
    per " A woman, silly."
    me " S-sorry I mean... I've never seen anyone like that before!"
    lars " She's a hippo!"
    lars" They're from waaaay down south where it's warm all year round, apparently! "
    per " Imagine seeing ladies like THAT walk around on the beach all year!"
    per " Lucky bastards..."
    me " I see! I'd never heard of \"hippos\" before!"
    per " ...You need to go back to school."
    me " I never went to school..."
    hide perblush
    show per base
    window hide
    hide hippobeach with fade
    pause 0.5
    window show
    lars " Now don't be rude, Per. "
    hide lareye
    show lars bigsmile
    with dissolve
    lars "[Protagonist]'s a capable guy! "
    show lareye right at left:
        zoom 0.9
        yalign 0.4 xalign -0.4
    with dissolve
    lars "Guy went from being a farmer to being a royal assistant IN A DAY! "

    show lars base
    with dissolve
    lars "And you're stuck sweating your balls off on this post for what, ten years now? "
    hide lareye
    show lars laugh
    with dissolve
    lars "Haha!"
    $ renpy.music.set_volume(0.00, delay=0, channel='music')
    play sound "audio/soundFX/Pig Oink.wav"
    show per surprise:
        zoom 0.9
        yalign 0.4 xalign 1.0
        linear 0.2 yalign 0.4 xalign 1.15 zoom 1.0
    with hpunch
    per "Wha- He's a royal assistant?!"

    show per sweat2 at center:
        yalign 0.4 xalign 1.15 zoom 1.0
    with dissolve
    show per sweat2 at center:
        yalign 0.4 xalign 1.15 zoom 1.0
        linear 0.5 zoom 0.9 yalign 0.4 xalign 1.0
    pause 0.5
    show per sweat2 at center:
        zoom 0.9 yalign 0.4 xalign 1.0
    per " F-fine! But at least I know what a hippo is!"
    $ renpy.music.set_volume(0.10, delay=0, channel='music')
    pause 0.1
    $ renpy.music.set_volume(0.30, delay=0, channel='music')
    pause 0.1
    $ renpy.music.set_volume(0.50, delay=0, channel='music')
    pause 0.1
    $ renpy.music.set_volume(0.70, delay=0, channel='music')
    pause 0.1
    $ renpy.music.set_volume(1.00, delay=0, channel='music')
    show larsblush at left:
        zoom 0.9
        yalign 0.4 xalign -0.4
    show lars bigsmilez
    with dissolve
    lars " Wait 'til you see an elephant, [Protagonist]! "
    show per smilez
    show perblush at center:
        zoom 0.9
        yalign 0.4 xalign 1.0
    with dissolve
    per " Goddesses!"
    show lars laugh
    show larsblush
    show per biglaugh
    with dissolve
label RPSquest:
    "They both laugh."
    window hide
    menu:
        with dissolve

        "I've got a question before I leave... \n Did you guys ever play {size=+1}Rock, Paper, Scissors{/size} with Rolf?":
            window show
            me "I've got a question before I leave... Did you guys ever play rock, paper, scissors with Rolf?"

        "{alpha=*0.90}{size=-2}I should get going!":
            window show
            me " I should get going, people are waiting for me! "
            hide perblush
            show per base
            with dissolve
            per " Aight. Back to guardin' it is, then. You have a good one."
            hide larsblush
            show lars base
            with dissolve
            lars "Enjoy the beach, friend!"

            me " Nice speaking with you both! Byebye!"
            stop music fadeout 1.0

            jump BeachDay


    show lars concern
    hide perblush
    hide larsblush
    show per smile
    with dissolve
    " The mood changes."
    show lars think with dissolve
    lars " He did that to you too, huh? "
    window hide
    play sound "audio/soundFX/FX5/unsheathsoft.wav"
    show per hammer with dissolve
    pause 0.2
    window show
    per " Hehehee!"
    " Per looks awfully smug all of a sudden, with Lars looking sort of uncomfy."
    show lars strange with dissolve
    lars " I opened scissors..."
    if RPS == "Scissors":
        me " Yeah, me too..."
    window hide
    play sound "audio/soundFX/Glint2.wav" volume 0.8
    show per hammer2
    show perhammerstar at center:
        zoom 0.9
        yalign 0.4 xalign 1.0
    with dissolve
    with vpunch
    window show
    per " Hah! And I opened paper!"
    hide perhammerstar with dissolve
    show per apologetic
    with dissolve
    per " Then I lost by continuing to throw paper over and over again..."


    show per smile
    with dissolve
    per "  But Rolf he told me it's only the first move that matters! "
    show per smilez with dissolve
    per" And I made the perfect choice!"
    if RPS == "Paper":
        me " I opened paper too!"
        if playbestof3 == False:
            if RPS == "Paper":
                me " But we didn't continue after the first tie."
                per " Aha!"
        if playbestof3 == True:
            if RPS == "Paper":
                if RPSwin == True:
                    me " And then I won a best-of-three!"
                    per " Very impressive!"
                if RPSwin == False: #THIS CONNECTS TO BELOW BLOBLO
                    me " But then he beat me in a best-of-three..."
                    per " A shame, but like Rolf says, it's only the opener that matters!"
                    per "Aaaaaand..."
        show per hammer2 with dissolve
        per " That makes Lars the only non-warrior here!"
        show per smile with dissolve
        per " Heheh!"
    show lars pff
    show lareye ughright at left:
        zoom 0.9
        yalign 0.4 xalign -0.4
    with dissolve
    lars " Pff."
    if RPS == "Scissors":
        if playbestof3 == False:
            lars " At least we won the actual game, Per."
        else:
            lars " At least I won the actual game, Per."
    else:
        lars " At least I won the actual game, Per."

    hide lareye with dissolve

    if RPS == "Paper":
        lars " But then came the whole \"not a real warrior \" spiel."

    else:
        lars "But then he started roasting me for not being a warrior or something!"


    lars " At first I just thought he was being a bad loser..."
    show lars think
    show lareye ughright at left:
        zoom 0.9
        yalign 0.4 xalign -0.4
    with dissolve
    lars "But then I heard poor Billy got a big scolding for being a \"wimp who opened rock\"."
    lars " So there's some other crazy logic behind it. "
    if RPS == "Rock":
        me " I opened rock too... And then he called me weak!"
        show per hammer2
        with dissolve
        per " Guess I'm the only proper fighter in the group."
        show per smile with dissolve
        per " Hehehe!"
        lars " Shut up..."
        hide lareye with dissolve
        lars "But yeah, it makes no sense to me."
    else:
        lars "Makes no sense to me."
    play sound "audio/soundFX/FX5/unsheathsoft.wav" volume 0.8
    show per hammer2 with dissolve
    per " I definitely think Rolf is onto something. "
    per "I always knew I had all the traits to be a great warrior!"
    if RPS == "Rock":
        show lareye ughright at left:
            zoom 0.9
            yalign 0.4 xalign -0.4
        with dissolve

    lars " ... You haven't seen a real battle in your whole life..."
    show per sweat2 with dissolve
    per " Neither have you!"
    show lars closed with dissolve
    lars " Whatever, Per."
    me " Wait...I thought you guys were in the war?"

    stop music fadeout 3.0

    show lars concern
    hide lareye
    with dissolve
    lars " Me and Per were too young to serve when the fighting was at its peak."
    lars " We became soldiers right as the war was wrapping up. "
    lars "That was a little over twenty years ago."
    play music "audio/Birds.wav" fadein 3.0 volume 0.3
    show per apologetic with dissolve
    per " We didn't see any combat, just the aftermath."
    show lars sad with dissolve
    lars " A lot of horrible stuff... Destroyed villages and everything that comes with that."
    show per sweat with dissolve
    per " Carrying rations all day long was still a lot of work, though!"
    lars " Yeah... Even if it's not the type of work that springs to mind when someone talks about \" being a soldier in the war \" ..."
    lars "Felt good to help people get back to their feet, at least."
    show lars closed with dissolve
    lars " But seeing all the devastation and crippled soldiers made me question how I would've managed if I'd been born just a few years earlier..."
    show pereye sidee at center:
        zoom 0.9
        yalign 0.4 xalign 1.0
    show per sweat2
    with dissolve
    per " That's why we have to take Rolf's word with this \"warrior talk\", Lars!"
    per " Rolf was fighting for more than ten years before we joined in the war effort. He was in the real shit."
    stop music fadeout 1.0
    show lareye right at left:
        zoom 0.9
        yalign 0.4 xalign -0.4
    with dissolve
    lars " You're right..."
    " They both look sort of down all of a sudden."
    play music "audio/9.+We+Are+Victorious+-+320bit.mp3"  volume 0.3 fadein 1.0
    me " Battles or not, you should feel proud about the people you helped!"
    me " Someone had to carry all those rations and make them feel safe again!"
    hide lareye
    show lars concern
    with dissolve
    lars " Hmm... I suppose we should see it that way!"
    hide pereye
    show per base
    with dissolve
    per " True... "
    play sound "audio/soundFX/FX5/unsheathsoft.wav" volume 0.8
    show per hammer
    with dissolve
    per "But those wolves are lucky I wasn't born ten years earlier. Or they would've got a REAL good taste of my warrior spirit!"
    show lareye ughright at left:
        zoom 0.9
        yalign 0.4 xalign -0.4
    show lars think
    with dissolve
    lars "..."
    me "But now I've got to get going to the beach, guys! People are waiting for me! "
    show lars bigsmile
    hide lareye
    with dissolve
    lars " Alright, [Protagonist]! Enjoy the beach!"
    show per smile3 with dissolve
    per " See ya around! And have a good one."
    me " Nice catching up with you both!"
    stop music fadeout 1.0





label BeachDay:


    window hide
    scene black with fade
    window show
    "I turn around and take a stroll down the coast of the beach."
    window hide
    scene bg bigbeach
    show blackshake at truecenter behind bg
    show bgbeach1
    show bgbeachactive

    with fade
    play music "audio/beachlong.mp3" fadein 0.4 volume 0.37
    pause 0.5
    window show
    "Wow!"
    " A lot of people seem to be enjoying themselves here today!"
    "That giant lady to my left has got to be one of those elephants Per & Lars mentioned!"
    " She sure seems like the kinda woman they'd be into, judging by their appreciation for the hippo!"
    " I hear some rapid steps approach me from the left-"
    window hide
    play sound "audio/soundFX/run2.wav"
    show billys base at left:
        yalign 0.4 xalign -0.08
    with easeinleft
    pause 0.2
    show beachsmokebilly behind billys
    show billys laugh
    show bill laughface at left:
        yalign 0.4 xalign -0.08
    with dissolve
    window show

    billy " [Protagonist], you made it!!"
    me " Sure did!"
    " Billy is... still wearing his armor."
    " I don't know what I was expecting."
    me " Still in your full armor, eh?"
    show billys wary
    show bill sadface
    with dissolve
    billy " No! I feel kinda naked and exposed, actually!"
    me " ... What?"
    billy " I got rid of my shoulder pads and elbow armor! As well as my tabard!"
    show billys finger
    show bill baseface
    with dissolve
    billy " But safety first! My buoyancy is perfect now!"
    show bill hapiface
    show billys hips
    with dissolve
    billy " I can both float AND dive in this if I need to rescue someone!"
    me " I see! I'm sure the beach is much safer with you around!"
    me " And you're rocking those swimming trunks, too!"
    me " Looking good! "
    show billys laugh
    show bill laughface
    with dissolve
    billy " Heehee, that's so nice to hear! Thank you, buddy!"
    # billy " I fell asleep and it seems some piggies drew on me with crayons. I like it!"
    window hide
    play sound "audio/soundFX/run2.wav"
    show emeswim normal at right:
        yalign -0.15
        zoom 0.95
    with easeinright
    pause 0.2
    show beachsmokeemelie behind emeswim
    show emf crotch at right:
        zoom 0.95 yalign -0.15
    with dissolve
    window show

    emelie " Wow, and speaking of \" rocking swimming trunks \"!"
    show emear high at right:
        zoom 0.95 yalign -0.15
    show emf normalblush
    with dissolve
    emelie " You look stunning, [Protagonist]!"

    if modest == True:
        me "So do you! That blue looks great on you!"
        show emeswim out
        hide emear
        show emf smile at right:
            zoom 0.95 yalign -0.15
        with dissolve
        emelie " Thank you!"


    if modest == False:

        me "So do you! That bikini sure catches the eye!"
        show emeswim out
        hide emear
        show emf sooth at right:
            zoom 0.95 yalign -0.15
        show emblush at right:
            zoom 0.95 yalign -0.15
        with dissolve
        emelie " H-heh, thank you!"


    show emf biggersmile
    hide emblush
    with dissolve
    if modest == True:
        emelie " I really like this swimsuit too!"
    if modest == False:
        emelie " I really like this bikini too!"
    #or bikini depending on choice
    show emeswim bellu
    show emf gross
    with dissolve
    emelie " But did you really get a size larger than average for the bust?..."
    emelie " It's... a bit tight."
    me " Yeah, I did!"
    show emf surprise with dissolve
    if modest == True:
        emelie " I must've grown quite a bit since my last swimsuit then, jeez!"
    if modest == False:
        emelie " I must've grown quite a bit since my last bikini then, jeez!"
    show emf yeaa
    show emeswim hips
    with dissolve
    emelie " But maybe you like my clothes a bit tight?..."
    me "... I do!"
    window hide
    show emf normal
    show billys fists
    show bill hearteyes
    with dissolve
    with vpunch
    window show
    billy " You two are full of compliments today, huh? The beach sure brings out positive vibes!"
    show bill casualface with dissolve
    billy " Do you like the beach, [Protagonist]?"
    me " For sure! I bathe in the ocean a lot in the summer! It's very convenient since I live so close."
    me " There's also a lake a bit further away from my farm if I want something a bit more calm."
    show bill waa
    show billys hips
    with dissolve
    billy " Oh, I see!"
    show bill wary
    show billys belly
    with dissolve
    billy " W-wait, speaking of your farm... I just remembered something!"
    billy" You had a cart all filled up with veggies when I found you!"
    show bill squint
    with dissolve
    billy " They'll go bad soon if nobody tends to them!"
    me " Oh right! Unless someone's stolen them already... "
    show bill waa
    show billys belly
    with dissolve
    billy " We should go grab 'em!"
    #"Emelie looks a little concerned."
    me " Hmmm...But I have this new job now as an assistant, now! I don't think I need them!"
    show billys wary
    show bill cryy
    with dissolve
    billy " But they're so tastyyyy! I want to try them!"
    me " Haha! Not one to waste food are ya, Billy? Neither am I most of the time!"
    show billys fists
    show bill wary
    with dissolve
    billy " Can I... run and eat them all? "
    "Billy looks over to Emelie."
    show bill baseface
    show billys base
    with dissolve
    billy " Now that you're with your assistant I should be able to leave your side for a moment, right?"
    show emeye side1 at right:
        zoom 0.95 yalign -0.15
    show emeswim out
    show emf normalblush
    with dissolve
    emelie " Sure thing! Just make sure to come join us again when you're done!"
    show billys laugh
    show bill laughface
    with dissolve
    billy " Wohooo! "

    billy " I'll see you both later!"
    show bill drool
    show billys base
    with dissolve
    billy " You're the best, [Protagonist]!"
    #HighTen?
    " His mouth starts watering and he runs off."


    window hide

    hide beachsmokebilly with dissolve
    play sound "audio/soundFX/run2.wav"
    hide billys
    hide bill
    with easeoutleft
    pause 0.2
    hide emeye
    show emf laugh
    show emeswim hips
    show emear high at right:
        zoom 0.95 yalign -0.15
    with dissolve
    window show
    emelie " Haha, you're both such great friends! I'm glad. "
    show emf normalblush
    hide emear
    with dissolve
    emelie " Now let's take a walk down the beach and look around some!"
    window hide
    hide beachsmokeemelie with dissolve
    play sound "audio/soundFX/run.mp3"
    hide emeswim
    hide emf
    with easeoutright
    pause 0.3
    scene bg beach
    show blackshake at truecenter behind bg
    with fade
    show emeswim normal at right:
        yalign -0.15 xalign 0.7
        zoom 0.95
    with easeinleft
    pause 0.5
    window show
    show emeswim think
    show emf think at right:
        yalign -0.15 xalign 0.7
        zoom 0.95
    with dissolve
    emelie " Hmm..."
    show emeye normal at right:
        yalign -0.15 xalign 0.7
        zoom 0.95
    with dissolve
    emelie " Doesn't the sand feel warm against those \"toes\" on a day like this?"
    me " They do!"
    me " Y'know an interesting thing about toes is-"
    window hide
    with hpunch
    window show
    bron " {size=+3}Hey you two!{/size}"
    " I turn around!"

    #You take a walk around the beach. Bronwen shows up.
    window hide
    stop music fadeout 0.3
    play sound "audio/soundFX/Glint2.wav" volume 0.8
    play music "audio/Seagul.wav" fadein 1.0 volume 0.8
    show white with dissolve
    window show
    " Gah! I'm blinded! "
    window hide
    scene bronbod
    show blackshake at truecenter behind bronbod
    show bronbodglare
    with dissolve
    #play sound "audio/soundFX/Dun.wav" volume 0.3
    with hpunch
    pause 0.5
    window show
    "I rub my eyes and collect myself."
    me " That stings, damn! "
    window hide


    hide bronbodglare with dissolve


    pause 0.3
    window show
    " But maybe the pain is worth it for this view!"
    "Bronwen's cleavage is on full display at my eye level! "
    "I step back ."

    window hide
    hide bronbod
    scene bg beach
    show blackshake at truecenter behind bg
    #Bigger xalign for bronwen = more to the right

    show emeswim normal at right:
        yalign -0.15 xalign 0.8
        zoom 0.95
    with fade
    play music "audio/Blacksmith+-+320bit.mp3" fadein 1.0 volume 0.4
    pause 0.3
    play sound "audio/soundFX/run2.wav"
    show bronsw base at left:
        yalign -0.0 xalign -0.8
        zoom 0.9
    show bron pout at left:
        yalign -0.0 xalign -0.8
        zoom 0.9
    with easeinleft
    pause 0.3
    with dissolve

    window show
    bron " Whoops. Sorry for blinding ya."
    me "  I-It's okay. Hello again!"
    show emf biggersmile at right:
        yalign -0.15 xalign 0.8
        zoom 0.95
    show emeye side1 at right:
        yalign -0.15 xalign 0.8
        zoom 0.95
    show emeswim hips
    with dissolve
    emelie " Oh hey, Bronwen!"
    show bron huhh
    show broneye lookright2 at left:
        yalign -0.0 xalign -0.8
        zoom 0.9
    with dissolve
    bron " Hey, Em!"
    hide broneye with dissolve
    bron " I couldn't find a proper swimsuit so had to throw something together myself."
    hide bron
    show bronsw hips
    with dissolve
    bron " Didn't consider the whole sun-reflection-thing..."
    show emeye down4b at right:
        yalign -0.15 xalign 0.8
        zoom 0.95
    show emear high at right:
        yalign -0.15 xalign 0.8
        zoom 0.95
    show emf surprise2
    with dissolve
    emelie " Wha- You made it yourself? "

    show bron grin behind broneye at left:
        yalign -0.0 xalign -0.8
        zoom 0.9
    show broneye lookright2 at left:
        yalign -0.0 xalign -0.8
        zoom 0.9
    with dissolve
    bron " Yea."
    show emf biggersmile
    show emeye side1
    with dissolve
    emelie "Wow! Very pretty! Your skills always impress!"

    show emf sooth
    show emblush at right:
        yalign -0.15 xalign 0.8
        zoom 0.95
    hide emear
    with dissolve
    emelie " And thank you so much for making the plug-"
    window hide
    show emeye side3
    show emf panic
    show emeswim out
    show emear high at right:
        yalign -0.15 xalign 0.8
        zoom 0.95
    with dissolve
    $ renpy.music.set_volume(0.70, delay=0, channel='music')
    pause 0.2
    $ renpy.music.set_volume(0.40, delay=0, channel='music')
    pause 0.2
    $ renpy.music.set_volume(0.0, delay=0, channel='music')
    play sound "audio/soundFX/Dun.wav" volume 0.7
    with vpunch
    window show
    emelie " Uuuuuhhh..."

    show bron hehh behind broneye at left:
        yalign -0.0 xalign -0.8
        zoom 0.9
    show broneye lookright2b at left:
        yalign -0.0 xalign -0.8
        zoom 0.9
    show bronsw base
    with dissolve
    "Bronwen grins. "
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
    show bron smilee with dissolve
    bron " No worries."

    bron " Your swimsuit looks good too, Em!"
    show emf insecure
    show emeye side1 behind emblush at right:
        yalign -0.15 xalign 0.8
        zoom 0.95
    hide emear
    with dissolve
    emelie " Thank you!"
    show bron bigsmile with dissolve
    if modest == False:
        bron " A lil' slutty maybe..." #If wearing melon bikini.
    else:
        bron " A lil' tight around the tits maybe..."

    hide broneye
    show bronsw hips
    show bron laugh
    with dissolve
    bron " But I like that."
    " Whew, Bronwen really doesn't speak softly around the princess."
    " But If I remember correctly, Emelie told me Rolf and the king are best friends! "
    " So I imagine they've spent lots of time together when growing up."
    show emf normalblush
    show emeswim bellu
    with dissolve
    emelie " T-thank you... I think..."
    show broneye lookright2 at left:
        yalign -0.0 xalign -0.8
        zoom 0.9
    show bron done
    with dissolve
    bron " Now don't forget to get some lotion or something for your skin today, Em."
    show bronsw think
    hide bron
    with dissolve
    bron " I remember a few years ago when you fell asleep in the sun... "
    show bron laugh at left:
        yalign -0.0 xalign -0.8
        zoom 0.9
    show bronsw base behind emeswim , emelon
    hide broneye
    with dissolve
    bron "And you had to spend the whole summer creeping around in the shadows! Hahah! "
    hide emeye
    show emeswim panic
    show emf panic2
    hide emblush
    with dissolve
    with hpunch
    emelie " Oh crap, right! I forgot! "
    show emf panic with dissolve
    emelie " I got sunburnt so bad I turned red like a tomato."
    show emf sad
    show emeswim out
    with dissolve
    emelie " It was awful! "
    show emf surprise

    with dissolve
    emelie" I'll run and grab something right away! Be back real soon!"
    window hide
    play sound "audio/soundFX/run2.wav"
    hide emf
    hide emeswim
    hide emelon
    with easeoutright
    window show
    "I give Emelie a little wave as she hurries off."
    stop music fadeout 1.0
    hide broneye
    show bron done
    with dissolve
    bron "..."
    play music "audio/Seagul.wav" fadein 1.0 volume 1.0
    " Bron gives me a snide look. "
    me " ...What?"
    show bronsw knuckles
    show bron donefor2
    with dissolve
    bron " You're a real degenerate, you know that?"
    me " Where did that come from?!"
    bron " Emelie thanked me for my work... "
    bron "And she's walking reaaaally funny today..."
    me "Uuuuuuh..."
    "Shit! She's found us out!"
    show bron grin
    show bronsw hips
    with dissolve
    bron " But that's all good. Especially after that generous tip earlier!"
    me " Okay, okay... Just don't speak too openly about it, please!"
    show bronsw base
    show bron baseface
    with dissolve
    bron " I'm not one to gossip."
    show bron bigsmile with dissolve
    bron " And this is a very lucrative arrangement for me!"
    show bron donefor2
    show bronsw knuckles
    with dissolve
    bron " What makes you a big degenerate though is that even after dicking down the princess, you're still staring down every damn lady you see on this beach!"
    # play sound "audio/soundFX/Dun.wav" volume 0.7
    with vpunch
    "...Is it that obvious?!"
    me " I... That's not true!"
    show bron done
    show bronsw base
    with dissolve
    bron " It is, don't bullshit me."
    me "..."
    show bronsw think
    hide bron
    with dissolve
    bron " But all that is to be expected from a guy like you, suddenly making big moves in life and getting some attention from gals..."
    bron " Just keep your expectations in check, [Protagonist]. "
    show bron pull at left:
        yalign -0.0 xalign -0.8
        zoom 0.9
    with dissolve
    bron "Most of the chicks you see on this beach will only be here today."
    bron " So have fun staring, but try not to get too disappointed when they leave."
    me " O-okay."
    " Bronwen makes a good point... Even if I wanted to, trying to make moves on all these beach girls would be a waste of time. "
    " If I want to build closer relationships with people I have to focus on the citizens of Hog Haven! "
    " Like Emelie, Victoria, Maple & Bronwen herself!"
    me " Staring it is."
    show bronsw base
    show bron baseface
    with dissolve
    bron " Mhm."
    #"..."
    #" And can't forget my best bud Billy."

label ilves:
    play music "audio/beachlong2.mp3" fadein 0.4 volume 0.37 loop
    $ cat_name = "???"
    #Cat shows up
    window hide
    pause 0.2
    play sound "audio/soundFX/run2.wav"
    show ilv base at right:
        yalign 10.2 zoom 0.80
    with easeinright
    pause 0.3
    show ilveye bigup at right:
        yalign 10.2 zoom 0.80
    with dissolve
    window show
    cat " Hello, madame! "
    hide ilveye
    show ilvouth smile at right:
        yalign 10.2 zoom 0.80
    with dissolve
    cat "And mister!"
    " The lynx Rolf spoke about earlier shows up! He's almost a head shorter than Emelie."
    me " Hello!"
    show broneye lookright2 at left:
        yalign -0.0 xalign -0.8
        zoom 0.9
    show bron bigsmile
    show bron hips
    with dissolve
    bron " Well, hey there."
    show ilv basegrin
    hide ilvouth
    show ilveye bigup at right:
        yalign 10.2 zoom 0.80
    with dissolve
    " His eyes glisten & he looks back up at Bronwen with a wide smile "
    show bron done
    show bronsw hips
    with dissolve
    bron " Speaking of staring..."
    show ilv lookup
    hide ilveye
    show ilvblush at right:
        yalign 10.2 zoom 0.80
    with dissolve
    cat " O-oh I apologize-"
    $ cat_name = "Ilves"
    show ilv close
    hide ilvblush
    with dissolve
    cat " The name is Ilves!"
    show bronsw base
    show bron grin
    with dissolve
    bron " I'm Bronwen."
    me " And I'm [Protagonist]!"
    show ilv bigsmile with dissolve
    cat " Nice to meet you two!"
    show ilv basehips
    show ilveye up at right:
        yalign 10.2 zoom 0.80
    with dissolve
    cat " I came by because... Well... "
    show ilv grabby
    hide ilveye
    with dissolve
    cat "You look really, really powerful! "
    show bronsw think behind bron
    hide bron
    with dissolve
    bron "Powerful, huh? "
    window hide
    play sound "audio/soundFX/FX3/postit.wav" volume 0.5
    show ilv grabby2 with dissolve
    show ilv draw1b with dissolve
    pause 0.2
    window show
    cat " Yes! And I was wondering if I could draw you real quick?"
    " Another dang artist."
    show bron pull behind broneye at left:
        yalign -0.0 xalign -0.8
        zoom 0.9
    with dissolve
    bron "Sure, why not. But be quick!"

    cat " Yes yes!"
    show ilvouth openn at right:
        yalign 10.2 zoom 0.80
    show ilveye bigup2 at right:
        yalign 10.2 zoom 0.80
    with dissolve
    cat " Now strike a strong pose!"
    window hide
    show bronsw flex
    show bron pout at left:
        yalign -0.0 xalign -0.8
        zoom 0.9
    show broneye lookright2b at left:
        yalign -0.0 xalign -0.8
        zoom 0.9
    with dissolve
    #play sound "audio/soundFX/Dun.wav" volume 0.7
    with vpunch
    pause 0.2
    window show

    "Bronwen flexes."
    hide ilvouth with dissolve
    cat " P-Purrfect!"
    hide ilveye
    show ilv draw1
    with dissolve
    play sound "audio/soundFX/FX3/scribble.wav"
    " He starts quickly drawing on the paper with what looks like some type of crayon."
    cat "I like to draw things on my travels."
    show ilvouth smile at right:
        yalign 10.2 zoom 0.80
    show ilveye downsquint at right:
        yalign 10.2 zoom 0.80
    with dissolve
    cat " Memories I can show the kittens back home."
    me " Aw, that's nice."
    show ilv grabby2
    show ilvouth openn at right:
        yalign 10.2 zoom 0.80
    show ilveye bigup2 at right:
        yalign 10.2 zoom 0.80
    with dissolve
    cat " Great posing!  Very strong!"
    show ilv draw2
    hide ilveye
    show ilvouth smile
    with dissolve
    cat " Now hold it just ooone more minute!"
    play sound "audio/soundFX/FX3/scribble.wav"
    " He continues scribbling at a fast pace, switching between a few different colored crayons."
    show ilv draw4
    show ilveye up at right:
        yalign 10.2 zoom 0.80
    with dissolve
    cat " Aaaand I'm done!"
    show bronsw hips
    show bron hehh
    with dissolve
    bron " Can I see? Did ya depict me like some slut?"
    hide ilveye
    show ilv draw3b
    hide ilvouth
    with dissolve
    cat " Some slu- "
    cat "No, absolutely not!! "
    show ilv draw4b
    with dissolve
    cat " You look like a magnificent warrior! The most muscles I've ever seen on a woman! "
    cat "This art will surely inspire my daughters when they see it!"
    show bron grin with dissolve
    bron " O-oh..."
    cat " Have a look!"
    window hide
    show ilv basehips
    show ilveye bigup at right:
        yalign 10.2 zoom 0.80
    with dissolve
#    "Bronwen looks at the art "
    play sound "audio/soundFX/Get.mp3"
    show bronsw artlook
    show bron grin2
    show broneye lookdown
    with dissolve
    pause 0.2
    show bron bigoo
    show broneye lookdownopen
    with dissolve
    play sound "audio/soundFX/Dun.wav" volume 0.4
    with vpunch
    window show
    bron " What the shit?! "
    show ilv lookup2
    hide ilveye
    with dissolve
    cat " ??"
    show bron grin2 with dissolve
    bron " This is incredible!"
    show broneye lookright2b at left:
        yalign -0.0 xalign -0.8
        zoom 0.9
    with dissolve
    bron "I kinda wanna keep this... If you finish my abs!"
    show ilv uphapi
    hide ilvvouth
    with dissolve
    cat "No can do! And I may unfortunately have to draw over the abs later. "
    cat "I'm saving some space on the paper for one final big memory!"
    show bron smilee with dissolve
    bron " Aha, I see!"
    window hide
    show bronsw base with dissolve
    play sound "audio/soundFX/Get.mp3"
    show ilv draw3
    show ilvouth smile at right:
        yalign 10.2 zoom 0.80
    show ilveye bigup at right:
        yalign 10.2 zoom 0.80
    with dissolve
    window show
    "Bron hands the drawing back." # Draw Ilv with hand on one hip and drawing in the other.
    show bron bigsmile
    show bronsw hips
    with dissolve
    bron " I hope Hog Haven gives ya plenty of great memories."
    show ilv draw4c
    hide ilveye
    hide ilvouth
    with dissolve
    cat " Thank you, miss!"
    show ilv draw3
    show ilvouth smile at right:
        yalign 10.2 zoom 0.80
    with dissolve

    cat " Do you want a look too, sir?"
    " He's so polite."
    me " Yes!"

    window hide
    show ilv base with dissolve
    pause 0.2
    show blackopacity with dissolve
    show hoghaven1tex with dissolve
    play sound "audio/soundFX/Get.mp3"
    with vpunch
    pause 0.6
    window show
    " ... WHAT?"
    me " You made this with a few crayons in minutes!?"
    " This makes me feel real bad about my figure-drawing efforts yesterday..."
    cat " When you're huddled up in the northern snow you don't have a lot of ways to pass the time. So I picked up drawing as a hobby!"
    me " It's incredible! "
    cat " Thank you, thank you. "
    " Bronwen looks amazing."
    #me " How did you get so fast?"
    #cat " You need to be quick when you're my size!"
    #cat" I imagine it carried over to my other hobbies too!"
    #me " That makes some sense."
    cat "I believe I've had good luck with my choice of models too! "
    cat " The citizens of Hog Haven seem very accommodating!"
    bron "Hmm not always... But you did catch me in a good mood."
    me " I've actually only spent a few days in Hog Haven myself!"
    cat " I see!"
    me" Have you had a chance to see the city yet?"

    bron " ... I don't think he'd be allowed inside the gates."
    me "O-oh right."
    me " Sorry, I forgot the city is a bit hesitant with letting new people in."
    " I hand the paper back to him. "
    window hide
    hide hoghaven1tex
    hide blackopacity
    with dissolve
    pause 0.1
    play sound "audio/soundFX/Get.mp3"
    show ilv draw3 with dissolve
    pause 0.3
    window show

    cat " No worries, lad!"
    " He rolls his paper up and pockets it."
    show ilv close
    hide ilvouth
    with dissolve
    cat "It's true... I wasn't allowed entry."
    cat" I tried to smooth-talk the guards but they told me off right away. "
    show ilveye up at right:
        yalign 10.2 zoom 0.80
    with dissolve
    cat "You sure keep your security high!"
    show bron cooldown
    show bronsw base
    hide broneye
    with dissolve
    bron " Yeaaah... It's a bit much. "
    show ilvouth smile at right:
        yalign 10.2 zoom 0.80
    show ilveye bigup2
    with dissolve
    cat " At least they were nice enough about it!"
    cat " I asked one of the guards if he could pull his visor down for a quick sketch and he did! "
    #" If it wasn't for the weapon I might've mistaken the guard for Billy!"
    show ilv laugh
    hide ilveye
    hide ilvouth
    with dissolve
    cat " Your guard armor is so bulky and cool! "
    show ilv basegrin
    show ilveye bigup at right:
        yalign 10.2 zoom 0.80
    with dissolve
    cat "And very well crafted! "
    #"Bronwen smiles with a slight blush."
    #"Oh right- She's probably responsible for a lot of the armor being a smith and all!"
    #"And Billy is in his swimming trunks today!"
    show bron apologetic at left:
        yalign -0.0 xalign -0.8
        zoom 0.9
    show broneye lookright2 at left:
        yalign -0.0 xalign -0.8
        zoom 0.9
    with dissolve
    bron " It's a shame you weren't allowed entry. "
    bron "I'm sure you were looking to take in more than just the fortified outer gates..."
    #me " That's unfortunate. Travelling so far and not being allowed entry into the city!"
    show ilv bigsmile
    show ilveye bigup2 at right:
        yalign 10.2 zoom 0.80
    with dissolve
    cat " Actually... I kind of expected to be turned away!"
    me " Oh?"
    show ilv basegrin
    hide ilveye
    with dissolve
    cat " I go on a short vacation every year, you see. With the goal of testing myself in combat against opponents all over the world!" #across the world?
    show ilv surprise
    show ilvouth smile at right:
        yalign 10.2 zoom 0.80
    with dissolve
    cat " And the fighting pit of Hog Haven is my destination this year!"
    show bron bigsmile with dissolve
    bron " Really?!" #:D
    show ilv bigsmile
    hide ilvouth
    show ilveye up at right:
        yalign 10.2 zoom 0.80

    with dissolve
    cat "The \" Pig Pit \" has an open weight bracket. So I signed up to that in hopes of a good challenge!"
    cat " I hear it takes place out here somewhere on the beach!"
    show bron laugh
    hide broneye
    show bronsw hips
    with dissolve
    bron " That's right, it does! Exciting!"
    me " Ooooh!"



    show ilv laugh
    hide ilveye
    with dissolve
    cat " Yess!"
    show ilv basegrin with dissolve
    cat " But now I have to get going. "
    show ilv grin with dissolve
    cat " 'Will spend some time scouting out all the other competitors before it's my turn. Hehehee."
    #" He lets out a mischievous little chuckle. "
    show bronsw knuckles
    show bron grin2
    show broneye lookright2b at left:
        yalign -0.0 xalign -0.8
        zoom 0.9
    with dissolve
    bron " Good luck! I'll be sure to check it out later and root for ya!"
    me " Yes! Good luck!"
    window hide
    show ilv basegrin with dissolve
    pause 0.2
    play sound "audio/soundFX/run2.wav"
    stop music fadeout 3.0
    hide ilv with easeoutright
    show bron laugh
    hide broneye
    with dissolve
    window show
    "He scurries away, joyous to have met us."
    me " What an interesting little guy!"
    play music "audio/Seagul.wav" fadein 2.0 volume 0.8
    hide bron
    show bronsw base
    with dissolve
    show bronsw at left:
        linear 0.5 yalign -0.0 xalign -11.5
        zoom 0.9
    pause 0.5
    show bronsw at left:
        yalign -0.0 xalign -11.5
        zoom 0.9
    bron "..."
    show bron biggersmilez at left:
        yalign -0.0 xalign -11.5
        zoom 0.9
    with dissolve
    bron "He called me a warrior."
    show bron rightlook
    show bronsw behindd
    show bronblush at left:
        yalign -0.0 xalign -11.5
        zoom 0.9
    with dissolve
    bron "I've never been called that before!"
    me " Really? You're on the beach with the option to wear anything you want, and you choose to wear steel! "
    me "The term definitely suits you!"
    play music "audio/Tavern+Brawl+-+320bit.mp3" fadein 4.0 volume 0.3
    show bron laugh with dissolve
    bron " Hah, when you put it like that! "
    bron "I just threw it together with the materials I had available."
    show bron apologetic
    hide bronblush
    with dissolve
    bron " Thing is, Hog Haven doesn't really have a program for women to become warriors or even guards. "
    show bron cooldown
    show bronsw hips
    with dissolve
    bron "Kinda shitty if ya ask me. I could easily beat most of our plump little guards up. "
    me " Huh, I definitely believe that!"
    me " Do you think you'd pursue work in the military if you could?"
    show bron baseface with dissolve
    bron " Probably. "
    bron "I'm from a military family after all, and dad taught me how to handle weapons at an early age. "
    show bronsw knuckles
    show bron hehh
    with dissolve
    bron "And I quickly learned how to get a good bash in with the hammer!"
    show bronsw hips
    show bron baseface2
    with dissolve
    bron" 'Guess that's what led me down the path of being a smith... "
    show bronsw fist
    show bron shady
    with dissolve
    bron " Beating the shit out of some steel gets a bit of aggression out!"
    " She still seemed plenty pissed when I first met her yesterday..."
    show bron rightlook
    show bronsw hips
    with dissolve
    bron " But I don't really think I'm needed in the force these days anyways. "
    show bron bigsmile with dissolve
    bron "Cousin Billy is out there keeping the streets clean!"
    show bron laugh with dissolve
    bron " Hahaha!"
    " We both laugh."
    #Menu: Ask about billy's guarding skills.
    show bron smile
    show bronsw base
    with dissolve
    bron " Billy might not be very tough... But he's actually a really great guard."
    show bron concern
    show bronsw hips
    with dissolve
    bron " Some guards like my dad are good at ensuring crime doesn't happen. But he's terrible at making people feel safe."
    me " Isn't that the truth..."
    show bron baseface2 with dissolve
    bron " Billy is kinda the opposite. "
    bron "He helps older piggies with their groceries, cheers sad people up and is good at sorting heated arguments out in the street."
    show bron smile with dissolve
    bron " And that's what being a guard in Hog Haven is mostly about anyways. Crime is really low these days!"
    show bron pout with dissolve
    bron " But when shit goes down, having someone like my dad around is definitely a good thing."
    show bronsw hips
    show bron laugh
    with dissolve
    bron " And he's a surprisingly good detective, haha! "
    show bron smile with dissolve
    bron "You should see how he gets when working a case!"
    #Could see Rolf has totally figured out the player has been banging Protag later. like a funny big board with lines and his drawings etc. making notes like " suspicious liquid on face? Bulge in pants? Hmm. But kind attitude and Emelie seemed calm. "
    me " He sure has his interrogations down to a science!"
    show bron laugh with dissolve
    bron " Haha, yeah."
    hide bron
    with dissolve
    bron " Now all he needs to do is stop interrogating my customers!"
    " I hear steps approaching from the left!-"
    window hide
    play sound "audio/soundFX/run2.wav"

    show maps basec:
        xoffset -200 yoffset 35
    with easeinleft
    window show
    maple "H-hey hey you two-" # {p=0.2}{nw}
    window hide
    show bronsuitglare at left:
        yalign -0.0 xalign -11.5
        zoom 0.9
    with dissolve

    show maps blinded with dissolve
    $ renpy.music.set_volume(0.80, delay=0, channel='music')
    pause 0.1
    $ renpy.music.set_volume(0.60, delay=0, channel='music')
    pause 0.1
    $ renpy.music.set_volume(0.40, delay=0, channel='music')
    pause 0.1
    $ renpy.music.set_volume(0.20, delay=0, channel='music')
    pause 0.1
    $ renpy.music.set_volume(0.00, delay=0, channel='music')
    play sound "audio/soundFX/Glint2.wav" volume 0.8
    show white with dissolve
    show maps blinded2
    hide white with dissolve
    pause 0.3
    window show
    with vpunch
    maple " Ghaa!"
    hide bronsuitglare with dissolve
    " Maple got blinded too!"
    window hide
    show bronsw snide with dissolve
    show bronsw snide:
        linear 0.5 xoffset 310
    pause 0.5
    show bronsw snide:
        xoffset 310
    show bronsw snide with dissolve
    window show
    bron " Oh hey, Maple!"
    $ renpy.music.set_volume(0.20, delay=0, channel='music')
    pause 0.1
    $ renpy.music.set_volume(0.40, delay=0, channel='music')
    pause 0.1
    $ renpy.music.set_volume(0.60, delay=0, channel='music')
    pause 0.1
    $ renpy.music.set_volume(0.80, delay=0, channel='music')
    pause 0.1
    $ renpy.music.set_volume(1.00, delay=0, channel='music')
    bron " Sorry about that."
    window hide
    show maps basez with dissolve
    pause 0.3
    show maps basez:
        linear 0.5 xoffset 90 yoffset 35
    pause 0.5
    show maps basez:
        xoffset 90 yoffset 35
    show mapnipcover:
        xoffset 90 yoffset 35

    show maf lookright:
        xoffset 90 yoffset 35
    with dissolve
    window show
    maple " It's okay !"
    show maf shy
    show maps out
    show mapeye right:
        xoffset 90 yoffset 35
    with dissolve
    maple " But jeez, to think I made this cap to keep the sun out of my eyes only for your bikini to beam it right up in there-"
    hide mapeye
    show maf happydown2
    show maps cheerupc
    hide mapnipcover
    with dissolve
    with vpunch
    maple " WOAA!"
    with hpunch
    maple " Oh my god, that STEEL BIKINI!"
    show mapeye right2:
        xoffset 90 yoffset 35
    with dissolve
    maple " This is AMAZING STUFF, BRONNIE!"
    " Bronnie?"
    show bron smile behind broneye at left:
        yalign -0.0 xalign -11.5
        zoom 0.9 xoffset 310
    show bronsw base
    show broneye lookleft at left:
        yalign -0.0 xalign -11.5
        zoom 0.9 xoffset 310
    with dissolve
    bron " You're looking hot today yourself."
    show maf shy
    show maps out
    show mapnipcover:
        xoffset 90 yoffset 35
    with dissolve
    maple " Gosh, never get into fashion, hun. Or you'll put me out of business! "
    show maf hapigrin
    with dissolve
    maple "Maybe I'll take some inspiration from it and make a few designs myself!"
    show mapeye down
    show maps tidc
    hide mapnipcover
    with dissolve
    maple " But first I'm gonna need you to make me a batch of those scales or whatever they are! "
    hide bron
    show bronsw think at left:
        yalign -0.0 xalign -11.5
        zoom 0.9
        xoffset 310
    show broneye lookleft at left:
        yalign -0.0 xalign -11.5
        zoom 0.9
        xoffset 310
    with dissolve
    bron " Of course. If ya pay up. "
    play sound "audio/soundFX/FX5/ding.wav" volume 0.2
    show mapeye rightwink
    show maps peacehighc
    with dissolve
    maple " Haha, you know I always doo!~ "
    " Maple throws Bronwen a flirtatious wink."
    me " ...You two seem like good friends!"
    hide mapeye
    show maps base
    show mapnipcover:
        xoffset 90 yoffset 35
    show maf biggrintongue
    with dissolve
    maple " Yes! And work associates since our shops are on the same street!  "
    show bron pull behind broneye at left:
        yalign -0.0 xalign -11.5
        zoom 0.9
        xoffset 310
    with dissolve
    bron " Mhm."
    show maf biggrinz with dissolve
    maple " Wen-wen works all dang day, though... "

    "Wen-Wen? Maple sure likes nicknames."
    show maf hmm
    hide mapnipcover
    show mapeye right:
        xoffset 90 yoffset 35
    show maps tiddownc
    with dissolve
    maple "And she gets all pissy when I disturb her."

    me "Yeah, she sure hates interruptions..."
    show bron cooldown
    show bronsw hips
    hide broneye
    with dissolve
    bron " Pff. I'm on a tight schedule."
    show bron done with dissolve
    bron " But whenever Maple needs a batch of belt buckles or whatever she hits me up. "
    show bron pout with dissolve
    bron "And she usually has some fabric I can use for tabards or weapon threads or whatever."
    show maf closeyes
    hide mapeye
    show maps out
    show mapnipcover:
        xoffset 90 yoffset 35
    with dissolve
    maple " Exactly! We do some trading like that!"
    me " Oh, that sounds like a good arrangement!"
    show maf biggrin with dissolve
    maple " For sure."
    show broneye lookleftb at left:
        yalign -0.0 xalign -11.5
        zoom 0.9
        xoffset 310
    show bronsw base
    show bron base
    with dissolve
    bron " But hey, you two. I think I'll go find my dad. He should be here somewhere. "
    show bron smile
    show bronsw knuckles
    hide broneye
    with dissolve
    bron "Gotta get some good seats for the Pig Pit! I hope that lil' cat does well."
    show mapeye right:
        xoffset 90 yoffset 35
    show maf opensmile2
    show maps back
    with dissolve
    maple " Okay! You two enjoy yourselves!"
    me " Have fun, Bronwen!"
    window hide
    play sound "audio/soundFX/run2.wav"
    hide bronsw
    hide broneye
    hide bron
    with easeoutright
    pause 0.2
    hide mapeye
    hide maf
    with dissolve
    window show
    "Bronwen gives us a nod and walks off."





    show maps basez
    hide mapnipcover
    with dissolve
    show maps basez:
        linear 0.5 xoffset 150 yoffset 15
    pause 0.5
    show maps basez:
        xoffset 150 yoffset 15
    show maf biggrin:
        xoffset 150 yoffset 15
    with dissolve
    maple " So... do you like my bikini? "
    me " Yeah, it looks great!"
    #Menu
    me "Pretty daring."


    show maf closeyes with dissolve
    maple "Yeah, I know...  Sexy, huh? "

    window hide
    play sound "audio/soundFX/run2.wav"
    show emeswim normal at right:
        yalign -0.20 xalign 0.80
        zoom 0.95
    with easeinright
    with hpunch
    play sound "audio/soundFX/FX3/clean-record-scratch.wav" volume 0.5
    show emf weirdo2 at right:
        yalign -0.20 xalign 0.80
        zoom 0.95
    show emeswim out
    with dissolve
    window show
    emelie " W-what are you two talking about?" #<o<
    me " Welcome back!-"
    show mapeye down:
        xoffset 150 yoffset 15
    show maf biggrin:
        xoffset 150 yoffset 15
    show maps out:
        xoffset 150 yoffset 15
    show mapnipcover:
        xoffset 150 yoffset 15
    with dissolve

    maple " Oh hey there! I don't think we've met!"
    maple " My name is-"
    show emf fluster at right:
        yalign -0.20 xalign 0.80
        zoom 0.95
    show emeye maple at right:
        yalign -0.20 xalign 0.80
        zoom 0.95
    with dissolve
    emelie " We've met lots of times before, Maple!"
    emelie "It's me, Emelie!"
    window hide
    show maps
    show maf ofoa

    show maps cheerc
    hide mapnipcover
    show mapeye downopen
    with dissolve
    play sound "audio/soundFX/Dun.wav" volume 0.7
    with vpunch
    window show
    maple " !!"
    if modest == True:
        maple " Wha- I didn't recognize you without your crown and in that casual swimsui-"
    else:
        maple " Wha- I didn't recognize you without your crown and in that skimpy bikin-"
    show maf fardown2
    show maps out
    show mapnipcover:
        xoffset 150 yoffset 15
    with dissolve
    play sound "audio/soundFX/Dun.wav" volume 0.7
    with hpunch
    maple " Wait, I made that!!"
    show maf fardown3
    show mapeye downopenb
    with dissolve
    maple " The princess is wearing a swimsuit I made?! "
#    maple " So Emelie's who you bought it for, Protag!"
    #me " Yes! "
    "Maple looks completely taken aback!"
    hide mapeye
    show maf shy
    show maps cheerc
    hide mapnipcover
    with dissolve
    maple " Jeez!  I would've sprinkled some gold on it or something if I knew!"
    show emf biggersmile
    show emeswim hips
    show emeye maple2
    show emear high at right:
        yalign -0.20 xalign 0.80
        zoom 0.95
    with dissolve
    emelie " Haha! I really love it, Maple! "
    hide emeye
    show emf insecure
    show emeswim bellu
    hide emear
    with dissolve
    emelie " But I think I picked a size too small 'cus my boobs are kinda falling out..."
    show maps thinking2
    hide maf
    show mapeye down:
        xoffset 150 yoffset 15
    hide mapnipcover
    with dissolve
    maple " Hmmm... What you're wearing right there is a pig-size-twenty around the bust."
    show emeswim panic
    show emeye maple at right:
        yalign -0.20 xalign 0.80
        zoom 0.95
    show emf panic
    show emear high at right:
        yalign -0.20 xalign 0.80
        zoom 0.95
    with dissolve
    emelie " Really?! Gosh, then it IS the same size as my previous one..."
    show emeye maple2 at right:
        yalign -0.20 xalign 0.80
        zoom 0.95
    show emf panic2
    with dissolve
    emelie " That means my bust must've grown since my last purchase!!"
    show maf closeyes :
        xoffset 150 yoffset 15
    show maps out
    hide mapeye
    show mapnipcover:
        xoffset 150 yoffset 15
    with dissolve
    maple" Haha, yeah you could've probably gone for a size or two larger!"
    show emf insecure
    show emeswim out
    hide emear
    with dissolve
    emelie " That's what I get for not testing it out myself first, huh? That's a little embarrassing..."
    show maf grin
    show mapeye down:
        xoffset 150 yoffset 15
    with dissolve
    maple " Oh hush, the smaller size is hot! "
    maple "I always wear a size or two smaller than I should myself! It's sexy!"
    show maps tidc
    show maf insecure
    hide mapnipcover
    with dissolve
    maple " A little uncomfortable sometimes maybe, but... "
    show maf lookbod2
    show mapeye close
    with dissolve
    maple "A little bit of restraint is something you learn to love quick~"
    "... What the hell does that mean?"
    show emf smile
    show emeswim out
    with dissolve
    emelie " I'll take your word for it, Maple!"
    show emf normalblush
    show emeswim hips
    with dissolve
    emelie "You do always look really good... And that swimsuit is amazing!."
    show maf biggrin
    show mapeye down
    show maps out
    show mapnipcover:
        xoffset 150 yoffset 15
    with dissolve
    maple " Why, thank you! That's actually what we were talking about when you showed up! "
    hide mapeye with dissolve
    maple " I was asking [Protagonist] what he thinks of my swimsuit!"
    show emf surprise with dissolve
    emelie " Oh! "
    hide emeye with dissolve
    emelie " Well, what do you think, [Protagonist]?"
    #Choice
    window hide
    menu:
        with dissolve

        " It's very pretty!":
            window show
            me " It's very pretty!"
            show maf closeyes
            show maps cheerupc
            hide mapnipcover
            with dissolve
            maple " Yay!"
            show emf sooth
            show emeye maple2 at right:
                yalign -0.20 xalign 0.80
                zoom 0.95
            with dissolve
            emelie " I think so too! "
            maple " Thank you both!"


        "I wouldn't mind seeing you in a similar design, Emelie!":
            window show
            me "I wouldn't mind seeing you in a similar design, Emelie!"
            show emf wide
            show emblush at right:
                yalign -0.20 xalign 0.80
                zoom 0.95
            show emear high at right:
                yalign -0.20 xalign 0.80
                zoom 0.95
            with dissolve
            emelie "It's a tad daring for me, I think!"
            hide emear
            show emf pout
            hide emblush
            hide emear
            with dissolve
            emelie " But maybe one day! "
            show maf closeyes
            show maps cheerupc
            hide mapnipcover
            with dissolve
            maple " I'm glad you like it!"

    show maf grin with dissolve

    maple " But I wasn't just fishing for a compliment!"

    show maf biggrin
    show maps dubpeacehigh
    show mapnipcover:
        xoffset 150 yoffset 15
    with dissolve
    maple " I'm participating in this year's swimsuit competition! "
    maple "And I was hoping I could get a confidence boost 'cus it's just about to start!"
    show emf surprise2
    show emeye maple2 at right:
        yalign -0.20 xalign 0.80
        zoom 0.95
    with dissolve
    emelie " Oh really?! Cool!!"
    show emeswim out
    show emf biggersmile
    hide emeye
    with dissolve
    emelie" We should go check it out, [Protagonist]!"
    me " Yeah for sure! Sounds fun!"
    show maf closeyes
    show maps tidc
    hide mapnipcover
    with dissolve
    maple " Woo!"
    show maf biggrin with dissolve
    maple " Then follow me, cuties! It isn't far from here!"
    window hide
    play sound "audio/soundFX/run2.wav"
    hide maps
    hide maf
    hide mapeye
    hide mapnipcover
    with easeoutleft
    pause 0.2
    play sound "audio/soundFX/run2.wav"
    hide emf
    show emeswim normal
    with dissolve
    hide emeswim
    hide emeye
    hide emelon
    with easeoutleft
    scene black with fade
    jump BikiniContest

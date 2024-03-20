label Chapter2AndHalf:
    window hide
    scene black with fade
    window show
    "I find myself in front of the fountain once again."
    window hide







    scene bg fountain with dissolve
    pause 0.5

    play sound "audio/soundFX/run2.wav"

    show billy base at left:
        yalign 0.4 xalign -0.08
    with easeinleft
    window show
    billy " So!"
    billy " We've got a little bit of time to spend together, eh?"
    show billy casualaugh at left:
        yalign 0.4 xalign -0.08
    with dissolve
    billy " Well, you're in luck!"
    billy "Cus I got this a while back! "
    window hide
    play sound "audio/soundFX/Get.mp3"
    show blackopacity
    show librarycard
    with dissolve
    pause 0.3
    window show
    billy " It'll let you loan any book you want from the local bookstore!"
    billy " Take it!"
    play sound "audio/soundFX/Get.mp3"
    hide blackopacity
    hide librarycard
    with dissolve
    "I put the card in my pocket."
    show billy finger with dissolve
    billy " The shop's just a few buildings down this road!"
    window hide
    scene black with dissolve
    window show
    "I follow Billy for a minute."
    window hide
    scene librarysign with dissolve
    pause 0.5
    window show
    billy " We're here!"
    "The sign looks just like the card I got!"
    billy "Let's head inside!"
    stop music fadeout 2.0
    window hide
    $ vic_name = "???"
    scene bg library

    show victoria glasses:
        yalign 1.1 xalign 0.0
    show vic lash:
        yalign 1.1 xalign 0.0
    show librarydesk

    with fade
    play sound "audio/soundFX/FX2/shop-door-bell.wav" volume 0.5
    play music "audio/Tavern+Brawl+-+320bit.mp3" fadein 2.0 volume 0.4
    pause 0.4
    window show
    #Victoria is introduced
    #BE KINDA SNAPPY
    #SoundBell
    vic " Welcome to Feathers and Fiction!"
    " A tall chicken lady stands behind her desk! "
    "She's probably a tiny bit taller than me, with her comb adding several inches to her height."
    show victoria hiphold
    show vic lash
    hide victoriahandonbook
    with dissolve
    vic " How can I help?"
    window hide
    play sound "audio/soundFX/run2.wav"
    show billy high at left with easeinleft:
        yalign 0.4 xalign -0.08
    window show
    billy " Hello again, Victoria! "
    $ vic_name = "Victoria"
    show billy casual with dissolve
    billy " We're looking to loan a book!"
    show vic smile with dissolve
    vic " Exciting! "
    vic " We just got two new releases in!"
    show billy laugh with dissolve
    billy " Ooo, I can't wait! "
    show billy base with dissolve
    billy " I'll go wait in the back while you pick one out, [Protagonist]!"
    window hide
    play sound "audio/soundFX/run2.wav"
    hide billy with easeoutright
    window show
    "He quickly runs off to one of the side rooms."
    show victoria handonbook:
        yalign 1.1 xalign 0.0
    show vic lash:
        yalign 1.1 xalign 0.0
    show victoriahandonbook:
        yalign 1.1 xalign 0.0
    with dissolve

    vic "I don't think I've seen you here before!"
    vic " 'You one of Billy's friends? "
    window hide
    menu:
        with dissolve
        "Yep.":
            window show
            me "Yep."
            show victoria hiphold
            hide victoriahandonbook
            show vic bigsmile
            with dissolve
            vic "I see!"
            vic "My name's Victoria and I run this shop! "

        "We're best buds!":
            window show
            me "We're best buds!"
            show victoria hiphold
            hide victoriahandonbook
            show vic bigsmile
            with dissolve
            vic "Aw, how sweet!"
            vic "My name's Victoria and I run this shop! "

        "I met him for the first time earlier today.":
            window show
            me "I met him for the first time earlier today."
            show victoria hiphold
            hide victoriahandonbook
            show vic sad
            with dissolve
            vic "Oh... "
            show victoria hiphold
            hide victoriahandonbook
            show vic bigsmile
            with dissolve
            vic "Well, my name's Victoria and I run this shop! "
    me " Nice to meet you! I'm [Protagonist]."
    show vic closed
    with dissolve
    vic " Nice to meet you too!"
    vic "I love some company!"
    show vic lash with dissolve
    vic " Billy used to come here all the time back in the day."
    show vic squint with dissolve
    vic " Mostly for some sneaky help with his homework... "
    show victoria proper
    show vic lash
    with dissolve
    vic " You'll find all sorts of books to loan or purchase here!"
    #vic " There's also a little library section in the side-room where you can read and study free of charge!"
    vic " We also specialize in quills."
    show victoria hiphands
    show vic bigsmile
    with dissolve
    vic " Some are plucked directly from my own bum!"
    show vic closed
    with dissolve
    vic" Cluck cluck cluck!"
    "She laughs to herself and keeps chatting at a rapid pace."
    show victoria hiphold
    show vic lash
    with dissolve
    vic " You must be from out of town or I think I would've seen you around!"
    show vic squint
    with dissolve
    vic " 'Come here to take advantage of the recent \"Humane Hunk \" popularity, hmm?"

    "I give her a questioning look."
    show victoria behindback
    show vic laugh
    with dissolve
    vic " Puk puk pukaaak!"
    show vic squint
    show victoria hiphold
    with dissolve
    vic "I'm just kidding."

    vic " But those books are just flying off the shelves! "
    show victoria handonbook:
        yalign 1.1 xalign 0.0
    show vic lash:
        yalign 1.1 xalign 0.0
    show victoriahandonbook:
        yalign 1.1 xalign 0.0
    with dissolve
    vic " Even got a lady like myself curious enough to read it."
    show victoria handonbooklow
    show vic surprise
    with dissolve
    vic " These young adult novels are really starting to push the age ratings..."
    me " I read some of it before and it seemed pretty raunchy."
    show vic blush with dissolve
    vic " Y-yeah you could definitely say that."
    vic "Media these days is getting more and more extreme, that's for sure!"
    vic "Or what do you think?"
    window hide
    menu:
        with dissolve
        "I like a lot of extreme stuff in my books!":
            $ lewdbooks = True
            window show
            me "I like a lot of extreme stuff in my books!"
            show victoria hiphold
            hide victoriahandonbook
            show vic bigsmile
            with dissolve
            vic "Oho! Not afraid of your boundaries being pushed a little, huh? "
            show vic squint with dissolve
            vic "Then your future will surely be bright when it comes to reading!"


        "Yeah, things are getting out of control!":
            $ lewdbooks = False
            window show
            me "Yeah, things are getting out of control!"
            show victoria hiphold
            hide victoriahandonbook
            show vic eeh
            with dissolve
            vic "Ahh... Well, at least you'll always have the classics!"
            show vic surprise with dissolve
            vic " Or... maybe stay away from those on second thought."
            show vic surprisesmall with dissolve
            vic " A lot of old books have absolutely degenerate stuff in them!"
            show vic eeh with dissolve
            vic " But they tend to leave out a lot of the...details."
    show victoria proper
    show vic lash
    hide victoriahandonbook
    with dissolve
    vic " Oh right speaking of which, Billy said you were looking to loan something! "
    show vic sad with dissolve
    vic " \"Humane Hunk\" is unfortunately out of stock."
    "I look down at what appears to be a copy right on her desk."
    show vic eeh
    show victoria handonbooklow:
        yalign 1.1 xalign 0.0

    show victoriahandonbook:
        yalign 1.1 xalign 0.0
    with dissolve
    vic " This one isn't for sale! I'm still reading it."
    show vic squint
    show victoria hiphold
    hide victoriahandonbook
    with dissolve
    vic " But we have plenty of the other two."
    if lewdbooks == True:
        show vic lash
        show victoria hiphands
        with dissolve
        vic " And they're sort of... intense too!"
        show vic bigsmile with dissolve
        vic " So right up your alley!"
    if lewdbooks == False:
        show vic blush
        show victoria hiphands
        with dissolve
        vic "They're sort of intense too, so maybe not up your alley if you dislike this modern boundary-pushing stuff!"
        me " It's okay, Billy seemed excited about them!"
        show vic bigsmile with dissolve
        vic " Aw, that's nice of you to consider with your pick!"
    me " What are the books about?"
    me " The bee one doesn't look like it'd be very intense."
    show vic laugh
    show victoria proper
    with dissolve
    vic " Well, don't judge a book by its cover! Cluck cluck! "
    show blackopacity
    show leftbook
    with dissolve
    vic " The one with the wolf on the cover is your typical horror book!"
    vic " Tense, scary, gruesome!"
    show rightbook
    show rightbookz behind bg
    with dissolve

    vic " And this bee one is the latest educational Sex-Ed book."
    hide rightbookz
    vic " We've gotten some complaints from parents about the \" explicit \" imagery within."
    vic " And I'm personally not too sure about the science... "
    me " Okay, I got ya."
label olbookchoice:
    vic " So which one will it be? "

    window hide
    show screen Chapter2HalfChoice1
    $ _skipping = False
    $ disableAFMbutton = True
    $ preferences.afm_enable = False
    $ renpy.pause(hard=True)

screen Chapter2HalfChoice1:
    #add "gui/choices/RolfInterrogationUI.png"

    imagebutton:
        style "mainmenunew"
        idle "images/Chapter2.5/leftbook.png"
        hover "gui/choices/leftbookhover.png"
        action Show(screen="ConfirmChoices", YesAction=Jump("horror"), Choice="bookright", NoAction=Show(screen="Chapter2HalfChoice1"), transition=dissolve)

    imagebutton:
        style "mainmenunew"
        idle "images/Chapter2.5/rightbook.png"
        hover "gui/choices/rightbookhover.png"
        action Show(screen="ConfirmChoices", YesAction=Jump("sexed"), Choice="bookleft", NoAction=Show(screen="Chapter2HalfChoice1"), transition=dissolve)

screen ChoicebookleftDark:
    add "gui/choices/ChoicebookleftDark.png"

screen ChoicebookrightDark:
    add "gui/choices/ChoicebookrightDark.png"

label horror:

    hide screen Chapter2HalfChoice1
    hide screen ChoicebookleftDark
    window show
    $ scarybook = True
    me "Horror!"
    $ disableAFMbutton = False
    $ _skipping = True
    window hide
    hide blackopacity
    hide leftbook
    hide rightbook
    show victoria hiphold
    show vic lash
    with dissolve
    window show

    vic " Oooh, you're a brave one arent'ya? "
    "I blush and hand her the library card I got from Billy. "
    show victoria proper
    show blackshake at truecenter behind bg
    show vic closed
    with dissolve
    "She gives me a joyful nod and reaches down under her desk to hand me a copy of the book."
    play sound "audio/soundFX/Sit Pillow.wav"
    with hpunch
    show vic bigsmile with dissolve
    vic " Happy reading!"
    me "Thank you! "

    window hide
    scene black with dissolve
    window show
    " I hurry on over to where Billy went. "


    window hide

    scene bg bookday
    show billy base at left:
        zoom 0.9 yalign 0.4 xalign 0.10
    show daydesk
    with fade
    window show
    me " I picked one out!"
    me " Was between this one and some educational book..."
    "I show him the book."
    me " It's supposedly pretty scary!"
    show billy ooo with dissolve
    billy " Waaah! I tend to stay away from horror!"
    billy "... But I also stay away from non-fiction in my spare time..."
    show billy base
    show bill surpriseface at left:
        zoom 0.9 yalign 0.4 xalign 0.10
    with dissolve
    billy " To be honest I kinda stay away from books in general on my free time."
    hide bill
    show billy belly
    with dissolve
    billy " I always end up falling asleep when I lie down to read."
    show billy casual
    with dissolve
    billy " You should read it for me!"
    me " Sure."
    me "I'm kinda excited, I don't think I've ever read a newly published book before!"
    me "Let's open it up."
    window hide
    show blackopacity
    show horror1:
        yalign 0.4

    with dissolve
    pause 0.8
    window show
    " That's a pretty scary-looking wolf..."
    me " \" Foreword.\""
    me " \" The war might have ended, but the threat of a wolf attack remains!\""
    billy " Eeek!"
    me " \" This book is based on one such horrific event...\""
    me " \" The tragedy of the three little pigs.\""
    window hide
    hide blackopacity
    hide horror1
    show billy wary
    with dissolve
    window show
    billy " Oh no, I think I heard about that when I was just a wee piglet!"
    me " There's a picture of a wolf in here too, look!"
    " I hand him the book."
    show billy holdinghuff
    with dissolve
    billy "..."
    show bill lookdownsweat at left:
        zoom 0.9 yalign 0.4 xalign 0.10
    with dissolve
    billy " AAH!"
    show bill squint with dissolve
    billy " The story hasn't even started yet and I'm already shaking in my armor!"

    billy "..."
    "He slowly turns the page."
    play sound "audio/soundFX/PageTurn.wav "
    show billy laugh
    show bill lookdownsweat at left:
        zoom 0.9 yalign 0.4 xalign 0.10
    show billyholdinghuffhigh at left:
        zoom 0.9 yalign 0.4 xalign 0.10
    with dissolve
    billy "WAAAAH!"
    show bill cryy with dissolve
    billy " Take it back!"
    show billy clench
    hide billyholdinghuffhigh
    hide bill
    with dissolve
    play sound "audio/soundFX/Get.mp3"
    show blackshake at truecenter behind bg
    with vpunch

    "He hands me the book again."
    window hide
    show blackopacity
    show horror2
    with dissolve
    pause 0.8
    window show
    me " Damn, are wolves really that big?!"
    billy " I-I don't know!"
    billy " Rolf isn't afraid of anything... but when he speaks of the war he gets this look in his eyes..."
    billy " If they were small there's no way he'd have gotten scratched up by one!"
    billy " They MUST be huge!"
    me "That's true..."
    me " Okay here's chapter one! "
    window hide
    hide blackopacity
    hide horror2
    with dissolve
    window show
    me " \"Once upon a time, there was an old sow with three little piglets.\" "
    me " \" When the piglets finally came of age they took what little money their mother had saved up and went to live on their own.\""
    hide bill
    show billy base
    with dissolve
    billy " Oh, how considerate of their mother to save some money for them!"
    me " \"The first little pig was very lazy and gluttonous.\""
    me " \"He didn't work at all and spent all his money on truffles and women.\""
    me " \" When he realized he was running out of money he grabbed some straw lying around and built himself a rugged straw hut. \""
    show billy casual
    show bill surpriseface at left:
        zoom 0.9 yalign 0.4 xalign 0.10
    with dissolve
    billy " Poor guy! I make sure to keep myself in check when truffle season comes around..."
    hide bill with dissolve
    billy " They're oh so good but OH SO PRICY!"
    me " \"The second little pig only partied on the weekends, and spent his weekdays doing hard physical labor.\""
    me " \"He used his wage and skills to build a sturdy wooden house to sleep in!\""
    show billy thumbup with dissolve
    billy " Aw, that's respectable! Perfect balance of work and leisure!"
    me " \"The third little pig worked hard all day and night, seven days a week.\""
    me " \" After a year of saving he bought the sturdiest, biggest bricks around and paid his skilled brother to build him a tiny brick fortress! \""
    me " \" Complete with a tiny moat and a tower to survey the area.\" "
    me " \"It could surely withstand the strongest of winds.\""
    show billy casualaugh with dissolve
    billy " I like this guy! Safety first, even if it's hard work! "
    "I flip the page."
    play sound "audio/soundFX/PageTurn.wav "
    show blackopacity
    show horror3
    with dissolve
    " Oh, just more text..."

    show bg booksunset
    hide daydesk
    show sunsetdesk
    show black
    with dissolve
    stop music fadeout 1.0
    "I continue reading. "
    play music "audio/Mega+Heavy+Suspense+-+320bit.mp3" fadein 1.0 volume 0.6
    "The book spends a lot of time on the pigs' relationships and families."
    "I read page after page with no real sign of a wolf... "
    "Billy seems completely immersed in the story, rocking back and forth in his chair."
    "Tension slowly builds with howls being heard at night."
    hide black
    hide blackopacity
    hide horror3
    with dissolve
    me "\"The following day a large, foul shadow passed by where the three little pigs lived.\""
    me "\"The creature saw the small straw hut, and its large nostrils flared wide to smell the pig sleeping inside. \""
    hide bill
    show billy wary
    with dissolve
    billy "W-what could that creature be!?"
    billy " He can smell the piggy through the walls? "
    show bill squint at left:
        zoom 0.9 yalign 0.4 xalign 0.10
    with dissolve
    billy "It must be a wolf! "
    billy " I hear their sense of smell is impressive but I didn't know it was THAT good!"
    me "\"His mouth began to water imagining his sharp teeth digging into flesh!\""
    hide bill
    show billy clench
    with dissolve
    billy " How cruel!"

    me "\"So he dug his claws into the door and growled-\""
    "I make my voice as deep and scary as I can. "
    me "\"{i}Little pig! Little pig!{/i} \""
    me "\"{i}Let me in! Let me in!{/i} \""
    show bill cryy at left:
        zoom 0.9 yalign 0.4 xalign 0.10
    with dissolve
    billy " Don't open!! "
    me "\"But the little pig, while careless with his money, was no fool! \""
    me "\"So he answered back-\""
    me "\"{i}No! No! No!{/i}\""
    me "\"{i}Not unless you've got truffles to sell!{/i}\""
    hide bill
    show billy ooo
    with dissolve
    billy " Smart pig!"

    me "\" The creature bared its teeth through the newly made scratches in the wall and yelled-\""
    me "\" {i}Then I'll huff and I'll puff!.{/i}\""
    me "\" {i}AND I'LL BLOW YOUR HOUSE DOWN!{/i}\""
    show billy wary
    with dissolve
    billy " Oh no! "
    me "\" The three pig brothers lived as neighbors, and the commotion had woken them all up!\""
    me "\" The strong brother in his wooden house grunted-\""
    me "\"{i}Stay away from my brother, beast!{/i}\""
    me "\" He was a very confident pig, his physical work making him tough!\""
    me "\" The third brother in his brick house looked down from his tower and yelled-\""
    me "\" {i}And you'll never blow this fortress down!{/i}\""
    show billy clench
    with dissolve
    billy " Yes! Gang up on him!"
    me "\" The large creature chuckled to himself-\""
    me "\" {i}Suit yourselves... {/i}\""
    me "\"{i}I only came here for a midnight snack...{/i}\""
    me "\" {i}But now I'll serve myself a three-course dinner!{/i}\""
    "I raise my voice."
    me "\"SO HE HUFFED!\""
    me "\" AND HE PUFFED!\""
    "I turn the page!"
    window hide
    play sound "audio/soundFX/PageTurn.wav "
    show blackopacity
    show horror4
    with dissolve
    pause 1.0
    window show
    "Woah!"
    " He blew all three of them away at once!"
    billy " And what?!?!"
    "There's no text accompanying it. Billy has to see this!"
    me " Billy, look!"
    window hide
    hide blackopacity
    hide horror4
    with dissolve

    pause 0.5
    show billy holdinghuff at left:
        zoom 0.9 yalign 0.4 xalign 0.10
    with dissolve
    pause 0.4
    show billy laugh
    show bill lookdownsweat at left:
        zoom 0.9 yalign 0.4 xalign 0.10
    show billyholdinghuffhigh at left:
        zoom 0.9 yalign 0.4 xalign 0.10
    with dissolve
    window show
    billy " NOOO!!!"
    play sound "audio/soundFX/PageTurn.wav "
    "He turns the page."
    show blackshake at truecenter behind bg
    show bill cryy
    with dissolve
    with hpunch
    billy "WAAAAAAAAAAAAAAAAHHHH!"
    billy " That's no fun! No fun at all!"
    " He hands it back over to me with tears in his eyes."

    window hide
    hide bill
    hide billyholdinghuffhigh
    show billy clench
    with dissolve



    show blackopacity
    show horror5
    with dissolve
    pause 1.5
    window show
    me " \"And they all suffered greatly before dying... \""
    stop music fadeout 2.0
    me "That's it...?"
    me " What an abrupt ending."
    billy " That came out of nowhere! "
    "I put the book down."

    window hide
    play sound "audio/soundFX/Sit Pillow.wav"
    play music "audio/Tavern+Brawl+-+320bit.mp3" fadein 1.0 volume 0.4
    hide blackopacity
    hide horror5
    with dissolve
    pause 0.5
    window show

    billy "I can't believe he took them all out in one big huff and puff!!!"
    me " That book was all build up and then it ended with like two sentences or something..."
    show bill cryy at left:
        zoom 0.9 yalign 0.4 xalign 0.10
    with dissolve
    billy " Made it even scarier! All seemed good in the world and suddenly..."
    billy "WHAM! All dead!"
    show bill sadface
    show billy belly
    with dissolve
    billy "..."
    window hide
    menu:
        with dissolve
        "I suppose you're right...{space=9} The story subverted our expectations for a bigger surprise!":
            window show
            me "I suppose you're right... The story subverted our expectations for a bigger surprise!"
            show bill surpriseface with dissolve
            billy " Exactly!"
            show bill casualface with dissolve
            billy " Genius, really."
            "I wouldn't go that far..."
            show bill surpriseface
            show billy finger
            with dissolve
            billy " But I do think the three brothers miscalculated!"


        "I thought it was a really lazy ending. Just bad!":
            window show
            me "I thought it was a really lazy ending. Just bad!"
            show bill surpriseface with dissolve
            billy " Hmmm, maybe I was just happy for it to be over so quick!"
            billy " I swear I could hear my own heartbeat echoing in my helmet!"
            show billy finger
            with dissolve
            billy " Which makes me think..."
    show billy base
    show bill surpriseface
    with dissolve
    billy " They should've bought armor instead of houses."
    show bill baseface with dissolve
    billy " We should get you some, buddy! "
    show billy casual
    show bill casualface
    with dissolve
    billy " That way you'll be safe just like me!"
    me " I don't think that lifestyle is for me."
    show bill downface
    show billy belly
    with dissolve
    billy "..."
    hide bill
    show billy casualaugh
    with dissolve
    billy " I'll just have to protect you then in the case of an attack!! "
    window hide
    show blackshake at truecenter behind bg
    play sound "audio/soundFX/FX2/Chicken.wav" volume 0.4
    with hpunch
    pause 0.2
    window show
    vic " The sun's going down, boys! Wrap it up!"
    hide bill
    show billy wary
    with dissolve
    billy "O-oh!"
    billy " Time really flew by, huh??"
    show billy base with dissolve
    billy " Thanks for reading, buddy! "
    billy " I'll hurry up and get you back to your room! "




    jump afterbook


label sexed:
    hide screen Chapter2HalfChoice1
    hide screen ChoicebookrightDark
    window show
    me "Sex-Ed!"
    $ _skipping = True
    $ disableAFMbutton = False
    $ scarybook = False
    window hide
    hide blackopacity
    hide leftbook
    hide rightbook
    show victoria hiphold
    show vic blush
    with dissolve
    window show
    vic "..."
    vic " Going for that one, huh?  "
    "I blush and hand her the library card I got from Billy. "
    show victoria proper
    show blackshake at truecenter behind bg
    show vic closed
    with dissolve
    "She gives me a joyful nod and reaches down under her desk to hand me a copy of the book."
    play sound "audio/soundFX/Sit Pillow.wav"
    with hpunch
    show vic bigsmile with dissolve
    vic " Happy reading!"
    me "Thank you! "
    window hide
    scene black with dissolve
    window show
    " I hurry on over to where Billy went. "
    window hide
    scene bg bookday
    show billy base at left:
        zoom 0.9 yalign 0.4 xalign 0.10
    show daydesk
    with fade
    window show
    me " I picked a book out!"
    me " This one seemed interesting."
    me " It's apparently got some... explicit stuff in it."
    show billy ooo with dissolve
    billy " Ooo! "
    show billy laugh with dissolve
    billy " Now I'm curious!"
    show billy base
    show bill surpriseface at left:
        zoom 0.9 yalign 0.4 xalign 0.10
    with dissolve
    billy "Thought it was an educational book?"
    show billy belly
    hide bill
    with dissolve
    billy " I don't often spend my free time studying... "
    show billy casual with dissolve
    billy " Maybe you can read it out for me? "
    me " Sure."
    me " Now let's see what this book is all about..."
    #stop music fadeout 1.0


    window hide
    play sound "audio/soundFX/Get.mp3"
    show blackopacity
    show lewd1
    with dissolve
    pause 0.8
    window show
    me " Okay... there's an image of a pig and some foreword text."
    billy " Hit me!"
    me "\" The history of pigkind is impressive and vast!\""
    me "\" From piggies spending their days digging around in the muck, to impressive inventions and agriculture! \""
    me "\" But what lies behind this development?\""
    me "\" Where were we thousands of years ago, and how does life even start?\""
    me "\" Read this book to find out! \""
    window hide
    hide blackopacity
    hide lewd1
    with dissolve
    window show
    billy " I'm pretty sure I know this stuff!"
    show billy base with dissolve
    billy " Read about it back in school."
    billy "..."
    show bill surpriseface at left:
        zoom 0.9 yalign 0.4 xalign 0.10
    with dissolve
    billy " But I probably forgot all about it..."
    hide bill
    show billy wary
    with dissolve
    billy " I have a horrible attention span!"
    show billy clench with dissolve
    billy " I had to do so much extra studying on the side..."

    show billy casual
    show bill baseface at left:
        zoom 0.9 yalign 0.4 xalign 0.10
    with dissolve

    billy " Victoria really helped me during the last few years of school! "
    billy " I would spend my days here just reading and trying my best not to fall asleep."
    show billy base
    show bill laughface at left:
        zoom 0.9 yalign 0.4 xalign 0.10
    with dissolve
    billy " It was a lot of work but I did OK in the end! "
    billy " Keep reading! I wanna see if I remember it all!"
    me " Alright."


    window hide
    play sound "audio/soundFX/Get.mp3"
    show blackopacity
    show lewd2
    with dissolve
    pause 1.2
    window show
    me " Damn!"
    billy " What??"
    me " There's a lot to take in... It's mostly pictures."
    me " One second and I'll let you have it."
    " Huh... did pigs really look like that once?"
    " So weird..."
    " \" It's not the stork!\""
    "This really must be aimed at a younger audience... but nothing too explicit so far..."
    "I'll hand it over to Billy. "
    window hide
    play sound "audio/soundFX/Get.mp3"
    hide blackopacity
    hide lewd2
    with dissolve

    hide bill
    show billy holdingf at left:
        zoom 0.9 yalign 0.4 xalign 0.10
    with dissolve
    window show


    me " Here you go."
    show billy laugh
    show bill lookdownstars at left:
        zoom 0.9 yalign 0.4 xalign 0.10
    show billyholdingfhigh at left:
        zoom 0.9 yalign 0.4 xalign 0.10
    with dissolve
    billy " Woaaaaahh! I love picture books!! "
    billy "We used to read all about how our ancestors looked, but I never had a visual for it!"
    billy " They sure look weird..."
    billy " But kinda cute!"
    show bill lookdownnormal with dissolve
    billy " \"So how does life begin? It's not the stork!\""
    billy " It's... not the stork?"
    show bill wary with dissolve
    "..."
    billy " Then what could it be?"
    "Oh no. "
    show bill lookdownnormal with dissolve
    billy " \" Sometimes when two piggies love each other very much... \""
    show bill laughface with dissolve
    billy " I'm getting really curious now!"
    me " Billy you really don't know?"
    billy " Know what?"
    "He turns the page. "
    play sound "audio/soundFX/PageTurn.wav "
    show bill lookdownnormal with dissolve
    billy "..."
    show bill lookdownbigeyes with dissolve
    billy "!"
    show bill lookdownsweat with dissolve
    show billybigblush at left:
        zoom 0.9 yalign 0.4 xalign 0.10
    with dissolve
    show blackshake at truecenter behind bg
    with hpunch
    billy " WHAAAAAA!?!?"
    " He quickly flips through a bunch of pages!"
    play sound "audio/soundFX/PageTurn.wav "
    billy "..."
    hide billyholdingfhigh
    show billy holdingf
    show bill wut
    with dissolve
    billy " Tadpoles... are... in my... "
    billy " WHAT?!"
    me " Hey, give it to me!"
    " I grab the book from him!"
    window hide
    hide billyholdingfhigh
    show billy base
    hide billybigblush
    with dissolve

    pause 0.2



    play sound "audio/soundFX/Get.mp3"
    show blackopacity
    show lewd3
    with dissolve
    pause 0.4
    window show
    me " WHOA."
    " Okay now THIS is EXPLICIT!"
    me " I can see why parents might have complained..."
    billy "Why? I'm learning a lot!"
    " Albino tadpoles... in my testicles? "
    " That's what cum is?"
    " Maybe this is what Victoria meant when she said the science didn't seem right."
    " But what do I know? "
    billy " You've been staring at those weenies for a while now!"
    me " O-oh sorry!"
    billy " It's okay! "
    billy "Trying to figure out which one looks like yours the most, huh?"
    "Billy giggles. "
    window hide
    hide blackopacity
    hide lewd3
    show bill baseface
    with dissolve
    window show

    billy " It's a good thing the book tries to cover various shapes I guess!"
    hide bill
    show billy casual
    with dissolve
    billy " Or maybe the artist just really wanted to draw a bunch of weird peens..."
    me " That's probably it. "
    show billy laugh with dissolve
    billy " Y'know I forgot all about how fun learning could be!"
    show billybigblush at left:
        zoom 0.9 yalign 0.4 xalign 0.10
    with dissolve

    billy " I wanna learn more!"
    " He seems really new to all this stuff..."
    " And I've seen a lot of bare skin today already."
    me " Sure, have at it!"
    "I hand him the book again."
    show billy holdingf at left:
        zoom 0.9 yalign 0.4 xalign 0.10
    with dissolve



    pause 0.4

    show billy laugh
    show bill lookdownstars behind billybigblush at left:
        zoom 0.9 yalign 0.4 xalign 0.10
    show billyholdingfhigh at left:
        zoom 0.9 yalign 0.4 xalign 0.10
    with dissolve

    " He continues eagerly flipping through it. "
    play sound "audio/soundFX/PageTurn.wav "

    billy " Woah! Wheeesh!"
    billy " You sure picked a good book!"
    show bg booksunset
    hide daydesk
    show sunsetdesk
    show bill lookdownhearts
    show billynoseb at left:
        zoom 0.9 yalign 0.4 xalign 0.10
    show black
    with dissolve

    "Billy spends a fair bit of time finishing the book, asking me basic questions and making sure to show me whenever he finds something interesting."
    hide black with dissolve
    show billy holdingf at left:
        zoom 0.9 yalign 0.4 xalign 0.10
    hide billyholdingfhigh
    with dissolve

    billy " Whew! I think that's it..."
    show bill baseface
    hide billynoseb
    hide billybigblush
    with dissolve
    billy " I definitely learned a lot!"
    show bill laughface with dissolve
    billy " And the book ended up having a really positive message I agree with too!"
    billy " Look!"
    show billy wary with dissolve


    window hide
    play sound "audio/soundFX/Get.mp3"
    show blackopacity
    show lewd4
    with dissolve
    pause 0.4
    window show
    billy " Everyone's unique and beautiful!!"
    billy " That sure puts a smile on my face. "
    "So much nudity!"
    me "Huh... even granny gets a full frontal."
    billy " I know!"
    billy "... What do you think about that?"
    menu:
        with dissolve

        "It's good! {space=9}The message would ring a bit hollow if all four girls were young supermodels." :
            window show
            me "It's good! The message would ring a bit hollow if all four girls were young supermodels."
            billy " That's true! It's not a nudie mag after all!"
            billy " A book like this should make people feel better about themselves!"
            billy "..."

            billy " And I feel kinda tingly after reading all this."
            billy " I think that's a good feeling!"



        "Gross. {space=9}Detracts from the three prettier girls." :
            window show
            me "Gross. Detracts from the three prettier girls."
            billy " That's a mean thing to say!"
            billy " Granny is unique and beautiful even if she's seventy!"
            billy " Or ninety... "
            billy "Either way, I don't think beauty has an age limit!"
            billy " It doesn't have to be some sexual thing! It can be the warm feeling you get seeing your grandma smile!"
            me " Okay fine I'm sorry for ruining the wholesome message."
            billy "I suppose you're just being honest."
            billy "..."
            billy " Y'know... I feel kinda tingly after reading all this."

        "Old ladies are hot." :
            window show
            me "Old ladies are hot."
            billy "!"
            billy " I haven't thought of 'em that way before..."
            billy " When I see an old lady I just make sure to keep an eye out so she doesn't fall!"
            billy " I'm a pig of the people after all! Got to make sure everyone's safe!"
            billy "..."
            billy " But y'know..."
            billy " I feel kinda tingly after reading all this."





    billy " What about you?"
    me " Yeeaaa..."
    "I put the book away. "
    play sound "audio/soundFX/Sit Pillow.wav"
    hide blackopacity
    hide lewd4
    hide bill
    show billy base
    with dissolve
    billy " Now I'm almost certain they never taught us any of that stuff in school!"
    show bill wary at left:
        zoom 0.9 yalign 0.4 xalign 0.10
    with dissolve
    billy " Or is my memory just THAT bad?"
    me " Maybe you're more of a visual learner."
    show billy casual
    show bill laughface
    with dissolve

    billy " That's probably it! "
    show billyblush at left:
        zoom 0.9 yalign 0.4 xalign 0.10
    with dissolve

    billy "I don't think these images will ever leave my mind."
    window hide
    show blackshake at truecenter behind bg
    play sound "audio/soundFX/FX2/Chicken.wav" volume 0.4
    with hpunch
    pause 0.2
    window show
    vic " The sun's going down, boys! Wrap it up!"

    hide billyblush
    hide bill
    show billy wary
    with dissolve
    billy "O-oh!"
    billy " Time really flew by, huh??"
    show billy base with dissolve
    billy " I'll hurry up and get you back to your room! "





    jump afterbook
label afterbook:

    window hide
    play sound "audio/soundFX/FX2/shop-door-bell.wav" volume 0.5
    scene victoriawavebye with fade
    window show

    vic " Was a pleasure seeing you two today!"
    me " Yes, it was really nice meeting you!"
    billy " Likewise, Victoria!"
    vic " Come back any time if you're in the mood for reading or need some information!"
    vic " I could always use some company!"
    vic " And have a good night, cuties~! "
    me "G-goodnight!"
    billy " Nightienight!"


    window hide
    scene black with dissolve
    window show
    "We run through town and quickly get back to Emelie's room."
    window hide

    show bg doorsunset with dissolve
    show billy base at left:
        yalign 0.4 xalign -0.08
    with dissolve
    window show

    billy " And we're back!"
    show bill surpriseface at left:
        yalign 0.4 xalign -0.08
    with dissolve

    billy " Phew, what a long day it's been, huh? "
    show billy casual
    show bill casualface at left:
        yalign 0.4 xalign -0.08
    with dissolve
    billy "Feels like I've known you forever!"


    billy " The sun will go down over the castle walls any time now and then it'll get dark quick!"
    if scarybook == True:
        show billy clench
        hide bill
        with dissolve
        billy " I'm still kinda scared... I'll have nightmares tonight for sure!"
        billy "Guess I'll be safe if I keep my armor on. Sounds like a plan!"
        show billy belly
        with dissolve
        billy "I better hurry on home!"

    else:
        hide bill baseface
        show billy belly
        with dissolve
        billy "That book sure was a lot..."
        show billy laugh
        with dissolve
        billy " I hope I get some related dreams!"
        billy "Y'know... so I learn more!"
        show billy casual with dissolve
        billy " You learn a lot when you sleep."

    show billy base
    hide bill
    with dissolve
    billy "See you tomorrow, buddy!"

    show billy high with dissolve
    "He holds his hand up for a high five."
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

            "Our hands clash hard!"
            me " We make a good team!"
            hide billystar with dissolve
            show bill laughface:
                yalign 0.4 xalign -0.08
            show billy clench
            with dissolve
            billy "For sure!"
            hide bill laughface
            show billy casual
            show bill baseface:
                yalign 0.4 xalign -0.08
            with dissolve
            billy "Now have a good night, buddy!"
            me " Night night!"

        "Leave him hanging.":
            window show
            "..."
            show bill sadface with dissolve:
                yalign 0.4 xalign -0.08
            "Billy lowers his hand with a look of betrayal on his face."
            show billy clench with dissolve
            billy "... "
            billy "Goodnight then."



            me " Goodnight."
    window hide
    play sound "audio/soundFX/Run.mp3"
    hide bill
    hide billy
    with easeoutleft
    window show

    "Billy runs off."
    "..."
    "Guess I'll head inside."

    play sound "audio/soundFX/run2.wav"
    show lars base at left with easeinleft:
        yalign 0.4 xalign -0.6
    lars " Oh, hey!"
    show lars concern with dissolve
    lars " 'Thought I heard something back here and then saw Billy bolt out in a hurry."
    me " Oh hey, Lars."
    "He looks surprised for a moment."
    show lars bigsmile with dissolve
    lars " Wait, I recognize your voice! You're the new guard!"
    if liename == True:
        lars "[lie_name] was it?"
        show lars laugh with dissolve
        lars "Thought you were a piggy!"
        me "About that..."
        show lars base with dissolve
        "I should just tell him the truth."
        me " That's not really my name."
        me " It was all just a cover to get in without angering Rolf."
        me " Billy had an order to bring me in but wanted to be careful not to raise any eyebrows."
        show lars weird with dissolve
        lars " O-oh... I see..."
        " He looks a little sad."
        show lars strange with dissolve
        lars " Now I feel like I did a bad job not seeing through the act..."
        show lars sad with dissolve
        lars " And I was looking forward to having someone new to hang out with on breaks."
        me " Sorry for lying about all that, my real name's [Protagonist]. "


    if liename == False:



        lars " [Protagonist], was it?"
        show lars laugh with dissolve
        lars "Thought you were a piggy!"
        show lars base with dissolve
        "I should tell him the truth."
        me " I'm not actually a guard..."
        me "It was just a cover to get in here without angering Rolf."
        me " Billy had an order to bring me in but wanted to be careful not to raise any eyebrows."
        show lars weird with dissolve
        lars " O-Oh... I see..."
        " He looks a little sad."
        show lars strange with dissolve
        lars " Now I feel like I did a bad job not seeing through the act..."
        show lars sad with dissolve
        lars " And I was looking forward to having someone new to hang out with on breaks."
        me " Sorry for lying back then."

    me " I'm actually the princess' new personal assistant!"
    me " As of today."
    me "So maybe we'll see each other around even if I'm not a guard!"
    show lars laugh with dissolve
    lars "Oh, is that so? Sounds like a plan!"
    show lars base with dissolve
    lars " And you can always be honest with me!"
    show lars laff with dissolve
    lars " Unless you're doing something illegal. Then I'll get ya!"

    me " I'll try to stay out of trouble going forward!"
    show lars laugh with dissolve
    lars "Good to hear!"
    show lars base with dissolve
    lars "I work late shifts here in the building, but it's almost always empty... "
    lars "Other than the baths maybe."
    show lars laugh with dissolve
    lars " Well, I better get back to patrolling! "
    lars "Don't be a stranger if you need anything!"
    me "Have a good one, Lars!"
    play sound "audio/soundFX/run2.wav"
    hide lars with easeoutleft

    "Lars skips away with a pep in his step, visibly happy we cleared things up!"


    $ moom_name = "???"
    $ moog_name = "???"
    $ deem_name = "???"
    $ deeg_name = "???"


    "I reach for the door."
    with hpunch
    moog "Thihihi-"
    "I hear a feminine giggle echo down the hallways!"
    window hide
    scene black with dissolve
    window show
    "I follow the sound and end up at the baths."
    window hide
    scene bg BathHallsSunset
    show bathbusy
    with dissolve
    window show
    #Nyaah!"
    "Multiple voices can be heard from one of the rooms."
    window hide
    menu:
        with dissolve
        "Peek inside!" :
            window show
            stop music fadeout 2.0
            $ peekingtom1 = True
            "I sneak up to the keyhole and peek inside."
            jump moosedeer

        "Don't peek." :
            window show
            "I don't think I should..."
            "Especially not with my new position as the princess' assistant!"
            window hide
            scene black with dissolve
            window show
            "And if Lars found me peeping into the baths he'd be super disappointed in me..."


            jump afterdeer



label moosedeer:
    window hide
    show black with dissolve
label moosedeergallery:
    play sound "audio/soundFX/Get.mp3"
    play music "audio/Farm+-+320bit.mp3" fadein 1.0 volume 0.4
    scene deer dicc1
    show keyhole
    with fade
    pause 0.8
    window show

    "Woah!"
    " Looks like a big moose man to the left with a deer guy standing right in front of him!"
    " And a busty moose lady in the bath with a deer girl behind."
    $ moom_name = "Moose Man"
    $ moog_name = "Moose Lady"
    $ deem_name = "Deer Guy"
    $ deeg_name = "Deer Girl"

    moom " Told ya!"
    moom " Of course mine's bigger."
    deem "..."
    moog " Now, now."
    moog " Let's not jump to conclusions!"
    moog " Sometimes you have to let things... unfold."
    moom " What?"
    moog " Look here-"
    window hide
    play sound "audio/soundFX/Get.mp3"
    show deer dicc2
    with dissolve
    pause 0.8
    window show
    "She pulled her top off!"

    deeg "Did you really just-"

    window hide
    show deer dicc3
    with dissolve
    pause 0.8
    window show

    deem " Eeeh!"
    moom "!"
    moog " Theere we go!"
    " The deer's a grower!"
    moom "..."
    moom " Mine's thicker!"

    window hide
    show deer dicc4
    with dissolve
    pause 0.8
    window show
    moog "Hmm what do you think, girl?"
    moog "Length or girth?"
    deeg "Uuuh, don't ask me that!!"
    "The deer girl's clearly very flustered by this whole situation..."
    moog " Both, huh?"
    moog "I could definitely go for both..."
    " The two lads seem taken aback by her teasing words."


    window hide
    show deer dicc5
    with dissolve
    pause 0.8
    window show
    "Their dicks touch!"
    moog "Hahaha!"
    moom "..."
    deem "Heh..."
    deeg "Woaah!"
    " This turn of events sure made the girls excited!"
    moog " A shame about the time..."
    moog "Things were only just getting fun."
    moog " Guess we'll have to continue another day."
    deem " I'd be okay with that-"
    moom " Hmph! This isn't fair, just humiliating!"
    moom " Next time you girls better show skin first! Or no deal!"
    moog " Okay, FINE."
    deeg " I-I don't know about that!!"

    play sound "audio/soundFX/FX2/water-slosh-spashing-3.wav"
    " They start moving out of the water. "
    window hide
    stop music fadeout 2.0
    scene black with dissolve
    window show
    "I better get out of here before I'm noticed!"
    $ unlock("S3")
    $ renpy.end_replay()
    jump afterdeer


label afterdeer:
    window show

    play music "audio/soundFX/FX2/crickets.wav" fadein 3.0 volume 0.3
    $ renpy.music.set_volume(0.20, delay=0, channel='music')

    " I spend some time finding my way back as the sun sets."
    window hide
    $ renpy.music.set_volume(0.50, delay=0, channel='music')
    pause 0.2
    $ renpy.music.set_volume(0.75, delay=0, channel='music')
    pause 0.2
    $ renpy.music.set_volume(1.00, delay=0, channel='music')
    scene bg nightcorridor with dissolve


    window show
    " Damn, it really got dark quick."
    " I find myself in front of the door again and push it open."
    window hide
    play sound "audio/soundFX/OpenDoor 1.wav"
    show bg emelieroomnight with fade
    pause 0.7
    window show


    "It's been a crazy day... I'm so tired."
    " I feel a cold breeze from the open window and approach it."
    window hide
    play music "audio/TrailsNight.mp3" fadein 0.1 volume 0.6
    scene nighttime with fade
    pause 1.0
    window show
    "Woah..."
    "I'm high enough to see past the outer walls!"
    "The sky is so clear tonight."
    "Wait... "
    "That lone tree on the hill is the one I always take my breaks under!"
    " Not even a full day ago I was down there snacking on a rock... And this city was a complete mystery to me."

    " Thinking back on it I feel silly being so wary of Billy. "
    " He really is harmless!"
    window hide
    show nighttime2 with dissolve
    pause 0.8
    window show
    " I never thought I'd befriend a city guard. "
    "Or meet the princess herself!"
    "And I definitely didn't think I'd get to see her... like I have today."
    " To think that all these years me and Emelie have been looking towards each other without knowing..."
    window hide
    show nighttimestars with dissolve
    pause 0.8
    window show
    " I wonder where she is now? "
    "..."
    "My eyelids feel so heavy... I think I'll go lie down."
    scene black with fade
    play sound "audio/soundFX/Door Close 2.wav"
    "I close the window and crawl in under the bedsheets."
    play sound "audio/soundFX/Sit Pillow.wav"
    "The pillow is soft and smells nice."
    play sound "audio/soundFX/Blanket Move.wav"
    "My thoughts slowly clear as I fall asleep."
    stop music fadeout 2.0
    "..."
    window hide
    pause 0.5
    jump DinnerDay

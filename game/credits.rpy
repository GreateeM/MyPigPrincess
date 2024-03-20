screen credits():
    tag menu

    add "gui/gamemenu.png"

    use game_menu()

    style_prefix "credits"

    viewport:
        area (485, 282, 1372, 602)
        scrollbars "vertical"
        side_yfill True
        pagekeys True
        mousewheel True
        draggable True

        vbox:
            spacing 10
            text "{color=#EB8D4E}{size=+10}My Pig Princess"
            text "{alpha=0.6}{size=-5}Version 0.7.0{/alpha}{/size}"


            hbox:
                text "Art, characters, story, writing & basic code by "
                textbutton "{a=https://twitter.com/CyanCapsule}{color=#80B0D8}CyanCapsule{/a}" action NullAction()
            hbox:
                text "Support my work or get the latest build on my "
                textbutton "{a=https://www.patreon.com/cyancapsule}{color=#80B0D8}Patreon{/a}" action NullAction()
                text "!"

            text "  "

            hbox:
                text "{alpha=0.6}{size=-5}Made with "
                textbutton "{a=https://renpy.org}{color=#80B0D8}Ren'Py{/a}" action NullAction()
            #text "  "
            hbox:
                text "{color=#EB8D4E}{size=+10}Code Help "
            hbox:
                text ""
                textbutton "{a=https://www.patreon.com/quonix}{color=#80B0D8}Quonix{/a}" action NullAction()
            hbox:
                text ""
                textbutton "{a=https://ipkcle.itch.io/}{color=#80B0D8}Ipkcle{/a}" action NullAction()
            text "{color=#EB8D4E}{size=+10}Music"
            hbox:
                text "Intro song and Emelie's Tower songs by"
                textbutton "{a=https://twitter.com/GucciFeline}{color=#80B0D8}Kalua{/a}" action NullAction()
            text "{alpha=0.6}{size=-5}Commissioned for this game!{/alpha}{/size}"
            text "  "
            hbox:
                text "Beach songs by"
                textbutton "{a=https://twitter.com/TempxaRK9}{color=#80B0D8}Tempxa{/a}" action NullAction()
            text "{alpha=0.6}{size=-5}Commissioned for this game!{/alpha}{/size}"
            text "  "

            hbox:
                textbutton "{a=https://incompetech.filmmusic.io/song/8287-adventures-in-adventureland}{color=#80B0D8}\"Adventures In Adventureland \"{/a}" action NullAction()
                text "by Kevin MacLeod"
                textbutton "{alpha=0.6}{a=https://incompetech.filmmusic.io/standard-license}{color=#80B0D8}( License ){/alpha}" action NullAction()

            hbox:
                    textbutton "{a=https://incompetech.filmmusic.io/song/7927-starting-out-waltz-vivace}{color=#80B0D8}\"Starting Out Waltz Vivace \"{/a}" action NullAction()
                    text "by Kevin MacLeod"
                    textbutton "{alpha=0.6}{a=https://incompetech.filmmusic.io/standard-license}{color=#80B0D8}( License ){/alpha}" action NullAction()

            text "  "


            hbox:
                text "Multiple songs by "
                textbutton "{a=https://www.patreon.com/anakarada}{color=#80B0D8}Alexander Nakarada{/a}" action NullAction()
            hbox:
                text "{alpha=0.6}{size=-5}\"Stöðvar\"                                            \"We Are Victorious\" "
            hbox:
                text "{alpha=0.6}{size=-5}\"Heartbeat\"                                      \"Tavern Brawl\""
            hbox:
                text "{alpha=0.6}{size=-5}\"Mega Heavy Suspense\"         \"Farm\""
            hbox:
                text "{alpha=0.6}{size=-5}\"Grundar\"                                          \"Blacksmith\" "
            hbox:
                text "{alpha=0.6}{size=-5}\"Planning\"                                          \"Forest Walk\" "
            hbox:
                text "{alpha=0.6}{size=-5}\"Vopna\"                                          \"Now We Feast\" "
            hbox:
                textbutton "{a=https://www.patreon.com/anakarada}{color=#80B0D8}(www.patreon.com/anakarada){/a}" action NullAction()
            hbox:
                textbutton "{a=https://creatorchords.com/}{color=#80B0D8}(www.creatorchords.com){/a}" action NullAction()



            textbutton "{alpha=0.6}{a=https://creativecommons.org/licenses/by/4.0/}{color=#80B0D8}License: Attribution 4.0 International (CC BY 4.0){/alpha}" action NullAction()


            text "{color=#EB8D4E}{size=+10}Sound Effects"
            hbox:
                text "Various sound effects commissioned from "
                textbutton "{a=https://twitter.com/GucciFeline}{color=#80B0D8}Kalua{/a}" action NullAction()
            hbox:
                text "A majority of sound effects downloaded from"
                textbutton "{alpha=0.6}{a=https://freesound.org/}{color=#80B0D8}Freesound.org{/alpha}" action NullAction()
            textbutton "{alpha=0.6}{a=https://docs.google.com/document/d/1n8dt33qNr3ce19EmvSdGkJMBXVizllABPWLPYzgbAHU/edit?usp=sharing}{color=#80B0D8}\"Freesound\" Sound Effects credited here!{/alpha}" action NullAction()


style credits_vscrollbar:
    base_bar Frame("gui/bar/vscroll.png", 12, 6, 12, 6)
    thumb Frame("gui/bar/vscrollbar.png", 12, 6, 12, 6)
    xsize 40
    mouse "hover"
    hover_sound "audio/UIsounds/hover.wav"

style credits_text:
    color "#4f2934"
    size 50

style credits_button_text:
    size 50
    hover_sound "audio/UIsounds/hover.wav"
    mouse "hover"
    outlines [(0, "#EB8D4E", 0, 0)]
    yoffset -5

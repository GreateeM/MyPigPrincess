################################################################################
## Initialization
################################################################################

init offset = -1


################################################################################
## Styles
################################################################################

style default:
    properties gui.text_properties()
    language gui.language

style input:
    properties gui.text_properties("input", accent=True)
    adjust_spacing False

style hyperlink_text:
    properties gui.text_properties("hyperlink", accent=True)
    hover_underline True

style gui_text:
    properties gui.text_properties("interface")


style button:
    properties gui.button_properties("button")

style button_text is gui_text:
    properties gui.text_properties("button")
    yalign 0.5


style label_text is gui_text:
    properties gui.text_properties("label", accent=True)

style prompt_text is gui_text:
    properties gui.text_properties("prompt")


style bar:
    ysize gui.bar_size
    left_bar Frame("gui/bar/left.png", gui.bar_borders, tile=gui.bar_tile)
    right_bar Frame("gui/bar/right.png", gui.bar_borders, tile=gui.bar_tile)

style vbar:
    xsize gui.bar_size
    top_bar Frame("gui/bar/top.png", gui.vbar_borders, tile=gui.bar_tile)
    bottom_bar Frame("gui/bar/bottom.png", gui.vbar_borders, tile=gui.bar_tile)

style scrollbar:
    ysize gui.scrollbar_size
    base_bar Frame("gui/scrollbar/horizontal_[prefix_]bar.png", gui.scrollbar_borders, tile=gui.scrollbar_tile)
    thumb Frame("gui/scrollbar/horizontal_[prefix_]thumb.png", gui.scrollbar_borders, tile=gui.scrollbar_tile)

style vscrollbar:
    xsize gui.scrollbar_size
    base_bar Frame("gui/scrollbar/vertical_[prefix_]bar.png", gui.vscrollbar_borders, tile=gui.scrollbar_tile)
    thumb Frame("gui/scrollbar/vertical_[prefix_]thumb.png", gui.vscrollbar_borders, tile=gui.scrollbar_tile)

style slider:
    ysize gui.slider_size
    base_bar Frame("gui/slider/horizontal_[prefix_]bar.png", gui.slider_borders, tile=gui.slider_tile)
    thumb "gui/slider/horizontal_[prefix_]thumb.png"

style vslider:
    xsize gui.slider_size
    base_bar Frame("gui/slider/vertical_[prefix_]bar.png", gui.vslider_borders, tile=gui.slider_tile)
    thumb "gui/slider/vertical_[prefix_]thumb.png"


style frame:
    padding gui.frame_borders.padding
    background Frame("gui/frame.png", gui.frame_borders, tile=gui.frame_tile)



################################################################################
## In-game screens
################################################################################


## Say screen ##################################################################
##
## The say screen is used to display dialogue to the player. It takes two
## parameters, who and what, which are the name of the speaking character and
## the text to be displayed, respectively. (The who parameter can be None if no
## name is given.)
##
## This screen must create a text displayable with id "what", as Ren'Py uses
## this to manage text display. It can also create displayables with id "who"
## and id "window" to apply style properties.
##
## https://www.renpy.org/doc/html/screen_special.html#say

screen say(who, what):
    style_prefix "say"

    window:
        id "window"

        if who is not None:

            window:
                id "namebox"
                style "namebox"
                text who id "who"

        text what id "what"


    ## If there's a side image, display it above the text. Do not display on the
    ## phone variant - there's no room.
    if not renpy.variant("small"):
        add SideImage() xalign 0.0 yalign 1.0


## Make the namebox available for styling through the Character object.
init python:
    config.character_id_prefixes.append('namebox')

style window is default
style say_label is default
style say_dialogue is default
style say_thought is say_dialogue

style namebox is default
style namebox_label is say_label


style window:
    xalign 0.5
    xfill True
    yalign gui.textbox_yalign
    ysize gui.textbox_height

    background Image("gui/textbox.png", xalign=0.5, yalign=1.0)

style namebox:
    xpos gui.name_xpos
    xanchor gui.name_xalign
    xsize gui.namebox_width
    ypos gui.name_ypos
    ysize gui.namebox_height

    background Frame("gui/namebox.png", gui.namebox_borders, tile=gui.namebox_tile, xalign=gui.name_xalign)
    padding gui.namebox_borders.padding

style say_label:
    properties gui.text_properties("name", accent=True)
    xalign gui.name_xalign
    yalign 0.5

style say_dialogue:
    properties gui.text_properties("dialogue")

    xpos gui.dialogue_xpos
    xsize gui.dialogue_width
    ypos gui.dialogue_ypos


## Input screen ################################################################
##
## This screen is used to display renpy.input. The prompt parameter is used to
## pass a text prompt in.
##
## This screen must create an input displayable with id "input" to accept the
## various input parameters.
##
## https://www.renpy.org/doc/html/screen_special.html#input

screen input(prompt):
    style_prefix "input"

    window:

        vbox:
            xalign gui.dialogue_text_xalign
            xpos gui.dialogue_xpos
            xsize gui.dialogue_width
            ypos gui.dialogue_ypos

            text prompt style "input_prompt"
            input id "input"

style input_prompt is default

style input_prompt:
    xalign gui.dialogue_text_xalign
    properties gui.text_properties("input_prompt")

style input:
    xalign gui.dialogue_text_xalign
    xmaximum gui.dialogue_width


## Choice screen ###############################################################
##
## This screen is used to display the in-game choices presented by the menu
## statement. The one parameter, items, is a list of objects, each with caption
## and action fields.
##
## https://www.renpy.org/doc/html/screen_special.html#choice

screen choice(items):
    style_prefix "choice"

    vbox:
        for i in items:
            textbutton i.caption action i.action


## When this is true, menu captions will be spoken by the narrator. When false,
## menu captions will be displayed as empty buttons.
define config.narrator_menu = True


style choice_vbox is vbox
style choice_button is button
style choice_button_text is button_text

style choice_vbox:
    xalign 0.5
    ypos 405
    yanchor 0.5

    spacing gui.choice_spacing

style choice_button is default:
    properties gui.button_properties("choice_button")
    activate_sound "audio/UIsounds/cluck.wav" #this should be the name of your sound effect and the file should be in the game folder
    hover_sound "audio/UIsounds/hover.wav"
    mouse "hover"
style choice_button_text is default:
    properties gui.button_text_properties("choice_button")


## Quick Menu screen ###########################################################
##
## The quick menu is displayed in-game to provide easy access to the out-of-game
## menus.

screen quick_menu():

    ## Ensure this appears on top of other screens.
    zorder 100

    if quick_menu:

        hbox:
            style_prefix "quick"

            xalign 0.5
            yalign 1.0

            textbutton _("Back") action Rollback()
            textbutton _("History") action ShowMenu('history')
            textbutton _("Skip") action Skip() alternate Skip(fast=True, confirm=True)
            textbutton "Auto":
                if disableAFMbutton == False:
                    action Preference("auto-forward", "toggle")
            textbutton _("Save"):
                if disableSavebutton == False:
                    action ShowMenu('save')
            #textbutton _("Q.Save") action QuickSave()
            #textbutton _("Q.Load") action QuickLoad()
            textbutton _("Settings") action ShowMenu('preferences')


## This code ensures that the quick_menu screen is displayed in-game, whenever
## the player has not explicitly hidden the interface.
init python:
    config.overlay_screens.append("quick_menu")

default quick_menu = True

style quick_button is default
style quick_button_text is button_text

style quick_button:
    properties gui.button_properties("quick_button")
    activate_sound "audio/UIsounds/cluck.wav" #this should be the name of your sound effect and the file should be in the game folder
    hover_sound "audio/UIsounds/hover.wav"
    mouse "hover"
    #Little buttons under dialoguebox
style quick_button_text:
    properties gui.button_text_properties("quick_button")


################################################################################
## Main and Game Menu Screens
################################################################################

## Navigation screen ###########################################################
##
## This screen is included in the main and game menus, and provides navigation
## to other menus, and to start the game.

screen navigation():

    vbox:
        style_prefix "navigation"

        xpos gui.navigation_xpos
        yalign 0.5

        spacing gui.navigation_spacing

        if main_menu:

            textbutton _("Start") action Start()

        else:

            textbutton _("History") action ShowMenu("history")

            textbutton _("Save"):
                if disableSavebutton == False:
                    action ShowMenu("save")

        textbutton _("Load") action ShowMenu("load")

        textbutton _("Preferences") action ShowMenu("preferences")

        if _in_replay:

            textbutton _("End Replay") action EndReplay(confirm=True)

        elif not main_menu:

            textbutton _("Main Menu") action MainMenu()

        textbutton _("About") action ShowMenu("about")

        if renpy.variant("pc") or (renpy.variant("web") and not renpy.variant("mobile")):

            ## Help isn't necessary or relevant to mobile devices.
            textbutton _("Help") action ShowMenu("help")

        if renpy.variant("pc"):

            ## The quit button is banned on iOS and unnecessary on Android and
            ## Web.
            textbutton _("Quit") action Quit(confirm=not main_menu)

style navigation_button is gui_button
style navigation_button_text is gui_button_text

style navigation_button:
    size_group "navigation"
    properties gui.button_properties("navigation_button")
    activate_sound "audio/UIsounds/cluck.wav" #this should be the name of your sound effect and the file should be in the game folder
    hover_sound "audio/UIsounds/hover.wav"
    mouse "hover"

    #MAIN MENU AND NORMAL MENU SOUNDS^

style navigation_button_text:
    properties gui.button_text_properties("navigation_button")


## Main Menu screen ############################################################
##
## Used to display the main menu when Ren'Py starts.
##
## https://www.renpy.org/doc/html/screen_special.html#main-menu

screen main_menu():

    ## This ensures that any other menu screen is replaced.
    tag menu

    add "gui/main_menu.png"
    imagebutton auto "gui/button/play_%s.png" action Start() style "mainmenunew" pos (84, 448)
    imagebutton auto "gui/button/load_%s.png" action ShowMenu("main_menu_load"), With(Sdissolve) style "mainmenunew" pos (56, 549)
    imagebutton auto "gui/button/settings_%s.png" action ShowMenu("main_menu_settings"), With(Sdissolve) style "mainmenunew" pos(34, 741)
    imagebutton auto "gui/button/gallery_%s.png" action ShowMenu("main_menu_gallery"), With(Sdissolve) style "mainmenunew" pos (37, 643)
    imagebutton auto "gui/button/exit_%s.png" action Quit() style "mainmenunew" pos (76, 832)
    imagebutton auto "gui/button/patreon_%s.png" action OpenURL("https://www.patreon.com/CyanCapsule") style "mainmenunew"
    add "gui/button/title-idle.png"
    add "gui/button/version.png"

style mainmenunew:
    focus_mask True
    activate_sound "audio/UIsounds/cluck.wav"
    hover_sound "audio/UIsounds/hover.wav"
    mouse "hover"

screen main_menu_settings():

    imagebutton auto "gui/button/gallery_%s.png" action NullAction() style "mainmenunew" pos (37, 643)
    imagebutton idle "gui/button/settings_darkbg.png" focus_mask True action [Hide("main_menu_settings"), With(Sdissolve)]

    add "gui/settingsmenu_bg.png"

    modal True

    imagebutton auto "gui/button/settings_%s.png" action [Hide("main_menu_settings"), With(Sdissolve)] style "mainmenunew" pos(34, 741)


    frame:
        area(736, 367, 849, 468)
        background None
        style_prefix "settingsmenu"

        hbox:

            vbox:

                yoffset 10

                if renpy.variant("pc") or renpy.variant("web"):

                    vbox:
                        #style_prefix "radio"
                        label _("Display")
                        textbutton _("Window") action Preference("display", "window")
                        textbutton _("Fullscreen") action Preference("display", "fullscreen")

                null height 0

                vbox:
                    yoffset 0
                    #style_prefix "check"
                    label _("Skip")
                    textbutton _("Unseen Text") action Preference("skip", "toggle")
                    textbutton _("After Choices") action Preference("after choices", "toggle")

                vbox:
                    yoffset 0
                    #style_prefix "check"
                    label _("Language")
                    textbutton _("English") action Language(None)
                    textbutton _("Russian") action Language("russian")

            null width 90

            vbox:
                #style_prefix "slider"
                if not renpy.variant("pc"):
                    yoffset -25
                vbox:

                    label _("Text Speed")

                    bar value Preference("text speed")

                    null height 15

                    label _("Auto-Forward Time")

                    bar value Preference("auto-forward time")

                null height 50

                vbox:

                    label _("Music Volume")

                    hbox:
                        bar value Preference("music volume")

                    null height 15

                    label _("Sound Volume")

                    hbox:
                        bar value Preference("sound volume")

style settingsmenu_label_text:
    color "#ecae76"
    outlines [(4, "#421805", 0, 0)]

style settingsmenu_button_text:
    idle_color "#b48a88"
    hover_color "#d0aea4"
    selected_color "#844f5c"
    outlines [(0, "#EB8D4E", 0, 0)]

style settingsmenu_button:
    selected_background "gui/button/radio_menu.png"
    padding (15, -8, 6, 6)

style settingsmenu_slider:
    base_bar "gui/bar/menu_scrollbar_bg.png"
    thumb "gui/bar/menu_scrollbarbutton_bg.png"
    ysize 40
    mouse "hover"
    hover_sound "audio/UIsounds/hover.wav"

screen main_menu_load():

    imagebutton idle "gui/button/load_darkbg.png" focus_mask True action [Hide("main_menu_load"), With(Sdissolve)]

    add "gui/loadmenu_bg.png"

    modal True

    imagebutton auto "gui/button/load_%s.png" action [Hide("main_menu_load"), With(Sdissolve)] style "mainmenunew" pos (56, 549)

    frame:
        background None
        area (623, 211, 1262, 714)

        default page_name_value = FilePageNameInputValue(pattern=_("Page {}"), auto=_("Automatic saves"), quick=_("Quick saves"))

        fixed:

            ## This ensures the input will get the enter event before any of the
            ## buttons do.
            order_reverse True

            ## The page name, which can be edited by clicking on a button.
            button:
                style "page_label"

                key_events True
                xalign 0.5
                action page_name_value.Toggle()

                input:
                    style "settingsmenu_label_text"
                    layout "subtitle"
                    value page_name_value

            ## The grid of file slots.
            grid gui.file_slot_cols gui.file_slot_rows:
                style_prefix "menuslot"

                xalign 0.5
                yalign 0.5

                for i in range(gui.file_slot_cols * gui.file_slot_rows):

                    $ slot = i + 1

                    button:
                        action FileLoad(slot)

                        has vbox

                        add FileScreenshot(slot) xsize 382 ysize 216 xoffset 10 yoffset 12

                        text FileTime(slot, format=_("{#file_time}%A, %B %d %Y, %H:%M"), empty=_("empty slot")):
                            style "menuslot_button_text"
                            yoffset 20

                        text FileSaveName(slot):
                            style "menuslot_button_text"
                            yoffset 20
                        key "save_delete" action FileDelete(slot)

            ## Buttons to access other pages.
            hbox:
                xalign 0.5
                yalign 1.0

                spacing 8

                textbutton _("<") action FilePagePrevious() text_style "menuslot_button_text" text_size 40

                if config.has_autosave:
                    textbutton _("{#auto_page}A") action FilePage("auto") text_style "menuslot_button_text" text_size 40

                if config.has_quicksave:
                    textbutton _("{#quick_page}Q") action FilePage("quick") text_style "menuslot_button_text" text_size 40

                null width 25

                ## range(1, 10) gives the numbers from 1 to 9.
                for page in range(1, 11):
                    textbutton "[page]" action FilePage(page) text_style "menuslot_button_text" text_size 40

                textbutton _(">") action FilePageNext() text_style "menuslot_button_text" text_size 40

style menuslot_button:
    background "gui/button/menuslot_idle_background.png"
    foreground "gui/button/menuslot_idle_foreground.png"
    hover_foreground "gui/button/menuslot_hover.png"
    xsize 414
    ysize 280

screen main_menu_gallery(page=1, part="Scenes"):
    imagebutton idle "gui/button/gallery_darkbg.png" focus_mask True action [Hide("main_menu_gallery"), With(Sdissolve)]
    add "gui/gallerymenu_bg.png"
    text "Gallery" style "settingsmenu_label_text" xoffset 1210 yoffset 27
    modal True
    imagebutton auto "gui/button/gallery_%s.png" action [Hide("main_menu_gallery"), With(Sdissolve)] style "mainmenunew" pos (37, 643)
    frame:
        background None
        area (629, 80, 1230, 1010)

        grid 3 3:
            xspacing 28
            yspacing 20
            for i in range(0, 9):
                frame:
                    padding (0, 0)
                    xsize 382 ysize 276
                    if page in galleryDict[part] and len(galleryDict[part][page]) >= i+1 and isUnlocked(part, page, i):
                        background "gui/button/menuslot_idle_background.png"
                        add galleryDict[part][page][i].button xoffset 20 yoffset 20
                        button:
                            xsize 392
                            ysize 286
                            idle_background im.MatrixColor("gui/button/hover_scene.png", im.matrix.opacity(0.1))
                            hover_background "gui/button/hover_scene.png"
                            if part == "Images":
                                action ShowMenu("main_menu_galleryPic", galleryDict[part][page][i].image)
                            else:
                                action Replay(galleryDict[part][page][i].label)
                            mouse "hover"
                            hover_sound "audio/UIsounds/hover.wav"
                            text galleryDict[part][page][i].name style "menuslot_button_text" yoffset 110
                        add "gui/button/menuslot_idle_foreground.png"
                    elif page in galleryDict[part] and len(galleryDict[part][page]) >= i+1 and not isUnlocked(part, page, i):
                        background "gui/button/menuslot_idle_background.png"
                        vbox:
                            add "gui/button/menuslot_idle_foreground.png"
                            text "? ? ?" style "menuslot_button_text" yoffset -70
                    else:
                        background None
                        vbox:
                            #add "gui/button/menuslot_idle_foreground.png"
                            #text "empty slot" style "menuslot_button_text" yoffset -70
                            add im.MatrixColor("gui/button/hover_scene.png", im.matrix.opacity(0))
    hbox:
        xoffset 750 yoffset 960
        spacing 10
        button:
            yoffset 24
            text "Scenes" style "galslot_button_text" size 55 xoffset 13 yoffset -25
            selected_background "gui/button/radio_menu.png"
            action ShowMenu("main_menu_gallery", page, "Scenes"), With(Dissolve(0.2)), SelectedIf(part == "Scenes")
        null width 30
        button:
            yoffset 24
            text "Images" style "galslot_button_text" size 55 xoffset 15 yoffset -25
            selected_background "gui/button/radio_menu.png"
            action ShowMenu("main_menu_gallery", page, "Images"), With(Dissolve(0.2)), SelectedIf(part == "Images")
        null width 50
        if page != 1:
            textbutton _("<") action ShowMenu("main_menu_gallery", page=page-1, part=part), With(Dissolve(0.2)) text_style "galslot_button_text" text_size 55
        else:
            textbutton _("<") text_style "menuslot_button_text" text_size 55

        for p in range(1, 11):
            textbutton "[p]" action ShowMenu("main_menu_gallery", page=p, part=part), With(Dissolve(0.2)), SelectedIf(p == page) text_style "galslot_button_text" text_size 55

        if page != 10:
            textbutton _(">") action ShowMenu("main_menu_gallery", page=page+1, part=part), With(Dissolve(0.2)) text_style "galslot_button_text" text_size 55
        else:
            textbutton _(">") text_style "galslot_button_text" text_size 55

screen main_menu_galleryPic(pic, nr=0):
    modal True

    imagebutton idle "gui/ImageBG.png" focus_mask True action [Hide("main_menu_galleryPic"), With(Sdissolve)]

    if type(pic) == type([]):
        imagebutton:
            idle pic[nr]
            if nr+1 >= len(pic):
                action Hide("main_menu_galleryPic")
            else:
                action ShowMenu("main_menu_galleryPic", pic, nr=nr+1)
    else:
        imagebutton:
            idle pic
            action Hide("main_menu_galleryPic")

style menuslot_button_text:
    idle_color "#b48a88"
    hover_color "#d0aea4"
    selected_color "#844f5c"
    selected_hover_color "#a36c79"
    outlines [(0, "#EB8D4E", 0, 0)]
    size 24
    xalign 0.5

style galslot_button_text:
    idle_color "#b48a88"
    hover_color "#d0aea4"
    selected_color "#844f5c"
    selected_hover_color "#a36c79"
    outlines [(0, "#EB8D4E", 0, 0)]
    xalign 0.5

style main_menu_frame is empty
style main_menu_vbox is vbox
style main_menu_text is gui_text
style main_menu_title is main_menu_text
style main_menu_version is main_menu_text

style main_menu_frame:
    xsize 420
    yfill True

    background "gui/overlay/main_menu.png"

style main_menu_vbox:
    xalign 1.0
    xoffset -30
    xmaximum 1200
    yalign 1.0
    yoffset -30

style main_menu_text:
    properties gui.text_properties("main_menu", accent=True)

style main_menu_title:
    properties gui.text_properties("title")

style main_menu_version:
    properties gui.text_properties("version")


## Game Menu screen ############################################################
##
## This lays out the basic common structure of a game menu screen. It's called
## with the screen title, and displays the background, title, and navigation.
##
## The scroll parameter can be None, or one of "viewport" or "vpgrid". When
## this screen is intended to be used with one or more children, which are
## transcluded (placed) inside it.

define Sdissolve = Dissolve(0.2)

screen game_menu():

    tag menu
    imagebutton idle "gui/gamemenu_dark.png" focus_mask True action Return()

    add "gui/gamemenu.png"
    vbox:
        area (114, 224, 258, 708)
        textbutton _("History") action ShowMenu("history"), With(Sdissolve) text_style "settingsmenu_button_text"

        textbutton _("Save"):
            if disableSavebutton == False:
                action ShowMenu("save"), With(Sdissolve) text_style "settingsmenu_button_text"

        textbutton _("Load") action ShowMenu("load"), With(Sdissolve) text_style "settingsmenu_button_text"

        textbutton _("Settings") action ShowMenu("preferences"), With(Sdissolve) text_style "settingsmenu_button_text"

        textbutton _("Main Menu") action MainMenu() text_style "settingsmenu_button_text"

        textbutton _("Credits") action ShowMenu("credits"), With(Sdissolve) text_style "settingsmenu_button_text"

        textbutton _("Key Bindings") action ShowMenu("help"), With(Sdissolve) text_style "settingsmenu_button_text"

        if _in_replay :
            textbutton _("End Replay") action EndReplay(confirm=not main_menu) text_style "settingsmenu_button_text"
        else:
            textbutton _("Exit Game") action Quit(confirm=True) text_style "settingsmenu_button_text"

        textbutton _("Return") action Return() yalign 1.0 text_style "settingsmenu_button_text" text_size 50

style game_menu_outer_frame is empty
style game_menu_navigation_frame is empty
style game_menu_content_frame is empty
style game_menu_viewport is gui_viewport
style game_menu_side is gui_side
style game_menu_scrollbar is gui_vscrollbar

style game_menu_label is gui_label
style game_menu_label_text is gui_label_text

style return_button is navigation_button
style return_button_text is navigation_button_text

style game_menu_outer_frame:
    bottom_padding 45
    top_padding 180

    background "gui/overlay/game_menu.png"

style game_menu_navigation_frame:
    xsize 420
    yfill True

style game_menu_content_frame:
    left_margin 60
    right_margin 30
    top_margin 15

style game_menu_viewport:
    xsize 1380

style game_menu_vscrollbar:
    unscrollable gui.unscrollable

style game_menu_side:
    spacing 15

style game_menu_label:
    xpos 75
    ysize 180

style game_menu_label_text:
    size gui.title_text_size
    color gui.accent_color
    yalign 0.5

style return_button:
    xpos gui.navigation_xpos
    yalign 1.0
    yoffset -45


## About screen ################################################################
##
## This screen gives credit and copyright information about the game and Ren'Py.
##
## There's nothing special about this screen, and hence it also serves as an
## example of how to make a custom screen.

screen about():

    tag menu

    ## This use statement includes the game_menu screen inside this one. The
    ## vbox child is then included inside the viewport inside the game_menu
    ## screen.
    use game_menu(_("About"), scroll="viewport"):

        style_prefix "about"

        vbox:

            label "[config.name!t]"
            text _("Version [config.version!t]\n")

            ## gui.about is usually set in options.rpy.
            if gui.about:
                text "[gui.about!t]\n"

            text _("Made with {a=https://www.renpy.org/}Ren'Py{/a} [renpy.version_only].\n\n[renpy.license!t]")


style about_label is gui_label
style about_label_text is gui_label_text
style about_text is gui_text

style about_label_text:
    size gui.label_text_size


## Load and Save screens #######################################################
##
## These screens are responsible for letting the player save the game and load
## it again. Since they share nearly everything in common, both are implemented
## in terms of a third screen, file_slots.
##
## https://www.renpy.org/doc/html/screen_special.html#save https://
## www.renpy.org/doc/html/screen_special.html#load

screen save():

    tag menu

    use file_slots(_("Save"))


screen load():

    tag menu

    use file_slots(_("Load"))


screen file_slots(title):

    default page_name_value = FilePageNameInputValue(pattern=_("Page {}"), auto=_("Automatic saves"), quick=_("Quick saves"))
    tag menu

    use game_menu()
    frame:
        background None
        area (500, 224, 1213, 708)
        fixed:

            ## This ensures the input will get the enter event before any of the
            ## buttons do.
            order_reverse True

            ## The page name, which can be edited by clicking on a button.
            button:
                style "page_label"

                key_events True
                xalign 0.5
                action page_name_value.Toggle()

                input:
                    style "gamesettings_text"
                    layout "subtitle"
                    value page_name_value

            ## The grid of file slots.
            grid gui.file_slot_cols gui.file_slot_rows:
                style_prefix "menuslot"

                xalign 0.5
                yalign 0.5

                spacing gui.slot_spacing

                for i in range(gui.file_slot_cols * gui.file_slot_rows):

                    $ slot = i + 1

                    button:
                        action FileAction(slot)

                        has vbox

                        add FileScreenshot(slot) xsize 382 ysize 216 xoffset 10 yoffset 12

                        text FileTime(slot, format=_("{#file_time}%A, %B %d %Y, %H:%M"), empty=_("empty slot")):
                            style "menuslot_button_text"
                            yoffset 20

                        text FileSaveName(slot):
                            style "menuslot_button_text"
                            yoffset 20

                        key "save_delete" action FileDelete(slot)

            ## Buttons to access other pages.
            hbox:
                xalign 0.5
                yalign 1.0

                spacing 8

                textbutton _("<") action FilePagePrevious() text_style "menuslot_button_text" text_size 40

                if config.has_autosave:
                    textbutton _("{#auto_page}A") action FilePage("auto") text_style "menuslot_button_text" text_size 40

                if config.has_quicksave:
                    textbutton _("{#quick_page}Q") action FilePage("quick") text_style "menuslot_button_text" text_size 40

                null width 25

                ## range(1, 10) gives the numbers from 1 to 9.
                for page in range(1, 11):
                    textbutton "[page]" action FilePage(page) text_style "menuslot_button_text" text_size 40

                textbutton _(">") action FilePageNext() text_style "menuslot_button_text" text_size 40


style page_label is gui_label
style page_label_text is gui_label_text
style page_button is gui_button
style page_button_text is gui_button_text

style slot_button is gui_button
style slot_button_text is gui_button_text
style slot_time_text is slot_button_text
style slot_name_text is slot_button_text

style page_label:
    xpadding 75
    ypadding 5

style page_label_text:
    text_align 0.5
    layout "subtitle"
    hover_color gui.hover_color

style page_button:
    properties gui.button_properties("page_button")

style page_button_text:
    properties gui.button_text_properties("page_button")

style slot_button:
    properties gui.button_properties("slot_button")

style slot_button_text:
    properties gui.button_text_properties("slot_button")


## Preferences screen ##########################################################
##
## The preferences screen allows the player to configure the game to better suit
## themselves.
##
## https://www.renpy.org/doc/html/screen_special.html#preferences

screen preferences():

    tag menu

    use game_menu()

    vbox:
        area(491, 236, 1300, 691)
        style_prefix "settingsmenu"

        hbox:

            spacing 40

            if renpy.variant("pc") or renpy.variant("web"):

                vbox:
                    #style_prefix "radio"
                    label _("Display") text_style "gamesettings_text"
                    textbutton _("Window") action Preference("display", "window")
                    textbutton _("Fullscreen") action Preference("display", "fullscreen")

            null width 0

            vbox:
                #style_prefix "check"
                label _("Skip") text_style "gamesettings_text"
                textbutton _("Unseen Text") action Preference("skip", "toggle")
                textbutton _("After Choices") action Preference("after choices", "toggle")
                # textbutton _("Transitions") action InvertSelected(Preference("transitions", "toggle"))

            null width 0

            vbox:
                #style_prefix "check"
                label _("Language") text_style "gamesettings_text"
                textbutton _("English") action Language(None)
                textbutton _("Russian") action Language("russian")

        hbox:

            spacing 50

            vbox:

                label _("Text Speed") text_style "gamesettings_text"

                bar value Preference("text speed") xsize 520

                null height 15

                label _("Auto-Forward Time") text_style "gamesettings_text"

                bar value Preference("auto-forward time") xsize 520

            vbox:

                label _("Music Volume") text_style "gamesettings_text"

                hbox:
                    bar value Preference("music volume") xsize 520

                null height 15

                label _("Sound Volume") text_style "gamesettings_text"

                hbox:
                    bar value Preference("sound volume") xsize 520

                textbutton _("Mute All") action Preference("all mute", "toggle") yoffset 20

style gamesettings_text:
    color "#EB8D4E"
    size 45

style pref_label is gui_label
style pref_label_text is gui_label_text
style pref_vbox is vbox

style radio_label is pref_label
style radio_label_text is pref_label_text
style radio_button is gui_button
style radio_button_text is gui_button_text
style radio_vbox is pref_vbox

style check_label is pref_label
style check_label_text is pref_label_text
style check_button is gui_button
style check_button_text is gui_button_text
style check_vbox is pref_vbox

style slider_label is pref_label
style slider_label_text is pref_label_text
style slider_slider is gui_slider
style slider_button is gui_button
style slider_button_text is gui_button_text
style slider_pref_vbox is pref_vbox

style mute_all_button is check_button
style mute_all_button_text is check_button_text

style pref_label:
    top_margin gui.pref_spacing
    bottom_margin 3

style pref_label_text:
    yalign 1.0

style pref_vbox:
    xsize 338

style radio_vbox:
    spacing gui.pref_button_spacing

style radio_button:
    properties gui.button_properties("radio_button")
    foreground "gui/button/radio_[prefix_]foreground.png"

style radio_button_text:
    properties gui.button_text_properties("radio_button")

style check_vbox:
    spacing gui.pref_button_spacing

style check_button:
    properties gui.button_properties("check_button")
    foreground "gui/button/check_[prefix_]foreground.png"

style check_button_text:
    properties gui.button_text_properties("check_button")

style slider_slider:
    xsize 525
    mouse "hover"

style slider_button:
    properties gui.button_properties("slider_button")
    yalign 0.5
    left_margin 15

style slider_button_text:
    properties gui.button_text_properties("slider_button")

style slider_vbox:
    xsize 675


## History screen ##############################################################
##
## This is a screen that displays the dialogue history to the player. While
## there isn't anything special about this screen, it does have to access the
## dialogue history stored in _history_list.
##
## https://www.renpy.org/doc/html/history.html

screen history():

    tag menu

    ## Avoid predicting this screen, as it can be very large.
    predict False

    use game_menu()

    style_prefix "historymenu"

    text "History" style "gamesettings_text" pos (900, 225)

    viewport:
        area (346, 282, 1511, 607)
        scrollbars "vertical"
        side_yfill True
        pagekeys True
        mousewheel True
        draggable True

        vpgrid:
            cols 1
            yinitial 1
            style_prefix "history"

            for h in historyReverse(_history_list):

                window:

                    ## This lays things out properly if history_height is None.
                    has fixed:
                        yfit True

                    if h.who:

                        label h.who:
                            style "history_name"
                            substitute False

                            ## Take the color of the who text from the Character, if
                            ## set.
                            if "color" in h.who_args:
                                text_color h.who_args["color"]
                            text_outlines [(3, "#4f2934", 0, 0)]

                    else:
                        label "-":
                            style "history_name"
                            substitute False
                            text_color "#4f2934"
                            text_outlines [(0, "#4f2934", 0, 0)]

                            ## Take the color of the who text from the Character, if
                            ## set.

                    $ what = renpy.filter_text_tags(h.what, allow=gui.history_allow_tags)
                    text what:
                        color "#4f2934"
                        substitute False
                        outlines [(0, "#4f2934", 0, 0)]

            if not _history_list:
                label _("The dialogue history is empty."):
                    text_outlines [(0, "#4f2934", 0, 0)]


## This determines what tags are allowed to be displayed on the history screen.

define gui.history_allow_tags = { "alt", "noalt" }

style historymenu_vscrollbar:
    base_bar Frame("gui/bar/vscroll.png", 12, 6, 12, 6)
    thumb Frame("gui/bar/vscrollbar.png", 12, 6, 12, 6)
    xsize 40
    mouse "hover"
    hover_sound "audio/UIsounds/hover.wav"

style history_window is empty

style history_name is gui_label
style history_name_text is gui_label_text
style history_text is gui_text

style history_text is gui_text

style history_label is gui_label
style history_label_text is gui_label_text

style history_window:
    xfill True
    ysize gui.history_height

style history_name:
    outlines [(0, "#EB8D4E", 0, 0)]
    xpos gui.history_name_xpos
    xanchor gui.history_name_xalign
    ypos gui.history_name_ypos
    xsize gui.history_name_width

style history_name_text:
    min_width gui.history_name_width
    text_align gui.history_name_xalign

style history_text:
    xpos gui.history_text_xpos
    ypos gui.history_text_ypos
    xanchor gui.history_text_xalign
    xsize gui.history_text_width
    min_width gui.history_text_width
    text_align gui.history_text_xalign
    layout ("subtitle" if gui.history_text_xalign else "tex")

style history_label:
    xfill True

style history_label_text:
    xalign 0.5


## Help screen #################################################################
##
## A screen that gives information about key and mouse bindings. It uses other
## screens (keyboard_help, mouse_help, and gamepad_help) to display the actual
## help.

screen help():

    tag menu

    default device = "keyboard"

    use game_menu()

    style_prefix "historymenu"

    hbox:
        pos (446, 185)
        textbutton _("Keyboard") action SetScreenVariable("device", "keyboard") text_style "settingsmenu_button_text"
        textbutton _("Mouse") action SetScreenVariable("device", "mouse") text_style "settingsmenu_button_text"

        if GamepadExists():
            textbutton _("Gamepad") action SetScreenVariable("device", "gamepad") text_style "settingsmenu_button_text"

    viewport:
        area (446, 282, 1411, 607)
        scrollbars "vertical"
        side_yfill True
        pagekeys True
        mousewheel True
        draggable True

        vbox:
            style_prefix "helpnew"
            spacing 23

            if device == "keyboard":
                use keyboard_help
            elif device == "mouse":
                use mouse_help
            elif device == "gamepad":
                use gamepad_help

style helpnew_label_text:
    color "#EB8D4E"
    outlines [(0, "#EB8D4E", 0, 0)]
    size 45
    xalign 1.0
    text_align 1.0

style helpnew_label:
    xsize 375
    right_padding 30

style helpnew_text:
    color "#4f2934"
    size 40

#style helpnew_hbox:
#    spacing 20
#    xalign 0.5

screen keyboard_help():

    hbox:
        label _("Enter")
        text _("Advances dialogue and activates the interface.")

    hbox:
        label _("Space")
        text _("Advances dialogue without selecting choices.")

    hbox:
        label _("Arrow Keys")
        text _("Navigate the interface.")

    hbox:
        label _("Escape")
        text _("Accesses the game menu.")

    hbox:
        label _("Ctrl")
        text _("Skips dialogue while held down.")

    hbox:
        label _("Tab")
        text _("Toggles dialogue skipping.")

    hbox:
        label _("Page Up")
        text _("Rolls back to earlier dialogue.")

    hbox:
        label _("Page Down")
        text _("Rolls forward to later dialogue.")

    hbox:
        label "H"
        text _("Hides the user interface.")

    hbox:
        label "S"
        text _("Takes a screenshot.")

    hbox:
        label "V"
        text _("Toggles assistive ")
        textbutton _("{a=https://www.renpy.org/l/voicing}{color=#80B0D8}self-voicing{/a}.") text_style "credits_button_text" text_size 40 action NullAction()


screen mouse_help():

    hbox:
        label _("Left Click")
        text _("Advances dialogue and activates the interface.")

    hbox:
        label _("Middle Click")
        text _("Hides the user interface.")

    hbox:
        label _("Right Click")
        text _("Accesses the game menu.")

    #hbox:
    #    label _("Mouse Wheel Up\nClick Rollback Side")
    #    text _("Rolls back to earlier dialogue.")

    hbox:
        label _("Mouse Wheel Down")
        text _("Rolls forward to later dialogue.")


screen gamepad_help():

    hbox:
        label _("Right Trigger\nA/Bottom Button")
        text _("Advances dialogue and activates the interface.")

    hbox:
        label _("Left Trigger\nLeft Shoulder")
        text _("Rolls back to earlier dialogue.")

    hbox:
        label _("Right Shoulder")
        text _("Rolls forward to later dialogue.")


    hbox:
        label _("D-Pad, Sticks")
        text _("Navigate the interface.")

    hbox:
        label _("Start, Guide")
        text _("Accesses the game menu.")

    hbox:
        label _("Y/Top Button")
        text _("Hides the user interface.")

    textbutton _("Calibrate") action GamepadCalibrate()


style help_button is gui_button
style help_button_text is gui_button_text
style help_label is gui_label
style help_label_text is gui_label_text
style help_text is gui_text

style help_button:
    properties gui.button_properties("help_button")
    xmargin 12

style help_button_text:
    properties gui.button_text_properties("help_button")

style help_label:
    xsize 375
    right_padding 30

style help_label_text:
    size gui.text_size
    xalign 1.0
    text_align 1.0



################################################################################
## Additional screens
################################################################################


## Confirm screen ##############################################################
##
## The confirm screen is called when Ren'Py wants to ask the player a yes or no
## question.
##
## https://www.renpy.org/doc/html/screen_special.html#confirm

screen confirm(message, yes_action, no_action):

    ## Ensure other screens do not get input while this screen is displayed.
    modal True

    zorder 200

    style_prefix "confirm"

    imagebutton idle "gui/confirm_dark.png" focus_mask True action Hide(screen="confirm")

    add "gui/confirm_bg.png"

    frame:
        background None
        vbox:
            xalign .5
            yalign .5
            spacing 45

            label _(message):
                style "newconfirm_prompt"

            hbox:
                xalign 0.5
                spacing 150

                textbutton _("Yes") action yes_action text_style "settingsmenu_button_text"
                textbutton _("No") action no_action text_style "settingsmenu_button_text"

    ## Right-click and escape answer "no".
    key "game_menu" action no_action

style newconfirm_prompt_text:
    color "#4f2934"
    size 40
    text_align 0.5
    layout "subtitle"
    outlines [(0, "#EB8D4E", 0, 0)]

style newconfirm_prompt is gui_prompt
style newconfirm_prompt_text is gui_prompt_text

style confirm_frame is gui_frame
style confirm_prompt is gui_prompt
style confirm_prompt_text is gui_prompt_text
style confirm_button is gui_medium_button
style confirm_button_text is gui_medium_button_text

style confirm_frame:
    background Frame([ "gui/confirm_frame.png", "gui/frame.png"], gui.confirm_frame_borders, tile=gui.frame_tile)
    padding gui.confirm_frame_borders.padding
    xalign .5
    yalign .5

style confirm_prompt_text:
    text_align 0.5
    layout "subtitle"

style confirm_button:
    properties gui.button_properties("confirm_button")

style confirm_button_text:
    properties gui.button_text_properties("confirm_button")


## Skip indicator screen #######################################################
##
## The skip_indicator screen is displayed to indicate that skipping is in
## progress.
##
## https://www.renpy.org/doc/html/screen_special.html#skip-indicator

screen skip_indicator():

    zorder 100
    style_prefix "skip"

    frame:

        hbox:
            spacing 9

            text _("Skipping")

            text "▸" at delayed_blink(0.0, 1.0) style "skip_triangle"
            text "▸" at delayed_blink(0.2, 1.0) style "skip_triangle"
            text "▸" at delayed_blink(0.4, 1.0) style "skip_triangle"


## This transform is used to blink the arrows one after another.
transform delayed_blink(delay, cycle):
    alpha .5

    pause delay

    block:
        linear .2 alpha 1.0
        pause .2
        linear .2 alpha 0.5
        pause (cycle - .4)
        repeat


style skip_frame is empty
style skip_text is gui_text
style skip_triangle is skip_text

style skip_frame:
    ypos gui.skip_ypos
    background Frame("gui/skip.png", gui.skip_frame_borders, tile=gui.frame_tile)
    padding gui.skip_frame_borders.padding

style skip_text:
    size gui.notify_text_size

style skip_triangle:
    ## We have to use a font that has the BLACK RIGHT-POINTING SMALL TRIANGLE
    ## glyph in it.
    font "DejaVuSans.ttf"


## Notify screen ###############################################################
##
## The notify screen is used to show the player a message. (For example, when
## the game is quicksaved or a screenshot has been taken.)
##
## https://www.renpy.org/doc/html/screen_special.html#notify-screen

screen notify(message):

    zorder 100
    style_prefix "notify"

    frame at notify_appear:
        text "[message!tq]"

    timer 3.25 action Hide('notify')


transform notify_appear:
    on show:
        alpha 0
        linear .25 alpha 1.0
    on hide:
        linear .5 alpha 0.0


style notify_frame is empty
style notify_text is gui_text

style notify_frame:
    ypos gui.notify_ypos

    background Frame("gui/notify.png", gui.notify_frame_borders, tile=gui.frame_tile)
    padding gui.notify_frame_borders.padding

style notify_text:
    properties gui.text_properties("notify")


## NVL screen ##################################################################
##
## This screen is used for NVL-mode dialogue and menus.
##
## https://www.renpy.org/doc/html/screen_special.html#nvl


screen nvl(dialogue, items=None):

    window:
        style "nvl_window"

        has vbox:
            spacing gui.nvl_spacing

        ## Displays dialogue in either a vpgrid or the vbox.
        if gui.nvl_height:

            vpgrid:
                cols 1
                yinitial 1.0

                use nvl_dialogue(dialogue)

        else:

            use nvl_dialogue(dialogue)

        ## Displays the menu, if given. The menu may be displayed incorrectly if
        ## config.narrator_menu is set to True, as it is above.
        for i in items:

            textbutton i.caption:
                action i.action
                style "nvl_button"

    add SideImage() xalign 0.0 yalign 1.0


screen nvl_dialogue(dialogue):

    for d in dialogue:

        window:
            id d.window_id

            fixed:
                yfit gui.nvl_height is None

                if d.who is not None:

                    text d.who:
                        id d.who_id

                text d.what:
                    id d.what_id


## This controls the maximum number of NVL-mode entries that can be displayed at
## once.
define config.nvl_list_length = gui.nvl_list_length

style nvl_window is default
style nvl_entry is default

style nvl_label is say_label
style nvl_dialogue is say_dialogue

style nvl_button is button
style nvl_button_text is button_text

style nvl_window:
    xfill True
    yfill True

    background "gui/nvl.png"
    padding gui.nvl_borders.padding

style nvl_entry:
    xfill True
    ysize gui.nvl_height

style nvl_label:
    xpos gui.nvl_name_xpos
    xanchor gui.nvl_name_xalign
    ypos gui.nvl_name_ypos
    yanchor 0.0
    xsize gui.nvl_name_width
    min_width gui.nvl_name_width
    text_align gui.nvl_name_xalign

style nvl_dialogue:
    xpos gui.nvl_text_xpos
    xanchor gui.nvl_text_xalign
    ypos gui.nvl_text_ypos
    xsize gui.nvl_text_width
    min_width gui.nvl_text_width
    text_align gui.nvl_text_xalign
    layout ("subtitle" if gui.nvl_text_xalign else "tex")

style nvl_thought:
    xpos gui.nvl_thought_xpos
    xanchor gui.nvl_thought_xalign
    ypos gui.nvl_thought_ypos
    xsize gui.nvl_thought_width
    min_width gui.nvl_thought_width
    text_align gui.nvl_thought_xalign
    layout ("subtitle" if gui.nvl_text_xalign else "tex")

style nvl_button:
    properties gui.button_properties("nvl_button")
    xpos gui.nvl_button_xpos
    xanchor gui.nvl_button_xalign

style nvl_button_text:
    properties gui.button_text_properties("nvl_button")



################################################################################
## Mobile Variants
################################################################################

style pref_vbox:
    variant "medium"
    xsize 675

## Since a mouse may not be present, we replace the quick menu with a version
## that uses fewer and bigger buttons that are easier to touch.
screen quick_menu():
    variant "touch"

    zorder 100

    if quick_menu:

        hbox:
            style_prefix "quick"

            xalign 0.5
            yalign 1.0

            textbutton _("Back") action Rollback()
            textbutton _("Skip") action Skip() alternate Skip(fast=True, confirm=True)
            textbutton _("Auto") action Preference("auto-forward", "toggle")
            textbutton _("Menu"):
                if disableSavebutton == False:
                    action ShowMenu()


style window:
    variant "small"
    background "gui/phone/textbox.png"

style radio_button:
    variant "small"
    foreground "gui/phone/button/radio_[prefix_]foreground.png"

style check_button:
    variant "small"
    foreground "gui/phone/button/check_[prefix_]foreground.png"

style nvl_window:
    variant "small"
    background "gui/phone/nvl.png"

style main_menu_frame:
    variant "small"
    background "gui/phone/overlay/main_menu.png"

style game_menu_outer_frame:
    variant "small"
    background "gui/phone/overlay/game_menu.png"

style game_menu_navigation_frame:
    variant "small"
    xsize 510

style game_menu_content_frame:
    variant "small"
    top_margin 0

style pref_vbox:
    variant "small"
    xsize 600

style bar:
    variant "small"
    ysize gui.bar_size
    left_bar Frame("gui/phone/bar/left.png", gui.bar_borders, tile=gui.bar_tile)
    right_bar Frame("gui/phone/bar/right.png", gui.bar_borders, tile=gui.bar_tile)

style vbar:
    variant "small"
    xsize gui.bar_size
    top_bar Frame("gui/phone/bar/top.png", gui.vbar_borders, tile=gui.bar_tile)
    bottom_bar Frame("gui/phone/bar/bottom.png", gui.vbar_borders, tile=gui.bar_tile)

style scrollbar:
    variant "small"
    ysize gui.scrollbar_size
    base_bar Frame("gui/phone/scrollbar/horizontal_[prefix_]bar.png", gui.scrollbar_borders, tile=gui.scrollbar_tile)
    thumb Frame("gui/phone/scrollbar/horizontal_[prefix_]thumb.png", gui.scrollbar_borders, tile=gui.scrollbar_tile)

style vscrollbar:
    variant "small"
    xsize gui.scrollbar_size
    base_bar Frame("gui/phone/scrollbar/vertical_[prefix_]bar.png", gui.vscrollbar_borders, tile=gui.scrollbar_tile)
    thumb Frame("gui/phone/scrollbar/vertical_[prefix_]thumb.png", gui.vscrollbar_borders, tile=gui.scrollbar_tile)

style slider:
    variant "small"
    ysize gui.slider_size
    base_bar Frame("gui/phone/slider/horizontal_[prefix_]bar.png", gui.slider_borders, tile=gui.slider_tile)
    thumb "gui/phone/slider/horizontal_[prefix_]thumb.png"

style vslider:
    variant "small"
    xsize gui.slider_size
    base_bar Frame("gui/phone/slider/vertical_[prefix_]bar.png", gui.vslider_borders, tile=gui.slider_tile)
    thumb "gui/phone/slider/vertical_[prefix_]thumb.png"

style slider_vbox:
    variant "small"
    xsize None

style slider_slider:
    variant "small"
    xsize 900

init -1 python:
    renpy.register_shader("MyPigPrincess.fade_bar", variables = """
        uniform float u_shader_time;
        uniform float u_duration;

        uniform sampler2D tex0;
        uniform vec2 u_model_size;

        attribute vec2 a_tex_coord;
        varying vec2 v_coords;
    """, fragment_functions="""
        uniform float u_shader_time;
        uniform float u_duration;

        float sample_alpha(in sampler2D tex, in vec2 coords) {
            float progress = u_shader_time / u_duration;
            coords.x -= progress;
            if (coords.x < 0.0) return 0.0;
            else return texture2D(tex, coords).a;
        }

    """,vertex_200 = """
        v_coords = a_tex_coord;
    """, fragment_300="""
        vec4 color = texture2D(tex0, v_coords);
        color *= sample_alpha(tex0, v_coords);
        gl_FragColor = color;
    """
    )

    renpy.register_shader("MyPigPrincess.animate_bell", variables = """
        uniform float u_shader_time;
        uniform float u_duration;

        uniform sampler2D tex0;
        uniform vec2 u_model_size;

        attribute vec2 a_tex_coord;
        varying vec2 v_coords;
    """, fragment_functions="""
        vec4 sample(in sampler2D tex, in vec2 coords) {
            if (coords.x < 0.0 || coords.y < 0.0 || coords.x > 1.0 || coords.y > 1.0) return vec4(0.0);
            else return texture2D(tex, coords);
        }

        vec2 scale_coords(in vec2 coords, in float scale) {
            coords -= 0.5;
            coords /= scale;
            coords += 0.5;
            return coords;
        }

    """,vertex_200 = """
        v_coords = a_tex_coord;
    """, fragment_300="""
        #define PI 3.1415926535897932384626433832795
        #define SPB (60.0 / 140.1)
        float beat_time = 0.8;
        float beat = mod(u_shader_time, SPB) / SPB;
        if (beat < beat_time) beat = smoothstep (0.0, 1.0, beat / beat_time);
        else beat = smoothstep (1.0, 0.0, (beat - beat_time) / (1.0 - beat_time));
        vec4 color = sample(tex0, scale_coords(v_coords, 1.0 - 0.04 * beat));
        gl_FragColor = color;
    """
    )

init -1:
    default cutspveryslow = False
    default cutspslow = False
    default cutspmedium = False
    default cutspfast = False
    default cutspveryfast = False

init:
    python:
        class Timer():
            def __init__(self, screen, duration, failure_label):
                self.screen = screen
                self.failure_label = failure_label
                self.duration = duration
                self.banished = False
                self.zero_time = False
                self.pause_time = False
                self.defused = False
                self.pause_duration = 0.0
                self.time_sans_pause_time = 0.0

            def paused(self):
                if renpy.get_screen(self.screen):
                    return False
                else:
                    return True

            def time(self):
                if self.pause_time:
                    return self.pause_time - self.pause_duration
                else:
                    return self.time_sans_pause_time - self.pause_duration

            def mark_time(self, time):
                if not self.zero_time:
                    self.zero_time = time
                self.time_sans_pause_time = time - self.zero_time
                if self.paused():
                    if not self.pause_time:
                        self.pause_time = self.time_sans_pause_time
                else:
                    if self.pause_time:
                        self.pause_duration += self.time_sans_pause_time - self.pause_time
                        self.pause_time = False
                return 0

            def end_cutgame(self):
                if self.defused:
                    renpy.hide_screen(self.screen)
                else:
                    self.fail_cutgame()

            def fail_cutgame(self):
                renpy.hide_screen(self.screen)
                renpy.jump(self.failure_label)

            def finished(self):
                return self.banished or self.time() >= self.duration

            def progress(self):
                return self.time() / self.duration

        timer = None

        def set_global_timer(new_timer):
            global timer
            timer = new_timer

        def banish_timer():
            global timer
            timer.banished = True
            renpy.hide_screen(timer.screen)
            renpy.with_statement(Dissolve(0.3))

        def win_cutgame():
            global timer
            timer.defused = True
            t = timer.time()

            global cutspveryslow
            global cutspslow
            global cutspmedium
            global cutspfast
            global cutspveryfast

            cutspslow = False
            cutspmedium = False
            cutspfast = False
            cutspveryfast = False
            cutspveryslow = False

            # Change victory dialogue thresholds here

            if t < 23:
                cutspveryfast = True
            elif t < 29:
                cutspfast = True
            elif t < 40:
                cutspmedium = True
            elif t < 57:
                cutspslow = True
            else:
                cutspveryslow = True

        def bar_fade(timer, model_based_rendering):

            def model_transform_function(trans, st, at):
                timer.mark_time(at)
                trans.shader = "MyPigPrincess.fade_bar"
                trans.mesh = True
                trans.u_shader_time = 0.0
                trans.u_duration = timer.duration
                trans.u_shader_time = timer.time()
                return 0

            def non_model_transform_function(trans, st, at):
                timer.mark_time(at)
                val = round(1548.0 * timer.progress())
                trans.offset = (val, 0)
                trans.crop = (val, 0, 2000, 100)
                return 0

            if model_based_rendering:
                return model_transform_function
            else:
                return non_model_transform_function

        def animate_bell(timer, model_based_rendering):
            def model_transform_function(trans, st, at):
                trans.shader = "MyPigPrincess.animate_bell"
                trans.mesh = True
                trans.u_shader_time = 0.0
                trans.u_duration = timer.duration
                trans.u_shader_time = timer.time()
                return 0

            def non_model_transform_function(trans, st, at):
                return None

            if model_based_rendering:
                return model_transform_function
            else:
                return non_model_transform_function

        def animate_highlight(timer, model_based_rendering):
            def model_transform_function(trans, st, at):
                trans.xpos = 155 + round(1548.0 * timer.progress())
                return 0
            def non_model_transform_function(trans, st, at):
                trans.xpos = 155 + round(1548.0 * timer.progress())
                return 0

            if model_based_rendering:
                return model_transform_function
            else:
                return non_model_transform_function

        def check_timer(timer):
            if timer.finished():
                timer.end_cutgame()

transform bar_transform_shader(timer, model_based_rendering):
    xpos 156
    ypos 26
    function bar_fade(timer, model_based_rendering)

transform highlight_transform(timer, model_based_rendering):
    ypos 26
    function animate_highlight(timer, model_based_rendering)

transform bell_transform_shader(timer, model_based_rendering):
    xpos 1697
    ypos 2
    function animate_bell(timer, model_based_rendering)

screen minigametimer(duration, failure_label):
    default timer = Timer("minigametimer", duration, failure_label)
    timer 0.001 repeat False action [SetScreenVariable("timer", Timer("minigametimer", duration, failure_label)),
                                     Function(set_global_timer, timer)]
    timer 0.1 repeat True action Function(check_timer, timer)
    fixed:
        ypos 15
        add "bar"
        add "rednewcropped" at bar_transform_shader(timer, renpy.get_renderer_info()["models"])
        add "barhighlightcropped" at highlight_transform(timer, renpy.get_renderer_info()["models"]) alpha 0.4
        add "belluicropped" at bell_transform_shader(timer, renpy.get_renderer_info()["models"])


transform timer_transform():
    ypos 15

label disable_saving:
    $ _game_menu_screen = "history"
    $ disableSavebutton = True
    return

label enable_saving:
    $ _game_menu_screen = "save"
    $ disableSavebutton = False
    $ renpy.block_rollback()
    return

label enable_minigame_mode:
    $ _skipping = False
    $ _dismiss_pause = False
    $ _rollback = False
    $ renpy.block_rollback()
    return

label disable_minigame_mode:
    $ _skipping = True
    $ _dismiss_pause = True
    $ _rollback = True
    $ renpy.block_rollback()
    return

screen positionable_choice(items, xpos=None, ypos=None):
    style_prefix "choice"

    vbox:
        if xpos != None:
            xpos xpos
        if ypos != None:
            ypos ypos
        for i in items:
            textbutton i.caption action i.action

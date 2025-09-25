import pyray as ray


class Engine:
    # 3d
    camera3d = ray.Camera3D()
    camera3d.position = ray.Vector3(10, 10, 10)
    camera3d.target = ray.Vector3(0, 0, 0)
    camera3d.up = ray.Vector3(0, 1, 0)
    camera3d.projection = ray.CameraProjection.CAMERA_ORTHOGRAPHIC
    camera3d.fovy = 12.0

    # 2d

    def __init__(self, app) -> None:
        self.app = app
        #
        self.load_fonts()

    def update(self):
        #
        pass

    def draw(self):
        #
        ray.begin_drawing()
        #
        ray.clear_background(ray.WHITE)
        # debug text
        self.debug_text()
        #
        self.draw_3d()
        self.draw_2d()
        #
        ray.end_drawing()

    def draw_2d(self):
        #
        pass

    def draw_3d(self):
        ray.begin_mode_3d(self.camera3d)
        # grid
        ray.draw_grid(20, 0.5)
        # big orange cube
        ray.draw_cube_v((0, 1, 0), (2, 2, 2), ray.ORANGE)
        ray.draw_cube_wires_v((0, 1, 0), (2, 2, 2), ray.MAROON)
        # small blue cube
        ray.draw_cube_v((1.5, 0.5, 0.5), (1, 1, 1), ray.BLUE)
        ray.draw_cube_wires_v((1.5, 0.5, 0.5), (1, 1, 1), ray.DARKBLUE)
        #
        ray.end_mode_3d()

    def debug_text(self):
        self.draw_text("Performance " + str(ray.get_fps()) + " fps", 0)
        self.draw_text(
            "Application Running " + str(ray.get_time())[0:5] + " seconds", 1
        )
        self.draw_text("AdwaitaMonoNerdFont_Regular_24", 2)
        pass

    DEBUG_LINEHEIGHT = 24

    def draw_text(self, text: str, line: int = 0):
        ray.draw_text_ex(
            self.AdwaitaMonoNerdFont_Regular_24,
            text,
            (0, self.DEBUG_LINEHEIGHT * line),
            24,
            0,
            ray.BLACK,
        )

    AdwaitaMonoNerdFont_Regular_24: ray.Font
    fonts_texture_filter = ray.TextureFilter.TEXTURE_FILTER_BILINEAR

    def load_fonts(self):
        #
        self.AdwaitaMonoNerdFont_Regular_24 = ray.load_font_ex(
            "src/resources/fonts/AdwaitaMono/AdwaitaMonoNerdFont-Regular.ttf",
            24,
            None,
            250,
        )
        ray.set_texture_filter(
            self.AdwaitaMonoNerdFont_Regular_24.texture, self.fonts_texture_filter
        )
        #

    def exit(self):
        ray.unload_font(self.AdwaitaMonoNerdFont_Regular_24)

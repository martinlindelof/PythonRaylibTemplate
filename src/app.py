import pyray as ray

from engine import Engine

TITLE = "App"
WINDOW_WIDTH, WINDOW_HEIGHT = 1000, 800


class Application:
    """The Application Singleton"""

    ray.init_window(WINDOW_WIDTH, WINDOW_HEIGHT, TITLE)
    ray.set_target_fps(60)

    engine: Engine

    def __init__(self) -> None:
        self.delta_time = 0.0
        self.engine = Engine(app=self)

    def run(self):
        while not ray.window_should_close():
            self.delta_time = ray.get_frame_time()
            self.engine.update()
            self.engine.draw()
        self.exit()

    def exit(self):
        # Exit code here
        self.engine.exit()
        # Close window and un-load opengl context
        ray.close_window()

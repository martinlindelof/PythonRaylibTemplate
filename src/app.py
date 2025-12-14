import pyray as ray

from engine import Engine


class Application:
    """The Application Singleton"""

    WINDOW_WIDTH, WINDOW_HEIGHT = 1000, 800
    TITLE = "App"

    _instance: "Application | None" = None
    _initialized: bool = False

    ray.init_window(WINDOW_WIDTH, WINDOW_HEIGHT, TITLE)
    ray.set_target_fps(60)

    engine: Engine

    def __new__(cls) -> "Application":
        # Singleton impl
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self) -> None:
        if not self._initialized:
            self._initialized = True
            self.engine = Engine(app=self)

    def run(self):
        while not ray.window_should_close():
            self.engine.update()
            self.engine.draw()
        self.exit()  # Exiting the loop

    def exit(self):
        # Exit code here
        self.engine.exit()
        # Close window and un-load opengl context
        ray.close_window()

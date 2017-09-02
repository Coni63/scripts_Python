import pyglet
import random

class MyWindow(pyglet.window.Window):
    def __init__(self, windows_settings):
        super(MyWindow, self).__init__(**windows_settings)
        self.set_minimum_size(400, 300)
        pyglet.gl.glPointSize(6)
        pyglet.gl.glLineWidth(1)
        self.pts = []
        for i in range(300):
            self.pts.append([random.randrange(0, 800), random.randrange(0, 600), random.randrange(0, 100)])

    def update(self, freq):
        pass

    def on_mouse_press(self, x, y, button, modifiers):
        print(x, y, button, modifiers)

    def on_mouse_release(self, x, y, button, modifiers):
        pass

    def on_mouse_drag(self, x, y, dx, dy, buttons, modifiers):
        # if buttons == 1:
        #     print(dx, dy)
        # elif buttons == 4:
        #     print(dx, dy)
        angleY = dx * 0.02
        angleX = dy * 0.02
        pyglet.gl.glLoadIdentity();
        pyglet.gl.glRotatef(angleX, 1.0, 0.0, 0.0);
        pyglet.gl.glRotatef(angleY, 0.0, 1.0, 0.0);


    def project(self):
        pyglet.gl.glViewport(0,0,800, 600)
        pyglet.gl.glMatrixMode(pyglet.gl.GL_PROJECTION)
        pyglet.gl.glLoadIdentity()
        pyglet.gl.glOrtho(0, 500, 0, 400, 0, 100)
        pyglet.gl.glMatrixMode(pyglet.gl.GL_MODELVIEW)

    def on_draw(self):
        self.clear()
        #self.project()
        pyglet.gl.glBegin(pyglet.gl.GL_POINTS)
        for pt in self.pts:
            pyglet.gl.glVertex3i(*pt)
        pyglet.gl.glEnd()


if __name__ == "__main__":
    setup_window = {
            "width": 800,
            "height": 600,
            "resizable": True,
            "caption": "test"
    }

    window = MyWindow(setup_window)
    pyglet.clock.schedule_interval(window.update, 1/24)
    pyglet.app.run()
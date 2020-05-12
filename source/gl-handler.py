##
##  Isolation Pong graphics handler
##  @version 0.01
##  @author Ben Hemsworth <ben_hemsworth@hotmail.co.uk>

from OpenGL.GL import *
from OpenGL.GLU import *
import glfw


def drawScreen():
    glClearColor(0.2,0.2,0.2, 1)
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    ###rendering here


def setup():
    glfw.init()

    glfw.window_hint(glfw.DOUBLEBUFFER, glfw.TRUE)
    window = glfw.create_window(800,600, "Isolation Pong", None, None)

    glfw.make_context_current(window)
    glfw.swap_interval(2)

    while not glfw.window_should_close(window):
        drawScreen()

        glfw.swap_buffers(window)
        glfw.poll_events()

    glfw.terminate()

setup()

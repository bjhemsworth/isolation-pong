##
##  Isolation Pong graphics handler
##  @version 0.01
##  @author Ben Hemsworth <ben_hemsworth@hotmail.co.uk>

import pathlib

from OpenGL.GL import *
##from OpenGL.GLU import *
import glfw


def load_shader(shader_file, GL_SHADER_TYPE):
    shader_ID = glCreateShader(GL_SHADER_TYPE)

    ## Load shaders in same folder as this file
    shader_file_location = pathlib.Path(__file__).parent.absolute() / shader_file

    file = open(shader_file_location, 'r')
    shader_source = file.read()

    glShaderSource(shader_ID, shader_source)
    glCompileShader(shader_ID)

    return shader_ID


def draw_screen():
    glClearColor(0.2,0.2,0.2, 1)
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    ###rendering here


def setup():

    glfw.init()
    glfw.window_hint(glfw.DOUBLEBUFFER, glfw.TRUE)
    window = glfw.create_window(800,600, "Isolation Pong", None, None)
    glfw.make_context_current(window)
    glfw.swap_interval(2)


    program_ID = glCreateProgram();
    glAttachShader(program_ID, load_shader('./simple.frag', GL_FRAGMENT_SHADER))
    glAttachShader(program_ID, load_shader('./simple.vert', GL_VERTEX_SHADER))
    glLinkProgram(program_ID)


    while not glfw.window_should_close(window):
        draw_screen()

        glfw.swap_buffers(window)
        glfw.poll_events()

    glfw.terminate()

setup()

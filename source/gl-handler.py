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

    file = open(shader_file_location, 'rt')
    shader_source = file.read()

    glShaderSource(shader_ID, shader_source)
    glCompileShader(shader_ID)

    return shader_ID

def load_obj(obj_file):
    obj_file_location = pathlib.Path(__file__).parent.absolute() / "obj" / obj_file


    ## Return all newlines as \n
    file = open(obj_file_location, 'rt', newline = None)
    vertex = []
    normals = []
    indices = []
    while True:
        raw = file.readline()
        if raw == '':
            break
        data_list = raw.strip().split(' ')
        data_type = data_list[0]
        if data_type == 'v':
            vertex.extend(data_list[1:])
        elif data_type == 'vn':
            normals.extend(data_list[1:])
        elif data_type == 'f':
            indices.extend(data_list[1:])
        else:
            pass
    return vertex, normals, indices





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

    

    v, n, i = load_obj('box.obj')


    while not glfw.window_should_close(window):
        draw_screen()

        glfw.swap_buffers(window)
        glfw.poll_events()

    glfw.terminate()


setup()

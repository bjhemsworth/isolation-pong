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

    if glGetShaderiv(shader_ID, GL_COMPILE_STATUS) == GL_FALSE:
        print(shader_file + " not compiled")

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


def glfw_setup():

    glfw.init()
    glfw.window_hint(glfw.CLIENT_API, glfw.OPENGL_API)
    glfw.window_hint(glfw.DOUBLEBUFFER, glfw.TRUE)
    glfw.window_hint(glfw.CONTEXT_VERSION_MAJOR, 4)
    glfw.window_hint(glfw.CONTEXT_VERSION_MINOR, 6)
    global window
    window = glfw.create_window(800,600, "Isolation Pong", None, None)
    glfw.make_context_current(window)
    glfw.swap_interval(2)


def gl_program_setup():

    global program_ID
    program_ID = glCreateProgram();
    vertex_s = load_shader('./simple.vert', GL_VERTEX_SHADER)
    fragment_s = load_shader('./simple.frag', GL_FRAGMENT_SHADER)
    glAttachShader(program_ID, vertex_s)
    glAttachShader(program_ID, fragment_s)
    glLinkProgram(program_ID)

    if glGetProgramiv(program_ID, GL_LINK_STATUS) == GL_FALSE:
        print("Program not linked")

    ## Progam linking sends shaders to the GPU and local references can now be removed
    glDetachShader(program_ID, vertex_s)
    glDeleteShader(vertex_s)

    glDetachShader(program_ID, fragment_s)
    glDeleteShader(fragment_s)




glfw_setup()
gl_program_setup()



attrib = glGetAttribLocation(program_ID, 'a_test')

v, n, i = load_obj('box.obj')


while not glfw.window_should_close(window):
    draw_screen()

    glfw.swap_buffers(window)
    glfw.poll_events()

glfw.terminate()

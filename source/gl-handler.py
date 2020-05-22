##
##  Isolation Pong graphics handler
##  @version 0.01
##  @author Ben Hemsworth <ben_hemsworth@hotmail.co.uk>

import pathlib

from OpenGL.GL import *
##from OpenGL.GLU import *
import glfw
import numpy as np


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


## PyOpenGL doesnt like python lists, return Numpy arrays where possible
def load_obj(obj_file):
    obj_file_location = pathlib.Path(__file__).parent.absolute() / "obj" / obj_file


    ## Return all newlines as \n
    file = open(obj_file_location, 'rt', newline = None)
    vertex = []
    normal = []
    vertex_indices = []
    normal_indices = []
    while True:
        raw = file.readline()
        if raw == '':
            break
        data_list = raw.strip().split(' ')
        data_type = data_list[0]
        if data_type == 'v':
            vertex.extend(data_list[1:])
        elif data_type == 'vn':
            normal.extend(data_list[1:])
        elif data_type == 'f':
            for item in data_list[1:]:
                vert_i, _, norm_i = item.strip().split('/')
                vertex_indices.extend(vert_i)
                normal_indices.extend(norm_i)
        else:
            pass
    return (np.array(vertex, dtype=np.float32),
           np.array(normal, dtype=np.float32),
           np.array(vertex_indices, dtype=np.uint8),
           np.array(normal_indices, dtype=np.uint8))




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

    program_ID = glCreateProgram();
    vertex_s = load_shader('./simple.vert', GL_VERTEX_SHADER)
    fragment_s = load_shader('./simple.frag', GL_FRAGMENT_SHADER)
    glAttachShader(program_ID, vertex_s)
    glAttachShader(program_ID, fragment_s)
    glLinkProgram(program_ID)

    if glGetProgramiv(program_ID, GL_LINK_STATUS) != GL_TRUE:
        print("Program not linked")

    glValidateProgram(program_ID)
    if glGetProgramiv(program_ID, GL_VALIDATE_STATUS) != GL_TRUE:
        print("Invalid program")


    ## Progam linking sends shaders to the GPU and local references can now be removed
    glDetachShader(program_ID, vertex_s)
    glDeleteShader(vertex_s)

    glDetachShader(program_ID, fragment_s)
    glDeleteShader(fragment_s)

    return program_ID


glfw_setup()

program = gl_program_setup()

glUseProgram(program)

vertices= np.array((-1.0, -1.0, 0.0, 1.0, -1.0, 0.0, 0.0, 1.0, 0.0),dtype=np.float32);
color = np.array((1.0, 0.0, 0.0, 1.0, 0.0, 0.0, 1.0, 1.0, 0.0, 1.0, 0.0, 1.0),dtype=np.float32)

VAO=glGenVertexArrays(1)
glBindVertexArray(VAO)

vert_b, col_b = glGenBuffers(2)
glBindBuffer(GL_ARRAY_BUFFER, vert_b)
glBufferData(GL_ARRAY_BUFFER, vertices, GL_STATIC_DRAW)
glVertexAttribPointer(0, 3, GL_FLOAT, GL_FALSE, 0, None)
glEnableVertexAttribArray(0)


glBindBuffer(GL_ARRAY_BUFFER, col_b)
glBufferData(GL_ARRAY_BUFFER, color.size*4 ,color, GL_STATIC_DRAW)
glVertexAttribPointer(1, 4, GL_FLOAT, GL_FALSE, 0, None)
glEnableVertexAttribArray(1)

glBindBuffer(GL_ARRAY_BUFFER,0)
glBindVertexArray(0)



glClearColor(0.2,0.2,0.2, 1)

while not glfw.window_should_close(window):
    glClear(GL_COLOR_BUFFER_BIT)
    glUseProgram(program)

    glBindVertexArray(VAO)
    glDrawArrays(GL_TRIANGLES, 0, 3);
    glBindVertexArray(0)


    glfw.swap_buffers(window)
    glfw.poll_events()

glfw.terminate()

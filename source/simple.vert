#version 460

layout (location = 0) in vec3 vertex_pos;
layout (location = 1) in vec4 vertex_col;
out vec4 color;

void main()
{
    gl_Position = vec4(vertex_pos.x, vertex_pos.y, vertex_pos.z, 1.0);
    color = vertex_col;
}

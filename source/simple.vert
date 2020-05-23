#version 460


layout (location = 2) in mat4 m_modelview;
layout (location = 3) in mat4 m_projection;

layout (location = 0) in vec3 v_position;
//layout (location = 1) in vec3 v_indices;
out vec4 color;

void main()
{
    vec3 v_color = (v_position +1) /2;

    gl_Position = vec4(v_position.x, v_position.y, v_position.z, 1.0);
    color = vec4(v_color,1);
}

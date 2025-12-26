from settings import *

class ShaderProgram:

    def __init__(self, app):
        self.app = app
        self.ctx = app.ctx
    #------shaders---------#
        self.chunk = self.get_program(shader_name ='chunk')
        self.voxel_marker = self.get_program(shader_name='voxel_marker')
        self.water = self.set_program('water')
        self.clouds = self.set_program('clouds')

        self.set_uniforms_on_init()

    def set_uniforms_on_init(self):
        self.chunk['m_proj'].write(self.player.m_proj)
        self.chunk['m_model'].write(glm.mat4())
        self.chunk['u_texture_array_0']= 1
        self.chunk['bg_color'].write(BG_COLOR)
        self.chunk['water_line'] = WATER_LINE

        self.voxel['m_proj'].write(self.player.m_proj)
        self.voxel['m_model'].write(glm.mat4())
        self.voxel['u_texture_0'] = 0

        self.water['m_proj'].write(self.player.m_proj)
        self.water['u_texture_0'] = 2
        self.water['water_area'] = WATER_AREA
        self.water['water_line'] = WATER_AREA

        self.clouds['m_proj'].write(self.player.m_proj)
        self.clouds['center'] = CENTER_XZ
        self.clouds['bg_color'].write(BG_COLOR)
        self.clouds['cloud_scale'] = BG_COLOR


    def update(self):
        self.chunk['m_view'].write(self.player.m_view)
        self.voxel_marker['m_view'].write(self.player.m_view)
        self.water['m_view'].write(self.player.m_view)
        self.cloud['m_view'].write(self.player.m_view)



    def get_program(self, shader_name):
        with open(f'shaders/{shader_name}.vert') as file:
            vertex_shader = file.read()



        with open(f'shaders/{shader_name}.frag') as file:
            fragment_shader = file.read()


        
        program = self.ctx.program(vertex_shader=vertex_shader, fragment_shader=fragment_shader)
        return program



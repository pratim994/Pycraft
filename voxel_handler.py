from settings import*
from meshes.chunk_mesh_builder import get_chunk_index

class VoxelHandler:
    def __init__(self, world):
        self.app = world.app
        self.chunks = world.chunks

        self.chunk = None
        self.voxel_id = None
        self.voxel_index = None
        self.voxel_local_pos = None
        self.voxel_world_pos = None
        self.voxel_normal = None

        self.interaction_mode = 0
        self.new_voxel_id = DIRT

    def add_voxel(self):
        if self.voxel_id:
            result = self.get_voxel_id(self.voxel_world_pos + self.voxel_normal)

            if not result[0]:
                _, voxel_index, _, chunk = result
                chunk.voxels[voxel_index] = self.new_voxel_id
                chunk.mesh.rebuild()

                if chunk.is_empty():
                    chunk.is_empty = False

    def rebuild_adj_chunk(self, adj_voxel_pos):
        index = get_chunk_index(adj_voxel_pos)
        if index != -1:
                self.chunks[index].mesh.rebuild()
    def rebuild_adj_chunks(self):
        lx, ly, lz = self.voxel_local_pos
        wx, wy, wz = self.voxel_world_pos

        if lx == 0:
            self.rebuild_adj_chunk((wx-1,wy,wz))
        elif lx == CHUNK_SIZE - 1:
            self.rebuild_adj_chunk((wx+1, wy, wz))

        if ly == 0:
            self.rebuild_adj_chunk(wx, wy-1, wz)
        elif ly == CHUNK_SIZE-1:
            self.rebuild_adj_chunk(wx, wy+1, wz)

        if lz == 0:
            self.rebuild_adj_chunk(wx, wy, wz-1)
        elif lz == CHUNK_SIZE-1:
            self.rebuild_adj_chunk(wx, wy, wz+1)

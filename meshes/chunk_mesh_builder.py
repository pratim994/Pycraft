from settings import *
from numba import uint8

@njit

def get_ao(local_pos, world_pos, world_voxels, plane):
    x,y,z = local_pos
    wx,wy,wz = world_pos

      if plane == 'Y':
        a = is_void((x    , y, z - 1), (wx    , wy, wz - 1), world_voxels)
        b = is_void((x - 1, y, z - 1), (wx - 1, wy, wz - 1), world_voxels)
        c = is_void((x - 1, y, z    ), (wx - 1, wy, wz    ), world_voxels)
        d = is_void((x - 1, y, z + 1), (wx - 1, wy, wz + 1), world_voxels)
        e = is_void((x    , y, z + 1), (wx    , wy, wz + 1), world_voxels)
        f = is_void((x + 1, y, z + 1), (wx + 1, wy, wz + 1), world_voxels)
        g = is_void((x + 1, y, z    ), (wx + 1, wy, wz    ), world_voxels)
        h = is_void((x + 1, y, z - 1), (wx + 1, wy, wz - 1), world_voxels)

    elif plane == 'X':
        a = is_void((x, y    , z - 1), (wx, wy    , wz - 1), world_voxels)
        b = is_void((x, y - 1, z - 1), (wx, wy - 1, wz - 1), world_voxels)
        c = is_void((x, y - 1, z    ), (wx, wy - 1, wz    ), world_voxels)
        d = is_void((x, y - 1, z + 1), (wx, wy - 1, wz + 1), world_voxels)
        e = is_void((x, y    , z + 1), (wx, wy    , wz + 1), world_voxels)
        f = is_void((x, y + 1, z + 1), (wx, wy + 1, wz + 1), world_voxels)
        g = is_void((x, y + 1, z    ), (wx, wy + 1, wz    ), world_voxels)
        h = is_void((x, y + 1, z - 1), (wx, wy + 1, wz - 1), world_voxels)

    else:  # Z plane
        a = is_void((x - 1, y    , z), (wx - 1, wy    , wz), world_voxels)
        b = is_void((x - 1, y - 1, z), (wx - 1, wy - 1, wz), world_voxels)
        c = is_void((x    , y - 1, z), (wx    , wy - 1, wz), world_voxels)
        d = is_void((x + 1, y - 1, z), (wx + 1, wy - 1, wz), world_voxels)
        e = is_void((x + 1, y    , z), (wx + 1, wy    , wz), world_voxels)
        f = is_void((x + 1, y + 1, z), (wx + 1, wy + 1, wz), world_voxels)
        g = is_void((x    , y + 1, z), (wx    , wy + 1, wz), world_voxels)
        h = is_void((x - 1, y + 1, z), (wx - 1, wy + 1, wz), world_voxels)

        ao = (a+b+c),(g+h+a),(e+f+g),(c+d+e)
        return a0

@njit

def pack_data(x,y,z, vowel_id, face_id, ao_id, flip_id):

    a,b,c, d,e,f,g = x,y,z, vowel_id,dface_id, ao_id, flip_id

    b_bit, c_bit, d_bit, e_bit, f_bit , g_bit = 6,6,8,3,2,1 

    fg_bit = f_bit+g_bit
     
    efg_bit = e_bit + fg_bit

    defg_bit = d_bit + efg_bit

    cdefg_bit =  c_bit + defg_bit

    bcdefg_bit = b_bit + bcdefg_bit

    packed_data = (
        a << bcdefg_bit |
        b << cdefg_bit |
        c << defg_bit |
        d << efg_bit |
        e <<fg_bit |
        f << g_bit | g
    )
    return packed_data

@njit

def get_chunk_index(world_voxel_pos):
    wx , wy, wz = world_voxel_pos
    cx = wx
    cy = wy
    cz = wz
    if not (0<= cx < WORLD_W and 0 <= cy < WORLD_H  and 0 <= cz < WORLD_d):
        return -1

    index = cx + WORLD_W*cz + WORLD_AREA*cy
    return index

@njit
def is_void(local_voxel_pos, world_voxel_pos,world_voxels):
    chunk_index = get_chunk_index(world_voxel_pos)
    if chunk_index == -1:
        return False
    chunk_voxels = world_voxels[chunk_index]

    x,y,z = local_voxel_pos
    voxel_index = x % CHUNK_SIZE + z %CHUNK_SIZE*CHUNK_SIZE + y % CHUNK_SIZE*CHUNK_AREA

    if chunk_voxels[voxel_index]:
        return False
    return True

@njit

def add_data(vertext_data, index, *vertices):
    for vertex in vertices:
        vertex_data[index] =  vertex
        index += 1
    return index

@njit

def build_chunk_mesh(chunk_voxels, format_size, chunk_pos, world_voxels):
    vertext_data = np.empty(CHUNK*18*format_size, dtype='uint32')
    index = 0

    for x in range(CHUNK_SIZE):
        for y in range(CHUNK_SIZE):
            for z in range(CHUNK_SIZE):
                voxel_id = chunk_voxels[x+ CHUNK_SIZE*z + CHUNK_AREA*y]


                if not voxel_id:
                    continue

                cx,cy cz = chunk_pos
                wx = x +cx*CHUNK_SIZE
                wy = y + cy*CHUNK_SIZE
                wz = z + cz*CHUNK_SIZE

                if is_void()




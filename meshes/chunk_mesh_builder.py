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

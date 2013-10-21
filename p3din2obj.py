import struct

def main():
    print 'started'
    data = open('test.bin').read()
    cursor = 0
    # start parsing
    header = struct.unpack('12sxxxxxxxxIIIIIIIIIII', data[cursor:0x40])
    cursor += 0x40
    # basic counts
    vertex_count = header[1]
    normal_count = header[2]
    uv_count = header[3]
    # tri face counts
    tri_faces_p = header[4]
    tri_faces_pn = header[5]
    tri_faces_pu = header[6]
    tri_faces_pun = header[7]
    # quad face counts
    quad_faces_p = header[8]
    quad_faces_pn = header[9]
    quad_faces_pu = header[10]
    quad_faces_pun = header[11]

    print 'version %s' % header[0]
    print '%s vertices' % vertex_count
    print '%s normals' % normal_count
    print '%s uvs' % uv_count
    print '%s total tris' % (tri_faces_p + tri_faces_pn + tri_faces_pu + tri_faces_pun)
    print '%s total quads' % (quad_faces_p + quad_faces_pn + quad_faces_pu + quad_faces_pun)

    print 'parsed header'

    

if __name__ == '__main__':
    main()

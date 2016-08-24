
# Python 2/3 compatibility
from __future__ import print_function

import numpy as np
from matplotlib import pyplot as plt
import cv2

ply_header = '''ply
format ascii 1.0
element vertex %(vert_num)d
property float x
property float y
property float z
property uchar red
property uchar green
property uchar blue
end_header
'''

def write_ply(fn, verts, colors):
    verts = verts.reshape(-1, 3)
    colors = colors.reshape(-1, 3)
    verts = np.hstack([verts, colors])
    with open(fn, 'wb') as f:
        f.write((ply_header % dict(vert_num=len(verts))).encode('utf-8'))
        np.savetxt(f, verts, fmt='%f %f %f %d %d %d ')


if __name__ == '__main__':
    print('loading images...')
    imgL = cv2.imread('aloeL.jpg', cv2.CV_LOAD_IMAGE_GRAYSCALE)  # downscale images for faster processing
    imgR = cv2.imread('aloeR.jpg', cv2.CV_LOAD_IMAGE_GRAYSCALE)

    # disparity range is tuned for 'aloe' image pair
    window_size = 3
    min_disp = 16
    num_disp = 112-min_disp
    stereo = cv2.StereoBM(cv2.STEREO_BM_BASIC_PRESET, ndisparities=num_disp, SADWindowSize=5)


    print('computing disparity...')
    disp = stereo.compute(imgL, imgR)
               # .astype(np.float32) / 16.0

    print('generating 3d point cloud...',)
    h, w = imgL.shape[:2]
    f = 0.8*w                          # guess for focal length
    Q = np.float32([[1, 0, 0, -0.5*w],
                    [0,-1, 0,  0.5*h], # turn points 180 deg around x-axis,
                    [0, 0, 0,     -f], # so that y-axis looks up
                    [0, 0, 1,      0]])
    points = cv2.reprojectImageTo3D(disp, Q)
    # colors = cv2.cvtColor(imgL, cv2.COLOR_BGR2RGB)
    mask = disp > disp.min()
    out_points = points[mask]
    # out_colors = colors[mask]
    # out_fn = 'out.ply'
    # write_ply('out.ply', out_points, out_colors)
    print('%s saved' % 'out.ply')

    plt.imshow(disp, 'gray')
    plt.figure()
    plt.imshow((disp-min_disp)/num_disp, 'gray')
    plt.show()
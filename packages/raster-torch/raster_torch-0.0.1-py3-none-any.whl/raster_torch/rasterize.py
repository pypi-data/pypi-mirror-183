import torch

from stroke2image_utils import *

def to_delXY(sketch, device='cpu'):
    new_skech = torch.vstack((torch.tensor([0., 0., 0.], device = device), sketch.clone()))
    new_skech[:-1,:2]  = new_skech[1:,:2] - new_skech[:-1,:2]
    new_skech[:-1, 2] = new_skech[1:, 2]
    return new_skech[:-1,:]

def to_Five_Point(sketch_points, max_seq_length, device='cpu'):
    len_seq = len(sketch_points[:, 0])
    new_seq = torch.zeros((max_seq_length, 5), device = device)
    new_seq[0:len_seq, :2] = sketch_points[:, :2]
    new_seq[0:len_seq, 3] = sketch_points[:, 2]
    new_seq[0:len_seq, 2] = 1 - new_seq[0:len_seq, 3]
    new_seq[(len_seq - 1):, 4] = 1
    new_seq[(len_seq - 1), 2:4] = 0
    new_seq = torch.cat([torch.zeros((1, 5),device=device), new_seq], dim=0)
    return new_seq, len_seq

def vec_to_sketch(points, device='cpu'):
    
    points.to(device)
    max_len = len(points)
    five_point, len_seq = to_Five_Point(to_delXY(points), max_len)
    
    five_point = five_point.unsqueeze(0).detach()
    five_point.requires_grad=True
    pixel_dims = torch.tensor([256., 256.]).to(device)
    padding = torch.round(torch.min(pixel_dims) / 10) * 2
    padding.to(device)
    

    sketch_vector = five_point
    stroke_gt_scaled = scale_and_center_strokes(sketch_vector, sketch_vector[:, :, 0:2], pixel_dims, padding)
    pixel_gt = strokes_to_image(stroke_gt_scaled, pixel_dims)    

    return pixel_gt, five_point
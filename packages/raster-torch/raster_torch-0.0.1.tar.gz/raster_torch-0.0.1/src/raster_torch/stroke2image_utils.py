import torch
import numpy as np

def scale_and_center_strokes(input_strokes, stroke_gt, pixel_dims, padding, device='cuda'):
    """
    Vectorized / differentiable scaling and centering function.
    Computes scaling and shift parameter based on stroke_gt to maximize size given pixel dimensions and padding.
    Applies these parameters to input_strokes to scale them.
    :param input_strokes:
    :param stroke_gt:
    :param pixel_dims:
    :param padding:
    :return:
    """
    shift_=[]
    scale_=[]
    for i,_ in enumerate(input_strokes):

        stroke_gt_abs = torch.cumsum(stroke_gt[i].unsqueeze(0), dim=1)
        min_x, max_x = torch.min(stroke_gt_abs[:, :, 0], dim=1)[0], torch.max(stroke_gt_abs[:, :, 0], dim=1)[0]
        min_y, max_y = torch.min(stroke_gt_abs[:, :, 1], dim=1)[0], torch.max(stroke_gt_abs[:, :, 1], dim=1)[0]
        # print(padding)
        
        curr_im_pts = torch.tensor([[min_x, max_x], [min_y, max_y]]).to(device)
        # print("Shape",curr_im_pts.shape)

        scale = torch.reshape(pixel_dims - padding, (1, -1)) / torch.reshape(torch.max(max_x - min_x, max_y - min_y)[0], shape=(-1, 1))
        scale = torch.reshape(scale, (-1, 1, 2))
        shift = (torch.reshape(pixel_dims, (1, 1, -1)) - torch.reshape(torch.sum(curr_im_pts, dim=1), (-1, 1, 2)) * scale) / 2.0
        scale_.append(scale.squeeze())
        shift_.append(shift.squeeze())
        # print("scale", scale.shape)

    shift = torch.stack(shift_).view(-1,1,2)
    scale = torch.stack(scale_).view(-1,1,2)
    # print(shift.shape)
    # print(scale.shape)
    scaled_strokes = input_strokes[:, :, 0:2] * scale
    scaled_and_centered_strokes = torch.cat((scaled_strokes[:, 0:1, 0:2] + shift, scaled_strokes[:, 1:, 0:2]), dim=1)
    scaled_and_centered_strokes = torch.cat((scaled_and_centered_strokes, input_strokes[:, :, 2:]), dim=-1)

    return scaled_and_centered_strokes

def strokes_to_image(strokes, image_dim,device='cuda'):
    """
    Given strokes, produce a greyscale image of dimensions image_dim.
    Pixel intensity is computed based off euclidean distance from rendered line segments described by strokes.
    :param strokes:
    :param image_dim:
    :return:
    """
    # print(strokes)

    batch_size = strokes.shape[0]
    relative_xy, pen = strokes[:, :, 0:2], strokes[:, :, 2:]
    abs_xy = torch.cumsum(relative_xy, dim=1).to(device)



    p_1, p_2 = (torch.reshape(x, (batch_size, 1, -1, 2)) for x in (abs_xy[:, :-1, :], abs_xy[:, 1:, :]))
    p_3 = torch.reshape(
        torch.stack(
            torch.meshgrid([
                torch.tensor(range(0, int(image_dim[0].item())), device = device, dtype=torch.float32),
                torch.tensor(range(0, int(image_dim[1].item())), device=device, dtype=torch.float32)
                ]), 
            dim=-1), 
        (1, -1, 1, 2))

    p_3.to(device)
    
    ab, ac, bc = p_2 - p_1, p_3 - p_1, p_3 - p_2

    # Computes AB . AC
    ab_dot_ac = torch.einsum("ikl,ijkl->ijk", ab[:, 0], ac)
    ab_cross_ac = (ab[:, :, :, 0] * ac[:, :, :, 1]) - (ab[:, :, :, 1] * ac[:, :, :, 0])
    ab_norm_sq = torch.sum(ab ** 2, dim=-1)

    pix_dist = torch.where(ab_dot_ac < 0,
                        torch.sum(ac ** 2, dim=-1),
                        torch.where(ab_dot_ac > ab_norm_sq, torch.sum(bc ** 2, dim=-1), (ab_cross_ac ** 2) / (ab_norm_sq + 1e-4)))

    pen_mask = torch.reshape(pen[:, :-1, 0], (batch_size, 1, -1))
    pix_dist += torch.where(pen_mask > 0.5, torch.zeros(pix_dist.shape,device=device), torch.ones(pix_dist.shape, device=device) * 1e6)
    min_dist = torch.min(pix_dist, dim=-1)[0]

    pix = torch.sigmoid(2 - 5. * min_dist)

    return torch.reshape(pix, (batch_size, 1, int(image_dim[0].item()), int(image_dim[1].item()))).permute(0, 1, 3, 2)

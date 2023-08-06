import numpy as np

iteration = 0


class MotionModel2D:
    def __init__(self, selection, **kwargs):
        ''' Creates a 2D fan-beam motion model.

        :param selection: string selecting one of the types below
        :param kwargs: selection specific additional arguments like number of projections/ number of spline nodes
        '''
        if selection == 'rigid_2d':
            assert 'num_projections' in kwargs.keys(), 'Please provide the num_projections argument for the motion model.'
            self.free_parameters_per_node = 3
            self.free_parameters = self.free_parameters_per_node * kwargs['num_projections']
            self.eval = self.rigid_2d
        else:
            print('This model is not implemented.')

    def rigid_2d(self, free_params, projection_matrices_input):
        '''Computes out = P @ M for M being a 2d rigid transformation matrix

        :param free_params: params for M; (r, tx, ty) for each projection as 1D numpy array of size 3*num_projections
        :param projection_matrices_input: the best guess for good projection matrices as 3D numpy array of size
        2x3xnum_projections
        :return: the motion adjusted projection matrices as 3D numpy array of size 2x3xnum_projections
        '''
        num_projections = projection_matrices_input.shape[2]
        assert (free_params.shape[0] == self.free_parameters), 'Wrong input to motion model rigid_2d.'

        free_params = np.asarray(np.split(free_params, num_projections))
        rotations = np.zeros((2, 2, num_projections))
        rotations[0, 0, :] = - np.sin(free_params[:, 0])
        rotations[0, 1, :] = np.cos(free_params[:, 0])
        rotations[1, 0, :] = np.cos(free_params[:, 0])
        rotations[1, 1, :] = np.sin(free_params[:, 0])

        translations = np.zeros((2, 1, num_projections))
        translations[0, :, :] = free_params[:, 1]
        translations[1, :, :] = free_params[:, 2]

        # lower row of 0s and 1s to make a 4x4 transformation matrix
        lower_row = np.zeros((1, 3, num_projections))
        lower_row[:, 2, :] = 1

        rigid_transform = np.concatenate((np.concatenate((rotations, translations), 1), lower_row), 0)
        # apply matrix multiplication along third dimension
        out = np.einsum('ijn,jkn->ikn', projection_matrices_input, rigid_transform)

        return out


if __name__ == '__main__':
    m = MotionModel2D('rigid_2d', num_projections=360)
    proj_mats_updated = m.eval(np.random.rand(360 * 3), np.random.rand(2, 3, 360))
    print('bla')
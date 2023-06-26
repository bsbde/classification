import os

import cv2

74


class GrayMarginCutter:

    def __init__(self, dir: str) -> None:
        dir_list = os.listdir(dir)
        img_files = [os.path.join(dir, x) for x in dir_list]
        self.imgs = list()
        self.names = list()
        for img_file in img_files:
            self.imgs.append(cv2.imread(img_file))
            self.names.append(img_file[img_file.rfind('/') + 1:])

    def __call__(self, save_path) -> None:
        if not os.path.exists(save_path):
            os.mkdir(save_path)

        for idx, img in enumerate(self.imgs):
            # print(img.shape)
            ori_width, ori_height = img.shape[0], img.shape[1]
            # print(ori_width, ori_height)
            self.imgs[idx] = img[int(ori_width * 0.1): ori_width - int(ori_width * 0.1),
                             int(ori_height * 0.1): ori_height - int(ori_height * 0.1)]
            cv2.imwrite(os.path.join(save_path, self.names[idx]), self.imgs[idx])

        print("processing end!")


dir = '../../../../DataSet/deep-learning-course-phase-project-1/train/Delta wings/'
grayCutter = GrayMarginCutter(dir)
grayCutter('../../../../DataSet/deep-learning-course-phase-project-1/train/New Delta wings/')
processing
end!
dir = '../../../../DataSet/deep-learning-course-phase-project-1/train/Forward-swept wings/'
grayCutter = GrayMarginCutter(dir)
grayCutter('../../../../DataSet/deep-learning-course-phase-project-1/train/New Forward-swept wings/')
processing
end!
dir = '../../../../DataSet/deep-learning-course-phase-project-1/train/Helicopter/'
grayCutter = GrayMarginCutter(dir)
grayCutter('../../../../DataSet/deep-learning-course-phase-project-1/train/Helicopter/')
processing
end!
dir = '../../../../DataSet/deep-learning-course-phase-project-1/train/Paragliding/'
grayCutter = GrayMarginCutter(dir)
grayCutter('../../../../DataSet/deep-learning-course-phase-project-1/train/Paragliding/')
processing
end!
dir = '../../../../DataSet/deep-learning-course-phase-project-1/train/Quadcopter/'
grayCutter = GrayMarginCutter(dir)
grayCutter('../../../../DataSet/deep-learning-course-phase-project-1/train/Quadcopter/')
processing
end!
dir = '../../../../DataSet/deep-learning-course-phase-project-1/train/Seaplane/'
grayCutter = GrayMarginCutter(dir)
grayCutter('../../../../DataSet/deep-learning-course-phase-project-1/train/Seaplane/')
processing
end!
dir = '../../../../DataSet/deep-learning-course-phase-project-1/train/Biplane/'
grayCutter = GrayMarginCutter(dir)
grayCutter('../../../../DataSet/deep-learning-course-phase-project-1/train/Biplane/')
processing
end!
dir = '../../../../DataSet/deep-learning-course-phase-project-1/train/Fighter plane/'
grayCutter = GrayMarginCutter(dir)
grayCutter('../../../../DataSet/deep-learning-course-phase-project-1/train/Fighter plane/')
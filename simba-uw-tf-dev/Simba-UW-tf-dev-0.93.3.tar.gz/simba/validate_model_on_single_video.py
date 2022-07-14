import warnings
warnings.filterwarnings('ignore',category=FutureWarning)
warnings.filterwarnings('ignore',category=DeprecationWarning)
import pickle
from configparser import ConfigParser, MissingSectionHeaderError, NoSectionError, NoOptionError
import cv2
import warnings
from simba.drop_bp_cords import createColorListofList, getBpNames, create_body_part_dictionary, drop_bp_cords
import matplotlib.pyplot as plt
import numpy as np
from PIL import Image
from simba.rw_dfs import *
from simba.features_scripts.unit_tests import *
from simba.misc_tools import (find_video_of_file,
                              get_fn_ext,
                              check_multi_animal_status,
                              get_video_meta_data,
                              plug_holes_shortest_bout,
                              get_bouts_for_gantt,
                              create_gantt_img,
                              resize_gantt)
from simba.features_scripts.unit_tests import read_video_info_csv, read_video_info
from simba.read_config_unit_tests import read_config_entry

plt.interactive(True)
plt.ioff()
warnings.simplefilter(action='ignore', category=FutureWarning)

class ValidateModelOneVideo(object):
    def __init__(self,
                 ini_path=None,
                 feature_file_path=None,
                 model_path=None,
                 d_threshold=None,
                 shortest_bout=None,
                 create_gantt='None'):
        self.ini_path = ini_path
        self.config = ConfigParser()
        try:
            self.config.read(self.ini_path)
        except MissingSectionHeaderError:
            raise AssertionError(('ERROR:  Not a valid project_config file. Please check the project_config.ini path.'))
        _, self.feature_filename, ext = get_fn_ext(feature_file_path)
        self.create_gantt = create_gantt
        self.discrimination_threshold = float(d_threshold)
        self.shortest_bout = shortest_bout
        self.project_folder = read_config_entry(config=self.config, section='General settings', option='project_path', data_type='folder_path')
        self.cnt_animals = read_config_entry(config=self.config, section='General settings', option='animal_no', data_type='int')
        self.file_type = read_config_entry(config=self.config, section='General settings', option='workflow_file_type', data_type='str', default_value='csv')
        self.video_folder = os.path.join(self.project_folder, 'videos')
        self.output_folder = os.path.join(self.project_folder, 'frames', 'output', 'validation')
        if not os.path.exists(self.output_folder): os.makedirs(self.output_folder)
        self.vid_info_df = read_video_info_csv(os.path.join(self.project_folder, 'logs', 'video_info.csv'))
        vid_info_df = read_video_info_csv(os.path.join(self.project_folder, 'logs', 'video_info.csv'))
        self.video_settings, self.px_per_mm, self.fps = read_video_info(vid_info_df, self.feature_filename)
        self.clf_name = os.path.basename(model_path).replace('.sav', '')
        self.vid_output_path = os.path.join(self.output_folder, '{} {}{}'.format(self.feature_filename, self.clf_name, '.avi'))
        self.clf = pickle.load(open(model_path, 'rb'))
        self.in_df = read_df(feature_file_path, self.file_type)

    def perform_clf(self):
        self.data_df = drop_bp_cords(self.in_df, self.ini_path)
        self.prob_col_name = 'Probability_' + self.clf_name
        self.data_df[self.prob_col_name] = self.clf.predict_proba(self.data_df)[:, 1]
        self.data_df[self.clf_name] = np.where(self.data_df[self.prob_col_name] > self.discrimination_threshold, 1, 0)

    def plug_small_bouts(self):
        self.data_df = plug_holes_shortest_bout(data_df=self.data_df, clf_name=self.clf_name, fps=self.fps, shortest_bout=self.shortest_bout)

    def save_classification_data(self):
        self.save_path = os.path.join(self.output_folder, self.feature_filename + '.' + self.file_type)
        save_df(self.data_df, self.file_type, self.save_path)
        print('Predictions created for video' + self.feature_filename + '...')


    def create_video(self):
        multi_animal_status, multi_animal_id_lst = check_multi_animal_status(self.config, self.cnt_animals)
        x_cols, y_cols, p_cols = getBpNames(self.ini_path)
        video_file_path = find_video_of_file(self.video_folder, self.feature_filename)
        cap = cv2.VideoCapture(video_file_path)
        fourcc = cv2.VideoWriter_fourcc(*'DIVX')
        video_meta_dict = get_video_meta_data(video_file_path)

        if video_meta_dict['height'] < video_meta_dict['width']:
            video_height, video_width = video_meta_dict['width'], video_meta_dict['height']
            flip_flag = True
        else:
            video_height, video_width = video_meta_dict['height'], video_meta_dict['width']
            flip_flag = False

        if self.create_gantt == 'None':
            writer = cv2.VideoWriter(self.vid_output_path, fourcc, self.fps, (video_width, video_height))

        space_scaler, radius_scaler, resolution_scaler, font_scaler = 60, 20, 1500, 1.5
        max_dim = max(video_width, video_height)
        circleScale = int(radius_scaler / (resolution_scaler / max_dim))
        font_size = float(font_scaler / (resolution_scaler / max_dim))
        spacingScale = int(space_scaler / (resolution_scaler / max_dim))
        font = cv2.FONT_HERSHEY_TRIPLEX
        color_lst = createColorListofList(self.cnt_animals, int(len(x_cols)/self.cnt_animals) + 1)
        animalBpDict = create_body_part_dictionary(multi_animal_status, multi_animal_id_lst, self.cnt_animals, x_cols, y_cols, p_cols, color_lst)
        if self.create_gantt != 'None':
            bouts_df = get_bouts_for_gantt(data_df=self.data_df, clf_name=self.clf_name, fps=self.fps)
            gantt_img = create_gantt_img(bouts_df, self.clf_name, len(self.data_df), self.fps, 'Behavior gantt chart (entire session)')
            if flip_flag:
                gantt_img = resize_gantt(gantt_img, video_width)
            else:
                gantt_img = resize_gantt(gantt_img, video_height)
            writer = cv2.VideoWriter(self.vid_output_path, fourcc, self.fps, (int(video_width + gantt_img.shape[1]), int(video_height)))

        frm_cnt, clf_cnt = 0, 0
        while (cap.isOpened()):
            try:
                clf_cnt += int(self.data_df.loc[frm_cnt, self.clf_name])
                clf_val = int(self.data_df.loc[frm_cnt, self.clf_name])
                ret, frame = cap.read()
                for animal_name, animal_data in animalBpDict.items():
                    id_flag = False
                    for bp in range(len(animal_data['X_bps'])):
                        x_header, y_header = animal_data['X_bps'][bp], animal_data['Y_bps'][bp]
                        animal_cords = tuple(self.in_df.loc[self.in_df.index[frm_cnt], [x_header, y_header]])
                        cv2.circle(frame, (int(animal_cords[0]), int(animal_cords[1])), 0, animal_data['colors'][bp], circleScale)
                        if ('centroid' in x_header.lower()) or ('center' in  x_header.lower()) and not id_flag:
                            cv2.putText(frame, animal_name, (int(animal_cords[0]), int(animal_cords[1])),font, font_size, animal_data['colors'][bp], 1)
                            id_flag = True
                    if not id_flag:
                        cv2.putText(frame, animal_name, (int(animal_cords[0]), int(animal_cords[1])),font, font_size, animal_data['colors'][bp], 1)



                target_timer = round((1 / self.fps) * clf_cnt, 2)
                if video_height < video_width:
                    frame = np.array(Image.fromarray(frame).rotate(90,Image.BICUBIC, expand=True))

                cv2.putText(frame, str('Timer'), (10, spacingScale), font, font_size, (0, 255, 0), 2)
                addSpacer = 2
                cv2.putText(frame, (str(self.clf_name) + ' ' + str(target_timer) + str('s')), (10, spacingScale*addSpacer), font, font_size, (0, 0, 255), 2)
                addSpacer+=1
                cv2.putText(frame, str('Ensemble prediction'), (10, spacingScale*addSpacer), font, font_size, (0, 255, 0), 2)
                addSpacer += 2
                if clf_val == 1:
                    cv2.putText(frame, self.clf_name, (10, + spacingScale * addSpacer), font, font_size, (2, 166, 249), 2)
                    addSpacer += 1

                # cv2.imshow('Window', frame)
                # key = cv2.waitKey(3000)
                # if key == 27:
                #     cv2.destroyAllWindows()

                if self.create_gantt == 'Gantt chart: final frame only (slightly faster)':
                    frame = np.concatenate((frame, gantt_img), axis=1)
                if self.create_gantt == 'Gantt chart: video':
                    gantt_img = create_gantt_img(bouts_df, self.clf_name, frm_cnt, self.fps, 'Behavior gantt chart')
                    if flip_flag:
                        gantt_img = resize_gantt(gantt_img, video_width)
                    else:
                        gantt_img = resize_gantt(gantt_img, video_height)
                    frame = np.concatenate((frame, gantt_img), axis=1)
                if self.create_gantt != 'None':
                    frame = cv2.resize(frame, (int(video_width + gantt_img.shape[1]), int(video_height)))

                writer.write(frame)
                print('Frame created: {} / {}'.format(str(frm_cnt+1), str(len(self.data_df))))
                frm_cnt += 1
                if frame is None:
                    print('Validation video saved @ ' + self.vid_output_path)
                    cap.release()
                    writer.release()
                    break

            except Exception as e:
                print(e)
                cap.release()
                writer.release()
                break
        cap.release()
        writer.release()
        print('Validation video saved @ ' + self.vid_output_path)

# inifile = r"Z:\DeepLabCut\DLC_extract\Troubleshooting\DLC_two_mice\project_folder\project_config.ini"
# featuresPath = r"Z:\DeepLabCut\DLC_extract\Troubleshooting\DLC_two_mice\project_folder\csv\features_extracted\Together_1.csv"
# modelPath = r"Z:\DeepLabCut\DLC_extract\Troubleshooting\DLC_two_mice\models\generated_models\Attack.sav"
#
# inifile = r"Z:\DeepLabCut\DLC_extract\Troubleshooting\Zebrafish\project_folder\project_config.ini"
# featuresPath = r"Z:\DeepLabCut\DLC_extract\Troubleshooting\Zebrafish\project_folder\csv\features_extracted\20200730_AB_7dpf_850nm_0002.csv"
# modelPath = r"Z:\DeepLabCut\DLC_extract\Troubleshooting\Zebrafish\models\validations\model_files\Rheotaxis_1.sav"
#
# dt = 0.4
# sb = 67
# generategantt = 'Gantt chart: video'
#
# test = ValidateModelOneVideo(ini_path=inifile,feature_file_path=featuresPath,model_path=modelPath,d_threshold=dt,shortest_bout=sb, create_gantt=generategantt)
# test.perform_clf()
# test.plug_small_bouts()
# test.save_classification_data()
# test.create_video()

# cv2.imshow('Window', frame)
# key = cv2.waitKey(3000)
# if key == 27:
#     cv2.destroyAllWindows()





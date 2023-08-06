import os
import glob
import datetime
from tkinter import filedialog
import pandas as pd
from tqdm import tqdm


def csv_to_xlsx():
    # 1. directory 선택
    root_dir_name = filedialog.askdirectory()
    
    # 2. 결과 파일 저장 경로 설정
    target_root_dir = os.getcwd()
    target_save_dir = target_root_dir + '/conv_data/'
    
    if not os.path.exists(target_save_dir):
        os.makedirs(target_save_dir)
    current_datetime = datetime.datetime.now()
    target_save_dir_datetime = target_save_dir + datetime.datetime.strftime(current_datetime, '%Y%m%d') + '/' + datetime.datetime.strftime(current_datetime, '%H%M%S') + '/'
    
    if not os.path.exists(target_save_dir_datetime):
        os.makedirs(target_save_dir_datetime)
    
    # 변환할 csv 파일 리스트업
    root_dir_name_target = root_dir_name + '/**/*.csv'
    csv_file_list = glob.glob(root_dir_name_target, recursive=True)
    pbar = tqdm(range(len(csv_file_list)), desc="Converting .csv file to .xlsx file format...", mininterval=1)
        
    # 변환 및 저장
    for file_idx in pbar:
        save_file_str = os.path.basename(csv_file_list[file_idx])
        save_dir_str = os.path.dirname(csv_file_list[file_idx])
        save_dir_str_split = save_dir_str.split('/')
        save_file_name_split = save_file_str.split('.')
        save_file_name = save_file_name_split[0] + '.xlsx'
        save_dir_concat = target_save_dir_datetime + save_dir_str_split[-1]
        if not os.path.exists(save_dir_concat):
            os.makedirs(save_dir_concat)
        save_file_name_final = save_dir_concat + '/' + save_file_name
        read_file = pd.read_csv(csv_file_list[file_idx])
        read_file.to_excel(save_file_name_final, header=True)

# def xlsx_to_csv():
#     root_dir_name = filedialog.askdirectory()
#     target_root_dir = os.getcwd()
#     target_save_dir = target_root_dir + '/conv_data/'
#     for xlsxfile in glob.glob(os.path.join('.', '*.csv')):
#         read_file = pd.read_csv('File name.csv')
#         read_file.to_excel('File name.xlsx', index=None, header=True)
        
        
if __name__ == '__main__':
    csv_to_xlsx()
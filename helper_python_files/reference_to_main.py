import os
from pathlib import Path
import pandas as pd
import numpy as np
import math
import xlwings as xw

# @brief is_empty_cell(value)
# @remarks Receives the cell value from csv and returns True if it is empty
# @param[in] - cell value
# @return - TRUE for empty cell
# @author Abdur Rahaman
def is_empty_cell(value):
    return ((isinstance(value, float) and math.isnan(float(
        value))) or value is None or value == 'NAN' or value == 'nan' or value == 'Nan' or value == '' or value == np.nan or pd.isna
            (value))

# @brief veh_sig_mapped_to_given_sensor_sig(sensor_sig,list_of_lis)
# @remarks Receives the sensor signal and list of list(contains sensor signal and all the mapped vehicle side arguments for a particular sensor msg) searching the sensor_sig in list of list if found returning list which contains veh_msg, veh_sig, index of the list in list_of_list
# @param[in] - sensor_sig, list_of_lis = [[sen_sig1, veh_msg1,veh_sig1],[sen_sig2, veh_msg2,veh_sig2], ...]
# @return - TRUE for empty cell
# @author Abdur Rahaman
def veh_sig_mapped_to_given_sensor_sig(sensor_sig, list_of_lis):
    for lst in list_of_lis:
        if sensor_sig in lst:
            lst.append(list_of_lis.index(lst))
            return lst[1:4]
    return []

# @brief find_string_in_excel(file_path, sheet_name, column_name, search_string)
# @remarks Receives the file path,sheet_name, column_name and string needs to be searched and returns the index in dataframe if found using binary search
# @param[in] - CSV file path, sheet_name, column_name, search_string
# @return - Index of the occurance of the searched string in dataframe
# @author Abdur Rahaman
def find_string_in_excel(file_path, sheet_name, column_name, search_string):
    # Load the Excel sheet into a pandas DataFrame
    dataframe = pd.read_excel(file_path, sheet_name=sheet_name, skiprows=[0])

    # Find the row index where the string is located using binary search
    left = 0
    right = len(dataframe) + 2
    while left <= right:
        mid = (left + right) // 2
        mid_value = dataframe[column_name][mid]
        mid1 = mid
        mid2 = mid
        if is_empty_cell(mid_value):
            while is_empty_cell(dataframe[column_name][mid1]) and is_empty_cell(dataframe[column_name][mid2]):
                mid1 -= 1
                mid2 += 1
            if not is_empty_cell(dataframe[column_name][mid1]):
                mid_value = dataframe[column_name][mid1]
                mid = mid1
            elif not is_empty_cell(dataframe[column_name][mid2]):
                mid_value = dataframe[column_name][mid2]
                mid = mid2
        if mid_value == search_string or (is_empty_cell(mid_value) and search_string == ''):
            return mid
        elif is_empty_cell(mid_value) or mid_value < search_string:
            left = mid + 1
        else:
            right = mid - 1

    # If the string is not found, return None
    return None


Dict = {}
# List = []
BASE_PATH = Path(__file__).resolve().parent
# p = Path(r"C:\Users\uif74893\Desktop\mapping_sheet_python_project\Mapping_sheet_C-HR_SRR320SU16.xlsm")
# reference mapping sheet path
p = Path(r"" + str(BASE_PATH) + "\mapping sheets\Mapping_sheet_C-HR_SRR320SU16.xlsm")
# reading necessary rows and cols from Excel file
df = pd.read_excel(p, sheet_name='Sheet1', skiprows=[0, 1, 2, 3, 4, 5, 7], usecols=[0, 2, 8, 10, 17, 18])
df = df.replace('', np.nan)
df = df.replace('', np.NaN)
df = df.replace('', np.NAN)
df.fillna('')
# print(df.columns)
List = []
Fixed_values = {}
Notice = {}
Signal_msg = []
for ind in df.index:
    # List = []
    if df['Message name'][ind] != 'end' and df['Message name'][ind] != 'Transmit':
        if is_empty_cell(df['Message name'][ind]):
            df['Message name'][ind] = curr
        else:
            curr = df['Message name'][ind]
            Signal_msg.append(df['Message name'][ind])
            if df['Message name'][ind] in Dict:
                List = Dict[df['Message name'][ind]]
            else:
                List = []
            # List = []
        if not is_empty_cell(df['Parameter'][ind]):
            curr_sen_sig = df['Parameter'][ind]
        if not is_empty_cell(df['Message name.1'][ind]):
            curr_veh_msg = df['Message name.1'][ind]
        if not is_empty_cell(df['Parameter.1'][ind]):
            curr_veh_sig = df['Parameter.1'][ind]
        # print(df[0][ind], df[][ind])
        if df['Parameter.1'][ind] != 'Not Found':
            if is_empty_cell(df['Parameter.1'][ind]):
                df['Parameter.1'][ind] = curr_veh_sig
            if is_empty_cell(df['Parameter'][ind]):
                df['Parameter'][ind] = curr_sen_sig
            if is_empty_cell(df['Message name.1'][ind]):
                df['Message name.1'][ind] = curr_veh_msg
            List.append([df['Parameter'][ind], df['Message name.1'][ind], df['Parameter.1'][ind]])
        else:
            Fixed_values[df['Parameter'][ind]] = df['Value'][ind]
        Notice[df['Parameter'][ind]] = df['Notice'][ind]
        if len(List) > 0:
            Dict[df['Message name'][ind]] = List
        # curr = df['Message name'][ind]
# res = Path(r"C:\Users\uif74893\Desktop\mapping_sheet_python_project\Target_main_mapping.xlsm")
# target mapping sheet path
res = Path(r"" + str(BASE_PATH) + "\mapping sheets\Target_main_mapping.xlsm")
book = xw.Book(res)
# print(Dict)
# print(Signal_msg)
Sheet1 = book.sheets[0]
Sensor = book.sheets[3]
Vehicle = book.sheets[4]
Sensor_rows = Sensor.range((3, 3)).end('down').row
Sensor_cols = 9  # no of cells containing sensor side info
Vehicle_rows = Vehicle.range((3, 3)).end('down').row
Vehicle_cols = 9  # no of cells containing vehicle side info
fix = 13  # printing after 13th row

for i in range(1, Sensor_rows):
    if Sensor.range((i, 1)).value in Signal_msg:
        current_msg = Sensor.range((i, 1)).value
        while (is_empty_cell(Sensor.range((i, 1)).value) or Sensor.range
            ((i, 1)).value == current_msg) and i <= Sensor_rows:
            for j in range(1, Sensor_cols):
                Sheet1.range((fix, j)).value = Sensor.range((i, j)).value
            if Sensor.range((i, 3)).value in Notice:
                Sheet1.range((fix, 19)).value = Notice[Sensor.range((i, 3)).value]
            if current_msg in Dict and len \
                        (veh_sig_mapped_to_given_sensor_sig(Sensor.range((i, 3)).value, Dict[current_msg])) > 0:
                veh_list = veh_sig_mapped_to_given_sensor_sig(Sensor.range((i, 3)).value, Dict[current_msg])
                k = find_string_in_excel(res, 'Vehicle', 'Message name', veh_list[0]) + 3
                Sheet1.range((fix, 9)).value = Vehicle.range((k, 1)).value
                Sheet1.range((fix, 10)).value = Vehicle.range((k, 2)).value
                while Vehicle.range((k, 3)).value != veh_list[1] and k <= Vehicle_rows:
                    k += 1
                if k > Vehicle_rows:
                    Sheet1.range((fix, 11)).value = veh_list[1]
                else:
                    for m in range(3, 9):
                        Sheet1.range((fix, m + 8)).value = Vehicle.range((k, m)).value
                Sheet1.range((fix, 17)).value = 'Mapping'
                # break

                Dict[current_msg].pop(veh_list[2])
                if len(veh_sig_mapped_to_given_sensor_sig(Sensor.range((i, 3)).value, Dict[current_msg])) > 0:
                    i -= 1
            else:
                Sheet1.range((fix, 11)).value = 'Not Found'
                Sheet1.range((fix, 17)).value = 'Fixed'
                if Sensor.range((i, 3)).value in Fixed_values:
                    Sheet1.range((fix, 18)).value = Fixed_values[Sensor.range((i, 3)).value]
                else:
                    Sheet1.range((fix, 18)).value = 0
            i += 1
            fix += 1
        Signal_msg.remove(current_msg)

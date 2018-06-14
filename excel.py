import xlrd
import xlwt


class OperationOnExcel(object):
    def __init__(self):
        pass

    def write_data_to_excel(self, data):
        # 输入的数据类型：dict
        # 输入的数据格式：{1:[1,2,3,4,5,6,7], 2:[2,3,4,5,6,7,8], ...}

        # 创建Excel对象
        table = xlwt.Workbook(encoding='utf-8', style_compression=0)
        sheet = table.add_sheet(sheetname="data", cell_overwrite_ok=True)

        # 当写入中文时候需要转成unicode字符

        keys = [x for x in data]
        keys.sort()

        for index in range(len(data)+1):
            if index == 0:
                column_name = ["Times", "First", "Second", "Third", "Fourth", "Fifth", "sixth", "Seventh"]
                for col in range(len(column_name)):
                    sheet.write(0, col, column_name[col])
            else:
                try:
                    sheet.write(index, 0, keys[index-1])  # 第几期
                    sheet.write(index, 1, data[keys[index-1]][0])     # 第一个数字
                    sheet.write(index, 2, data[keys[index-1]][1])
                    sheet.write(index, 3, data[keys[index-1]][2])
                    sheet.write(index, 4, data[keys[index-1]][3])
                    sheet.write(index, 5, data[keys[index-1]][4])
                    sheet.write(index, 6, data[keys[index-1]][5])
                    sheet.write(index, 7, data[keys[index-1]][6])

                except KeyError:
                    print("KeyError: {0}".format(index))
                    continue

        table.save(r"D:/data/prediction_cp.xls")


if __name__ == '__main__':
    a = {
        1: [1,2,3,4,5,6,7],
        2: [4,5,6,7,8,9,0],
        3: [3,4,5,6,7,8,9],
        5: [3,4,4,5,6,7,8],
        12: [1,2,3,4,5,6,7]
    }

    OperationOnExcel().write_data_to_excel(a)

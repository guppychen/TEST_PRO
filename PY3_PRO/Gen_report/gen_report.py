"""
    柱状图显示20.1版本ARF GS4227E 测试数据
"""
import csv
import matplotlib.pyplot as plt

def draw_pass(file_path):
    """
        处理csv文件,折线图显示pass_rate
    """
    with open(file_path, mode='r', encoding='utf-8') as f:
        reader = csv.reader(f)
        header_row = next(reader)
        print(','.join(header_row))
        version = []
        pass_rate = []
        for row in reader:
            print(', '.join(row))
            # 取版本的后三位为版本号
            str_version = row[0]
            ver = str_version[9:]
            version.append(ver)
            # pass rate 转换为数字
            str_rate = row[6]
            rate = float(str_rate[:-1])
            pass_rate.append(rate)
        print(version)
        print(pass_rate)
        plt.figure(figsize=(8,8))
        plt.plot(version,pass_rate)
        plt.xlabel('Version')
        plt.ylabel('Pass Rate %',rotation=0)
        plt.title('GS4227E Pass Rate Trend on R20.1.0')
        plt.ylim((0,100))
        plt.xticks(version,rotation=90,size=8)
        # 给柱装加显示数值
        for a, b in zip(version, pass_rate):
            plt.text(a, b + 0.05, '%.0f' % b+'%', ha='center', va='bottom', fontsize=7)
        plt.show()


def draw_case(file_path):
    """
        处理csv文件,柱状图显示case数量
    """
    with open(file_path, mode='r', encoding='utf-8') as f:
        reader = csv.reader(f)
        header_row = next(reader)
        print(','.join(header_row))
        version = []
        pass_number= []
        fail_number = []
        pass_rate = []
        for row in reader:
            print(', '.join(row))
            # 取版本的后三位为版本号
            str_version = row[0]
            ver = str_version[9:]
            version.append(ver)
            # pass数量转换为数字
            str_pass = row[2]
            pass_int = int(str_pass)
            pass_number.append(pass_int)
            # fail数量转换为数字
            str_fail = row[3]
            fail_int = int(str_fail)
            fail_number.append(fail_int)
            # pass rate 转换为数字
            str_rate = row[6]
            rate = float(str_rate[:-1])
            pass_rate.append(rate)
        print('version is: {}'.format(version))
        print('pass_number is: {}'.format(pass_number))
        print('fail_number is: {}'.format(fail_number))
        print('pass_rate is: {}'.format(pass_rate))
        plt.figure(figsize=(10,10))
        plt.bar(version, pass_number, color='g')
        plt.bar(version, fail_number, color='orange', bottom=pass_number)
        plt.xlabel('Version')
        plt.ylabel('Pass Rate %',rotation=0)
        plt.title('GS4227E Pass Rate Trend on R20.1.0')
        plt.ylim((0,180))
        plt.xticks(version,rotation=90,size=8)
        # 给柱装加显示数值
        for a, b ,c in zip(version, pass_rate, pass_number):
            plt.text(a, c + 0.05, '%.2f' % b + '%', ha='center', va='bottom', fontsize=7)
        plt.legend(['pass','fail'],bbox_to_anchor=(1.01, 1), loc='best', borderaxespad=0)
        plt.show()


def main():
    """
        main
    """
    file_path = 'test4227.csv'
    # draw_pass(file_path)
    draw_case(file_path)

if __name__ == '__main__':
    main()
"""
    柱状图显示20.1版本ARF GS4227E 测试数据
    v2:增加pass rate折线图，双Y轴显示
"""
import csv
import matplotlib.pyplot as plt


def draw_case(file_path):
    """
        处理csv文件,柱状图显示case数量，折线图显示pass rate，双Y轴显示
    """
    with open(file_path, mode='r', encoding='utf-8') as f:
        reader = csv.reader(f)
        # 读取第一行表头，不作为画图数据
        header_row = next(reader)
        print(','.join(header_row))

        version = []
        pass_number= []
        fail_number = []
        pass_rate = []
        x = []
        for row in reader:
            print(', '.join(row))
            # 取版本的后三位为版本号
            str_version = row[0]
            ver = str_version[9:]
            version.append(ver)
            # 版本号 + 日期作为X轴
            str_x = ver + '\n' + row[1]
            x.append(str_x)

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
        print('X轴: {}'.format(x))
        fig = plt.figure(figsize=(12,9))
        ax = fig.add_subplot()
        ax.bar(x, pass_number, color='SteelBlue')
        ax.bar(x, fail_number, color='Coral', bottom=pass_number)
        ax.set_xlabel('Version')
        ax.set_ylabel('Case Number')
        ax.set_title('GS4227E Pass Rate Trend on R20.1.0')
        ax.set_ylim((0,175))
        plt.xticks(x,rotation=90,size=8)
        # 给柱装加显示数值
        for a, b ,c in zip(x, pass_rate, pass_number):
            ax.text(a, c + 0.05, '%.2f' % b + '%', ha='center', va='bottom', fontsize=7)
        ax.legend(['pass','fail'],bbox_to_anchor=(1.13, 1), loc='best', borderaxespad=0)
        # 第二Y轴显示
        ax2 = ax.twinx()
        ax2.plot(x, pass_rate, color='LimeGreen',marker='o')
        ax2.set_ylabel('Pass Rate%')
        ax2.set_ylim((0, 103))

        plt.show()


def main():
    """
        main
    """
    file_path = 'test4227.csv'
    draw_case(file_path)

if __name__ == '__main__':
    main()
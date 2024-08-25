import pandas as pd
import matplotlib.pyplot as plt


def open_file(path: str) -> pd.DataFrame:
    file = pd.read_csv(path, sep=' ' * 14,
                       names=['Частота, Гц', 'Re, Ом', 'Im, Ом'], engine='python')  # encoding = 'windows-1251'
    return file


def find_f(file: pd.DataFrame) -> int:
    if file['Im, Ом'][0] < 0:
        f = file['Частота, Гц'][0]
        return round(f)
    for i in range(len(file)):
        if file['Im, Ом'][i] > 0:
            j = i
        else:
            break
    a = file['Im, Ом'][j]
    b = file['Im, Ом'][j + 1]
    c = file['Частота, Гц'][j]
    d = file['Частота, Гц'][j + 1]
    f = c - a * (c - d) / (a - b)
    return round(f)


def imp_plot(file: pd.DataFrame):
    file_plot = file.copy()
    file_plot['Im, Ом'] = file_plot['Im, Ом'] * (-1)
    x = file_plot['Re, Ом']
    y = file_plot['Im, Ом']
    # file_plot.plot()
    graph = plt.plot(x, y, label='Годограф импеданса', color='black', marker='o', linestyle='')
    plt.title('Impedance')
    plt.ylabel('-Im, Ом')
    plt.xlabel('Re, Ом')
    plt.ylim(ymin=0)
    return graph


if __name__ == '__main__':
    path = r'C:\Users\krant\PycharmProjects\Impedance\785С_30mV_5.z'
    file = open_file(path)
    print(file)
    print(find_f(file))
    imp_plot(file)
    plt.show()

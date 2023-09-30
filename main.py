from downwin import DownWin

def main(url, filename):
    dw = DownWin()
    dw.active = True
    while dw.active:
        current_time = dw.current_time()
        dw.check_current_time(url=url, current_time=current_time, filename=filename)


if __name__ == "__main__":
    url = input("Enter the Url: ")
    filename = input("Enter filename: ")
    main(url, filename)


from pynput import keyboard
from pynput.keyboard import Key

selected: list[any] = []
data: list[any] = []
selected_number: int = 0
multiple_select: bool = False
delete_select: bool = False


class inputList():
    def print_data():
        try:
            print("\r" + str(data[selected_number]) + ' ' * 15, end="")
        except IndexError:
            exit(0)

    def _arrowInput(key: any):
        global selected, selected_number

        if key == Key.right and selected_number != len(data)-1:
            selected_number += 1
        elif key == Key.left and selected_number != 0:
            selected_number -= 1
        elif key == Key.enter:
            selected.append(data[selected_number])

            if delete_select:
                data.remove(data[selected_number])
                selected_number = 0  # to prevent IndexError: list index out of range

            print("\n" + str(selected))  # print selected item

            if multiple_select == False:
                return False  # stop listening for keys
        elif key == Key.esc and multiple_select:
            return False

        inputList.print_data()

    def get(content: list[str], multiple: bool, deleteSelected: bool) -> list[any]:
        global selected, selected_number, data, multiple_select, delete_select
        self = inputList

        multiple_select = multiple
        delete_select = deleteSelected

        for x in content:
            data.append(x + " ")
        print(str(data))

        self.print_data()

        # start listening for keys
        with keyboard.Listener(on_release=self._arrowInput) as listener:
            listener.join()

        return selected


if __name__ == "__main__":
    inputList.get(["a", "b", "c"], True, True)

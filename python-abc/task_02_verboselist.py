from typing import SupportsIndex


class VerboseList(list):
       
    def append(self, item):
        super().append(item)
        print(f"Added [{item}] to the list.")

    def extend(self, items):
        super().extend(items)
        print(f"Extended the list with [{len(items)}] items.")

    def remove(self, value):
        super().remove(value)
        print(f"Removed [{value}] from the list.")

    def pop(self, index: SupportsIndex = -1):
        item = super().pop(index)
        print(f"Popped [{item}] from the list.")
        return item

from enum import  Enum


class Operations(Enum):
    Expo = "exp"
    log = "log"
    log10 = "log10"
    sqrt = "sqrt"
    ln = "ln"

    def __str__(self):
        return self.value






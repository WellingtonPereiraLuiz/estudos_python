import re

teste = r"^(?=.*[A-Z])(?=.*\d)(?=.*[@#$*]).{6,12}$"

print(bool(re.match(teste, "3@FORTE2!")))
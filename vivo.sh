#!/bin/bash -e
# File: count-message.sh
# Date: Sun Apr 12 21:01:01 2015 +0900
# Author: Kangjing Huang <huangkangjing@gmail.com>

# Tao excel
./dump-msg2.py decrypted.db output resource avatar.index "💯ASM Check In"
./dump-msg2.py decrypted.db output resource avatar.index "💯Office Check In"
./dump-msg2.py decrypted.db output resource avatar.index "💯PC Check In"
./dump-msg2.py decrypted.db output resource avatar.index "💯Sales Check In"

# Tao html
# ./dump-html.py --db decrypted.db --avt avatar.index  --res resource --output "💯ASM Check In.html" "💯ASM Check In"
# ./dump-html.py --db decrypted.db --avt avatar.index  --res resource --output "💯Office Check In.html" "💯Office Check In"
# ./dump-html.py --db decrypted.db --avt avatar.index  --res resource --output "💯PC Check In.html" "💯PC Check In"
# ./dump-html.py --db decrypted.db --avt avatar.index  --res resource --output "💯Sales Check In.html" "💯Sales Check In"
